"""STEP 11–12: çözüm yöntemleri ve kısa yolları doğrular ve derler.

Girdi : scripts/data_solutions_u*.py  (SOLUTIONS, SHORTCUTS)
Çıktı : knowledge-base/physics-11/solution-methods/solution-methods.json, shortcuts/shortcuts.json, solutions.md
Kullanım: python3 build_solutions.py [--check] [modül ...]

SOLUTIONS: {aile_slug: {
    "standard": M, "conceptual": M, "fast": M | None, "alternative": M | None,
    "expert_insight": str,                      # soruyu hızlı tanımaya yarayan ipucu
    "worked_example": {"problem": str (ÖZGÜN), "steps": [str], "answer": str,
                       "python_check": str}     # çalıştırılınca assert'lerle cevabı doğrulayan kod
}}
  M = {"steps": [str], "validity": [str], "limits": [str], "risks": [str]}
SHORTCUTS: [{"slug", "name", "question_families": [slug], "shortcut", "why_it_works",
             "validity_conditions": [str], "failure_cases": [str] (zorunlu), "risk_level": "LOW"|"MEDIUM"|"HIGH",
             "sources": [{"type": "textbook"|"derivation"|"program", "ref": str}],
             "numeric_check": str}]   # rastgele/özel değerlerde kısa yolu tam yöntemle karşılaştıran assert'li kod
Kurallar: kapsamdaki (CORE) her ailenin çözümü olmalı; python_check ve numeric_check hatasız çalışmalı.
"""
import importlib
import subprocess
import sys
from collections import Counter
from pathlib import Path

from build_curriculum import TODAY, CURRICULUM_VERSION
from kb_common import KB, family_slugs, report, write_json

CHECK = "--check" in sys.argv
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
HERE = Path(__file__).resolve().parent
MODULES = ARGS or sorted(p.stem for p in HERE.glob("data_solutions_u*.py"))
METHOD_KEYS = ("steps", "validity", "limits", "risks")


CHECK_TIMEOUT = 20  # saniye; sonsuz döngüye giren doğrulama kodu tüm hattı kilitlemesin


def run_check(code, label, errors):
    """Doğrulama kodunu ayrı süreçte, zaman sınırıyla çalıştırır."""
    try:
        r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=CHECK_TIMEOUT)
    except subprocess.TimeoutExpired:
        errors.append(f"{label}: doğrulama kodu {CHECK_TIMEOUT} sn içinde bitmedi (sonsuz döngü?)")
        return False
    if r.returncode != 0:
        last = (r.stderr.strip().splitlines() or ["?"])[-1]
        errors.append(f"{label}: doğrulama kodu başarısız ({last[:100]})")
        return False
    return True


