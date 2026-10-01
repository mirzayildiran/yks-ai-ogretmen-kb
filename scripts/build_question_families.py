"""STEP 8: soru ailesi ontolojisini üretir ve doğrular.

Girdi : scripts/data_question_families_u*.py
Çıktı : knowledge-base/physics-11/question-families/{question-families.json, question-families.md, coverage.md}
        learning-outcomes.json -> question_families

Kontroller (hata → çıkış kodu 1):
  - süreç bileşeni, kavram, formül referansları çözülüyor; yinelenen slug yok
  - kanıt: kitap anahtarı ilgili sayfada geçiyor; program anchor'ı ilgili çıktının resmî metninde geçiyor
  - çeldirici ve öğrenci hatası alanları dolu; hata türü kodları tanımlı
  - kapsamdaki (CORE) her öğrenme çıktısının ve her süreç bileşeninin en az bir ailesi var
Uyarılar: çıktı başına grafik / tablo / deney / günlük hayat uyarıcısı eksikliği
"""
import importlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from build_curriculum import KB, TODAY, CURRICULUM_VERSION, letters_only
from enrich_learning_outcomes import book_pages

OUT = KB / "question-families"
# Varsayılan: mevcut tüm ünite modülleri. Komut satırı: python3 build_question_families.py [--check] [modül ...]
#   --check : yalnız doğrular, hiçbir dosya yazmaz (paralel çalışan ajanlar için)
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
CHECK_ONLY = "--check" in sys.argv
MODULES = ARGS or sorted(p.stem for p in Path(__file__).parent.glob("data_question_families_u*.py"))
UNITS = {m: int(m.rsplit("_u", 1)[1]) for m in MODULES}
ERROR_TYPES = {"CONCEPTUAL_ERROR", "FORMULA_SELECTION_ERROR", "FORMULA_APPLICATION_ERROR", "SIGN_ERROR", "UNIT_ERROR",
               "VECTOR_ERROR", "GRAPH_READING_ERROR", "TABLE_READING_ERROR", "ALGEBRA_ERROR", "ARITHMETIC_ERROR",
               "QUESTION_INTERPRETATION_ERROR", "METHOD_SELECTION_ERROR", "PREREQUISITE_GAP", "CARELESS_ERROR"}
STIMULI = {"TEXT", "DIAGRAM", "GRAPH", "TABLE", "EXPERIMENT", "DAILY_LIFE_CONTEXT", "DATA_SET"}
KINDS = {"common", "graph", "table", "experimental", "daily_life"}
SCOPES = {"CORE", "ENRICHMENT", "OUT_OF_SCOPE_CALC"}
KIL_PAGES = 123


