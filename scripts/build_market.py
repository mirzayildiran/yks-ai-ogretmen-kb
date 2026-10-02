"""STEP 9: piyasa kaynaklarının (Tier 3) yapısal analizini doğrular ve derler. Telifli soru KOPYALANMAZ.

Girdi : scripts/data_market.py (SOURCES)
Çıktı : knowledge-base/physics-11/question-patterns/{market-sources.json, market-analysis.md}
Kullanım: python3 build_market.py [--check]

SOURCES öğesi:
  slug, publisher, title, kind ("soru_bankasi"|"konu_anlatimi"|"fasikul"|"deneme"|"yaprak_test"|"dijital_platform"|"video_kanal"),
  target ("11"|"AYT"|"TYT"|"YKS"), edition_year (int|None), maarif_claim (True|False|None = bilinmiyor),
  url (ürün/yayınevi sayfası), verified_by_fetch (bool: sayfa okundu mu),
  question_styles [KLASIK_ISLEM|BAGLAM_TEMELLI|GRAFIK_TABLO|DENEY_VERI|KAVRAMSAL|COK_ADIMLI],
  difficulty ("kolay"|"orta"|"zor"|"karma"|None), pedagogical_style (str), unique_characteristics [str],
  sample_evidence [{"url", "what": str}]   (yayınevinin herkese açık örnek sayfa/PDF'i; okunduysa),
  family_mapping [{"family": aile_slug, "evidence": str, "match": "exact"|"partial"}]  (yalnız örnek sayfada GÖRÜLEN kalıplar),
  old_curriculum_risk (bool: eski müfredat içeriği taşıma olasılığı), notes, confidence ("HIGH"|"MEDIUM"|"LOW")
"""
import sys
from collections import Counter

from build_curriculum import TODAY, CURRICULUM_VERSION
from kb_common import KB, family_slugs, report, write_json

CHECK = "--check" in sys.argv
KINDS = {"soru_bankasi", "konu_anlatimi", "fasikul", "deneme", "yaprak_test", "dijital_platform", "video_kanal"}
STYLES = {"KLASIK_ISLEM", "BAGLAM_TEMELLI", "GRAFIK_TABLO", "DENEY_VERI", "KAVRAMSAL", "COK_ADIMLI"}


def main():
    import data_market as d
    fams = family_slugs()
    errors, warnings = [], []
    for s, n in Counter(x["slug"] for x in d.SOURCES).items():
        if n > 1:
            errors.append(f"Yinelenen kaynak: {s}")
    for x in d.SOURCES:
        t = x["slug"]
        if x["kind"] not in KINDS:
            errors.append(f"{t}: geçersiz kind")
        if x["target"] not in {"11", "AYT", "TYT", "YKS"}:
            errors.append(f"{t}: geçersiz target")
        if not x["url"].startswith("http"):
            errors.append(f"{t}: URL yok")
        for st in x["question_styles"]:
            if st not in STYLES:
                errors.append(f"{t}: geçersiz stil {st}")
        for fm in x["family_mapping"]:
            if fm["family"] not in fams:
                errors.append(f"{t}: bilinmeyen aile {fm['family']}")
            if not x["sample_evidence"]:
                errors.append(f"{t}: örnek sayfa kanıtı olmadan aile eşlemesi yapılamaz")
        if x["question_styles"] and not (x["verified_by_fetch"] or x["sample_evidence"]):
            warnings.append(f"{t}: soru stili iddiası var ama sayfa okunmadı")
    mapped = Counter(fm["family"] for x in d.SOURCES for fm in x["family_mapping"])
    lines = [f"{len(d.SOURCES)} kaynak; okunarak doğrulanan {sum(x['verified_by_fetch'] for x in d.SOURCES)}; "
             f"Maarif beyanlı {sum(x['maarif_claim'] is True for x in d.SOURCES)}; eski müfredat riski {sum(x['old_curriculum_risk'] for x in d.SOURCES)}",
             f"tür: {dict(Counter(x['kind'] for x in d.SOURCES))}",
             f"piyasa kanıtı olan aile: {len(mapped)}"]
    if not CHECK:
        write_json("question-patterns/market-sources.json", {
            "subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION, "generated_at": TODAY,
            "generated_by": "scripts/build_market.py", "tier": 3,
            "copyright_note": "Yalnız künye ve yapısal gözlem; telifli soru metni yok.",
            "sources": d.SOURCES, "family_market_evidence": dict(mapped)})
        L = ["# Piyasa Kaynakları — Yapısal Analiz", "", "> Otomatik üretildi: `scripts/build_market.py`. Tier 3; telifli içerik kopyalanmadı.", "",
             "| Yayınevi | Kitap | Tür | Hedef | Maarif | Stiller | Okundu | Eski müfredat riski |", "|---|---|---|---|---|---|---|---|"]
        for x in d.SOURCES:
            mc = {True: "evet", False: "hayır", None: "?"}[x["maarif_claim"]]
            L.append(f"| {x['publisher']} | {x['title']} | {x['kind']} | {x['target']} | {mc} | {', '.join(x['question_styles']) or '—'} | "
                     f"{'✓' if x['verified_by_fetch'] else '—'} | {'⚠️' if x['old_curriculum_risk'] else ''} |")
        (KB / "question-patterns" / "market-analysis.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    else:
        lines.append("(--check: dosya yazılmadı)")
    return report("PİYASA ANALİZİ", errors, warnings, lines)


if __name__ == "__main__":
    raise SystemExit(main())
