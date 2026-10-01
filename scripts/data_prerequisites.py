"""STEP 6 — ön koşul eşlemelerinin elle yazılmış kaynak verisi.

PRIOR_OUTCOMES: ön koşul kavramı -> (önceki sınıf resmî öğrenme çıktısı, eşleme terimleri)
  Betik her eşlemeyi, terimin o çıktının resmî metninde / öğretme uygulamasında geçip geçmediğine bakarak doğrular.

BASIC_ASSUMPTIONS: ünitelerin resmî "Temel Kabuller" cümlesindeki ön bilgiler -> kavram
  (ortaokul fen bilimleri kökenli; ortaokul programı bu aşamada toplanmadığı için resmî kod yok)
"""

PRIOR_OUTCOMES = {
    "vektorel-nicelik": [("FİZ.9.2.2", ["vektörel"]), ("FİZ.9.2.3", ["vektör"])],
    "skaler-nicelik": [("FİZ.9.2.2", ["skaler"])],
    "vektor-bilesenleri": [("FİZ.9.2.4", ["bileşenlerine ayırma"])],
    "konum": [("FİZ.9.2.6", ["konum"]), ("FİZ.10.1.1", ["konum"])],
    "yer-degistirme": [("FİZ.9.2.6", ["yer değiştirme"]), ("FİZ.10.1.1", ["yer değiştirme"])],
    "hiz": [("FİZ.9.2.6", ["hız"]), ("FİZ.10.1.1", ["hız"])],
    "surat": [("FİZ.9.2.6", ["sürat"])],
    "ivme": [("FİZ.10.1.2", ["ivme"])],
    "sabit-hizli-hareket": [("FİZ.10.1.1", ["sabit hızlı"])],
    "sabit-ivmeli-hareket": [("FİZ.10.1.2", ["ivme"]), ("FİZ.10.1.3", ["sabit ivme"])],
    "hareket-grafikleri": [("FİZ.10.1.3", ["grafik"])],
    "grafik-egim-alan": [("FİZ.10.1.1", ["eğim"]), ("FİZ.10.1.3", ["grafik"])],
    "kuvvet": [("FİZ.9.2.5", ["kuvvet"])],
    "periyot": [("FİZ.10.4.1", ["periyot"]), ("FİZ.10.4.2", ["periyot"])],
    "frekans": [("FİZ.10.4.2", ["frekans"])],
    "enerji-donusumu": [("FİZ.10.2.3", ["enerji"]), ("FİZ.10.2.4", ["mekanik enerji"])],
    "elektrik-akimi": [("FİZ.10.3.2", ["elektrik akımı"])],
    "potansiyel-fark": [("FİZ.10.3.1", ["potansiyel fark"])],
    "direnc": [("FİZ.10.3.1", ["direnç"]), ("FİZ.10.3.3", ["Ohm"])],
}

# Temel kabul cümlesinden çıkarılan ön bilgiler. "phrase" resmî cümlede birebir geçmelidir.
BASIC_ASSUMPTIONS = {
    1: [("hız", "hiz"), ("ivme", "ivme"), ("ağırlık", "agirlik"), ("periyot", "periyot"), ("frekans", "frekans"),
        ("ilgili hesaplamaları yapabildikleri", None)],
    2: [("elektriklenme çeşitlerini", "elektrik-yuku"), ("elektroskop", "elektroskop"),
        ("mıknatısların kutuplarını", "manyetik-kutup"), ("mıknatısların etkileşimini", "miknatis"),
        ("pusula kullanımını", "pusula")],
    3: [("ışın", "isik"), ("ışık", "isik"), ("aydınlanma", None), ("düzlem ayna", None), ("küresel ayna", None),
        ("mercekleri", None), ("yansıma", "yansima"), ("kırılma", "kirilma"), ("odak noktası", "odak-noktasi")],
}

# Matematik ön koşulları: matematik programı bu aşamada toplanmadı; resmî kod yok.
MATH_NOTES = {
    "trigonometrik-oranlar": "FİZ.11.1.3 öğretme uygulaması trigonometri ön bilgisini varsayar ('trigonometrik hesaplamalara yönelik ön bilgisini hatırlatarak'). Matematik programındaki karşılığı doğrulanmadı.",
    "oran-oranti": "Hesaplamasız (oran/yorum) çıktıların temel aracı. Matematik programındaki karşılığı doğrulanmadı.",
    "ters-kare-iliskisi": "Coulomb ve aydınlanma modellerinde kullanılır. Matematik programındaki karşılığı doğrulanmadı.",
    "grafik-egim-alan": "Fizik 10. sınıfta (FİZ.10.1.1) eğim ve alan olarak işlenir.",
}