def main():
    lo_doc = json.loads((KB / "learning-outcomes" / "learning-outcomes.json").read_text(encoding="utf-8"))
    los = {o["official_code"]: o for o in lo_doc["learning_outcomes"]}
    concepts = {c["slug"]: c["id"] for c in json.loads((KB / "concepts" / "concepts.json").read_text(encoding="utf-8"))["concepts"]}
    fdoc = json.loads((KB / "formulas" / "formulas.json").read_text(encoding="utf-8"))
    formulas = {f["slug"]: f for f in fdoc["formulas"]}
    pages = {k: letters_only(v) for k, v in book_pages().items()}
    errors, warnings, out = [], [], []
    units_done = set()

    families = []
    for m in MODULES:
        mod = importlib.import_module(m)
        units_done.add(UNITS[m])
        families += mod.FAMILIES
    for s, n in Counter(f["slug"] for f in families).items():
        if n > 1:
            errors.append(f"Yinelenen aile: {s}")

    for i, f in enumerate(families, 1):
        fid = f"phys11-qf-{i:03d}"
        comps, lo_codes = [], []
        for ref in f["components"]:
            code, label = ref.split(":")
            o = los.get(code)
            c = next((c for c in o["process_components"] if c["label"] == label), None) if o else None
            if not c:
                errors.append(f"{f['slug']}: bilinmeyen süreç bileşeni {ref}")
                continue
            comps.append({"component_id": c["id"], "official_code": code, "label": label,
                          "skill_component": c["skill_component"]["code"], "official_text": c["official_text"]})
            if code not in lo_codes:
                lo_codes.append(code)
        for c in f["concepts"]:
            if c not in concepts:
                errors.append(f"{f['slug']}: bilinmeyen kavram {c}")
        for fs in f["formulas"]:
            if fs not in formulas:
                errors.append(f"{f['slug']}: bilinmeyen formül {fs}")
        for s in f["stimulus"]:
            if s not in STIMULI:
                errors.append(f"{f['slug']}: geçersiz uyarıcı türü {s}")
        for v in f["variations"]:
            if v["kind"] not in KINDS:
                errors.append(f"{f['slug']}: geçersiz varyasyon türü {v['kind']}")
        if not f["distractors"]:
            errors.append(f"{f['slug']}: çeldirici yok")
        if not f["errors"]:
            errors.append(f"{f['slug']}: öğrenci hatası yok")
        for e in f["errors"]:
            if e["error_type"] not in ERROR_TYPES:
                errors.append(f"{f['slug']}: tanımsız hata türü {e['error_type']}")
        if f["scope"] not in SCOPES:
            errors.append(f"{f['slug']}: geçersiz kapsam {f['scope']}")

        evidence = []
        for ev in f["evidence"]:
            if ev[0] == "tb":
                _, page, item, key = ev
                ok = letters_only(key) in pages.get(page, "")
                if not ok:
                    errors.append(f"{f['slug']}: kitap kanıtı doğrulanamadı s.{page} '{key}'")
                evidence.append({"source_id": "src-meb-fiz11-ders-kitabi", "printed_page": page, "item": item,
                                 "verified_keyword": key, "verified": ok})
            elif ev[0] == "prog":
                anchor = ev[1]
                hit = [c for c in lo_codes if anchor in los[c]["official_teaching_practice"]
                       or any(anchor in x["official_text"] for x in los[c]["process_components"])]
                if not hit:
                    errors.append(f"{f['slug']}: program anchor'ı ilgili çıktılarda yok: '{anchor}'")
                evidence.append({"source_id": "src-meb-fizik-op-2026", "anchor": anchor, "outcomes": hit, "verified": bool(hit)})
            elif ev[0] == "kil":
                ok = 1 <= ev[1] <= KIL_PAGES
                evidence.append({"source_id": "src-tymm-soru-yazim-kilavuzu", "printed_page": ev[1], "verified": ok,
                                 "note": "yöntem ilkesi"})
            else:
                errors.append(f"{f['slug']}: bilinmeyen kanıt türü {ev[0]}")

        calc = sorted({formulas[x]["program_calc_status"] for x in f["formulas"] if x in formulas})
        conflict = any(formulas[x]["textbook_vs_program_conflict"] for x in f["formulas"] if x in formulas)
        out.append({
            "id": fid, "slug": f["slug"], "name": f["name"],
            "learning_outcomes": lo_codes, "learning_outcome_ids": [los[c]["id"] for c in lo_codes],
            "process_components": comps,
            "skills": sorted({c["skill_component"].rsplit(".SB", 1)[0] for c in comps}),
            "concepts": [concepts[c] for c in f["concepts"] if c in concepts],
            "prerequisites": sorted({p for c in lo_codes for p in los[c].get("prior_concepts", [])}),
            "formulas": [formulas[x]["id"] for x in f["formulas"] if x in formulas],
            "difficulty": f["difficulty"],
            "question_structure": f["structure"],
            "stimulus_types": f["stimulus"],
            "variables": {"given": f["given"], "asked": f["asked"]},
            "common_variations": [v["text"] for v in f["variations"] if v["kind"] == "common"],
            "graph_variations": [v["text"] for v in f["variations"] if v["kind"] == "graph"],
            "table_variations": [v["text"] for v in f["variations"] if v["kind"] == "table"],
            "experimental_variations": [v["text"] for v in f["variations"] if v["kind"] == "experimental"],
            "daily_life_variations": [v["text"] for v in f["variations"] if v["kind"] == "daily_life"],
            "osym_like_characteristics": [], "osym_status": "pending_STEP_10",
            "market_evidence": [], "market_status": "pending_STEP_9",
            "common_distractors": f["distractors"],
            "common_student_errors": f["errors"],
            "solution_methods": f["methods"], "solution_methods_status": "summary_only_detail_in_STEP_11",
            "shortcuts": f["shortcuts"], "shortcuts_status": "names_only_detail_in_STEP_12",
            "scope": f["scope"], "scope_note": f["scope_note"],
            "program_calc_status": calc, "textbook_vs_program_conflict": conflict,
            "sources": evidence,
            "curriculum_version": CURRICULUM_VERSION,
            "confidence": "MEDIUM", "review_status": "ai_authored_pending_expert_review",
            "created_at": TODAY, "updated_at": TODAY,
        })

    # kapsam: işlenen ünitelerde her çıktı ve süreç bileşeni
    by_lo, by_comp = defaultdict(list), defaultdict(list)
    for q in out:
        if q["scope"] != "CORE":
            continue
        for c in q["learning_outcomes"]:
            by_lo[c].append(q)
        for c in q["process_components"]:
            by_comp[c["component_id"]].append(q["id"])
    coverage = []
    for code, o in los.items():
        unit = int(code.split(".")[2])
        if unit not in units_done:
            continue
        fams = by_lo.get(code, [])
        if not fams:
            errors.append(f"{code}: kapsamdaki soru ailesi yok")
        for c in o["process_components"]:
            if not by_comp.get(c["id"]):
                errors.append(f"{c['id']} ({code} {c['label']}): hiçbir aile bu süreç bileşenini ölçmüyor")
        st = Counter(s for q in fams for s in q["stimulus_types"])
        missing = [s for s in ("GRAPH", "TABLE", "EXPERIMENT", "DAILY_LIFE_CONTEXT") if not st[s]]
        if missing:
            warnings.append(f"{code}: uyarıcı türü yok → {', '.join(missing)}")
        coverage.append({"code": code, "families": len(fams), "stimuli": dict(st), "missing_stimuli": missing})
        o["question_families"] = [q["id"] for q in out if code in q["learning_outcomes"]]
    for code, o in los.items():
        if int(code.split(".")[2]) not in units_done:
            o["question_families"] = []

    if CHECK_ONLY:
        print("(--check: dosya yazılmadı)")
    else:
        write_all(out, lo_doc, coverage, units_done)
    report(out, by_comp, warnings, errors, units_done)
    return 1 if errors else 0


