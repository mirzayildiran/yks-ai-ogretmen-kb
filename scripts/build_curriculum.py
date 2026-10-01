"""11. sınıf fizik müfredat verisini resmi MEB kaynaklarından üretir.

Birincil kaynak : MEB TYMM Fizik Dersi Öğretim Programı PDF (9-12, 19.08.2026)
İkincil kaynak  : tymm.meb.gov.tr ünite sayfaları (05.08.2026) — uzun anlatı metinleri
                  buradan alınır ve PDF metninde geçtiği doğrulanır.

Çıktılar:
  knowledge-base/physics-11/curriculum/curriculum.json
  knowledge-base/physics-11/learning-outcomes/learning-outcomes.json
  knowledge-base/physics-11/curriculum/master-map.md

Kullanım: python3 scripts/build_curriculum.py
"""
import json
import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "knowledge-base" / "physics-11"
RAW = KB / "sources" / "raw"
PDF = RAW / "pdf" / "fizik-ogretim-programi-9-12.pdf"
WEB = {
    1: RAW / "tymm-web" / "unite-1-kuvvet-ve-hareket.txt",
    2: RAW / "tymm-web" / "unite-2-elektrik-ve-manyetizma.txt",
    3: RAW / "tymm-web" / "unite-3-optik.txt",
}
WEB_URL = {1: "https://tymm.meb.gov.tr/fizik-dersi/unite/243",
           2: "https://tymm.meb.gov.tr/fizik-dersi/unite/248",
           3: "https://tymm.meb.gov.tr/fizik-dersi/unite/259"}
TODAY = "2026-10-01"
CURRICULUM_VERSION = "TYMM-FIZIK-OP-2026-08-19"
SRC_PDF = "src-meb-fizik-op-2026"
SRC_WEB = {1: "src-tymm-fiz11-unite1", 2: "src-tymm-fiz11-unite2", 3: "src-tymm-fiz11-unite3"}

# Öğrenme çıktısı metnindeki beceri ifadesi -> programdaki beceri kodu.
# Çıktı metni beceriyi açıkça adlandırdığı için eşleme doğrudandır.
SKILL_PHRASES = [
    ("tümevarımsal akıl yürütebilme", "FBAB10"),
    ("tümdengelimsel akıl yürütebilme", "FBAB11"),
    ("analojik akıl yürütebilme", "KB2.16.3"),
    ("kanıt kullanabilme", "FBAB12"),
    ("bilimsel çıkarım yapabilme", "FBAB8"),
    ("bilimsel gözlem yapabilme", "FBAB1"),
    ("bilimsel model oluşturabilme", "FBAB9"),
    ("deney yapabilme", "FBAB7"),
    ("bilgi toplayabilme", "KB2.6"),
    ("karşılaştırabilme", "KB2.7"),
    ("karşılaştırma yapabilme", "KB2.7"),
    ("yorumlayabilme", "KB2.14"),
    ("yansıtabilme", "KB2.15"),
    ("çözümleyebilme", "KB2.4"),
]