def main():
    fams = family_slugs()
    fam_unit = {}
    fam_scope, fam_shortcuts = {}, {}
    for p in sorted(HERE.glob("data_question_families_u*.py")):
        mod = importlib.import_module(p.stem)
        for f in mod.FAMILIES:
            fam_unit[f["slug"]] = int(p.stem.rsplit("_u", 1)[1])
            fam_scope[f["slug"]] = f["scope"]
            fam_shortcuts[f["slug"]] = f["shortcuts"]
    errors, warnings, sols, shorts = [], [], [], []
    units = set()
    for m in MODULES:
        units.add(int(m.rsplit("_u", 1)[1]))
        mod = importlib.import_module(m)
        for slug, s in mod.SOLUTIONS.items():
            if slug not in fams:
                errors.append(f"{m}: bilinmeyen aile {slug}")
                continue
            for k in ("standard", "conceptual"):
                if not s.get(k):
                    errors.append(f"{slug}: '{k}' yöntemi yok")
            for k in ("standard", "conceptual", "fast", "alternative"):
                meth = s.get(k)
                if meth:
                    for f in METHOD_KEYS:
                        if not meth.get(f):
                            errors.append(f"{slug}.{k}: '{f}' boş")
            if not s.get("expert_insight"):
                errors.append(f"{slug}: expert_insight boş")
            we = s.get("worked_example") or {}
            ok = bool(we.get("python_check")) and run_check(we["python_check"], f"{slug}.worked_example", errors)
            if not we.get("python_check"):
                errors.append(f"{slug}: worked_example.python_check yok")
            sols.append({"id": f"phys11-sol-{slug}", "question_family": slug, **s, "worked_example_verified": ok,
                         "review_status": "ai_authored_pending_expert_review"})
        for sc in mod.SHORTCUTS:
            t = sc["slug"]
            for f in sc["question_families"]:
                if f not in fams:
                    errors.append(f"{t}: bilinmeyen aile {f}")
            if not sc["failure_cases"]:
                errors.append(f"{t}: failure_cases zorunlu")
            if not sc["validity_conditions"] or not sc["why_it_works"]:
                errors.append(f"{t}: geçerlilik koşulu / gerekçe boş")
            if sc["risk_level"] not in ("LOW", "MEDIUM", "HIGH"):
                errors.append(f"{t}: geçersiz risk_level")
            ok = run_check(sc["numeric_check"], f"{t}.numeric_check", errors) if sc.get("numeric_check") else False
            if not sc.get("numeric_check"):
                warnings.append(f"{t}: numeric_check yok (nitel kısa yol)")
            shorts.append({"id": f"phys11-sc-{t}", **sc, "numeric_verified": ok, "review_status": "ai_authored_pending_expert_review"})

    covered = {s["question_family"] for s in sols}
    for f, u in fam_unit.items():
        if u in units and fam_scope[f] == "CORE" and f not in covered:
            errors.append(f"Ünite {u}: kapsamdaki aile çözümsüz: {f}")
    sc_fams = {f for s in shorts for f in s["question_families"]}
    for f, names in fam_shortcuts.items():
        if fam_unit[f] in units and names and f not in sc_fams:
            warnings.append(f"{f}: ailede kısa yol adı var ({names[0][:40]}) ama SHORTCUTS kaydına bağlanmamış")
    for s, n in Counter(x["slug"] for x in shorts).items():
        if n > 1:
            errors.append(f"Yinelenen kısa yol: {s}")

    lines = [f"modüller: {MODULES}", f"{len(sols)} aile çözümü (doğrulanan çözümlü örnek {sum(s['worked_example_verified'] for s in sols)})",
             f"{len(shorts)} kısa yol (sayısal doğrulanan {sum(s['numeric_verified'] for s in shorts)}), risk: {dict(Counter(s['risk_level'] for s in shorts))}"]
    if not CHECK:
        meta = {"subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION, "generated_at": TODAY,
                "generated_by": "scripts/build_solutions.py", "units_covered": sorted(units)}
        write_json("solution-methods/solution-methods.json", {**meta, "count": len(sols), "solutions": sols})
        write_json("shortcuts/shortcuts.json", {**meta, "count": len(shorts), "shortcuts": shorts})
        L = ["# Kısa Yollar — 11. Sınıf Fizik", "", "> Otomatik üretildi: `scripts/build_solutions.py`. Her kısa yol sayısal olarak tam yöntemle karşılaştırıldı.", "",
             "| Kısa yol | Aileler | Risk | Ne zaman çalışmaz (ilk madde) |", "|---|---|---|---|"]
        L += [f"| **{s['name']}** — {s['shortcut']} | {', '.join(s['question_families'])} | {s['risk_level']} | {s['failure_cases'][0]} |" for s in shorts]
        (KB / "shortcuts" / "shortcuts.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    else:
        lines.append("(--check: dosya yazılmadı)")
    return report("ÇÖZÜM YÖNTEMLERİ VE KISA YOLLAR", errors, warnings, lines)


if __name__ == "__main__":
    raise SystemExit(main())
