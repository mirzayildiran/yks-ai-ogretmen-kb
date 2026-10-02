"""ÖSYM yayımlanmış fizik sorularının yapısal analizi (STEP 10).

Kaynak: osym.gov.tr "Temel Soru Kitapçıkları ve Cevap Anahtarları" duyurularındaki resmî PDF'ler
(dokuman.osym.gov.tr). Sorular PDF'den görsel olarak okunmuş; soru metni KOPYALANMAMIŞTIR, yalnız yapısal özet.
question_no = AYT Fen Bilimleri testinin Fizik bölümündeki sıra (1-14); TYT için Fizik bölümü sırası (1-7).
"""

_D = "https://dokuman.osym.gov.tr/pdfdokuman"
URLS = {
    ("AYT", 2018): f"{_D}/2018/YKS/AYT_01072018.pdf",
    ("TYT", 2018): f"{_D}/2018/YKS/TYT_01072018.pdf",
    ("AYT", 2019): f"{_D}/2019/YKS/TSK/ayt_yks_2019_web.pdf",
    ("TYT", 2019): f"{_D}/2019/YKS/TSK/tyt_yks_2019_web.pdf",
    ("AYT", 2020): f"{_D}/2020/YKS/TSK/ayt_yks_2020.pdf",
    ("TYT", 2020): f"{_D}/2020/YKS/TSK/tyt_yks_2020.pdf",
    ("AYT", 2021): f"{_D}/2021/YKS/TSK/ayt_yks_2021.pdf",
    ("TYT", 2021): f"{_D}/2021/YKS/TSK/tyt_yks_2021.pdf",
    ("AYT", 2022): f"{_D}/2022/YKS/TSK/yks_2022_ayt.pdf",
    ("TYT", 2022): f"{_D}/2022/YKS/TSK/yks_2022_tyt.pdf",
    ("AYT", 2023): f"{_D}/2023/YKS/TSK/yks_ayt_2023_kitapcik_g5A2H.pdf",
    ("TYT", 2023): f"{_D}/2023/YKS/TSK/yks_tyt_2023_kitapcik_T23ky.pdf",
    ("AYT", 2024): f"{_D}/2024/YKS/TSK/yks_ayt_2024_kitapcik_ts85k.pdf",
    ("TYT", 2024): f"{_D}/2024/YKS/TSK/yks_tyt_2024_kitapcik_T24kt.pdf",
    ("AYT", 2025): f"{_D}/2025/YKS/TSK/yks_ayt_2025_kitapcik_st12.pdf",
    ("TYT", 2025): f"{_D}/2025/YKS/TSK/yks_tyt_2025_kitapcik_d250.pdf",
}

