"""STEP 13 verisi: hata taksonomisi (ERROR_TYPES) ve kavram yanılgıları (MISCONCEPTIONS).

Şema ve doğrulama kuralları: build_errors.py docstring'i.
Kaynak dürüstlüğü: SRC sözlüğündeki her kayıt gerçekten bulunmuş bir kaynaktır. `verified_by_fetch=True`
yalnızca tam metin ya da özet/kayıt sayfası bu çalışmada okunmuş kaynaklar için verilmiştir; ayrıntı
her kaydın citation alanındaki köşeli parantez notundadır. Hiçbir kaynak uydurulmamıştır.
Tier 1: MEB resmî; Tier 2: akademik.
"""

ACC = "2026-10-02"


def _s(citation, url, tier, verified):
    return {"citation": citation, "url": url, "tier": tier, "accessed": ACC, "verified_by_fetch": verified}


SRC = {
    # --- Mekanik (Tier 2) ---
    "FCI": _s("Hestenes, D., Wells, M. & Swackhamer, G. (1992). Force Concept Inventory. The Physics Teacher, 30(3), 141–158. "
              "[yanılgı taksonomisi tablosu yazarın tam metin PDF'inden okundu]",
              "https://doi.org/10.1119/1.2343497", 2, True),
    "HH85": _s("Halloun, I. A. & Hestenes, D. (1985). Common sense concepts about motion. American Journal of Physics, 53(11), 1056–1065. "
               "[özet okundu: Newton kuramıyla çelişen sağduyu kavramlarının taksonomisi]",
               "https://doi.org/10.1119/1.14031", 2, True),
    "CLEM": _s("Clement, J. (1982). Students' preconceptions in introductory mechanics. American Journal of Physics, 50(1), 66–71. "
               "[özet okundu: kuvvet–ivme ilişkisine dair kararlı alternatif görüş]",
               "https://doi.org/10.1119/1.12989", 2, True),
    "MCCL": _s("McCloskey, M., Caramazza, A. & Green, B. (1980). Curvilinear motion in the absence of external forces: naive beliefs about the "
               "motion of objects. Science, 210(4474), 1139–1141. [özet okundu]",
               "https://doi.org/10.1126/science.210.4474.1139", 2, True),
    "TM80": _s("Trowbridge, D. E. & McDermott, L. C. (1980). Investigation of student understanding of the concept of velocity in one dimension. "
               "American Journal of Physics, 48(12), 1020–1028. [özet okundu: hız karşılaştırmasında konum ölçütü]",
               "https://doi.org/10.1119/1.12298", 2, True),
    "BEI94": _s("Beichner, R. J. (1994). Testing student interpretation of kinematics graphs. American Journal of Physics, 62(8), 750–762. "
                "[özet okundu: grafiği resim sanma, eğim/yükseklik karıştırma]",
                "https://doi.org/10.1119/1.17449", 2, True),
    "POTV23": _s("Potvin, P., Chastenay, P., Thibault, F., Riopel, M., Ahr, E. & Brault Foisy, L. (2023). An understanding of falling bodies across "
                 "schooling and experience based on the conceptual prevalence framework. Disciplinary and Interdisciplinary Science Education Research, 5. "
                 "[özet okundu: havalı/havasız ortamda düşen cisimlerde kütle–hız yanılgısı]",
                 "https://doi.org/10.1186/s43031-023-00075-4", 2, True),
    "FERR17": _s("Ferreira, A., Seyffert, A. S. & Lemmer, M. (2017). Developing a graphical tool for students to understand air resistance and free fall: "
                 "when heavier objects do fall faster. Physics Education, 52(3), 034002. [özet okundu: 'hava direncini ihmal et' varsayımının "
                 "günlük deneyimle çelişmesi]",
                 "https://doi.org/10.1088/1361-6552/aa65da", 2, True),
    "TAIBU15": _s("Taibu, R., Rudge, D. & Schuster, D. (2015). Textbook presentations of weight: conceptual difficulties and language ambiguities. "
                  "Physical Review Special Topics – Physics Education Research, 11, 010117. [özet okundu: ağırlık = yerçekimi kuvveti ile "
                  "tartı okuması ayrımının ivmeli cisimlerde yarattığı güçlük]",
                  "https://doi.org/10.1103/PhysRevSTPER.11.010117", 2, True),
    "UG07": _s("Ünlü, P. & Gök, B. (2007). Öğrencilerin düzgün dairesel harekette merkezcil kuvvet hakkındaki kavram yanılgılarının araştırılması. "
               "Gazi Üniversitesi Gazi Eğitim Fakültesi Dergisi, 27(3), 141–150. [tam metin okundu; 119 lise 3. sınıf öğrencisi]",
               "https://dergipark.org.tr/en/download/article-file/77147", 2, True),
    "KG11": _s("Kızılcık, H. Ş. & Güneş, B. (2011). Düzgün dairesel hareket konusunda üç aşamalı kavram yanılgısı testi geliştirilmesi. "
               "Hacettepe Üniversitesi Eğitim Fakültesi Dergisi, 41, 278–292. [tam metin okundu]",
               "https://dergipark.org.tr/tr/download/article-file/87404", 2, True),
    "KGU05": _s("Kuru, İ. & Güneş, B. (2005). Lise 2. sınıf öğrencilerinin kuvvet konusundaki kavram yanılgıları. Gazi Üniversitesi Gazi Eğitim "
                "Fakültesi Dergisi, 25(2), 1–17. [yalnızca özet/künye sayfası okundu; 456 öğrenci]",
                "https://dergipark.org.tr/en/pub/gefad/issue/6756/90844", 2, True),
    "AT21": _s("Aygün, M. & Tan, M. (2021). Bir çarpışmada kütlenin etki-tepki kuvvetlerine etkisi: kavram yanılgısını ortadan kaldırmada kavramsal "
               "değişim metni ya da geleneksel açıklayıcı metin. Pamukkale Üniversitesi Eğitim Fakültesi Dergisi, 51, 65–91. [tam metin okundu]",
               "https://dergipark.org.tr/en/download/article-file/1348542", 2, True),
    "KAS21": _s("Kızılcık, H. Ş., Aygün, M., Şahin, E., Önder-Çelikkanlı, N., Türk, O., Taşkın, T. & Güneş, B. (2021). Possible misconceptions about "
                "solid friction. Physical Review Physics Education Research, 17, 023107. [özet okundu: 42 makalenin içerik analizi; dört tema]",
                "https://doi.org/10.1103/PhysRevPhysEducRes.17.023107", 2, True),
    "TK16": _s("Temiz, B. K. & Kızılcık, H. Ş. (2016). Sürtünmeli eğik düzlemde hareketin dinamiğine ilişkin öğrenci görüşleri. Eğitim ve Toplum "
               "Araştırmaları Dergisi, 3(2), 15–30. [özet ve giriş okundu; 108 lise 2. sınıf öğrencisi]",
               "https://dergipark.org.tr/tr/download/article-file/269500", 2, True),
    # --- Elektrik ve manyetizma (Tier 2) ---
    "FG98": _s("Furió, C. & Guisasola, J. (1998). Difficulties in learning the concept of electric field. Science Education, 82(4), 511–526. "
               "[özet okundu: üniversite öğrencileri bile alan fikri yerine uzaktan etki modelini tercih ediyor]",
               "https://doi.org/10.1002/(SICI)1098-237X(199807)82:4%3C511::AID-SCE6%3E3.0.CO;2-E", 2, True),
    "TPT93": _s("Törnkvist, S., Pettersson, K.-A. & Tranströmer, G. (1993). Confusion by representation: on student's comprehension of the electric "
                "field concept. American Journal of Physics, 61(4), 335–338. [özet okundu: kuvvet ve kuvvet alanı kavramlarının karışması]",
                "https://doi.org/10.1119/1.17265", 2, True),
    "VR92": _s("Viennot, L. & Rainson, S. (1992). Students' reasoning about the superposition of electric fields. International Journal of Science "
               "Education, 14(4), 475–487. [özet okundu]",
               "https://doi.org/10.1080/0950069920140409", 2, True),
    "RTV94": _s("Rainson, S., Tranströmer, G. & Viennot, L. (1994). Students' understanding of superposition of electric fields. American Journal of "
                "Physics, 62(11), 1026–1032. [özet okundu: nedensel yorum; alanı kabul etmek için hareket/etki arama]",
                "https://doi.org/10.1119/1.17701", 2, True),
    "CAMP19": _s("Campos, E., Zavala, G., Zuka, K. & Guisasola, J. (2019). Electric field lines: the implications of students' interpretation on their "
                 "understanding of the concept of electric field and of the superposition principle. American Journal of Physics, 87(8), 660–667. "
                 "[özet okundu]",
                 "https://doi.org/10.1119/1.5100588", 2, True),
    "WJL23": _s("Wallace, C. S., Jones, L. & Lin, A. (2023). Four errors students make with inverse-square law vectors. arXiv:2311.16811. "
                "[tam metin okundu: vektörleri skaler gibi toplama; yük işaretini bileşen işaretine yanlış bağlama]",
                "https://arxiv.org/abs/2311.16811", 2, True),
    "MAL01": _s("Maloney, D. P., O'Kuma, T. L., Hieggelke, C. J. & Van Heuvelen, A. (2001). Surveying students' conceptual knowledge of electricity "
                "and magnetism. American Journal of Physics, 69(S1), S12–S23. [özet okundu]",
                "https://doi.org/10.1119/1.1371296", 2, True),
    "SAA07": _s("Saarelainen, M., Laaksonen, A. & Hirvonen, P. (2007). Students' initial knowledge of electric and magnetic fields — more profound "
                "explanations and reasoning models for undesired conceptions. European Journal of Physics, 28, 51–60. [özet okundu]",
                "https://doi.org/10.1088/0143-0807/28/1/006", 2, True),
    "BG98": _s("Borges, A. T. & Gilbert, J. K. (1998). Models of magnetism. International Journal of Science Education, 20(3), 361–378. "
               "[özet okundu; 'elektrik olarak manyetizma' modeli Voutsina & Ravanis (2011) tam metninden teyit edildi]",
               "https://doi.org/10.1080/0950069980200308", 2, True),
    "GAZ04": _s("Guisasola, J., Almudí, J. M. & Zubimendi, J. L. (2004). Difficulties in learning the introductory magnetic field theory in the first "
                "years of university. Science Education, 88(3), 443–464. [özet okundu: öğrenciler manyetik alanın kaynağını belirleyemiyor, "
                "manyetik kuvvet ile alanı karıştırıyor]",
                "https://doi.org/10.1002/sce.10119", 2, True),
    "VR11": _s("Voutsina, L. & Ravanis, K. (2011). History of physics and conceptual constructions: the case of magnetism. Themes in Science & "
               "Technology Education, 4(1), 1–20. [tam metin okundu; 10. ve 11. sınıf öğrencileriyle mülakat]",
               "https://files.eric.ed.gov/fulltext/EJ1131502.pdf", 2, True),
    "UC21": _s("Ürek, H. & Çoramık, M. (2021). A cross sectional survey about students' agreement rates on nonscientific ideas concerning the concept of "
               "magnet. Journal of Turkish Science Education, 18, 218–232. [özet okundu; 436 öğrenci]",
               "https://doi.org/10.36681/tused.2021.61", 2, True),
    "SN05": _s("Secrest, S. & Novodvorsky, I. (2005). Identifying student difficulties with understanding induced EMF. arXiv:physics/0501093. "
               "[tam metin okundu: indüksiyon akımının yönü, akı ile alanın karıştırılması]",
               "https://arxiv.org/abs/physics/0501093", 2, True),
    "TUR16": _s("Turgut, Ü., Salar, R. & Çolak, A. (2016). Elektromanyetizma konusunda kavramsal başarı testi geliştirilmesi. Bayburt Eğitim Fakültesi "
                "Dergisi, 11(1), 117–142. [özet ve yöntem bölümü okundu: 11. sınıf 'Manyetizma ve Elektromanyetik İndüklenme' testinde literatürdeki "
                "kavram yanılgıları çeldirici olarak kullanılmış]",
                "https://dergipark.org.tr/tr/download/article-file/214856", 2, True),
    "TY19": _s("Taşkın, T. & Ünlü Yavaş, P. (2019/2021). Examining knowledge levels of high school students related to conductors at electrostatic "
               "equilibrium and electric field lines using the drawing method. Research in Science Education, 51, 577–597. "
               "[yalnızca künye doğrulandı; özet erişilemedi]",
               "https://doi.org/10.1007/s11165-018-9808-6", 2, False),
    # --- Optik (Tier 2) ---
    "GH00": _s("Galili, I. & Hazan, A. (2000). Learners' knowledge in optics: interpretation, structure and analysis. International Journal of "
               "Science Education, 22(1), 57–88. [özet okundu: lise ve öğretmen adayı öğrencilerin ışık, görme ve ilgili konulardaki bilgisi]",
               "https://doi.org/10.1080/095006900290000", 2, True),
    "GM87": _s("Goldberg, F. M. & McDermott, L. C. (1987). An investigation of student understanding of the real image formed by a converging lens or "
               "concave mirror. American Journal of Physics, 55(2), 108–119. [özet okundu: öğrenciler mercek/ayna ve ekranın işlevini, "
               "cisim–ayna–ekran ilişkisinin tekliğini anlamıyor]",
               "https://doi.org/10.1119/1.15254", 2, True),
    "LRE97": _s("Langley, D., Ronen, M. & Eylon, B.-S. (1997). Light propagation and visual patterns: preinstruction learners' conceptions. Journal of "
                "Research in Science Teaching, 34(4), 399–424. [özet okundu]",
                "https://doi.org/10.1002/(SICI)1098-2736(199704)34:4%3C399::AID-TEA8%3E3.0.CO;2-M", 2, True),
    "CV01": _s("Colin, P. & Viennot, L. (2001). Using two models in optics: students' difficulties and suggestions for teaching. American Journal of "
               "Physics, 69(S1), S36–S44. [özet okundu: çizimlerin statüsü, ışık yolunun geriye doğru seçimi]",
               "https://doi.org/10.1119/1.1371256", 2, True),
    "KG16": _s("Kaltakçı-Gürel, D., Eryılmaz, A. & McDermott, L. C. (2016). Identifying pre-service physics teachers' misconceptions and conceptual "
               "difficulties about geometrical optics. European Journal of Physics, 37(4), 045705. [özet okundu: düzlem ayna, küresel ayna, mercek; "
               "ışın modeli, gözlemci ve ekranın işlevi]",
               "https://doi.org/10.1088/0143-0807/37/4/045705", 2, True),
    "KG17": _s("Kaltakçı-Gürel, D., Eryılmaz, A. & McDermott, L. C. (2017). Development and application of a four-tier test to assess pre-service "
               "physics teachers' misconceptions about geometrical optics. Research in Science & Technological Education, 35(2), 238–260. "
               "[özet okundu; 243 öğretmen adayı, 12 Türk devlet üniversitesi]",
               "https://doi.org/10.1080/02635143.2017.1310094", 2, True),
    "KAE10": _s("Kaewkhong, K., Mazzolini, A., Emarat, N. & Arayathanitkul, K. (2010). Thai high-school students' misconceptions about and models of "
                "light refraction through a planar surface. Physics Education, 45(1), 97–107. [ERIC özeti okundu: 220 öğrenciden yalnız 1'i "
                "görüntü konumunu doğru gerekçeyle buldu]",
                "https://doi.org/10.1088/0031-9120/45/1/012", 2, True),
    "MAT05": _s("Mateycik, F., Wagner, D. J., Rivera, J. J. & Jennings, S. (2005). Student descriptions of refraction and optical fibers. AIP "
                "Conference Proceedings (PERC), 790, 169–172. [tam metin okundu: fiber içinde gümüşlenmiş ayna/opak kaplama modelleri; tam "
                "yansımanın seyrek ortamdan yoğun ortama geçişte olduğu inancı]",
                "https://www.per-central.org/items/perc/3452.pdf", 2, True),
    # --- Tier 1 (MEB) ---
    "TB": _s("MEB (2026). Fizik Dersi 11. Sınıf Ders Kitabı (TYMM). [ilgili bölüm yerel metin kopyasından okundu; kitap kavram yanılgısı "
             "kaydetmez, yalnız doğru modeli verir]",
             "https://tymm.meb.gov.tr/kitap/404/fizik-dersi-11sinif-ders-kitabi", 1, True),
    "QWK": _s("MEB (2025). TYMM Bağlam Temelli Çoktan Seçmeli Soru Yazım Kılavuzu, s. 15–16: çeldiriciler öğrencilerin düşebileceği kavram yanılgılarından "
              "seçilmelidir. [ilgili sayfalar okundu; ilke kaynağı]",
              "https://tymm.meb.gov.tr/upload/kilavuz/coktan-secmeli-soru-yazim-kilavuzu.pdf", 1, True),
}


def S(*keys):
    return [dict(SRC[k]) for k in keys]


def LO(*ids):
    return [f"FİZ.11.{i}" for i in ids]


def DI(stem, A, B, C, D, E, ans, mis):
    """5 şıklı tanı sorusu."""
    return {"stem": stem, "options": {"A": A, "B": B, "C": C, "D": D, "E": E}, "answer": ans, "misconception_option": mis}


def RM(q, conflict, analogy):
    return {"socratic_questions": q, "cognitive_conflict": conflict, "analogy": analogy}


def MC(slug, statement, correct, concepts, los, et, appears, di, rem, sources, conf):
    return {"slug": slug, "statement": statement, "correct_view": correct, "concepts": concepts, "learning_outcomes": los,
            "error_type": et, "how_it_appears": appears, "diagnostic_item": di, "remediation": rem, "sources": sources, "confidence": conf}


ERROR_TYPES = []
MISCONCEPTIONS = []

