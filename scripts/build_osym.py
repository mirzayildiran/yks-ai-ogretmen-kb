"""STEP 10: ÖSYM sorularının yapısal analizini doğrular ve derler.

Girdi : scripts/data_osym.py  (ANNOUNCEMENTS, ITEMS)
Çıktı : knowledge-base/physics-11/osym-analysis/{osym-items.json, osym-analysis.md}
Kullanım: python3 build_osym.py [--check]

ITEMS öğesi alanları:
  year (2018–2026), exam ("TYT"|"AYT"), question_no (fizik testindeki sıra, int), source_url, read_method
  ("official_pdf"|"official_page_image"|"secondary_site"), topic, learning_outcomes [11. sınıf kodları, boş olabilir],
  out_of_11_scope (learning_outcomes boşsa zorunlu: ör. "12. sınıf FİZ.12.1.3" / "10. sınıf FİZ.10.3.4" / "programda yok"),
  question_family (aile slug'ı | None), family_match ("exact"|"partial"|"none"), skills [beceri kodları],
  conceptual_load / interpretation_load (1–3), mathematical_load (0–3), multi_step, graph_based, table_based,
  experimental_context, daily_life_context (bool), distractor_structure, solution_strategy,
  summary (kendi cümlenle ≤ 35 kelime; soru metni KOPYALANMAZ), fit_2028 ("yes"|"form_changes"|"no"),
  fit_reason, confidence ("HIGH"|"MEDIUM"|"LOW")
ANNOUNCEMENTS öğesi: id, title, organization, url, date, summary, relevance, verified_read (bool)
"""
import sys
from collections import Counter, defaultdict

from build_curriculum import TODAY, CURRICULUM_VERSION
from kb_common import family_slugs, lo_codes, report, skill_codes, write_json, KB

CHECK = "--check" in sys.argv
EXAMS = {"TYT", "AYT"}
READ = {"official_pdf", "official_page_image", "secondary_site"}
CONF = {"HIGH", "MEDIUM", "LOW"}
FIT = {"yes", "form_changes", "no"}


def main():
    import data_osym as d
    los, fams, skills = lo_codes(), family_slugs(), skill_codes()
    errors, warnings, items = [], [], []
    seen = set()
    for i, it in enumerate(d.ITEMS, 1):
        key = (it["year"], it["exam"], it["question_no"])
        tag = f"{it['year']} {it['exam']} S{it['question_no']}"
        if key in seen:
            errors.append(f"Yinelenen soru: {tag}")
        seen.add(key)
        if not 2018 <= it["year"] <= 2026 or it["exam"] not in EXAMS:
            errors.append(f"{tag}: geçersiz yıl/sınav")
        if it["read_method"] not in READ:
            errors.append(f"{tag}: geçersiz read_method")
        if not it["source_url"].startswith("http"):
            errors.append(f"{tag}: kaynak URL yok")
        for c in it["learning_outcomes"]:
            if c not in los:
                errors.append(f"{tag}: bilinmeyen çıktı {c}")
        if not it["learning_outcomes"] and not it.get("out_of_11_scope"):
            errors.append(f"{tag}: 11. sınıf dışıysa out_of_11_scope zorunlu")
        if it["question_family"] and it["question_family"] not in fams:
            errors.append(f"{tag}: bilinmeyen aile {it['question_family']}")
        if it["family_match"] not in {"exact", "partial", "none"} or (it["question_family"] is None) != (it["family_match"] == "none"):
            errors.append(f"{tag}: family_match ile question_family tutarsız")
        for s in it["skills"]:
            if s not in skills:
                warnings.append(f"{tag}: 11. sınıf beceri listesinde olmayan beceri {s}")
        for k, lo, hi in (("conceptual_load", 1, 3), ("interpretation_load", 1, 3), ("mathematical_load", 0, 3)):
            if not lo <= it[k] <= hi:
                errors.append(f"{tag}: {k} aralık dışı")
        if len(it["summary"].split()) > 35:
            errors.append(f"{tag}: özet 35 kelimeyi aşıyor (telif: kısa ve kendi cümlenle)")
        if it["fit_2028"] not in FIT or it["confidence"] not in CONF:
            errors.append(f"{tag}: geçersiz fit_2028/confidence")
        items.append({"id": f"osym-{it['year']}-{it['exam'].lower()}-{it['question_no']:02d}", **it,
                      "question_family_module": fams.get(it["question_family"]) if it["question_family"] else None})
    for a in d.ANNOUNCEMENTS:
        if not a["url"].startswith("http"):
            errors.append(f"Duyuru {a['id']}: URL yok")

    by_year = defaultdict(list)
    for it in items:
        by_year[(it["year"], it["exam"])].append(it)
    lo_count = Counter(c for it in items for c in it["learning_outcomes"])
    lines = [f"{len(items)} ÖSYM sorusu, {len(by_year)} sınav oturumu, {len(d.ANNOUNCEMENTS)} duyuru",
             f"11. sınıf çıktısına eşlenen: {sum(1 for it in items if it['learning_outcomes'])}",
             f"aileye eşlenen: {dict(Counter(it['family_match'] for it in items))}",
             f"2028 uyumu: {dict(Counter(it['fit_2028'] for it in items))}"]
    if not CHECK:
        write_json("osym-analysis/osym-items.json", {
            "subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION, "generated_at": TODAY,
            "generated_by": "scripts/build_osym.py", "copyright_note": "Soru metinleri kopyalanmadı; yalnız yapısal analiz ve kısa özet.",
            "announcements": d.ANNOUNCEMENTS, "count": len(items), "items": items})
        write_md(items, by_year, lo_count, d.ANNOUNCEMENTS)
    else:
        lines.append("(--check: dosya yazılmadı)")
    return report("ÖSYM ANALİZİ", errors, warnings, lines)