ANNOUNCEMENTS = [
    {"id": "ann-osym-2028-not-found", "title": "ÖSYM'nin 2028 YKS / Maarif Modeli için resmî açıklaması: osym.gov.tr'de bulunamadı",
     "organization": "ÖSYM (osym.gov.tr)", "url": "https://www.osym.gov.tr/SinavGrubu/Index/2", "date": "2026-10-02",
     "summary": "YKS duyuru listesi ve 2026-YKS Kılavuzu PDF'i tarandı; 2028 sınavı, Maarif Modeli veya beceri temelli soru modeline dair ÖSYM kaynaklı resmî açıklama bulunamadı. Blog iddiaları duyuru olarak kaydedilmedi.",
     "relevance": "2028 YKS biçimi hakkında ÖSYM tarafından yayımlanmış bağlayıcı bir belge yok; analiz 2018-2025 gerçek sorularına ve 11. sınıf program sınırlarına dayanır.",
     "verified_read": True},
    {"id": "ann-meb-2025-12-yks-lgs-2028", "title": "YKS ve LGS'de yeni müfredata uyumlu soru modeli 2028'de hayata geçecek",
     "organization": "MEB (ÖSYM ile iş birliği)", "url": "https://www.meb.gov.tr/yks-ve-lgsde-yeni-mufredata-uyumlu-soru-modeli-2028de-hayata-gececek/haber/39265/tr",
     "date": "2025-12-15",
     "summary": "MEB Bakan Yardımcısı: yeni müfredata uyumlu, beceri ve bağlam temelli soru modeli 2028'de YKS ve LGS'de kullanılacak; soru modelleme ÖSYM ile sürüyor; çoktan seçmeli biçim korunacak; örnek sorular MEB platformlarından paylaşılacak.",
     "relevance": "Soru biçiminin bilgi hatırlamadan bağlam içinde bilgi kullanımına kayacağını resmî düzeyde bildirir; sınav sistemi (TYT-AYT) değişikliği değil.",
     "verified_read": True},
    {"id": "ann-meb-2024-11-osym-ziyaret", "title": "Bakan Tekin, ÖSYM Başkanı Ersoy'u kabul etti",
     "organization": "MEB", "url": "https://meb.gov.tr/bakan-tekin-osym-baskani-ersoyu-kabul-etti/haber/35320/tr", "date": "2024-11-04",
     "summary": "9. sınıfta Maarif Modeli ile başlayan öğrencilerin YKS'ye 2028'de gireceği, 10-12. sınıfların eski müfredatla sınava gireceği; TYT ve AYT için MEB-ÖSYM uzman çalıştayları yapıldığı belirtildi.",
     "relevance": "2028 YKS'nin Maarif müfredatına uyumlu olacağını ve geçiş takvimini doğrular.",
     "verified_read": True},
]

ITEMS = []


def Q(year, exam, no, topic, los, out, fam, fm, skills, c, i, m, flags, distractor, strategy, summary, fit, fit_reason, conf, rm="official_pdf"):
    """Kompakt kayıt üretici. flags: boşlukla ayrılmış {ms gr tb ex dl} (multi_step, graph, table, experimental, daily_life)."""
    f = set(flags.split())
    assert f <= {"ms", "gr", "tb", "ex", "dl"}, flags
    return {"year": year, "exam": exam, "question_no": no, "source_url": URLS[(exam, year)], "read_method": rm, "topic": topic,
            "learning_outcomes": los, "out_of_11_scope": out, "question_family": fam, "family_match": fm, "skills": skills,
            "conceptual_load": c, "interpretation_load": i, "mathematical_load": m, "multi_step": "ms" in f, "graph_based": "gr" in f,
            "table_based": "tb" in f, "experimental_context": "ex" in f, "daily_life_context": "dl" in f, "distractor_structure": distractor,
            "solution_strategy": strategy, "summary": summary, "fit_2028": fit, "fit_reason": fit_reason, "confidence": conf}


# Ortak çeldirici yapısı etiketleri
ROMAN = "I-II-III öncülleri; şıklar öncül kombinasyonları (Yalnız I … I, II ve III)"
NUM = "sayısal şıklar (A–E artan değerler)"


