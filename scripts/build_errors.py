"""STEP 13: hata taksonomisi ve kavram yanılgılarını doğrular ve derler.

Girdi : scripts/data_errors.py (ERROR_TYPES, MISCONCEPTIONS)
Çıktı : knowledge-base/physics-11/error-taxonomy/{error-types.json, misconceptions.json, error-taxonomy.md}
Kullanım: python3 build_errors.py [--check]

ERROR_TYPES öğesi: code (14 zorunlu koddan biri; ek kod eklenebilir), name_tr, definition, symptoms [],
  diagnostic_questions [] (öğretmenin öğrenciye soracağı kısa sorular), remediation_strategy [] (adımlar),
  recommended_question_families [aile slug'ları], related_error_types [kodlar]
MISCONCEPTIONS öğesi: slug, statement (yanılgı cümlesi), correct_view, concepts [kavram slug'ları],
  learning_outcomes [kodlar], error_type (kod), how_it_appears (hangi soruda/çeldiricide görünür),
  diagnostic_item {stem, options {A..E}, answer, misconception_option}  (ÖZGÜN soru),
  remediation {socratic_questions [3–5], cognitive_conflict, analogy},
  sources [{citation, url, tier (1|2|3), accessed (YYYY-MM-DD), verified_by_fetch (bool)}], confidence
"""
import sys
from collections import Counter

from build_curriculum import TODAY, CURRICULUM_VERSION
from kb_common import ERROR_CODES, KB, concept_slugs, family_slugs, lo_codes, report, write_json

CHECK = "--check" in sys.argv


def main():
    import data_errors as d
    los, cons, fams = lo_codes(), concept_slugs(), family_slugs()
    errors, warnings = [], []
    codes = [e["code"] for e in d.ERROR_TYPES]
    for c in ERROR_CODES - set(codes):
        errors.append(f"Zorunlu hata türü eksik: {c}")
    for c, n in Counter(codes).items():
        if n > 1:
            errors.append(f"Yinelenen hata türü: {c}")
    for e in d.ERROR_TYPES:
        for k in ("definition", "symptoms", "diagnostic_questions", "remediation_strategy"):
            if not e.get(k):
                errors.append(f"{e['code']}: '{k}' boş")
        for f in e["recommended_question_families"]:
            if f not in fams:
                errors.append(f"{e['code']}: bilinmeyen aile {f}")
        for r in e["related_error_types"]:
            if r not in codes:
                errors.append(f"{e['code']}: bilinmeyen ilişkili tür {r}")
    mslugs = [m["slug"] for m in d.MISCONCEPTIONS]
    for s, n in Counter(mslugs).items():
        if n > 1:
            errors.append(f"Yinelenen yanılgı: {s}")
    for m in d.MISCONCEPTIONS:
        t = m["slug"]
        for c in m["concepts"]:
            if c not in cons:
                errors.append(f"{t}: bilinmeyen kavram {c}")
        for c in m["learning_outcomes"]:
            if c not in los:
                errors.append(f"{t}: bilinmeyen çıktı {c}")
        if m["error_type"] not in codes:
            errors.append(f"{t}: bilinmeyen hata türü {m['error_type']}")
        di = m["diagnostic_item"]
        if set(di["options"]) != set("ABCDE") or di["answer"] not in di["options"] or di["misconception_option"] not in di["options"] \
                or di["answer"] == di["misconception_option"]:
            errors.append(f"{t}: tanı sorusu biçimi hatalı (A–E, cevap ≠ yanılgı şıkkı)")
        if not 3 <= len(m["remediation"]["socratic_questions"]) <= 5:
            errors.append(f"{t}: 3–5 Sokratik soru olmalı")
        if not m["sources"]:
            errors.append(f"{t}: kaynak yok")
        for s in m["sources"]:
            if not s["url"].startswith("http"):
                errors.append(f"{t}: kaynak URL'si yok ({s['citation'][:40]})")
            if not s["verified_by_fetch"]:
                warnings.append(f"{t}: kaynak okunarak doğrulanmadı ({s['citation'][:50]})")
        if not any(s["tier"] in (1, 2) for s in m["sources"]):
            warnings.append(f"{t}: Tier 1–2 kaynak yok")
    covered = Counter(c for m in d.MISCONCEPTIONS for c in m["learning_outcomes"])
    for c in los:
        if not covered[c]:
            warnings.append(f"{c}: kavram yanılgısı kaydı yok")

    lines = [f"{len(d.ERROR_TYPES)} hata türü, {len(d.MISCONCEPTIONS)} kavram yanılgısı",
             f"yanılgısı olan çıktı: {sum(1 for c in los if covered[c])}/{len(los)}",
             f"kaynak: {sum(len(m['sources']) for m in d.MISCONCEPTIONS)} "
             f"(okunarak doğrulanan {sum(s['verified_by_fetch'] for m in d.MISCONCEPTIONS for s in m['sources'])}), "
             f"tier: {dict(Counter(s['tier'] for m in d.MISCONCEPTIONS for s in m['sources']))}"]
    if not CHECK:
        meta = {"subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION, "generated_at": TODAY,
                "generated_by": "scripts/build_errors.py"}
        write_json("error-taxonomy/error-types.json", {**meta, "error_types": [
            {"id": f"err-{e['code'].lower().replace('_', '-')}", **e} for e in d.ERROR_TYPES]})
        write_json("error-taxonomy/misconceptions.json", {**meta, "misconceptions": [
            {"id": f"phys11-mc-{m['slug']}", **m,
             "concept_ids": [cons[c] for c in m["concepts"] if c in cons],
             "learning_outcome_ids": [los[c]["id"] for c in m["learning_outcomes"] if c in los],
             "review_status": "ai_authored_pending_expert_review"} for m in d.MISCONCEPTIONS]})
        write_md(d)
    else:
        lines.append("(--check: dosya yazılmadı)")
    return report("HATA TAKSONOMİSİ", errors, warnings, lines)


def write_md(d):
    L = ["# Hata Taksonomisi ve Kavram Yanılgıları — 11. Sınıf Fizik", "", "> Otomatik üretildi: `scripts/build_errors.py`.", "",
         "## Hata türleri", "", "| Kod | Ad | Tanım |", "|---|---|---|"]
    L += [f"| `{e['code']}` | {e['name_tr']} | {e['definition']} |" for e in d.ERROR_TYPES]
    L += ["", "## Kavram yanılgıları", "", "| Yanılgı | Çıktı | Hata türü | Kaynak |", "|---|---|---|---|"]
    for m in d.MISCONCEPTIONS:
        L.append(f"| {m['statement']} | {', '.join(m['learning_outcomes'])} | `{m['error_type']}` | "
                 f"{'; '.join(s['citation'][:60] for s in m['sources'])} |")
    (KB / "error-taxonomy" / "error-taxonomy.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
