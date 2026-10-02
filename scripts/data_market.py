"""STEP 9 verisi: piyasa kaynaklarının (Tier 3) YAPISAL analizi. Telifli soru/sayfa içeriği kopyalanmaz.

Tarama tarihi: 2026-10-02. Yöntem: yayınevi/ürün sayfası okundu (WebFetch/curl); herkese açık örnek sayfa
(flipbook / yayınevi örnek PDF'i) varsa tarayıcıda sayfalar tek tek görüntülenip yalnız soru TARZI ve KALIP not edildi.
Kural: örnek sayfa okunmadıysa family_mapping boş; Maarif beyanı yalnız yayınevi/ürün sayfası ya da kapakta AÇIKÇA yazıyorsa True.
"""


def _s(**kw):
    base = dict(edition_year=None, maarif_claim=None, verified_by_fetch=False, question_styles=[], difficulty=None,
                pedagogical_style="", unique_characteristics=[], sample_evidence=[], family_mapping=[],
                old_curriculum_risk=False, notes="", confidence="LOW")
    base.update(kw)
    return base


def _fm(family, evidence, match="exact"):
    return {"family": family, "evidence": evidence, "match": match}


SOURCES = []

# ---------------------------------------------------------------------------------------------------------------
# 1) Paraf — 11. sınıf (yayınevi sitesi + herkese açık flipbook örneği okundu)
# ---------------------------------------------------------------------------------------------------------------
SOURCES += [
    _s(slug="paraf-11-iq-fizik-soru-kutuphanesi", publisher="Paraf", title="11. Sınıf IQ Fizik Soru Kütüphanesi",
       kind="soru_bankasi", target="11", edition_year=None, maarif_claim=True,
       url="https://parafyayinlari.com/11-sinif/11-sinif-iq-fizik-soru-kutuphanesi", verified_by_fetch=True,
       question_styles=["KLASIK_ISLEM", "GRAFIK_TABLO", "KAVRAMSAL", "BAGLAM_TEMELLI"], difficulty="karma",
       pedagogical_style="Ünite > bölüm > test; her test 10 soru, sayfa altında cevap anahtarı şeridi; kısa stemli, şekilli, "
                         "çoktan seçmeli; testlerin sonuna doğru 'Bağlam Temelli' etiketli sorular.",
       unique_characteristics=[
           "Kapakta 'Yeni — Maarif Modeline Uygundur' ve 'Temelli Bağlam & Beceri Testler' rozeti; video çözüm, akıllı tahta ve mobil kütüphane simgeleri",
           "Örnek bölümde konu başına 3-4 test (Serbest Düşme 4, İki Boyutta Sabit İvmeli Hareket 5, Newton Yasaları 2 test görüldü)",
           "Sorular kısa ve şematik: bağlam sahnesi yok, ağırlık I-II-III öncül ve oran soruları",
           "'Bağlam Temelli' etiketli sorular (öğrenci iddiası + tablo, hava balonu/uçak/kamyon sahnesi, gezegen g tablosu) testin ikinci yarısında toplanıyor",
       ],
       sample_evidence=[{"url": "https://numunekitap.com/paraf/11-sinif/11-sinif-iq-fizik-soru-kutuphanesi",
                         "what": "Yayınevinin herkese açık flipbook örneği, s.1-31 görüntülendi: Ünite 1 Kuvvet ve Hareket; Bölüm 1 Serbest Düşme "
                                 "(Test 1-4, s.11-18), Bölüm 2 İki Boyutta Sabit İvmeli Hareket (Test 5-9, s.19-28), Bölüm 3 Newton'un Hareket Yasaları "
                                 "(Test 10-11, s.29-31). Soru metni kaydedilmedi."}],
       family_mapping=[
           _fm("ff-kinematics-v0zero", "Test 1 (s.11-12): ilk hızsız bırakılan cisimde yere ulaşma süresi/çarpma hızı ve yükseklik sorulan, seçenekleri tablo olan sorular"),
           _fm("ff-upward-throw", "Test 3 (s.14-16): düşey yukarı atış, maksimum yükseklik ve havada kalma sorusu, v-t grafiği ile verilen yukarı atış"),
           _fm("ff-downward-throw-or-moving-carrier", "Test 3 (s.15) aşağı yönlü ilk hızlı atış; Test 7 (s.23) ve Test 4 (s.18) hava balonundan bırakılan cisim"),
           _fm("ff-motion-graphs", "Test 3 s.16 (aşağı atılan cismin v-t grafiğini seçme, 5 grafik seçenekli), Test 4 s.17 (v-t grafikleriyle büyüklük sıralaması)"),
           _fm("ff-data-pattern-g", "Test 4 s.18: farklı gezegenlerin çekim ivmesi tablosu verilip yargı değerlendirme", "partial"),
           _fm("ff-data-evidence", "Test 4 s.17 (Bağlam Temelli): öğrencinin tablo üzerinden iddiası ve hatalı çıkarımı bulma", "partial"),
           _fm("2d-horizontal-launch", "Test 5-6 (s.19-21): yatay atışta uçuş süresi, menzil, yere çarpma hızı, hız oranları, ızgaralı şekil"),
           _fm("2d-angled-launch", "Test 8 (s.24-26): 37/53 derece açılı atışta uçuş süresi, maksimum yükseklik, menzil, yargı öncülleri"),
           _fm("2d-velocity-at-point", "Test 8 s.26: yörünge üzerinde K-L-M noktalarında hız büyüklüklerinin karşılaştırılması"),
           _fm("2d-component-graphs", "Test 7 s.23 ve Test 8 s.26: bileşen (v_y-t) grafiği ve seçenekleri tablo olan grafik soruları"),
           _fm("2d-component-data", "Test 5 s.20: öğrenci iddiası + hız bileşeni değişkenleri tablosunda hatalı hücreyi bulma", "partial"),
           _fm("2d-moving-reference-launch", "Test 9 (s.27): uçaktan bırakılan paket ve hareketli kamyon üzerinden atış; yer ve araç referanslı hız bileşenleri (Bağlam Temelli)"),
           _fm("newton1-inertia", "Test 10 (s.29): eylemsizlik durumlarının öncüllerle yorumlanması (Bağlam Temelli)"),
           _fm("newton2-f-m-a-relations", "Test 10 s.30 (v-t grafiğinden kuvvet oranı) ve Test 11 s.31 (kuvvet-ivme grafiğinden kütle karşılaştırma)"),
           _fm("net-force-motion-state", "Test 11 s.31: kuvvet vektörleri verilen cisimlerin hareket durumu ve ivme karşılaştırması", "partial"),
       ],
       notes="Örnek flipbook 31 sayfalık ilk bölümle sınırlı; Optik ve Elektrik-Manyetizma üniteleri görülmedi. Baskı yılı ürün sayfasında yok (kapak 'YENİ' diyor). "
             "Maarif beyanı kapaktan okundu (yayınevi beyanı). Serbest düşme 11. sınıfta Maarif'e özgü ilk konudur; eski müfredat konusu (tork, momentum, vektör) örnekte görülmedi.",
       confidence="HIGH"),

    _s(slug="paraf-11-mod-fizik-anlatim-fasikulu", publisher="Paraf", title="11. Sınıf MOD Fizik Anlatım Fasikülü",
       kind="fasikul", target="11", edition_year=None, maarif_claim=True,
       url="https://parafyayinlari.com/11-sinif/11-sinif-mod-fizik-anlatim-fasikulu", verified_by_fetch=True,
       question_styles=["KLASIK_ISLEM", "BAGLAM_TEMELLI", "GRAFIK_TABLO", "KAVRAMSAL"], difficulty="karma",
       pedagogical_style="Konu anlatımı + 'Örnek' (çözümü boş bırakılmış) + 'Sıra Sende' çiftleri; kenar notlar ('Not'); bölüm başında öğrenme çıktısı kodları.",
       unique_characteristics=[
           "Kapakta 'Yeni — Maarif Modeline Uygundur', 'Bu kitap 2 modülden oluşur'; 'Temel Bilgiler, Etkinlikler, Açık Uçlu Sorular, Kavrama Testleri' bölümleri",
           "Bölüm açılışında resmî öğrenme çıktısı kodları (FİZ.11.1.x) basılı",
           "Örnek soruların çözüm alanı boş ('ÇÖZÜM ...'); Bağlam Temelli etiketli örnekler",
           "Ürün sayfası 2 modül/fasikül yapısını ve örnek sayfa bağlantısını veriyor; baskı yılı yok",
       ],
       sample_evidence=[{"url": "https://numunekitap.com/paraf/11-sinif/11-sinif-mod-fizik-anlatim-fasikulu",
                         "what": "Yayınevinin herkese açık flipbook örneği, kapak ve s.11-21 görüntülendi (1. Bölüm Serbest Düşme: kavram sayfaları, hareket formülleri, "
                                 "düşey yukarı atış, grafik üçlüsü, Örnek/Sıra Sende, Bağlam Temelli tablo sorusu). Metin kaydedilmedi."}],
       family_mapping=[
           _fm("ff-upward-throw", "s.17: 'Düşey yukarı doğru ilk hızla atılan cisimler' başlığı, tepe noktası ve çıkış süresi notu"),
           _fm("ff-motion-graphs", "s.17: serbest düşme/yukarı atış için konum-hız-ivme zaman grafiklerinin şematik anlatımı"),
           _fm("ff-mass-independence", "s.11: farklı kütleli (pinpon topu, tenis topu, demir bilye) cisimlerin aynı anda düşüşünü gösteren şema ve kütleden bağımsızlık notu"),
           _fm("ff-data-evidence", "s.21 (Bağlam Temelli Örnek 8): robot/kütle/ivme tablosundan yalnız veriye dayalı çıkarım yapan öğrencinin yargılarını değerlendirme"),
       ],
       notes="Örnek bölüm yalnız 1. Bölüm (Serbest Düşme); diğer üniteler görülmedi. Maarif beyanı kapaktan (yayınevi beyanı).",
       confidence="HIGH"),

    _s(slug="paraf-2028-maarif-fizik-soru-bankasi", publisher="Paraf", title="Paraf 2028 Maarif Fizik Soru Bankası",
       kind="soru_bankasi", target="TYT", edition_year=None, maarif_claim=True,
       url="https://parafyayinlari.com/maarif-2028/paraf-2028-maarif-fizik-soru-bankasi", verified_by_fetch=True,
       question_styles=["BAGLAM_TEMELLI"], difficulty="karma",
       pedagogical_style="Basitten karmaşığa ilerleyen testler; bölüm sonu konu değerlendirme; 'Bağlam ve Beceri Temelli Testler' (gerçek yaşam senaryosu).",
       unique_characteristics=["Yayınevi sayfası: seri 2028 ÖSYM sınavını Maarif Modeli'ne göre hedefliyor", "Sayfada çoktan seçmeli, açık uçlu ve kısa cevaplı soru türleri sayılıyor"],
       notes="Kapsam 9-10. sınıf (TYT, 1. aşama) — 11. sınıf konularını İÇERMEZ; yalnız 2028 piyasa eğilimini göstermek için alındı. Baskı yılı sayfada yok. Örnek sayfa okunmadı.",
       confidence="MEDIUM"),
]

