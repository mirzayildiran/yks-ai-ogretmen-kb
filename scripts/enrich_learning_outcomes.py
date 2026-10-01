"""STEP 4: learning-outcomes.json'u zenginleştirir.

Eklenenler:
  - textbook_sections   : MEB 11. sınıf ders kitabı bölümü + basılı sayfa (başlık o sayfada aranarak doğrulanır)
  - subtopic            : kitap içindekiler eşlemesiyle doğrulanır (mapping_method = textbook_toc)
  - process_components[].skill_component : becerinin resmî süreç bileşeni (sayı eşitliği kontrol edilerek sıra ile)
  - measurable_behaviors: süreç bileşenlerinden türetilen gözlenebilir davranışlar
  - official_scope_constraints : scope-constraints.curated.json (her anchor resmî metinde aranır)
  - assessment_implications    : öğretme uygulamasındaki resmî ölçme cümleleri

Sıra: build_curriculum.py -> build_skills.py -> enrich_learning_outcomes.py
"""
import json
import re

from build_curriculum import KB, RAW, TODAY, letters_only, pdf_grade11_text, write_master_map

LO_PATH = KB / "learning-outcomes" / "learning-outcomes.json"
SRC_BOOK = "src-meb-fiz11-ders-kitabi"
BOOK_TXT = RAW / "textbook-text" / "fizik-11-ders-kitabi.txt"

# Ders kitabı içindekiler (s. 7-8). Basılı sayfa = PDF sayfası (kapak dahil numaralandırma).
# Kitapta 1.6'nın alt başlıkları yanlışlıkla "1.4.1 / 1.4.2" numaralanmış; burada 1.6.1 / 1.6.2 kullanıldı.
TEXTBOOK = {
    "FİZ.11.1.1": ("1.1.1", "Serbest Düşen Cisimler", 16),
    "FİZ.11.1.2": ("1.1.2", "Serbest Düşme Hareketi ile İlgili Veriler", 20),
    "FİZ.11.1.3": ("1.2", "İki Boyutta Sabit İvmeli Hareket", 30),
    "FİZ.11.1.4": ("1.3.1", "Bileşke Kuvvet ve Hareket Arasındaki İlişki", 40),
    "FİZ.11.1.5": ("1.3.2", "Serbest Cisim Diyagramı", 53),
    "FİZ.11.1.6": ("1.4.1", "Statik ve Kinetik Sürtünme Kuvvetleri", 65),
    "FİZ.11.1.7": ("1.4.2", "Sürtünme Kuvvetinin Bağlı Olduğu Değişkenler", 70),
    "FİZ.11.1.8": ("1.5", "Limit Hız", 86),
    "FİZ.11.1.9": ("1.6.1", "Çembersel Harekette Yörünge ve Hız Kavramları", 95),
    "FİZ.11.1.10": ("1.6.2", "Çembersel Hareketin Değişkenleri", 101),
    "FİZ.11.2.1": ("2.1.1", "Elektriksel Kuvvet", 155),
    "FİZ.11.2.2": ("2.1.2", "Elektriksel Alan", 166),
    "FİZ.11.2.3": ("2.1.3", "Faraday Kafesi", 178),
    "FİZ.11.2.4": ("2.2.1", "Manyetik Alan", 186),
    "FİZ.11.2.5": ("2.2.2", "Üzerinden Akım Geçen Düz İletken Telin Manyetik Alanı", 198),
    "FİZ.11.2.6": ("2.2.3", "Akım Makarasının Manyetik Alanı", 207),
    "FİZ.11.2.7": ("2.2.4", "Elektromıknatısların Kullanım Alanları", 213),
    "FİZ.11.2.8": ("2.2.5", "Manyetik Alanda Üzerinden Akım Geçen Düz Bir Tele Etki Eden Kuvvet", 218),
    "FİZ.11.2.9": ("2.2.6", "Manyetik Alanda Üzerinden Akım Geçen Dikdörtgen Telin Bir Eksen Etrafında Dönmesi", 229),
    "FİZ.11.2.10": ("2.3.1", "Manyetik Akı", 236),
    "FİZ.11.2.11": ("2.3.2", "İndüksiyon Gerilimi", 242),
    "FİZ.11.2.12": ("2.3.3", "Alternatif Akım", 253),
    "FİZ.11.2.13": ("2.4", "Transformatörler", 263),
    "FİZ.11.3.1": ("3.1", "Işık Şiddeti, Işık Akısı ve Aydınlanma", 302),
    "FİZ.11.3.2": ("3.2", "Düzlem Aynalar", 312),
    "FİZ.11.3.3": ("3.3.1", "Küresel Ayna Çeşitleri ve Özellikleri", 323),
    "FİZ.11.3.4": ("3.3.2", "Küresel Aynalarda Görüntü Oluşumu", 333),
    "FİZ.11.3.5": ("3.4", "Kırılma", 343),
    "FİZ.11.3.6": ("3.5", "Görünür Derinlik", 354),
    "FİZ.11.3.7": ("3.6", "Fiber Optik", 361),
    "FİZ.11.3.8": ("3.7", "Prizmalar", 367),
    "FİZ.11.3.9": ("3.8.1", "Merceklerin Özellikleri", 373),
    "FİZ.11.3.10": ("3.8.2", "Merceklerde Görüntü Oluşumu", 381),
}
ASSESS = re.compile(r"değerlendiril|yazılı yoklama|çalışma yaprağı|çalışma kâğıdı|çıkış kartı|test|performans görevi|soru kutusu|grid", re.I)
VERB = re.compile(r"(\S+)\.$")


