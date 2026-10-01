"""11. sınıf fizik programında geçen becerilerin resmî tanımlarını ve süreç bileşenlerini çıkarır.

Kaynak: TYMM Öğretim Programları Ortak Metni (src-tymm-ortak-metin), EK-3 ve kavramsal beceriler bölümü.
Beceri adları fizik programındaki listelerden (curriculum.json) alınır.

Çıktı: knowledge-base/physics-11/learning-outcomes/skills.json
"""
import json
import re

from build_curriculum import KB, RAW, TODAY, CURRICULUM_VERSION

TEXT = RAW / "textbook-text" / "tymm-ortak-metin.txt"
SRC = "src-tymm-ortak-metin"
STOP = re.compile(r"^(===|TÜRKİYE YÜZYILI|\d+$|EK-\d|Süreç Bileşenleri|(KB|FBAB)[\d.]+\.\s*$)")


def lines():
    return [l.rstrip() for l in TEXT.read_text(encoding="utf-8").splitlines()]


def components(L, code):
    """CODE.SBn. satırlarını, alt satıra taşan devamlarıyla birlikte toplar."""
    pat = re.compile(rf"^\s*{re.escape(code)}\.SB(\d+)\.\s*(.*)")
    out, cur = [], None
    for l in L:
        m = pat.match(l)
        if m:
            cur = {"code": f"{code}.SB{m.group(1)}", "official_text": m.group(2).strip()}
            out.append(cur)
            continue
        if cur is not None:
            s = l.strip()
            if s and not STOP.match(s) and not re.match(r"^(KB|FBAB)[\d.]+\.SB", s) and \
                    (cur["official_text"].endswith("-") or s[:1].islower()):
                cur["official_text"] = (cur["official_text"][:-1] if cur["official_text"].endswith("-")
                                        else cur["official_text"] + " ") + s
                continue
            cur = None
    seen, uniq = set(), []
    for c in out:  # metin bazı bileşenleri iki kez listeleyebilir
        if c["code"] not in seen:
            seen.add(c["code"])
            uniq.append(c)
    return uniq


def definition(L, code):
    if code.startswith("FBAB"):
        i = next(i for i, l in enumerate(L) if l.strip().endswith(f"({code})"))
        body = []
        for l in L[i + 1:]:
            if l.strip().startswith("Süreç Bileşenleri") or re.match(rf"^{code}\.\s*$", l.strip()):
                break
            body.append(l.strip())
    else:
        sb1 = [i for i, l in enumerate(L) if re.match(rf"^\s*{re.escape(code)}\.SB1\.", l)]
        if sb1:
            j = max(k for k in range(sb1[0]) if L[k].strip().startswith("Süreç Bileşenleri"))
        else:  # şemsiye beceri (ör. KB2.16): tanım, etiket satırının hemen önündedir
            j = next(i for i, l in enumerate(L) if re.match(rf"^\s*{re.escape(code)}\.\s*$", l))
        body = []
        for l in reversed(L[:j]):
            s = l.strip()
            if not s or "Becerisi" in s or STOP.match(s) or s.endswith("Beceriler") or \
                    re.match(r"^(KB|FBAB)[\d.]+\.SB\d", s):
                break
            body.insert(0, s)
    text = ""
    for s in body:
        text = text[:-1] + s if text.endswith("-") else (text + " " + s).strip()
    return text


def main():
    cur = json.loads((KB / "curriculum" / "curriculum.json").read_text(encoding="utf-8"))
    los = json.loads((KB / "learning-outcomes" / "learning-outcomes.json").read_text(encoding="utf-8"))["learning_outcomes"]
    names = {}
    for u in cur["units"]:
        for item in u["field_skills"] + u["conceptual_skills"]:
            for m in re.finditer(r"((?:FBAB|KB)\d+(?:\.\d+)*)\.\s+([^,()]+)", item):
                names.setdefault(m.group(1), m.group(2).strip())
    used = {o["skills"][0]["code"] for o in los}
    L = lines()
    skills, warnings = [], []
    for code in sorted(names, key=lambda c: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", c)]):
        try:
            d = definition(L, code)
        except (StopIteration, ValueError):
            d = ""
        comps = components(L, code)
        if not d.endswith("ifade eder."):
            warnings.append(f"{code}: tanım bulunamadı ya da eksik ({d[:50]!r})")
        subs = [c for c in names if c.startswith(code + ".")]
        if not comps and not subs:
            warnings.append(f"{code}: süreç bileşeni bulunamadı")
        skills.append({
            "id": f"skill-{code.lower().replace('.', '-')}",
            "official_code": code,
            "official_name": names[code],
            "family": "Fen Bilimleri Alan Becerileri" if code.startswith("FBAB") else "Kavramsal Beceriler",
            "official_definition": d or None,
            "process_components": comps,
            "sub_skills": [c for c in names if c.startswith(code + ".")],
            "used_as_primary_skill_by": [o["official_code"] for o in los if o["skills"][0]["code"] == code],
            "listed_in_units": [u["unit_no"] for u in cur["units"]
                                if any(i.startswith(code + ".") or f"({code}." in i
                                       for i in u["field_skills"] + u["conceptual_skills"])],
            "curriculum_version": CURRICULUM_VERSION,
            "sources": [{"source_id": SRC, "fields": ["official_definition", "process_components"]},
                        {"source_id": "src-meb-fizik-op-2026", "fields": ["official_name", "listed_in_units"]}],
            "confidence": "HIGH" if d.endswith("ifade eder.") and (comps or subs) else "MEDIUM",
            "created_at": TODAY, "updated_at": TODAY,
        })
    missing_used = used - set(names)
    if missing_used:
        warnings.append(f"Çıktılarda kullanılıp ünite listelerinde olmayan beceri: {missing_used}")
    out = {"subject": "physics", "grade": 11, "curriculum_version": CURRICULUM_VERSION,
           "generated_by": "scripts/build_skills.py", "generated_at": TODAY, "count": len(skills), "skills": skills}
    (KB / "learning-outcomes" / "skills.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(skills)} beceri ({len(used)} tanesi çıktıların birincil becerisi)")
    for s in skills:
        print(f"  {s['official_code']:9} {s['official_name'][:28]:28} SB={len(s['process_components'])} "
              f"tanım={'✓' if s['official_definition'] else '✗'}  {s['confidence']}")
    for w in warnings:
        print("UYARI:", w)


if __name__ == "__main__":
    main()