# ============================================================================================
# BÖLÜM 1 — HATA TÜRLERİ
# ============================================================================================
ERROR_TYPES += [
    {
        "code": "CONCEPTUAL_ERROR", "name_tr": "Kavramsal hata",
        "definition": "Öğrenci bir fiziksel kavramı, büyüklüğü ya da ilkeyi bilimsel anlamından farklı kurmuştur; hata hesap ya da dikkatten değil "
                      "zihinsel modelden gelir. Aynı yanılgı farklı bağlamlarda tutarlı biçimde tekrarlanır.",
        "symptoms": [
            "Sabit hızla giden cisme hareket yönünde net kuvvet çizmek ('hareket kuvveti').",
            "Büyük kütleli cismin küçük kütleliye daha büyük etki kuvveti uyguladığını söylemek.",
            "Tepe noktasında hız sıfır olduğu için ivmenin de sıfır olduğunu savunmak.",
            "Merkezkaç kuvveti gerçek bir kuvvet gibi serbest cisim diyagramına eklemek.",
            "Akı ile akının değişim hızını (ya da alanı) aynı şey saymak; sabit akıda emk beklemek.",
            "Aynı soruyu sayısal yapınca doğru, 'neden' diye sorunca yanlış gerekçe vermek.",
        ],
        "diagnostic_questions": [
            "Cismi bu kararı vermeye iten şeyi kendi cümlenle söyler misin: hangi kuvvet bunu yapıyor?",
            "Bu kuvveti hangi cisim uyguluyor, hangi cisme uyguluyor?",
            "Aynı durumu iki farklı sayıyla çözsen sonuç nasıl değişirdi, neden?",
            "Hareketin sürmesi ile hızın değişmesi arasındaki fark nedir?",
            "Günlük hayattan bu düşüncenin doğru çıktığı bir örnek ve yanlış çıktığı bir örnek verebilir misin?",
        ],
        "remediation_strategy": [
            "Öğrencinin gerekçesini yargılamadan sözlü ya da yazılı olarak açığa çıkar (tahmin–gerekçe).",
            "Yanılgının doğru göründüğü günlük bağlamı kabul et (ör. sürtünmenin gizli kuvvet olduğu durumlar).",
            "Çatışma yaratan tek bir gözlem, simülasyon ya da ters örnek sun; öğrenciden tahminini yeniden yapmasını iste.",
            "Doğru modeli en küçük bağlamda (tek cisim, tek kuvvet) kurdur; cümleyi öğrencinin kendisi söylesin.",
            "Modeli ikinci ve üçüncü bağlamda (grafik, sayısal, günlük) sınatarak aktar.",
            "Birkaç gün sonra, bağlamı değiştirilmiş benzer bir tanı sorusuyla kalıcılığı kontrol et.",
        ],
        "recommended_question_families": ["newton1-inertia", "newton3-action-reaction", "ff-mass-independence", "string-cut-trajectory",
                                          "efield-direction-and-lines", "flux-factors-analogy", "lenz-induced-current-direction"],
        "related_error_types": ["PREREQUISITE_GAP", "QUESTION_INTERPRETATION_ERROR", "FBD_ERROR"],
    },
    {
        "code": "FORMULA_SELECTION_ERROR", "name_tr": "Bağıntı seçme hatası",
        "definition": "Soruda verilen–istenen durum için uygun olmayan bir bağıntı seçilir; çoğu zaman bağıntının uygulanma koşulları (sabit ivme, "
                      "ideal model, hangi değişken sabit) göz ardı edilir.",
        "symptoms": [
            "Serbest düşmede h = ½gt² yerine h = g·t kullanmak.",
            "Düzgün elektrik alanda E = V·d yazmak (doğrusu E = V/d).",
            "Telin manyetik kuvvetinde sinθ yerine cosθ seçmek.",
            "Alternatif akımda T = f yazmak; periyot–frekans ters ilişkisini atlamak.",
            "İletim kaybında P = iR (yerine P = i²R) kullanmak.",
            "Doğrusal orantı gerektiren yerde karesel, karesel gereken yerde doğrusal bağıntı kullanmak.",
        ],
        "diagnostic_questions": [
            "Bu soruda verilenler neler, istenen ne? Bu üçlüyü içeren bağıntı hangisi?",
            "Bu bağıntı hangi koşulda geçerli? Bu soruda o koşul sağlanıyor mu?",
            "Bağıntının birimlerini kontrol edersen sol ve sağ taraf aynı birime çıkıyor mu?",
            "Değişkenlerden birini iki katına çıkarsak sonuç nasıl değişirdi, seçtiğin bağıntı bunu veriyor mu?",
        ],
        "remediation_strategy": [
            "Önce 'verilen–istenen–sabit kalan' tablosunu öğrenciye yaptır.",
            "Bağıntıyı ezberden değil, hangi fiziksel ilişkiden çıktığından seçtir (ör. alan çizgisi sıklığı, yol–zaman ilişkisi).",
            "Birim analiziyle seçilen bağıntıyı sına; birimler tutmuyorsa seçimi yeniden yaptır.",
            "Uç durum (değer sıfır ya da çok büyük) kontrolü ile bağıntının davranışını yorumlat.",
            "Aynı konudaki iki benzer bağıntıyı yan yana koyup ayırt edici koşulu öğrenciye yazdır.",
        ],
        "recommended_question_families": ["ff-reaction-time-ruler", "efield-uniform-plates", "wire-force-data-model", "induction-emf-ratio-calc",
                                          "ac-frequency-period-counting", "flux-closed-surface", "transformer-transmission-loss"],
        "related_error_types": ["FORMULA_APPLICATION_ERROR", "METHOD_SELECTION_ERROR", "UNIT_ERROR"],
    },
    {
        "code": "FORMULA_APPLICATION_ERROR", "name_tr": "Bağıntıyı uygulama hatası",
        "definition": "Doğru bağıntı seçilmiştir ancak içindeki katsayı, üs, açı, kütle ya da kuvvet yanlış yerleştirilir ya da yanlış nicelik kullanılır.",
        "symptoms": [
            "½ katsayısını unutmak; ϑ² = 2gh'de ya da F = BiL sinθ'da çarpanı atlamak.",
            "tanθ yerine sinθ almak (eğik düzlemde kayma açısı, eğimli viraj).",
            "Eğik gelişte r yerine yüzeye iz düşümünü kullanmak.",
            "Tek cisim denkleminde yanlış kütle kullanmak (sistemin kütlesi yerine tek cismin kütlesi).",
            "ϑ ve ω ile yazılan merkezcil bağıntılarda r'nin üssünü karıştırmak.",
            "Ters kare ilişkisinde uzaklığı iki katına çıkarıp kuvveti yarıya indirmek.",
        ],
        "diagnostic_questions": [
            "Bağıntıdaki her harfin yerine koyduğun değeri tek tek söyler misin; bu değer hangi cisme ait?",
            "Bu bağıntıdaki açı, hangi iki doğru arasındaki açı?",
            "Aynı sonucu orantı kurarak (kaç katına çıkar?) bulsan sonuç aynı mı?",
            "Katsayıyı unutmadığını nasıl sınarsın (özel durum, birim)?",
        ],
        "remediation_strategy": [
            "Öğrenciden bağıntıyı yerine koymadan önce her sembolün anlamını ve ilgili cismi yazmasını iste.",
            "Orantı yoluyla ikinci bir çözüm yaptırıp iki sonucu karşılaştır (çapraz kontrol).",
            "Açı içeren bağıntılarda şekil çizdirip açının hangi doğrular arasında olduğunu işaretlet.",
            "Uç durumla sına: θ = 0° ve 90° için bağıntı fiziksel olarak mantıklı mı?",
            "Hatalı uygulamayı bilinçli olarak içeren bir çözümü öğrenciye bulduracak 'hata avı' görevi ver.",
        ],
        "recommended_question_families": ["ff-kinematics-v0zero", "friction-incline-coefficient", "horizontal-circle", "wire-force-magnitude-angle",
                                          "illum-inverse-square", "accelerating-frame-pendulum"],
        "related_error_types": ["FORMULA_SELECTION_ERROR", "ALGEBRA_ERROR", "VECTOR_ERROR"],
    },
    {
        "code": "SIGN_ERROR", "name_tr": "İşaret / yön hatası",
        "definition": "Pozitif yön seçimi tutarsızdır ya da bir niceliğin işareti (ivme, kuvvet bileşeni, yük işareti, akım yönü) yanlış atanır; "
                      "büyüklük doğru, yön ya da işaret yanlıştır.",
        "symptoms": [
            "Yukarı atışta yön değişince ivmenin işaretini de değiştirmek.",
            "Tümsek köprü tepesinde mg − N yerine N − mg yazmak.",
            "Eğik kuvvette düşey bileşeni normal kuvvete eklemek yerine çıkarmak (ya da tersi).",
            "Negatif yüke etki eden kuvveti alan yönünde çizmek.",
            "Telin ağırlığı ile manyetik kuvveti yönlerine bakmadan toplamak.",
            "İndüksiyon alanını dış alanla aynı yönde almak (Lenz yasasının işareti).",
        ],
        "diagnostic_questions": [
            "Hangi yönü pozitif seçtin? Soru boyunca hepsini bu yöne göre mi yazdın?",
            "Bu kuvvet merkeze doğru mu, merkezden dışarı mı? Merkeze doğru olanı pozitif almışsın, öyleyse bu terimin işareti ne olmalı?",
            "Yük negatif olunca kuvvet ile alan yönü arasında ne değişir?",
            "Sonucun işareti fiziksel olarak mantıklı mı (ör. normal kuvvet negatif çıkabilir mi)?",
        ],
        "remediation_strategy": [
            "Problem başında pozitif yönü ve ok yönünü şekil üzerinde zorunlu olarak işaretlet.",
            "Her kuvveti 'bileşen = işaret × büyüklük' olarak yazdır; ΣF denklemini tek yön üzerinden kurdur.",
            "Sonuç işaretini fiziksel anlamla sınat: negatif normal kuvvet temasın kesildiğini gösterir gibi.",
            "Yön kuralı (sağ el, Lenz, yük işareti) için ayrı küçük bir kontrol listesi oluşturt.",
            "Yönü bilerek ters seçip aynı sonucun çıktığını göstererek 'seçim keyfi, tutarlılık zorunlu' ilkesini yerleştir.",
        ],
        "recommended_question_families": ["ff-upward-throw", "hump-bridge", "friction-angled-force", "wire-force-balance-dynamics",
                                          "coulomb-collinear-net-force", "vertical-circle-tension"],
        "related_error_types": ["VECTOR_ERROR", "FBD_ERROR", "CONCEPTUAL_ERROR"],
    },
    {
        "code": "UNIT_ERROR", "name_tr": "Birim hatası",
        "definition": "Birim dönüşümü yapılmaz ya da yanlış yapılır; farklı birimde verilen büyüklükler aynı denklemde birleştirilir; birimin fiziksel "
                      "büyüklükle eşleşmesi karıştırılır (cd, lm, lx; Wb, T).",
        "symptoms": [
            "cm cinsinden yakalama mesafesini m'ye çevirmeden g = 10 m/s² ile işleme sokmak.",
            "Dakikadaki devir sayısını saniyeye çevirmeden ω ya da f hesaplamak.",
            "Alanı cm² ile verip emk hesabında m²'ye çevirmemek.",
            "Işık şiddeti (cd), ışık akısı (lm), aydınlanma (lx) birimlerini niceliklerle yanlış eşleştirmek.",
            "Uzaklığı cm olarak ters kare ilişkisinde kullanıp m ile verilen değerle karıştırmak.",
        ],
        "diagnostic_questions": [
            "Her verinin birimini yazarak tablo kurar mısın?",
            "Sonucun birimi ne çıkıyor; istenen birimle aynı mı?",
            "1 cm² kaç m²'dir? (Çevirme katsayısı 100 mü, 10 000 mi?)",
            "lx hangi niceliğin birimi, hangisinin değil?",
        ],
        "remediation_strategy": [
            "İşleme girmeden önce tüm verileri SI'ya çevirme alışkanlığı kazandır.",
            "Çevirme çarpanlarını üsler ile yazdır (cm² = 10⁻⁴ m²) ve alan/hacim için kare/küp etkisini göster.",
            "Boyut analiziyle sonucun birimini önceden tahmin ettir.",
            "Aynı problemi iki farklı birim sisteminde çözdürüp sonuçların aynı fiziksel değere gittiğini göster.",
        ],
        "recommended_question_families": ["ff-reaction-time-ruler", "circular-kinematics", "illum-inverse-square", "induction-emf-ratio-calc",
                                          "sm-experiment-data-analysis"],
        "related_error_types": ["CARELESS_ERROR", "ARITHMETIC_ERROR", "FORMULA_SELECTION_ERROR"],
    },
    {
        "code": "VECTOR_ERROR", "name_tr": "Vektör hatası",
        "definition": "Vektörel nicelikler skaler gibi toplanır, bileşenlere ayırma sırasında sin/cos karıştırılır ya da yön belirleme kuralı "
                      "(sağ el, bileşke yönü) yanlış uygulanır.",
        "symptoms": [
            "Çarpma hızını bileşenlerin cebirsel toplamı olarak yazmak (Pisagor yerine).",
            "Eğik düzlemde mg'nin bileşenlerinde sin ile cos'u karıştırmak.",
            "İki elektriksel alanın büyüklüklerini yönlerine bakmadan toplamak.",
            "Sağ el kuralında baş parmak ile dört parmağın rolünü değiştirmek.",
            "Düzgün çembersel harekette hız vektörünü merkeze doğru çizmek.",
            "Düzlem aynada cisim–görüntü göreli hızını tek hız olarak almak.",
        ],
        "diagnostic_questions": [
            "Bu nicelik skaler mi vektörel mi? Vektörse yönü nereye bakıyor?",
            "Açı hangi iki doğru arasında, bu açıyla komşu bileşen sin mi cos mu?",
            "Bileşkenin büyüklüğü bileşenlerin büyüklükleri toplamından büyük olabilir mi?",
            "Sağ elinle bunu göstererek yapar mısın: baş parmak ne, dört parmak ne?",
        ],
        "remediation_strategy": [
            "Önce vektörü ölçekli ok olarak çizdirip bileşenleri paralelkenar/üçgen yöntemiyle bulundur.",
            "θ = 0° ve 90° uç durumlarıyla sin/cos seçimini sınat ('açıya komşu = cos').",
            "Bileşke büyüklüğü için üçgen eşitsizliğini (|a−b| ≤ R ≤ a+b) kontrol aracı olarak kullandır.",
            "Elle yön kuralı için aynı kuralı iki farklı durumda fiziksel olarak canlandırt.",
            "Vektörleri bileşen bileşen (x ve y ayrı) toplayan tabloyu alışkanlık yap.",
        ],
        "recommended_question_families": ["2d-velocity-at-point", "2d-angled-launch", "banked-curve", "wire-field-superposition",
                                          "efield-superposition-collinear", "pm-moving-object-image", "wire-field-direction-rhr", "loop-force-directions"],
        "related_error_types": ["SIGN_ERROR", "PREREQUISITE_GAP", "FORMULA_APPLICATION_ERROR"],
    },
    {
        "code": "GRAPH_READING_ERROR", "name_tr": "Grafik okuma hatası",
        "definition": "Grafik, yol/şekil olarak (resim gibi) okunur; eğim, değer ve alan karıştırılır; eksenlerin ve bölgelerin anlamı yanlış yorumlanır.",
        "symptoms": [
            "ϑ–t yerine x–t grafiğinin eğimini ivme sanmak; grafiği hareketin resmi sanmak.",
            "Φ–t grafiğinde Φ'nin değerini emk saymak (eğim yerine yükseklik).",
            "f–F grafiğinde maksimum statik eşik ile kinetik düzeyi karıştırmak.",
            "Limit hıza yaklaşırken eğimin azalmasını hızın azalması sanmak.",
            "Doğrusal olmayan grafiği (F–d) doğrusal orantı gibi yorumlamak.",
            "Osiloskopta sıfır geçişleri ve periyodu sayarken kareleri yanlış okumak.",
        ],
        "diagnostic_questions": [
            "Bu grafikte yatay ve düşey eksen neyi gösteriyor, birimi ne?",
            "Aradığın şey grafiğin değeri mi, eğimi mi, altındaki alan mı?",
            "Eğim burada hangi fiziksel niceliği verir? Bu nicelik hangi noktada en büyük?",
            "Grafiğin 'resmi' ile cismin gerçek yolu aynı mı?",
        ],
        "remediation_strategy": [
            "Eksenleri sözlü olarak okutup 'bu grafik hareketin resmi değil, nicelikler arası ilişki' vurgusunu yap.",
            "Aynı hareketin x–t, ϑ–t, a–t grafiklerini birlikte çizdir; üçü arasında dönüşüm yapmayı öğret.",
            "Eğim ve alanın birim analizini (ör. Wb/s = V) yaptırarak fiziksel anlamı çıkar.",
            "Grafikteki özel noktalarda (tepe, kesişim, eşik) neyin sıfır, neyin maksimum olduğunu tablo ile doldurt.",
            "Gerçek veriden grafik çizdirip yorumlatan kısa deney ya da simülasyon kullan.",
        ],
        "recommended_question_families": ["ff-motion-graphs", "friction-applied-force-graph", "terminal-velocity-graph", "induction-flux-time-graphs",
                                          "ac-loop-graphs", "2d-component-graphs"],
        "related_error_types": ["TABLE_READING_ERROR", "CONCEPTUAL_ERROR", "PREREQUISITE_GAP"],
    },
    {
        "code": "TABLE_READING_ERROR", "name_tr": "Tablo / veri okuma hatası",
        "definition": "Veri tablosu yanlış yorumlanır: iki değişkenin aynı anda değiştiği satırlar karşılaştırılır, ardışık fark yerine değerin kendisi "
                      "kullanılır, sütunlar karıştırılır.",
        "symptoms": [
            "Konum tablosunda ardışık farklar yerine konum değerlerine bakıp ivmeyi yorumlamak.",
            "Hem yükün hem uzaklığın değiştiği satırlardan tek değişkenin etkisini çıkarmaya çalışmak.",
            "Sürtünme tablosunda yüzey alanı ve normal kuvveti birlikte değiştiren satırları karşılaştırmak.",
            "Oran okurken birincil–ikincil (ya da cisim–görüntü) sütunlarını karıştırmak.",
            "Tek satırdan genelleme yapmak.",
        ],
        "diagnostic_questions": [
            "Hangi iki satırı karşılaştırıyorsun? Bu iki satırda sadece bir değişken mi değişiyor?",
            "Tabloda ardışık değerlerin farkı sabit mi, oranı mı sabit?",
            "Sütun başlıkları ve birimleri ne? Cisim mi görüntü mü, birincil mi ikincil mi?",
            "Bu sonucu tek bir satıra mı dayandırıyorsun?",
        ],
        "remediation_strategy": [
            "Kontrol değişkeni kuralıyla (yalnız bir değişken değişir) uygun satır çiftlerini seçtir.",
            "Fark tablosu (Δ) ve oran tablosu sütunları eklettir.",
            "Bulduğu ilişkiyi bir başka satır çiftinde sınatarak genelleme yapmayı öğret.",
            "Sütun başlıklarına sembol ve birim ekleyip yeniden yazdır.",
        ],
        "recommended_question_families": ["ff-data-pattern-g", "coulomb-data-table-graph", "friction-variables-data", "drag-variables-data",
                                          "solenoid-data-model", "sm-experiment-data-analysis", "circular-variables-data"],
        "related_error_types": ["EXPERIMENT_DESIGN_ERROR", "GRAPH_READING_ERROR", "QUESTION_INTERPRETATION_ERROR"],
    },
    {
        "code": "ALGEBRA_ERROR", "name_tr": "Cebirsel işlem hatası",
        "definition": "Fiziksel model ve bağıntı doğrudur; denklemin düzenlenmesi, karekök/üs alma, denklem sistemi çözümü ya da oran sadeleştirmesi "
                      "sırasında cebir hatası yapılır.",
        "symptoms": [
            "ϑ² = 2gh denkleminde karekök almayı unutmak.",
            "İkinci dereceden denklemde negatif/pozitif kök seçimini yanlış yapmak.",
            "İki bilinmeyenli ivme–gerilme denklem sisteminde yerine koymayı hatalı yapmak.",
            "Oran kurarken payı paydayı karıştırmak (ters orantı).",
            "Kütle sadeleşen denklemde kütleyi son sonuca taşımak.",
        ],
        "diagnostic_questions": [
            "Bu adımda denklemin iki tarafına ne yaptın?",
            "Bulduğun ifadeyi geriye yerine koyup orijinal denklemi sağlıyor mu?",
            "İki kökten hangisi fiziksel olarak anlamlı, neden?",
            "Sadeleşmesi gereken büyüklük gerçekten sadeleşti mi?",
        ],
        "remediation_strategy": [
            "Önce sembolik çözüm yaptır, sayıyı en son yerleştirt.",
            "Her adımın sonunda geriye yerine koyma kontrolü alışkanlığı kazandır.",
            "Birim kontrolüyle cebir adımlarını sına (kareköke karşılık gelen birim).",
            "Fiziksel anlamsız kökleri eleme gerekçesini yazılı hale getirt.",
        ],
        "recommended_question_families": ["ff-kinematics-v0zero", "ff-upward-throw", "connected-bodies-same-acceleration", "coupled-wheels",
                                          "friction-horizontal-dynamics"],
        "related_error_types": ["ARITHMETIC_ERROR", "FORMULA_APPLICATION_ERROR", "PREREQUISITE_GAP"],
    },
    {
        "code": "ARITHMETIC_ERROR", "name_tr": "Aritmetik hata",
        "definition": "Kavram, bağıntı ve cebir doğru olmasına rağmen sayısal işlemde (çarpma, bölme, yuvarlama, trigonometrik değer) hata yapılır.",
        "symptoms": [
            "sin30° değerini 0,87 almak.",
            "Çarpanları çarpmak yerine toplamak (2·2 yerine 2+2 gibi) ya da tersi.",
            "Filtre geçirgenliklerini çarpmak yerine toplamak.",
            "Gerekli ampul sayısını yuvarlarken aşağı yuvarlamak (yeterli aydınlanma koşulu).",
            "Özel açıların (30°, 37°, 53°, 60°) trigonometrik değerlerini karıştırmak.",
        ],
        "diagnostic_questions": [
            "Bu çarpmayı tek tek yazar mısın?",
            "Sonucun büyüklük mertebesi mantıklı mı (yaklaşık hesapla sına)?",
            "sin30° ile cos30°'u bir dik üçgen çizerek bulabilir misin?",
            "Yuvarlama yönün sorunun koşuluyla uyumlu mu?",
        ],
        "remediation_strategy": [
            "Yaklaşık hesapla büyüklük mertebesi kontrolü iste.",
            "Trigonometrik değerleri 3-4-5 ve 30-60-90 üçgenleriyle yeniden kurdur.",
            "Orantısal düşünmeyi (kaç katına çıktı?) aritmetik yerine geçirt.",
            "Hesap makinesi/zihinden hesap sonuçlarını iki yolla doğrulat.",
        ],
        "recommended_question_families": ["wire-force-magnitude-angle", "wire-field-ratio", "illum-filters-multiple-sources", "lamp-lumen-efficiency",
                                          "pm-self-view-mirror-length"],
        "related_error_types": ["CARELESS_ERROR", "ALGEBRA_ERROR", "UNIT_ERROR"],
    },
    {
        "code": "QUESTION_INTERPRETATION_ERROR", "name_tr": "Soruyu yanlış yorumlama",
        "definition": "Soru kökü, şekil ya da koşul yanlış okunur: ihmal edilen etki (hava direnci), neyin istendiği, hangi cismin/uzaklığın "
                      "kastedildiği ya da 'her zaman' gibi ifadelerdeki istisna gözden kaçar.",
        "symptoms": [
            "'Hava direnci ihmal edilir' koşulunu görmeyip ağır cismi daha hızlı düşürmek.",
            "Cisim–ayna uzaklığı yerine cisim–göz ya da cisim–görüntü uzaklığını kullanmak.",
            "Şebeke gerilimi yerine cihaz etiketindeki değeri kullanmak.",
            "'Her zaman gerçektir' ifadesinde çukur aynada odak içi istisnayı denetlememek.",
            "Birincil ve ikincil bobini karıştırmak.",
        ],
        "diagnostic_questions": [
            "Sorunun istediği tam olarak ne? Kendi cümlenle yeniden söyler misin?",
            "Soruda verilen koşullardan hangisini kullanmadın?",
            "Şekilde hangi uzaklık ölçülüyor, nereden nereye?",
            "'Her zaman' dediği ifadeye bir karşı örnek bulabilir misin?",
        ],
        "remediation_strategy": [
            "Soruyu yeniden anlat ve verilenleri/istenenleri işaretletme alışkanlığı kazandır.",
            "Koşul sözcüklerini (ihmal, sabit, yalnızca, her zaman) renkle işaretlet.",
            "Şekli kendi çizimiyle yeniden oluşturup uzaklıkları üzerinde etiketlet.",
            "'Her zaman/asla' ifadelerinde karşı örnek aramayı alışkanlık yap.",
        ],
        "recommended_question_families": ["ff-mass-independence", "terminal-velocity-daily-life", "transformer-applications-record",
                                          "sm-image-position-properties", "pm-field-of-view", "illum-oblique-angle"],
        "related_error_types": ["CARELESS_ERROR", "CONCEPTUAL_ERROR", "TABLE_READING_ERROR"],
    },
    {
        "code": "METHOD_SELECTION_ERROR", "name_tr": "Yöntem seçme hatası",
        "definition": "Konuya uygun çözüm stratejisi seçilemez: bileşenlerin bağımsızlığı yerine tek denklem, simetri yerine hesap, "
                      "ışın çiziminde normal çizmeden yansıtma, ya da eşit olan niceliğin yanlış belirlenmesi.",
        "symptoms": [
            "Uçuş süresini yatay hareketten bulmaya çalışmak.",
            "Aynı noktadan iki kez geçen cismin tepeye çıkış süresini t₂ − t₁ saymak.",
            "Kayışla bağlı tekerlerde açısal hızı eşit, bağlı eş eksenli tekerlerde çizgisel hızı eşit saymak.",
            "Normali çizmeden ışını yüzeyin simetriği olarak yansıtmak.",
            "Üst üste bloklarda ortak ivmeyi bulmadan üst blok için sürtünmeyi hesaplamak.",
        ],
        "diagnostic_questions": [
            "Bu soruyu çözmek için hangi büyüklüğü önce bulman gerekiyor?",
            "Hangi nicelikler iki hareket/cisim arasında eşit, hangileri farklı?",
            "Simetri kullanarak çözülebilir mi?",
            "Bu çizimde ilk adım ne olmalıydı (normal, odak, merkez)?",
        ],
        "remediation_strategy": [
            "Çözüm planını yazdır: 'önce ..., sonra ...'. Planı hesaptan önce sınat.",
            "Benzer ama yöntemi farklı iki problemi yan yana koyup ayırt edici özelliği buldur.",
            "Eşit olan niceliği bağlantı türünden (kayış / eş eksen) çıkartan kural tablosu oluşturt.",
            "Işın çizimlerinde 'önce normal' gibi sabit sıralama kuralı yazdır.",
        ],
        "recommended_question_families": ["ff-passing-point-twice", "2d-horizontal-launch", "coupled-wheels", "friction-stacked-blocks-together",
                                          "pm-reflection-ray-paths", "sm-arbitrary-ray-path"],
        "related_error_types": ["CONCEPTUAL_ERROR", "FORMULA_SELECTION_ERROR", "PREREQUISITE_GAP"],
    },
    {
        "code": "PREREQUISITE_GAP", "name_tr": "Önkoşul bilgi eksikliği",
        "definition": "Hata, 11. sınıf konusundan değil önceki sınıflardan ya da matematikten gelen eksik bilgiden kaynaklanır: trigonometri, "
                      "vektör toplama, orantı, periyot–frekans, elektrik akımı–direnç ilişkisi.",
        "symptoms": [
            "Hız vektörünü bileşenlerine ayırırken trigonometrik oranları kuramamak.",
            "Doğru/ters/karesel orantıyı ayırt edememek.",
            "Periyot ile frekansı ters orantılı bilmemek.",
            "Akım, direnç ve gerilim ilişkisini (V = iR) bilmediği için manyetik alan zincirini kuramamak.",
            "Yatay–düşey bileşenlerin bağımsızlığını 10. sınıf bilgisi olarak bilmemek.",
        ],
        "diagnostic_questions": [
            "Bu soruda kullandığın matematiksel araç ne? Onu tek başına küçük bir örnekle yapabilir misin?",
            "Frekans iki katına çıkarsa periyot ne olur, neden?",
            "Bir dik üçgende sinüs hangi kenarların oranı?",
            "Akımı artırmak için hangi büyüklükleri değiştirebiliriz?",
        ],
        "remediation_strategy": [
            "Önkoşulu 3–4 dakikalık izole mini-sınavla ayırt et (konudan bağımsız).",
            "Eksik önkoşulu somut fiziksel bağlamda yeniden kur (ör. trigonometriyi bileşen çiziminde).",
            "Ön kavramın yeniden eksik olmadığını kısa aralıklı tekrar ile sına.",
            "Asıl konuya, önkoşul bağlı alt basamağın doğru çözüldüğünü gördükten sonra dön.",
        ],
        "recommended_question_families": ["ac-factors-identification", "2d-angled-launch", "wire-field-ratio", "friction-angled-force", "circular-kinematics"],
        "related_error_types": ["CONCEPTUAL_ERROR", "ALGEBRA_ERROR", "VECTOR_ERROR"],
    },
    {
        "code": "CARELESS_ERROR", "name_tr": "Dikkat hatası",
        "definition": "Öğrenci konuyu bilir; ancak dikkatsizlik, acele ya da okuma/yazma kaymasıyla yanlış yapar. Aynı soru bir sonraki seferde "
                      "doğru çözülür ve hata örüntüsü tutarlı değildir.",
        "symptoms": [
            "Kuvvetlerden birini (normal ya da sürtünme) eksik çizmek.",
            "Çap ile yarıçapı karıştırmak.",
            "Birimkareli şekilde f ve r'yi ters sayarak konum belirlemek.",
            "Ayna yazısında harfleri çevirmeyip yalnız satır sırasını tersine çevirmek.",
            "Gelme açısını θ yerine 90° − θ almak.",
        ],
        "diagnostic_questions": [
            "Aynı soruyu yavaşça bir daha çözer misin?",
            "Şekilde verilen değerleri bir de sen işaretleyerek gözden geçirir misin?",
            "Bu sorudaki hangi adımı daha önce başka bir soruda doğru yaptın?",
            "Hata örüntüsü var mı, yoksa rastlantısal mı?",
        ],
        "remediation_strategy": [
            "Aynı hatanın ikinci bir sorunun içinde tekrarlanıp tekrarlanmadığını kontrol ederek örüntüyü ayırt et.",
            "Basit kontrol listesi (şekil, birim, yön, kuvvet sayısı) kullandır.",
            "Hatayı kendisinin bulmasını sağla (çözümde 'hata avı').",
            "Zaman baskısı varsa tempoyu ayarlayıp kontrol süresini planla.",
        ],
        "recommended_question_families": ["fbd-identify-forces", "circular-kinematics", "pm-retroreflector", "sm-basic-elements", "pm-image-properties"],
        "related_error_types": ["ARITHMETIC_ERROR", "UNIT_ERROR", "QUESTION_INTERPRETATION_ERROR"],
    },
    # ------------------------- Fizikte ayırt edici ek türler (gerekçeli, 3 adet) -------------------------
    {
        "code": "FBD_ERROR", "name_tr": "Serbest cisim diyagramı hatası",
        "definition": "Programın merkezî becerisi olan serbest cisim diyagramında (FİZ.11.1.5) kuvvetlerin belirlenmesi hatası: olmayan kuvvet eklemek "
                      "(hareket kuvveti, merkezkaç, çift sayım), olan kuvveti çizmemek, kuvveti uygulayan/maruz kalan cismi karıştırmak. "
                      "CONCEPTUAL_ERROR'dan ayrılmasının nedeni, çözümün ilk ve zorunlu adımı olması ve tanısının çizimle yapılabilmesidir.",
        "symptoms": [
            "Hareket yönünde ayrı bir 'itme / hareket kuvveti' oku çizmek.",
            "Merkezcil kuvveti diyagramda ayrı bir kuvvet olarak çizmek.",
            "Cismin başka cisme uyguladığı kuvveti de diyagrama eklemek (etki–tepki çift sayımı).",
            "Eğik düzlemde normal kuvveti ağırlığa eşit çizmek.",
            "Normal ya da sürtünme kuvvetini hiç çizmemek.",
            "İp gerilmesini asılı cismin ağırlığı kadar çizmek (sistem ivmeliyken).",
        ],
        "diagnostic_questions": [
            "Bu okun kuvvetini hangi cisim uyguluyor? Bu cisim neresinde?",
            "Cismin temas ettiği her yüzeyi saydın mı? Her temasta hangi kuvvetler olabilir?",
            "Bu kuvvetin tepkisi hangi cisme etki ediyor; o diyagramda yer alır mı?",
            "Bu diyagramla cismin ivmesi hangi yönde çıkıyor; gözlediğinle uyuşuyor mu?",
        ],
        "remediation_strategy": [
            "Önce cismi çevreden ayır (kapalı çizgi); sonra çizgiyi kesen her temas ve uzaktan etkiyi say.",
            "Her ok için 'uygulayan cisim' etiketini zorunlu kıl; uygulayan cismi söyleyemediği oku sildir.",
            "Gravitasyon + temas kuralı: önce ağırlık, sonra her temas için normal ve sürtünme.",
            "Diyagramdan ΣF yönünü okuyup gözlenen ivmeyle karşılaştır.",
            "Hatalı diyagram içeren 'bulmaca' (hata avı) çözdürt.",
        ],
        "recommended_question_families": ["fbd-identify-forces", "fbd-equilibrium-tension", "frictionless-incline", "connected-bodies-same-acceleration",
                                          "apparent-weight-elevator", "friction-wall-press"],
        "related_error_types": ["CONCEPTUAL_ERROR", "VECTOR_ERROR", "SIGN_ERROR"],
    },
    {
        "code": "SCOPE_CONFUSION", "name_tr": "Kapsam / eski müfredat yöntemi karışıklığı",
        "definition": "Öğrenci 11. sınıf Maarif programının kapsam sınırlarını aşan ya da eski müfredattan kalma yöntem ve terimleri kullanır: "
                      "'düşey/yatay/eğik atış' ezber formülleri, Coulomb/alan sayısal hesabı, ayna–mercek denklemi, görünür derinlik formülü. "
                      "Bu tür bir hata öğrencinin bilgisizliğinden değil, yöntemin bu programda aranmamasından kaynaklanır.",
        "symptoms": [
            "Menzil ve maksimum yükseklik için ezber formül (R = ϑ₀² sin2θ / g) kullanıp bileşen–bağımsızlık yaklaşımını göstermemek.",
            "Coulomb kuvveti ve elektriksel alan sorularında sayısal sonuç aramak (program oran ve yorum düzeyinde).",
            "Küresel ayna/mercek görüntü konumunu ayna denklemi (1/f = 1/p + 1/q) ile bulmaya çalışmak.",
            "Görünür derinliği formülle hesaplamaya çalışmak (program yalnız nitel).",
            "Limit hız için sayısal hesap yapmak (program yalnız değişken yorumu).",
            "Transformatörde sarım–gerilim–akım sayısal hesabı beklemek.",
        ],
        "diagnostic_questions": [
            "Bu soruda ışın çizimi ile ya da orantı ile çözebilir miydin?",
            "Bu formülü nereden öğrendin; sınıfta bu soruya hangi yöntemle yaklaşmıştınız?",
            "Sayı vermeden, yalnız 'kaç katına çıkar?' diye düşünerek çözebilir misin?",
            "Bu soruda çizimin ve ölçeğin rolünü açıklar mısın?",
        ],
        "remediation_strategy": [
            "Önce programın bu çıktıda hangi yöntemi beklediğini (çizim, oran, yorum) kısaca belirt.",
            "Ezber formüle gerek kalmayan eşdeğer çözümü (bileşenler, simetri, ışın çizimi, orantı) kurdur.",
            "Eski formülün yalnız özel bir durum olduğunu göster; genel yöntemi önceliklendir.",
            "Aynı soruyu yöntemi değiştirerek iki kez çözdürüp sonucun tutarlılığını sınat.",
        ],
        "recommended_question_families": ["ff-downward-throw-or-moving-carrier", "coulomb-ratio-generalization", "efield-point-charge-ratio",
                                          "transformer-turns-voltage-current-ratio", "sm-focal-length-dependence", "sm-image-ray-construction-grid"],
        "related_error_types": ["METHOD_SELECTION_ERROR", "FORMULA_SELECTION_ERROR", "CONCEPTUAL_ERROR"],
    },
    {
        "code": "EXPERIMENT_DESIGN_ERROR", "name_tr": "Deney tasarımı / kanıt değerlendirme hatası",
        "definition": "Programın deney, veri ve kanıt çıktılarında (FBAB1, FBAB7, FBAB8, FBAB12, KB2.6) karşılaşılan yöntem hatası: kontrol değişkenini "
                      "sabit tutmamak, aynı anda birden fazla bağımsız değişkeni değiştirmek, tek ölçümle genelleme, kaynak güvenilirliğini sorgulamamak. "
                      "TABLE_READING_ERROR'dan farkı, hatanın veriyi okurken değil deneyi/araştırmayı kurarken olmasıdır.",
        "symptoms": [
            "Cisim konumu ve ayna türünü aynı anda değiştirerek veri toplamak.",
            "Yüzey alanı ile normal kuvveti birlikte değiştirip sürtünmeye alanın etkisini çıkarmak.",
            "Tek ölçümü yeterli saymak, tekrarı gereksiz görmek.",
            "Reklam amaçlı ürün sayfasını ya da yazarı belirsiz siteyi güvenilir kaynak saymak.",
            "Ölçülen niceliği kontrol değişkenleri arasında listelemek.",
            "Doğrulanmamış bilgiyi doğrulama basamağını atlayarak kaydetmek.",
        ],
        "diagnostic_questions": [
            "Bu deneyde neyi değiştiriyorsun, neyi ölçüyorsun, neyi sabit tutuyorsun?",
            "Aynı anda iki şeyi değiştirirsen sonucu hangisine bağlarsın?",
            "Tek ölçüm yeterli mi? Ölçümü tekrarlarsan neyi öğrenirsin?",
            "Bu kaynağı kim hazırlamış, ne amaçla? Başka bir kaynakla doğrulayabilir misin?",
        ],
        "remediation_strategy": [
            "Bağımsız–bağımlı–kontrol değişkeni tablosunu önceden yaptır.",
            "'Tek değişken' kuralını, iki değişkenin birlikte değiştiği örnekle çatışma yaratarak göster.",
            "Ölçüm tekrarı ve ortalama kavramını küçük bir etkinlikle (ölçüm dağılımı) yaşat.",
            "Kaynak değerlendirme ölçütlerini (yazar, tarih, amaç, ikinci kaynakla teyit) kontrol listesi yap.",
            "Hatalı bir deney kurgusu verip hataları bulmasını iste.",
        ],
        "recommended_question_families": ["sm-experiment-design", "magnet-data-collection", "friction-variables-data", "drag-variables-data",
                                          "induction-experiment-factors", "fcage-source-and-search", "emag-source-and-search"],
        "related_error_types": ["TABLE_READING_ERROR", "METHOD_SELECTION_ERROR", "QUESTION_INTERPRETATION_ERROR"],
    },
]

