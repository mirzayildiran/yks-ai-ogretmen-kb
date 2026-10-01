"""STEP 5: kavram grafiğini üretir ve doğrular.

Girdi : scripts/data_concepts.py (elle yazılmış kavram + ilişki listesi)
Çıktı : knowledge-base/physics-11/concepts/concepts.json
        knowledge-base/physics-11/concepts/relations.json
        knowledge-base/physics-11/concepts/concept-graph.md
        learning-outcomes.json -> her çıktının `concepts` alanı

Kontroller (hata → çıkış kodu 1):
  - yinelenen kavram, kırık ilişki ucu, öz-döngü, yinelenen kenar, REQUIRES döngüsü
  - programın 36 resmî anahtar kavramının her biri tam bir kavrama eşlenmiş mi
  - her öğrenme çıktısında en az bir 11. sınıf kavramı var mı
Uyarılar:
  - kavram–çıktı bağlantısı resmî metinde ya da ilgili ders kitabı bölümünde kanıtlanamıyorsa
"""
import json
import re
from collections import Counter, defaultdict

from build_curriculum import KB, TODAY, CURRICULUM_VERSION, letters_only
from data_concepts import CONCEPTS, RELATIONS
from enrich_learning_outcomes import TEXTBOOK, book_pages

OUT = KB / "concepts"
UNIT_END = {1: 120, 2: 274, 3: 391}  # ünite ölçme-değerlendirme bölümünün başladığı sayfa
TYPES = {"REQUIRES", "PART_OF", "SPECIAL_CASE_OF", "CAUSES", "USED_IN", "RELATED_TO"}


def cid(slug):
    return f"phys11-c-{slug}"


def section_pages():
    starts = sorted((p, code) for code, (_, _, p) in TEXTBOOK.items())
    ranges = {}
    for i, (p, code) in enumerate(starts):
        unit = int(code.split(".")[2])
        nxt = starts[i + 1][0] if i + 1 < len(starts) and int(starts[i + 1][1].split(".")[2]) == unit else UNIT_END[unit]
        ranges[code] = range(p, nxt)
    return ranges


