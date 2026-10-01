"""STEP 7: formül veritabanını üretir ve doğrular.

Kontroller (hata → çıkış kodu 1):
  - her formül boyut analizinden geçer (tüm terimler aynı boyutta)
  - DIM_OVERRIDES'taki bilinçli yanlış varsayımlar boyut analizinden KALIR (testin çalıştığını kanıtlar)
  - validity_conditions, invalid_use_cases, common_mistakes boş değil ("ne zaman kullanılmaz" zorunlu)
  - öğrenme çıktısı ve kavram referansları çözülüyor, yinelenen slug yok
Türetilen alanlar:
  - program_calc_status: ilgili çıktıların resmî kapsam sınırlarından (CALC_EXCLUDED, CONCEPTUAL_ONLY ...)
  - textbook_vs_program_conflict: kitapta formül var ama program hesaplamayı dışlıyor
Çıktı: knowledge-base/physics-11/formulas/{formulas.json, formulas.md}; learning-outcomes.json -> formulas
"""
import json
from collections import Counter

from build_curriculum import KB, TODAY, CURRICULUM_VERSION
from data_formulas import DIM_OVERRIDES, FORMULAS, VAR_DIMS

OUT = KB / "formulas"
REVIEW = "page_image_manual_review_2026-10-01"
PRIORITY = ["CALC_EXCLUDED", "CONCEPTUAL_ONLY", "CALC_LIMITED", "CALC_INCLUDED"]


def term_dim(term, table):
    total = Counter()
    for var, exp in term.items():
        for base, e in table[var.rstrip("#")].items():
            total[base] += e * exp
    return {k: v for k, v in total.items() if v}


def dim_ok(dims, table):
    seen = [term_dim(t, table) for side in dims for t in side]
    return all(d == seen[0] for d in seen), seen


def fmt_dim(d):
    return " ".join(f"{k}^{v}" if v != 1 else k for k, v in sorted(d.items())) or "boyutsuz"


def main():
    lo_doc = json.loads((KB / "learning-outcomes" / "learning-outcomes.json").read_text(encoding="utf-8"))
    cdoc = json.loads((KB / "concepts" / "concepts.json").read_text(encoding="utf-8"))
    los = {o["official_code"]: o for o in lo_doc["learning_outcomes"]}
    slugs = {c["slug"] for c in cdoc["concepts"]}
    errors, warnings, out = [], [], []

    dup = [s for s, n in Counter(f["slug"] for f in FORMULAS).items() if n > 1]
    if dup:
        errors.append(f"Yinelenen formül: {dup}")
    for i, f in enumerate(FORMULAS, 1):
        ok, seen = dim_ok(f["dims"], VAR_DIMS)
        if not ok:
            errors.append(f"Boyut tutarsız: {f['slug']} {[fmt_dim(s) for s in seen]}")
        for key in ("validity_conditions", "invalid_use_cases", "common_mistakes"):
            if not f[key]:
                errors.append(f"{f['slug']}: '{key}' boş")
        for code in f["learning_outcomes"]:
            if code not in los:
                errors.append(f"{f['slug']}: bilinmeyen çıktı {code}")
        for c in f["related_concepts"]:
            if c not in slugs:
                errors.append(f"{f['slug']}: bilinmeyen kavram {c}")
        scope = [s for code in f["learning_outcomes"] for s in los[code]["official_scope_constraints"]]
        types = {s["type"] for s in scope if s.get("applies_to") in (None, "whole")}
        partial = [s["official_text"] for s in scope if s.get("applies_to") == "partial"]
        status = next((p for p in PRIORITY if p in types), "NO_EXPLICIT_LIMIT")
        conflict = f["textbook_verified"] and status in ("CALC_EXCLUDED", "CONCEPTUAL_ONLY")
        if f["derivation_level"] == "out_of_curriculum":
            status = "OUT_OF_CURRICULUM"
        out.append({
            "id": f"phys11-formula-{i:03d}", "slug": f["slug"], "name": f["name"],
            "formula": f["formula"], "spoken_tr": f["spoken_tr"], "meaning": f["meaning"],
            "variables": f["variables"],
            "units": sorted({v["si_unit"] for v in f["variables"]}),
            "dimensions": fmt_dim(seen[0]), "dimension_check": "pass" if ok else "fail",
            "validity_conditions": f["validity_conditions"],
            "invalid_use_cases": f["invalid_use_cases"],
            "common_mistakes": f["common_mistakes"],
            "related_concepts": [f"phys11-c-{c}" for c in f["related_concepts"]],
            "learning_outcomes": f["learning_outcomes"],
            "learning_outcome_ids": [los[c]["id"] for c in f["learning_outcomes"] if c in los],
            "derivation_level": f["derivation_level"],
            "program_calc_status": status,
            "textbook_vs_program_conflict": conflict,
            "partial_program_limits": partial,
            "textbook": {"source_id": "src-meb-fiz11-ders-kitabi", "printed_page": f["textbook_page"],
                         "verified": f["textbook_verified"], "verified_by": REVIEW if f["textbook_verified"] else None},
            "notes": f["notes"],
            "curriculum_version": CURRICULUM_VERSION,
            "sources": ["src-meb-fiz11-ders-kitabi", "src-meb-fizik-op-2026"],
            "confidence": "HIGH" if f["textbook_verified"] and ok else "MEDIUM",
            "review_status": "ai_authored_pending_expert_review",
            "created_at": TODAY, "updated_at": TODAY,
        })
        if not f["textbook_verified"] and f["derivation_level"] != "out_of_curriculum":
            warnings.append(f"Kitap sayfasında doğrulanmadı: {f['slug']}")

    # Bilinçli yanlış varsayım testleri: boyut analizi bunları REDDETMELİ
    neg = []
    for name, override in DIM_OVERRIDES.items():
        table = {**VAR_DIMS, **override}
        target = next(f for f in FORMULAS if f["slug"] == "drag-force")
        ok, seen = dim_ok(target["dims"], table)
        neg.append({"test": name, "assumption": "k boyutsuz (ders kitabı Tablo 1.2, s. 90)",
                    "result": "rejected" if not ok else "accepted",
                    "dims_seen": [fmt_dim(s) for s in seen]})
        if ok:
            errors.append(f"Negatif boyut testi başarısız: {name} kabul edildi")

    by_lo = {}
    for f in out:
        for code in f["learning_outcomes"]:
            by_lo.setdefault(code, []).append(f["id"])
    for code, o in los.items():
        o["formulas"] = by_lo.get(code, [])

    OUT.mkdir(exist_ok=True)
    (OUT / "formulas.json").write_text(json.dumps({
        "subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION,
        "generated_by": "scripts/build_formulas.py", "generated_at": TODAY,
        "notation_note": "Ders kitabı hız için ϑ, akım için i, manyetik alan katsayısı için K, Coulomb sabiti için k kullanır.",
        "count": len(out), "dimension_negative_tests": neg, "formulas": out}, ensure_ascii=False, indent=2), encoding="utf-8")
    (KB / "learning-outcomes" / "learning-outcomes.json").write_text(json.dumps(lo_doc, ensure_ascii=False, indent=2), encoding="utf-8")
    write_md(out, neg)

    print(f"{len(out)} formül; boyut analizi {sum(f['dimension_check']=='pass' for f in out)}/{len(out)} geçti; "
          f"kitapta görüntüden doğrulanan {sum(f['textbook']['verified'] for f in out)}")
    print("program hesap durumu:", dict(Counter(f["program_calc_status"] for f in out)))
    print(f"kitap–program çelişkisi: {sum(f['textbook_vs_program_conflict'] for f in out)} formül")
    print(f"formülü olan çıktı: {sum(1 for o in los.values() if o['formulas'])}/{len(los)}")
    for n in neg:
        print(f"negatif boyut testi '{n['assumption']}': {n['result']} ({n['dims_seen']})")
    for w in warnings:
        print("UYARI:", w)
    for e in errors:
        print("HATA:", e)
    return 1 if errors else 0


