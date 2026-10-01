# 11. Sınıf Fizik (Maarif) ve AYT Fizik: Piyasa Kaynakları Envanteri

Hazırlanma tarihi: 30 Eylül 2026. Yalnızca künye/metadata; kitap içeriği kopyalanmamıştır.
Tam liste: `piyasa-kaynaklari.csv` (72 satır: 54 adet 11. sınıf, 18 adet AYT/2028).

## 0. Okumadan önce: doğrulama sınırları

Bu envanter sınırlı bir oturumda, web arama ve sayfa özetleme araçlarıyla çıkarıldı. Oturum kotası dolduğu için bazı doğrulamalar yarım kaldı.

- **En güvenilir katman:** kitapsec.com ürün sayfaları (yayınevi, ad, yazar, ISBN, sayfa sayısı, bazen baskı yılı), yayınevi sitesi sayfaları (Paraf), MEB/TYMM sayfaları.
- **Orta güvenilirlik:** askakitap.com ve kitapsec.com blog yazıları. Seviye ve "Maarif uyumlu" bilgileri çoğunlukla buradan; bunlar satıcı/blog beyanıdır.
- **Doğrulanamayan:** YouTube oynatma listeleri (YouTube sayfaları araçla okunamadı), forum yorumları (technopat 403 verdi, yalnızca arama özeti var), Karekök/Limit/Endemik yayınevi siteleri (erişilemedi).
- **Soru sayısı:** hiçbir 11. sınıf kitabı için sayfada soru sayısı yer almıyordu. CSV'de `bilinmiyor`. Yalnızca Çap Tematik için "101 test" bilgisi var (soru sayısı değil).
- **Seviye:** çoğu kitap için `bilinmiyor`. Dolu olanlar blog tahminidir, kitabı görmeden kesin kabul edilmemeli.
- **"Maarif uyumlu" sütunu** dört değerden birini alır:
  - `evet (başlıkta / yayınevi beyanı)`: kapakta veya başlıkta Maarif ifadesi var.
  - `örtük`: yeni ISBN bloğu (978-625-8...), 2026 listeleme kimliği veya "tematik/beceri temelli" gibi ifadeler var ama açık Maarif beyanı doğrulanamadı.
  - `doğrulanamadı`: listelemede beyan yok, baskı yılı bilinmiyor.
  - `hayır olası`: baskı yılı veya seri eski müfredata ait görünüyor.
  Bu çıkarımlar heuristiktir. Her kitap için yayınevi kataloğu veya fiziksel kapak ile teyit gerekir.

## 1. Bağlam: neyi hedefliyoruz

- 11. sınıf fizik, 2026-2027 öğretim yılında TYMM (Maarif) programıyla işleniyor. MEB sitesinde 11. sınıf fizik ders kitabı (TYMM) yayımlanmış, ücretsiz PDF var.
- MEB resmi programı (fizik-ogretim-programi-9-12.pdf, 19.08.2026, s. 10-11): 11. sınıfta **3 ünite, 33 öğrenme çıktısı**: Kuvvet ve Hareket (54 saat), Elektrik ve Manyetizma (48), Optik (36), okul temelli planlama (6); toplam 144 saat.
- Bazı blog/yayınevi siteleri 11. sınıfta "Madde ve Doğası" ünitesi (yarı iletkenlik, süper iletkenlik) gösteriyor; bu **yanlış/eskimiş** bilgi. Madde ve Doğası 12. sınıf ünitesidir (FİZ.12.4.x). Böyle bir kitap görülürse içerik 12. sınıf kapsamına aittir.
- 2028 YKS: TYT 9-10, AYT 11-12 içeriği. ÖSYM, Temmuz 2026 itibarıyla kesin konu/soru dağılımını yayımlamamıştı (kitapsec ve askakitap blogları böyle aktarıyor). Soru tipinin metin, veri seti, grafik, deney sonucu, gerçek yaşam problemi gibi bağlamlı/beceri temelli olması bekleniyor.
- **Önemli bulgu:** "2028 Maarif" etiketli kitapların neredeyse tamamı **1. aşama (9-10. sınıf, TYT)** kapsamlı (Çap, Paraf, Bilgi Sarmal, Orijinal, Altuğ Güneş 1. Oturum). 11-12. sınıf AYT'ye dönük "2. aşama" Maarif kitaplarının piyasada yaygınlaştığına dair doğrulanmış kayıt bulunamadı. Mevcut **AYT fizik soru bankalarının büyük kısmı 2027 (eski müfredat)** kitaplarıdır. Bu, öğrencinin getireceği fotoğrafların bir kısmının eski müfredat/eski tarz soru olacağı anlamına gelir.

