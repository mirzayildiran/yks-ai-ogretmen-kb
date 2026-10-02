"""STEP 14: AI öğretmenin pedagojik davranış modelini doğrular ve derler.

Girdi : scripts/data_pedagogy.py (PROTOCOLS, HINT_LADDER, INTERVENTIONS, VOICE_GUIDELINES)
Çıktı : knowledge-base/physics-11/pedagogy/{pedagogy.json, pedagogy.md}
Kullanım: python3 build_pedagogy.py [--check]

PROTOCOLS: [{"slug", "trigger" (öğrenci durumu), "goal", "steps": [{"n", "action", "teacher_says_example",
             "observe", "branch": {koşul: sonraki_adım_n | protokol_slug}}], "exit_criteria", "sources": [str]}]
HINT_LADDER: [{"level" (1..), "name", "what_to_give", "what_not_to_give", "example"}]
INTERVENTIONS: [{"error_type" (hata kodu), "first_move", "diagnostic_prompt", "remediation_steps": [str],
                 "fallback_to_prerequisite": bool, "recommended_question_families": [slug]}]
VOICE_GUIDELINES: [{"rule", "why", "example"}]
Kurallar: her hata türünün bir müdahalesi olmalı; dallar var olan adımlara ya da protokollere gitmeli.
"""
import sys

from build_curriculum import TODAY, CURRICULUM_VERSION
from kb_common import KB, family_slugs, report, write_json

CHECK = "--check" in sys.argv


def main():
    import data_pedagogy as d
    import data_errors as de
    fams = family_slugs()
    codes = {e["code"] for e in de.ERROR_TYPES}
    errors, warnings = [], []
    pslugs = {p["slug"] for p in d.PROTOCOLS}
    for p in d.PROTOCOLS:
        ns = {s["n"] for s in p["steps"]}
        for s in p["steps"]:
            for cond, target in s.get("branch", {}).items():
                if target not in ns and target not in pslugs:
                    errors.append(f"{p['slug']} adım {s['n']}: dal hedefi yok ({target})")
        if not p["exit_criteria"]:
            errors.append(f"{p['slug']}: çıkış ölçütü yok")
    levels = [h["level"] for h in d.HINT_LADDER]
    if levels != list(range(1, len(levels) + 1)):
        errors.append("İpucu merdiveni seviyeleri 1'den ardışık olmalı")
    covered = {i["error_type"] for i in d.INTERVENTIONS}
    for c in codes - covered:
        errors.append(f"Hata türünün müdahalesi yok: {c}")
    for i in d.INTERVENTIONS:
        if i["error_type"] not in codes:
            errors.append(f"Bilinmeyen hata türü: {i['error_type']}")
        for f in i["recommended_question_families"]:
            if f not in fams:
                errors.append(f"{i['error_type']}: bilinmeyen aile {f}")
    lines = [f"{len(d.PROTOCOLS)} protokol, {len(d.HINT_LADDER)} ipucu seviyesi, {len(d.INTERVENTIONS)} müdahale, "
             f"{len(d.VOICE_GUIDELINES)} sesli anlatım kuralı"]
    if not CHECK:
        write_json("pedagogy/pedagogy.json", {"subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION,
                                               "generated_at": TODAY, "generated_by": "scripts/build_pedagogy.py",
                                               "protocols": d.PROTOCOLS, "hint_ladder": d.HINT_LADDER,
                                               "interventions": d.INTERVENTIONS, "voice_guidelines": d.VOICE_GUIDELINES})
        L = ["# AI Öğretmen Pedagojik Davranış Modeli", "", "> Otomatik üretildi: `scripts/build_pedagogy.py`.", ""]
        for p in d.PROTOCOLS:
            L += [f"## {p['slug']} — {p['trigger']}", "", f"**Amaç:** {p['goal']}", ""]
            L += [f"{s['n']}. **{s['action']}** — _“{s['teacher_says_example']}”_" for s in p["steps"]]
            L += ["", f"**Çıkış:** {p['exit_criteria']}", ""]
        L += ["## İpucu merdiveni", "", "| Seviye | Ad | Ver | Verme |", "|---|---|---|---|"]
        L += [f"| {h['level']} | {h['name']} | {h['what_to_give']} | {h['what_not_to_give']} |" for h in d.HINT_LADDER]
        (KB / "pedagogy" / "pedagogy.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    else:
        lines.append("(--check: dosya yazılmadı)")
    return report("PEDAGOJİ", errors, warnings, lines)


if __name__ == "__main__":
    raise SystemExit(main())