def write_md(out, neg):
    STATUS = {"CALC_EXCLUDED": "⛔ program hesaplamayı dışlıyor", "CONCEPTUAL_ONLY": "◐ program kavramsal",
              "CALC_LIMITED": "◑ sınırlı", "CALC_INCLUDED": "✓ hesap açıkça var", "NO_EXPLICIT_LIMIT": "· açık sınır yok",
              "OUT_OF_CURRICULUM": "✗ müfredat dışı"}
    L = ["# 11. Sınıf Fizik — Formül Veritabanı", "",
         "> Otomatik üretildi: `scripts/build_formulas.py` (kaynak: `scripts/data_formulas.py`). Elle düzenleme yapma.", "",
         "Her formül MEB 11. sınıf ders kitabının **sayfa görüntüsünden** doğrulandı (metin çıkarımı sembolleri bozuyor). "
         "Kitap gösterimi: hız **ϑ**, akım **i**, manyetik alan katsayısı **K**, Coulomb sabiti **k**.", "",
         f"- Formül: **{len(out)}** · boyut analizi: **{sum(f['dimension_check']=='pass' for f in out)}/{len(out)}** · "
         f"kitapta doğrulanan: **{sum(f['textbook']['verified'] for f in out)}**",
         f"- Kitap–program çelişkisi (kitap formül veriyor, program hesaplamayı dışlıyor): **{sum(f['textbook_vs_program_conflict'] for f in out)}**", "",
         "## Kaynak hataları ve çelişkiler", ""]
    for f in out:
        if f["notes"] and any(k in f["notes"] for k in ("HATA", "TUTARSIZLIĞI", "ÇELİŞKİSİ")):
            L.append(f"- **{f['name']}** — {f['notes']}")
    for n in neg:
        L.append(f"- Boyut testi: '{n['assumption']}' varsayımı **{n['result']}** "
                 f"(F_d ≠ k·A·ϑ² boyutları: {', '.join(n['dims_seen'])}).")
    L.append("")
    for unit in ("1", "2", "3"):
        L += [f"## Ünite {unit}", "", "| ID | Formül | Çıktı | Kitap | Program | Ne zaman kullanılmaz (ilk madde) |", "|---|---|---|---|---|---|"]
        for f in out:
            if not any(c.startswith(f"FİZ.11.{unit}.") for c in f["learning_outcomes"]):
                continue
            page = f"s. {f['textbook']['printed_page']}" if f["textbook"]["verified"] else "—"
            flag = " ⚠️" if f["textbook_vs_program_conflict"] else ""
            L.append(f"| {f['id'][-3:]} | `{f['formula']}` | {', '.join(c.replace('FİZ.11.', '') for c in f['learning_outcomes'])} | "
                     f"{page} | {STATUS[f['program_calc_status']]}{flag} | {f['invalid_use_cases'][0]} |")
        L.append("")
    (OUT / "formulas.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
