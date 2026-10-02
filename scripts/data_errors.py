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