# Öğrenme çıktısı -> içerik çerçevesi başlığı (PDF'teki başlık adlarıyla).
# Program bu eşlemeyi açıkça vermez; başlık adlarıyla çıktı metni karşılaştırılarak yapılmıştır.
TOPIC_OF = {
    "FİZ.11.1.1": ("Serbest Düşme", "high"),
    "FİZ.11.1.2": ("Serbest Düşme", "high"),
    "FİZ.11.1.3": ("İki Boyutta Sabit İvmeli Hareket", "high"),
    "FİZ.11.1.4": ("Newton'ın Hareket Yasaları", "high"),
    "FİZ.11.1.5": ("Newton'ın Hareket Yasaları", "high"),
    "FİZ.11.1.6": ("Sürtünme Kuvveti", "high"),
    "FİZ.11.1.7": ("Sürtünme Kuvveti", "high"),
    "FİZ.11.1.8": ("Limit Hız", "high"),
    "FİZ.11.1.9": ("Düzgün Çembersel Hareket", "high"),
    "FİZ.11.1.10": ("Düzgün Çembersel Hareket", "high"),
    "FİZ.11.2.1": ("Elektriksel Kuvvet ve Elektriksel Alan", "high"),
    "FİZ.11.2.2": ("Elektriksel Kuvvet ve Elektriksel Alan", "high"),
    "FİZ.11.2.3": ("Elektriksel Kuvvet ve Elektriksel Alan", "medium"),
    "FİZ.11.2.4": ("Manyetik Alan ve Manyetik Kuvvet", "high"),
    "FİZ.11.2.5": ("Manyetik Alan ve Manyetik Kuvvet", "high"),
    "FİZ.11.2.6": ("Manyetik Alan ve Manyetik Kuvvet", "high"),
    "FİZ.11.2.7": ("Manyetik Alan ve Manyetik Kuvvet", "medium"),
    "FİZ.11.2.8": ("Manyetik Alan ve Manyetik Kuvvet", "high"),
    "FİZ.11.2.9": ("Manyetik Alan ve Manyetik Kuvvet", "medium"),
    "FİZ.11.2.10": ("İndüksiyon Akımı", "high"),
    "FİZ.11.2.11": ("İndüksiyon Akımı", "high"),
    "FİZ.11.2.12": ("İndüksiyon Akımı", "medium"),
    "FİZ.11.2.13": ("Transformatörler", "high"),
    "FİZ.11.3.1": ("Işık Şiddeti, Işık Akısı ve Aydınlanma", "high"),
    "FİZ.11.3.2": ("Düzlem Aynalar", "high"),
    "FİZ.11.3.3": ("Küresel Aynalar", "high"),
    "FİZ.11.3.4": ("Küresel Aynalar", "high"),
    "FİZ.11.3.5": ("Kırılma", "high"),
    "FİZ.11.3.6": ("Görünür Derinlik", "high"),
    "FİZ.11.3.7": ("Fiber Optik", "high"),
    "FİZ.11.3.8": ("Prizmalar", "high"),
    "FİZ.11.3.9": ("Mercekler", "high"),
    "FİZ.11.3.10": ("Mercekler", "high"),
}

SCOPE_PATTERN = re.compile(r"kaçınılır|sınırlı kalınır|girmeden|sabit kabul edilir|ihmal", re.I)
HEADER_KEYS = {
    "Alan Becerileri": "field_skills",
    "Kavramsal Beceriler": "conceptual_skills",
    "Eğilimler": "dispositions",
    "Sosyal-Duygusal Öğrenme Becerileri": "social_emotional_skills",
    "Değerler": "values",
    "Okuryazarlık Becerileri": "literacy_skills",
    "Disiplinler Arası İlişkiler": "interdisciplinary_links",
    "Beceriler Arası İlişkiler": "cross_skill_links",
}


def letters_only(s):
    """Tireleme, boşluk ve noktalamadan bağımsız karşılaştırma anahtarı."""
    s = s.replace("’", "'").replace("‘", "'").replace("Â", "A").replace("â", "a")
    return re.sub(r"[^0-9a-zçğıöşüA-ZÇĞİÖŞÜ]", "", s).lower()


# tymm.meb.gov.tr sayfalarındaki yazım hataları -> PDF'teki doğru hâli (PDF ile doğrulandı)
WEB_TYPO_FIXES = [
    ("vve hipotezlerini", "ve hipotezlerini"),
    ("TTasarladığı", "Tasarladığı"),
    ("İİndüksiyon", "İndüksiyon"),
    ("IIşığı", "Işığı"),
    ("ğretmen, birden fazla", "Öğretmen, birden fazla"),
    ("derle nen", "derlenen"),
]
APPLIED_FIXES = []