# ============================================================================================
# BÖLÜM 2 — KAVRAM YANILGILARI: ÜNİTE 1 (KUVVET VE HAREKET, FİZ.11.1.1–FİZ.11.1.10)
# ============================================================================================
# Ünite 1'e özgü ek kaynaklar (her biri bu çalışmada bulunup okunmuştur; okuma düzeyi citation içinde yazılıdır).
SRC.update({
    "MC83": _s("McCloskey, M. (1983). Intuitive physics. Scientific American, 248(4), 122–130. [ERIC kayıt sayfası ve özeti okundu: "
               "katılımcıların hareketi Newton öncesi 'impetus' (itki) kuramına benzer biçimde açıklaması]",
               "https://eric.ed.gov/?id=EJ277094", 2, True),
    "DUR21": _s("Durkaya, F. (2021). Matematik öğretmen adaylarının serbest cisim diyagramı gösterimine ilişkin performans değerlendirmesi. Fen, "
                "Matematik, Girişimcilik ve Teknoloji Eğitimi Dergisi, 4(1), 60–80. [tam metin okundu; 33 öğretmen adayı: eğik düzlemde normal "
                "kuvveti 16'sı gösterdi, 17'si unuttu ya da göz ardı etti; düzgün dairesel harekette merkezcil kuvveti 9'u dışa yönelik çizdi]",
                "https://dergipark.org.tr/en/download/article-file/1291648", 2, True),
    "YK22": _s("Yüzbaşıoğlu, M. K. & Kurnaz, M. A. (2022). Ortaokul öğrencilerinin kuvvetin ölçülmesi ve sürtünme ünitesine yönelik alternatif "
               "fikirlerinin incelenmesi: skor analizi. Mehmet Akif Ersoy Üniversitesi Eğitim Fakültesi Dergisi, 61, 1–22. [tam metin okundu; "
               "140 beşinci sınıf öğrencisi; en az doğru yanıtlanan soru sürtünme kuvvetinin yönüyle ilgili (%19,29)]",
               "https://dergipark.org.tr/tr/download/article-file/1922462", 2, True),
    "BL23": _s("Boudreaux, A. & Lindsey, B. (2023). Investigation of student reasoning about air resistance and terminal speed behavior of falling "
               "objects. APS April Meeting 2023 (bildiri özeti, bibcode 2023APS..APRF17006B). [yalnızca arama özeti görüldü: öğrenciler kesit "
               "alanı gibi tek değişkene odaklanıyor ve kuvvet dengesiyle çelişen yanıtlar veriyor; sayfa açılamadı]",
               "https://ui.adsabs.harvard.edu/abs/2023APS..APRF17006B/abstract", 2, False),
})


_U1_START = len(MISCONCEPTIONS)