# ============================ 2018 AYT (14/14 okundu) ============================
ITEMS += [
    Q(2018, "AYT", 1, "Makara düzeneğinde bağlı cisimlerin ivmesi (Newton II)", ["FİZ.11.1.5"], "", "connected-bodies-same-acceleration", "exact", ["KB2.14"],
      2, 2, 2, "ms", NUM, "Her sistemde net kuvvet / toplam kütle; birinden kütle bulunup diğerinin ivmesine geçilir",
      "Biri doğrudan çekilen, biri asılı ağırlıklarla çekilen iki özdeş sandıktan birinin ivmesi verilip diğerinin ivmesi isteniyor.",
      "yes", "Aynı ivmeyle hareket eden bağlı cisimler programda var; tek sistemde farklı ivmeli cisim yok.", "HIGH"),
    Q(2018, "AYT", 2, "Çembersel yörüngeden kopan taşın hız-ivme vektörleri", ["FİZ.11.1.9", "FİZ.11.1.3"], "", "string-cut-trajectory", "exact", ["KB2.16.3"],
      2, 2, 0, "ms dl", "nokta kümeleri (Yalnız II, I ve IV, …)", "Kopma anındaki hız teğettir; sonra ivme düşey g olduğundan hız düşey olan noktalar seçilir",
      "Düşey çemberde döndürülen taş serbest kalınca hız ve ivmenin birbirine paralel olduğu kopma noktaları isteniyor.",
      "yes", "Çembersel hareketin hız vektörü ve iki boyutlu hareketin ivmesi (yalnız g) doğrudan kapsamda.", "HIGH"),
    Q(2018, "AYT", 3, "Buz pateni: karşılıklı itme, momentum ve itme", [], "12. sınıf FİZ.12.1.3", None, "none", [],
      2, 1, 0, "dl", ROMAN, "Momentum korunumu: eşit büyüklükte momentum, kütle farkından hız karşılaştırması",
      "İki patenci birbirini iterek zıt yönlere kayıyor; hız, momentum ve itme büyüklüklerinin hangisinin öğrencide daha büyük olduğu soruluyor.",
      "no", "İtme-momentum 12. sınıfa (FİZ.12.1.3-4) taşındı; 11. sınıf programında yok.", "HIGH"),
    Q(2018, "AYT", 4, "Çubuğun dengesi ve tork oranı", [], "12. sınıf FİZ.12.1.1", None, "none", [],
      2, 2, 2, "", "kesirli şıklar (1/3, 2/3, 3/2, 3, 1)", "Mil noktasına göre tork dengesi; kuvvet kolu oranı",
      "Eşit bölmeli çubuk iki kuvvetle dengede; birinin torku verilmişken diğerinin torkunun oranı bulunuyor.",
      "no", "Tork ve denge 12. sınıf (FİZ.12.1.1-2) konusudur.", "HIGH"),
    Q(2018, "AYT", 5, "Düzgün elektrik alanda asılı yüklü cismin sapma açısı", ["FİZ.11.2.2", "FİZ.11.1.5"], "", "efield-force-balance-droplet", "partial", ["KB2.14"],
      2, 2, 0, "ms", ROMAN, "Denge: tanα = qE/mg; hangi niceliğin artınca açının arttığına nitel karar",
      "Elektrik alanda ipe asılı yüklü cisim dengede; ip uzunluğu, kütle ve alan artırılınca sapma açısının değişimi soruluyor.",
      "yes", "Alan–kuvvet oran/yön yorumu ve serbest cisim diyagramı; hesap gerekmiyor.", "HIGH"),
    Q(2018, "AYT", 6, "Manyetik alandaki akım taşıyan çubuğun harekete geçmesi", ["FİZ.11.2.8"], "", "wire-force-direction-rhr", "exact", ["FBAB10"],
      2, 2, 0, "ex", "hareket durumu seçenekleri (hareketsiz / I ya da II yönünde hızlanır / sabit hızlı)", "Sağ el kuralıyla kuvvet yönü; sürtünmesiz rayda ivmeli hareket",
      "Mıknatıs içinde ray üstünde duran çubuk, anahtar kapanınca akım taşır; çubuğun ilk hareketinin yönü ve türü soruluyor.",
      "yes", "Akımlı tele etki eden kuvvetin yönü ve F=BIL mantığı doğrudan kapsamda.", "HIGH"),
    Q(2018, "AYT", 7, "Transformatörde doğru ve alternatif akımla sekonder gerilimi", ["FİZ.11.2.13", "FİZ.11.2.12"], "", "transformer-turns-voltage-current-ratio", "partial", ["FBAB8"],
      3, 2, 0, "ms", "iki sütunlu şıklar (Sıfırdır / primerden büyük / küçük)", "DC primerde akı değişimi yok → sekonder sıfır; AA'da sarım oranına göre karşılaştırma",
      "Biri doğru akım, biri alternatif akım kaynağına bağlı iki transformatörün sekonder gerilimlerinin primere göre durumu soruluyor.",
      "yes", "Transformatör nitelikleri yalnız yorumlanıyor; sayısal sarım hesabı yok, program ile uyumlu.", "HIGH"),
    Q(2018, "AYT", 8, "Sarkacın en alt noktasında net kuvvet, ivme ve hız yönleri", ["FİZ.11.1.5", "FİZ.11.1.9"], "", "net-force-motion-state", "partial", ["KB2.14"],
      2, 3, 0, "", "vektör çizimi seçenekleri (üç vektörün yön kombinasyonları)", "Merkezcil ivme merkeze, net kuvvet ivmeyle aynı yön; hız teğet",
      "Salınan bilyenin en alt noktasından geçerken net kuvvet, merkezcil ivme ve hız vektörlerinin yönlerini gösteren doğru çizim seçiliyor.",
      "yes", "Net kuvvet-ivme ilişkisi ve çembersel hareketin merkezcil ivmesi kapsamda; sarkaç yalnız bağlam.", "MEDIUM"),
    Q(2018, "AYT", 9, "Dünya'nın yörüngesinde günberi: hız, açısal momentum, çekim kuvveti", [], "programda yok (kütle çekim/Kepler; açısal momentum yalnız 12. sınıf FİZ.12.1.6 dönme bağlamında)", None, "none", [],
      3, 2, 0, "", ROMAN, "Günberide hız ve çekim büyük; açısal momentum korunur (eşit)",
      "Dünya'nın Güneş'e en yakın olduğu günle uzak olduğu günün çizgisel hız, açısal momentum ve çekim kuvveti büyüklükleri karşılaştırılıyor.",
      "no", "Kütle çekim ve Kepler yasaları 9-12. sınıf programında yer almıyor.", "MEDIUM"),
    Q(2018, "AYT", 10, "Yay-kütle ve basit sarkaç periyotlarının eşitlenmesi", [], "programda yok (BHH periyot hesabı; 10. sınıf FİZ.10.4.1 yalnız kavramsal)", None, "none", [],
      2, 2, 3, "ms", NUM, "T=2π√(l/g) ile T=2π√(m/k) eşitlenir; k=mg/l",
      "Düşey yaya asılı kütlenin periyodu, belirli uzunluktaki basit sarkaçla eşit olacak şekilde yay sabiti soruluyor.",
      "no", "Basit harmonik hareket hesabı yeni programda yok.", "HIGH"),
    Q(2018, "AYT", 11, "Radyo dalgalarının doğası", [], "12. sınıf FİZ.12.3.5", None, "none", [],
      1, 1, 0, "dl", ROMAN, "Elektromanyetik dalga: enine, boşlukta yayılır, ses değildir",
      "Radyo vericisinden alıcıya gelen dalganın ses mi, enine mi, maddesel ortam gerektirir mi olduğu öncüllerle yargılanıyor.",
      "no", "Elektromanyetik dalgalar 12. sınıf (FİZ.12.3.5) konusu.", "HIGH"),
    Q(2018, "AYT", 12, "Döteryum-trityum füzyonu ve çekirdek kararlılığı", [], "12. sınıf FİZ.12.4.8", None, "none", [],
      3, 2, 0, "", ROMAN, "Enerji açığa çıkması: ürün çekirdek bağlanma enerjisi başına daha kararlı",
      "Füzyon tepkimesi enerji verdiğine göre hangi çekirdeklerin birbirine göre daha kararlı olması gerektiği öncüllerle soruluyor.",
      "no", "Nükleer enerji 12. sınıf (FİZ.12.4.8) konusu.", "MEDIUM"),
    Q(2018, "AYT", 13, "Fotoelektrik olay: Ek–f grafiği", [], "12. sınıf FİZ.12.4.2", None, "none", [],
      3, 2, 0, "gr", ROMAN, "Eğim h evrensel; eşik frekansı üstündeki f için elektron çıkar",
      "Maksimum kinetik enerji–frekans grafiğinden eğimin, eşik frekansının ve dalga boyunun yorumlanmasına dair öncüller değerlendiriliyor.",
      "no", "Fotoelektrik olay 12. sınıf (FİZ.12.4.2) konusu.", "HIGH"),
    Q(2018, "AYT", 14, "X ışınlarının görünür ışığa göre büyüklükleri", [], "12. sınıf FİZ.12.3.5", None, "none", [],
      2, 1, 0, "dl", ROMAN, "Elektromanyetik tayf sırası: X ışını frekansı büyük, dalga boyu küçük, hız aynı",
      "X ışınlarının canlılara zarar verebilmesinin hız, dalga boyu ve frekanstan hangisinin görünür ışıktan kesinlikle büyük olmasından kaynaklandığı soruluyor.",
      "no", "Elektromanyetik tayf 12. sınıf (FİZ.12.3.5) konusu.", "HIGH"),
]