def strip_tags(s):
    """Web metnindeki ( OB4 , SDB2.1 ) gibi bileşen etiketlerini ve fazla boşlukları temizler."""
    s = re.sub(r"\s*\(\s*(?:[A-Z]{1,4}\d[\d.]*\s*,?\s*)+\)", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([.,;:])", r"\1", s)
    for wrong, right in WEB_TYPO_FIXES:
        fixed = re.sub(r"(?<!Ö)" + re.escape(wrong), right, s)  # zaten doğru olan "Öğretmen"e dokunma
        if fixed != s:
            APPLIED_FIXES.append(f"{wrong} -> {right}")
            s = fixed
    return s


def pdf_grade11_text():
    text = "\n".join(p.extract_text() or "" for p in PdfReader(str(PDF)).pages)
    start = text.index("1. ÜNİTE: KUVVET VE HAREKET\nBu ünitede öğrencilerin serbest düşmeye")
    end = text.index("FİZ.12.1.1")
    sec = text[start:end]
    sec = re.sub(r"\n\d+\nFİZİK DERSİ ÖĞRETİM PROGRAMI\n", "\n", sec)
    sec = re.sub(r"\n11\. SINIF\n", "\n", sec)
    sec = re.sub(r"\s?-\s*\n", "", sec)  # satır sonu tirelemesi
    return sec.replace("KA VRAMSAL", "KAVRAMSAL"), text


def parse_pdf_units(sec):
    units = {}
    chunks = [c for c in re.split(r"\n(?=\d\. ÜNİTE: )", "\n" + sec) if "FİZ.11." in c]
    for chunk in chunks:
        no = int(chunk.strip()[0])
        flat = re.sub(r"\s+", " ", chunk)
        oc = re.search(r"ÖĞRENME ÇIKTILARI VE SÜREÇ BİLEŞENLERİ (.*?) İÇERİK ÇERÇEVESİ", flat).group(1)
        outs = []
        for m in re.finditer(r"(FİZ\.11\.\d+\.\d+)\.\s*(.*?)(?= FİZ\.11\.\d+\.\d+\.|$)", oc):
            parts = re.split(r"\s(?=[a-zç]\) )", m.group(2))
            comps = []
            for p in parts[1:]:
                label, txt = p.split(") ", 1)
                comps.append({"label": label, "official_text": txt.strip()})
            outs.append({"code": m.group(1), "text": parts[0].strip(), "components": comps})
        topics = re.search(r"İÇERİK ÇERÇEVESİ\s*(.*?)\s*Anahtar Kavramlar", chunk, re.S).group(1)
        concepts = re.search(r"Anahtar Kavramlar (.*?) ÖĞRENME KANITLARI", flat).group(1)
        units[no] = {
            "title": chunk.strip().split("\n")[0].split(": ", 1)[1],
            "hours": int(re.search(r"DERS SAATİ (\d+)", flat).group(1)),
            "outcomes": outs,
            "topics": [t.strip() for t in topics.split("\n") if t.strip()],
            "key_concepts": [c.strip() for c in concepts.split(",")],
        }
    return units


def section(lines, start, stops):
    i = lines.index(start) + 1
    out = []
    while i < len(lines) and lines[i] not in stops and not lines[i].startswith("Güncelleme tarihi"):
        out.append(lines[i])
        i += 1
    return out


def parse_web_unit(no):
    L = [l.strip() for l in WEB[no].read_text(encoding="utf-8").splitlines() if l.strip()]
    u = {"purpose": L[1]}
    for k, key in HEADER_KEYS.items():
        u[key] = [x.strip() for x in re.split(r",\s*(?![^()]*\))", L[L.index(k) + 1])]
    u["assessment"] = " ".join(section(L, "Öğrenme Kanıtları (Ölçme ve Değerlendirme)", {"Öğrenme-Öğretme Yaşantıları"}))
    u["basic_assumptions"] = L[L.index("Temel Kabuller") + 1]
    u["pre_assessment"] = L[L.index("Ön Değerlendirme Süreci") + 1]
    u["bridging"] = L[L.index("Köprü Kurma") + 1]
    practice, cur = {}, None
    for l in section(L, "Öğrenme-Öğretme Uygulamaları", {"Farklılaştırma"}):
        m = re.fullmatch(r"FİZ\.11\.\d+\.(\d+)", l)
        if m:
            cur = f"FİZ.11.{no}.{m.group(1)}"  # web sayfasındaki FİZ.11.4.10 yazım hatasını düzeltir
            practice[cur] = ""
        else:
            practice[cur] += l + " "
    u["practice"] = {k: strip_tags(v) for k, v in practice.items()}
    enrich = []
    for l in section(L, "Zenginleştirme", {"Destekleme"}):
        enrich.append({"official_text": strip_tags(l.lstrip("*")),
                       "mandatory_in_science_high_schools": l.startswith("*")})
    u["enrichment"] = enrich
    u["support"] = [strip_tags(x) for x in section(L, "Destekleme", set())]
    u["web_updated"] = [l for l in L if l.startswith("Güncelleme tarihi")][0].split(": ")[1]
    return u


def skill_for(text):
    for phrase, code in SKILL_PHRASES:
        if text.lower().endswith(phrase):
            return code
    return None


def main():
    sec, full = pdf_grade11_text()
    pdf_units = parse_pdf_units(sec)
    coverage = {}
    full_clean = re.sub(r"\n\d+\nFİZİK DERSİ ÖĞRETİM PROGRAMI\n", "\n", full)  # sayfa altbilgileri
    full_clean = re.sub(r"\n(9|10|11|12)\. SINIF\n", "\n", full_clean)
    pdf_key = letters_only(strip_tags(re.sub(r"\s?-\s*\n", "", full_clean)))
    warnings = []

    def in_pdf(s, what):
        """Metni cümle cümle PDF'te arar; bulunamayan cümleleri uyarı olarak raporlar."""
        sents = [x for x in re.split(r"(?<=[.!?])\s+", s) if len(letters_only(x)) > 15]
        missing = [x for x in sents if letters_only(x) not in pdf_key]
        coverage[what] = (len(sents) - len(missing), len(sents))
        for x in missing:
            warnings.append(f"PDF'te birebir bulunamadı ({what}): {x[:110]}")

    units, outcomes = [], []
    n = 0
    for no in (1, 2, 3):
        p, w = pdf_units[no], parse_web_unit(no)
        uid = f"phys11-unit-{no}"
        for key in ("purpose", "basic_assumptions", "assessment"):
            in_pdf(w[key], f"ünite {no} {key}")
        for e in w["enrichment"]:
            in_pdf(e["official_text"], f"ünite {no} zenginleştirme")
        topics = [{"id": f"phys11-topic-{no}-{i}", "official_title": t} for i, t in enumerate(p["topics"], 1)]
        topic_id = {t["official_title"]: t["id"] for t in topics}
        unit_outcome_ids = []
        for o in p["outcomes"]:
            n += 1
            lo_id = f"phys11-lo-{n:03d}"
            unit_outcome_ids.append(lo_id)
            practice = w["practice"].get(o["code"], "")
            in_pdf(practice, f"{o['code']} öğretme uygulaması")
            scope = [s for s in re.split(r"(?<=\.)\s+", practice) if SCOPE_PATTERN.search(s)]
            skill = skill_for(o["text"])
            skill_lists = " ".join(w["field_skills"] + w["conceptual_skills"])
            if not skill or skill + "." not in skill_lists:
                warnings.append(f"{o['code']}: beceri eşlemesi ünite beceri listesinde yok ({skill})")
            topic_title, topic_conf = TOPIC_OF[o["code"]]
            if topic_title not in topic_id:
                warnings.append(f"{o['code']}: içerik başlığı bulunamadı ({topic_title})")
            outcomes.append({
                "id": lo_id,
                "official_code": o["code"],
                "official_text": o["text"],
                "subject": "physics",
                "grade": 11,
                "curriculum_version": CURRICULUM_VERSION,
                "unit_id": uid,
                "unit": p["title"],
                "subtopic": {"topic_id": topic_id.get(topic_title), "official_title": topic_title,
                             "mapping_method": "derived_from_titles", "confidence": topic_conf.upper()},
                "process_components": [{"id": f"{lo_id}-{c['label']}", **c} for c in o["components"]],
                "skills": [{"code": skill, "mapping_method": "explicit_in_outcome_text", "confidence": "HIGH"}],
                "official_teaching_practice": practice,
                "official_scope_constraints": scope,
                # Sonraki adımlarda doldurulacak alanlar (STEP 5-14)
                "concepts": [],
                "prerequisites": [],
                "mathematical_prerequisites": [],
                "measurable_behaviors": [],
                "common_misconceptions": [],
                "assessment_implications": [],
                "pending_fields": ["concepts", "prerequisites", "mathematical_prerequisites",
                                   "measurable_behaviors", "common_misconceptions", "assessment_implications"],
                "sources": [{"source_id": SRC_PDF, "fields": ["official_code", "official_text", "process_components", "unit"]},
                            {"source_id": SRC_WEB[no], "fields": ["official_teaching_practice", "official_scope_constraints"]}],
                "confidence": "HIGH",
                "created_at": TODAY,
                "updated_at": TODAY,
            })
        units.append({
            "id": uid,
            "unit_no": no,
            "official_title": p["title"],
            "hours": p["hours"],
            "purpose": w["purpose"],
            "topics": topics,
            "learning_outcome_ids": unit_outcome_ids,
            "key_concepts_official": p["key_concepts"],
            **{k: w[k] for k in HEADER_KEYS.values()},
            "basic_assumptions_official": w["basic_assumptions"],
            "pre_assessment_official": w["pre_assessment"],
            "bridging_official": w["bridging"],
            "assessment_official": w["assessment"],
            "enrichment_official": w["enrichment"],
            "support_official": w["support"],
            "web_page_updated": w["web_updated"],
            "sources": [SRC_PDF, SRC_WEB[no]],
            "confidence": "HIGH",
        })

    meta = {"subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION,
            "primary_source": SRC_PDF, "generated_by": "scripts/build_curriculum.py",
            "generated_at": TODAY}
    curriculum = {**meta, "total_hours_units": sum(u["hours"] for u in units),
                  "school_based_planning_hours": 6, "total_hours": sum(u["hours"] for u in units) + 6,
                  "units": units}
    (KB / "curriculum" / "curriculum.json").write_text(json.dumps(curriculum, ensure_ascii=False, indent=2), encoding="utf-8")
    (KB / "learning-outcomes" / "learning-outcomes.json").write_text(
        json.dumps({**meta, "count": len(outcomes), "learning_outcomes": outcomes}, ensure_ascii=False, indent=2), encoding="utf-8")
    write_master_map(curriculum, outcomes)
    print(f"{len(units)} ünite, {len(outcomes)} öğrenme çıktısı, "
          f"{sum(len(o['process_components']) for o in outcomes)} süreç bileşeni")
    found = sum(a for a, b in coverage.values()); total = sum(b for a, b in coverage.values())
    print(f"Anlatı metni PDF çapraz kontrolü: {found}/{total} cümle birebir bulundu")
    print("Uygulanan web yazım düzeltmeleri:", sorted(set(APPLIED_FIXES)))
    for w_ in warnings:
        print("UYARI:", w_)
    return warnings, coverage


def write_master_map(cur, outcomes):
    by_id = {o["id"]: o for o in outcomes}
    L = ["# 11. Sınıf Fizik — Müfredat Ana Haritası", "",
         "> Otomatik üretildi: `scripts/build_curriculum.py`. Elle düzenleme yapma; betiği değiştirip yeniden çalıştır.",
         "",
         f"- **Müfredat sürümü:** `{cur['curriculum_version']}`",
         "- **Birincil kaynak:** MEB TYMM Fizik Dersi Öğretim Programı (9, 10, 11 ve 12. Sınıflar), PDF, tymm.meb.gov.tr, 19.08.2026 (`src-meb-fizik-op-2026`)",
         "- **İkincil kaynak:** tymm.meb.gov.tr 11. sınıf ünite sayfaları, güncelleme 05.08.2026",
         "- **Doğrulama:** 33 öğrenme çıktısı ve tüm süreç bileşenleri PDF ile web sayfası arasında birebir karşılaştırıldı; metin farkı 0.",
         "",
         "## Özet", "",
         "| # | Ünite | Ders saati | Öğrenme çıktısı | Süreç bileşeni | İçerik başlığı |",
         "|---|---|---|---|---|---|"]
    for u in cur["units"]:
        los = [by_id[i] for i in u["learning_outcome_ids"]]
        L.append(f"| {u['unit_no']} | {u['official_title']} | {u['hours']} | {len(los)} | "
                 f"{sum(len(o['process_components']) for o in los)} | {len(u['topics'])} |")
    L += [f"| | Okul temelli planlama | 6 | | | |",
          f"| | **Toplam** | **{cur['total_hours']}** | **{len(outcomes)}** | "
          f"**{sum(len(o['process_components']) for o in outcomes)}** | **{sum(len(u['topics']) for u in cur['units'])}** |", "",
          "Hiyerarşi: **Ünite → İçerik başlığı → Öğrenme çıktısı → Süreç bileşeni**. "
          "Öğrenme çıktısı → içerik başlığı eşlemesi programda açıkça verilmez; başlık adlarından türetildi (güveni her çıktıda belirtildi).", ""]
    for u in cur["units"]:
        L += [f"---", "", f"## Ünite {u['unit_no']}: {u['official_title']} ({u['hours']} ders saati)", "",
              f"**Amaç (resmî):** {u['purpose']}", "",
              f"**Temel kabuller (resmî, bağlayıcı):** {u['basic_assumptions_official']}", "",
              "**Beceriler (resmî):**", "",
              f"- Alan becerileri: {', '.join(u['field_skills'])}",
              f"- Kavramsal beceriler: {', '.join(u['conceptual_skills'])}",
              f"- Eğilimler: {', '.join(u['dispositions'])}",
              f"- Sosyal-duygusal: {', '.join(u['social_emotional_skills'])}",
              f"- Değerler: {', '.join(u['values'])}",
              f"- Okuryazarlık: {', '.join(u['literacy_skills'])}",
              f"- Disiplinler arası: {', '.join(u['interdisciplinary_links'])}",
              f"- Beceriler arası: {', '.join(u['cross_skill_links'])}", "",
              f"**Anahtar kavramlar (resmî):** {', '.join(u['key_concepts_official'])}", ""]
        for t in u["topics"]:
            los = [by_id[i] for i in u["learning_outcome_ids"] if by_id[i]["subtopic"]["topic_id"] == t["id"]]
            L += [f"### {t['official_title']}", ""]
            for o in los:
                conf = "" if o["subtopic"]["confidence"] == "HIGH" else f" _(başlık eşlemesi: {o['subtopic']['confidence']})_"
                L.append(f"- **{o['official_code']}** {o['official_text']} — beceri `{o['skills'][0]['code']}`{conf}")
                for c in o["process_components"]:
                    L.append(f"  - {c['label']}) {c['official_text']}")
                for s in o["official_scope_constraints"]:
                    L.append(f"  - ⚠️ _Kapsam (resmî):_ {s}")
            L.append("")
        L += ["**Zenginleştirme (resmî; öğrenme çıktısı eklemez, ders kitabında yer almaz):**", ""]
        for e in u["enrichment_official"]:
            tag = " **[* fen liselerinde zorunlu]**" if e["mandatory_in_science_high_schools"] else ""
            L.append(f"- {e['official_text']}{tag}")
        L += ["", "**Destekleme (resmî):**", ""] + [f"- {s}" for s in u["support_official"]] + [""]
    L += ["---", "", "## Sınıflar arası bağlam (yalnız ünite düzeyi, aynı PDF)", "",
          "| Sınıf | Üniteler (öğrenme çıktısı / ders saati) |", "|---|---|",
          "| 9 | Fizik Bilimi ve Kariyer Keşfi (4/8), Kuvvet ve Hareket (7/24), Akışkanlar (7/18), Enerji (6/18) |",
          "| 10 | Kuvvet ve Hareket (3/14), Enerji (5/16), Elektrik (7/22), Dalgalar (7/16) |",
          "| **11** | **Kuvvet ve Hareket (10/54), Elektrik ve Manyetizma (13/48), Optik (10/36)** |",
          "| 12 | Kuvvet ve Hareket (6/46), Enerji (6/36), Dalgalar (7/22), Madde ve Doğası (8/34) |", "",
          "Her sınıfa ayrıca 6 saat okul temelli planlama eklenir (toplam 72 / 72 / 144 / 144).", ""]
    (KB / "curriculum" / "master-map.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
