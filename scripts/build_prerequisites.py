"""STEP 6: ön koşul grafiğini üretir ve doğrular.

Üç katman:
  1. 11. sınıf içi: çıktı A, çıktı B'yi gerektirir ⇐ A'nın kavramı, B'nin "ev" kavramını REQUIRES/SPECIAL_CASE_OF ile gerektirir
     (bir 11. sınıf kavramının evi, bağlı olduğu ilk çıktıdır). Kavram grafiğinden otomatik türetilir.
  2. Önceki sınıflar: ön koşul kavramı -> 9/10. sınıf resmî çıktısı (data_prerequisites.PRIOR_OUTCOMES, metinde doğrulanır)
  3. Ortaokul / matematik: resmî temel kabuller ve matematik notları (resmî kod yok)

Çıktı: knowledge-base/physics-11/prerequisites/{prerequisite-graph.json, prerequisites.md}
       learning-outcomes.json -> prerequisites, mathematical_prerequisites
"""
import json
import re
from collections import defaultdict

from build_concepts import find_cycle
from build_curriculum import KB, RAW, TODAY, CURRICULUM_VERSION, letters_only, strip_tags
from data_prerequisites import BASIC_ASSUMPTIONS, MATH_NOTES, PRIOR_OUTCOMES

OUT = KB / "prerequisites"
OTHER = RAW / "tymm-web" / "diger-siniflar"


