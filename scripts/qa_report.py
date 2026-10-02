"""STEP 15: katmanlar arası kalite kontrolü ve kapsam panosu.

Derlenmiş JSON'ları ve veri modüllerini birlikte okur; her öğrenme çıktısı için katman kapsamını ve
katmanlar arası tutarlılığı denetler.

Çıktı: knowledge-base/physics-11/audits/qa-report.md   (--check ile yalnız ekrana yazar)
Hata (çıkış kodu 1): katmanlar arası kırık referans. Uyarı: kapsam boşluğu.
"""
import importlib
import sys
from collections import Counter, defaultdict
from pathlib import Path

from build_curriculum import KB, TODAY
from kb_common import ERROR_CODES, load_json, report

CHECK = "--check" in sys.argv
HERE = Path(__file__).resolve().parent


def mods(prefix):
    out = []
    for p in sorted(HERE.glob(f"{prefix}*.py")):
        out.append(importlib.import_module(p.stem))
    return out


def main():
    errors, warnings = [], []
    los = {o["official_code"]: o for o in load_json("learning-outcomes/learning-outcomes.json")["learning_outcomes"]}
    concepts = load_json("concepts/concepts.json")["concepts"]
    formulas = load_json("formulas/formulas.json")["formulas"]
    qfs = load_json("question-families/question-families.json")["question_families"]
    osym = load_json("osym-analysis/osym-items.json")["items"]
    errs = importlib.import_module("data_errors")
    ped = importlib.import_module("data_pedagogy")
    sols, shorts = {}, []
    for m in mods("data_solutions_u"):
        sols.update(m.SOLUTIONS)
        shorts += m.SHORTCUTS
    err_codes = {e["code"] for e in errs.ERROR_TYPES}

    # --- katmanlar arası tutarlılık
    for c in ERROR_CODES - err_codes:
        errors.append(f"Görev tanımındaki hata kodu taksonomide yok: {c}")
    for q in qfs:
        for e in q["common_student_errors"]:
            if e["error_type"] not in err_codes:
                errors.append(f"{q['slug']}: aile hatası taksonomide yok ({e['error_type']})")
    for m in errs.MISCONCEPTIONS:
        if m["error_type"] not in err_codes:
            errors.append(f"yanılgı {m['slug']}: hata türü yok")
    qslugs = {q["slug"] for q in qfs}
    for s in sols:
        if s not in qslugs:
            errors.append(f"çözüm var ama aile yok: {s}")
    for i in ped.INTERVENTIONS:
        for f in i["recommended_question_families"]:
            if f not in qslugs:
                errors.append(f"pedagoji müdahalesi bilinmeyen aileye işaret ediyor: {f}")

    # --- çıktı başına pano
    by = defaultdict(lambda: Counter())
    for c in concepts:
        for l in c["learning_outcome_links"]:
            by[l["learning_outcome"]]["kavram"] += 1
    for f in formulas:
        for code in f["learning_outcomes"]:
            by[code]["formül"] += 1
    core = {q["slug"] for q in qfs if q["scope"] == "CORE"}
    for q in qfs:
        for code in q["learning_outcomes"]:
            by[code]["aile"] += 1
            if q["slug"] in sols:
                by[code]["çözüm"] += 1
            elif q["slug"] in core:
                by[code]["çözümsüz_aile"] += 1
    sc_fams = Counter(f for s in shorts for f in s["question_families"])
    for q in qfs:
        for code in q["learning_outcomes"]:
            if sc_fams[q["slug"]]:
                by[code]["kısa_yol_ailesi"] += 1
    for m in errs.MISCONCEPTIONS:
        for code in m["learning_outcomes"]:
            by[code]["yanılgı"] += 1
    for it in osym:
        for code in it["learning_outcomes"]:
            by[code]["ösym"] += 1
            if it["fit_2028"] == "yes":
                by[code]["ösym_2028_uyumlu"] += 1
    cols = ["kavram", "formül", "aile", "çözüm", "çözümsüz_aile", "kısa_yol_ailesi", "yanılgı", "ösym", "ösym_2028_uyumlu"]
    for code, o in los.items():
        b = by[code]
        if not b["aile"]:
            warnings.append(f"{code}: soru ailesi yok")
        if b["çözümsüz_aile"]:
            warnings.append(f"{code}: {b['çözümsüz_aile']} çekirdek aile çözümsüz")
        if not b["yanılgı"]:
            warnings.append(f"{code}: kavram yanılgısı yok")

    # --- distractor targets ↔ yanılgı eşleşmesi (sözcük örtüşmesiyle kaba ölçü)
    def toks(s):
        return {w for w in s.lower().replace(",", " ").split() if len(w) > 4}
    mtoks = [toks(m["statement"]) for m in errs.MISCONCEPTIONS]
    matched = total = 0
    for q in qfs:
        for d in q["common_distractors"]:
            total += 1
            t = toks(d["targets"])
            if any(len(t & mt) >= 2 for mt in mtoks):
                matched += 1

    lines = [f"{len(los)} çıktı · {len(concepts)} kavram · {len(formulas)} formül · {len(qfs)} aile · {len(sols)} çözüm · "
             f"{len(shorts)} kısa yol · {len(errs.MISCONCEPTIONS)} yanılgı · {len(osym)} ÖSYM sorusu · {len(ped.PROTOCOLS)} pedagoji protokolü",
             f"çeldirici hedeflerinin yanılgı kayıtlarıyla kaba eşleşmesi: {matched}/{total}"]
    if not CHECK:
        L = ["# Kalite Kontrol Panosu — 11. Sınıf Fizik", "", f"> Otomatik üretildi: `scripts/qa_report.py` ({TODAY}).", "",
             "## Özet", "", *[f"- {l}" for l in lines], "",
             "## Çıktı başına katman kapsamı", "", "| Çıktı | " + " | ".join(cols) + " |", "|---" * (len(cols) + 1) + "|"]
        for code in los:
            L.append(f"| {code} | " + " | ".join(str(by[code][c]) for c in cols) + " |")
        L += ["", "## Uyarılar", ""] + [f"- {w}" for w in warnings] + ["", "## Hatalar", ""] + ([f"- {e}" for e in errors] or ["- Yok"])
        (KB / "audits" / "qa-report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return report("KALİTE KONTROL (STEP 15)", errors, warnings, lines)


if __name__ == "__main__":
    raise SystemExit(main())