# --- FİZ.11.1.1–FİZ.11.1.2: Serbest düşme ---
MISCONCEPTIONS += [
    MC("heavier-falls-faster",
       "Ağır cisim, hafif cisimden daha büyük ivmeyle düşer; bu yüzden önce yere ulaşır.",
       "Hava direncinin ihmal edildiği ortamda serbest düşen tüm cisimlerin ivmesi aynıdır (g). Cisme etki eden tek kuvvet ağırlığıdır; "
       "a = mg/m = g olduğundan kütle sadeleşir. Kütle büyüdükçe çeken kuvvet büyür, ama hızlandırılması gereken eylemsizlik de aynı oranda büyür.",
       ["serbest-dusme", "yer-cekimi-ivmesi", "kutle", "agirlik"], LO("1.1", "1.2"), "CONCEPTUAL_ERROR",
       "ff-mass-independence ailesinin çeldiricileri: 'ağır cisim daha büyük ivmeyle düşer / önce yere ulaşır' ve 'kütle iki katına çıkınca düşme "
       "süresi yarıya iner'. FCI taksonomisinde G3 (heavier objects fall faster). Veri tablosu ve ϑ–t sorularında da ivmenin kütleye bağlandığı seçenekler.",
       DI("Havası boşaltılmış uzun bir tüpün tepesinden 2 kg'lık demir bilya ile 20 g'lık plastik bilya aynı anda, ilk hızsız bırakılıyor. "
          "Bilyaların tüpün dibine varma süreleri t_demir ve t_plastik ile gösterilirse hangisi doğrudur?",
          "t_demir < t_plastik; çünkü demir bilyanın ağırlığı çok daha büyüktür.",
          "t_demir = t_plastik; çünkü ikisinin de ivmesi g'dir.",
          "t_demir > t_plastik; çünkü demir bilyanın eylemsizliği daha büyüktür.",
          "t_demir = t_plastik; çünkü havasız ortamda cisimlere hiçbir kuvvet etki etmez.",
          "t_demir, t_plastik'in yüzde biri kadardır; çünkü kütle oranı 100'dür.",
          "B", "A"),
       RM(["Havasız tüpte demir bilyaya hangi kuvvetler etki ediyor? Plastik bilyaya?",
           "Demir bilyanın ağırlığı plastik olanınkinin 100 katı. Newton'un 2. yasasında ivmeyi yalnız kuvvet mi belirler, yoksa başka bir nicelik de var mı?",
           "İki plastik bilyayı birbirine yapıştırıp bırakırsak kütle iki katına çıkar. Sistem daha hızlı mı düşer? Neden?",
           "Havalı ortamda yaprak neden yavaş düşer? Bunu farklı kılan kuvvet ağırlık mı, başka bir şey mi?"],
          "Ay'da (havasız ortam) çekiç ile tüy aynı yükseklikten aynı anda bırakıldığında birlikte yere düşer; oysa çekicin ağırlığı tüyünkinden çok daha büyüktür.",
          "Bir kişiyi iten tek arkadaş ile iki kişiyi iten iki arkadaş: kişi başına düşen itme aynı olduğundan ivme değişmez. Ağırlık bu 'itme' gibidir; "
          "kütle büyüdükçe hem itici kuvvet hem de itilen kütle aynı oranda büyür."),
       S("FCI", "POTV23", "FERR17"), "HIGH"),

    MC("speed-up-means-accel-up",
       "Serbest düşen cismin hızı arttığı için ivmesi de artar (hız ile ivme karıştırılır).",
       "Hava direncinin ihmal edildiği serbest düşmede ivme sabit g'dir: hız eşit zaman aralıklarında eşit miktarda artar (yaklaşık her saniye 10 m/s). "
       "İvme, hızın büyüklüğüne değil hızın değişme hızına bağlıdır; ϑ–t grafiğinde sabit eğimli doğru çizilir.",
       ["serbest-dusme", "yer-cekimi-ivmesi", "ivme", "hiz"], LO("1.1", "1.2"), "CONCEPTUAL_ERROR",
       "ff-data-pattern-g ailesinin 'hızlar arttığı için ivme de artıyor' çeldiricisi; ff-motion-graphs ve ff-kinematics-v0zero sorularında "
       "ivmenin zamanla arttığını düşünen seçenekler. FCI taksonomisinde K2 (velocity–acceleration undiscriminated) ve AF5.",
       DI("Bir gezegende serbest düşen cismin hızı saniyede bir ölçülüyor: t = 0'da 0, 1 s'de 4 m/s, 2 s'de 8 m/s, 3 s'de 12 m/s. "
          "Bu gezegende cismin ivmesi için hangisi söylenir?",
          "Zamanla artar; çünkü hız her saniye daha büyük bir değere ulaşıyor.",
          "Sabit ve 4 m/s²'dir; çünkü hız her saniye 4 m/s artıyor.",
          "Sabit ve 12 m/s²'dir; çünkü 3. saniyede hız 12 m/s'dir.",
          "Zamanla artar; çünkü her saniyede alınan yol bir öncekinden fazladır.",
          "Verilerden bulunamaz; çünkü cismin kütlesi verilmemiştir.",
          "B", "A"),
       RM(["İvme neyi ölçer: hızın kendisini mi, hızın değişme hızını mı?",
           "Tablodaki her saniyedeki hız artışını yan yana yaz. Bu sayılar değişiyor mu?",
           "Hız iki katına çıkınca ivme de iki katına çıkıyor mu? ϑ–t grafiğini çizsen eğim nasıl olurdu?",
           "Sabit 100 km/sa hızla giden bir arabanın ivmesi nedir?"],
          "Sabit 100 km/sa ile giden araba büyük hızlıdır ama ivmesi sıfırdır; durgun hâlden her saniye 4 m/s artan araba küçük hızlıdır ama ivmesi vardır. "
          "'Hız büyükse ivme büyüktür' düşüncesi bu iki araba karşısında çöker.",
          "Hız, su deposundaki seviyeye; ivme ise musluğun debisine benzer. Seviye yüksek olabilir ama musluk kapalıysa (ivme sıfır) seviye değişmez; "
          "musluk sabit akıyorsa seviye eşit aralıklarla yükselir."),
       S("FCI", "HH85", "BEI94"), "HIGH"),

    MC("apex-accel-zero",
       "Yukarı atılan cisim tepe noktasında anlık durduğu için ivmesi de sıfırdır (cisim dengededir).",
       "Tepe noktasında hız anlık olarak sıfırdır, ancak cisme ağırlığı etki etmeye devam eder; net kuvvet mg ve aşağı yönlüdür, ivme g'dir (hava direnci ihmal). "
       "Hızın sıfır olması ivmenin sıfır olmasını gerektirmez; ivme hızın değişme hızıdır ve hız tepede işaret değiştirmektedir.",
       ["tepe-noktasi-hareket", "serbest-dusme", "ivme", "hiz"], LO("1.2", "1.3"), "CONCEPTUAL_ERROR",
       "ff-upward-throw ve ff-motion-graphs ailelerinin 'tepe noktasında ivme sıfırdır / a–t grafiğinde ivme sıfıra iner' çeldiricileri; "
       "2d-angled-launch'ta tepe noktasında ivme sıfır seçeneği. FCI K2 ve Clement (1982) yukarı atılan madeni para sorusu.",
       DI("Hava direncinin ihmal edildiği ortamda dik yukarı fırlatılan bir top yükselip tepe noktasına ulaşıyor. "
          "Topun tepe noktasındaki anı için hangisi doğrudur? (g = 10 m/s², yukarı yön pozitif)",
          "Hızı sıfır, ivmesi sıfırdır.",
          "Hızı sıfır, ivmesi 10 m/s² büyüklüğünde ve aşağı yönlüdür.",
          "Hızı sıfır, ivmesi 10 m/s² büyüklüğünde ve yukarı yönlüdür.",
          "Hızı sıfır, ivmesi 5 m/s² ve aşağı yönlüdür; çünkü ivme yükselirken azalmıştır.",
          "Hızı sıfır; ivme yükselirken 10 m/s², tepede sıfır, inerken tekrar 10 m/s² olur.",
          "B", "A"),
       RM(["Tepe noktasında topa etki eden kuvvetleri çiz. Ağırlık kayboldu mu?",
           "Bir saniye sonra top ne yapıyor? Hızı hangi yönde ve sıfırdan farklı mı?",
           "Hızın sıfırdan aşağı yönlü bir değere geçmesi için bir ivme gerekir mi?",
           "ϑ–t grafiğinde t = tepe anında eğim ne kadar? Grafik orada kırılıyor mu?"],
          "İvme sıfır olsaydı net kuvvet de sıfır olurdu ve top tepede havada asılı kalırdı (Newton'ın 1. yasası). Oysa top bir an sonra aşağı iner; "
          "öyleyse ivme tepede sıfır olamaz.",
          "Salıncağın en yüksek noktasında salıncak bir an durur ama hemen geri döner; durması, o anda net kuvvetin sıfır olduğu anlamına gelmez."),
       S("CLEM", "FCI", "HH85"), "HIGH"),

    MC("upward-motion-needs-upward-force",
       "Elden çıktıktan sonra yukarı giden cisme 'atma kuvveti' gibi yukarı yönlü bir kuvvet etki eder; yer çekimi bu kuvveti yenince cisim durur.",
       "Elden çıkan cisme yalnızca ağırlığı (aşağı yönlü) etki eder; hava direnci ihmal edildiğinde yukarı yönlü kuvvet yoktur. Yukarı yönlü hareket kuvvetten değil "
       "ilk hızdan (eylemsizlikten) gelir; net kuvvet aşağı yönlü olduğundan hız yukarı yönde azalır.",
       ["tepe-noktasi-hareket", "serbest-dusme", "newton-birinci-yasa", "bileske-kuvvet"], LO("1.2", "1.4"), "CONCEPTUAL_ERROR",
       "ff-upward-throw ve fbd-identify-forces ailelerinde 'hareket yönünde ayrı bir hareket kuvveti oku'; yukarı atılan cisim için serbest cisim diyagramı. "
       "Clement (1982) madeni para atışı ve FCI taksonomisinde I3 (impetus dissipation) ile AF2 (motion implies active force).",
       DI("Elinizden dik yukarı fırlattığınız bir taş elden çıktıktan sonra yükselirken (hava direnci ihmal) taşa etki eden kuvvetler için hangisi doğrudur?",
          "Yalnızca aşağı yönlü ağırlık kuvveti etki eder.",
          "Aşağı yönlü ağırlık ile ağırlıktan büyük, sabit, yukarı yönlü bir kuvvet etki eder.",
          "Aşağı yönlü ağırlık ile yukarı yönlü bir kuvvet etki eder; yukarı kuvvet başlangıçta ağırlıktan büyüktür, giderek azalır.",
          "Yalnızca yukarı yönlü bir kuvvet etki eder; ağırlık taş durduktan sonra etkili olmaya başlar.",
          "Aşağı yönlü ağırlık ile ona eşit yukarı yönlü kuvvet etki eder; net kuvvet sıfırdır.",
          "A", "C"),
       RM(["Taş elinden ayrıldı. Taşa dokunan herhangi bir cisim var mı? Yukarı iten kuvveti hangi cisim uyguluyor?",
           "Bir kuvvetten söz edebilmek için o kuvveti uygulayan bir cisim bulunması gerekir mi?",
           "Taşa yalnızca aşağı yönlü net kuvvet etki ediyorsa ivme hangi yönde olur? Hız yukarı yönlü iken azalması bununla uyumlu mu?",
           "Yerçekimsiz uzayda elinizle ittiğiniz top, elinizden çıktıktan sonra ne yapar?"],
          "Taş elden çıktığı anda temas biter; 'yukarı kuvveti' uygulayan hiçbir cisim gösterilemez. Kuvvet olmadan da cisim hareketini sürdürebilir; "
          "bu yüzden yukarı yönlü hareket yukarı yönlü kuvvetin kanıtı sayılamaz.",
          "Buz üzerinde itilen paten elden ayrıldıktan sonra kayar: itme bittiği hâlde hareket sürer. Hareketin devamı 'saklı bir itmeden' değil, eylemsizlikten gelir."),
       S("CLEM", "FCI", "MC83"), "HIGH"),

    MC("carrier-release-v0-zero",
       "Hareket eden bir taşıyıcıdan (uçak, yükselen balon, koşan kişi) bırakılan cismin ilk hızı sıfırdır; cisim bırakıldığı noktanın hemen altına düşer.",
       "Bırakılan cisim, bırakıldığı anda taşıyıcının hızına sahiptir ve hava direnci ihmal edildiğinde yatay (ya da düşey) hız bileşenini korur. "
       "Sabit hızla giden taşıyıcının tam altında kalarak düşer; yükselen balondan bırakılan cisim ise başlangıçta yukarı yönlü hızla hareket eder.",
       ["serbest-dusme", "hiz", "bilesenlerin-bagimsizligi", "newton-birinci-yasa"], LO("1.2", "1.3"), "CONCEPTUAL_ERROR",
       "ff-downward-throw-or-moving-carrier çeldiricileri 'bırakılan cismin ilk hızı sıfırdır' ve 'yukarı çıkan balondan bırakılan cisim hemen aşağı düşer'; "
       "2d-moving-reference-launch'ta 'top atıldığı noktanın gerisine düşer'. McCloskey (1983) impetus açıklamaları.",
       DI("Sabit 8 m/s hızla yatay doğrultuda uçan bir drondan bir paket bırakılıyor; drone hızını koruyarak uçmaya devam ediyor ve hava direnci ihmal ediliyor. "
          "Yerdeki bir gözlemciye göre paketin hareketi için hangisi doğrudur?",
          "Paket bırakıldığı noktanın tam altına düşer; drone ilerlemeye devam eder.",
          "Paket, dronun tam altında kalarak düşer ve dronun bulunduğu noktanın altına çarpar.",
          "Paket dronun gerisinde kalır; çünkü bırakılınca yatay hızı giderek azalır.",
          "Paket dronun önüne geçer; çünkü bırakılınca drondan daha hızlı hareket eder.",
          "Paket yalnızca düşey doğrultuda 8 m/s ilk hızla aşağı atılmış gibi hareket eder.",
          "B", "A"),
       RM(["Paket dronun altına bağlıyken yatay hızı kaçtı? Bırakılınca bu hız hangi kuvvetle yok olur?",
           "Hava direncinin ihmal edildiği ortamda pakete yatay doğrultuda hangi kuvvet etki ediyor?",
           "Hareket eden trende bozuk para bıraksanız ayağınıza mı düşer, trenin gerisine mi?",
           "Yatay ve düşey hareket birbirini etkiler mi, yoksa ayrı ayrı mı incelenebilir?"],
          "Hareket eden bir trende elinizdeki bozuk para ayağınızın dibine düşer, trenin gerisine düşmez. Para bırakılır bırakılmaz hızı sıfırlansaydı geride kalırdı.",
          "Koşarken havaya zıplayan kişi geriye düşmez; zıplarken koşu hızını korur ve koşuya devam eder. Bırakılan paket de taşıyıcının hızını 'yanında götürür'."),
       S("MC83", "HH85", "TB"), "MEDIUM"),

    MC("xt-graph-as-trajectory",
       "Konum–zaman grafiği cismin izlediği yolun resmidir: ters U şeklinde bir grafik, cismin bir tepeye tırmanıp indiği anlamına gelir.",
       "Grafiğin yatay ekseni zamandır, cismin yatay konumu değil. Düşey doğrultuda yukarı atılıp aynı yere dönen cismin konum–zaman grafiği ters U (parabol) olur "
       "ama hareket tek bir düşey doğru boyuncadır. Grafiğin eğimi anlık hızı verir; tepede eğim sıfırdır, yani hız anlık sıfırdır.",
       ["hareket-grafikleri", "grafik-egim-alan", "serbest-dusme", "konum"], LO("1.2"), "GRAPH_READING_ERROR",
       "ff-motion-graphs ve ff-data-evidence ailelerinde konum–zaman grafiğinin yorumlanması; 'grafiği resim sanma' (graph-as-picture) "
       "Beichner (1994) kinematik grafik yorumlama testinin bilinen hata kategorisidir.",
       DI("Düşey yukarı fırlatılıp aynı noktaya dönen bir cismin yer–zaman (y–t) grafiği ters U (parabol) biçimindedir. Bu grafikle ilgili hangisi doğrudur?",
          "Cisim önce eğri bir yokuşa tırmanır, sonra aşağı kayar; yörünge parabolik bir eğridir.",
          "Cisim düşey bir doğru boyunca hareket eder; grafiğin tepesinde eğim sıfır olduğu için hız anlık sıfırdır.",
          "Grafiğin tepesinde eğim sıfır olduğundan cismin ivmesi de o anda sıfırdır.",
          "Cisim yükselirken hızı sabittir; çünkü grafik düzgün biçimde yükselmektedir.",
          "Grafik parabol olduğundan cisim aynı zamanda yatay doğrultuda da hareket etmektedir.",
          "B", "A"),
       RM(["Grafiğin yatay ekseni neyi gösteriyor? Cismin kendisi yatay doğrultuda mı hareket ediyor?",
           "t = 0 ve t = T anlarında cisim nerede? Aradaki yolculuğu bir yan kamerayla çekseydin cisim hangi yolu izlerdi?",
           "Grafiğin bir noktadaki eğimi hangi fiziksel niceliği verir? Tepedeki eğim kaç?",
           "Eğim sıfırsa ivme de sıfır mıdır? Eğimin değişmesi neyi anlatır?"],
          "Stroboskopla çekilmiş düşey hareketin ardışık konumlarını zaman ekseni boyunca yan yana dizersen ters U çıkar; oysa cisim aynı düşey doğru üzerinde gidip gelmiştir. "
          "Grafik, cismin yolundan farklı bir şeydir.",
          "Günlük sıcaklık–zaman grafiğindeki tepe noktası havanın gerçekten bir tepeye tırmandığı anlamına gelmez; grafik zamanla değişimi anlatır, yolu değil."),
       S("BEI94", "TB"), "HIGH"),

    MC("vt-height-vs-slope",
       "Hız–zaman grafiğinde çizginin o anki yüksekliği (değeri) ivmedir; çizgi yüksekteyse ivme büyük, eksene yaklaşınca küçüktür.",
       "İvme, hız–zaman grafiğinin eğimidir; çizginin yüksekliği hızı verir. Yukarı yönlü fırlatılan cismin ϑ–t grafiği, yukarı yön pozitif alındığında, tüm yolculuk "
       "boyunca eğimi sabit (−g) olan tek bir doğrudur; hızın sıfırdan geçtiği noktada bile eğim değişmez.",
       ["hareket-grafikleri", "grafik-egim-alan", "ivme", "serbest-dusme"], LO("1.2", "1.3"), "GRAPH_READING_ERROR",
       "ff-motion-graphs ve 2d-component-graphs ailelerinde ϑ–t grafiğinden ivme okuma; 'eğim ile yüksekliği karıştırma' Beichner (1994)'te belgelenmiş hata kategorisidir.",
       DI("Düşey doğrultuda fırlatılan bir cismin, yukarı yön pozitif alınarak çizilen hız–zaman grafiği; t = 0'da +20 m/s'den başlayıp t = 2 s'de sıfırdan, "
          "t = 4 s'de −20 m/s'den geçen bir doğrudur (g = 10 m/s², hava direnci ihmal). Bu grafikten ivme için hangisi söylenir?",
          "İvme t = 0'da 20 m/s², t = 2 s'de 0, t = 4 s'de −20 m/s²'dir.",
          "İvme 0–4 s boyunca değişmez ve −10 m/s²'dir; t = 2 s'de de −10 m/s²'dir.",
          "İvme t = 2 s'ye kadar −10 m/s², sonrasında +10 m/s²'dir; çünkü hız işaret değiştirir.",
          "İvme t = 2 s'de sıfırdır; çünkü doğru eksene o anda temas eder.",
          "Eğim hızı verir; ivme ancak grafikle eksen arasındaki alanla bulunabilir.",
          "B", "A"),
       RM(["Hız–zaman grafiğinde dikey eksen hangi niceliği gösterir? İvmenin tanımı ne?",
           "Grafikte t = 0 ve t = 2 s noktalarını seç: hız farkını süre farkına böl. Kaç buluyorsun?",
           "Çizgi çok yüksekte ama tamamen yatay olsaydı (sabit hız) ivme kaç olurdu?",
           "Bu doğrunun eğimi 0–4 s boyunca değişiyor mu? Eksenle kesiştiği noktada eğim farklı mı?"],
          "'Yükseklik = ivme' kuralıyla t = 0'da 20 m/s², t = 4 s'de −20 m/s² bulunur; oysa cisme etki eden kuvvet (ağırlık) hiç değişmemiştir ve ivme her an −10 m/s²'dir.",
          "3000 m yükseklikteki düz bir yaylada yol yataydır; yükseklik (deniz seviyesinden uzaklık) ile yokuşun dikliği (eğim) farklı şeylerdir."),
       S("BEI94", "TB"), "HIGH"),
]