def prior_outcomes():
    """9. ve 10. sınıf ham sayfalarından çıktı kodu, metni ve öğretme uygulamasını okur."""
    res = {}
    for f in sorted(OTHER.glob("sinif*_unite_*.txt")):
        grade = int(re.match(r"sinif(\d+)", f.name).group(1))
        if grade not in (9, 10):
            continue
        L = [l.strip() for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
        for i, l in enumerate(L):
            m = re.match(r"(FİZ\.\d+\.\d+\.\d+)\.\s*(.+)", l)
            if m and m.group(1) not in res:
                comps = []
                for x in L[i + 1:]:
                    if re.match(r"^[a-zç]\) ", x):
                        comps.append(x)
                    else:
                        break
                res[m.group(1)] = {"code": m.group(1), "grade": grade, "official_text": m.group(2).strip(),
                                   "components": comps, "practice": "", "unit_file": f.name}
        cur = None
        for l in L:
            m = re.fullmatch(r"(FİZ\.\d+\.\d+\.\d+)", l)
            if m:
                cur = m.group(1)
            elif cur and cur in res and l not in ("Farklılaştırma", "Zenginleştirme", "Destekleme"):
                res[cur]["practice"] += l + " "
            if l == "Farklılaştırma":
                cur = None
    for v in res.values():
        v["practice"] = strip_tags(v["practice"])
    return res


def main():
    lo_doc = json.loads((KB / "learning-outcomes" / "learning-outcomes.json").read_text(encoding="utf-8"))
    cur = json.loads((KB / "curriculum" / "curriculum.json").read_text(encoding="utf-8"))
    cdoc = json.loads((KB / "concepts" / "concepts.json").read_text(encoding="utf-8"))
    rdoc = json.loads((KB / "concepts" / "relations.json").read_text(encoding="utf-8"))
    los = lo_doc["learning_outcomes"]
    order = {o["official_code"]: i for i, o in enumerate(los)}
    by_code = {o["official_code"]: o for o in los}
    concepts = {c["id"]: c for c in cdoc["concepts"]}
    prior = prior_outcomes()
    errors, warnings = [], []

    # --- 2. önceki sınıf eşlemeleri (metinde doğrulanır)
    prior_links = {}
    for slug, items in PRIOR_OUTCOMES.items():
        cidv = f"phys11-c-{slug}"
        if cidv not in concepts:
            errors.append(f"Bilinmeyen kavram: {slug}")
            continue
        if concepts[cidv]["origin_grade"] == "11":
            errors.append(f"{slug} 11. sınıf kavramı; önceki sınıf eşlemesi olmamalı")
        links = []
        for code, terms in items:
            p = prior.get(code)
            if not p:
                errors.append(f"{slug}: önceki sınıf çıktısı bulunamadı {code}")
                continue
            hay_off = letters_only(p["official_text"] + " " + " ".join(p["components"]))
            hay_pr = letters_only(p["practice"])
            where = ("official_outcome_text" if any(letters_only(t) in hay_off for t in terms)
                     else "official_teaching_practice" if any(letters_only(t) in hay_pr for t in terms) else None)
            if not where:
                warnings.append(f"Kanıtsız önceki sınıf eşlemesi: {slug} → {code} ({terms})")
            links.append({"code": code, "grade": p["grade"], "official_text": p["official_text"],
                          "evidence": where, "confidence": "HIGH" if where == "official_outcome_text" else
                          "MEDIUM" if where else "LOW"})
        prior_links[cidv] = links

    # --- 3. temel kabuller
    assumptions = {}
    for u in cur["units"]:
        text = u["basic_assumptions_official"]
        items = []
        for phrase, slug in BASIC_ASSUMPTIONS[u["unit_no"]]:
            if phrase not in text:
                errors.append(f"Ünite {u['unit_no']} temel kabul ifadesi resmî metinde yok: '{phrase}'")
            items.append({"phrase": phrase, "concept_id": f"phys11-c-{slug}" if slug else None})
        assumptions[u["unit_no"]] = {"official_text": text, "items": items}

    # --- 1. 11. sınıf içi bağımlılık
    home = {}
    for c in cdoc["concepts"]:
        if c["origin_grade"] == "11" and c["learning_outcome_links"]:
            home[c["id"]] = min((l["learning_outcome"] for l in c["learning_outcome_links"]), key=order.get)
    req = defaultdict(list)
    for r in rdoc["relations"]:
        if r["type"] in ("REQUIRES", "SPECIAL_CASE_OF"):
            req[r["source"]].append(r["target"])
    lo_edges = defaultdict(list)  # A -> [(B, via)]
    for o in los:
        a = o["official_code"]
        for c in o["concepts"]:
            for t in req.get(c, []):
                b = home.get(t)
                if b and b != a:
                    lo_edges[a].append((b, f"{concepts[c]['slug']} → {concepts[t]['slug']}"))
    edge_list = []
    for a, lst in lo_edges.items():
        for b in sorted({x for x, _ in lst}, key=order.get):
            via = sorted({v for x, v in lst if x == b})
            forward = order[b] > order[a]
            if forward:
                warnings.append(f"İleri bağımlılık: {a} → {b} (program sırasında sonra gelen çıktıyı gerektiriyor; via {via})")
            edge_list.append({"from": a, "to": b, "type": "REQUIRES_OUTCOME", "via_concepts": via,
                              "forward_in_program_order": forward, "derived": True, "confidence": "MEDIUM"})
    cyc = find_cycle([(e["from"], e["to"]) for e in edge_list])
    if cyc:
        errors.append("Çıktı düzeyinde döngü: " + " → ".join(cyc))

    # --- çıktılara yaz
    for o in los:
        code = o["official_code"]
        unit = int(code.split(".")[2])
        pre = [{"type": "learning_outcome", "grade": 11, "code": e["to"], "id": by_code[e["to"]]["id"],
                "via_concepts": e["via_concepts"], "confidence": "MEDIUM", "derived_from": "concept_graph"}
               for e in edge_list if e["from"] == code]
        seen = set()
        for pc in o.get("prior_concepts", []):
            c = concepts[pc]
            if c["type"] == "math":
                continue
            for l in prior_links.get(pc, []):
                key = (l["code"], pc)
                if key not in seen:
                    seen.add(key)
                    pre.append({"type": "learning_outcome", "grade": l["grade"], "code": l["code"],
                                "via_concepts": [c["slug"]], "confidence": l["confidence"],
                                "derived_from": "prior_concept_mapping"})
            if c["origin_grade"] == "ortaokul":
                pre.append({"type": "external_prior_knowledge", "grade": "ortaokul", "concept_id": pc,
                            "via_concepts": [c["slug"]], "confidence": "MEDIUM",
                            "derived_from": "official_basic_assumption" if any(
                                i["concept_id"] == pc for i in assumptions[unit]["items"]) else "concept_origin"})
        o["prerequisites"] = pre
        o["unit_basic_assumptions"] = assumptions[unit]
        math = [pc for pc in o.get("prior_concepts", []) if concepts[pc]["type"] == "math"]
        o["mathematical_prerequisites"] = [{"concept_id": m, "name": concepts[m]["name"],
                                            "note": MATH_NOTES.get(concepts[m]["slug"]), "official_code": None,
                                            "confidence": "MEDIUM"} for m in math]
        o["pending_fields"] = [f for f in o["pending_fields"] if f not in ("prerequisites", "mathematical_prerequisites")]

    OUT.mkdir(exist_ok=True)
    graph = {"subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION,
             "generated_by": "scripts/build_prerequisites.py", "generated_at": TODAY,
             "intra_grade_outcome_edges": edge_list,
             "prior_concept_to_outcome": {k: v for k, v in prior_links.items()},
             "unit_basic_assumptions": assumptions,
             "prior_outcomes_catalog": {k: {x: v[x] for x in ("grade", "official_text", "unit_file")}
                                        for k, v in sorted(prior.items())},
             "math_notes": MATH_NOTES}
    (OUT / "prerequisite-graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    (KB / "learning-outcomes" / "learning-outcomes.json").write_text(json.dumps(lo_doc, ensure_ascii=False, indent=2), encoding="utf-8")
    write_md(los, edge_list, prior_links, assumptions, concepts, prior)

    n_prior = sum(len(v) for v in prior_links.values())
    print(f"önceki sınıf çıktı kataloğu: {len(prior)} (9. sınıf {sum(1 for p in prior.values() if p['grade']==9)}, "
          f"10. sınıf {sum(1 for p in prior.values() if p['grade']==10)})")
    print(f"ön koşul kavramı → önceki çıktı eşlemesi: {n_prior} "
          f"(resmî metinde kanıtlı {sum(1 for v in prior_links.values() for l in v if l['evidence']=='official_outcome_text')}, "
          f"uygulamada {sum(1 for v in prior_links.values() for l in v if l['evidence']=='official_teaching_practice')})")
    print(f"11. sınıf içi çıktı bağımlılığı: {len(edge_list)} kenar, ileri bağımlılık "
          f"{sum(e['forward_in_program_order'] for e in edge_list)}")
    print(f"önceki sınıf çıktısına bağlanan 11. sınıf çıktısı: "
          f"{sum(1 for o in los if any(p['grade'] in (9, 10) for p in o['prerequisites']))}/{len(los)}")
    for w in warnings:
        print("UYARI:", w)
    for e in errors:
        print("HATA:", e)
    return 1 if errors else 0


def write_md(los, edges, prior_links, assumptions, concepts, prior):
    L = ["# 11. Sınıf Fizik — Ön Koşul Grafiği", "",
         "> Otomatik üretildi: `scripts/build_prerequisites.py`. Elle düzenleme yapma.", "",
         "Üç katman: (1) 11. sınıf içi çıktı bağımlılıkları — kavram grafiğinden türetilir; "
         "(2) 9–10. sınıf resmî çıktıları — her eşleme resmî metinde doğrulanır; "
         "(3) ortaokul ve matematik — resmî temel kabullerden, kodsuz.", ""]
    for unit in (1, 2, 3):
        codes = [o["official_code"] for o in los if o["official_code"].startswith(f"FİZ.11.{unit}.")]
        L += [f"## Ünite {unit}", "", f"**Temel kabuller (resmî):** {assumptions[unit]['official_text']}", "",
              "```mermaid", "flowchart TB"]
        for c in codes:
            L.append(f'  {c.replace("İ", "I").replace(".", "_")}["{c}"]')
        for e in edges:
            if e["from"] in codes:
                a, b = e["from"].replace("İ", "I").replace(".", "_"), e["to"].replace("İ", "I").replace(".", "_")
                if e["to"] not in codes:
                    L.append(f'  {b}["{e["to"]}"]')
                L.append(f"  {b} --> {a}")
        L += ["```", "", "Ok yönü: önce öğrenilmesi gereken → sonra gelen.", "",
              "| Çıktı | 11. sınıf ön koşul çıktıları | 9–10. sınıf ön koşulları | Ortaokul / matematik |", "|---|---|---|---|"]
        for o in los:
            if o["official_code"] not in codes:
                continue
            p11 = ", ".join(sorted({p["code"] for p in o["prerequisites"] if p.get("grade") == 11}))
            p910 = ", ".join(sorted({p["code"] for p in o["prerequisites"] if p.get("grade") in (9, 10)}))
            ext = sorted({concepts[p["concept_id"]]["name"] for p in o["prerequisites"] if p["type"] == "external_prior_knowledge"}
                         | {m["name"] for m in o["mathematical_prerequisites"]})
            L.append(f"| {o['official_code']} | {p11 or '—'} | {p910 or '—'} | {', '.join(ext) or '—'} |")
        L.append("")
    L += ["## Kullanılan 9–10. sınıf çıktıları", "", "| Kod | Resmî metin |", "|---|---|"]
    used = sorted({l["code"] for v in prior_links.values() for l in v}, key=lambda c: [int(x) for x in c.split(".")[1:]])
    for c in used:
        L.append(f"| {c} | {prior[c]['official_text']} |")
    (OUT / "prerequisites.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
