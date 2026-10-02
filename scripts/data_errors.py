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


# ============================================================================================
# BÖLÜM 3 — KAVRAM YANILGILARI: ÜNİTE 2 (ELEKTRİK VE MANYETİZMA, FİZ.11.2.1–FİZ.11.2.13)
# ============================================================================================
# Ünite 2'ye özgü ek kaynaklar. Üst bölümdeki SRC kayıtlarından CSEM (MAL01), Furió–Guisasola (FG98), Törnkvist vd. (TPT93),
# Viennot–Rainson (VR92, RTV94), Campos vd. (CAMP19), Wallace vd. (WJL23), Saarelainen vd. (SAA07), Borges–Gilbert (BG98),
# Guisasola vd. (GAZ04), Voutsina–Ravanis (VR11), Ürek–Çoramık (UC21), Secrest–Novodvorsky (SN05), Turgut vd. (TUR16),
# Taşkın–Ünlü Yavaş (TY19) burada da kullanılır; bu çalışmada bulunan ve okunan yeni kaynaklar aşağıdadır.
# Okuma düzeyi her citation'ın köşeli parantez notundadır. Transformatör ve alternatif akım için öğrenci yanılgısı ölçen akademik çalışma
# bulunamadı; o kayıtlar yalnız ders kitabına (Tier 1) dayanır ve bu durum how_it_appears alanında açıkça yazılıdır.
SRC.update({
    "SIN08": _s("Singh, C. (2008). Improving students' understanding of magnetism. ASEE Annual Conference & Exposition 2008 bildirisi (arXiv:1701.01523). "
                "[tam metin okundu: 466 öğrenci son-test, 127 öğrenci ön-test, 25 görüşme; kalkülüslü giriş fiziği (üniversite); akım taşıyan teller, "
                "mıknatıs–yük, parçacığa etkiyen kuvvet soruları ve yaygın yanlış seçenekler]",
                "https://arxiv.org/abs/1701.01523", 2, True),
    "MBS22": _s("Maries, A., Brundage, M. J. & Singh, C. (2022; arXiv:2311.17170, Phys. Rev. Phys. Educ. Res. 18 olarak kayıtlı). Using the Conceptual Survey of "
                "Electricity and Magnetism to investigate progression in student understanding from introductory to advanced levels. "
                "[tam metin okundu; üniversite: giriş düzeyi, ileri düzey lisans ve lisansüstü; CSEM maddeleri, en sık yanlış seçenekler ve yazılı gerekçeler]",
                "https://arxiv.org/abs/2311.17170", 2, True),
    "ZUZ14": _s("Zuza, K., Almudí, J.-M., Leniz, A. & Guisasola, J. (2014). Addressing students' difficulties with Faraday's law: A guided problem solving approach. "
                "Physical Review Special Topics – Physics Education Research, 10, 010122. [tam metin PDF'i okundu; giriş bölümündeki literatür özeti "
                "(ortaöğretim ve ilk yıl üniversite öğrencilerinin indüksiyondaki başlıca güçlükleri, a–f maddeleri) kullanıldı]",
                "https://doi.org/10.1103/PhysRevSTPER.10.010122", 2, True),
    "JPP17": _s("Jelicic, K., Planinic, M. & Planinsic, G. (2017). Analyzing high school students' reasoning about electromagnetic induction. Physical Review "
                "Physics Education Research, 13, 010112. [yalnızca özet okundu: 9 Hırvat lise öğrencisiyle görüşme; geleneksel öğretimde indüksiyon için "
                "tutarlı zihinsel model oluşmuyor]",
                "https://doi.org/10.1103/PhysRevPhysEducRes.13.010112", 2, True),
    "THG08": _s("Thong, W. M. & Gunstone, R. (2008). Some student conceptions of electromagnetic induction. Research in Science Education, 38, 31–44. "
                "[yalnızca arama özeti görüldü: 15 görüşme, ikinci sınıf fizik öğrencileri; indüksiyon akımının bobindeki akımla orantılı olduğu, 'zıt yönlü' "
                "ile 'karşı koyma' karışıklığı; tam metin ve DOI sayfası açılamadı]",
                "https://www.researchgate.net/publication/225802488_Some_Student_Conceptions_of_Electromagnetic_Induction", 2, False),
    "CAO16": _s("Cao, Y. & Brizuela, B. M. (2016). High school students' representations and understandings of electric fields. Physical Review Physics "
                "Education Research, 12, 020102. [özet ve giriş okundu: 92 Çinli 15–16 yaş öğrenci, ön öğretim; giriş bölümü literatürde 'büyük yük daha güçlü "
                "kuvvet uygular' ve 'alan çizgisi hareketli yükün yörüngesidir' düşüncelerini aktarır]",
                "https://doi.org/10.1103/PhysRevPhysEducRes.12.020102", 2, True),
    "KUS16": _s("Kustusch, M. B. (2016). Assessing the impact of representational and contextual problem features on student use of right-hand rules. Physical "
                "Review Physics Education Research, 12, 010102. [özet ve giriş okundu; üniversite öğrencileri; sağ el kuralı sorularında doğruluk düşük, "
                "kuralın uygulanış biçimi ve zorluğu başarıyı etkiliyor]",
                "https://doi.org/10.1103/PhysRevSTPER.12.010102", 2, True),
})

_U2_START = len(MISCONCEPTIONS)