## 2. 11. sınıf fizik kitapları (Maarif dönemi)

Fiyatlar kitapsec (Eylül 2026) listelemesinden; burada tutulmadı, güncelliğini hızla kaybeder.

### 2.1 Maarif beyanı açık (başlıkta) olanlar

| Yayınevi | Kitap | Tür | Baskı | Not (künye/öne çıkan özellik) | Yapay zekâ notu |
|---|---|---|---|---|---|
| Bilgi Sarmal | 11. Sınıf Fizik Maarif Soru Bankası | soru bankası | 2026 | Ümit Akça, Cenk Çayırcıoğlu; ISBN 9786256712775; ~336 s; didaktik, ünite, YKS beceri temelli, sarmal testler; akıllı kağıtlar; video çözüm | Karışık: klasik işlem soruları + kısa bağlamlı "beceri temelli" testler. Sarmal (tekrarlı) test yapısı nedeniyle aynı kazanımın farklı zorluklarıyla karşılaşılır. |
| Sonuç | 11. Sınıf Fizik Maarif Modele Uygun SB Modüller Set | soru bankası (modül) | 2026 | ISBN 9786258203950; "Sonuç Komisyon" | Okul destekli, temel-orta; büyük olasılıkla kazanım odaklı klasik + orta uzunlukta bağlam. |
| Miray | 11. Sınıf Fizik Maarif Model Tematik Soru Bankası | soru bankası (tematik) | bilinmiyor | Yazar Mustafa Demir (arama özeti) | Tematik (ünite yerine tema) düzen: soruların bir teması var, ardışık sorular aynı senaryoyu paylaşabilir. |
| Fizipedia | 11. Sınıf Fizik Maarif Model Soru Bankası | soru bankası | bilinmiyor | Maarif beyanı başlıkta | Yayınevi AYT'de zor/özgün soru ile anılıyor (blog); bu kitapta da çok aşamalı, uzun bağlamlı sorular beklenmeli (teyitsiz). |
| Çap | 11. Sınıf Fizik Maarif Model Set 2028 | set | bilinmiyor | Yalnız arama başlığı; sayfa doğrulanamadı | Doğrulanana kadar varsayım yapma. |
| Karekök | 11. Sınıf Maarif Modeline Uygun Mat-Geo-Fizik-Kimya-Biyoloji TYT Hazırlık SB | çok dersli set | bilinmiyor | Fizik bölümü tek başına kitap değil | Kısa, TYT tarzı sorular; 11. sınıf derinliği sınırlı olabilir. |

### 2.2 Maarif'e göre hazırlandığı örtük / muhtemel olanlar (yeni ürün, 2026)