# ---------------------------------------------------------------------------------------------------------------
# 2) Okyanus 40 Seans (yayınevi sitesi + yayınevinin herkese açık örnek PDF'i okundu)
# ---------------------------------------------------------------------------------------------------------------
SOURCES += [
    _s(slug="okyanus-11-40-seans-fizik", publisher="Okyanus", title="11. Sınıf 40 Seans Fizik",
       kind="konu_anlatimi", target="11", edition_year=None, maarif_claim=True,
       url="https://okyanusyayincilik.com/Urun/20702/11.-s%C4%B1n%C4%B1f-40-seans-fizik", verified_by_fetch=True,
       question_styles=["BAGLAM_TEMELLI", "GRAFIK_TABLO", "KLASIK_ISLEM", "COK_ADIMLI"], difficulty="orta",
       pedagogical_style="40 'seans': Bilgi (kısa konu) > Etkinlik > Çözümlü Örnekler > 'Test Tekniği' kutuları > Test 1-2; seans testlerinde QR kodlu video çözüm; "
                         "ünite sonlarında 3 ayrı 'Bağlam Temelli Test' bölümü; çözümler kitap içinde.",
       unique_characteristics=[
           "Yayınevi ürün sayfası ve ön söz: Türkiye Yüzyılı Maarif Modeli'ne uygun, ÖSYM'nin son yıllardaki sorularından hareketle, 2028 YKS'yi hedefleyen bağlam temelli sorular",
           "Örnek PDF'te her test sorusu gerçek yaşam sahnesi (spor salonu, seyir kulesi, hava balonu, avcı, kartal) ve uzun bir hikâye cümlesiyle başlıyor; foto-gerçekçi çizimler",
           "'Test Tekniği' kutuları: 5-15-25-35 m kuralı, v-t grafiğinin altındaki alan gibi kısa yol yöntemleri",
           "İçindekiler 40 seansı 3 ünitede veriyor (Kuvvet ve Hareket 16 seans + Bağlam Temelli Test; Elektrik ve Manyetizma seans 17-28 + Bağlam Temelli Test; Optik seans 29-40 + Bağlam Temelli Test), cevap anahtarı s.291",
           "Tork/momentum/vektör/sığaç gibi eski müfredat başlıkları içindekilerde YOK; 296 sayfa",
       ],
       sample_evidence=[{"url": "https://b2b.okyanusyayincilik.com/Istem/PdfViewer/kitaplar/9786258823073.pdf",
                         "what": "Yayınevinin ürün sayfasından indirilen herkese açık 24 sayfalık örnek PDF (damgalı 'ÖRNEKTİR'): ön söz, içindekiler (40 seans), "
                                 "1. Seans Serbest Düşme-İlk Hızlı Hareket (bilgi, etkinlik, Test 1-2), 2. Seans başlığı ve Test 2, 3. Seans İki Boyutta İvmeli Hareket (Yatay) çözümlü örnekler. Soru metni kaydedilmedi."}],
       family_mapping=[
           _fm("ff-equal-interval-ratios", "s.6: 'Eşit zaman aralıklarında alınan yolların pratik özelliği' (h, 3h, 5h, 7h) şeması ve s.11 'Test Tekniği' kutusunda aynı kural"),
           _fm("ff-motion-graphs", "s.6: serbest düşme için konum-zaman, hız-zaman, ivme-zaman grafik üçlüsü"),
           _fm("ff-kinematics-v0zero", "s.6: t-hız-yol tablosu ve v=gt, h=gt²/2, v²=2gh denklemleri; ilk hızsız düşme"),
           _fm("ff-downward-throw-or-moving-carrier", "s.11, s.14-15 (Test 1-2): aşağı yönlü ilk hızlı atışlarda yükseklik/süre/hız soruları; s.21 hava balonundan bırakılan cisim"),
           _fm("ff-upward-throw", "s.21 (2. Seans, 'aşağıdan yukarıya düşey hareket'): yükselen balondan bırakılan cisim ve yukarı atılan top soruları"),
           _fm("2d-horizontal-launch", "s.22-24 (3. Seans): yatay atışta havada kalma süresi, menzil, çarpma hızı; 5-15-25 m kuralı ile çözüm"),
       ],
       notes="Baskı yılı sayfada yok. Örnek PDF 24 sayfa; 4. Seans sonrası (eğik atış, Newton, vb.) örnekte yok. Maarif beyanı ürün sayfası + ön sözden (yayınevi beyanı). "
             "Piyasa tarzının en belirgin 'foto-gerçekçi bağlam' örneği; ÖSYM sorularının sade şeması ile karşılaştırılırken bağlam yoğunluğu abartılı kabul edilmeli.",
       confidence="HIGH"),

    # ------------------------------------------------------------------------------------------------------------
    # 3) Limit — ESKİ baskı (yayınevinin dijital kataloğu okundu): eski müfredat riskinin doğrudan kanıtı
    # ------------------------------------------------------------------------------------------------------------
    _s(slug="limit-11-fizik-konu-anlatim-foyleri-eski", publisher="Limit", title="11. Sınıf Fizik Konu Anlatım Föyleri (eski baskı, 28 föy)",
       kind="konu_anlatimi", target="11", edition_year=2021, maarif_claim=None,
       url="https://fliphtml5.com/tsyqb/nmsg/11.SINIF_F%C4%B0Z%C4%B0K_KONU_ANLATIM_F%C3%96YLER%C4%B0/", verified_by_fetch=True,
       question_styles=["KLASIK_ISLEM", "KAVRAMSAL"], difficulty="orta",
       pedagogical_style="8 sayfalık konu föyleri; 'Örnek Konu' ve 'Sıra Sende' çiftleri, çözüm alanları, 'ÖSYM Sorusu' kutuları.",
       unique_characteristics=[
           "Kapakta '28 föy', 'Açıklı Teknikle Uyumlu', 'Video Çözümlü', 'Yeni Müfredata Uygun', 'Yeni Nesil Sorular' rozetleri (2021 müfredatına göre)",
           "Ünite 1 'Vektörler' ile açılıyor (bileşke vektör, uç uca ekleme, paralelkenar yöntemi, bileşenlere ayırma) — Maarif 11. sınıfta yok",
           "'ÖSYM Sorusu 2019 AYT' etiketli vektör sorusu",
       ],
       sample_evidence=[{"url": "https://fliphtml5.com/tsyqb/nmsg/11.SINIF_F%C4%B0Z%C4%B0K_KONU_ANLATIM_F%C3%96YLER%C4%B0/",
                         "what": "Limit Grup'un kendi dijital yayın kataloğu (flipbook, 225 s., 03.06.2021): kapak ve ilk 7 sayfa (Ünite 1 Vektörler) görüntülendi. Soru metni kaydedilmedi."}],
       family_mapping=[],
       old_curriculum_risk=True,
       notes="Bu kayıt YENİ Maarif föyü değil (yeni föy ayrı: limit-11-fizik-konu-anlatim-foyleri-yeni). Ürün künyesi (retailer): ISBN 9786052754160, 224 s., yazar Yener Yasun. "
             "edition_year dijital katalog yayın tarihidir (2021). Vektörler açılışı nedeniyle aile eşlemesi yapılmadı. Öğrencinin elinde bulunma olasılığı yüksek eski baskı örneği.",
       confidence="MEDIUM"),
]