def write_all(out, lo_doc, coverage, units_done):
    OUT.mkdir(exist_ok=True)
    (OUT / "question-families.json").write_text(json.dumps({
        "subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION,
        "generated_by": "scripts/build_question_families.py", "generated_at": TODAY,
        "units_covered": sorted(units_done),
        "design_principles_source": "src-tymm-soru-yazim-kilavuzu (s. 16-24)",
        "count": len(out), "question_families": out}, ensure_ascii=False, indent=2), encoding="utf-8")
    (KB / "learning-outcomes" / "learning-outcomes.json").write_text(json.dumps(lo_doc, ensure_ascii=False, indent=2), encoding="utf-8")
    write_md(out, coverage)


def report(out, by_comp, warnings, errors, units_done):
    print(f"{len(out)} soru ailesi (ünite {sorted(units_done)}); kapsam: {dict(Counter(q['scope'] for q in out))}")
    print(f"kitap kanıtı: {sum(e['verified'] for q in out for e in q['sources'] if 'item' in e)}/"
          f"{sum(1 for q in out for e in q['sources'] if 'item' in e)} doğrulandı; "
          f"program kanıtı: {sum(e['verified'] for q in out for e in q['sources'] if 'anchor' in e)}/"
          f"{sum(1 for q in out for e in q['sources'] if 'anchor' in e)}")
    print(f"süreç bileşeni kapsamı: {sum(1 for c in by_comp if by_comp[c])} bileşen ölçülüyor")
    print("uyarıcı türleri:", dict(Counter(s for q in out for s in q["stimulus_types"])))
    print("zorluk aralıkları:", dict(Counter(q["difficulty"]["range"][-1] for q in out)))
    print(f"kitap–program çelişkili formül kullanan aile: {sum(q['textbook_vs_program_conflict'] for q in out)}")
    for w in warnings:
        print("UYARI:", w)
    for e in errors:
        print("HATA:", e)