| Yayınevi | Kitap | Tür | Not | Yapay zekâ notu |
|---|---|---|---|---|
| Bilgi Sarmal | 11. Sınıf Fizik Tema Konu Anlatım Modülleri | konu anlatımlı modül | 2026; 368 s; ISBN 9786256712829 | Anlatım kitabı: soru fotoğrafı yerine "örnek soru + çözüm" sayfaları gelir. Tema adları (ör. Kuvvet ve Hareket teması) MEB ile aynı dilde. |
| Palme | 11. Sınıf Fizik Joker Tematik Soru Kitabı | soru bankası (tematik) | 360 s; ISBN 9786258542677 | Tematik düzen, muhtemelen bağlam ağırlıklı. |
| Hız ve Renk | 11. Sınıf Fizik HİT Soru Bankası | soru bankası | 304 s; ISBN 9786258715194 | Hız ve Renk AYT'de orta düzey pratik çözümle anılıyor (blog). |
| Orijinal | Orijinal Mikro 11. Sınıf Fizik MÖF Set | fasikül (öğreten) | 416 s; ISBN 9786255708656; Engin Aydın, Zeynep Uslu | Forumlarda Bilgi Sarmal/Çap ile birlikte sık önerilen "öğreten" fasikül. Anlatım + örnek soru; klasik temel soru + kavramsal sorular. |
| Limit | 11. Sınıf Fizik Konu Anlatım Föyleri (yeni baskı) | föy | 304 s; Mesut Aksoy; ISBN 9786052758281; ÖSYM soruları, klasik ve beceri temelli etkinlikler, kazanım testleri | Föy formatı: 8 sayfalık konu föyleri, fotoğrafta tablo/etkinlik şablonları görülebilir. |
| Nitelik | 11. Sınıf Fizik Beceri Temelli Soru Kitabı | soru bankası | 264 s; ISBN 9786052724873 | Adı gereği beceri temelli: uzun bağlam, yorumlama, veri okuma. |
| Kafadengi | 11. Sınıf Fizik Extra SB | soru bankası | ISBN 9786256333680; Ömer Öztel | Bilinmiyor. |
| ProFizik | 11. Sınıf Fizik Konu Anlatımlı Soru Kitabı | konu anlatımlı + soru | 432 s; ISBN 9786259369822; Musa Özdemir, Erdal Aras | Konu + soru karışık. |
| Paraf | 11. Sınıf IQ Fizik Soru Kütüphanesi | soru bankası | ISBN 9786258584400 | Yayınevi sitesinde "YENİ". |
| Paraf | 11. Sınıf MOD Fizik Anlatım Fasikülü | fasikül | ISBN 9786258584813 | Yayınevi sitesinde "YENİ". |
| Armada | 11. Sınıf Görev Fizik Yeni Nesil Çalışma Föyleri (36 Hafta) | föy | haftalık program | Haftalık föy, kısa-orta uzunlukta yeni nesil sorular. |
| ENS | 11. Sınıf Fizik Defter Kitap | konu anlatımlı | yeni ID | Defter tarzı not sayfası: elle yazılmış benzeri düzen, OCR için farklı. |
| Aydın | 11. Sınıf Fizik SB ve Ders İşleyiş Modülleri | soru bankası / modül | ISBN 9786057710185 ve 9786057710192 (eski ISBN bloğu) | Maarif uyumu doğrulanamadı; yeni baskı mı eski baskı mı belirsiz. |

### 2.3 Maarif durumu doğrulanamayan (listelemede var, beyan yok)

Palme Konu Anlatımlı ve Fen Liseleri Konu Anlatımlı, Palme Yaprak Test, Karekök MPS Konu Anlatımı, Karekök 11 Fizik SB, Limit 11 Fizik SB (Yener Yasun, 272 s, QR video çözüm; 10. sınıf için "Etkinlikli Maarif SB" var, 11. için bulunamadı), Çap Anadolu Lisesi SB (askakitap Maarif uyumlu diye öneriyor; teyitsiz) ve Çap Fen Lisesi SB (303 s; tam video çözüm, hibrit yeni nesil testler; fen lisesi), Sonuç Modüler Set, Nitelik Konu Anlatımlı, Armada Görev Fizik Konu Kitabı ve Süper Fizik, Okyanus Iceberg SB, Tammat Origami Fizik Koçu SB, Fen Bilimleri Yayıncılık SB, Tudem SB, Pegem SB ve Konu Anlatımı, EİS Ders Anlatım Föyü, Gür Öğreten Fizik Seti, Yanıt Yes Serisi, Derece Modüler Set, Sınav Yayınları SB, Editör Özetli Lezzetli SB, Endemik 2025-2026 SB, Apotemi Çap çok dersli set. Künye ve URL'ler CSV'de.

### 2.4 Eski müfredata ait olması olası (öğrenci getirebilir)