MISCONCEPTIONS += [
    # --- FİZ.11.2.1: Coulomb Yasası (elektriksel kuvvet) ---
    MC("bigger-charge-exerts-bigger-force",
       "Büyük yüklü cisim, küçük yüklü cisme, küçüğün büyüğe uyguladığından daha büyük elektriksel kuvvet uygular.",
       "İki yüklü cisim arasındaki elektriksel kuvvetler etki–tepki çiftidir: büyüklükleri eşit, yönleri zıttır ve farklı cisimlere etki eder. "
       "Coulomb Yasası'ndaki q₁·q₂ çarpımı iki yüke simetriktir. Yükü büyük olanın alanı daha büyüktür, ama küçük yük de büyük yüke aynı büyüklükte kuvvet uygular; "
       "kütleleri farklıysa farklı olan, kuvvet değil ivmedir.",
       ["elektriksel-kuvvet", "coulomb-yasasi", "etki-tepki", "noktasal-yuk"], LO("2.1"), "CONCEPTUAL_ERROR",
       "coulomb-direction-newton3 ailesinin 'büyük yük küçük yüke daha büyük kuvvet uygular' çeldiricisi; coulomb-free-charge-dynamics ailesinin 'hafif parçacığa uygulanan "
       "kuvvet daha büyüktür' çeldiricisi. Cao ve Brizuela (2016) girişi, CSEM çalışmasına dayanarak 'büyük yüklerin daha güçlü kuvvet uyguladığı' düşüncesini yaygın bulgu olarak aktarır "
       "(bu kaynakta oran ölçülmemiştir; örneklemler üniversite düzeyindedir).",
       DI("Yalıtkan ince ipliklerle asılı, noktasal sayılabilecek iki küçük kürenin yükleri +4q ve +q'dur; küreler aralarında d uzaklık olacak biçimde duruyor. "
          "+4q yüklü kürenin +q yüklü küreye uyguladığı kuvvet F₁, +q yüklü kürenin +4q yüklü küreye uyguladığı kuvvet F₂ ile gösterilirse hangisi doğrudur?",
          "F₁ = 4F₂; çünkü +4q yüklü küre daha büyük yüke sahiptir.",
          "F₁ = F₂; kuvvetler eşit büyüklükte ve zıt yönlüdür.",
          "F₂ = 4F₁; çünkü +q yüklü küre daha küçük olduğu için yük etkisinden daha fazla etkilenir.",
          "F₁ = F₂; kuvvetler eşit büyüklükte ve aynı yönlüdür.",
          "F₁ ve F₂'nin büyüklüğü yalnız araya giren ortama bağlıdır; yük miktarı kuvveti belirlemez.",
          "B", "A"),
       RM(["F = k·q₁·q₂/d² bağıntısında q₁ ile q₂ yer değiştirirse sonuç değişir mi?",
           "Birinci küre ikinciyi iterse, ikinci küre birinciye ne yapar? Bu iki kuvvet hangi cisimlere etki ediyor?",
           "İki küreyi serbest bırakırsak ikisi de aynı ivmeyle mi hareket eder? İvme farkı kuvvet farkından mı kütle farkından mı gelir?",
           "Tek bir yükün (+4q) kuvveti nasıl 'tek taraflı' olabilir? Etki eden bir cisim olduğunda karşı cismin ona hiçbir şey yapmadığını düşünebilir miyiz?"],
          "Kütleleri eşit, yükleri +4q ve +q olan iki küre serbest bırakılırsa ikisi de aynı büyüklükte ivmeyle birbirinden uzaklaşır; çünkü kuvvetleri eşittir. "
          "'Büyük yük daha çok iter' görüşü, bu iki kürenin ivmelerinin farklı olmasını gerektirirdi; böyle bir gözlem yoktur.",
          "Bir kamyon ile küçük araba çarpışınca arabanın zarar görmesi kamyonun arabaya daha büyük kuvvet uyguladığı anlamına gelmez; kuvvetler eşittir, "
          "fark kütlelerin ivmeleri ve dayanıklılığındadır. Yüklü kürelerde de büyük yük 'kamyon', küçük yük 'araba' gibi değildir; iki yük birbirine eşit kuvvet uygular."),
       S("CAO16", "MAL01", "TB"), "MEDIUM"),

    MC("coulomb-force-inverse-distance",
       "Yükler arasındaki elektriksel kuvvet uzaklıkla ters orantılıdır: uzaklık iki katına çıkarsa kuvvet yarıya iner.",
       "Coulomb Yasası'nda kuvvet uzaklığın karesiyle ters orantılıdır (F ∝ 1/d²): uzaklık 2 katına çıkarsa kuvvet 1/4'üne, 3 katına çıkarsa 1/9'una iner. "
       "F–d grafiği azalan bir eğridir; F–1/d² grafiği ise orijinden geçen doğrudur.",
       ["coulomb-yasasi", "elektriksel-kuvvet", "ters-kare-iliskisi", "oran-oranti", "grafik-egim-alan"], LO("2.1"), "FORMULA_SELECTION_ERROR",
       "coulomb-data-table-graph ailesinin 'd ile ters orantılıdır' ve coulomb-ratio-generalization ailesinin 'd iki katına çıkınca kuvvet yarıya iner' çeldiricileri. "
       "Ders kitabı etkinliği (s. 159, 14. etkinlik) 2d durumunu doğrudan sorar. Bu kayıt için yaygınlığını ölçen akademik bir çalışma bulunamadı; Wallace vd. (2023) yalnızca "
       "ters kare vektörlerinde başka hataları (skaler toplama, r veya r²'yi yanlış bileşenlere ayırma) belgelemiştir.",
       DI("Bir deneyde iki küçük yüklü cisim arasındaki uzaklık değiştirilerek elektriksel kuvvet ölçülüyor (yükler sabit): "
          "uzaklık 2 cm iken F = 36 mN, 4 cm iken F = 9 mN. Uzaklık 6 cm yapılırsa kuvvet kaç mN olur?",
          "4 mN",
          "12 mN",
          "18 mN",
          "27 mN",
          "81 mN",
          "A", "B"),
       RM(["2 cm'den 4 cm'e geçerken uzaklık kaç katına çıktı, kuvvet kaç katına düştü? Yarıya mı indi?",
           "Kuvvet uzaklıkla ters orantılı olsaydı 4 cm'de kaç mN beklenirdi? Ölçüm bununla uyuşuyor mu?",
           "6 cm, 2 cm'nin kaç katıdır? Aynı mantıkla kuvvet kaç katına düşmeli?",
           "F ile 1/d² arasındaki grafiği çizsen nasıl bir şekil elde edersin?"],
          "Tabloda uzaklık 2 katına çıkarken kuvvet 36'dan 9'a iniyor, yani yarıya değil dörtte bire düşüyor. 'Ters orantı' ile bu veri uyuşmaz.",
          "Bir lambanın ışığı 2 m uzaklıktan 1 m'ye göre sönükleşir; uzaklık iki katına çıkınca aynı ışık daha büyük bir alana yayıldığından yüzeye düşen ışık dörtte bire iner. "
          "Elektriksel kuvvet de aynı 'ters kare' mantığıyla uzaklıkla azalır (benzetme yalnız ilişkinin biçimi içindir)."),
       S("TB", "WJL23"), "MEDIUM"),

    MC("collinear-forces-added-as-magnitudes",
       "Aynı doğru üzerindeki yüklerde bir yüke etki eden bileşke kuvvet, diğer yüklerin uyguladığı kuvvetlerin büyüklüklerinin toplamıdır.",
       "Elektriksel kuvvet vektörel bir niceliktir. Aynı doğru üzerinde yönler aynıysa büyüklükler toplanır, zıtsa birbirinden çıkarılır. "
       "Bu yüzden iki eşit yükün tam ortasındaki yüke etki eden bileşke kuvvet sıfırdır; kuvvetlerin yönü, yüklerin işaretine ve konumuna bağlıdır.",
       ["coulomb-yasasi", "elektriksel-kuvvet", "bileske-kuvvet", "vektorel-nicelik"], LO("2.1"), "VECTOR_ERROR",
       "coulomb-collinear-net-force ailesinin 'bileşke kuvvet büyüklüklerin toplamıdır' çeldiricisi. Wallace, Jones ve Lin (2023): Coulomb ve elektrik alan dahil ters kare vektörlerinde "
       "678 sınav kâğıdında en sık görülen hatalardan biri vektörleri skalermiş gibi toplamaktır (üniversite düzeyi, giriş mekaniği ve E&M).",
       DI("Aralarındaki uzaklıklar eşit (d) olan K, L ve M noktasal yükleri aynı doğru üzerinde, bu sırayla yerleşmiş ve üçü de +q yüklüdür. K'nin L'ye uyguladığı kuvvetin "
          "büyüklüğü F'dir. L'ye etki eden bileşke kuvvet için hangisi doğrudur?",
          "2F büyüklüğünde ve M yönündedir.",
          "F büyüklüğünde ve K yönündedir.",
          "Sıfırdır.",
          "2F büyüklüğünde ve K yönündedir.",
          "F/4 büyüklüğünde ve M yönündedir.",
          "C", "A"),
       RM(["K, L'yi hangi yöne iter? M, L'yi hangi yöne iter?",
           "Bu iki kuvvetin yönleri aynı mı, zıt mı? Büyüklükleri nasıl karşılaştırılır?",
           "L, iki yük arasında tam ortadaysa, hangi yöne gitmek isterdi?",
           "Kuvvet vektör olmasaydı, L'nin ortada dengede kalmasını nasıl açıklardın?"],
          "L serbest olsaydı K ve M'nin her ikisi de L'yi itecekti, ama zıt yönlerde. Toplam 2F olsaydı L, iki yükten birine doğru ivmelenirdi; oysa simetriden dolayı hangisine gideceğini söyleyemeyiz. "
          "Bileşkenin sıfır olması simetriyle uyumludur.",
          "İki arkadaşın seni aynı büyüklükte zıt yönlerden çektiğini düşün: toplam çekme 2F değil, sıfırdır ve olduğun yerde kalırsın. Kuvvetlerin yönü 'toplam'ı belirler."),
       S("WJL23", "VR92"), "HIGH"),

    # --- FİZ.11.2.2: Elektriksel alan ---
    MC("field-line-is-particle-trajectory",
       "Elektrik alan çizgisi, o alana bırakılan yüklü parçacığın izleyeceği yolu gösterir; serbest bırakılan parçacık alan çizgisi boyunca hareket eder.",
       "Alan çizgisinin her noktadaki teğeti, o noktadaki elektriksel alanın (pozitif yüke etkiyen kuvvetin) yönünü gösterir. Parçacığın ivmesi alan yönündedir, ama konumu ve hızı "
       "ivmenin geçmişine bağlıdır. Alan çizgileri eğri olduğunda parçacık çizgiyi izlemez; yörünge ile alan çizgisi yalnızca çizgiler doğru ve parçacık ilk hızsız bırakıldığında çakışır.",
       ["elektriksel-alan-cizgileri", "elektriksel-alan", "elektriksel-kuvvet", "noktasal-yuk"], LO("2.2"), "CONCEPTUAL_ERROR",
       "efield-direction-and-lines ailesinin 'alan çizgisi yüklü cismin hareket yolunu gösterir' çeldiricisi; efield-charged-particle-deflection ve efield-uniform-plates ailelerinde parçacığın "
       "yolunu alan çizgisiyle özdeşleştiren seçenekler. Cao ve Brizuela (2016) girişi, Furió–Guisasola (1998) ve Törnkvist vd. (1993)'e dayanarak 'alan çizgisinin hareketli yükün yörüngesi "
       "olduğunu' yaygın görüş olarak aktarır; CAMP19 alan çizgilerinin yorumlanmasının alan ve süperpozisyon anlayışına etkisini inceler (üniversite örneklemleri).",
       DI("İki zıt işaretli noktasal yükün çevresinde oluşan elektrik alanda, eğri bir alan çizgisinin üzerindeki P noktasında duran, pozitif yüklü küçük bir parçacık ilk hızsız "
          "bırakılıyor. Parçacığa yalnız elektriksel kuvvet etki ettiğine göre hareketi için hangisi doğrudur?",
          "P'den geçen alan çizgisini birebir izleyerek hareket eder.",
          "P'de alan çizgisinin teğeti doğrultusunda ivmelenmeye başlar; çizgi eğri olduğundan genellikle çizgiyi izlemez.",
          "Alan çizgisine dik doğrultuda ivmelenir.",
          "Alan çizgisinin tersi yönünde ivmelenir.",
          "Alan çizgisi gerçek bir yol olmadığı için hareketsiz kalır.",
          "B", "A"),
       RM(["Alan çizgisinin teğeti neyin yönünü gösteriyor: kuvvetin mi, hızın mı?",
           "İvme ile hız aynı doğrultuda olmak zorunda mı? Bir cismi yukarı atıp ivmesine bakarsak yol ile ivme aynı doğrultuda mı?",
           "Parçacık ilk anda çizgi boyunca kıpırdarsa, bir an sonra hız yönü ile o yeni noktadaki alan yönü aynı olur mu?",
           "Alan çizgisi eğri ise parçacık çizgi boyunca gidebilmek için sürekli yön mü değiştirmek zorunda kalır? Bunu sağlayan şey ne olur?"],
          "Bir yatay atışta ivme sürekli aşağı yönlüdür ama cismin yolu parabol olur; ivmenin yönü yolun teğeti değildir. Alan çizgisi ivmenin (kuvvetin) yönünü gösterdiğine göre yörünge ile çakışması beklenemez.",
          "Virajda dönen bir arabanın ivmesi merkeze doğrudur, ama araba merkeze gitmez; hız yönü ile ivme yönü aynı değildir. Alan çizgisi 'ivmenin yönünü' çizer, 'arabanın yolunu' değil."),
       S("CAO16", "FG98", "TPT93", "CAMP19"), "HIGH"),

    MC("field-depends-on-test-charge",
       "Elektrik alanın büyüklüğü, alana konulan test yüküne bağlıdır; test yükü büyürse alan da büyür.",
       "E = F/q ile tanımlanan elektriksel alan, kaynak yüke ve noktanın konumuna (uzaklığa, ortama) bağlıdır; alana konan test yükünden bağımsızdır. "
       "Test yükü q katına çıkarsa o noktadaki kuvvet q katına çıkar, ama F/q oranı, yani alan değişmez.",
       ["elektriksel-alan", "noktasal-yuk", "elektriksel-kuvvet", "oran-oranti"], LO("2.2"), "CONCEPTUAL_ERROR",
       "efield-data-table-graph ailesinin 'E, alandaki test yüküne bağlıdır' ve efield-point-charge-ratio ailesinin 'test yükü büyürse alan da büyür' çeldiricileri. "
       "Törnkvist vd. (1993): kuvvet ile kuvvet alanı kavramlarının karışması; Furió ve Guisasola (1998): üniversite öğrencileri alan fikri yerine uzaktan etki modelini tercih eder "
       "(kaynaklar özet düzeyinde; örneklem üniversite).",
       DI("Q yüklü bir noktasal kaynaktan belli bir uzaklıktaki A noktasına +q test yükü konulduğunda A'daki elektrik alan E, test yüküne etki eden kuvvet F olarak ölçülüyor. "
          "Test yükü +3q'lu bir yükle değiştirilirse A noktasındaki elektrik alan ve test yüküne etki eden kuvvet nasıl değişir?",
          "Alan 3E olur, kuvvet 3F olur.",
          "Alan E olarak kalır, kuvvet 3F olur.",
          "Alan 3E olur, kuvvet F olarak kalır.",
          "Alan E, kuvvet F olarak kalır.",
          "Alan E/3 olur, kuvvet F olarak kalır.",
          "B", "A"),
       RM(["Elektrik alanın tanımı E = F/q ise q üç katına çıkınca F'ye ne olur? Oran değişir mi?",
           "A noktasındaki alanı kim oluşturuyor: Q kaynağı mı, A'ya konan küçük yük mü?",
           "Test yükünü hiç koymasak A noktasında alan var mıdır?",
           "Sıfır yüklü (test yükü olmayan) bir noktada alandan söz etmek anlamsız mıdır?"],
          "Alan test yüküne bağlı olsaydı test yükünü kaldırdığımızda alan da kaybolurdu; oysa Q kaynağı aynı yerdedir ve çevresindeki uzayın özelliği de ondan kaynaklanır. "
          "Ölçtüğümüz kuvvet test yüküyle değişir, alan ise değişmez.",
          "Bir yolun eğimi, yola çıkan arabanın ağırlığına bağlı değildir; ağır araba daha büyük kuvvete maruz kalır ama eğim aynı kalır. Alan 'eğim' gibi yerin özelliğidir, kuvvet ise yüke bağlı sonuçtur."),
       S("TPT93", "FG98"), "HIGH"),

    MC("midpoint-between-opposite-charges-zero-field",
       "Eşit büyüklükte, zıt işaretli iki yükün tam ortasında alanlar birbirini götürür; bileşke elektrik alan sıfırdır.",
       "Zıt işaretli yüklerin ortasında her iki yükün alanı aynı yönündedir (pozitif yükten uzağa, negatif yüke doğru) ve büyüklükleri toplanır: bileşke alan tek yükünkinin iki katıdır. "
       "Alanın sıfır olması için alanların zıt yönlü olması gerekir; bu, eşit işaretli yüklerin ortasında gerçekleşir.",
       ["bileske-elektriksel-alan", "elektriksel-alan", "noktasal-yuk", "vektorel-nicelik"], LO("2.2"), "VECTOR_ERROR",
       "efield-superposition-collinear ailesinin 'zıt işaretli yüklerin ortasında alan sıfırdır' çeldiricisi (tersi, 'iki eşit yükün ortasında alan 2E'dir' çeldiricisidir). "
       "Singh (2008): görüşmelerde bazı öğrenciler iki eşit ve zıt yükün orta noktasında alanın 'sıfır olduğunu' savundu ve bunu açıklarken alanı yönleriyle çizmekte güçlük çekti; "
       "Viennot ve Rainson (1992) ile Rainson vd. (1994) alan süperpozisyonunda nedensel yorumlama güçlüklerini belgeler (üniversite örneklemleri).",
       DI("Birbirinden 2d uzaklıktaki +q (solda) ve −q (sağda) noktasal yüklerin tam ortasındaki K noktasında, her bir yükün tek başına oluşturduğu elektrik alanın büyüklüğü E'dir. "
          "K noktasındaki bileşke elektrik alan için hangisi doğrudur?",
          "Sıfırdır; çünkü iki alan birbirini götürür.",
          "2E büyüklüğünde ve −q yüküne doğrudur.",
          "2E büyüklüğünde ve +q yüküne doğrudur.",
          "E büyüklüğünde ve −q yüküne doğrudur.",
          "√2 E büyüklüğünde olup yatayla 45° açı yapar.",
          "B", "A"),
       RM(["K noktasına küçük bir pozitif test yükü koysak +q onu hangi yöne iter?",
           "Aynı test yükünü −q hangi yöne çeker?",
           "Bu iki kuvvet (ve alan) aynı yönde mi, zıt yönde mi?",
           "Alanın sıfır olabilmesi için iki alanın hangi koşulu sağlaması gerekirdi? İki yük aynı işaretli olsaydı ortada ne olurdu?"],
          "Pozitif test yükü ortada olsaydı, solundaki +q onu sağa iterdi, sağındaki −q ise yine sağa çekerdi; iki etki zıt değil, aynı yönde. Bu yüzden test yükü ortada kalamaz, sağa doğru ivmelenir; alan sıfır olamaz.",
          "İki kişi bir sandığı aynı yönden, biri iterek biri çekerek hareket ettirirse sandık daha çok kuvvetle gider; birbirlerini götürmezler. Zıt yüklerin ortasında test yükü için 'iten' ve 'çeken' aynı tarafa etki eder."),
       S("SIN08", "RTV94", "VR92"), "HIGH"),

    MC("negative-charge-force-along-field",
       "Negatif yüklü bir parçacığa etki eden elektriksel kuvvet, elektrik alan yönündedir (kuvvet her zaman alanla aynı yönlüdür).",
       "F = qE bağıntısında q'nun işareti kuvvetin yönünü belirler: pozitif yüke etkiyen kuvvet alanla aynı yönde, negatif yüke etkiyen kuvvet alana zıt yöndedir. "
       "Elektron, alan çizgilerinin yönüne ters doğru (pozitif levhaya doğru) ivmelenir.",
       ["elektriksel-alan", "elektriksel-kuvvet", "elektrik-yuku", "elektriksel-alan-cizgileri"], LO("2.2"), "SIGN_ERROR",
       "efield-charged-particle-deflection ailesinin 'elektron pozitif levhadan uzağa sapar' ve efield-uniform-plates ailesinin alan yönünü ters bilme çeldiricileri. "
       "Wallace vd. (2023): elektrik alan ya da kuvvetin bileşenlerinin işaretini yük işaretine yanlış bağlama, ters kare vektörlerinde sık görülen dört hatadan biridir; "
       "Maries vd. (2022): 'negatif yük olduğu için sola gider' türü gerekçeler CSEM yanıtlarında görülmüştür (üniversite düzeyi).",
       DI("Yatay konumda ve birbirine paralel iki levha arasında, düşey aşağı yönlü düzgün bir elektrik alan var. Bir elektron levhalara paralel bir ilk hızla levhalar arasına giriyor "
          "ve yalnız elektriksel kuvvetin etkisinde kalıyor. Elektronun sapma yönü için hangisi doğrudur?",
          "Aşağı doğru sapar; çünkü elektriksel kuvvet alan yönündedir.",
          "Yukarı doğru sapar; çünkü negatif yüke etki eden kuvvet alanın tersi yöndedir.",
          "Sapmaz; çünkü ilk hızı alana diktir.",
          "İlk hızı doğrultusunda hızlanır; çünkü kuvvet hız yönündedir.",
          "Önce yukarı sonra aşağı sapar; çünkü alan yönü sürekli değişir.",
          "B", "A"),
       RM(["Alanın yönü hangi yüke etkiyen kuvvetin yönüyle tanımlanıyor?",
           "Pozitif bir parçacık bu alana girse hangi yöne sapardı? Elektronun yük işareti ters olunca sapma yönü nasıl olur?",
           "F = qE bağıntısında q negatifse F ile E arasında nasıl bir yön ilişkisi vardır?",
           "Elektron levhalardan hangisine doğru hareket eder: alan çizgisinin çıktığı levhaya mı, girdiği levhaya mı?"],
          "Alan aşağı yönlü ise alanın çıktığı yer üstteki (+) levha, girdiği yer alttaki (−) levhadır. Elektron negatif olduğundan pozitif levhaya, yani yukarı çekilir. "
          "Kuvvet alan yönünde olsaydı elektron negatif levhaya, kendi cinsinden yüke doğru gider ve zıt cins çekme kuralı bozulurdu.",
          "Bir yokuşta 'aşağı' yönü alan yönü olsun; pozitif yük aşağı yuvarlanır, ama negatif yük yukarı yuvarlanır. Yük işareti, hangi yöne yuvarlanacağını belirleyen 'ters çevirme düğmesi' gibidir."),
       S("WJL23", "MBS22", "TB"), "MEDIUM"),

    # --- FİZ.11.2.3: Faraday kafesi ---
    MC("conductor-shell-does-not-shield-inner-charge",
       "İletken kabuğun (Faraday kafesinin) içindeki yük ile kabuğun dışındaki yük birbirine eşit büyüklükte, zıt yönlü kuvvet uygular; kabuk iç yükü dış yükten korumaz.",
       "Statik dengede iletkenin içinde elektriksel alan sıfırdır: kabuk üzerindeki yükler, dış yükün alanını kabuğun iç bölgesinde sıfırlayacak biçimde yeniden dağılır. "
       "Bu yüzden kabuğun merkezindeki yüke dışarıdaki yükten ötürü net kuvvet etki etmez; dıştaki yüke ise kabuğun dış yüzeyindeki yük dağılımı kuvvet uygular. "
       "Etki–tepki ilkesi yükün kendisine değil, birbirine kuvvet uygulayan yük çiftlerine uygulanır; kabuk bu çiftlerin parçasıdır.",
       ["faraday-kafesi", "elektriksel-alan", "elektriksel-kuvvet", "etki-tepki"], LO("2.3"), "CONCEPTUAL_ERROR",
       "fcage-verify-claims ailesinin kafes içi/dışı etkileşimini yanlış yorumlayan çeldiricileri. Maries vd. (2022): CSEM'in kabuk soruları (Q13–Q14) ileri düzey lisans öğrencileri dahil "
       "bütün düzeylerde kalıcı güçlük gösterir; Q14'ü giriş düzeyinde %38, ileri düzeyde %44 doğru yanıtlamış, en yaygın yanlış yanıt 'iki yük birbirine eşit ve zıt kuvvet uygular' (giriş %34, ileri düzey %29).",
       DI("Nötr ve yalıtılmış, içi boş bir iletken küresel kabuğun tam merkezinde +q yüklü bir cisim asılı duruyor; kabuğun dışında, kabuğa yakın bir noktada ise +Q yüklü küçük bir cisim sabit tutuluyor. "
          "Yükler dengeye ulaştıktan sonra aşağıdakilerden hangisi doğrudur?",
          "+q ve +Q yüklü cisimler birbirine eşit büyüklükte ve zıt yönlü kuvvet uygular.",
          "+q yüklü cisme net elektriksel kuvvet etki etmez; +Q yüklü cisme net bir kuvvet etki eder.",
          "+q yüklü cisme net bir kuvvet etki eder; +Q yüklü cisme net kuvvet etki etmez.",
          "İki cisme de net kuvvet etki etmez; kabuk her iki yönde de koruma sağlar.",
          "İki cisme de farklı büyüklükte net kuvvet etki eder; +q yüklü cisme etki eden daha büyüktür.",
          "B", "A"),
       RM(["Kabuğun iletken olması iç bölgede dış yükün alanına ne yapar? Bu alanın değeri nedir?",
           "Merkezdeki +q yüküne etki eden dış alan sıfırsa, o yüke net kuvvet uygulayan başka kaynak kalır mı?",
           "Dıştaki +Q yükü hangi yüklerle etkileşiyor: yalnız +q ile mi, yoksa kabuğun dış yüzeyindeki yüklerle de mi?",
           "İki yük arasında 'eşit ve zıt kuvvet' dediğimizde tam olarak hangi iki cisim kastediliyor?"],
          "Merkezdeki +q'ya dışarıdan net kuvvet gelmediğine göre iki yük arasında 'eşit ve zıt' bir kuvvet çifti yoktur. +Q'ya etki eden kuvvet ise +q'nun ve kabuk yüzeylerinin toplam "
          "alanından gelir; iç yük, kabuk ve dış yük birlikte ele alınmadan etki–tepki çifti kurulamaz.",
          "Kapalı metal bir odanın içindeki biri dışarıdaki bir topun itmesini hissetmez; topun etkisini odanın duvarları karşılar. İç yük ile dış yük arasına konan bu 'duvar', "
          "yüklerin doğrudan karşılıklı kuvvet uygulamasını engeller."),
       S("MBS22", "MAL01", "TB"), "HIGH"),

    MC("faraday-cage-works-with-insulator",
       "Faraday kafesi içindeki cisim, kafes yalıtkan malzemeden yapılmış olsa bile dış elektrik alandan korunur.",
       "Faraday kafesinin korumasını sağlayan, iletken malzemedeki serbest yüklerin dış alan karşısında hareket edip kafesin iç bölgesinde alanı sıfırlayacak biçimde yeniden dağılmasıdır. "
       "Yalıtkanda serbest yük olmadığı için bu yeniden dağılım olmaz; dış alan kafesin içine ulaşır. Koruma kapalı (veya yeterince sık örgülü) bir iletken yüzey gerektirir.",
       ["faraday-kafesi", "elektriksel-alan", "elektrik-yuku"], LO("2.3"), "CONCEPTUAL_ERROR",
       "fcage-verify-claims ailesinin 'kafes yalıtkan malzemeden de yapılabilir' ve 'kafesteki boşluklar büyüdükçe koruma artar' çeldiricileri. "
       "Ders kitabı (s. 181), korumayı iletkenlerin içinde alanın sıfır olmasıyla açıklar. Bu yanılgının görülme sıklığını ölçen bir akademik çalışma bulunamadı "
       "(Taşkın ve Ünlü Yavaş'ın iletkenler ve alan çizgileri çalışmasına yalnız künye düzeyinde erişildi, bu nedenle kaynak olarak kullanılmadı); "
       "iletken kabuk sorularındaki genel güçlük için bkz. Maries vd. (2022).",
       DI("Pozitif yüklü büyük bir cisim, içinde nötr ve hafif bir metal küre bulunan iki farklı kafese sırayla yaklaştırılıyor: I. kafes metal tel örgüden, II. kafes aynı biçimde örülmüş plastik tel örgüden yapılmıştır "
          "(kafesler iç kürenin hareketini kısıtlamıyor, kafesin kendisi de nötr). Metal kürenin davranışı için hangisi doğrudur?",
          "I'de küre pozitif cisme doğru çekilmez; II'de küre pozitif cisme doğru çekilir.",
          "İki durumda da küre hareketsiz kalır; çünkü koruma kafesin biçiminden gelir.",
          "I'de küre pozitif cisme doğru çekilir; II'de hareketsiz kalır.",
          "İki durumda da küre pozitif cisme doğru çekilir.",
          "I'de küre pozitif cisimden uzağa itilir; II'de pozitif cisme doğru çekilir.",
          "A", "B"),
       RM(["Dış alan iletken bir tel örgüye ulaşınca örgüdeki serbest yüklere ne olur?",
           "Plastikte hareket edebilen serbest yük var mı? O halde plastik örgü dış alana nasıl bir cevap verir?",
           "Nötr metal küreye dış alan nasıl etki eder: küreyi kutuplandırır mı? Kutuplanan küre pozitif cisme doğru mu uzağa mı gider?",
           "Kafesin içinde alan sıfır olduysa, kafesin içindeki küre neden hareketsiz kalır?"],
          "Plastik tel örgünün olduğu durumda nötr metal küre yakındaki pozitif cismin alanında kutuplanır ve ona doğru çekilir (nötr bir cismin yüklü bir cisim tarafından çekilmesi); "
          "bu, kafesin 'şekil'iyle korumanın sağlanamayacağını gösterir. Koruyan şey kafesin iletken olmasıdır.",
          "Bir bahçe çitinin tel örgüsü yağmuru kesmez, ama metal bir kutu yıldırımdan korur: önemli olan şeklin kendisi değil, yükleri serbestçe yeniden dağıtabilen iletken yapıdır."),
       S("TB", "MBS22"), "MEDIUM"),

    # --- FİZ.11.2.4: Mıknatıslar ve manyetik alan ---
    MC("magnet-poles-are-electric-charges",
       "Mıknatısın kutupları, uçlarında toplanmış pozitif ve negatif elektrik yükleridir; mıknatıs bir tür elektrik dipolüdür.",
       "Mıknatısın kutupları elektrik yükü taşıyan bölgeler değildir. Manyetik özellik, atomlardaki elektronların hareketinden (yörünge hareketi ve spin) doğan manyetik etkilerin düzenli hizalanmasından gelir. "
       "Kutuplar, manyetik alan çizgilerinin mıknatısın uçlarında yoğunlaştığı bölgelerdir. Durgun bir yük, durgun bir mıknatısın manyetik alanı tarafından itilmez ya da çekilmez.",
       ["miknatis", "manyetik-kutup", "manyetik-alan", "elektrik-yuku"], LO("2.4"), "CONCEPTUAL_ERROR",
       "magnet-pole-interaction ve magnet-field-lines-pattern ailelerinde kutup etkileşimini yük etkileşimine benzeten çeldiriciler. Voutsina ve Ravanis (2011): 15–17 yaşındaki 40 öğrenciyle "
       "yapılan görüşmelerde 10. sınıfta 20 öğrencinin 7'si, 11. sınıfta 20 öğrencinin 9'u manyetizmayı mıknatısın kutuplarındaki elektrik yüklerinin ayrışmasına bağladı (11. sınıf, konuyu yeni görmüş öğrenciler). "
       "Singh (2008): CSEM türü bir soruda (çubuk mıknatıs ve elektrik dipolü) son-test doğru oranı %41 (ön-test %38); görüşmelerde bazı öğrenciler çubuk mıknatısın uçlarında zıt yükler olduğunu savundu.",
       DI("Durgun, küçük, pozitif yüklü bir cisim bir çubuk mıknatısın N kutbuna yakın bir noktada durgun biçimde tutuluyor (başka cisim ya da alan yok). Cisme mıknatıs tarafından uygulanan net kuvvet için hangisi doğrudur?",
          "N kutbundan uzağa doğru bir itme kuvveti vardır; çünkü N kutbu pozitif yük gibi davranır.",
          "Net kuvvet yoktur; durgun yüke manyetik alan kuvvet uygulamaz ve mıknatısın kutupları elektrik yükü taşımaz.",
          "N kutbuna doğru bir çekme kuvveti vardır; çünkü zıt yükler birbirini çeker.",
          "Alan çizgilerine paralel bir kuvvet vardır.",
          "Alan çizgilerine dik ve sabit büyüklükte bir kuvvet vardır.",
          "B", "A"),
       RM(["Mıknatısın kutupları elektrik yükü olsaydı, bir tüyü ya da plastik bir tarağı yaklaştırdığımızda ne gözlerdik?",
           "Demir bir çiviyi mıknatısa yaklaştırınca çivi çekilir. Çivi yüklü mü? Yüksüz bir çivinin çekilmesi yükle açıklanabilir mi?",
           "Mıknatısın N ve S kutbunda zıt yükler olsaydı bunları nasıl ayırabilirdin? Mıknatısı ikiye kesince ne olduğunu düşün.",
           "Durgun bir yük ile mıknatıs arasında kuvvet gözleniyor mu?"],
          "Yüklü bir tarak mıknatısa yaklaştırıldığında mıknatıs tarafından hiçbir itme ya da çekme gözlenmez; yüksüz demir ise mıknatısa yapışır. "
          "Kutuplar elektrik yükü olsaydı bu gözlemin tersi beklenirdi.",
          "Pusulayı ve bir tüy parçasını aynı mıknatısın yanına koyduğumuzda pusula iğnesi döner, tüy kıpırdamaz; iki 'alan' farklı şeylere etki eder (manyetik alan manyetik maddelere ve hareketli yüklere, elektrik alan yüklere)."),
       S("VR11", "SIN08", "BG98"), "HIGH"),

    MC("cut-magnet-separates-poles",
       "Çubuk mıknatıs ortadan kesilirse N ve S kutupları birbirinden ayrılır; bir parça yalnız N, diğeri yalnız S kutbu taşır.",
       "Manyetik tek kutup yoktur: mıknatıs ortadan kesildiğinde her parçanın kendi N ve S kutbu oluşur; parçalar daha zayıf ama tam birer mıknatıs olur. "
       "Her iki kutup birlikte var olur, çünkü manyetik alan çizgileri kapalı eğrilerdir.",
       ["miknatis", "manyetik-kutup", "manyetik-alan-cizgileri"], LO("2.4"), "CONCEPTUAL_ERROR",
       "magnet-pole-interaction ailesinin 'mıknatısı ikiye kesersek N ve S ayrı iki tek kutuplu parça elde edilir' çeldiricisi. Voutsina ve Ravanis (2011) görüşmelerinde, mıknatısta iki ayrı madde olduğunu düşünen "
       "bir 11. sınıf öğrencisi kesilince 'her cins ayrılır' dedi; Singh (2008) ise tersine çoğu öğrencinin parçaların yine kutuplu olacağını söylediğini bildirir. Yanılgı azınlıkta ve örneklem çok küçüktür (güven orta).",
       DI("Bir çubuk mıknatıs, N ve S kutuplarının tam ortasından kesilerek iki parçaya ayrılıyor. Parçalar için hangisi doğrudur?",
          "Bir parça yalnız N kutbu taşır, diğeri yalnız S kutbu taşır.",
          "İki parça da manyetik özelliğini tamamen kaybeder.",
          "Her parçanın kendi N ve S kutbu vardır; iki parça da mıknatıs olarak davranır.",
          "Parçalardan biri mıknatıs olarak kalır, diğeri demir parçasına dönüşür.",
          "Kesim yüzeylerinde kutup oluşmaz; parçalar yalnız eski uçlarında kutup taşır.",
          "C", "A"),
       RM(["Bir parça yalnız N, diğeri yalnız S kutbu taşıyorsa ilk parçanın tüm alan çizgileri nereden çıkıp nereye gider?",
           "Kırılmış mıknatısın iki parçasını yan yana getirdiğinde nasıl davranırlar? İkisi de bir mıknatıs gibi çekiyor mu?",
           "Elektrik yükünde pozitifi ve negatifi ayırabiliyoruz: sürtünmeyle bir cisme (+), diğerine (−) yük aktarıyoruz. Mıknatıs için benzer bir şey yapabilir miyiz?",
           "Alan çizgileri kapalı eğriler ise bir kutbu diğerinden ayırmak mümkün olur mu?"],
          "Kırılmış bir mıknatısın her parçası küçük toplu iğneleri uçlarından çeker ve pusula iğnesini döndürür; hiçbir parçada yalnız N ya da yalnız S davranışı gözlenmez. "
          "Kutuplar ayrılsaydı yalnızca N ya da yalnızca S davranışı gösteren bir parça bulunurdu.",
          "Bir kâğıdı ikiye kestiğinde 'yalnız ön yüz' ve 'yalnız arka yüz' parçaları elde edemezsin; her parçanın yine iki yüzü olur. Mıknatıstaki N ve S kutupları da böyle birbirinden ayrılamaz."),
       S("VR11", "SIN08", "TB"), "MEDIUM"),

    MC("compass-needle-n-points-to-magnet-n",
       "Pusula iğnesinin N ucu, yakındaki çubuk mıknatısın N kutbuna doğru yönelir.",
       "Pusula iğnesi bulunduğu noktadaki bileşke manyetik alanın yönünde hizalanır; iğnenin N ucu alanın yönünü gösterir. Çubuk mıknatısın dışında alan çizgileri N kutbundan çıkıp S kutbuna girdiğinden, "
       "iğnenin N ucu mıknatısın S kutbuna doğru, S ucu ise N kutbuna doğru yönelir (zıt kutuplar birbirini çeker). Dünya'nın coğrafi kuzeyindeki kutup manyetik olarak S kutbu gibi davranır.",
       ["pusula", "manyetik-kutup", "manyetik-alan-cizgileri", "manyetik-alan"], LO("2.4"), "CONCEPTUAL_ERROR",
       "magnet-vector-compass-earth ailesinin 'pusulanın N ucu mıknatısın S kutbundan uzağı gösterir' çeldiricisi (pusula–alan yönü ilişkisini ters kurma); magnet-field-lines-pattern ailesinde "
       "çizgi yönünü ters bilme. Voutsina ve Ravanis (2011) literatür özeti, Bradamante ve Viennot'un (2007) bulgusunu aktarır: 9–11 yaşındaki çocuklar manyetik çizgi fikrini kolay kavrar ama "
       "pusula iğnelerinin dipol doğası nedeniyle yönünü belirlemekte güçlük çeker (ikincil aktarım; kayıt ders kitabıyla desteklenir).",
       DI("Yatay bir masada duran çubuk mıknatısın N kutbunun hemen yanına küçük bir pusula konuyor (Dünya'nın alanı ve diğer etkiler ihmal ediliyor). "
          "Pusula iğnesi hangi durumda dengede durur?",
          "İğnenin N ucu mıknatısın N kutbuna bakar.",
          "İğnenin S ucu mıknatısın N kutbuna bakar.",
          "İğne mıknatısın ekseninden dik bir yöne hizalanır.",
          "İğnenin yönü mıknatıs uzaklaştırıldıkça sürekli değişir; denge yoktur.",
          "İğnenin N ucu ile S ucu mıknatısın N kutbundan eşit uzaklıkta kalır ve iğne hareketsizdir.",
          "B", "A"),
       RM(["Çubuk mıknatısın dışındaki alan çizgileri hangi kutuptan çıkıp hangisine girer? Pusula iğnesi bu çizgilerin yönünü mü gösterir yoksa tersini mi?",
           "Zıt kutuplar birbirini çekiyorsa iğnenin hangi ucu mıknatısın N kutbuna yaklaşır?",
           "Pusulanın N ucu Dünya'da coğrafi kuzeyi gösteriyor. Dünya'nın kuzeydeki manyetik kutbu bir N mi bir S mi gibi davranıyor?",
           "Mıknatısı pusulanın yanında çevirdiğinde iğne hangi hareketi yapar? Bu hareket 'aynı kutuplar çeker' kuralını destekler mi?"],
          "Pusulanın N ucu Dünya'nın kuzeyini gösteriyorsa ve zıt kutuplar çekiyorsa, Dünya'nın kuzeyindeki manyetik kutup S kutbu gibi davranmalıdır. "
          "'N ucu N kutbuna bakar' kuralı doğru olsaydı pusula güneyi gösterirdi.",
          "İki mıknatısı uçlarından birleştirdiğinde N ile S yapışır, N ile N birbirini iter. Pusula iğnesi küçük bir mıknatıstır; N ucu başka bir N'ye bakmak yerine S'ye çekilir."),
       S("VR11", "TB"), "MEDIUM"),

    # --- FİZ.11.2.5: Akım geçen düz telin manyetik alanı ---
    MC("opposite-currents-midpoint-field-zero",
       "Zıt yönlü akım taşıyan iki paralel telin tam ortasında iki telin manyetik alanları birbirini götürür; bileşke manyetik alan sıfırdır.",
       "Zıt yönlü akımlarda iki telin ortasındaki alanlar aynı yönlüdür ve toplanır (bileşke, tek telin alanının iki katı). Alanların birbirini götürmesi için akımların aynı yönlü olması gerekir: "
       "iki özdeş paralel telin ortasındaki bileşke alan, akımlar aynı yönlüyse sıfırdır. Her telin alanı sağ el kuralıyla yönüyle birlikte belirlenip vektörel toplanmalıdır.",
       ["duz-telin-manyetik-alani", "sag-el-kurali", "manyetik-alan", "vektorel-nicelik"], LO("2.5"), "VECTOR_ERROR",
       "wire-field-superposition ailesinin bileşke alanı yönlere bakmadan hesaplayan çeldiricileri ve 'akımlar zıt yönlüyse ortada alan sıfırdır' tipi seçenekler. Singh (2008): zıt yönlü akım taşıyan iki telin "
       "ortasındaki alanı soran maddede son-test doğru oranı %39 (ön-test benzer); en yaygın yanlış yanıt 'alan sıfırdır' idi ve öğrenciler bunu iki eşit zıt yükün ortasındaki elektrik alanla özdeşleştirdi. "
       "Maries vd. (2022): iki halkanın ortasında alanın sıfır olduğunu söyleyenler hem giriş hem ileri düzeyde yaklaşık %26 (üniversite örneklemleri).",
       DI("Aynı düşey düzlemde, birbirine paralel iki uzun yatay tel yerleştirilmiş: üstteki K telinden sağa, alttaki L telinden sola doğru eşit şiddette akım geçiyor. "
          "Tellerin tam ortasındaki P noktasında iki telin manyetik alanının bileşkesi için hangisi doğrudur? (Düzlem, kâğıt düzlemi kabul edilir.)",
          "Sıfırdır; çünkü iki telin alanı birbirini götürür.",
          "Her telin alanının iki katı büyüklüğündedir ve kâğıt düzlemine dik, içeri doğrudur.",
          "Her telin alanının iki katı büyüklüğündedir ve kâğıt düzlemine dik, dışarı doğrudur.",
          "Bir telin alanı kadardır ve kâğıt düzlemine dik, içeri doğrudur.",
          "Tellere paralel ve sağa doğrudur.",
          "B", "A"),
       RM(["K telinin P noktasındaki alanı hangi yönde? Baş parmağını akım yönüne (sağa) çevirip dört parmağınla P'nin bulunduğu tarafı gösterirsen alan kâğıda mı girer, çıkar mı?",
           "L telinin P noktasındaki alanını aynı yöntemle bul: L'nin akımı sola, P ise L'nin üstünde.",
           "İki alan aynı yönlü mü, zıt yönlü mü? Büyüklükleri eşit olduğuna göre bileşke ne olur?",
           "Akımlardan birini ters çevirirsek P'deki bileşke alan ne olur?"],
          "Akımlardan birini ters çevirdiğimizde P'deki bileşke sıfır olur: alanlar birbirini ancak akımlar aynı yönlü olduğunda götürür. Zıt yönlü akımlarda 'götürür' diyen görüş bu denemeyle çelişir.",
          "İki kişi aynı sandığı iki yandan, biri iterek biri çekerek taşır: ikisi de sandığı aynı tarafa gönderir. Zıt akımlı iki telin ortasındaki alanlar da 'aynı tarafa' etki eder; bu yüzden toplanırlar."),
       S("SIN08", "MBS22", "KUS16"), "HIGH"),

    MC("wire-field-radial-or-along-wire",
       "Akım taşıyan düz telin manyetik alanı, elektrik alan gibi telden uzağa/tele doğru (radyal) ya da tel boyunca yönelir.",
       "Düz telin manyetik alan çizgileri, tele dik düzlemde ve telin çevresinde merkezdaş çemberlerdir; yön sağ el kuralıyla bulunur (baş parmak akım yönünde, dört parmak alanın dönüş yönünde). "
       "Alan telden uzağa ya da tele doğru değil, teğet doğrultudadır; çizgiler tele paralel de değildir. Bir pusula iğnesi telin yakınında tele doğru değil, yarıçapa dik yönde hizalanır.",
       ["duz-telin-manyetik-alani", "manyetik-alan-cizgileri", "sag-el-kurali", "oersted-deneyi"], LO("2.5"), "CONCEPTUAL_ERROR",
       "wire-field-direction-rhr ailesinin 'alan çizgileri tele paralel (telin boyunca) uzanır' çeldiricisi ve wire-field-data-model ailesindeki alan–tel ilişkisini elektrik alana benzeten seçenekler. "
       "Singh (2008): bazı manyetizma yanılgıları elektrostatikten kaynaklanan benzetmelerdir; Guisasola vd. (2004): öğrenciler manyetik alanın kaynağını belirlemekte ve manyetik kuvvet ile alanı ayırmakta güçlük çeker. "
       "Bu yanılgının akım taşıyan tel için görülme oranı ölçülmemiş; örneklemler üniversite düzeyindedir.",
       DI("Uzun, düz ve düşey bir telden yukarı doğru sabit akım geçiyor. Telin 5 cm yanında, aynı yükseklikte yatay bir düzleme küçük bir pusula konuyor "
          "(Dünya'nın alanı ve başka alanlar ihmal ediliyor). Pusula iğnesinin N ucu için hangisi doğrudur?",
          "Tele doğru (yarıçap doğrultusunda) yönelir.",
          "Yatay düzlemde, telden pusulaya çizilen doğruya dik bir doğrultuda yönelir.",
          "Tel ile aynı doğrultuda, yani düşey yönde yönelir.",
          "Telden uzağa doğru (yarıçap doğrultusunda) yönelir.",
          "Telin etrafında sürekli dönmeye devam eder.",
          "B", "A"),
       RM(["Ørsted deneyinde pusula iğnesi telin altında/üstünde nasıl dönüyordu: tele doğru mu, telden uzaklaşarak mı, tele paralel mi?",
           "Elektrik alan çizgileri yükten çıkıp (ya da yüke girip) uzaya yayılır. Manyetik alan çizgilerinin bir 'başlangıç noktası' var mı?",
           "Sağ el kuralında baş parmak akım yönünü gösterirken dört parmağın kıvrılışı sana alanın nasıl bir yol izlediğini anlatır mı?",
           "Telin çevresinde pusula iğnesini farklı noktalara koyarsan iğnelerin yönleri bir çember çizer mi?"],
          "Pusula iğnesi telin yanında tele doğru değil, ona dik yönde sapar; iğneleri telin çevresine çember boyunca dizersek uçları çembere teğet olur. "
          "Radyal ya da tele paralel bir alan olsaydı iğneler tele doğru ya da tele paralel dönerdi.",
          "Bir kuyunun etrafında dönen su girdabı gibi düşün: su kuyuya doğru ya da kuyudan uzağa değil, kuyunun çevresinde döner. Manyetik alan çizgileri de telin çevresinde 'dönen' çizgilerdir."),
       S("SIN08", "GAZ04", "TB"), "MEDIUM"),

    MC("wire-field-inverse-square-with-distance",
       "Düz telin manyetik alanı, noktasal yükün alanında olduğu gibi uzaklığın karesiyle ters orantılıdır: uzaklık iki katına çıkarsa alan dörtte birine iner.",
       "Sonsuz uzun düz telin manyetik alanı telden olan dik uzaklıkla ters orantılıdır (B ∝ 1/d): uzaklık iki katına çıkarsa alan yarıya iner. "
       "Noktasal yükün elektrik alanındaki ters kare ilişkisi (E ∝ 1/r²) bu geometride geçerli değildir; çünkü kaynak tek nokta değil, çizgisel bir akımdır.",
       ["duz-telin-manyetik-alani", "manyetik-alan", "oran-oranti", "ters-kare-iliskisi"], LO("2.5"), "FORMULA_SELECTION_ERROR",
       "wire-field-ratio ailesinin 'd iki katına çıkınca alan dörtte bire iner' çeldiricisi (düz tel için noktasal yük karışıklığı). Singh (2008) manyetizma yanılgılarının önemli bir kısmının elektrostatik "
       "benzetmelerinden kaynaklandığını bildirir; ancak bu çeldiricinin oranı için doğrudan bir ölçüm bulunamadı (güven orta; ders kitabının s. 198'de başlayan etkinliğiyle tutarlı).",
       DI("Uzun, düz bir telden sabit bir akım geçerken telden 4 cm uzaklıktaki bir noktada manyetik alan büyüklüğü B ölçülüyor. Aynı akımda telden 8 cm uzaklıktaki bir noktada "
          "manyetik alanın büyüklüğü kaç B olur?",
          "B/4",
          "B/2",
          "2B",
          "B",
          "4B",
          "B", "A"),
       RM(["Noktasal bir yük ile uzun düz bir tel aynı türden 'kaynak' mıdır? Birinin şekli nokta, diğerinin çizgi ise alanın uzaklığa bağlılığı da aynı olmak zorunda mı?",
           "Noktasal yükün çevresinde alan her yöne yayılır; düz telin çevresinde ise alan telin boyunca eşit dağılmıştır. Hangi durumda alan uzaklıkla daha yavaş azalır?",
           "Telden 4 cm'den 8 cm'e geçerken uzaklık kaç katına çıktı? Düz tel için alan hangi kuvvetle azalır?",
           "Ders kitabındaki deney verisini (alan–uzaklık tablosu) yan yana koyduğunda alan ile d'nin çarpımı sabit mi çıkıyor, alan ile d²'nin çarpımı mı?"],
          "Deneysel B–d verisinde B·d çarpımı sabit kalıyorsa B ∝ 1/d'dir; B·d² sabit kalmıyorsa ters kare değildir. Veri tablosundaki oran, ters kareden beklenen 1/4 yerine 1/2 çıkar.",
          "Işık noktasal bir lambadan her yöne yayıldığı için şiddeti 1/r² ile azalır; çok uzun bir floresan tüpün yanında ise ışık şiddeti uzaklıkla daha yavaş (yaklaşık 1/d ile) azalır. "
          "Kaynağın biçimi (nokta ya da uzun çizgi), uzaklık bağımlılığını belirler."),
       S("SIN08", "TB"), "MEDIUM"),

    # --- FİZ.11.2.6–FİZ.11.2.7: Akım makarası ve elektromıknatıs ---
    MC("solenoid-field-depends-on-radius",
       "Akım makarasının merkez eksenindeki manyetik alan, makaranın yarıçapı büyüdükçe azalır (yarıçapa bağlıdır).",
       "Uzunluğu yarıçapına göre çok büyük, sık sarılmış ideal bir akım makarasında iç bölgedeki alan düzgündür ve B = 4πK·i·N/L ile verilir: akıma, birim uzunluktaki sarım sayısına ve ortama bağlıdır; "
       "makaranın yarıçapına bağlı değildir. Tek bir çembersel halkanın merkezindeki alanın yarıçapla azalması, ideal makara için geçerli değildir.",
       ["akim-makarasi", "manyetik-alan", "sarim-sayisi", "manyetik-alan-katsayisi"], LO("2.6"), "FORMULA_SELECTION_ERROR",
       "solenoid-ratio-generalization ailesinin 'yarıçap artınca merkez eksenindeki alan azalır' çeldiricisi ve solenoid-data-model ailesindeki bağlı değişkenleri yanlış sayan seçenekler. "
       "Ders kitabı (s. 210) ideal makarada alanın yalnız i, N, L ve K'ye bağlı olduğunu verir. Bu yanılgının görülme sıklığını ölçen bir çalışma bulunamadı; tek halka formülünün makaraya aktarılması "
       "olası bir kaynak olarak değerlendirilmiştir (güven orta).",
       DI("Aynı telden, aynı sarım sayısıyla (N) ve aynı uzunlukta (L) sarılmış, ancak yarıçapları r ve 2r olan iki ideal akım makarasından eşit şiddette akım geçiriliyor (uzunluklar yarıçaplara göre çok büyüktür). "
          "Makaraların merkez eksenindeki alan büyüklükleri B₁ (r yarıçaplı) ve B₂ (2r yarıçaplı) için hangisi doğrudur?",
          "B₂ = B₁/2; çünkü yarıçap büyüdükçe alan azalır.",
          "B₂ = B₁; çünkü ideal makarada alan yarıçapa bağlı değildir.",
          "B₂ = 2B₁; çünkü makara büyüdükçe daha fazla tel alan oluşturur.",
          "B₂ = B₁/4; çünkü alan yarıçapın karesiyle ters orantılıdır.",
          "B₂ = 4B₁; çünkü alan yarıçapın karesiyle orantılıdır.",
          "B", "A"),
       RM(["Ders kitabındaki B = 4πK·i·N/L bağıntısında yarıçap geçiyor mu?",
           "N, L ve i değişmedikçe makarayı 'şişirirsek' birim uzunluktaki sarım sayısı değişir mi?",
           "Tek bir halkanın merkezindeki alan ile uzun bir makaranın içindeki alan neden aynı bağımlılığı göstermez? Kaynak sayısı (halka sayısı) neden önemli?",
           "İdeal makarada iç alan 'her noktada aynı' ise merkezi eksene yakın ya da uzak noktalar arasında fark olur mu?"],
          "Aynı N, L ve i ile yarıçap 2 katına çıkarıldığında makaranın birim uzunluğundaki sarım sayısı aynı kalır; yani her bir parça uzunluk için aynı akım halkaları vardır. "
          "İç bölgedeki bileşke alanı bu halkaların toplamı belirlediğinden alan değişmez. Alan yarıçapa bağlı olsaydı, düzgün iç alan fikri de ideal makarayı tanımlayamazdı.",
          "Bir yolun her metresine aynı sıklıkta lamba dizildiğinde yolu genişletsek de 'metre başına lamba' değişmez. İdeal makarada iç alanı belirleyen de metre başına düşen akım halkası sayısıdır "
          "(benzetme yalnız bu bağımlılığı vurgular)."),
       S("TB"), "MEDIUM"),

    MC("solenoid-field-depends-on-turns-not-turns-per-length",
       "Aynı akımda, sarım sayısı arttıkça akım makarasının merkez eksenindeki manyetik alan da artar; alan yalnız toplam sarım sayısına (N) bağlıdır.",
       "İdeal akım makarasının alanı B = 4πK·i·N/L ile verildiğinden, alanı belirleyen birim uzunluktaki sarım sayısıdır (N/L). Sarım sayısı iki katına çıkarken makara boyu da iki katına çıkarsa alan değişmez; "
       "makara boyu sabit kalırken sarım sayısı iki katına çıkarsa alan iki katına çıkar.",
       ["akim-makarasi", "sarim-sayisi", "manyetik-alan", "oran-oranti"], LO("2.6"), "FORMULA_APPLICATION_ERROR",
       "solenoid-data-model ailesinin 'B yalnız akıma bağlıdır' ve solenoid-ratio-generalization ailesinin 'L artınca N sabitken B artar' çeldiricileri; ders kitabı etkinliğinde (s. 211) 4. düzenekte "
       "sarım sayısı 2N ve uzunluk 2L'dir ve alan birinci düzenekle aynıdır. Bu yanılgının oranı için akademik ölçüm bulunamadı (güven orta).",
       DI("Aynı telden, aynı akımla çalışan üç ideal akım makarası şöyle sarılıyor: I. makara N sarım ve L uzunluk; II. makara 2N sarım ve 2L uzunluk; III. makara 2N sarım ve L uzunluk. "
          "Merkez eksenlerindeki manyetik alan büyüklükleri B_I, B_II, B_III için hangisi doğrudur?",
          "B_I = B_II < B_III",
          "B_I < B_II = B_III",
          "B_I < B_II < B_III",
          "B_I = B_II = B_III",
          "B_II < B_I < B_III",
          "A", "B"),
       RM(["Alanı toplam sarım sayısı mı, yoksa birim uzunluğa düşen sarım sayısı mı belirliyor? Bağıntıda hangi oran görünüyor?",
           "II. makarada hem sarım sayısı hem boy iki katına çıktı. Birim uzunluktaki sarım sayısı değişti mi?",
           "III. makarada aynı boya iki kat sarım sığdırmak için sarımlar sıklaşır mı? Bu alanı nasıl etkiler?",
           "Makarayı iki katına uzatıp tele yeni sarımlar eklemeden bırakırsak alan nasıl değişir?"],
          "II. makara I. makaranın iki özdeş kopyasının uç uca eklenmesiyle elde edilir; birim uzunluktaki sarım aynıdır ve iç alan, ortada bir noktada aynı kalır. "
          "Alan yalnız toplam sarım sayısına bağlı olsaydı uzun makara kısa makaradan daha güçlü olmak zorunda kalırdı.",
          "Bir duvara dizilmiş lambaların sayısını iki katına çıkarıp duvarı da iki katına uzatırsan duvar boyunca aydınlık yoğunluğu değişmez. Makarada da alanı belirleyen 'sarım yoğunluğu' (N/L)'dir."),
       S("TB"), "MEDIUM"),

    MC("any-metal-core-strengthens-coil-field",
       "Akım makarasının içine herhangi bir metal çubuk (bakır, alüminyum gibi) konulursa makaranın manyetik alanı belirgin biçimde artar.",
       "Akım makarasının manyetik alanını belirgin biçimde artıran, demir, nikel, kobalt gibi ferromanyetik maddelerdir: bu maddeler makaranın alanında mıknatıslanıp kendi alanlarını ekler "
       "(elektromıknatıs). Bakır ve alüminyum gibi ferromanyetik olmayan metaller, iletken olsalar da alanı belirgin biçimde artırmaz.",
       ["akim-makarasi", "elektromiknatis", "manyetik-alan", "miknatis"], LO("2.6", "2.7"), "CONCEPTUAL_ERROR",
       "emag-verify-and-apply ailesinin 'çekirdek olarak bakır kullanılırsa alan çok artar' ve emag-record-information ailesinin çekirdek malzemesi çeldiricileri; "
       "magnet-pole-interaction ailesinde 'mıknatıslar arasına her cisim konulsa etkileşim aynı kalır' tipi seçenekler. Ders kitabı (s. 210) çekirdek olarak demir, nikel, kobalt'ı anar. "
       "Bu yanılgının oranı ölçen akademik bir çalışma bulunamadı (güven orta).",
       DI("Aynı akımla çalışan, özdeş üç akım makarasının içi sırasıyla boş bırakılıyor, bakır çubukla dolduruluyor ve yumuşak demir çubukla dolduruluyor. "
          "Makaraların uçlarına yaklaştırılan küçük çivilerden yapışan çivi sayısı sırasıyla n₁ (boş), n₂ (bakır), n₃ (demir) ise hangisi doğrudur?",
          "n₁ < n₂ < n₃; bakır da demir gibi alanı artırır ama daha az.",
          "n₁ ≈ n₂ < n₃; yalnız demir çekirdek alanı belirgin biçimde artırır.",
          "n₂ < n₁ < n₃; bakır çekirdek alanı azaltır.",
          "n₁ = n₂ = n₃; çekirdek malzemesi alanı etkilemez.",
          "n₃ < n₁ ≈ n₂; demir çekirdek alanı zayıflatır.",
          "B", "A"),
       RM(["Bir mıknatıs bakır bir paraya yapışır mı? Demir bir çiviye yapışır mı?",
           "Makaranın alanı içindeki demir çubuğu mıknatıslar mı? Mıknatıslanan çubuk makaranın alanına ne ekler?",
           "Bakır iyi bir iletken olduğuna göre iletken olmak mıknatıslanabilmek için yeterli mi?",
           "Çekirdek olarak demir yerine nikel ya da kobalt kullanırsak ne beklersin?"],
          "Mıknatıs bakır paraya yapışmaz ama demir çiviye yapışır; yani bakır, demir gibi mıknatıslanmaz. Mıknatıslanma özelliği olmayan çekirdek, makaranın alanına bir katkı ekleyemez.",
          "Rüzgârın önüne yelken (demir çekirdek) koyarsan tekne hızlanır, ama koyduğun düz bir tahta (bakır çekirdek) rüzgârı tekneye 'katkı' olarak çevirmez. Çekirdeğin makaranın alanını yönlendirmesi için mıknatıslanabilir olması gerekir."),
       S("TB"), "MEDIUM"),

    MC("electromagnet-keeps-magnetism-after-current-off",
       "Elektromıknatıs, devreden geçen akım kesildikten sonra da mıknatıslığını korur; demir çekirdek kalıcı bir mıknatıs olur.",
       "Elektromıknatıs, akım geçtiği sürece güçlü bir mıknatıstır. Çekirdek yumuşak demir ise akım kesilince manyetik özelliğinin büyük bölümünü kaybeder (geçici mıknatıs). "
       "Bu özellik, hurda vincinde yükü akımı keserek bırakmayı ve elektromıknatısın açılıp kapanabilir bir mıknatıs olarak kullanılmasını sağlar.",
       ["elektromiknatis", "akim-makarasi", "manyetik-alan", "miknatis"], LO("2.7"), "CONCEPTUAL_ERROR",
       "emag-verify-and-apply ailesinin 'elektromıknatıs akım kesilince de mıknatıslığını korur' çeldiricisi. Ders kitabı (s. 210–213) elektromıknatısı akım makarasının demir çekirdeği mıknatıslaması olarak anlatır ve "
       "vinç gibi kullanım alanlarını verir. Bu yanılgının görülme sıklığını ölçen bir akademik çalışma bulunamadı; kayıt soru ailesinin çeldirici tasarımına ve ders kitabına dayanır (güven orta).",
       DI("Bir hurdalıkta, yumuşak demir çekirdekli büyük bir elektromıknatıslı vinç demir hurdaları kaldırıp taşıyor. Hurdayı bırakmak için vinç operatörü devredeki anahtarı açıyor. "
          "Anahtar açıldığı anda olanlar için hangisi doğrudur?",
          "Çekirdek mıknatıslığını korur; hurda yerinde kalır.",
          "Elektromıknatısın manyetik alanı büyük ölçüde kaybolur; hurda düşer.",
          "Elektromıknatıs hurdayı daha da kuvvetle çeker; çünkü devre açılmıştır.",
          "Kutuplar yer değiştirir ve hurda itilir.",
          "Anahtarın açılması etkisizdir; hurda yalnız akımın yönü ters çevrilince düşer.",
          "B", "A"),
       RM(["Elektromıknatısın alanını oluşturan şey nedir: yalnız demir çekirdek mi, makaradan geçen akım mı?",
           "Akım kesildiğinde makaranın kendi alanına ne olur?",
           "Hurda vinci yükü bırakamıyor olsaydı bu cihaz hurdalıkta işe yarar mıydı?",
           "Kalıcı mıknatıs ile elektromıknatıs arasındaki en önemli fark nedir?"],
          "Eğer çekirdek akım kesilince de mıknatıs kalsaydı, vinç yükü bırakmak için başka yöntem gerektirirdi; oysa vinç yalnız anahtarı açarak hurdayı bırakır. "
          "Bu gözlem elektromıknatısın geçici mıknatıs olduğunu gösterir.",
          "Bir ışık düğmesi gibi düşün: düğme kapanınca ışık söner. Elektromıknatısta anahtar da 'alanın düğmesi'dir; kalıcı mıknatıs ise düğmesiz sürekli yanan bir lamba gibidir."),
       S("TB"), "MEDIUM"),

    MC("reversing-current-makes-electromagnet-release",
       "Elektromıknatıstan geçen akımın yönü ters çevrilirse mıknatıs demir cisimleri çekmez, iter (bırakır).",
       "Akımın yönünü ters çevirmek elektromıknatısın kutuplarını yer değiştirir (N ucu S, S ucu N olur) ama demir gibi mıknatıslanabilen cisimler her iki kutba da çekilir: "
       "çekim kuvvetinin büyüklüğü aynı kalır. Cismi bırakmak için akımın yönü değil, akımın kendisi kesilmelidir (ya da şiddeti çok azaltılmalıdır).",
       ["elektromiknatis", "akim-makarasi", "manyetik-kutup", "sag-el-kurali"], LO("2.7"), "CONCEPTUAL_ERROR",
       "emag-verify-and-apply ailesinin 'vinç, akım ters çevrilince hurdayı bırakır' çeldiricisi (akım yönü ile akım büyüklüğünü karıştırma). Yanılgı, zıt kutupların çektiği, aynı kutupların ittiği (kalıcı mıknatıs) "
       "deneyiminin demir gibi mıknatıslanabilen cisimlere de uygulanmasından doğabilir. Bu yanılgının oranını ölçen akademik çalışma bulunamadı; kayıt soru ailesi ve ders kitabına (s. 213) dayanır (güven orta).",
       DI("Yumuşak demir çekirdekli bir elektromıknatısın ucuna yapışmış demir bir raptiye duruyor. Pilin bağlantı uçları ters çevrilerek akımın yönü değiştiriliyor (akımın şiddeti aynı kalıyor). "
          "Raptiye için hangisi doğrudur?",
          "Raptiye elektromıknatıstan itilir ve düşer.",
          "Raptiye yapışık kalmaya devam eder; çekim kuvvetinin büyüklüğü aynıdır.",
          "Raptiye elektromıknatısın diğer ucuna geçer.",
          "Raptiye daha büyük bir kuvvetle çekilir.",
          "Raptiye sürekli salınır.",
          "B", "A"),
       RM(["Raptiye (yumuşak demir) kalıcı bir mıknatıs mıdır, yoksa mıknatıslanabilen yüksüz bir cisim mi?",
           "Elektromıknatısın N ucu raptiyeyi çekerken raptiyenin hangi ucunu mıknatıslar? Elektromıknatısın S ucu olsaydı raptiyenin uçları nasıl değişirdi?",
           "Elektromıknatıs ve raptiye arasındaki kuvvet akımın yönüne mi, yoksa yalnız alanın büyüklüğüne mi bağlı?",
           "Raptiye bırakılmak istenirse hangisi etkili olur: akımı ters çevirmek mi, kesmek mi?"],
          "Elektromıknatısın N ucu raptiyenin yakın ucunu S yapar ve çeker; S ucu olsaydı yakın ucu N yapar ve yine çeker. Hangi kutup olursa olsun mıknatıslanabilen raptiye çekilir; "
          "ters akımda raptiye düşseydi, yumuşak demirin hiçbir kutba yapışması mümkün olmazdı.",
          "Metal bir bilya hem N hem S kutuplu çubuk mıknatısın uçlarına yapışır; mıknatısı çevirdiğinde bilya düşmez. Elektromıknatısta akımı ters çevirmek, mıknatısı çevirmek gibidir."),
       S("TB"), "MEDIUM"),

    # --- FİZ.11.2.8: Manyetik alanda akım geçen tele etki eden kuvvet ---
    MC("same-direction-currents-repel",
       "Aynı yönlü akım taşıyan paralel teller (aynı cins yükler gibi) birbirini iter; zıt yönlü akımlı teller birbirini çeker.",
       "Paralel akım taşıyan teller arasındaki kuvvet, yüklerin kuvvetinin tersi biçimde davranır: aynı yönlü akımlar birbirini çeker, zıt yönlü akımlar birbirini iter. "
       "Bunu bir telin diğer tel konumunda oluşturduğu manyetik alanı sağ el kuralıyla bulup, o alandaki akımlı tele etki eden kuvvetin yönünü yine sağ el kuralıyla belirleyerek göstermek gerekir; "
       "kuvvetler her zaman eşit büyüklükte ve zıt yönlüdür.",
       ["tele-etki-eden-manyetik-kuvvet", "duz-telin-manyetik-alani", "sag-el-kurali", "manyetik-kuvvet"], LO("2.8"), "CONCEPTUAL_ERROR",
       "parallel-wires-force ailesinin 'aynı yönlü akımlı teller birbirini iter' çeldiricisi. Maries vd. (2022): CSEM Q24'te (akımları aynı yönlü iki tel) ileri düzey lisans öğrencilerinin yaklaşık %32'si tellerin "
       "birbirini ittiğini seçti; yazılı gerekçeler bu sonucun ezberlenmiş bir kuralın yanlış hatırlanmasından ve telleri 'aynı cins yük' gibi görmekten geldiğini gösterir. "
       "Singh (2008): zıt yönlü akımlarda teller 'zıtlar çeker' benzetmesiyle birbirini çeker diye düşünüldü; öğrencilerin hiçbiri bu tahminini deneyle uzlaştıramadı.",
       DI("Düşey ve birbirine paralel iki uzun telden sol telde yukarı doğru i, sağ telde yukarı doğru 2i akımı geçiyor. Sol telin sağ tele uyguladığı kuvvet F₁, "
          "sağ telin sol tele uyguladığı kuvvet F₂ ile gösterilirse hangisi doğrudur?",
          "Teller birbirini iter; F₂ = 2F₁.",
          "Teller birbirini çeker; F₁ = F₂.",
          "Teller birbirini çeker; F₂ = 2F₁.",
          "Teller birbirini iter; F₁ = F₂.",
          "Teller arasında kuvvet yoktur; çünkü yalnız hareketli yükler birbirini etkiler.",
          "B", "D"),
       RM(["Sol telin sağ telin bulunduğu yerde oluşturduğu manyetik alan hangi yönde? (Sağ el kuralı)",
           "Bu alan içinde yukarı akım taşıyan sağ tele etkiyen kuvvet hangi yönde? (Sağ el kuralı)",
           "Sağ telin sol tele uyguladığı kuvvetin yönü bu kuvvetin tersi mi oluyor?",
           "Akım yönlerinden birini ters çevirirsek kuvvetin yönüne ne olur?"],
          "Tellerin akımlarını aynı yöne ayarlayıp laboratuvarda gözlediğimizde (örneğin iki ince alüminyum şerit) teller birbirine doğru yaklaşır; birbirinden uzaklaşmaz. "
          "Bu gözlem 'aynı yön = aynı cins yük = itme' düşüncesiyle çelişir.",
          "Burada işe yarayan bir günlük benzetme yoktur; yüklerdeki 'aynılar iter' sezgisi tam tersi sonuç verir. Kuralı ezberlemek yerine her seferinde iki sağ el kuralıyla türetmek gerekir."),
       S("MBS22", "SIN08", "KUS16"), "HIGH"),

    MC("magnetic-force-along-field-direction",
       "Manyetik alanda bulunan akım taşıyan tele etki eden kuvvet, manyetik alan yönündedir (elektrik alandaki yük gibi alan çizgisi boyunca).",
       "Manyetik kuvvet hem manyetik alana hem de akım yönüne diktir (F = i·L·B·sinθ, yönü sağ el kuralıyla bulunur). Elektrik alandaki yüke etkiyen kuvvet alan doğrultusundadır, "
       "ama manyetik alan akım taşıyan tele alan doğrultusunda kuvvet uygulamaz.",
       ["tele-etki-eden-manyetik-kuvvet", "manyetik-alan", "sag-el-kurali", "manyetik-kuvvet"], LO("2.8"), "CONCEPTUAL_ERROR",
       "wire-force-direction-rhr ailesinin 'kuvvet, alan yönündedir' çeldiricisi. Singh (2008): manyetik alana ters yönde giren yüklü parçacık sorusunda en yaygın yanlış yanıt 'parçacık yavaşlar' idi; "
       "öğrenciler kuvvetin alan yönünde (hıza zıt) olduğunu varsaydı. Aynı çalışmanın özeti, öğrencilerin manyetik kuvvet ile alanın birbirine dik olduğu fikriyle gösterilen deney karşısında, "
       "denklemden anlatılmasına göre daha büyük güçlük yaşadığını bildirir (üniversite öğrencileri; yük örneği, tel için de benzer yapıdadır).",
       DI("Doğu-batı doğrultusunda yatay duran uzun düz bir telden doğuya doğru akım geçiyor. Tel, düşey yukarı yönlü düzgün bir manyetik alanın içindedir. "
          "Tele etki eden manyetik kuvvetin yönü için hangisi doğrudur? (Kuzey–doğu–yukarı doğrultuları sağ el koordinat sistemi oluşturur.)",
          "Yukarı; çünkü kuvvet alan yönündedir.",
          "Güney; çünkü kuvvet hem akıma hem alana diktir.",
          "Kuzey; çünkü kuvvet hem akıma hem alana diktir.",
          "Doğu; çünkü kuvvet akım yönündedir.",
          "Aşağı; çünkü kuvvet alanın tersi yöndedir.",
          "B", "A"),
       RM(["Sağ el kuralında dört parmağını akım yönünde (doğu) uzatıp, alan yönüne (yukarı) doğru kıvırdığında baş parmağın nereyi gösteriyor?",
           "Tele etki eden kuvvet alanla aynı doğrultuda olsaydı, akımın yönünü ters çevirince kuvvetin yönü nasıl değişirdi?",
           "Bir elektrik alanda +q yüke etkiyen kuvvetle manyetik alanda akımlı tele etkiyen kuvveti karşılaştır: ikisinin alanla ilişkisi aynı mı?",
           "Telin üzerindeki kuvvet alan yönündeyse, alan çizgileri boyunca hareket eden bir parçacık için ne öngörürsün? Deneyde bu gözlenir mi?"],
          "Güçlü bir mıknatısı bir elektron demetinin tam önüne alan çizgileri demete paralel olacak biçimde yaklaştırdığımızda demetin hemen hiç sapmadığı gözlenir; kuvvet alan yönünde olsaydı demet ya yavaşlar ya hızlanırdı. "
          "Telde de benzer olarak kuvvet alan yönünde ortaya çıkmaz.",
          "Bir kapıyı itmeye çalışırken kuvvetinin doğrultusu kapının menteşelerinden geçen eksene değil, kapı yüzeyine diktir. Manyetik kuvvet de 'bir yüzeyi iter' gibi: alan ve akımın oluşturduğu düzleme diktir."),
       S("SIN08", "MBS22", "KUS16"), "HIGH"),

    MC("wire-parallel-to-field-feels-maximum-force",
       "Akım taşıyan tel manyetik alana paralel olduğunda üzerine etki eden manyetik kuvvet en büyüktür (ya da sıfırdan farklıdır).",
       "Manyetik kuvvetin büyüklüğü F = i·L·B·sinθ ile verilir; θ, akım yönü ile manyetik alan arasındaki açıdır. Tel alana paralel (θ = 0°) iken kuvvet sıfırdır, "
       "alana dik (θ = 90°) iken kuvvet en büyüktür. Alan çizgileri boyunca hareket eden ya da akan yüklere manyetik kuvvet etki etmez.",
       ["tele-etki-eden-manyetik-kuvvet", "manyetik-alan", "manyetik-kuvvet", "trigonometrik-oranlar"], LO("2.8"), "FORMULA_APPLICATION_ERROR",
       "wire-force-data-model ailesinin 'Tel B'ye paralel iken F en büyüktür' ve wire-force-magnitude-angle ailesinin 'paralel iken kuvvet en büyüktür' / '30°'de cos30° ile orantılıdır' çeldiricileri. "
       "Singh (2008): manyetik alana paralel hareket eden yüklü parçacık maddesinde (Q4) öğrencilerin önemli bir bölümü kuvvetin sıfır olmadığını, parçacığın yavaşlayacağını ya da bükülmesi gerektiğini düşündü; "
       "bu, tel için de benzer 'paralel = kuvvet var' yanılgısına zemin hazırlar (kaynaktaki örnek yüklü parçacıktır, tel değil). Ayrıca bazı öğrenciler, alana paralel gelen elektronun 'alandan kaçmak için' büküldüğünü söyledi.",
       DI("Uzunluğu L olan düz bir telden i akımı geçerken tel, B büyüklüğündeki düzgün bir manyetik alanda üç farklı konumdan geçiriliyor: telin alanla yaptığı açı sırasıyla 0°, 30° ve 90°. "
          "Tele etki eden manyetik kuvvet büyüklükleri F₀, F₃₀ ve F₉₀ için hangisi doğrudur?",
          "F₀ > F₃₀ > F₉₀",
          "F₀ = 0 < F₃₀ < F₉₀",
          "F₀ = F₃₀ = F₉₀",
          "F₀ < F₃₀ = F₉₀",
          "F₃₀ < F₀ < F₉₀",
          "B", "A"),
       RM(["Manyetik kuvvet ifadesindeki sinθ, telin alana paralel olduğu durumda (θ = 0°) kaç değerini alır?",
           "Alan çizgisi boyunca giden bir elektron demeti için kuvvet var mıdır? Deneyde demetin sapıp sapmadığını düşün.",
           "Kuvvetin yönü hem akıma hem alana dik ise akım ile alan aynı doğrultudayken dik olabilecek bir 'ortak dik' yön var mıdır?",
           "Tel alana dik konuma gelirse ne olur: kuvvet artar mı, azalır mı?"],
          "Alana paralel akıma sahip bir telin kuvvetinin sıfır olmaması durumunda, sağ el kuralıyla kuvvetin yönünü belirleyemezdik: akım ile alan aynı doğrultuda iken dik bir 'ortak dik' sonsuz sayıda olurdu ve kuvvetin yönü belirsiz kalırdı. "
          "Bu belirsizlik, kuvvetin sıfır olduğunu gösterir.",
          "Bir kapıyı menteşe eksenine paralel (kapı düzleminde) itmek kapıyı döndürmez; kuvvet dik uygulandığında döndürme en büyüktür. Manyetik kuvvet de 'dik uygulandığında' en büyük olan bir etkidir."),
       S("SIN08", "TB"), "MEDIUM"),

    # --- FİZ.11.2.9: Elektrik motoru ---
    MC("zero-net-force-means-no-rotation-of-loop",
       "Akım taşıyan çerçevenin zıt kenarlarına eşit büyüklükte, zıt yönlü kuvvetler etki ettiğinden bileşke kuvvet sıfırdır; bu yüzden çerçeve dönmez.",
       "Zıt kenarlara etki eden kuvvetler eşit büyüklükte ve zıt yönlü olduğundan bileşke kuvvet sıfırdır ve çerçeve ötelenmez; ama bu kuvvetler aynı doğru üzerinde değildir (bir kuvvet çifti oluşturur) "
       "ve çerçeveyi eksen etrafında döndüren bir tork meydana getirir. Dönme etkisi çerçeve düzlemi manyetik alana paralel iken en büyük, dik iken sıfırdır.",
       ["elektrik-motoru", "tele-etki-eden-manyetik-kuvvet", "bileske-kuvvet", "manyetik-kuvvet"], LO("2.9"), "CONCEPTUAL_ERROR",
       "loop-rotation-torque ailesinin 'bileşke kuvvet sıfır olduğundan çerçeve dönmez' çeldiricisi ve loop-force-directions ailesinin 'bileşke kuvvet büyük, bu yüzden öteleme yapar' çeldiricisi. "
       "Ders kitabı (s. 232) zıt kenarlardaki kuvvetlerin çerçeveyi 'aynı yönde döndürme etkisi' oluşturduğunu anlatır. Bu yanılgının oranı için ölçüm bulunamadı; "
       "kuvvet–hareket ilişkisine dair genel bir yanılgının (net kuvvet sıfırsa her tür hareket yoktur) dönme hareketine uygulanması olduğu varsayımı bir çıkarımdır (güven orta).",
       DI("Düzgün bir manyetik alanda, düzlemi alana paralel olan, üzerinden akım geçen dikdörtgen bir tel çerçeve iki karşılıklı kenarının ortasından geçen bir eksen etrafında serbestçe dönebilmektedir. "
          "Alana dik olan karşılıklı iki kenara eşit büyüklükte ve zıt yönlü manyetik kuvvetler etki ettiğine göre çerçevenin ilk andaki davranışı için hangisi doğrudur?",
          "Bileşke kuvvet sıfır olduğundan çerçeve hareketsiz kalır.",
          "Bileşke kuvvet sıfır olsa da kuvvetler farklı doğrular üzerinde olduğundan çerçeve eksen etrafında dönmeye başlar.",
          "Bileşke kuvvet sıfır olmadığından çerçeve alan yönünde ilerler.",
          "Kuvvetler eşit olduğundan çerçeve eksen etrafında sürekli aynı yönde salınır.",
          "Çerçeve dönmez ama zıt kuvvetler yüzünden uzaması (gerilmesi) beklenir.",
          "B", "A"),
       RM(["İki kuvvet eşit ve zıt ise bileşke kuvvet nedir? Bileşke kuvvetin sıfır olması cismin dönmeyeceğini mi söyler?",
           "Kapının kenarına menteşe tarafında bir kuvvet, açılan kenarında zıt yönde eşit bir kuvvet uygularsan kapı döner mi?",
           "Direksiyonu iki elinle zıt yönlerde eşit kuvvetle çevirdiğinde direksiyon hareket eder mi, araba öteleme yapar mı?",
           "Çerçevenin zıt kenarlarındaki kuvvetler aynı doğru üzerinde mi, farklı doğrular üzerinde mi?"],
          "Direksiyonu iki elinle zıt yönlerde eşit büyüklükte kuvvetle ittiğinde bileşke kuvvet sıfırdır ama direksiyon döner. 'Bileşke sıfır, o halde dönmez' düşüncesi bu gözlemi açıklayamaz.",
          "Bir tornavidayı döndürürken parmaklarınla iki zıt yönde eşit kuvvet uygularsın; tornavida ilerlemez (bileşke sıfır) ama döner. Çerçevedeki iki kenara etki eden kuvvet çifti de aynı işi yapar."),
       S("TB"), "MEDIUM"),

    MC("motor-converts-mechanical-to-electrical",
       "Elektrik motoru mekanik enerjiyi elektrik enerjisine dönüştürür.",
       "Elektrik motoru, manyetik alandaki akımlı çerçeveye etki eden kuvvet çiftiyle elektrik enerjisini dönme (mekanik) enerjisine dönüştürür; bir kısmı ısıya dönüşür. "
       "Mekanik enerjiyi elektrik enerjisine çeviren aygıt jeneratördür (indüksiyonla çalışır).",
       ["elektrik-motoru", "enerji-donusumu", "jenerator", "tele-etki-eden-manyetik-kuvvet"], LO("2.9"), "CONCEPTUAL_ERROR",
       "motor-principle-evaluation ailesinin 'elektrik motoru mekanik enerjiyi elektrik enerjisine dönüştürür' çeldiricisi (motor ve jeneratörün enerji dönüşüm yönünü karıştırma). "
       "Ders kitabı (s. 232) 'basit bir elektrik motorunda elektrik enerjisi hareket enerjisine dönüştürülür' der. Bu karışıklığın oranını ölçen bir akademik çalışma bulunamadı (güven orta).",
       DI("Küçük bir doğru akım motoru bir pile bağlandığında mili dönüyor. Aynı motorun mili elle hızla çevrildiğinde ise uçlarına bağlanan voltmetre sapıyor. "
          "Bu iki durumdaki enerji dönüşümleri için hangisi doğrudur?",
          "Pile bağlıyken mekanik enerji elektrik enerjisine, elle çevirirken elektrik enerjisi mekanik enerjiye dönüşür.",
          "Pile bağlıyken elektrik enerjisi mekanik enerjiye (ve bir miktar ısıya), elle çevirirken mekanik enerji elektrik enerjisine dönüşür.",
          "Her iki durumda da elektrik enerjisi mekanik enerjiye dönüşür.",
          "Her iki durumda da mekanik enerji elektrik enerjisine dönüşür.",
          "Motor enerji dönüşümü yapmaz; yalnızca enerjiyi aktarır.",
          "B", "A"),
       RM(["Pil motoru döndürürken enerjiyi kim sağlıyor: pil mi, mil mi?",
           "Mili elle çevirirken voltmetrenin sapması enerjiyi hangi yönde aktardığını gösterir?",
           "Bu ikisinden hangisi bir elektrik motoruna, hangisi bir jeneratöre benzer?",
           "Motor çalışırken ısınır mı? Bu enerji nereden gelir?"],
          "Pile bağlıyken mili döndüren enerji piline harcanan enerjidir; mili elle çevirdiğimizde ise voltmetre sapar çünkü elle verdiğimiz mekanik enerji elektrik enerjisine dönüşür. "
          "Motorun yalnız mekanik→elektrik yönünde çalıştığı düşünülürse pille dönen bir motoru açıklayamayız.",
          "Bisiklet dinamosu tekerlek dönerken lambayı yakar (mekanik→elektrik); elektrikli bisikletin motoru ise pilin enerjisiyle tekeri döndürür (elektrik→mekanik). "
          "Aynı tür aygıt iki yönde de çalışabilir."),
       S("TB"), "MEDIUM"),

    # --- FİZ.11.2.10: Manyetik akı ---
    MC("flux-same-as-field",
       "Manyetik akı ile manyetik alan aynı şeydir; manyetik alan sabitse bir yüzeyden geçen akı da sabittir.",
       "Manyetik akı, manyetik alanın bir yüzeyden geçen çizgi sayısının ölçüsüdür ve Φ = B·A·cosθ ile verilir (θ: yüzey normali ile B arasındaki açı). "
       "Alan sabit olsa bile yüzey alanı büyütülürse ya da yüzeyin yönü değiştirilirse akı değişir. Akı bir yüzeye ve onun yönelimine bağlı bir nicelik, alan ise uzayın bir noktasındaki bir özelliktir.",
       ["manyetik-aki", "manyetik-alan", "manyetik-alan-cizgileri", "kesit-alani"], LO("2.10"), "CONCEPTUAL_ERROR",
       "flux-factors-analogy ailesinin 'akı yalnız manyetik alanın büyüklüğüne bağlıdır' çeldiricisi ve flux-relationship-qualitative ailesinin akıyı çizgi sayısıyla karıştıran seçenekleri. "
       "Zuza vd. (2014) literatür özeti: birçok öğrenci akıyı alandan 'akan' bir şey sayar ya da alanın kendisiyle karıştırır ve ortaöğretim ve ilk yıl üniversite öğrencileri arasında indüksiyon güçlüklerinin başında gelir. "
       "Secrest ve Novodvorsky (2005): öğrencilerin çoğu değişen manyetik alanın akım oluşturduğunu söyleyebildi, ancak halkanın alanı değiştiğinde (akı değişimi) akım oluşacağını kavrayamadı (47 üniversite öğrencisi).",
       DI("Düzgün ve zamanla değişmeyen bir manyetik alanın içinde, yüzey normali alan çizgilerine paralel olan bir tel halkanın yüzeyinden geçen manyetik akı Φ'dir. "
          "Aşağıdaki işlemlerden hangisinde halkadan geçen akı Φ'den farklı olur? (Halka her durumda düzgün alanın içinde kalıyor.)",
          "Hiçbirinde; alan sabit olduğundan akı da sabit kalır.",
          "Halka kendi yüzey normali etrafında döndürülürse.",
          "Halkanın yarıçapı iki katına çıkarılırsa.",
          "Halka alan çizgilerine paralel yönde ötelenirse.",
          "Halka alana dik doğrultuda ötelenirse.",
          "C", "A"),
       RM(["Φ = B·A·cosθ ifadesinde yalnız B mi var, başka çarpanlar da var mı?",
           "Halkanın yarıçapı iki katına çıkınca yüzey alanı kaç katına çıkar? Halkadan geçen alan çizgisi sayısı ne olur?",
           "Halka normali etrafında döndürüldüğünde yüzey normali ile alan arasındaki açı değişiyor mu?",
           "Alan ile akı aynı şey olsaydı birimleri neden farklı (T ile T·m²) olurdu?"],
          "Aynı alan içinde küçük ve büyük iki halka düşün: büyük halkadan geçen alan çizgisi sayısı daha fazladır. Alan aynı kalmasına rağmen akı farklıdır; demek ki akı yalnız alan değildir.",
          "Yağmur düşünün: yağış şiddeti (alan benzeri) aynıyken büyük bir kova küçük kovadan daha fazla su toplar (akı benzeri). Toplanan miktar hem yağışın yoğunluğuna hem de kovanın ağzının büyüklüğüne ve yönüne bağlıdır."),
       S("ZUZ14", "SN05", "TB"), "HIGH"),

    MC("flux-maximum-when-surface-parallel-to-field",
       "Yüzey manyetik alan çizgilerine paralel olduğunda yüzeyden geçen manyetik akı en büyüktür.",
       "Akı Φ = B·A·cosθ ile verilir ve θ, yüzey normali ile alan arasındaki açıdır. Yüzey düzlemi alana dik (normal alana paralel, θ = 0°) iken akı en büyük, yüzey düzlemi alana paralel (θ = 90°) iken sıfırdır; "
       "çünkü alan çizgileri yüzeye teğet geçer ve onu delmez.",
       ["manyetik-aki", "manyetik-alan-cizgileri", "trigonometrik-oranlar", "vektor-bilesenleri"], LO("2.10"), "FORMULA_APPLICATION_ERROR",
       "flux-relationship-qualitative ailesinin 'yüzey alana paralel olduğunda akı en büyüktür' çeldiricisi ve flux-factors-analogy ailesinin açı etkisini yanlış kuran seçenekleri. "
       "Ders kitabı (s. 239) akıyı yüzeyi delen çizgi sayısıyla tanımlar ve θ = 90°'de akının sıfır olduğunu gösterir. Bu yanılgının oranı için doğrudan ölçüm bulunamadı; "
       "Zuza vd. (2014) akıyı alanın 'akışı' gibi düşünmenin yaygınlığını bildirir (güven orta).",
       DI("Düzgün bir manyetik alanın içinde aynı yüzey alanına sahip üç özdeş düz halka şöyle yerleştirilmiş: I. halkanın düzlemi alana dik; II. halkanın düzlemi alana paralel; "
          "III. halkanın düzlemi ile alan çizgileri arasındaki açı 30°. Halkalardan geçen manyetik akılar Φ_I, Φ_II, Φ_III için hangisi doğrudur?",
          "Φ_I > Φ_III > Φ_II",
          "Φ_II > Φ_III > Φ_I",
          "Φ_III > Φ_I > Φ_II",
          "Φ_I = Φ_II = Φ_III",
          "Φ_II > Φ_I > Φ_III",
          "A", "B"),
       RM(["Düzlemi alana paralel olan halkanın düzlemine alan çizgileri nasıl yaklaşıyor: halkayı delerek mi geçiyor, halkayla birlikte uzanıyor mu?",
           "Yüzey normali ile alan arasındaki açı I. halkada kaç derece? II. halkada kaç derece?",
           "cos0° ve cos90° değerleri nedir? Hangisi akıyı en büyük yapar?",
           "III. halkada normal–alan açısı kaç derecedir ve cos'u kaç eder?"],
          "Halkanın düzlemi alan çizgilerine paralelse çizgiler halkanın içinden geçmez; yüzeye teğet uzanır. Hiç çizgi geçmeyen bir yüzeyden en büyük akı geçemez.",
          "Rüzgâr esiyorken bir kapıyı rüzgâra paralel (kenar kenara) tuttuğunda rüzgârdan hiç etkilenmezsin; kapıyı rüzgâra dik tuttuğunda ise rüzgârı tam karşılarsın. Alan çizgileri 'rüzgâr', halka 'kapı'dır."),
       S("TB", "ZUZ14"), "MEDIUM"),

    MC("motion-of-loop-always-changes-flux",
       "Düzgün bir manyetik alanın içinde bir tel halka hareket ettiği sürece halkadan geçen akı değişir.",
       "Akı yalnız B, A ve θ'ya bağlıdır; hareket tek başına akıyı değiştirmez. Düzgün ve sabit bir alan içinde halka ötelenirken (alan dışına çıkmıyor ve yönelimi değişmiyor) B, A ve θ sabit kalır ve akı sabittir. "
       "Akı ancak halkanın alanı, yönelimi (θ) ya da halkanın içinde bulunduğu alanın değeri değişirse değişir.",
       ["manyetik-aki", "manyetik-alan", "induksiyon-akimi", "faraday-induksiyon-yasasi"], LO("2.10", "2.11"), "CONCEPTUAL_ERROR",
       "flux-change-in-motion ailesinin 'halka hareket ettiği için her durumda akı değişir' çeldiricisi ve induction-experiment-factors ailesindeki hareket–indüksiyon karıştırması. "
       "Secrest ve Novodvorsky (2005): bazı öğrenciler indüksiyon akımının yönünü yalnız hareketin yönüne bağladı; Maries vd. (2022): CSEM Q29'da en yaygın yanlış yanıt, indüksiyon için mıknatıs–halka arasında göreli hareket "
       "ya da alan değişimi arayıp halkanın alanındaki değişimi fark etmemektir (iki yanılgı birbirinin tersidir; ikisi de akı kavramı yerine hareket sezgisine dayanır).",
       DI("Düzgün ve zamanla değişmeyen bir manyetik alan içinde, düzlemi alana dik olan küçük bir dikdörtgen tel halka, düzgün alanın dışına çıkmadan alan doğrultusunda sabit hızla ötelenmektedir. "
          "Halka için hangisi doğrudur?",
          "Akı değişir; halkada sürekli bir indüksiyon akımı oluşur.",
          "Akı sabittir; halkada indüksiyon akımı oluşmaz.",
          "Akı sabittir; ama hareket nedeniyle halkada yine de bir akım oluşur.",
          "Akı yalnız halkanın alan bölgesinin içinde olduğu sürece artar.",
          "Akı hızla orantılı olarak artar; indüksiyon akımı da hızla birlikte artar.",
          "B", "A"),
       RM(["Halkanın yüzey alanı değişiyor mu? Yüzey normali ile alan arasındaki açı değişiyor mu? Alanın değeri değişiyor mu?",
           "Φ = B·A·cosθ ifadesinde halkanın konumu geçiyor mu, yoksa yalnız B, A ve θ mı?",
           "Halka ötelenirken içinden geçen alan çizgisi sayısı artıyor mu, azalıyor mu?",
           "İndüksiyon için neye ihtiyaç var: hareket mi, akı değişimi mi?"],
          "Halka düzgün alan içinde ötelenirken içinden geçen alan çizgisi sayısı aynı kalıyor; halkada hiçbir akım gözlenmiyorsa ('hareket varsa indüksiyon vardır' diyen düşünce yanlış olurdu) bu, hareketin tek başına akımı oluşturmadığını gösterir.",
          "Düzgün yağan yağmur altında yürüyen şemsiyenin altından geçen yağmur miktarı, şemsiye aynı biçimde tutulduğu sürece aynıdır; yürümek (hareket) tek başına şemsiyenin altından geçen yağmuru değiştirmez, ama şemsiyeyi eğmek ya da büyütmek değiştirir."),
       S("SN05", "MBS22", "ZUZ14"), "HIGH"),

    # <<U2-INSERT>>
]

_balance_answer_positions(MISCONCEPTIONS[_U2_START:])