def write_md(out, coverage):
    L = ["# 11. Sınıf Fizik — Soru Aileleri", "",
         "> Otomatik üretildi: `scripts/build_question_families.py`. Elle düzenleme yapma.", "",
         "Soru ailesi = aynı fiziksel durum + aynı ölçülen süreç bileşeni + aynı çözüm mantığı. Sayılar ve bağlam değişince aile değişmez.",
         "Her ailenin ölçtüğü süreç bileşeni MEB Soru Yazım Kılavuzu'ndaki gibi beceri koduyla etiketlidir (ör. `FBAB10.SB1`).",
         "Piyasa (STEP 9) ve ÖSYM (STEP 10) kanıtları henüz eklenmedi.", ""]
    cur = None
    for q in out:
        unit_lo = q["learning_outcomes"][0]
        if unit_lo != cur:
            cur = unit_lo
            L += [f"## {unit_lo}", ""]
        sc = {"CORE": "", "ENRICHMENT": " · **zenginleştirme**", "OUT_OF_SCOPE_CALC": " · **hesap kapsam dışı**"}[q["scope"]]
        cf = " · ⚠️ kitap–program çelişkili formül" if q["textbook_vs_program_conflict"] else ""
        L += [f"### {q['id'][-3:]} · {q['name']}{sc}{cf}", "",
              f"- **Ölçülen:** {', '.join(c['official_code'] + ' ' + c['label'] + ' `' + c['skill_component'] + '`' for c in q['process_components'])}",
              f"- **Yapı:** {q['question_structure']}",
              f"- **Uyarıcı:** {', '.join(q['stimulus_types'])} · **Zorluk:** {'–'.join(q['difficulty']['range'])}",
              f"- **Çeldiriciler:** " + "; ".join(f"“{d['distractor_logic']}” ({d['targets']})" for d in q["common_distractors"]),
              f"- **Öğrenci hataları:** " + "; ".join(f"{e['error']} `{e['error_type']}`" for e in q["common_student_errors"]),
              f"- **Kanıt:** " + "; ".join(
                  (f"kitap s.{e['printed_page']} {e['item']}" if "item" in e else
                   f"program “{e['anchor'][:50]}…”" if "anchor" in e else f"kılavuz s.{e['printed_page']}")
                  for e in q["sources"]), ""]
        if q["scope_note"]:
            L.insert(len(L) - 1, f"- **Kapsam notu:** {q['scope_note']}")
    (OUT / "question-families.md").write_text("\n".join(L), encoding="utf-8")
    C = ["# Soru Ailesi Kapsam Raporu", "", "| Çıktı | Aile | GRAPH | TABLE | EXPERIMENT | DAILY_LIFE | Eksik uyarıcı |", "|---|---|---|---|---|---|---|"]
    for c in coverage:
        s = c["stimuli"]
        C.append(f"| {c['code']} | {c['families']} | {s.get('GRAPH', 0)} | {s.get('TABLE', 0)} | {s.get('EXPERIMENT', 0)} | "
                 f"{s.get('DAILY_LIFE_CONTEXT', 0)} | {', '.join(c['missing_stimuli']) or '—'} |")
    (OUT / "coverage.md").write_text("\n".join(C) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