- Nihat Bilgin 11. Sınıf Fizik SB (2018 baskı, 368 s), Esen 11. Sınıf Fizik Konu Anlatımlı (2019, 624 s), Özdebir Fizik Branş Deneme (2021/2024), Miray Konu Özetli SB, Paraf eski Soru Kütüphanesi (tükendi), Sonuç Elektrik-Manyetizma SB, Ertan Sinan Şahin 11. Sınıf Fizik Seti (2022 baskı kitap; set 1 Eylül 2026'ya kadar geçerli).
- Not: askakitap yarı iletken/süper iletkenliği 11. sınıfa ekliyor; resmi programa göre bunlar 12. sınıftadır. Eski kitapların öğrenme çıktısı/konu sıralaması da TYMM ile birebir örtüşmeyebilir (örtüşme farkları bu taramada kitap kitap doğrulanmadı). Yapay zekâ, fotoğraftaki sorunun kapsam ve dilinden eski müfredat şüphesi duyarsa öğrenciyi uyarmalı.

## 3. AYT ve 2028 Maarif kitapları

| Yayınevi | Kitap | Kapsam | Maarif | Not |
|---|---|---|---|---|
| Çap | 2028 YKS TYT AYT Fizik Ders Platosu Maarif Tematik SB 1. Aşama | 9-10 içeriği | evet (yayınevi beyanı: "%100 uyumlu") | 208 s; 101 test (81 tematik + 20 karma); Metin Çengel, Bayram Tükenmez; video çözümler; "100% Maarif uyumlu" beyanı yayınevinindir, doğrulanmamıştır |
| Paraf | 2028 Maarif Fizik SB; Konu Anlatımı 1. ve 2. Modül | SB: 9-10 | evet | ISBN 9786255506948; bağlam ve beceri temelli testler, kolaydan zora |
| Bilgi Sarmal | 2028 YKS TYT AYT Fizik Maarif Modeli İlk Aşama SB | 9-10 | evet | |
| Orijinal | Fizik SB 2028 Maarif Model 1. Aşama | 9-10 | evet | |
| KR Akademi / Altuğ Güneş | 2028 Maarif 1. Oturum Fizik Video Ders Kitabı | 9-10 | evet | video anlatımlı |
| 345 | 2027 AYT Fizik SB | 11-12 (eski müfredat) | hayır | 392 s; Ümit Akıncı; tamamı video çözümlü; ÖSYM'ye yakın; 47.715+ satış; askakitap AYT'de "zor" sınıfında |
| 3D, Çap (Plus), Egzersiz, MF Kazanım, Apotemi, Aydın, Benim Hocam, Fizipedia, ENS, Hız ve Renk, Bilgi Sarmal AYT SB | AYT Fizik SB'ler | 11-12 (eski müfredat) | hayır olası | askakitap "2027 AYT Fizik Kaynak Önerileri" özeti: ENS ve Çap Plus kolay-orta, Benim Hocam kolay, Hız ve Renk orta, 3D orta-zor, Bilgi Sarmal orta-zor, 345 ve Fizipedia zor. Bu seviye dizilimi blog özetidir, kendim doğrulamadım. |
| Altuğ Güneş | AYT Fizik 2. Kitap (11. sınıf konuları, video) | 11. sınıf | hayır olası | |
| Apotemi | Modern Fizik | AYT modern fizik | hayır olası | Yeni 12. sınıf "Madde ve Doğası" (FİZ.12.4.x) ile kısmen örtüşebilir |

Sonuç: 2028 AYT'ye (11-12) yönelik **Maarif 2. aşama** kitapları bu tarama tarihinde doğrulanamadı. Bu, veri setimiz için bir boşluktur: 12. sınıf 2027-28'de bu kitapların çıkması beklenmeli; ÖSYM örnek soruları ve MEB yayınları bu dönem için daha güvenilir kaynak.

## 4. Kitap türüne göre yapay zekâ için genel not

Kitap kitap değil tür bazında, çünkü çoğu kitabın içini görmedik.

| Tür | Öğrencinin getireceği soru tarzı | Yapay zekâ yaklaşımı |
|---|---|---|
| Klasik soru bankası (eski seri) | Sayısal işlem yoğun, kısa metin, tek adımlı veya iki adımlı | Formül ve birim kontrolü; eski müfredat uyarısı |
| Tematik / beceri temelli (Maarif) | Uzun bağlam (ulaşım, enerji, elektrikli araç, spor), grafik/tablo/deney verisi, "hangisi söylenebilir?" tarzı çoklu öncül | Önce verilenleri ve bağlamı yapılandır, sonra ilkeyi bul; şıkları eleme |
| Konu anlatımı / fasikül / föy | Örnek sorular, boşluk doldurma, etkinlik | Anlatımdaki terimle tutarlı ol (TYMM kazanım dili) |
| Yaprak test, branş deneme | Kısa testler, süreli | Çözüm süresi ve hata analizi |
| Fen lisesi kitapları | Daha yüksek soyutlama, çok adımlı | Adım adım, kavramsal zemin |

## 5. Ücretsiz dijital kaynaklar

### 5.1 MEB ve resmi

| Kaynak | Ne var | URL | Doğrulama |
|---|---|---|---|
| TYMM 11. Sınıf Fizik Ders Kitabı | Ücretsiz PDF, Maarif ders kitabı (sayfa son güncelleme 07.09.2026) | https://tymm.meb.gov.tr/kitap/404/fizik-dersi-11sinif-ders-kitabi | Doğrulandı |
| TYMM Fizik Öğretim Programı 11. Sınıf | Kazanım listesi, ünite yapısı | https://tymm.meb.gov.tr/ogretim-programlari/fizik-dersi/13 | Arama sonucunda görüldü |
| MEB Fizik Programı PDF (2024) | Program metni | https://mufredat.meb.gov.tr/Dosyalar/202582694751283-fizik.pdf | Arama sonucunda görüldü |
| MEBİ | Ücretsiz bireysel öğrenme platformu: YKS denemeleri, tarama testleri, çıkmış soru kitapları | https://mebi.eba.gov.tr/ | Arama özeti; 11. fizik içeriğinin Maarif'e göre güncelliği doğrulanamadı |
| OGM Materyal (EBA) | 11. sınıf fizik etkileşimli kitaplar, ders sunuları, kazanım kavrama etkinlikleri | https://ogmmateryal.eba.gov.tr/etkilesimli-kitap/fizik?s=8&d=34&u=0&k=0 | Arama sonucunda görüldü |
| ÖDSGM Kazanım Testleri | 11. sınıf fizik kazanım testleri (2022-2023, eski müfredat) | https://odsgm.meb.gov.tr/www/11-sinif-fizik-kazanim-testleri-2022-2023/icerik/886 | Eski müfredat |

### 5.2 YouTube kanalları (Maarif 11. sınıf oynatma listesi doğrulanamadı)

YouTube sayfaları araçla okunamadı. Aşağıdakiler kanalın varlığını ve genel içeriğini gösteren arama sonuçlarıdır. "11. sınıf Maarif listesi var mı" sorusu için **hepsi doğrulanamadı**.

| Kanal | Öğretmen | Not | URL |
|---|---|---|---|
| Fizikfinito | Didar Baskın (ODTÜ Fizik Öğretmenliği, 2016) | TYT/AYT ve lise fizik anlatımları; arama sonucunda "11. sınıf yeni müfredat" videoları görüldü (ör. "6) 11. Sınıf Yeni Müfredat Fizik"; kanal sahibi doğrulanmadı) | https://www.youtube.com/@Fizikfinito |
| Altuğ Güneş FİZİK | Altuğ Güneş | TYT/AYT, video ders kitapları; "11. Sınıf Fizik Güncel Konu Anlatımı #2023" listesi görüldü (eski müfredat) | https://www.youtube.com/@altuggunesfizik |
| FizMat Serhat | Serhat (soyadı doğrulanmadı) | 9-10-11. sınıf okul müfredatı videoları, YouTube kampları | https://www.youtube.com/c/fizmatserhat |
| Benim Hocam Lise | doğrulanmadı | 9-10-11. sınıf | https://www.youtube.com/@benimhocamlise |
| Umut Öncül Akademi | Umut Öncül (ODTÜ Fizik Öğretmenliği) | TYT/AYT listeleri, PDF notlar | https://www.youtube.com/user/umutoncul |
| Ahmetle Fizik | Ahmet (öğrenci/YKS içerik üreticisi) | TYT-AYT konu ve soru çözümü (Çap 2028 kitabı video çözüm kanalı olarak anılıyor) | https://www.youtube.com/@ahmetlefizik |
| Ertan Sinan Şahin | Ertan Sinan Şahin | Çoğu içerik ücretli set; sitede 345/MF Kazanım AYT çözüm PDF ve YouTube listeleri var | https://ertansinansahin.com/ |
| "11. SINIF FİZİK MEB KİTABI (ATA YAY)" | doğrulanmadı | MEB (eski/yeni?) 11. sınıf kitabı çözümleri | https://www.youtube.com/playlist?list=PL5Tyg7PG_93q9H9G98l4bjs87A8dapXeH |

Not: "Ahmetle Fizik" ve "Fizmat Serhat", Çap'ın kitap sayfasında video çözüm kanalı olarak anılıyor. Bu, Çap serisi sorularının video çözümlerinin kamuya açık olabileceğini gösterir; ürün tasarımında "video çözüm var mı" bilgisi kullanıcıya yönlendirme olarak değerlendirilebilir (iç telif değerlendirmesi ayrı).

### 5.3 Ücretsiz PDF/test siteleri

Kesin bir liste çıkarılamadı. Arama sonuçlarında scribd.com, dokumen.pub ve fliphtml5.com üzerinde yayınevi kitaplarının (Limit, Miray, Sınav, Aydın, 345) **yetkisiz olması olası** PDF kopyaları görüldü. Bunlar envantere alınmadı ve ürün için kaynak olarak kullanılması önerilmez. Yasal dijital örnekler: yayınevi "örnek sayfa" sayfaları (numunekitap.com, Paraf, Özdebir Dijital, Sınav Digital), MEB/EBA içerikleri.

## 6. Telif ve lisans notu (genel bilgi, hukuki tavsiye değildir)

Aşağıdaki açıklamalar Türkiye'deki 5846 sayılı Fikir ve Sanat Eserleri Kanunu (FSEK) hakkında genel bilgidir. Bir avukat görüşü yerine geçmez; ürün kararı öncesi fikri mülkiyet avukatına danışılmalıdır.

**Soruların veritabanına konması**
- Soru bankası soruları, çözümleri, şekilleri ve kitabın derlenme/düzeni FSEK kapsamında eser (ilim ve edebiyat eseri, bazen derleme eser) olarak korunabilir. Hak sahibi genellikle yazar veya yayınevidir (eser sahibi, hakları yayınevine devretmiş olabilir).
- Soruları kopyalayıp veritabanına koymak, çoğaltma (md. 22), işleme (md. 21) ve umuma iletim (md. 25) haklarıyla ilgili olur. Bunun için hak sahibinden **yazılı lisans/izin** gerekir. Pratikte: yayınevi ile lisans sözleşmesi (kapsam: soru metni, şekil, çözüm; süre; ürün; bölge; yapay zekâ eğitimi/retrieval ayrımı; ücret; atıf).
- "Yapay zekâ eğitimi" ve "çıktıda gösterme" ayrı izin konularıdır; sözleşmede ayrı yazılmalıdır.
- Soruyu "kendimiz yeniden yazdık" yaklaşımı (sorunun özgün soru kalıbını, sayılarını, bağlamını kopyalayıp hafifçe değiştirmek) işleme sayılma riski taşır. Özgün soru üretimi, MEB kazanımlarından ve kamuya açık kaynaklardan (ÖSYM/MEB soruları için ayrıca kendi koşullarına bakılmalı) yapılmalıdır.
- MEB ders kitapları ve MEB yayınları için ayrı kullanım koşulları vardır (çoğu serbest erişimli ama yeniden dağıtım şartları kontrol edilmeli).

**Öğrencinin kendi kitabından fotoğraf çekip sorması**
- Öğrencinin kendi satın aldığı kitaptan tek bir soruyu kişisel öğrenme amacıyla fotoğraflaması, üründe kalıcı bir soru arşivi oluşturmaz. Kitabı hukuka uygun edinen kişi açısından kişisel kullanım, eğitim amaçlı küçük alıntı ve FSEK'teki sınırlamalar (ör. md. 30 kişisel kullanım amacıyla sınırlı çoğaltma, md. 34 alıntı) gündeme gelir. Bu, genel bir tartışmadır; kesin sonuç olay bazındadır.
- Farklı olan: ürün, öğrencinin tek seferlik, kendi isteğiyle gönderdiği girdiyi işler; ürün kitabı dağıtmaz, soruyu başkalarına göstermez.
- **Dikkat edilmesi gereken riskler:** (a) öğrenci fotoğraflarının ürün tarafından kalıcı olarak saklanıp veritabanına/eğitim verisine dönüştürülmesi, yayınevi lisansı olmadan aynı kopyalama sorununa yol açar; (b) yapay zekânın çözümde soruyu veya kitabın çözüm metnini birebir tekrar etmesi; (c) fotoğrafta çok sayıda sayfa/tüm kitap gönderilmesi; (d) kişisel veriler (KVKK) ve öğrenci fotoğraflarında yüz/ad gibi veriler.
- Önerilen ilke: fotoğraftan OCR ile soruyu işle, çözümü yapay zekâ üretsin (kitabın çözümünü kopyalamasın), fotoğrafı/soru metnini oturum dışında saklama, kitap içeriğini model eğitimine alma; saklanacaksa açık rıza ve yayınevi lisansı.

## 7. Doğrulanamayanlar ve yapılacaklar

1. "Maarif uyumlu" bilgisi çoğu kitap için satıcı beyanı veya çıkarım. Yayınevi kataloglarından (özellikle Karekök, Limit, Endemik, Palme, Aydın, 345, Apotemi, 3D, Acil) teyit edilmeli. **345, 3D, Apotemi, Acil, Esen, Özdebir, Endemik için 11. sınıf Maarif baskısı bu taramada bulunamadı.**
2. Baskı yılı ve soru sayısı çoğu kitap için yok; fiziksel kitap veya yayınevi PDF kataloğu gerekir.
3. YouTube Maarif 11. sınıf oynatma listeleri hiçbir kanal için doğrulanamadı.
4. Acil, Esen (Maarif), Apotemi (11. fizik tek başına), 3D (11. sınıf), 345 (11. sınıf): ya yok ya da bulunamadı. Ertan Sinan Şahin'in 11. sınıf seti eski (2022 baskı).
5. Tarama oturum kotası nedeniyle yarıda kesildi: Çap 11 Maarif seti, Fizipedia ve Miray Maarif kitaplarının ürün sayfaları doğrulanamadı; YouTube kanal sayfaları, forumlar (eksisozluk, technopat içerikleri) okunamadı.

## 8. Başlıca kaynak URL'leri

- https://www.kitapsec.com/Products/11-Sinif-Yardimci-Kitaplar/11-Sinif-Fizik/ (47 ürün listesi)
- https://askakitap.com/blog/11-sinif-hangi-test-kitabi-alinmali-maarif-modeli
- https://askakitap.com/blog/ayt-fizik-kaynak-onerileri
- https://askakitap.com/blog/maarif-modeli-nedir-kademeli-gecis-takvimi-2028-sinav-rehberi
- https://askakitap.com/maarif-modeli-soru-bankasi
- https://askakitap.com/cap-yayinlari-fizik-tematik-soru-bankasi-maarif-modeli
- https://www.kitapsec.com/blog/ayt-maarif-modeli-fizik-konulari-281.html
- https://www.kitapsec.com/blog/maarif-modelinde-yks-nasil-olacak-2028-rehberi-289.html
- https://sinavhanem.com/11-sinif-fizik-kaynak-onerileri/
- https://parafyayinlari.com/11-sinif
- https://parafyayinlari.com/maarif-2028
- https://www.indekskitap.com/urun/cap-yayinlari-yks-tyt-ayt-fizik-ders-platosu-maarif-modeli-tematik-soru-bankasi
- https://tymm.meb.gov.tr/kitap/404/fizik-dersi-11sinif-ders-kitabi
- https://tymm.meb.gov.tr/ogretim-programlari/fizik-dersi/13
- https://ertansinansahin.com/11-sinif-fizik-konulari/
- Ürün düzeyindeki URL'ler `piyasa-kaynaklari.csv` içinde.