def write_md(items, by_year, lo_count, ann):
    L = ["# ÖSYM Yapısal Analizi — 11. Sınıf Fizik", "", "> Otomatik üretildi: `scripts/build_osym.py`. Soru metinleri kopyalanmadı.", "",
         "## Resmî duyurular", ""]
    L += [f"- **{a['title']}** ({a['organization']}, {a['date']}) — {a['summary']} {'' if a['verified_read'] else '_(okunamadı)_'}" for a in ann] or ["- Kayıt yok"]
    L += ["", "## Oturum bazında 11. sınıf payı ve soru tarzı", "",
          "| Oturum | Soru | 11. sınıf | Grafik | Tablo | Deney | Günlük hayat | Çok adımlı |", "|---|---|---|---|---|---|---|---|"]
    for (y, e), lst in sorted(by_year.items()):
        L.append(f"| {y} {e} | {len(lst)} | {sum(1 for i in lst if i['learning_outcomes'])} | {sum(i['graph_based'] for i in lst)} | "
                 f"{sum(i['table_based'] for i in lst)} | {sum(i['experimental_context'] for i in lst)} | {sum(i['daily_life_context'] for i in lst)} | "
                 f"{sum(i['multi_step'] for i in lst)} |")
    L += ["", "## Öğrenme çıktısı başına soru sayısı", "", "| Çıktı | Soru |", "|---|---|"]
    L += [f"| {c} | {n} |" for c, n in sorted(lo_count.items(), key=lambda x: [int(v) for v in x[0].split('.')[1:]])]
    L += ["", "## Sorular", "", "| Oturum | No | Konu | Çıktı | Aile | 2028 | Özet |", "|---|---|---|---|---|---|---|"]
    for it in sorted(items, key=lambda i: (i["year"], i["exam"], i["question_no"])):
        L.append(f"| {it['year']} {it['exam']} | {it['question_no']} | {it['topic']} | {', '.join(it['learning_outcomes']) or it['out_of_11_scope']} | "
                 f"{it['question_family'] or '—'} ({it['family_match']}) | {it['fit_2028']} | {it['summary']} |")
    (KB / "osym-analysis" / "osym-analysis.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