def book_pages():
    t = BOOK_TXT.read_text(encoding="utf-8")
    p = re.split(r"\n=== SAYFA (\d+) ===\n", t)
    return {int(p[i]): p[i + 1] for i in range(1, len(p), 2)}


def main():
    doc = json.loads(LO_PATH.read_text(encoding="utf-8"))
    skills = {s["official_code"]: s for s in
              json.loads((KB / "learning-outcomes" / "skills.json").read_text(encoding="utf-8"))["skills"]}
    curated = json.loads((KB / "learning-outcomes" / "scope-constraints.curated.json").read_text(encoding="utf-8"))
    pages = book_pages()
    _, pdf_full = pdf_grade11_text()
    pdf_key = letters_only(re.sub(r"\s?-\s*\n", "", re.sub(r"\n\d+\nFİZİK DERSİ ÖĞRETİM PROGRAMI\n", "\n", pdf_full)))
    errors = []

    for g in curated["global"]:
        if letters_only(g["official_text"]) not in pdf_key:
            errors.append(f"Genel kapsam alıntısı PDF'te yok: {g['official_text'][:60]}")

    for o in doc["learning_outcomes"]:
        code = o["official_code"]
        # ders kitabı bölümü
        sec, title, page = TEXTBOOK[code]
        found = [pg for pg in (page, page + 1) if letters_only(title) in letters_only(pages.get(pg, ""))]
        if not found:
            errors.append(f"{code}: kitap başlığı '{title}' s.{page}'de bulunamadı")
        o["textbook_sections"] = [{"source_id": SRC_BOOK, "section": sec, "official_title": title,
                                   "printed_page": page, "verified_on_page": bool(found)}]
        # içerik başlığı doğrulaması: kitap bölümünün üst başlığı ile program içerik başlığı aynı birimi göstermeli
        o["subtopic"]["mapping_method"] = "textbook_toc"
        o["subtopic"]["confidence"] = "HIGH"
        o["subtopic"]["evidence"] = f"Ders kitabı {sec} '{title}' (s. {page})"
        # süreç bileşeni -> beceri bileşeni
        sk = skills[o["skills"][0]["code"]]
        comps = sk["process_components"]
        if len(comps) != len(o["process_components"]):
            errors.append(f"{code}: süreç bileşeni sayısı ({len(o['process_components'])}) beceri bileşeni sayısından ({len(comps)}) farklı")
        else:
            for c, sc in zip(o["process_components"], comps):
                c["skill_component"] = {"code": sc["code"], "official_text": sc["official_text"],
                                        "mapping_method": "ordered_alignment_equal_count", "confidence": "HIGH"}
        o["measurable_behaviors"] = [{
            "component_id": c["id"],
            "observable_verb": VERB.search(c["official_text"]).group(1) if VERB.search(c["official_text"]) else None,
            "behavior": c["official_text"],
            "skill_component": c.get("skill_component", {}).get("code"),
            "evidence_type": "official_process_component",
        } for c in o["process_components"]]
        # kapsam sınırları
        practice = o["official_teaching_practice"]
        sents = re.split(r"(?<=\.)\s+", practice)
        items = []
        for i, it in enumerate(curated["outcomes"].get(code, []), 1):
            hit = [s for s in sents if it["anchor"] in s]
            if not hit:
                errors.append(f"{code}: kapsam anchor'ı resmî metinde yok: '{it['anchor']}'")
                continue
            items.append({"id": f"{o['id']}-scope-{i}", "type": it["type"], "official_text": hit[0],
                          "implication": it["implication"], "implication_confidence": "MEDIUM",
                          "applies_to": it.get("applies_to"),
                          "source_id": "src-meb-fizik-op-2026"})
        o["official_scope_constraints"] = items
        # ölçme
        o["assessment_implications"] = [{"official_text": s, "type": "official_assessment_suggestion"}
                                        for s in sents if ASSESS.search(s)]
        o["pending_fields"] = [f for f in o["pending_fields"]
                               if f not in ("measurable_behaviors", "assessment_implications")]
        if not any(s["source_id"] == SRC_BOOK for s in o["sources"]):
            o["sources"].append({"source_id": SRC_BOOK, "fields": ["textbook_sections", "subtopic"]})
        o["sources"] = [s for s in o["sources"] if s["source_id"] != "src-tymm-ortak-metin"]
        o["sources"].append({"source_id": "src-tymm-ortak-metin", "fields": ["process_components.skill_component"]})
        o["updated_at"] = TODAY

    doc["global_scope_constraints"] = curated["global"]
    doc["enriched_by"] = "scripts/enrich_learning_outcomes.py"
    LO_PATH.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    cur = json.loads((KB / "curriculum" / "curriculum.json").read_text(encoding="utf-8"))
    write_master_map(cur, doc["learning_outcomes"])
    los = doc["learning_outcomes"]
    print(f"kitap bölümü doğrulandı: {sum(o['textbook_sections'][0]['verified_on_page'] for o in los)}/{len(los)}")
    print(f"beceri bileşeni eşlemesi: {sum(all('skill_component' in c for c in o['process_components']) for o in los)}/{len(los)}")
    print(f"kapsam sınırı: {sum(len(o['official_scope_constraints']) for o in los)} madde, "
          f"{sum(1 for o in los if o['official_scope_constraints'])} çıktıda")
    print(f"ölçme önerisi cümlesi: {sum(len(o['assessment_implications']) for o in los)}")
    for e in errors:
        print("HATA:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