# --- FİZ.11.1.3–FİZ.11.1.4: İki boyutta sabit ivmeli hareket; Newton'ın hareket yasaları ---
MISCONCEPTIONS += [
    MC("horizontal-speed-changes-fall-time",
       "Yatay doğrultuda ilk hızı büyük olan cisim yere daha geç (ya da daha erken) düşer; yatay hız düşey hareketi etkiler.",
       "Yatay ve düşey hareket bileşenleri birbirinden bağımsızdır. Aynı yükseklikten yatay fırlatılan cismin yere varış süresi yalnızca yüksekliğe ve g'ye bağlıdır; "
       "yatay hızdan bağımsızdır ve aynı yükseklikten serbest bırakılan cismin süresine eşittir. Yatay hız yalnızca yatay ilerleme miktarını (menzili) değiştirir.",
       ["bilesenlerin-bagimsizligi", "ucus-suresi", "iki-boyutta-sabit-ivmeli-hareket", "serbest-dusme"], LO("1.3"), "CONCEPTUAL_ERROR",
       "2d-horizontal-launch ailesinin 'yatay hızı büyük olan cisim daha geç yere düşer' çeldiricisi; 2d-component-data ve 2d-launch-onto-incline-or-steps "
       "sorularında yatay hıza bağlanan uçuş süresi seçenekleri.",
       DI("Aynı masanın kenarından, aynı anda özdeş iki bilyadan biri sessizce bırakılıyor, diğeri 6 m/s yatay hızla fırlatılıyor (hava direnci ihmal). "
          "Bilyaların yere varış süreleri sırasıyla t_1 (bırakılan) ve t_2 (fırlatılan) ise hangisi doğrudur?",
          "t_2 > t_1; çünkü fırlatılan bilya daha uzun bir yol alır.",
          "t_2 = t_1; çünkü düşey hareket iki bilya için de aynıdır.",
          "t_2 < t_1; çünkü yatay hızı olan bilya yere daha büyük hızla çarpar.",
          "t_2 = t_1; çünkü iki bilyanın toplam hızı da aynıdır.",
          "Hangisinin önce düşeceği yatay hızın değerine bağlıdır; verilen bilgiyle karşılaştırılamaz.",
          "B", "A"),
       RM(["Fırlatılan bilyaya düşey doğrultuda hangi kuvvet etki ediyor? Bu kuvvet yatay hız değişince değişir mi?",
           "Yere varış süresini hangi doğrultudaki hareket belirler: yüksekliği aşmak mı, yatayda ilerlemek mi?",
           "Yatay hızı iki katına çıkarsan hangisinin değişmesini beklersin: süre mi, yatay ilerleme mesafesi mi?",
           "Stroboskopla iki bilyanın ardışık konumlarını işaretlesen, aynı anlarda aynı yükseklikte olurlar mı?"],
          "Masanın kenarından aynı anda bırakılan ve yatay fırlatılan iki bilyanın stroboskop görüntüsünde bilyalar her anda aynı yükseklikte yer alır ve birlikte yere çarpar. "
          "Yatay hızın süreyi uzattığı düşüncesi bu görüntüyü açıklayamaz.",
          "Hareket eden bir trenin içinde yukarı zıplayan yolcunun havada kalma süresi trenin hızına bağlı değildir; yatay ilerleme ile yukarı-aşağı hareket birbirinden bağımsızdır."),
       S("HH85", "MC83", "TB"), "MEDIUM"),

    MC("two-stage-path-then-vertical",
       "Yatay hızla fırlatılan cisim önce bir süre yatay gider, yatay itki bitince dik biçimde aşağı düşer; yörüngesi 'L' biçimindedir.",
       "Yer çekimi, cisim elden ya da masadan ayrıldığı andan itibaren etki eder. Hava direnci ihmal edildiğinde yatay hız sabit kalırken düşey hız düzgün artar; "
       "iki hareket aynı anda gerçekleşir ve yörünge parabolik bir eğridir.",
       ["parabolik-yorunge", "bilesenlerin-bagimsizligi", "iki-boyutta-sabit-ivmeli-hareket", "newton-birinci-yasa"], LO("1.3"), "CONCEPTUAL_ERROR",
       "2d-horizontal-launch ve 2d-component-graphs ailelerinde yörünge çizimi; 2d-launch-onto-incline-or-steps'te 'cisim ilk basamağa düşer' çeldiricisi. "
       "FCI taksonomisinde G5 (yer çekimi impetus tükenince etki eder) ve I3/I4 (impetusun azalması, gecikmeli oluşması).",
       DI("Bir bilye yatay bir masanın kenarından yuvarlanarak ayrılıp havada hareket ediyor (hava direnci ihmal). "
          "Bilyenin masadan ayrıldıktan sonraki hareketi için hangisi doğrudur?",
          "Önce bir süre yatay doğrultuda ilerler, sonra düşey olarak aşağı düşer.",
          "Yatay hızı sabit kalırken düşey hızı artar; yörüngesi paraboldür.",
          "Yatay hızı giderek azalıp sıfırlanır, ardından serbest düşme yapar.",
          "Hem yatay hem düşey hızı sabittir; yörüngesi eğik bir doğrudur.",
          "Düşey hızı sabittir, yatay hızı giderek artar.",
          "B", "A"),
       RM(["Bilye masadan ayrıldığı anda ağırlığı etkisini yitiriyor mu? Ağırlık ne zaman devreye giriyor?",
           "Masadan ayrılan bilyeye yatay doğrultuda hangi kuvvet etki ediyor (hava ihmal)? Yatay hızı kim azaltsın?",
           "Önce yatay gidip sonra dik düşseydi bilyenin yolu nasıl görünürdü? Yatay atılan bir topun fotoğrafı buna benziyor mu?",
           "İki hareket aynı anda gerçekleşiyorsa yolun şekli nasıl olur?"],
          "Yatay atılan bir topun stroboskop fotoğrafında 'L' biçimli bir yol değil, pürüzsüz bir eğri görülür; çünkü elden ya da masadan çıkar çıkmaz yer çekimi cismi aşağı doğru hızlandırır.",
          "Nehirde karşıya yüzen kişiyi akıntı yana taşırken kürekleri karşıya götürür; iki etki aynı anda gerçekleşir, kişi önce akıntıyla sonra karşıya gitmez."),
       S("FCI", "MC83", "HH85"), "HIGH"),

    MC("resultant-velocity-scalar-sum",
       "İki boyutlu harekette bir andaki bileşke hız, yatay ve düşey hız bileşenlerinin cebirsel toplamıdır (v = v_x + v_y).",
       "Yatay ve düşey bileşenler birbirine dik vektörlerdir; bileşke hızın büyüklüğü v = √(v_x² + v_y²), yönü tanθ = v_y/v_x ile bulunur. "
       "Büyüklükler yalnızca bileşenler aynı doğrultudaysa cebirsel olarak toplanır.",
       ["vektor-bilesenleri", "cizgisel-hiz", "vektorel-nicelik", "iki-boyutta-sabit-ivmeli-hareket"], LO("1.3"), "VECTOR_ERROR",
       "2d-velocity-at-point ailesinin 'bileşke hız bileşenlerin toplamıdır' çeldiricisi; 2d-horizontal-launch'ta 'çarpma hızı yalnız düşey hızdır' çeldiricisi. "
       "FCI taksonomisinde K3 (nonvectorial velocity composition).",
       DI("Hava direncinin ihmal edildiği ortamda yatay doğrultuda fırlatılan bir cismin, belirli bir anda yatay hız bileşeni 6 m/s, düşey hız bileşeni 8 m/s'dir. "
          "Cismin o andaki hızının büyüklüğü kaç m/s'dir?",
          "14", "10", "2", "48", "7",
          "B", "A"),
       RM(["Yatay ve düşey hız bileşenleri birbirine göre hangi açıyla duruyor?",
           "Bir kişi 6 m doğuya, ardından 8 m kuzeye yürüyor. Başlangıç noktasından kaç metre uzaktadır? 14 m mi?",
           "Bu iki hız bileşenini bir dik üçgenin dik kenarları olarak çiz. Bileşke hız hangi kenara karşılık gelir?",
           "Bileşenlerin cebirsel toplamı bileşke büyüklüğe hangi özel durumda eşit olur?"],
          "6 m doğuya sonra 8 m kuzeye yürüyen kişi başlangıçtan 14 m değil 10 m uzaktadır. Hız da yer değiştirme gibi vektördür; dik bileşenlerde toplama cebirsel değildir.",
          "Dikdörtgen bir parkın köşegeni boyunca yürümek, iki kenarı dolaşmaktan kısadır: 6 + 8 = 14 m yerine yalnızca 10 m yürürsünüz."),
       S("FCI", "WJL23", "TB"), "HIGH"),

    MC("motion-requires-net-force",
       "Bir cismin hareketini sürdürmesi için hareket yönünde bir kuvvet gerekir; sabit hızla giden cisme hareket yönünde net kuvvet etki eder, kuvvet yoksa cisim durur.",
       "Net kuvvet sıfırsa cisim durgunluğunu ya da sabit hızlı hareketini sürdürür (Newton'ın 1. yasası). Sabit hızla giden cisimde motor gibi bir itme sürtünme ve "
       "direnç kuvvetlerini dengeler, net kuvvet sıfırdır. Net kuvvet hızı korumaz; hızı değiştirir.",
       ["newton-birinci-yasa", "eylemsizlik", "bileske-kuvvet", "kuvvet"], LO("1.4", "1.5"), "CONCEPTUAL_ERROR",
       "newton1-inertia ailesinin 'hareket eden cismin hareketini sürdürmesi için kuvvet gerekir' çeldiricisi; net-force-motion-state ve fbd-identify-forces'ta "
       "hareket yönünde ayrı bir 'hareket kuvveti' oku. FCI taksonomisinde AF2 (motion implies active force), I1 ve AF3; Türkiye'de de en sık görülen yanılgılar arasındadır.",
       DI("Sürtünmesi ihmal edilemeyen yatay bir yolda bir araba, motorunun uyguladığı kuvvetle sabit 20 m/s hızla gidiyor. Araca etki eden net kuvvet için hangisi doğrudur?",
          "Hareket yönündedir ve büyüklüğü motorun uyguladığı kuvvete eşittir.",
          "Sıfırdır; motorun uyguladığı kuvvet, sürtünme ve direnç kuvvetlerinin toplamına eşittir.",
          "Hareket yönündedir; çünkü motor kuvveti sürtünmeden büyük olmalıdır.",
          "Hareket yönünün tersindedir ve büyüklüğü sürtünme kuvvetine eşittir.",
          "Büyüklüğü 20 m/s ile orantılı bir değerdir ve hareket yönündedir.",
          "B", "A"),
       RM(["Araca etki eden bütün kuvvetleri çiz. Kaç tane var, yönleri nasıl?",
           "Motor kapatılınca araç ne yapar? Yavaşlamasına hangi kuvvet neden olur?",
           "Sürtünmesiz buz üzerinde kayan bir diskin hareketini sürdürmesi için bir kuvvet gerekir mi?",
           "Hızı sabit olan bir cismin ivmesi kaçtır? Newton'ın 2. yasasına göre net kuvvet ne olur?"],
          "Buz üzerinde itilen disk elden ayrıldıktan sonra uzun süre kayar; hareket kuvvetle sürseydi disk hemen dururdu. Disk durmaz, çünkü ona etki eden net kuvvet çok küçüktür.",
          "Motoru kapatılan bir uzay aracı uzayda sonsuza kadar sürüklenir: durması için 'hareket kuvveti' değil, onu durduracak bir kuvvet gerekir."),
       S("FCI", "CLEM", "TK16", "KGU05"), "HIGH"),

    MC("constant-net-force-constant-velocity",
       "Bir cisme sabit bir net kuvvet uygulanırsa cisim sabit hızla hareket eder (hız kuvvetle orantılıdır); kuvvet iki katına çıkınca hız iki katına çıkar.",
       "Net kuvvet ivmeyi belirler (F = ma): sabit net kuvvet sabit ivme, yani hızın düzgün artması demektir. Hız, kuvvetle değil kuvvetin etki süresiyle (v = at) ve kütleyle ilişkilidir.",
       ["newton-ikinci-yasa", "bileske-kuvvet", "hiz", "ivme", "kutle"], LO("1.4"), "CONCEPTUAL_ERROR",
       "net-force-motion-state ve newton2-f-m-a-relations ailelerinde kuvvet–hız ilişkisi; friction-horizontal-dynamics'te sabit itme altında hızın sabit kaldığı seçenekler. "
       "FCI taksonomisinde AF4 (velocity proportional to applied force) ve K2.",
       DI("Sürtünmesiz yatay düzlemde durgun hâlden başlayan 4 kg'lık bir cisme yatay doğrultuda sabit 8 N'luk net kuvvet uygulanıyor. Kuvvetin 3 s boyunca etkimesinden sonra cismin hızı kaç m/s olur?",
          "2 m/s; çünkü sabit kuvvet sabit hız oluşturur ve hız F/m'dir.",
          "6 m/s; çünkü a = F/m = 2 m/s² olup hız her saniye 2 m/s artar.",
          "24 m/s; çünkü hız kuvvet ile süre çarpımına (8·3) eşittir.",
          "8 m/s; çünkü hız kuvvetle aynı sayısal değere sahiptir.",
          "12 m/s; çünkü hız F·t / 2 ile bulunur.",
          "B", "A"),
       RM(["Aynı cisme 1 s sonra ve 3 s sonra bakarsan hızı aynı mıdır? Kuvvet değişmediği hâlde hız değişiyorsa kuvvet neyi belirliyor?",
           "F = ma'daki ivme hangi niceliğin değişimidir?",
           "Kuvvet iki katına çıkarsa hız mı iki katına çıkar, yoksa hızın artış hızı mı?",
           "Aynı kuvvetle itilen kızağın hızı 1 s ve 10 s sonra aynı olur mu?"],
          "Sürtünmesiz buzda sabit bir kuvvetle itilen kızak her saniye biraz daha hızlanır. Sabit kuvvet sabit hız verseydi kızak itildiği anda son hızına ulaşır ve hızlanma hiç görülmezdi.",
          "Banka hesabına her ay aynı tutarda para yatırmak gibi: yatırılan miktar (kuvvet) bakiyenin (hızın) değişme miktarını belirler, bakiyenin kendisini değil."),
       S("FCI", "CLEM", "TB"), "HIGH"),

    MC("heavier-exerts-bigger-force",
       "İki cisim etkileştiğinde (çarpışma, itme) büyük kütleli olan küçük kütleliye daha büyük kuvvet uygular.",
       "Etki ve tepki kuvvetleri her durumda büyüklükçe eşit, zıt yönlüdür ve farklı cisimlere etki eder (Newton'ın 3. yasası). Kütle, kuvvetin büyüklüğünü değil, "
       "o kuvvetin cisimlerde oluşturduğu ivmeyi belirler.",
       ["etki-tepki", "kutle", "kuvvet", "newton-ikinci-yasa"], LO("1.4"), "CONCEPTUAL_ERROR",
       "newton3-action-reaction ailesinin 'büyük kütleli cisim daha büyük kuvvet uygular' çeldiricisi. FCI taksonomisinde AR1 (greater mass implies greater force); "
       "Aygün ve Tan (2021) çarpışmada bu yanılgının ders sonrasında bile sürdüğünü gösterir.",
       DI("Sürtünmesiz yatay yolda 1200 kg'lık bir kamyonet, durmakta olan 300 kg'lık bir arabaya çarpıp onu itiyor. Çarpışma sırasında kamyonetin arabaya uyguladığı "
          "kuvvet F_1, arabanın kamyonete uyguladığı kuvvet F_2 ise hangisi doğrudur?",
          "F_1 = 4F_2; çünkü kamyonetin kütlesi daha büyüktür.",
          "F_1 = F_2; ancak araba, kamyonetten daha büyük büyüklükte ivme kazanır.",
          "F_1 = F_2 ve iki cismin ivmesinin büyüklüğü de eşittir.",
          "F_1 < F_2; çünkü daha hafif olan araç çarpışmada daha çok sarsılır.",
          "F_1 = F_2; ancak bu kuvvetler birbirini dengelediği için iki cisim de ivmelenmez.",
          "B", "A"),
       RM(["İki araç arasındaki etkileşimde toplam kaç kuvvet var? Hangi cisme etki ediyorlar?",
           "Kamyonet arabaya daha çok kuvvet uygulasaydı, arabanın kamyoneti 'geri itmesi' neden daha az olsun? Bu durum etkileşimin simetrisiyle uyumlu mu?",
           "Çarpışmada küçük aracın 'daha çok sarsılması' hangi büyüklüğün farkıdır: kuvvetin mi, ivmenin mi?",
           "a = F/m'de aynı F için kütlesi küçük olan cismin ivmesi nasıl olur?"],
          "Farklı kütleli iki arabaya aynı yatay doğrultuda bağlanmış iki kuvvet ölçer, ne kadar farklı kütleli olursalar olsunlar, her zaman aynı değeri gösterir.",
          "El sıkışırken iki kişinin birbirine uyguladığı sıkma kuvveti, kişi ağır ya da hafif olsun, her zaman eşittir; farklı olan, el sıkışmanın kişileri ne kadar sarstığıdır."),
       S("AT21", "FCI", "TK16"), "HIGH"),

    MC("action-reaction-cancel",
       "Etki ve tepki kuvvetleri eşit ve zıt olduğu için birbirini dengeler; bu yüzden cisimler kuvvet uygulanarak hareket ettirilemez.",
       "Etki ve tepki kuvvetleri farklı cisimlere etki eder; bu yüzden aynı serbest cisim diyagramında birlikte bulunmaz ve birbirini dengeleyemez. "
       "Bir cismin ivmesi yalnızca o cisme etki eden net kuvvete bağlıdır.",
       ["etki-tepki", "bileske-kuvvet", "serbest-cisim-diyagrami", "newton-ikinci-yasa"], LO("1.4", "1.5"), "CONCEPTUAL_ERROR",
       "newton3-action-reaction ailesinin 'etki-tepki kuvvetleri birbirini dengeler' çeldiricisi; fbd-identify-forces'ta cismin başka cisme uyguladığı kuvvetin diyagrama eklenmesi. "
       "Temiz ve Kızılcık (2016) 'etki ve tepki aynı cisme etki eder' görüşünü lise düzeyinde sık görülen yanılgılar arasında sayar.",
       DI("Sürtünmesiz zeminde durgun bir arabayı bir kişi elleriyle ileri itiyor. Newton'ın 3. yasasına göre araba da kişiyi aynı büyüklükte geri itiyor. "
          "Araba bu durumda neden yine de hızlanabilir?",
          "Etki ve tepki kuvvetleri birbirini dengelediği için net kuvvet sıfırdır; araba yalnızca ilk anda hareket eder.",
          "Etki ve tepki farklı cisimlere (araba ve kişi) etki eder; arabaya yalnızca kişinin itmesi etki ettiğinden araba üzerinde net kuvvet vardır.",
          "Kişi arabaya, arabanın kişiye uyguladığından daha büyük bir kuvvet uygular.",
          "Tepki kuvveti etkiden biraz sonra oluştuğundan arabaya kısa bir süre etki etmez.",
          "Araba kişiden hafif olduğu için kişiye uyguladığı tepki kuvveti daha küçüktür.",
          "B", "A"),
       RM(["Kişiyi geri iten kuvvet hangi cisme etki ediyor? Arabanın hareketini belirlerken hangi kuvvetlere bakarsın?",
           "Arabanın serbest cisim diyagramını çiz. Kişiyi iten tepki kuvveti bu diyagramda yer alıyor mu?",
           "Eşit ve zıt iki kuvvetin birbirini dengelemesi için hangi koşul gerekir?",
           "Atın arabayı çekmesi: at–araba etkileşimi ile at–zemin etkileşimini ayrı ayrı değerlendir. Atı ileri götüren kuvvet hangisidir?"],
          "Etki ve tepki birbirini dengeleseydi, itilen kapı, tekmelenen top ya da yürüyen insan hiç hızlanamazdı. Oysa hepsi hızlanır; demek ki bu kuvvetler aynı cisme etki etmiyor.",
          "Buz üzerindeki iki patenciden biri diğerini iterse, ikisi de zıt yönlerde hızlanır: her biri yalnızca kendisine uygulanan kuvvetle ivmelenir."),
       S("TK16", "KGU05"), "HIGH"),

    MC("weight-normal-are-action-reaction",
       "Masa üstünde duran cisme etki eden ağırlık ile normal kuvvet, eşit ve zıt oldukları için Newton'ın 3. yasasındaki etki-tepki çiftidir.",
       "Ağırlık Dünya'nın cisme çekim kuvvetidir; tepkisi cismin Dünya'yı çekmesidir. Normal kuvvet masanın cisme uyguladığı temas kuvvetidir; tepkisi cismin masaya uyguladığı itmedir. "
       "Ağırlık ve normal kuvvet aynı cisme etki eder; durgun cisimde eşit olmaları Newton'ın 1. yasasının sonucudur ve ivmeli sistemlerde eşit olmayabilir.",
       ["etki-tepki", "agirlik", "normal-kuvvet", "newton-birinci-yasa"], LO("1.4", "1.5"), "CONCEPTUAL_ERROR",
       "newton3-action-reaction ailesinin 'ağırlık ve normal kuvvet etki-tepki çiftidir' çeldiricisi; apparent-weight-elevator ve fbd-identify-forces'ta ağırlık ile normal kuvvetin her koşulda eşit sanılması.",
       DI("Yatay masa üzerinde durgun bir kitap için hangi iki kuvvet Newton'ın 3. yasasındaki etki-tepki çiftidir?",
          "Kitabın ağırlığı ile masanın kitaba uyguladığı normal kuvvet.",
          "Dünya'nın kitaba uyguladığı çekim kuvveti ile kitabın Dünya'ya uyguladığı çekim kuvveti.",
          "Masanın kitaba uyguladığı normal kuvvet ile masanın yere uyguladığı kuvvet.",
          "Masanın kitaba uyguladığı normal kuvvet ile kitabın Dünya'ya uyguladığı çekim kuvveti.",
          "Kitabın masaya uyguladığı kuvvet ile yerin masaya uyguladığı kuvvet.",
          "B", "A"),
       RM(["Bir etki-tepki çifti hangi iki cisim arasındaki etkileşimi anlatır? Ağırlığın kaynağı kim?",
           "Ağırlığın tepkisini bul: Dünya'ya kim, hangi kuvveti uyguluyor?",
           "Kitap ivmeyle yükselen bir asansörde olsaydı ağırlık ile normal kuvvet hâlâ eşit olur muydu?",
           "Ağırlık ve normal kuvvet aynı cisme mi, farklı cisimlere mi etki ediyor?"],
          "Masa çekilirse kitap serbest düşer: normal kuvvet kaybolur ama ağırlık sürer. Ağırlık ve normal kuvvet etki-tepki çifti olsaydı birlikte var olup birlikte yok olmak zorundaydı.",
          "Aynı kişiyi zıt yönlerde çeken iki arkadaş denge oluşturur (aynı cisme etki eden iki kuvvet); iki kişinin birbirini çekmesi ise etki-tepkidir (farklı kişilere etki eden iki kuvvet)."),
       S("TB", "KGU05"), "MEDIUM"),
]