# ============================ 2019 AYT (14/14 okundu) ============================
ITEMS += [
    Q(2019, "AYT", 1, "Göreli hız: iki aracın hız vektörlerinden gözlemciye göre hız", [], "9. sınıf FİZ.9.2.4 (vektör toplama); hareketli referans yalnız 11. sınıf zenginleştirmede", None, "none", [],
      2, 2, 2, "ms dl", "büyüklük+yön çiftleri (15√2 güneybatı …)", "Referans değişimi: vektör farkı; dik bileşenlerden Pisagor",
      "Batıya ve kuzeye sabit hızla giden iki araçtan birinin sürücüsüne göre diğerinin hızının büyüklüğü ve yönü isteniyor.",
      "no", "Vektör toplama 9. sınıf konusu; hareketli referanstan bakış 11. sınıf programında yalnız zenginleştirme düzeyinde.", "MEDIUM"),
    Q(2019, "AYT", 2, "Farklı yüksekliklerden yatay fırlatılan cisimlerin ilk hız oranı", ["FİZ.11.1.3"], "", "2d-horizontal-launch", "exact", ["FBAB10"],
      2, 2, 2, "ms gr", "kesirli/köklü oran şıkları (1/4, 1/√2, 1/2, 1, √2)", "Düşme süresi √h ile orantılı; aynı menzilde v ∝ 1/t",
      "Aynı noktaya düşen ve farklı yüksekliklerden yatay atılan iki cismin ilk hızlarının oranı soruluyor; yol şekille veriliyor.",
      "yes", "İki boyutta sabit ivmeli hareket için sayısal hesap programda kapsam içinde (CALC_INCLUDED).", "HIGH"),
    Q(2019, "AYT", 3, "Çarpışma testi: ortalama itme kuvveti", [], "12. sınıf FİZ.12.1.3", None, "none", [],
      2, 1, 2, "dl", NUM, "İtme = momentum değişimi; F = m·Δv/Δt",
      "Hareketli arabadan duran mankenin durması için gereken en az ortalama kuvvet, kütle, hız ve çarpışma süresiyle hesaplatılıyor.",
      "no", "İtme-momentum 12. sınıfa taşındı.", "HIGH"),
    Q(2019, "AYT", 4, "Dengedeki sandıkta net kuvvet sıfırken ivme, tork ve momentum", ["FİZ.11.1.4"], "tork ve momentum öncülleri 12. sınıf FİZ.12.1.1-3", None, "none", [],
      2, 2, 0, "dl", ROMAN, "Net kuvvet sıfır → ivme sıfır; tork ve momentum için 'kesinlikle' ayrımı",
      "Birkaç kişinin taşıdığı sandığa etkiyen bileşke kuvvet sıfırken kütle merkezi ivmesi, toplam tork ve çizgisel momentumun kesinlikle sıfır olup olmadığı yargılanıyor.",
      "form_changes", "Yalnız net kuvvet–ivme öncülü 11. sınıfta; tork ve momentum öncülleri 12. sınıf, biçim değişmeli.", "MEDIUM"),
    Q(2019, "AYT", 5, "Farklı yarıçaplı iletken bilyelerde yük aktarımı sonrası yük ve potansiyel", [], "programda yok (iletkenlerde yük paylaşımı, elektriksel potansiyel; 8. sınıf elektriklenme temel kabul)", None, "none", [],
      3, 2, 0, "ex", ROMAN, "Dokundurma sonrası potansiyeller eşit; yük miktarı yarıçapa bağlı, aynı işaretli",
      "İki farklı boyutta metal bilye yüklenip dokundurulduktan sonra net yük, potansiyel ve yük cinsi ile ilgili öncüller değerlendiriliyor.",
      "no", "Elektriksel potansiyel ve iletkende yük dağılımı yeni 9-12. sınıf programında yok.", "MEDIUM"),
    Q(2019, "AYT", 6, "Mıknatıs ve silginin halkadan düşerken Lenz etkisi", ["FİZ.11.2.10", "FİZ.11.2.11"], "", "magnet-falling-through-ring", "exact", ["KB2.4", "FBAB10"],
      3, 3, 0, "ex", "beş durum önermesi (yükseklik karşılaştırması, kutup/kütle bağımlılığı)", "Mıknatıs akı değişimi nedeniyle frenlenir; silgi serbest düşer; kontrol değişkeni mantığı",
      "Mıknatıs ile silgi alüminyum halkadan düşerken halkada akım oluşmasının mıknatısı geciktirmesi nedeniyle bunların halkayı geçtikten sonraki yükseklikleri karşılaştırılıyor.",
      "yes", "Akı değişimi ve indüksiyon akımının yönü/etkisi nitel; programda hesapsız kapsam uygun.", "HIGH"),
    Q(2019, "AYT", 7, "Müzik çalar devresinde frekansa göre direnç gösteren eleman", [], "programda yok (bobin/kondansatör reaktansı, AA devre elemanları)", None, "none", [],
      3, 2, 0, "dl", ROMAN, "Kondansatör düşük frekansa büyük direnç; bobin yüksek frekansa büyük direnç; reosta frekanstan bağımsız",
      "Düşük frekanslı sinyallere daha büyük direnç gösterecek devre elemanının bobin, reosta ve kondansatörden hangileri olabileceği soruluyor.",
      "no", "Bobin ve kondansatörün AA'daki davranışı programda yok.", "HIGH"),
    Q(2019, "AYT", 8, "Otoyol virajlarını güvenli kılan önlemler", ["FİZ.11.1.10"], "", "banked-curve", "exact", ["FBAB10"],
      2, 1, 0, "dl", ROMAN, "Eğimli viraj ve sürtünme kuvveti merkezcil kuvvete katkı; yarıçap küçültmek tehlikeli",
      "Araçların virajda güvenli dönmesi için yol-lastik sürtünmesi, virajın eğimi ve yarıçapına ilişkin önlemlerden hangilerinin uygulanması gerektiği öncüllerle soruluyor.",
      "yes", "Yatay ve eğimli viraj ile viraj güvenliği programda doğrudan var.", "HIGH"),
    Q(2019, "AYT", 9, "Kollarını gövdesine yaklaştıran patencide açısal momentum ve eylemsizlik momenti", [], "12. sınıf FİZ.12.1.5-6", None, "none", [],
      2, 2, 0, "dl", "iki sütunlu şıklar (artar / azalır / değişmez)", "Dış tork yok → açısal momentum korunur; kütle merkeze yaklaşınca eylemsizlik momenti azalır",
      "Buz pistinde dönen kişi kollarını gövdesine yaklaştırınca açısal momentum ve eylemsizlik momentinin nasıl değiştiği soruluyor.",
      "no", "Eylemsizlik momenti ve açısal momentum korunumu 12. sınıf konusu.", "HIGH"),
    Q(2019, "AYT", 10, "Yay-kütle sistemlerinde titreşim frekansları karşılaştırması", [], "programda yok (basit harmonik hareket frekansı, yay bağlama; 12. sınıf FİZ.12.2.1-2 yalnız Hooke)", None, "none", [],
      3, 3, 0, "ms", "frekans sıralaması şıkları (fX < fY = fZ …)", "f ∝ √(k_eş/m); eğik düzlem frekansı değiştirmez; seri yay k_eş küçük",
      "Düşeyde asılı, eğik düzlemde ve iki yaya seri asılı üç özdeş kütlenin titreşim frekansları arasındaki sıralama soruluyor.",
      "no", "Basit harmonik hareket ve yay sabitlerinin eşdeğeri yeni programda yok.", "MEDIUM"),
    Q(2019, "AYT", 11, "Elektromanyetik tayfta hız, frekans ve dalga boyu karşılaştırması", [], "12. sınıf FİZ.12.3.5", None, "none", [],
      2, 1, 0, "", ROMAN, "Aynı ortamda sürat aynı değil (boşlukta eşit); frekans: X > mikrodalga; dalga boyu: kırmızı > mavi",
      "Gama, X, mikrodalga, radyo ve görünür ışık dalgalarının sürat, frekans ve dalga boyu bakımından birbirine göre durumu öncüllerle sınanıyor.",
      "no", "Elektromanyetik dalga sınıflandırması 12. sınıf (FİZ.12.3.5-6).", "HIGH"),
    Q(2019, "AYT", 12, "Radyoaktif bozunma zincirinde yayınlanan parçacıklar", [], "12. sınıf FİZ.12.4.8 (yalnız sorgulama düzeyi; bozunma türleri programda açık değil)", None, "none", [],
      3, 2, 1, "ms", "iki sütunlu şıklar (β⁻/β⁺/α kombinasyonları)", "Kütle ve atom numarası değişimini izleyerek bozunma türünü bulma",
      "Bizmut çekirdeğinin iki ardışık bozunmayla kurşuna dönüşmesinde her adımda yayınlanan parçacığın türü kütle ve proton sayısı değişiminden bulunuyor.",
      "no", "Radyoaktif bozunma 12. sınıfta yalnız nükleer enerji sorgulaması kapsamında.", "MEDIUM"),
    Q(2019, "AYT", 13, "Fotoelektrik düzenekte kullanılabilecek eşik enerjisi sınırı", [], "12. sınıf FİZ.12.4.2", None, "none", [],
      3, 2, 3, "ms", NUM, "E = hc/λ ile ışık enerji aralığı; eşik ≤ foton enerjisi koşulu",
      "Dalga boyu aralığı ve hc değeri verilen ışıkla fotoelektron koparabilmek için metalin eşik enerjisinin en çok ne olabileceği hesaplatılıyor.",
      "no", "Fotoelektrik olay 12. sınıf konusu.", "HIGH"),
    Q(2019, "AYT", 14, "Termal kamera, PET ve sonarın görüntü oluşturma prensipleri", [], "12. sınıf FİZ.12.3.7", None, "none", [],
      2, 2, 0, "dl", "üçlü eşleştirme şıkları (cihaz sıralamaları)", "Cihaz–dalga türü eşleştirme (kızılötesi, ses, antiparçacık)",
      "Üç görüntüleme cihazının hangi fiziksel ilkeyle (kızılötesi yayım, ses yansıması, antiparçacık yok oluşu) görüntü oluşturduğu eşleştiriliyor.",
      "no", "Dalga kullanan cihazlar 12. sınıf (FİZ.12.3.7); PET kapsam dışı.", "MEDIUM"),
]
