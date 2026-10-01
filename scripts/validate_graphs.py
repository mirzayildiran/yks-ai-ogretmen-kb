"""Kavram ve ön koşul katmanlarının dosyalar arası tutarlılığını doğrular.

  - kavram / ilişki / beceri ID'leri benzersiz
  - öğrenme çıktılarındaki concepts, prior_concepts, prerequisites, skill referansları çözülüyor
  - ilişki uçları mevcut kavramlara işaret ediyor
  - her 11. sınıf çıktısının kavramı ve kanıtı var; kanıtsız kavram–çıktı bağlantısı yok
  - yetim kavram yok; müfredat sürümü tüm dosyalarda aynı
"""
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_curriculum import KB  # noqa: E402


def main():
    errors, warnings = [], []
    load = lambda p: json.loads((KB / p).read_text(encoding="utf-8"))
    lo_doc, cdoc, rdoc = load("learning-outcomes/learning-outcomes.json"), load("concepts/concepts.json"), load("concepts/relations.json")
    sdoc, pdoc = load("learning-outcomes/skills.json"), load("prerequisites/prerequisite-graph.json")
    los, concepts, rels, skills = lo_doc["learning_outcomes"], cdoc["concepts"], rdoc["relations"], sdoc["skills"]

    for name, items in (("kavram", concepts), ("ilişki", rels), ("beceri", skills), ("çıktı", los)):
        dup = [k for k, n in Counter(i["id"] for i in items).items() if n > 1]
        if dup:
            errors.append(f"Yinelenen {name} ID: {dup}")
    cids = {c["id"] for c in concepts}
    lo_ids = {o["id"] for o in los}
    lo_codes = {o["official_code"] for o in los}
    skill_codes = {s["official_code"] for s in skills}
    prior_catalog = set(pdoc["prior_outcomes_catalog"])

    for r in rels:
        for x in (r["source"], r["target"]):
            if x not in cids:
                errors.append(f"{r['id']}: kırık kavram referansı {x}")
    for o in los:
        for c in o.get("concepts", []) + o.get("prior_concepts", []):
            if c not in cids:
                errors.append(f"{o['official_code']}: kırık kavram referansı {c}")
        if not o.get("concepts"):
            errors.append(f"{o['official_code']}: 11. sınıf kavramı yok")
        for s in o["skills"]:
            if s["code"] not in skill_codes:
                errors.append(f"{o['official_code']}: tanımsız beceri {s['code']}")
        for c in o["process_components"]:
            sc = c.get("skill_component", {}).get("code")
            if not sc or sc.rsplit(".SB", 1)[0] != o["skills"][0]["code"]:
                errors.append(f"{c['id']}: süreç bileşeni beceri bileşenine bağlı değil")
        for p in o.get("prerequisites", []):
            if p["type"] == "learning_outcome":
                ok = p["code"] in lo_codes if p["grade"] == 11 else p["code"] in prior_catalog
                if not ok:
                    errors.append(f"{o['official_code']}: kırık ön koşul {p['code']}")
            elif p["concept_id"] not in cids:
                errors.append(f"{o['official_code']}: kırık ön koşul kavramı {p['concept_id']}")
        for f in o.get("pending_fields", []):
            if f != "common_misconceptions":  # STEP 13'te doldurulacak
                warnings.append(f"{o['official_code']}: bekleyen alan {f}")
    for c in concepts:
        for l in c["learning_outcome_links"]:
            if l["learning_outcome_id"] not in lo_ids:
                errors.append(f"{c['id']}: kırık çıktı referansı")
            if l["evidence_strength"] == "none":
                errors.append(f"{c['id']} → {l['learning_outcome']}: kanıtsız bağlantı")
        if not c["learning_outcome_links"]:
            errors.append(f"{c['id']}: hiçbir çıktıya bağlı değil")
    deg = Counter([r["source"] for r in rels] + [r["target"] for r in rels])
    for c in concepts:
        if deg[c["id"]] == 0:
            warnings.append(f"Yetim kavram: {c['id']}")
    versions = {d["curriculum_version"] for d in (lo_doc, cdoc, rdoc, sdoc, pdoc)}
    if len(versions) != 1:
        errors.append(f"Tutarsız müfredat sürümü: {versions}")
    if any(e["forward_in_program_order"] for e in pdoc["intra_grade_outcome_edges"]):
        warnings.append("Program sırasına ters ön koşul kenarı var")

    print(f"GRAFİK DOĞRULAMA: {len(concepts)} kavram, {len(rels)} ilişki, {len(skills)} beceri, "
          f"{len(pdoc['intra_grade_outcome_edges'])} çıktı-içi ön koşul kenarı")
    for w in warnings:
        print("  !", w)
    for e in errors:
        print("  ✗", e)
    print(f"  {'✓ 0 hata' if not errors else f'{len(errors)} hata'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