# --- FİZ.11.1.5–FİZ.11.1.6: Serbest cisim diyagramı; statik ve kinetik sürtünme ---
MISCONCEPTIONS += [
    MC("fbd-extra-forces-added",
       "Serbest cisim diyagramına cismin hareket yönünde ayrı bir 'hareket (itme) kuvveti', 'eylemsizlik kuvveti' ya da cismin başka bir cisme uyguladığı kuvvet de çizilir.",
       "Serbest cisim diyagramında yalnızca incelenen cisme, çevresindeki başka cisimler (Dünya, yüzey, ip, el vb.) tarafından uygulanan gerçek kuvvetler gösterilir; "
       "her kuvvetin bir uygulayıcı cismi bulunmalıdır. Hareket yönü ayrı bir kuvvet gerektirmez; cismin başka cisme uyguladığı kuvvet o diğer cismin diyagramına aittir.",
       ["serbest-cisim-diyagrami", "kuvvet", "surtunme-kuvveti", "gerilme-kuvveti"], LO("1.5"), "FBD_ERROR",
       "fbd-identify-forces ailesinin 'hareket yönünde ayrı bir hareket kuvveti oku' ve 'cismin başka cisme uyguladığı kuvvet diyagrama eklenmiş' çeldiricileri; "
       "Temiz ve Kızılcık (2016) lise öğrencilerinin diyagramlarında ortamda bulunmayan kuvvetlerin eklendiğini, eylemsizlik kuvvetinin engelleyen kuvvet sayıldığını bildirir.",
       DI("Sürtünmeli yatay zeminde bir kutu, ipten uygulanan 30 N'luk yatay kuvvetle sabit hızla sağa doğru çekiliyor. Kutunun serbest cisim diyagramı için hangisi doğrudur?",
          "Ağırlık (aşağı), normal kuvvet (yukarı), ip gerilmesi (sağa, 30 N) ve sürtünme (sola, 30 N) çizilir; ayrıca bir 'hareket kuvveti' çizilmez.",
          "Ağırlık, normal kuvvet, ip gerilmesi (sağa), sürtünme (sola) ve hareket yönünde ayrıca bir 'hareket kuvveti' (sağa) çizilir.",
          "Ağırlık, normal kuvvet, ip gerilmesi (sağa) ve kutunun ipe uyguladığı kuvvet (sola) çizilir.",
          "Yalnızca ip gerilmesi (sağa) ve sürtünme (sola) çizilir; ağırlık ile normal kuvvet birbirini dengelediği için çizilmez.",
          "Ağırlık, normal kuvvet ve ip gerilmesi çizilir; sabit hızda sürtünme olmaz.",
          "A", "B"),
       RM(["Çizdiğin her okun yanına 'bu kuvveti hangi cisim uyguluyor?' diye yaz. 'Hareket kuvvetini' hangi cisim uyguluyor?",
           "Kutu sabit hızla gidiyor. Net kuvvet kaç olmalı? Çizdiğin oklar bunu veriyor mu?",
           "Kutunun ipe uyguladığı kuvvet kimin serbest cisim diyagramına aittir?",
           "Kutunun sağa gitmesi için sağa doğru ekstra bir kuvvet mi gerekiyor, yoksa hız eylemsizlikten mi sürüyor?"],
          "Hareket yönüne ekstra bir 'hareket kuvveti' çizersen sağa doğru net kuvvet sıfırdan büyük olur ve kutu giderek hızlanırdı; oysa kutu sabit hızla gidiyor.",
          "Serbest cisim diyagramı, tek bir cismin 'kimlik fotoğrafı' gibidir: yalnızca o cismin üstüne gelen kuvvetler girer; onun başkalarına yaptığı etkiler başkalarının fotoğrafında yer alır."),
       S("TK16", "KGU05"), "HIGH"),

    MC("supporting-surface-exerts-no-force",
       "Hareketsiz yüzeyler (masa, zemin, eğik düzlem) kuvvet uygulamaz; bu yüzden durgun cismin serbest cisim diyagramında normal kuvvet gösterilmez ya da gerekmez.",
       "Sert yüzey, cismin yüzeye içine girmesine karşı dik doğrultuda bir itme (normal kuvvet) uygular; bu bir temas kuvvetidir. Durgun cisimde ağırlığı dengeleyen "
       "kuvvet yüzeyin normal kuvvetidir. Yüzey, yalnızca 'pasif' göründüğü için kuvvetsiz değildir.",
       ["normal-kuvvet", "serbest-cisim-diyagrami", "agirlik", "newton-birinci-yasa"], LO("1.5"), "FBD_ERROR",
       "fbd-identify-forces ve frictionless-incline ailelerinde normal kuvvetin unutulması; Temiz ve Kızılcık (2016) eğik düzlem diyagramlarında yüzeyin tepki kuvvetini "
       "yalnızca %17,59 oranında doğru gösterildiğini bildirir. FCI taksonomisinde Ob (obstacles exert no force).",
       DI("Yatay bir masa üzerinde durgun duran 2 kg'lık bir kitabın serbest cisim diyagramı çiziliyor (g = 10 m/s²). Hangisi doğrudur?",
          "Yalnızca aşağı yönlü 20 N'luk ağırlık gösterilir; masa pasif olduğundan kuvvet uygulamaz.",
          "Aşağı yönlü 20 N'luk ağırlık ile masanın kitaba uyguladığı yukarı yönlü 20 N'luk normal kuvvet gösterilir.",
          "Aşağı yönlü 20 N'luk ağırlık ile kitabın masaya uyguladığı yukarı yönlü 20 N'luk kuvvet gösterilir.",
          "Aşağı yönlü 20 N'luk ağırlık ile yukarı yönlü 20 N'luk 'eylemsizlik kuvveti' gösterilir.",
          "Kitap durgun olduğu için hiçbir kuvvet gösterilmez.",
          "B", "A"),
       RM(["Kitap durgun: net kuvvet kaç olmalı? Yalnızca ağırlığı çizersen net kuvvet kaç olur?",
           "Kitabı bir süngerin üstüne koy: sünger ne yapar? Sert bir masa bundan temelde farklı mı davranır?",
           "Elini bir kitabın üstüne bastırdığında elin neyi hissediyor? Masa kitabı aynı biçimde 'hissediyor' mu?",
           "Masa aniden çekilirse kitap ne yapar? Masa o ana kadar neyi sağlıyordu?"],
          "Yalnızca ağırlık etki etseydi kitap masanın üstünde de aşağı doğru ivmelenirdi. Kitap durgun olduğuna göre ağırlığı dengeleyen yukarı yönlü bir kuvvet olmak zorundadır: masanın itmesi.",
          "Sert masa, çok az sıkışan ama aynı işi yapan çok sert bir yay gibidir: kitabın ağırlığı yayı biraz sıkıştırır, yay da kitabı yukarı iter."),
       S("FCI", "TK16", "DUR21"), "HIGH"),

    MC("scale-reading-always-weight",
       "Tartının (baskülün) gösterdiği değer her zaman cismin ağırlığıdır; asansör hızlansa ya da yavaşlasa da 'ağırlık = tartı okuması' geçerlidir.",
       "Tartı, cismin tartıya uyguladığı kuvveti (normal kuvvetin tepkisini) ölçer. Cismin ağırlığı (Dünya'nın çekim kuvveti) mg olarak sabit kalır; "
       "ivmeli bir sistemde normal kuvvet N = m(g ± a) olduğundan tartı okuması ağırlıktan farklı olabilir.",
       ["agirlik", "normal-kuvvet", "newton-ikinci-yasa", "serbest-cisim-diyagrami"], LO("1.5"), "CONCEPTUAL_ERROR",
       "apparent-weight-elevator ailesinin 'tartı her zaman ağırlığı gösterir' ve 'sabit hızla yukarı çıkan asansörde tartı daha büyük gösterir' çeldiricileri. "
       "Taibu, Rudge ve Schuster (2015) ders kitaplarında ağırlık tanımı ile tartı okumasının karıştırıldığını, ivmeli sistemlerde güçlük doğurduğunu belirtir.",
       DI("70 kg'lık bir kişi asansördeki baskülün üzerinde dururken asansör yukarı yönlü 2 m/s² ivmeyle hızlanıyor (g = 10 m/s²). "
          "Baskülün okuduğu kuvvet ile kişinin ağırlığı (Dünya'nın çekim kuvveti) için hangisi doğrudur?",
          "Baskül 700 N okur; ağırlık 700 N'dur.",
          "Baskül 840 N okur; ağırlık 700 N'dur.",
          "Baskül 840 N okur; ağırlık da 840 N olur.",
          "Baskül 560 N okur; ağırlık 700 N'dur.",
          "Baskül 700 N okur; ağırlık 840 N olur.",
          "B", "C"),
       RM(["Baskül hangi kuvveti ölçüyor: kişinin baskülü ittiği kuvveti mi, Dünya'nın kişiyi çekmesini mi?",
           "Kişinin serbest cisim diyagramını çiz. İvme yukarıysa net kuvvet hangi yönde? N ile mg'yi karşılaştır.",
           "Asansör serbest düşerse baskül ne okur? Dünya kişiyi çekmeyi bırakır mı?",
           "Asansör sabit hızla yükselirken baskül ne okur?"],
          "Serbest düşen asansörde baskül sıfır okur; ama Dünya kişiyi hâlâ mg kuvvetiyle çeker. Demek ki baskül okuması çekim kuvvetinin kendisi değildir.",
          "Bir yayın uzaması, yayı çeken kuvveti gösterir; baskül de sizin ona uyguladığınız basma kuvvetini gösterir. Bu kuvvet, ivmesiz ortamda ağırlığa eşit olur ama ağırlığın tanımı değildir."),
       S("TAIBU15", "TB"), "MEDIUM"),

    MC("normal-equals-weight",
       "Normal kuvvet her zaman cismin ağırlığına (mg) eşittir; eğik düzlemde, açılı bir kuvvet altında ya da ivmeli sistemde de değişmez.",
       "Normal kuvvet yüzeye dik doğrultudaki hareket denkleminden bulunur: eğik düzlemde N = mg cosθ; yukarı doğru açılı F kuvvetiyle çekilen cisimde N = mg − F sinθ; "
       "ivmeli asansörde N = m(g ± a). Yalnızca yatay yüzeyde, düşey kuvvet ve ivme yokken N = mg olur.",
       ["normal-kuvvet", "agirlik", "egik-duzlem", "vektor-bilesenleri"], LO("1.5", "1.7"), "CONCEPTUAL_ERROR",
       "frictionless-incline ailesinin 'normal kuvvet ağırlığa eşittir' çeldiricisi; friction-angled-force ailesinin 'normal kuvvet her durumda mg'dir' çeldiricisi. "
       "Temiz ve Kızılcık (2016) 'bir cisme etki eden normal kuvvet cismin ağırlığına eşittir' görüşünü literatürde sık rastlanan yanılgılar arasında sayar.",
       DI("Sürtünmesiz bir eğik düzlemde (eğim açısı 37°) durgun hâlden serbest bırakılan 5 kg'lık bir cisim kayıyor (g = 10 m/s², sin37° = 0,6, cos37° = 0,8). "
          "Cisme etki eden normal kuvvetin büyüklüğü kaç N'dur?",
          "50", "40", "30", "25", "0",
          "B", "A"),
       RM(["Normal kuvvet yüzeye göre hangi doğrultuda? Ağırlık hangi doğrultuda?",
           "Cisim yüzeye dik doğrultuda ivmeleniyor mu? O doğrultudaki net kuvvet kaç olmalı?",
           "Eğim açısı 0° iken ve 90° iken (dik duvar) normal kuvvet kaç olurdu?",
           "Ağırlığın yüzeye dik bileşeni kaç N?"],
          "Eğim açısı arttıkça normal kuvvet ağırlığa eşit kalsaydı, dik bir duvarda (90°) normal kuvvet mg olurdu; oysa duvara yalnızca değen bir cisme duvar hiç kuvvet uygulamaz (N = 0).",
          "Bir kapıya yaslanan kişi ne kadar bastırırsa kapı da o kadar iter; yüzeyin itme miktarı, cismin yüzeye ne kadar bastırdığına bağlıdır, cismin ağırlığına değil."),
       S("TK16", "KGU05"), "HIGH"),

    MC("friction-always-opposes-motion",
       "Sürtünme kuvveti her zaman cismin hareket yönünün tersinedir; yürürken ya da tekerlek dönerken bile sürtünme hareketi hep engeller.",
       "Sürtünme kuvveti temas eden yüzeylerin birbirine göre bağıl hareketine (ya da hareket etme eğilimine) zıttır. Kaymadan yürüyen kişinin yere basan ayağına yerin uyguladığı "
       "statik sürtünme kuvveti hareket yönündedir; kişiyi ilerleten kuvvet budur. Dönerek ötelemede de itici sürtünme hareket yönünde olabilir.",
       ["surtunme-kuvveti", "statik-surtunme", "donerek-oteleme"], LO("1.6"), "CONCEPTUAL_ERROR",
       "friction-direction ailesinin 'sürtünme her zaman hareket yönüne zıttır' çeldiricisi. Kızılcık ve ark. (2021) incelemesinde 'sürtünme hareketin tersinedir' en çok makalede "
       "rastlanan olası yanılgıdır; Yüzbaşıoğlu ve Kurnaz (2022)'de sürtünmenin yönü sorusu en az doğru yanıtlanan sorudur (%19,29).",
       DI("Yatay zeminde kaymadan sağa doğru yürüyen bir kişinin, yere basan ayağına yerin uyguladığı sürtünme kuvveti için hangisi doğrudur?",
          "Sola, yani hareketin tersi yöndedir; çünkü sürtünme hareketi engeller.",
          "Sağa, yani hareket yönündedir; ayak yere sola kuvvet uygular, yer de tepki olarak ayağı sağa iter.",
          "Sıfırdır; çünkü ayak yere göre kayarak ilerlemektedir.",
          "Sağa yönelmiştir ve kinetik sürtünmedir; çünkü kişi hareket etmektedir.",
          "Sola yönelmiştir; çünkü ayak yerde geriye doğru kayar.",
          "B", "A"),
       RM(["Buzda yürümeye çalışınca ne olur? Neden ilerleyemezsin?",
           "Ayağın yere hangi yönde kuvvet uyguluyor? Bunun tepkisi hangi cisme, hangi yönde etki eder?",
           "Ayağın yere değdiği noktanın yere göre bağıl hareketi var mı, yoksa kayma eğilimi mi var? Bu eğilim hangi yönde?",
           "Gaz verince hızlanan bir kamyonetin kasasındaki kutuyu kamyonete göre hangi yöne kayma eğiliminde görürsün? Sürtünme kutuyu hangi yöne iter?"],
          "Sürtünme hep hareketi engelleseydi insan karada da ilerleyemezdi. Yürümeyi sağlayan, zeminin ayağa uyguladığı ve hareket yönünü gösteren sürtünme kuvvetidir.",
          "Yürürken ayağımız zemini geri iter, zemin de bizi ileri iter; zemin, bir çıpa gibi 'tutunma' sağlar. Tutunma olmadan (buzda) ilerleme de olmaz."),
       S("KAS21", "YK22"), "HIGH"),

    MC("no-motion-no-friction",
       "Kuvvet uygulandığı hâlde kıpırdamayan cisme sürtünme kuvveti etki etmez (sürtünme yalnızca hareket varken oluşur), ya da cisim, uygulanan kuvvetten büyük bir sürtünmeyle durur.",
       "Cisim harekete zorlanmasına rağmen durgunsa üzerine statik sürtünme etki eder; büyüklüğü uygulanan kuvvete eşit, yönü ters olur (net kuvvet sıfır). "
       "Sürtünmenin var olması için hareket gerekmez, hareket etme eğilimi yeterlidir. Statik sürtünme, uygulanan kuvvetle birlikte artar.",
       ["statik-surtunme", "surtunme-kuvveti", "bileske-kuvvet", "maksimum-statik-surtunme"], LO("1.6", "1.7"), "CONCEPTUAL_ERROR",
       "friction-type-identification ailesinin 'harekete zorlanmasına rağmen durmakta olan cisme etki eden sürtünme' bileşeni; friction-threshold ve friction-applied-force-graph ailelerinde "
       "durgun cisimde sürtünmenin yok sayıldığı ya da uygulanan kuvvetten büyük sanıldığı seçenekler. FCI taksonomisinde AF3 (no motion implies no force).",
       DI("Yatay zeminde duran 10 kg'lık bir sandığa yatay doğrultuda 20 N'luk kuvvet uygulanıyor, ancak sandık kıpırdamıyor (maksimum statik sürtünme kuvveti 40 N'dur). "
          "Sandığa etki eden sürtünme kuvveti için hangisi doğrudur?",
          "Sürtünme yoktur; çünkü sandık hareket etmiyor.",
          "20 N'dur ve uygulanan kuvvetin tersi yöndedir.",
          "40 N'dur ve uygulanan kuvvetin tersi yöndedir.",
          "20 N'dur ve uygulanan kuvvetle aynı yöndedir.",
          "20 N'dan büyüktür; çünkü sandığı durduran sürtünme uygulanan kuvveti yenmiştir.",
          "B", "A"),
       RM(["Sandık durgun: net kuvvet kaç olmalı? Bunun için sürtünme ne kadar olmalı?",
           "Uygulanan kuvveti 20 N'dan 30 N'a çıkarırsan sandık hâlâ durgunsa sürtünme ne olur?",
           "Sürtünme hiç olmasaydı 20 N'luk kuvvet sandığa ne yapardı?",
           "Sürtünmenin var olması için gerekli olan şey hareket mi, hareket etme eğilimi mi?"],
          "Sürtünme olmasaydı 20 N'luk kuvvet sandığı hızlandırırdı. Sandığın kıpırdamaması sürtünmenin var olduğunun, hatta uygulanan kuvveti tam dengelediğinin kanıtıdır.",
          "Bir kapıyı iki kişi zıt yönlerde eşit şiddette ittiğinde kapı kıpırdamaz; kıpırdamıyor diye kimsenin itmediği söylenemez. Kuvvetler birbirini dengeler."),
       S("FCI", "KAS21"), "MEDIUM"),

    MC("rolling-friction-is-kinetic",
       "Yuvarlanan (dönerek öteleme yapan) cisimlere kinetik sürtünme etki eder; hareket eden her cisimde sürtünme kinetiktir.",
       "Kaymadan yuvarlanan tekerlekte yola değen nokta yola göre anlık olarak durgundur; bu yüzden sürtünme statik sürtünmedir. Kinetik sürtünme yalnızca temas yüzeyleri arasında "
       "bağıl kayma varken, yani kayarak ötelemede oluşur.",
       ["donerek-oteleme", "kayarak-oteleme", "statik-surtunme", "kinetik-surtunme"], LO("1.6"), "CONCEPTUAL_ERROR",
       "friction-type-identification ailesinin 'hareket eden her cisme kinetik sürtünme etki eder' çeldiricisi. Kızılcık ve ark. (2021) kayma–yuvarlanma ve statik–kinetik "
       "ayrımının çoğu zaman göz ardı edildiğini bulmuştur.",
       DI("Düz yolda kaymadan yuvarlanan bir bisiklet tekerleği ile, frenin kilitlenmesi sonucu aynı yolda kayarak ilerleyen bir bisiklet tekerleği karşılaştırılıyor. "
          "Tekerlek ile yol arasındaki sürtünme türleri için hangisi doğrudur?",
          "İkisinde de kinetik sürtünme vardır; çünkü iki durumda da bisiklet hareket etmektedir.",
          "Yuvarlanan tekerlekte statik, kayan tekerlekte kinetik sürtünme vardır.",
          "Yuvarlanan tekerlekte kinetik, kayan tekerlekte statik sürtünme vardır.",
          "Yuvarlanan tekerlekte sürtünme yoktur, kayan tekerlekte kinetik sürtünme vardır.",
          "İkisinde de statik sürtünme vardır.",
          "B", "A"),
       RM(["Kaymadan yuvarlanan tekerleğin yola değdiği nokta, yere göre anlık olarak hangi hızdadır?",
           "Temas noktalarında bağıl hareket yoksa hangi sürtünme türünden söz edersin?",
           "Fren kilitlenip tekerlek kayarsa temas noktasının yere göre hızı ne olur? Sürtünme türü değişir mi?",
           "Kinetik sürtünme tam olarak hangi koşulda oluşur?"],
          "Kilitli tekerlekte lastik yolda iz ve ses bırakarak kayar; normal yuvarlanmada bu olmaz. İki durumda sürtünme türü aynı olamaz.",
          "Yürürken ayağınızın yere basan noktası bir an için yere yapışık gibidir: kişi hareket etse de ayağın o noktası yere göre durgundur ve sürtünme statiktir."),
       S("KAS21", "TB"), "HIGH"),

    MC("kinetic-greater-than-max-static",
       "Kinetik sürtünme kuvveti maksimum statik sürtünme kuvvetinden büyüktür; cisim harekete geçince sürtünme artar.",
       "Aynı yüzey çifti için kinetik sürtünme katsayısı statik katsayıdan küçüktür (μ_k < μ_s); bu nedenle f_k < f_s,max olur. Cisim harekete geçtiğinde sürtünme kuvveti "
       "maksimum statik değerden daha küçük bir kinetik değere düşer; harekete geçirmek, hareketi sürdürmekten zordur.",
       ["statik-surtunme", "kinetik-surtunme", "maksimum-statik-surtunme", "surtunme-katsayisi"], LO("1.6", "1.7"), "CONCEPTUAL_ERROR",
       "static-vs-kinetic-compare ailesinin 'kinetik sürtünme maksimum statikten büyüktür' ve friction-applied-force-graph ailesinin 'cisim harekete geçince sürtünme artar' çeldiricileri; "
       "friction-threshold'da eşiğin kinetik değer sanılması.",
       DI("Yatay zeminde durgun bir dolaba uygulanan yatay kuvvet sıfırdan başlayarak artırılıyor; dolap 120 N'da harekete geçiyor, ardından 100 N'luk yatay kuvvetle sabit hızla itiliyor. "
          "Dolaba etki eden sürtünme kuvvetleri için hangisi doğrudur?",
          "Maksimum statik sürtünme 100 N, kinetik sürtünme 120 N'dur; çünkü hareket eden cisimde sürtünme artar.",
          "Maksimum statik sürtünme 120 N, kinetik sürtünme 100 N'dur.",
          "Maksimum statik ve kinetik sürtünme kuvvetlerinin ikisi de 120 N'dur.",
          "İkisi de 100 N'dur; çünkü sabit hızda net kuvvet sıfırdır.",
          "Kinetik sürtünme sıfırdır; çünkü cisim harekete geçince statik sürtünme kaybolur ve başka sürtünme oluşmaz.",
          "B", "A"),
       RM(["Dolap 120 N'da harekete geçti. Bu, maksimum statik sürtünme hakkında ne söylüyor?",
           "Sabit hızla giderken net kuvvet kaç? Buna göre kinetik sürtünme kaç N?",
           "Bir dolabı harekete geçirmek neden hareket hâlinde tutmaktan daha zordur? Kendi deneyiminden örnek ver.",
           "Sürtünme–uygulanan kuvvet grafiğinde cisim harekete geçtiği anda çizgi yukarı mı aşağı mı gider?"],
          "Kinetik sürtünme maksimum statikten büyük olsaydı, harekete geçen cisim yavaşlar ve yeniden dururdu; oysa bir kez kayan dolap daha az kuvvetle sürüklenmeye devam eder.",
          "Kapıyı açarken en çok başlangıçta zorlanırsın; kapı hareket etmeye başlayınca daha az kuvvet yeter. Yapışkan bir zemin koptuktan sonra daha az tutar."),
       S("KAS21", "TB"), "MEDIUM"),
]

