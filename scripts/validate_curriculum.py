"""11. sınıf fizik müfredat verisini doğrular (bağımlılık: yalnız pypdf).

Kontroller:
  - JSON geçerliliği, zorunlu alanlar, izinli değerler (şemalarla aynı kurallar)
  - yinelenen ID / resmî kod, kod dizisinin kesintisizliği
  - kırık referanslar (ünite, içerik başlığı, kaynak), sahipsiz öğrenme çıktısı
  - resmî PDF ile yeniden karşılaştırma: ünite sayısı, saatler, çıktı metinleri, süreç bileşenleri
  - müfredat sürümü tutarlılığı, master-map kapsamı, kaynak dosya hash'leri
  - kritik alanlarda LOW / UNVERIFIED güven raporu

Kullanım: python3 scripts/validate_curriculum.py   (hata varsa çıkış kodu 1)
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_curriculum as build  # noqa: E402

KB = build.KB
CONF = {"HIGH", "MEDIUM", "LOW", "UNVERIFIED"}
REQUIRED_LO = ["id", "official_code", "official_text", "subject", "grade", "curriculum_version", "unit_id", "unit",
               "subtopic", "process_components", "skills", "sources", "confidence", "created_at", "updated_at"]
REQUIRED_SRC = ["id", "title", "organization", "tier", "source_type", "url", "access_date", "reliability", "status", "notes"]

errors, warnings, passed = [], [], []


def check(cond, ok_msg, err_msg, level="error"):
    if cond:
        if ok_msg:
            passed.append(ok_msg)
    else:
        (errors if level == "error" else warnings).append(err_msg)
    return cond


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # geçersiz JSON
        errors.append(f"Geçersiz JSON: {path} ({e})")
        return None


def main():
    cur = load(KB / "curriculum" / "curriculum.json")
    lo_doc = load(KB / "learning-outcomes" / "learning-outcomes.json")
    src_doc = load(KB / "sources" / "sources.json")
    if not (cur and lo_doc and src_doc):
        return report()
    los, units, sources = lo_doc["learning_outcomes"], cur["units"], src_doc["sources"]
    passed.append("3 JSON dosyası geçerli")

    # --- kaynaklar
    src_ids = [s["id"] for s in sources]
    check(len(src_ids) == len(set(src_ids)), "Kaynak ID'leri benzersiz", "Yinelenen kaynak ID")
    for s in sources:
        miss = [k for k in REQUIRED_SRC if k not in s]
        check(not miss, None, f"Kaynak {s.get('id')} eksik alan: {miss}")
        check(s.get("reliability") in CONF, None, f"Kaynak {s['id']} geçersiz reliability")
        if s.get("sha256"):
            p = build.ROOT / s["local_path"]
            ok = p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == s["sha256"]
            check(ok, f"Hash doğru: {p.name}", f"Kaynak dosyası değişmiş veya yok: {s['local_path']}")
        if s["tier"] == 4 and s["status"].startswith("used"):
            errors.append(f"Tier 4 kaynak kritik veri için kullanılmış: {s['id']}")

    # --- öğrenme çıktıları: yapı
    ids = [o["id"] for o in los]
    codes = [o["official_code"] for o in los]
    check(len(ids) == len(set(ids)), "Öğrenme çıktısı ID'leri benzersiz", "Yinelenen öğrenme çıktısı ID")
    check(len(codes) == len(set(codes)), "Resmî kodlar benzersiz", "Yinelenen resmî kod")
    check(lo_doc["count"] == len(los), "count alanı doğru", "count alanı çıktı sayısıyla uyuşmuyor")
    versions = {o["curriculum_version"] for o in los} | {cur["curriculum_version"], lo_doc["curriculum_version"]}
    check(len(versions) == 1, f"Müfredat sürümü tutarlı ({versions.pop()})", f"Tutarsız müfredat sürümü: {versions}")
    src_set = set(src_ids)
    unit_ids = {u["id"] for u in units}
    topic_ids = {t["id"] for u in units for t in u["topics"]}
    for o in los:
        miss = [k for k in REQUIRED_LO if k not in o]
        check(not miss, None, f"{o.get('id')} eksik alan: {miss}")
        check(re.fullmatch(r"phys11-lo-\d{3}", o["id"]), None, f"ID biçimi hatalı: {o['id']}")
        check(re.fullmatch(r"FİZ\.11\.[1-9]\.\d{1,2}", o["official_code"]), None, f"Kod biçimi hatalı: {o['official_code']}")
        check(o["unit_id"] in unit_ids, None, f"{o['id']}: kırık ünite referansı")
        check(o["subtopic"]["topic_id"] in topic_ids, None, f"{o['id']}: kırık içerik başlığı referansı")
        check(len(o["process_components"]) >= 1, None, f"{o['id']}: süreç bileşeni yok")
        for s in o["sources"]:
            check(s["source_id"] in src_set, None, f"{o['id']}: kırık kaynak referansı {s['source_id']}")
        for field in ("confidence",):
            check(o[field] in CONF, None, f"{o['id']}: geçersiz güven değeri")
        if o["subtopic"]["confidence"] in ("LOW", "UNVERIFIED") or o["confidence"] in ("LOW", "UNVERIFIED"):
            warnings.append(f"{o['official_code']}: kritik alanda düşük güven")
        if o["subtopic"]["confidence"] == "MEDIUM":
            warnings.append(f"{o['official_code']}: içerik başlığı eşlemesi MEDIUM ({o['subtopic']['official_title']})")
    passed.append("Zorunlu alanlar, biçimler ve referanslar kontrol edildi")

    # kod dizisi kesintisiz mi (ünite başına 1..n)
    for u in units:
        nums = sorted(int(c.split(".")[-1]) for c in codes if c.startswith(f"FİZ.11.{u['unit_no']}."))
        check(nums == list(range(1, len(nums) + 1)), f"Ünite {u['unit_no']} kod dizisi kesintisiz (1–{len(nums)})",
              f"Ünite {u['unit_no']} kod dizisinde boşluk: {nums}")
    # sahipsiz çıktı
    listed = [i for u in units for i in u["learning_outcome_ids"]]
    check(sorted(listed) == sorted(ids), "Sahipsiz öğrenme çıktısı yok", "Ünitelere bağlanmamış veya fazla çıktı var")
    # sahipsiz içerik başlığı
    used_topics = {o["subtopic"]["topic_id"] for o in los}
    check(used_topics == topic_ids, "Her içerik başlığına en az bir çıktı bağlı",
          f"Çıktısı olmayan içerik başlığı: {topic_ids - used_topics}", level="warning")

    # --- resmî PDF ile yeniden karşılaştırma
    sec, full = build.pdf_grade11_text()
    pdf_units = build.parse_pdf_units(sec)
    check(len(pdf_units) == len(units) == 3, "Ünite sayısı PDF ile aynı (3)", "Ünite sayısı PDF ile uyuşmuyor")
    table = re.search(r"FİZİK DERSİ 11\. SINIF.*?TOPLAM (\d+) (\d+)", re.sub(r"\s+", " ", full))
    check(table and int(table.group(1)) == len(los), f"PDF tablosu: {table.group(1)} öğrenme çıktısı = veri",
          "PDF tablosundaki çıktı sayısı veriyle uyuşmuyor")
    check(table and int(table.group(2)) == cur["total_hours"], f"PDF tablosu: {table.group(2)} saat = veri",
          "PDF tablosundaki toplam saat veriyle uyuşmuyor")
    by_code = {o["official_code"]: o for o in los}
    mism = 0
    for no, pu in pdf_units.items():
        u = next(x for x in units if x["unit_no"] == no)
        check(pu["hours"] == u["hours"], None, f"Ünite {no} saati PDF ile uyuşmuyor")
        check(pu["key_concepts"] == u["key_concepts_official"], None, f"Ünite {no} anahtar kavramları PDF ile uyuşmuyor")
        check([t["official_title"] for t in u["topics"]] == pu["topics"], None, f"Ünite {no} içerik başlıkları PDF ile uyuşmuyor")
        for po in pu["outcomes"]:
            o = by_code.get(po["code"])
            if not o:
                errors.append(f"PDF'teki {po['code']} veride yok"); mism += 1; continue
            if o["official_text"] != po["text"]:
                errors.append(f"{po['code']} resmî metni PDF'ten farklı"); mism += 1
            if [c["official_text"] for c in o["process_components"]] != [c["official_text"] for c in po["components"]]:
                errors.append(f"{po['code']} süreç bileşenleri PDF'ten farklı"); mism += 1
    check(mism == 0, f"{len(los)} çıktı metni ve {sum(len(o['process_components']) for o in los)} süreç bileşeni PDF ile birebir aynı",
          f"PDF ile {mism} uyuşmazlık")

    # --- master map kapsamı
    mm = (KB / "curriculum" / "master-map.md").read_text(encoding="utf-8")
    missing = [c for c in codes if f"**{c}**" not in mm]
    check(not missing, "master-map.md tüm resmî kodları içeriyor", f"master-map.md'de eksik kod: {missing}")

    # --- bekleyen alanlar (bilgi amaçlı)
    pending = sorted({f for o in los for f in o.get("pending_fields", [])})
    warnings.append(f"Sonraki adımlarda doldurulacak alanlar (tüm çıktılarda boş): {', '.join(pending)}")
    for s in sources:
        if s["status"] in ("downloaded_not_analyzed", "download_failed", "superseded_not_compared"):
            warnings.append(f"Kaynak işlenmedi: {s['id']} ({s['status']})")
    return report()


def report():
    print(f"GEÇTİ ({len(passed)}):")
    for p in passed:
        print("  ✓", p)
    print(f"UYARI ({len(warnings)}):")
    for w in warnings:
        print("  !", w)
    print(f"HATA ({len(errors)}):")
    for e in errors:
        print("  ✗", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
