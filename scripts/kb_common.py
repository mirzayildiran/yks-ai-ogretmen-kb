"""Derleyicilerin ortak yardımcıları: kimlik tabloları ve basit doğrulama."""
import importlib
import json
from pathlib import Path

from build_curriculum import KB

HERE = Path(__file__).resolve().parent
ERROR_CODES = {"CONCEPTUAL_ERROR", "FORMULA_SELECTION_ERROR", "FORMULA_APPLICATION_ERROR", "SIGN_ERROR", "UNIT_ERROR",
               "VECTOR_ERROR", "GRAPH_READING_ERROR", "TABLE_READING_ERROR", "ALGEBRA_ERROR", "ARITHMETIC_ERROR",
               "QUESTION_INTERPRETATION_ERROR", "METHOD_SELECTION_ERROR", "PREREQUISITE_GAP", "CARELESS_ERROR"}


def load_json(rel):
    return json.loads((KB / rel).read_text(encoding="utf-8"))


def lo_codes():
    return {o["official_code"]: o for o in load_json("learning-outcomes/learning-outcomes.json")["learning_outcomes"]}


def concept_slugs():
    return {c["slug"]: c["id"] for c in load_json("concepts/concepts.json")["concepts"]}


def formula_slugs():
    return {f["slug"]: f["id"] for f in load_json("formulas/formulas.json")["formulas"]}


def skill_codes():
    return {s["official_code"] for s in load_json("learning-outcomes/skills.json")["skills"]}


def family_slugs():
    """Tüm ünite modüllerindeki soru ailesi slug'ları (derlenmiş JSON'dan bağımsız)."""
    out = {}
    for p in sorted(HERE.glob("data_question_families_u*.py")):
        try:
            mod = importlib.import_module(p.stem)
        except Exception as e:  # başka bir ajan dosyayı o anda yazıyor olabilir
            print(f"UYARI: {p.name} içe aktarılamadı ({type(e).__name__}); aileleri atlandı")
            continue
        for f in mod.FAMILIES:
            out[f["slug"]] = p.stem
    return out


def write_json(rel, obj):
    path = KB / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def report(title, errors, warnings, lines=()):
    print(title)
    for l in lines:
        print(" ", l)
    for w in warnings:
        print("UYARI:", w)
    for e in errors:
        print("HATA:", e)
    return 1 if errors else 0