# --- FİZ.11.1.7–FİZ.11.1.8: Sürtünme kuvvetinin matematiksel modeli; limit hız ---
MISCONCEPTIONS += [
    MC("static-friction-always-maximum",
       "Cisim durgunken statik sürtünme kuvveti her zaman maksimum değerindedir (f_s = μ_s·N); uygulanan kuvvet değişse de bu değer sabittir.",
       "Statik sürtünme kuvveti uygulanan kuvvete eşit ve zıt olacak biçimde 0 ile f_s,max = μ_s·N arasında değişir; yalnızca harekete geçmeden hemen önce maksimum değerine ulaşır. "
       "μ_s·N sürtünmenin üst sınırıdır, her zamanki değeri değildir.",
       ["statik-surtunme", "maksimum-statik-surtunme", "surtunme-katsayisi", "normal-kuvvet"], LO("1.6", "1.7"), "CONCEPTUAL_ERROR",
       "friction-threshold ailesinin 'cisim durgunken sürtünme her zaman maksimum statik değerdedir', static-vs-kinetic-compare ailesinin 'statik sürtünme her zaman sabittir' ve "
       "friction-stacked-blocks-together ailesinin 'üst bloğa etki eden sürtünme her zaman maksimum değerdedir' çeldiricileri. Hesapta μ_s·N'nin her durumda kullanılması.",
       DI("Yatay zeminde durgun duran 20 kg'lık bir kutuya (μ_s = 0,5; μ_k = 0,4; g = 10 m/s²) yatay doğrultuda 60 N'luk kuvvet uygulanıyor ve kutu kıpırdamıyor. "
          "Kutuya etki eden sürtünme kuvvetinin büyüklüğü kaç N'dur?",
          "100", "60", "80", "40", "0",
          "B", "A"),
       RM(["Kuvveti 60 N'dan 80 N'a çıkarırsan kutu hâlâ durgunsa sürtünme değişir mi?",
           "Kutu durgunken net kuvvet kaç olmalı? Bu durumda sürtünme ne kadar olmalı?",
           "f_s,max neyi anlatır: sürtünmenin her zamanki değerini mi, ulaşabileceği üst sınırı mı?",
           "Sürtünme–uygulanan kuvvet grafiğinde kutu hareket etmeden önceki kısım nasıl bir şekil çizer?"],
          "Statik sürtünme her zaman 100 N olsaydı, 60 N'luk kuvvetle itilen kutuya ters yönde 40 N'luk net kuvvet etki eder ve kutu geriye doğru hızlanırdı; oysa kutu yerinde kalır.",
          "Güvenlik halatı en çok 100 N taşıyacak şekilde üretilmiştir (üst sınır), ama 60 N'luk yük asılıysa yalnızca 60 N gerilir. Sürtünme de gerektiği kadar tutar, sınır aşılınca kopar."),
       S("KAS21", "TB"), "MEDIUM"),

    MC("friction-depends-on-contact-area",
       "Temas yüzey alanı büyüdükçe sürtünme kuvveti artar (geniş yüz daha çok sürtünür).",
       "Kuru yüzeylerde sürtünme kuvveti temas alanına bağlı değildir: f = μ·N. Alan büyürken birim alana düşen basınç azalır, toplam sürtünme (N ve μ aynı kaldığı sürece) değişmez.",
       ["surtunme-kuvveti", "surtunme-katsayisi", "normal-kuvvet"], LO("1.7"), "CONCEPTUAL_ERROR",
       "friction-variables-data ailesinin 'temas yüzey alanı büyüdükçe sürtünme artar' çeldiricisi; friction-incline-coefficient ve friction-horizontal-dynamics'te alanın hesaba katıldığı seçenekler. "
       "Temiz ve Kızılcık (2016) öğrencilerin sürtünmeyi alanla ilişkilendirdiğini, basınç gerekçesi kurduğunu bildirir.",
       DI("Üç yüzü farklı alanlı, 6 kg'lık bir tuğla yatay bir masada önce geniş yüzü, sonra dar yüzü üzerinde olacak biçimde sabit hızla çekiliyor (kinetik sürtünme katsayısı her iki yüz için 0,3; g = 10 m/s²). "
          "Sabit hızla çekmek için gereken yatay kuvvet için hangisi doğrudur?",
          "Geniş yüz üzerindeyken daha büyüktür; çünkü temas alanı daha büyüktür.",
          "İki durumda da 18 N'dur.",
          "Dar yüz üzerindeyken daha büyüktür; çünkü basınç daha büyüktür.",
          "Geniş yüz üzerindeyken 18 N, dar yüz üzerindeyken alanla orantılı olarak daha küçüktür.",
          "İki durumda da 60 N'dur.",
          "B", "A"),
       RM(["f = μN bağıntısında alan var mı? N neye eşit? Tuğla yan yatınca ağırlığı değişir mi?",
           "Alan iki katına çıkınca basınç nasıl değişir? Sürtünmeyi belirleyen basınç mı, toplam normal kuvvet mi?",
           "Sürtünmenin alana bağlı olup olmadığını denemek için hangi değişkenleri sabit tutarak nasıl bir deney tasarlarsın?"],
          "Aynı iki tuğla yan yana bağlanırsa alan ve ağırlık iki katına çıkar ve sürtünme iki katına çıkar; ama tek tuğla yan yatırılırsa alan iki katına çıkar, ağırlık değişmez ve sürtünme değişmez. "
          "Sürtünmeyi değiştiren şey alan değil normal kuvvettir.",
          "Tek ayak üstünde ya da iki ayak üstünde durmak tartının okumasını değiştirmez: temas alanı değişir, ama yüzeye uygulanan toplam kuvvet aynı kalır."),
       S("TK16", "KAS21", "KGU05"), "HIGH"),

    MC("wall-press-increases-friction",
       "Duvara bastırılarak dengede tutulan cisimde bastırma kuvveti artırılırsa sürtünme kuvveti de artar (sürtünme bastırma kuvvetine eşittir ya da μN kadardır).",
       "Cisim düşey doğrultuda dengede olduğu sürece statik sürtünme ağırlığa eşittir (f = mg) ve bastırma kuvveti artınca değişmez. Bastırma kuvveti yalnızca maksimum statik sürtünmeyi "
       "(μ_s·N) yani kaymama güvence sınırını artırır.",
       ["statik-surtunme", "maksimum-statik-surtunme", "normal-kuvvet", "agirlik"], LO("1.7"), "CONCEPTUAL_ERROR",
       "friction-wall-press ailesinin 'bastırma kuvveti artınca sürtünme de artar (cisim dengedeyken)' çeldiricisi; friction-stacked-blocks-together'da sürtünmenin her zaman μN alınması.",
       DI("Düşey bir duvara 2 kg'lık bir kutu, yatay doğrultuda F = 50 N'luk kuvvetle bastırılarak kaymadan durgun tutuluyor (μ_s = 0,6; g = 10 m/s²). "
          "F, 80 N'a çıkarıldığında kutu hâlâ durgun kalıyor. Duvarın kutuya uyguladığı sürtünme kuvveti nasıl değişir?",
          "Bastırma kuvvetine eşit olduğundan 50 N'dan 80 N'a çıkar.",
          "20 N olarak değişmez.",
          "μ_s·N kadar olduğundan 30 N'dan 48 N'a çıkar.",
          "Yarıya iner; çünkü yüzey daha sıkı kavrar.",
          "Sıfırlanır; çünkü kutu duvara yapışmıştır.",
          "B", "C"),
       RM(["Kutu durgun: düşey doğrultuda hangi kuvvetler var ve net kuvvet kaç olmalı?",
           "Bastırma kuvvetini artırınca düşey kuvvetlerin dengesi bozuluyor mu?",
           "Bu sürtünme kuvveti neyi dengeliyor?",
           "f_s,max'ın artması, f_s'nin artması anlamına gelir mi?"],
          "Bastırma kuvveti sürtünmeyi artırıyor olsaydı, düşeyde yukarı yönlü net kuvvet oluşur ve kutu yukarı doğru hızlanırdı; oysa kutu yerinde duruyor.",
          "Daha güçlü bir halat daha ağır yükü taşıyabilir, ama bugün asılı olan yük aynıysa halat yine aynı gerilmeyi taşır. Daha sıkı bastırmak taşıma sınırını artırır, taşınan yükü değil."),
       S("KAS21", "TB"), "MEDIUM"),

    MC("incline-slip-angle-depends-on-mass",
       "Sürtünmeli eğik düzlemde cismin kayıp kaymayacağı (ya da ivmesi) cismin kütlesine veya konumuna bağlıdır; ağır cisim daha küçük açıda kayar.",
       "Kaymaya başlama koşulu mg sinθ ≥ μ_s·mg cosθ, yani tanθ ≥ μ_s'dir; kütle sadeleşir. Kritik açı kütleden ve cismin eğik düzlem üzerindeki konumundan bağımsızdır, "
       "yalnızca yüzey çiftine (μ_s) bağlıdır. Kayma hâlinde de a = g(sinθ − μ_k cosθ) kütleden bağımsızdır.",
       ["egik-duzlem", "surtunme-katsayisi", "statik-surtunme", "kutle"], LO("1.7"), "CONCEPTUAL_ERROR",
       "friction-incline-coefficient ailesinin 'katsayı cismin kütlesine bağlıdır' ve 'kaymaya başlama açısı kinetik katsayıyı verir' çeldiricileri; "
       "frictionless-incline ailesinin 'ağır cisim daha büyük ivmeyle kayar' çeldiricisi. Temiz ve Kızılcık (2016): lise öğrencilerinin büyük çoğunluğu, eğik düzlemdeki cismin konumu ve kütlesi gibi etkisiz değişkenlerin hareketi etkilediğini düşünüyor.",
       DI("Aynı tahta eğik düzlem üzerinde, aynı yüzeye sahip 1 kg'lık ve 4 kg'lık iki blok durgun hâlde duruyor. Eğim açısı yavaş yavaş artırıldığında bloklar için hangisi doğrudur?",
          "4 kg'lık blok daha küçük açıda kaymaya başlar; çünkü ağırlığı daha büyüktür.",
          "İki blok da aynı açıda kaymaya başlar.",
          "1 kg'lık blok daha küçük açıda kaymaya başlar; çünkü normal kuvveti daha küçüktür.",
          "Kayma açıları arasındaki fark kütle oranı kadardır (4 kat).",
          "4 kg'lık blok hiç kaymaz; çünkü normal kuvveti daha büyüktür.",
          "B", "A"),
       RM(["Blok kaymaya başlamak üzereyken eğik düzlem boyunca ve düzleme dik doğrultuda hangi kuvvetler dengede?",
           "mg sinθ ve μ_s·mg cosθ ifadelerinde kütle sadeleşiyor mu?",
           "Ağırlık 4 katına çıkınca hem kaydırıcı bileşen hem de sürtünme kaç katına çıkar?",
           "Yüzey çifti aynıysa kritik açıyı belirleyen nedir?"],
          "4 kg'lık blok, yapışık dört adet 1 kg'lık bloktan başka bir şey değildir. Tek bir blok bu açıda kaymıyorsa, dört bloğu birbirine yapıştırmak hiçbir şeyi değiştirmeyeceğinden dörtlü yığın da kaymaz.",
          "Aynı yokuşta ya da buzda dört kardeş birbirinin elini tutarak yürüse her biri tek başına yürürken kaydığı koşulda kayar; el ele tutuşmak yüzeyin tutuşunu değiştirmez."),
       S("TK16", "TB"), "HIGH"),

    MC("terminal-velocity-net-force-nonzero",
       "Limit hıza ulaşan cismin ivmesi hâlâ g'dir ya da hava direnci ağırlığından büyüktür; hız sabit kalsa bile net kuvvet sıfır olmaz.",
       "Limit hızda hava direnci kuvveti ağırlığa eşit büyüklükte ve zıt yöndedir; net kuvvet sıfır, ivme sıfırdır ve cisim sabit hızla düşer. "
       "Hız arttıkça direnç arttığı için ivme azalarak sıfıra yaklaşır.",
       ["limit-hiz", "hava-direnci", "bileske-kuvvet", "newton-birinci-yasa"], LO("1.8"), "CONCEPTUAL_ERROR",
       "terminal-velocity-graph ailesinin 'limit hızda ivme g'dir' ve 'limit hıza ulaşınca hava direnci ağırlıktan büyüktür' çeldiricileri; terminal-velocity-daily-life ve drag-variables-data sorularında "
       "net kuvvetin sıfır olduğunun görülmemesi. FCI taksonomisinde AF6 (force causes acceleration to terminal velocity).",
       DI("Yüksekten atlayan bir paraşütçü, paraşütü açılmadan yeterince uzun süre düştükten sonra limit hıza ulaşıyor. Limit hıza ulaşıldıktan sonra paraşütçü için hangisi doğrudur?",
          "İvmesi g'dir; çünkü ağırlığı hâlâ etki etmektedir.",
          "Hava direnci kuvveti ağırlığına eşittir, net kuvvet sıfırdır ve sabit hızla düşer.",
          "Hava direnci ağırlığından büyüktür; bu yüzden hızı azalır.",
          "Hava direnci ağırlığından küçüktür ama hızındaki artış durmuştur.",
          "Hava direnci sıfırdır; paraşütçü serbest düşme yapar.",
          "B", "A"),
       RM(["Limit hızda paraşütçüye etki eden kuvvetleri çiz. Aşağı ve yukarı yönlü okların büyüklükleri nasıl?",
           "Hız artık değişmiyorsa ivme kaç? İvme sıfırsa net kuvvet kaç olmalı?",
           "Hız arttıkça hava direnci nasıl değişir? Bu değişim hızın artışını nasıl durdurur?",
           "Hava direnci ağırlıktan büyük olsaydı hız ne olurdu?"],
          "Limit hızda ivme g olsaydı hız her saniye 10 m/s artmaya devam ederdi; oysa limit hız tanımı gereği hız artık değişmiyor.",
          "Deliği olan bir su deposunda doluluk arttıkça akış artar; giren su ile çıkan su eşitlenince seviye sabit kalır, oysa musluk hâlâ açıktır. Ağırlık hâlâ vardır; yalnızca direnç onu dengelemiştir."),
       S("FCI", "FERR17", "BL23"), "MEDIUM"),

    MC("heavier-lower-terminal-speed",
       "Kütlesi büyük olan cismin limit hızı küçüktür (ağır cisim daha çabuk yavaşlar) ya da limit hız kütleye hiç bağlı değildir.",
       "Limit hızda mg = direnç kuvveti olur. Direnç hızla ve kesit alanıyla arttığından, aynı şekil ve kesit alanında daha ağır cisim, direncin ağırlığa ulaşması için daha büyük hıza çıkmak zorundadır; "
       "limit hız kütle arttıkça artar.",
       ["limit-hiz", "hava-direnci", "kutle", "kesit-alani"], LO("1.8"), "CONCEPTUAL_ERROR",
       "terminal-velocity-variables ailesinin 'kütlesi büyük olanın limit hızı küçüktür' çeldiricisi; terminal-velocity-daily-life ve ff-mass-independence ile birlikte serbest düşmede "
       "ivmenin kütleden bağımsızlığının limit hıza yanlış genellenmesi. Potvin ve ark. (2023) ile Ferreira ve ark. (2017) havalı ortamda kütle–hız ilişkisinin öğrencilerin "
       "günlük deneyimiyle çeliştiğini bildirir.",
       DI("Aynı boyutta ve aynı şekilde iki küre havada yeterince yüksekten bırakılıyor: biri içi boş plastik (50 g), diğeri içi dolu demir (500 g). "
          "Her ikisi de limit hıza ulaşıyor. Limit hızlar v_plastik ve v_demir için hangisi doğrudur?",
          "v_demir < v_plastik",
          "v_demir = v_plastik; çünkü şekilleri aynıdır.",
          "v_demir > v_plastik; çünkü demir kürenin ağırlığını dengelemek için daha büyük bir direnç, dolayısıyla daha büyük hız gerekir.",
          "v_demir = v_plastik; çünkü serbest düşmede ivme kütleden bağımsızdır.",
          "v_demir > v_plastik; çünkü demir küreye daha az hava direnci etki eder.",
          "C", "A"),
       RM(["Limit hızda ağırlıkla hangi kuvvet eşitleniyor? Ağırlık büyükse dengelemek için bu kuvvet de büyük olmak zorunda mı?",
           "Hava direnci neye bağlı: hıza, kesit alanına? Kesit alanı aynıysa direncin büyümesi için ne artmalı?",
           "Hangi küre direncini ağırlığına ulaştırmak için daha çok hızlanmalıdır?",
           "1 filtre kâğıdı ile aynı şekilli 4 filtre kâğıdını üst üste bırakırsan hangisi daha hızlı düşer?"],
          "Aynı şekilli dört kahve filtresi üst üste yüksekten bırakılınca, tek filtreye göre belirgin biçimde daha hızlı düşer: ağır olan 'daha yavaş' olsaydı tersi beklenirdi.",
          "Aynı bisiklet ve aynı duruşla yokuş aşağı inen iki sürücüden ağır olan daha yüksek hızda dengeye ulaşır; çünkü onu aşağı çeken kuvvet büyüktür ve rüzgâr direncinin buna yetişmesi için hızın artması gerekir."),
       S("POTV23", "FERR17", "TB"), "MEDIUM"),
]