def find_cycle(edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    state = {}

    def dfs(n, path):
        state[n] = 1
        for m in graph[n]:
            if state.get(m) == 1:
                return path + [n, m]
            if m not in state:
                c = dfs(m, path + [n])
                if c:
                    return c
        state[n] = 2
        return None

    for n in list(graph):
        if n not in state:
            c = dfs(n, [])
            if c:
                return c
    return None


def main():
    lo_doc = json.loads((KB / "learning-outcomes" / "learning-outcomes.json").read_text(encoding="utf-8"))
    cur = json.loads((KB / "curriculum" / "curriculum.json").read_text(encoding="utf-8"))
    los = {o["official_code"]: o for o in lo_doc["learning_outcomes"]}
    pages = {k: letters_only(v) for k, v in book_pages().items()}
    ranges = section_pages()
    errors, warnings = [], []

    # --- kavramlar
    slugs = [c[0] for c in CONCEPTS]
    for s, n in Counter(slugs).items():
        if n > 1:
            errors.append(f"Yinelenen kavram: {s}")
    official = {}
    for u in cur["units"]:
        for k in u["key_concepts_official"]:
            official[k] = u["unit_no"]
    mapped = defaultdict(list)
    concepts = []
    for (slug, name, typ, origin, key, lo_codes, sym, unit, terms, definition) in CONCEPTS:
        if key:
            mapped[key].append(slug)
            if key not in official:
                errors.append(f"{slug}: resmî anahtar kavram listesinde olmayan ifade: '{key}'")
        links = []
        for code in lo_codes:
            if code not in los:
                errors.append(f"{slug}: bilinmeyen öğrenme çıktısı {code}")
                continue
            o = los[code]
            official_txt = letters_only(" ".join([o["official_text"]] + [c["official_text"] for c in o["process_components"]]))
            practice_txt = letters_only(o["official_teaching_practice"])
            ev = []
            for t in terms:
                lt = letters_only(t)
                if lt in official_txt:
                    ev.append({"where": "official_outcome_text", "term": t})
                elif lt in practice_txt:
                    ev.append({"where": "official_teaching_practice", "term": t})
                else:
                    pg = [p for p in ranges[code] if lt in pages.get(p, "")]
                    if pg:
                        ev.append({"where": "textbook_section", "term": t, "pages": pg[:5]})
            strength = ("official" if any(e["where"].startswith("official") for e in ev)
                        else "textbook" if ev else "none")
            if strength == "none":
                warnings.append(f"Kanıtsız bağlantı: {slug} → {code} (terimler: {terms})")
            links.append({"learning_outcome": code, "learning_outcome_id": o["id"],
                          "evidence_strength": strength, "evidence": ev[:3]})
        concepts.append({
            "id": cid(slug), "slug": slug, "name": name, "type": typ,
            "origin_grade": origin, "is_prior_knowledge": origin != "11",
            "official_key_concept": key, "official_key_concept_unit": official.get(key) if key else None,
            "symbol": sym, "si_unit": unit,
            "short_definition": definition,
            "definition_status": "ai_authored_pending_expert_review",
            "learning_outcome_links": links,
            "match_terms": terms,
            # Sesli öğretmen için planlanan alanlar (sonraki aşama)
            "short_explanation": None, "normal_explanation": None, "deep_explanation": None,
            "teacher_dialogue": None, "common_student_question": None,
            "curriculum_version": CURRICULUM_VERSION,
            "sources": ["src-meb-fizik-op-2026", "src-meb-fiz11-ders-kitabi"],
            "confidence": "HIGH" if key else "MEDIUM",
            "confidence_note": ("Resmî anahtar kavram." if key else
                                "Kavram listesi ve tanım bizim tarafımızdan yazıldı; bağlantı kanıtı evidence alanında."),
            "created_at": TODAY, "updated_at": TODAY,
        })
    for k in official:
        if len(mapped.get(k, [])) != 1:
            errors.append(f"Resmî anahtar kavram '{k}' {len(mapped.get(k, []))} kavrama eşlendi (1 olmalı)")

    # --- ilişkiler
    sset = set(slugs)
    seen = set()
    rels = []
    for i, (a, t, b, why) in enumerate(RELATIONS, 1):
        if t not in TYPES:
            errors.append(f"Geçersiz ilişki türü: {t}")
        for x in (a, b):
            if x not in sset:
                errors.append(f"Kırık ilişki ucu: {x} ({a} {t} {b})")
        if a == b:
            errors.append(f"Öz-döngü: {a}")
        if (a, t, b) in seen:
            errors.append(f"Yinelenen ilişki: {a} {t} {b}")
        seen.add((a, t, b))
        rels.append({"id": f"phys11-rel-{i:03d}", "source": cid(a), "type": t, "target": cid(b), "rationale": why,
                     "confidence": "MEDIUM", "status": "ai_authored_pending_expert_review"})
    cyc = find_cycle([(a, b) for a, t, b, _ in RELATIONS if t == "REQUIRES"])
    if cyc:
        errors.append("REQUIRES döngüsü: " + " → ".join(cyc))
    hier = find_cycle([(a, b) for a, t, b, _ in RELATIONS if t in ("PART_OF", "SPECIAL_CASE_OF")])
    if hier:
        errors.append("PART_OF/SPECIAL_CASE_OF döngüsü: " + " → ".join(hier))
    degree = Counter([a for a, *_ in RELATIONS] + [b for _, _, b, _ in RELATIONS])
    for s in slugs:
        if degree[s] == 0:
            warnings.append(f"İlişkisiz (yetim) kavram: {s}")

    # --- çıktılara kavram bağla
    by_lo = defaultdict(list)
    for c in concepts:
        for l in c["learning_outcome_links"]:
            by_lo[l["learning_outcome"]].append(c)
    for code, o in los.items():
        cs = by_lo.get(code, [])
        if not any(c["origin_grade"] == "11" for c in cs):
            errors.append(f"{code}: 11. sınıf kavramı bağlı değil")
        o["concepts"] = [c["id"] for c in cs if c["origin_grade"] == "11"]
        o["prior_concepts"] = [c["id"] for c in cs if c["origin_grade"] != "11"]
        o["pending_fields"] = [f for f in o["pending_fields"] if f != "concepts"]
        if not any(s["source_id"] == "phys11-concepts" for s in o["sources"]):
            pass

    OUT.mkdir(exist_ok=True)
    meta = {"subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION,
            "generated_by": "scripts/build_concepts.py", "generated_at": TODAY}
    (OUT / "concepts.json").write_text(json.dumps({**meta, "count": len(concepts), "concepts": concepts},
                                                  ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "relations.json").write_text(json.dumps({
        **meta, "count": len(rels),
        "relation_types": {"REQUIRES": "A'yı anlamak için B gerekir (tersi PREREQUISITE_OF, türetilir, saklanmaz)",
                           "PART_OF": "A, B'nin parçası/öğesidir", "SPECIAL_CASE_OF": "A, B'nin özel durumudur",
                           "CAUSES": "A, B'yi oluşturur/doğurur", "USED_IN": "A, B'de araç olarak kullanılır",
                           "RELATED_TO": "Yönsüz ilgi (karşılaştırma, karıştırılma, analoji)"},
        "relations": rels}, ensure_ascii=False, indent=2), encoding="utf-8")
    (KB / "learning-outcomes" / "learning-outcomes.json").write_text(json.dumps(lo_doc, ensure_ascii=False, indent=2), encoding="utf-8")
    write_graph_md(concepts, rels, cur, by_lo)

    print(f"{len(concepts)} kavram ({sum(1 for c in concepts if c['origin_grade']=='11')} 11. sınıf, "
          f"{sum(1 for c in concepts if c['origin_grade']!='11')} ön koşul), {len(rels)} ilişki")
    print("ilişki türleri:", dict(Counter(r["type"] for r in rels)))
    print(f"resmî anahtar kavram eşlemesi: {sum(1 for k in official if len(mapped.get(k, [])) == 1)}/{len(official)}")
    ev = Counter(l["evidence_strength"] for c in concepts for l in c["learning_outcome_links"])
    print("kavram–çıktı bağlantı kanıtı:", dict(ev))
    for w in warnings:
        print("UYARI:", w)
    for e in errors:
        print("HATA:", e)
    return 1 if errors else 0


def write_graph_md(concepts, rels, cur, by_lo):
    by_id = {c["id"]: c for c in concepts}
    L = ["# 11. Sınıf Fizik — Kavram Grafiği", "",
         "> Otomatik üretildi: `scripts/build_concepts.py` (kaynak veri: `scripts/data_concepts.py`). Elle düzenleme yapma.", "",
         f"- **Kavram:** {len(concepts)} ({sum(1 for c in concepts if c['origin_grade']=='11')} 11. sınıf, "
         f"{sum(1 for c in concepts if c['origin_grade']!='11')} ön koşul)",
         f"- **İlişki:** {len(rels)}",
         "- Kavram tanımları ve ilişkiler yapay zekâ tarafından yazıldı, **uzman incelemesi bekliyor** (güven: MEDIUM). "
         "Resmî anahtar kavramlar HIGH.", "",
         "Okuma: `A --> B` = A, B'yi gerektirir (REQUIRES). Kesikli ok: özel durum / parçası.", ""]
    for u in cur["units"]:
        codes = [f"FİZ.11.{u['unit_no']}.{i}" for i in range(1, len(u["learning_outcome_ids"]) + 1)]
        ids = {c["id"] for code in codes for c in by_lo.get(code, [])}
        L += [f"## Ünite {u['unit_no']}: {u['official_title']}", "", "```mermaid", "flowchart LR"]
        for i in sorted(ids):
            c = by_id[i]
            label = c["name"].replace('"', "'")
            shape = f'(["{label}"])' if c["is_prior_knowledge"] else f'["{label}"]'
            L.append(f"  {c['slug'].replace('-', '_')}{shape}")
        for r in rels:
            if r["source"] in ids and r["target"] in ids and r["type"] in ("REQUIRES", "PART_OF", "SPECIAL_CASE_OF", "CAUSES"):
                a, b = by_id[r["source"]]["slug"].replace("-", "_"), by_id[r["target"]]["slug"].replace("-", "_")
                arrow = {"REQUIRES": "-->", "PART_OF": "-.->|parçası|", "SPECIAL_CASE_OF": "-.->|özel durum|",
                         "CAUSES": "==>|oluşturur|"}[r["type"]]
                L.append(f"  {a} {arrow} {b}")
        L += ["```", "", "Yuvarlak kutu = önceki sınıflardan gelen ön koşul kavramı.", "",
              "| Öğrenme çıktısı | 11. sınıf kavramları | Ön koşul kavramları |", "|---|---|---|"]
        for code in codes:
            cs = by_lo.get(code, [])
            L.append(f"| {code} | {', '.join(c['name'] for c in cs if not c['is_prior_knowledge'])} | "
                     f"{', '.join(c['name'] for c in cs if c['is_prior_knowledge'])} |")
        L.append("")
    (OUT / "concept-graph.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