# --- FİZ.11.1.9–FİZ.11.1.10: Düzgün çembersel hareket ---
MISCONCEPTIONS += [
    MC("constant-speed-means-no-acceleration",
       "Düzgün çembersel harekette sürat sabit olduğundan hız da sabittir; hız değişmediği için ivme ve net kuvvet yoktur (cisim dengededir).",
       "Hız vektörel bir niceliktir; sürat sabit olsa da yönü sürekli değiştiği için hız değişir ve cismin merkezcil ivmesi vardır (a = ϑ²/r = ω²r). Net kuvvet merkeze yönelir ve sıfır değildir; cisim dengede değildir.",
       ["duzgun-cembersel-hareket", "cizgisel-hiz", "cizgisel-surat", "merkezcil-ivme"], LO("1.9", "1.10"), "CONCEPTUAL_ERROR",
       "circular-velocity-direction ailesinin 'sürat sabit olduğundan hız da sabittir' çeldiricisi; circular-analogies ailesinin 'düzgün çembersel harekette ivme yoktur' çeldiricisi. "
       "Kızılcık ve Güneş (2011) 'düzgün dairesel harekette hız değişmez' yanılgısını en yüksek oranda (%18,88), denge şartı arayışını ise %6,99 oranında bulmuştur.",
       DI("Yarıçapı 2 m olan bir çember üzerinde 4 m/s sabit süratle hareket eden bir cisim düzgün çembersel hareket yapıyor. Cismin ivmesi için hangisi doğrudur?",
          "Sıfırdır; çünkü sürat sabittir.",
          "8 m/s² büyüklüğündedir ve merkeze yöneliktir.",
          "8 m/s² büyüklüğündedir ve hareket yönündedir (yörüngeye teğettir).",
          "2 m/s² büyüklüğündedir ve merkeze yöneliktir.",
          "8 m/s² büyüklüğündedir ve merkezden dışarı yöneliktir.",
          "B", "A"),
       RM(["Hız nasıl bir niceliktir: yalnızca büyüklük mü, büyüklük ve yön mü?",
           "Çember üzerinde iki farklı noktadaki hız vektörlerini çiz. Aynı vektör mü?",
           "İvmenin tanımı hız vektörünün değişimi mi, yoksa yalnızca büyüklüğünün değişimi mi?",
           "Net kuvvet sıfır olsaydı Newton'ın 1. yasasına göre cisim nasıl bir yol izlerdi?"],
          "Net kuvvet sıfır olsaydı cisim doğrusal bir yolda giderdi. Çember boyunca gidiyorsa yönü sürekli değişiyor demektir; bu da bir ivme ve dolayısıyla net kuvvet gerektirir.",
          "Hız göstergesi 60 km/sa'te sabit olan bir araç viraja girdiğinde içindekiler yana doğru bastırıldığını hisseder: sürat sabit, ama yön değişiyor ve bu bir ivmedir."),
       S("KG11", "UG07", "FCI"), "HIGH"),

    MC("circular-velocity-toward-center",
       "Düzgün çembersel harekette hız vektörü yarıçap doğrultusunda (merkeze doğru) yönelir; hız ile ivme aynı doğrultudadır.",
       "Hız vektörü her an yörüngeye teğettir ve yarıçap vektörüne diktir. İvme (ve net kuvvet) ise merkeze yönelir, yani hıza diktir; hıza dik olan bir ivme hızın büyüklüğünü değil yalnızca yönünü değiştirir.",
       ["duzgun-cembersel-hareket", "cizgisel-hiz", "yaricap-vektoru", "merkezcil-ivme"], LO("1.9"), "CONCEPTUAL_ERROR",
       "circular-velocity-direction ailesinin 'hız vektörü merkeze doğrudur' çeldiricisi; circular-analogies'te farklı hareketlerin hız vektörlerinin karşılaştırılması. "
       "Kızılcık ve Güneş (2011) 'hız ve ivme aynı doğrultudadır' yanılgısını %5,07, 'hız vektörü net kuvvet doğrultusundadır' yanılgısını %4,20 oranında bulmuştur.",
       DI("Düzgün çembersel hareket yapan bir cismin çember üzerindeki bir noktada hız vektörü ϑ, ivme vektörü a ile gösteriliyor. Hangisi doğrudur?",
          "ϑ merkeze yönelir; a yörüngeye teğettir.",
          "ϑ ve a aynı doğrultudadır ve ikisi de merkeze yönelir.",
          "ϑ yörüngeye teğettir; a merkeze yöneliktir ve ϑ'ye diktir.",
          "ϑ merkezden dışarı yöneliktir; a merkeze doğrudur.",
          "ϑ yörüngeye teğettir; a da teğettir ve ϑ ile zıt yönlüdür.",
          "C", "B"),
       RM(["Çember üzerinde dönen cismi bir noktada serbest bıraksan hangi yönde gider? Bu yön hızın yönü mü?",
           "Hız merkeze doğru olsaydı cisim merkeze yaklaşır mıydı? Yarıçap sabit kalır mıydı?",
           "Hıza dik bir ivme hızın büyüklüğünü mü yoksa yönünü mü değiştirir?",
           "Kuvvet hızı nasıl değiştirir: büyüklüğünü, yönünü ya da ikisini?"],
          "Hız vektörü merkeze doğru olsaydı cisim yarıçap boyunca merkeze doğru ilerler ve çember çizmezdi.",
          "Çekiç atan atlet çekici bıraktığında çekiç, bırakıldığı andaki yörüngeye teğet doğrultuda uçar; bu doğrultu o andaki hızın doğrultusudur."),
       S("KG11", "MCCL", "TB"), "MEDIUM"),

    MC("string-cut-circular-motion-continues",
       "İp koptuğunda (ya da merkezcil kuvvet ortadan kalktığında) cisim çembersel yolunu bir süre sürdürür ya da merkezden dışarı doğru savrulur; merkezcil etki kopmadan sonra da devam eder.",
       "İp koptuğu anda cismin hızı yörüngeye teğettir. Net kuvvet sıfır olduğundan (yatay düzlemde ağırlık dengelenmişse) Newton'ın 1. yasası gereği cisim o teğet doğrultuda sabit hızla doğrusal gider. "
       "Merkezcil kuvvet yalnızca onu uygulayan ip varken vardır.",
       ["cizgisel-hiz", "newton-birinci-yasa", "merkezcil-kuvvet", "duzgun-cembersel-hareket"], LO("1.9"), "CONCEPTUAL_ERROR",
       "string-cut-trajectory ailesinin 'cisim merkezden dışa doğru (radyal) uçar' ve 'cisim kopma anından sonra eğri yol izlemeye devam eder' çeldiricileri. "
       "McCloskey ve ark. (1980) dış kuvvet yokken eğrisel hareket beklentisini belgelemiştir; Kızılcık ve Güneş (2011) 'merkezcil kuvvetin etkisi hareket bitse de devam eder' yanılgısını %13,99 oranında bulmuştur. FCI taksonomisinde I5 (circular impetus).",
       DI("Yatay, sürtünmesiz bir masada ipin ucuna bağlı bir bilye, üstten bakıldığında saat yönünde düzgün çembersel hareket yapıyor. Bilye çemberin en üst (kuzey) noktasındayken, hızı doğuya doğruyken ip kopuyor. "
          "Bilyenin kopmadan sonraki hareketi için hangisi doğrudur?",
          "Bir süre çember yayı boyunca hareketini sürdürür, sonra doğrusal yola geçer.",
          "Doğuya doğru, kopma anındaki hızıyla sabit hızlı doğrusal hareket yapar.",
          "Merkezden dışarı doğru (kuzeye) doğrusal hareket yapar.",
          "Merkeze doğru (güneye) doğrusal hareket yapar.",
          "Doğuya doğru gider ama giderek yavaşlayıp durur.",
          "B", "A"),
       RM(["Kopma anında bilyenin hızı hangi yönde? İp koptuktan sonra bilyeye yatay düzlemde hangi kuvvetler etki ediyor?",
           "İp varken bilyeyi hangi yöne çekiyordu? İp koptuğunda bu çekmeye ne olur?",
           "Newton'ın 1. yasasına göre net kuvvet sıfır olunca bilye ne yapar?",
           "Bilye çember yolunda kalmaya devam etseydi, merkeze doğru gerekli kuvveti hangi cisim uyguluyor olurdu?"],
          "Çember yolunda kalmak için merkeze yönelen bir kuvvet gerekir. İp koptuktan sonra bu kuvveti uygulayan hiçbir cisim kalmadığı için bilyenin çembersel hareketini sürdürmesi mümkün değildir.",
          "Dönen bir tekerleğin kenarından kopan çamur parçası yörüngeye teğet doğrultuda fırlar; çembersel yolda kalmaz ve radyal olarak da savrulmaz."),
       S("KG11", "MCCL", "FCI"), "HIGH"),

    MC("centrifugal-real-force",
       "Düzgün çembersel hareket yapan cisme merkezden dışa doğru, merkezcil kuvvete eşit büyüklükte gerçek bir 'merkezkaç kuvveti' etki eder; bu kuvvet cismi dışarı savurur.",
       "Yerdeki (eylemsiz) gözlemciye göre merkezkaç diye gerçek bir kuvvet yoktur; cismin dışarı savrulma eğilimi eylemsizliğidir (Newton'ın 1. yasası). Cisme etki eden net kuvvet merkeze yöneliktir.",
       ["merkezcil-kuvvet", "eylemsizlik", "yatay-viraj", "duzgun-cembersel-hareket"], LO("1.9", "1.10"), "CONCEPTUAL_ERROR",
       "string-cut-trajectory, vertical-circle-min-speed, flat-curve ve rail-system-circular ailelerinin 'merkezkaç kuvvet' çeldiricileri; fbd-identify-forces'ta dışa yönelik kuvvet oku. "
       "Ünlü ve Gök (2007), Kızılcık ve Güneş (2011, %8,80), FCI taksonomisinde CF (centrifugal force) ve Durkaya (2021) bunu doğrular: 33 öğretmen adayının 9'u merkezcil kuvveti dışa yönelik çizmiştir.",
       DI("Yatay bir yolda sabit süratle sağa viraj alan bir arabadaki yolcu kendini kapıya (virajın dışına) doğru bastırılmış hisseder. Yerdeki gözlemcinin bakış açısından bu durum nasıl açıklanır?",
          "Yolcuya dışa doğru etki eden gerçek bir merkezkaç kuvveti vardır.",
          "Yolcu eylemsizliği nedeniyle doğrusal yolda gitmek ister; araç ve koltuk yolcuya merkeze yönelen kuvvet uygulayarak onu çembersel yola zorlar.",
          "Merkezcil ve merkezkaç kuvvetleri eşit olduğundan yolcu dengededir.",
          "Yolcuya viraj içine doğru etki eden hiçbir kuvvet yoktur.",
          "Dışa doğru etki eden bir sürtünme kuvveti yolcuyu kapıya bastırır.",
          "B", "A"),
       RM(["Yolcuyu dışa iten kuvveti hangi cisim uyguluyor?",
           "Araç kaygan zeminde dönme gücünü kaybederse hangi yönde gider: radyal dışa mı, teğet doğrultuda mı?",
           "Yolcuya etki eden net kuvvetin yönü nedir? Bu yön ivmenin yönüyle uyumlu mu?",
           "'Hissedilen' bir etkiyle bir cismin uyguladığı gerçek kuvvet arasındaki fark nedir?"],
          "Kaygan zeminde araç, virajın dışına radyal olarak değil, kopma anındaki yola teğet doğrultuda gider; merkezkaç gerçek bir kuvvet olsaydı doğrudan dışarı fırlardı.",
          "Hızlanan bir otobüste geriye yaslandığınızı hissedersiniz ama sizi kimse geri itmiyor; otobüs size ileri kuvvet uyguluyor. Virajda 'dışa itilme' de benzer bir eylemsizlik hissidir."),
       S("UG07", "KG11", "FCI", "DUR21"), "HIGH"),

    MC("centripetal-force-extra-separate-force",
       "Merkezcil kuvvet, çembersel hareket yapan cisme ayrıca etki eden yeni bir kuvvettir; hareket çembersel olunca ortaya çıkar ve serbest cisim diyagramında diğer kuvvetlere eklenir.",
       "Merkezcil kuvvet ayrı bir kuvvet türü değildir; merkeze yönelen net (bileşke) kuvvetin adıdır. İp gerilmesi, sürtünme, normal kuvvet ya da ağırlık gibi gerçek kuvvetlerin merkeze yönelik bileşkesi merkezcil kuvvet görevi görür. "
       "Çembersel hareket merkezcil kuvvetin sonucudur, nedeni değil.",
       ["merkezcil-kuvvet", "serbest-cisim-diyagrami", "statik-surtunme", "gerilme-kuvveti"], LO("1.5", "1.10"), "CONCEPTUAL_ERROR",
       "fbd-identify-forces ailesinin 'merkezcil kuvvet ayrı bir kuvvet olarak çizilmiş' çeldiricisi; rotor-and-regulator ailesinin 'merkezcil kuvvet ayrı bir kuvvettir' çeldiricisi. "
       "Kızılcık ve Güneş (2011): öğrencilerin %11,01'i 'merkezcil kuvvet düzgün dairesel hareket olduğunda oluşan bir kuvvettir', %13,99'u 'merkezcil kuvvetin etkisi hareket bitse de devam eder' görüşündedir.",
       DI("Yatay, pürüzlü bir platformun kenarında duran bir cisim, platformla birlikte sabit açısal hızla dönüyor ve platforma göre kaymıyor. Cismin serbest cisim diyagramında merkezcil kuvvet için hangisi doğrudur?",
          "Ağırlık, normal kuvvet ve sürtünme kuvvetine ek olarak, merkeze doğru ayrı bir 'merkezcil kuvvet' da çizilir.",
          "Ayrı bir merkezcil kuvvet çizilmez; platformun cisme uyguladığı ve merkeze yönelen statik sürtünme kuvveti merkezcil kuvvet görevini üstlenir.",
          "Merkezcil kuvvet, ağırlık ile normal kuvvetin bileşkesidir.",
          "Merkezcil kuvvet merkezden dışarı doğru çizilir.",
          "Cisim sabit hızla döndüğü için cisme sürtünme etki etmez; merkezcil kuvvet çizilmez.",
          "B", "A"),
       RM(["Cisme çevresindeki hangi cisimler kuvvet uyguluyor? Bu kuvvetlerden hangisi merkeze doğru?",
           "Merkeze yönelen kuvveti uygulayan cisim kim?",
           "Platform çok kaygan olsaydı cisim ne yapardı? Bu hangi kuvvetin yokluğunu gösterir?",
           "Hem sürtünmeyi hem ayrı bir merkezcil kuvveti çizersen merkeze yönelen kuvvet iki kez sayılmış olmaz mı?"],
          "Hem sürtünmeyi hem de ayrı bir merkezcil kuvveti çizersek merkeze doğru gerekenin iki katı kuvvet olur; bu durumda ivme mω²r ile uyuşmaz.",
          "'Takım kaptanı' ayrı bir oyuncu değildir, mevcut oyunculardan birinin üstlendiği rolün adıdır. Merkezcil kuvvet de ip gerilmesi ya da sürtünme gibi kuvvetlerden birinin (ya da bileşkesinin) üstlendiği rolün adıdır."),
       S("KG11", "UG07", "DUR21"), "HIGH"),

    MC("centripetal-force-decreases-with-radius",
       "Merkezcil kuvvet, cismin dönme merkezine uzaklığı (yarıçap) arttıkça her koşulda azalır.",
       "Merkezcil kuvvet F = mϑ²/r = mω²r ile verilir: sabit çizgisel hızda yarıçapla ters orantılıdır, sabit açısal hızda (aynı platform üzerindeki cisimler) yarıçapla doğru orantılı artar. "
       "Hangi niceliğin sabit tutulduğuna dikkat etmek gerekir.",
       ["merkezcil-kuvvet", "yatay-duzlemde-cembersel", "acisal-hiz", "oran-oranti"], LO("1.10"), "FORMULA_APPLICATION_ERROR",
       "circular-variables-data ailesinin 'F_m yarıçapla doğru orantılıdır' / ters kurma çeldiricileri; rotating-platform-friction ailesinin 'merkeze yakın cisim önce kayar' çeldiricisi ve "
       "coupled-wheels'te 1/r ilişkisinin ters kurulması. Ünlü ve Gök (2007): 8. ve 9. sorularda öğrencilerin %30'u merkezcil kuvvetin merkeze uzaklık arttıkça azaldığını savunmuştur.",
       DI("Yatay dönen bir platform üzerinde, aynı kütleli iki cisim platformla birlikte aynı açısal hızla dönüyor; biri dönme ekseninden 0,5 m, diğeri 1 m uzaklıkta. "
          "Cisimleri çembersel yolda tutmak için gereken merkezcil kuvvetler (0,5 m'deki F_1, 1 m'deki F_2) için hangisi doğrudur?",
          "F_2 = F_1/2; çünkü merkezcil kuvvet yarıçapla ters orantılıdır.",
          "F_2 = 2F_1; çünkü açısal hız aynıyken F = mω²r'dir.",
          "F_2 = 4F_1; çünkü merkezcil kuvvet yarıçapın karesiyle orantılıdır.",
          "F_2 = F_1; çünkü kütleleri aynıdır.",
          "F_2 = F_1/4; çünkü merkezcil kuvvet yarıçapın karesiyle ters orantılıdır.",
          "B", "A"),
       RM(["Bu iki cismin hangi niceliği aynıdır: çizgisel hız mı, açısal hız mı?",
           "F = mϑ²/r ve F = mω²r bağıntılarının ikisi de doğruysa hangisini bu soruda kullanmak daha uygundur ve neden?",
           "Aynı sürede iki cisim de bir tur atıyorsa dış cisim daha uzun bir yol alıyor mu? Çizgisel hızı ne olur?",
           "Platformun dönüşünü hızlandırdığında hangi cisim önce kayar ve neden?"],
          "Dönen bir platformda dış kenardaki cisim daha çabuk kayar; yani merkezcil kuvvet gereksinimi dışa doğru artar. 'Uzaklık arttıkça azalır' düşüncesi bunu açıklayamaz.",
          "Dönen bir atlıkarıncada dış sıradaki hayvanın üstündeki çocuk, aynı sürede daha büyük çember çizer ve daha hızlı gider; onu çembersel yolda tutmak için daha sıkı tutunması gerekir."),
       S("UG07", "KG11", "TB"), "HIGH"),
]

_U1_END = len(MISCONCEPTIONS)


def _balance_answer_positions(items):
    """Tanı sorularında doğru şıkkın konumunu A–E arasında dengeler (yazım sırasında doğru şık hep aynı harfe düşmesin).

    Şıklar dairesel olarak kaydırılır; göreli sıra korunur. Metin içinde şık harfine gönderme yoktur."""
    for i, m in enumerate(items):
        di = m["diagnostic_item"]
        letters = "ABCDE"
        shift = (letters.index(di["answer"]) - i % 5) % 5   # doğru şık, i'inci sıradaki harfe gelsin
        old = [di["options"][k] for k in letters]
        new = old[shift:] + old[:shift]
        remap = {letters[(j + shift) % 5]: letters[j] for j in range(5)}
        di["options"] = dict(zip(letters, new))
        di["answer"] = remap[di["answer"]]
        di["misconception_option"] = remap[di["misconception_option"]]


_balance_answer_positions(MISCONCEPTIONS[_U1_START:_U1_END])
