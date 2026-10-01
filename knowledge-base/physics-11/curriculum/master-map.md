# 11. Sınıf Fizik — Müfredat Ana Haritası

> Otomatik üretildi: `scripts/build_curriculum.py`. Elle düzenleme yapma; betiği değiştirip yeniden çalıştır.

- **Müfredat sürümü:** `TYMM-FIZIK-OP-2026-08-19`
- **Birincil kaynak:** MEB TYMM Fizik Dersi Öğretim Programı (9, 10, 11 ve 12. Sınıflar), PDF, tymm.meb.gov.tr, 19.08.2026 (`src-meb-fizik-op-2026`)
- **İkincil kaynak:** tymm.meb.gov.tr 11. sınıf ünite sayfaları, güncelleme 05.08.2026
- **Doğrulama:** 33 öğrenme çıktısı ve tüm süreç bileşenleri PDF ile web sayfası arasında birebir karşılaştırıldı; metin farkı 0.

## Özet

| # | Ünite | Ders saati | Öğrenme çıktısı | Süreç bileşeni | İçerik başlığı |
|---|---|---|---|---|---|
| 1 | KUVVET VE HAREKET | 54 | 10 | 25 | 6 |
| 2 | ELEKTRİK VE MANYETİZMA | 48 | 13 | 34 | 4 |
| 3 | OPTİK | 36 | 10 | 26 | 8 |
| | Okul temelli planlama | 6 | | | |
| | **Toplam** | **144** | **33** | **85** | **18** |

Hiyerarşi: **Ünite → İçerik başlığı → Öğrenme çıktısı → Süreç bileşeni**. Öğrenme çıktısı → içerik başlığı eşlemesi programda açıkça verilmez; başlık adlarından türetildi (güveni her çıktıda belirtildi).

---

## Ünite 1: KUVVET VE HAREKET (54 ders saati)

**Amaç (resmî):** Bu ünitede öğrencilerin serbest düşmeye yönelik matematiksel hesaplamaları yapmaları, matematiksel modelleri ve grafiksel dönüşümleri iki boyutta sabit ivmeli harekete yönelik problem durumlarına çözüm getirmek için kullanabilmeleri, Newton'ın Hareket Yasalarını açıklamaları, bir cisme etki eden kuvvetleri serbest cisim diyagramında göstermeleri, statik ve kinetik sürtünme kuvvetinin bağlı olduğu değişkenleri gözlemleyerek sürtünme kuvvetinin matematiksel modelini oluşturmaları, limit hızı tanımlamaları ve limit hıza ait değişkenleri belirlemeleri, çembersel hareketin temel kavramları arasındaki ilişkileri açıklamaları amaçlanmaktadır.

**Temel kabuller (resmî, bağlayıcı):** Öğrencilerin hız, ivme ve ağırlık kavramlarını bildikleri, ilgili hesaplamaları yapabildikleri, periyot ve frekans kavramlarını bildikleri kabul edilmektedir.

**Beceriler (resmî):**

- Alan becerileri: FBAB8. Bilimsel Çıkarım Yapma, FBAB10. Tümevarımsal Akıl Yürütme, FBAB12. Kanıt Kullanma
- Kavramsal beceriler: KB2.7. Karşılaştırma, KB2.14. Yorumlama, KB2.16. Muhakeme (Akıl Yürütme) (KB2.16.3. Analojik Akıl Yürütme)
- Eğilimler: E1.2. Bağımsızlık, E1.3. Azim ve Kararlılık, E1.6. Seçicilik, E2.5. Oyunseverlik, E3.1. Muhakeme, E3.2. Odaklanma, E3.3. Yaratıcılık, E3.5. Açık Fikirlilik, E3.6. Analitiklik, E3.10. Eleştirel Bakma
- Sosyal-duygusal: SDB1.1. Kendini Tanıma (Öz Farkındalık), SDB2.1. İletişim, SDB2.2. İş Birliği, SDB2.3. Sosyal Farkındalık
- Değerler: D3. Çalışkanlık, D4. Dostluk, D12. Sabır, D14. Saygı
- Okuryazarlık: OB4. Görsel Okuryazarlık, OB7. Veri Okuryazarlığı, OB9. Sanat Okuryazarlığı
- Disiplinler arası: Astronomi ve Uzay Bilimleri, Beden Eğitimi, Görsel Sanatlar, Matematik
- Beceriler arası: KB2.3. Özetleme, KB2.18. Tartışma, KB3.2. Problem Çözme

**Anahtar kavramlar (resmî):** serbest düşme, eylemsizlik, etki-tepki kuvvetleri, serbest cisim diyagramı, sürtünme kuvveti, statik sürtünme kuvveti, kinetik sürtünme kuvveti, limit hız, düzgün çembersel hareket, çizgisel sürat, açısal hız, çizgisel hız, merkezcil ivme, açısal ivme, merkezcil kuvvet

### Serbest Düşme

- **FİZ.11.1.1** Serbest düşme hareketi yapan cisimlerin ivmesine yönelik tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 1.1.1 (s. 16)
  - a) Serbest düşme hareketi yapan cisimleri gözlemleyerek ivme ve hız değişimleri arasındaki ilişkiyi bulur. `[FBAB10.SB1]`
  - b) Serbest düşme hareketi yapan cisimlerin ivmesi hakkında genelleme yapar. `[FBAB10.SB2]`
  - ⚠️ `ASSUMPTION` _Öğretmen video, animasyon ya da simülasyon gibi dijital içeriklerden birini kullanarak hava direncinin ihmal edildiği ortamda serbest düşen farklı kütleli cisimlere örnek olacak görselleri hazır veri seti ile ilişkilendirerek sunar._ → Hava direnci yok sayılır.
  - ⚠️ `ASSUMPTION` _Yer çekimi ivmesi sabit kabul edilir._ → g yükseklikle değişmez.
- **FİZ.11.1.2** Serbest düşme hareketi ile ilgili kanıt kullanabilme — beceri `FBAB12` · ders kitabı 1.1.2 (s. 20)
  - a) Serbest düşme hareketi ile ilgili verileri toplayarak kaydeder. `[FBAB12.SB1]`
  - b) Serbest düşme hareketi ile ilgili veri setleri oluşturur. `[FBAB12.SB2]`
  - c) Serbest düşme hareketini verilere dayalı olarak açıklar. `[FBAB12.SB3]`
  - ⚠️ `SCOPE_INCLUDED` _Öğrenciler, deney ya da dijital içerikler yolu ile düşey doğrultuda ilk hızı sıfır olan ve ilk hızı sıfırdan farklı olan serbest düşen cisimlerin hareketlerini gözlemleyerek hız, ivme, konum, zaman ve yer değiştirme ile ilgili verileri toplayıp kaydeder._ → İlk hızlı (aşağı/yukarı) düşey hareket de serbest düşme kapsamında.
  - ⚠️ `ASSUMPTION` _Hava direncini ihmal ederek hız, ivme, konum, yer değiştirme ve zaman değişkenleri ile ilgili veri setleri oluşturur._ → Hava direnci yok sayılır.
  - ⚠️ `SCOPE_INCLUDED` _Ön öğrenmelerindeki ivmeli hareket grafiklerini dikkate alarak oluşturduğu veri setleri üzerinden hız-zaman, ivme-zaman ve konum-zaman grafiklerini çizer._ → Üç hareket grafiği ve aralarındaki dönüşüm kapsamda.
  - ⚠️ `TERMINOLOGY` _Hareket türü ifade edilirken serbest düşmenin sadece yer çekimi etkisindeki tüm hareketlerin ortak adı olduğu vurgulanır ve ‘’düşey atış hareketi’’ şeklinde hareket türü tanımından kaçınılır._ → 'Düşey atış' adı kullanılmaz; hepsi 'serbest düşme'.

### İki Boyutta Sabit İvmeli Hareket

- **FİZ.11.1.3** İki boyutta sabit ivmeli hareket ile ilgili tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 1.2 (s. 30)
  - a) İki boyutta sabit ivmeli hareketin bileşenleri ile sabit hızlı ve sabit ivmeli hareket arasındaki ilişkiyi bulur. `[FBAB10.SB1]`
  - b) İki boyutta sabit ivmeli harekete yönelik genelleme yapar. `[FBAB10.SB2]`
  - ⚠️ `SCOPE_INCLUDED` _Öğrenciler, yalnızca yer çekimi ivmesi etkisi altında iki boyutta sabit ivmeyle hareket eden cisimlerin hareketini gözlemler._ → İki boyutlu hareketin ivmesi yalnız g; başka sabit ivme kaynağı yok.
  - ⚠️ `SCOPE_INCLUDED` _Öğretmen, öğrencilerin trigonometrik hesaplamalara yönelik ön bilgisini hatırlatarak hız vektörünün bileşenlerinin trigonometrik hesaplamalar ile bulunabileceğine yönelik farkındalık kazandırır._ → Hız bileşenleri trigonometriyle bulunur.
  - ⚠️ `TERMINOLOGY` _‘’Yatay atış” ve “eğik atış” şeklinde hareket türü tanımından kaçınılır._ → 'Yatay atış' ve 'eğik atış' adları kullanılmaz.
  - ⚠️ `CALC_INCLUDED` _Yazılı yoklama ile öğrencilerin iki boyutta sabit ivmeli harekete yönelik matematiksel hesaplamalar ve grafiklere dayalı yorumlar yapmaları istenir._ → Sayısal hesap ve grafik yorumu ölçülür.

### Newton'ın Hareket Yasaları

- **FİZ.11.1.4** Newton'ın Hareket Yasaları ile ilgili tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 1.3.1 (s. 40)
  - a) Bileşke kuvvet ile cisimlerin hareketi arasındaki ilişkileri keşfeder. `[FBAB10.SB1]`
  - b) Newton'ın Hareket Yasalarına yönelik genellemeler yapar. `[FBAB10.SB2]`
- **FİZ.11.1.5** Newton'ın Hareket Yasalarını serbest cisim diyagramını kullanarak yorumlayabilme — beceri `KB2.14` · ders kitabı 1.3.2 (s. 53)
  - a) Bir cisme etki eden kuvvetleri belirler. `[KB2.14.SB1]`
  - b) Bir cisme etki eden kuvvetleri serbest cisim diyagramı üzerinde gösterir. `[KB2.14.SB2]`
  - c) Serbest cisim diyagramını kullanarak Newton'ın Hareket Yasalarını yeniden ifade eder. `[KB2.14.SB3]`
  - ⚠️ `CALC_LIMITED` _Farklı büyüklükteki ivmeyle hareket eden cisimlerin bir arada olduğu sistemlerle ilgili matematiksel hesaplamalardan kaçınılır._ → Bağlı sistemlerde tüm cisimler aynı ivmeyle hareket eder; farklı ivmeli sistem hesaplanmaz.
  - ⚠️ `CALC_LIMITED` _Sabit ivmeli hareket ile sınırlı kalınır._ → Değişken ivmeli dinamik yok.

### Sürtünme Kuvveti

- **FİZ.11.1.6** Statik ve kinetik sürtünme kuvvetlerini karşılaştırabilme — beceri `KB2.7` · ders kitabı 1.4.1 (s. 65)
  - a) Statik ve kinetik sürtünme kuvvetlerine ilişkin özellikleri belirler. `[KB2.7.SB1]`
  - b) Statik ve kinetik sürtünme kuvvetlerine ilişkin benzerlikleri listeler. `[KB2.7.SB2]`
  - c) Statik ve kinetik sürtünme kuvvetlerine ilişkin farklılıkları listeler. `[KB2.7.SB3]`
  - ⚠️ `SCOPE_INCLUDED` _Öğretmen, örnek olay ya da dijital içeriklerde yer alan görselleri yorumlayarak öğrencilerin harekete zorlanmasına rağmen durmakta olan, kayarak öteleme hareketi yapmakta olan ve dönerek öteleme hareketi yapmakta olan cisimlere etki eden sürtünme kuvvetini fark etmesini sağlar._ → Duran, kayan ve yuvarlanan cisimlerde sürtünme (nitel).
- **FİZ.11.1.7** Sürtünme kuvvetinin matematiksel modeline ilişkin tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 1.4.2 (s. 70)
  - a) Sürtünme kuvvetinin bağlı olduğu değişkenler arasındaki ilişkiyi keşfederek matematiksel modeline ulaşır. `[FBAB10.SB1]`
  - b) Farklı veri setleri ile hesaplamalar yaparak sürtünme kuvvetinin matematiksel modelini geneller. `[FBAB10.SB2]`
  - ⚠️ `CALC_INCLUDED` _Öğrenciler, matematiksel model kullanarak statik ve kinetik sürtünme kuvvetleriyle ilgili hesaplamalar yapar ve modeli geneller._ → Sürtünme kuvveti hesabı kapsamda.
  - ⚠️ `SCOPE_INCLUDED` _Öğrencilerden dijital içerik ya da deney verilerini kullanarak sürtünme kuvveti-uygulanan kuvvet grafiğini çizmeleri istenebilir._ → f–F grafiği kapsamda.

### Limit Hız

- **FİZ.11.1.8** Limit hızı etkileyen değişkenler ile ilgili bilimsel çıkarım yapabilme — beceri `FBAB8` · ders kitabı 1.5 (s. 86)
  - a) Limit hızı etkileyen değişkenleri tanımlar. `[FBAB8.SB1]`
  - b) Limit hızı etkileyen değişkenlerle ilgili verileri toplayarak kaydeder. `[FBAB8.SB2]`
  - c) Limit hızı etkileyen değişkenlerle ilgili verileri yorumlayarak değerlendirir. `[FBAB8.SB3]`
  - ⚠️ `CALC_EXCLUDED` _Matematiksel modeli ile ilgili örneklerde limit hızın bağlı olduğu değişkenlerin ilişkilerine yönelik yorumlamalarla sınırlı kalınır._ → Limit hız sayısal hesaplanmaz; yalnız değişken ilişkisi yorumlanır.

### Düzgün Çembersel Hareket

- **FİZ.11.1.9** Düzgün çembersel hareket yapan cisimlerin yörüngeleri ve hız vektörleri hakkında analojik akıl yürütebilme — beceri `KB2.16.3` · ders kitabı 1.6.1 (s. 95)
  - a) Düzgün çembersel hareket yapan farklı cisimlerin hareketlerini gözlemler. `[KB2.16.3.SB1]`
  - b) Düzgün çembersel hareket yapan farklı cisimlerin hareketlerinin özelliklerini tespit eder. `[KB2.16.3.SB2]`
  - c) Düzgün çembersel hareket yapan farklı cisimlerin hareketlerinin benzerliklerinden yola çıkarak yörüngeleri ve hız vektörü hakkında çıkarım yapar. `[KB2.16.3.SB3]`
- **FİZ.11.1.10** Düzgün çembersel hareketin değişkenleri arasındaki ilişkilerin matematiksel olarak modellenmesine ilişkin tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 1.6.2 (s. 101)
  - a) Düzgün çembersel hareketin değişkenlerini keşfederek aralarındaki ilişkileri matematiksel olarak modeller. `[FBAB10.SB1]`
  - b) Farklı veri setleri ile hesaplamalar yaparak düzgün çembersel hareketin değişkenleri arasındaki ilişkilere yönelik matematiksel modelleri geneller. `[FBAB10.SB2]`
  - ⚠️ `SCOPE_INCLUDED` _Drama etkinliği sırasında grup üyeleri arasında sağlanan etkileşim sonucu ulaştıkları değişkenler arasındaki ilişkilere yönelik matematiksel modelleri; yatay düzlemde düzgün çembersel hareket, düşey düzlemde düzgün çembersel hareket, yatay ve eğimli virajlardaki düzgün çembersel hareket problemlerinin çözümlerinde kullanarak geneller._ → Yatay düzlem, düşey düzlem, yatay ve eğimli viraj problemleri kapsamda.
  - ⚠️ `CALC_EXCLUDED` _Ray sisteminde çembersel hareketle ilgili matematiksel işlemlerden kaçınılır._ → Ray (ör. lunapark rayı) problemleri hesaplanmaz.
  - ⚠️ `CALC_INCLUDED` _Matematiksel hesaplamalar yapabilmeleri için açık uçlu test kullanılabilir._ → Düzgün çembersel hareket problemlerinde sayısal hesap ölçülür.

**Zenginleştirme (resmî; öğrenme çıktısı eklemez, ders kitabında yer almaz):**

- Farklı çekim ivmesine sahip uydu ve gezegenlerdeki serbest düşme hareketine yönelik problem durumları ele alınabilir. Serbest düşme hareketinde farklı yüksekliklerdeki konumlardan çeşitli açılarla atılan cisimlerin hareketleriyle ilgili hesaplamalar yapılabilir. Hareketli referanslardan farklı açılarla atılan cisimlerin hareketine yönelik problem durumları ele alınabilir. Eğimli virajda yol alan araçlara etki eden statik sürtünme kuvvetinin matematiksel hesaplamaları yapılabilir. Türkiye’de ve dünyada araç kazalarının sebepleri arasında “viraj güvenliği”nin yeri ve kazalardaki istatistik oranları araştırılabilir. Araçlarda kullanılan fren sistemleri incelenerek ABS fren sisteminin avantajlarının, statik ve kinetik sürtünme kuvvetleri arasındaki farklarla ilişkilendirilerek açıklanması istenebilir.
- Farklı açılarla atılan cisimlerin hareketini dikkate alan basit malzemeleri kullanarak bir oyun tasarlamaları istenebilir. Virajlarda güvenli sürüş yapmak için gereken önlemler ile Newton'ın Hareket Yasaları, sürtünme kuvveti ve çembersel hareket konu başlıkları ilişkilendirilerek araba lastiği tasarım önerisi oluşturulabilir. **[* fen liselerinde zorunlu]**
- Trigonometrik hesaplamaların kullanıldığı bileşenlerine ayırarak toplama işleminde sık kullanılan açı değerlerinin dışında başka açılar verilerek hesap makinesi ya da dinamik matematik uygulamalarının kullanımı teşvik edilebilir. Trigonometrik hesaplamaların kullanıldığı bileşenlerine ayırarak toplama işleminde en az iki vektörün toplanması sağlanabilir. Newton'ın Hareket Yasaları, Bernoulli İlkesi, sürtünme kuvveti ve düzgün çembersel hareket konuları ile ilişkilendirerek yarış arabası tasarımı yapılabilir. **[* fen liselerinde zorunlu]**

**Destekleme (resmî):**

- Serbest düşme gibi konular için basit veri toplama etkinlikleri ve bu verileri kullanarak temel matematiksel modellere ulaşmaları için basılı öğretim materyalleri sağlanabilir. Trigonometrik hesaplamaların kullanıldığı bileşenlerine ayırarak toplama işleminde sadece bir vektör kullanılabilir. Bu vektörün bileşenleri trigonometrik hesaplamalar ile bulunabilir. Bu bileşenler toplanarak vektörün kendisine ulaşılabilir. Trigonometrik hesaplamalarda sadece özel üçgenlerden yararlanılan vektörler kullanılabilir. Newton'ın Hareket Yasalarına yönelik problem çözümlerinde yalnızca tek cisim içeren örnekler tercih edilebilir. Sürtünme kuvvetinin hesaplanmasına yönelik örnek problem durumlarında yatay zemindeki cisimlere kendi ağırlıkları ve zemin tarafından uygulanan tepki kuvvetleri dışında herhangi bir düşey kuvvetin uygulanmadığı örnekler kullanılabilir. Limit hız ile ilgili örnek ve açıklamalarda yağmur damlasının ve paraşütle atlayan kişinin hareketi ile sınırlı kalınarak limit hız konusu sadece kavramsal düzeyde verilebilir.

---

## Ünite 2: ELEKTRİK VE MANYETİZMA (48 ders saati)

**Amaç (resmî):** Bu ünitede öğrencilerin elektrik motorları ve elektrik jeneratörleri arasındaki ilişki ile transformatörlerin yapısı ve kullanımı hakkında çıkarım yapmaları amaçlanmaktadır.

**Temel kabuller (resmî, bağlayıcı):** Öğrencilerin elektriklenme çeşitlerini ve yüklü cisimler ile elektroskop arasındaki etkileşimi, mıknatısların kutuplarını, mıknatısların etkileşimini ve pusula kullanımını bildiği kabul edilmektedir.

**Beceriler (resmî):**

- Alan becerileri: FBAB1. Bilimsel Gözlem, FBAB8. Bilimsel Çıkarım, FBAB10. Tümevarımsal Akıl Yürütme
- Kavramsal beceriler: KB2.4. Çözümleme, KB2.6. Bilgi Toplama, KB2.15. Yansıtma
- Eğilimler: E1.1. Merak, E3.6. Analitiklik
- Sosyal-duygusal: SDB1.1. Kendini Tanıma (Öz Farkındalık), SDB1.2. Kendini Düzenleme (Öz Düzenleme), SDB2.1. İletişim, SDB2.2. İş Birliği, SDB2.3 Sosyal Farkındalık
- Değerler: D17.Tasarruf, D19. Vatanseverlik
- Okuryazarlık: OB1. Bilgi Okuryazarlığı, OB4. Görsel Okuryazarlık, OB7. Veri Okuryazarlığı, OB8. Sürdürülebilirlik
- Disiplinler arası: Biyoloji, Görsel Sanatlar, Matematik
- Beceriler arası: KB2.10. Çıkarım Yapma, KB2.12. Mevcut Bilgiye/Veriye Dayalı Tahmin Etme, KB2.19. Mantıksal Denetleme, KB3.2. Problem Çözme

**Anahtar kavramlar (resmî):** elektriksel kuvvet, elektriksel alan, manyetik alan, manyetik kuvvet, manyetik akı, indüksiyon akımı, indüksiyon gerilimi, alternatif akım, transformatör

### Elektriksel Kuvvet ve Elektriksel Alan

- **FİZ.11.2.1** Elektrik yükleri arasındaki elektriksel kuvvetin matematiksel modeline yönelik tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 2.1.1 (s. 155)
  - a) Elektrik yükleri arasındaki elektriksel kuvvetin bağlı olduğu değişkenler arasındaki keşfettiği ilişkiyi matematiksel olarak modeller. `[FBAB10.SB1]`
  - b) Elektrik yükleri arasındaki elektriksel kuvvetin matematiksel modeli üzerinden genellemeler yapar. `[FBAB10.SB2]`
  - ⚠️ `CALC_EXCLUDED` _Öğrenciler, Coulomb Yasası ile ilgili farklı problem durumlarında matematiksel hesaplamalara girmeden uygulamalar yaparak matematiksel modeli geneller._ → Coulomb kuvveti yalnız oran/yön/yorum düzeyinde; sayısal hesap yok.
- **FİZ.11.2.2** Elektriksel alanın matematiksel modeline yönelik tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 2.1.2 (s. 166)
  - a) Elektrik yüklerinin oluşturduğu elektriksel alana ilişkin keşfettiği etmenler arasındaki ilişkiyi matematiksel olarak modeller. `[FBAB10.SB1]`
  - b) Elektrik yüklerinin oluşturduğu elektriksel alanın matematiksel modeli üzerinden genellemeler yapar. `[FBAB10.SB2]`
  - ⚠️ `CALC_EXCLUDED` _Öğrenciler, matematiksel hesaplara girmeden elektriksel alanla ilgili farklı problem türleri üzerinden uygulamalar yaparak matematiksel modeli geneller._ → Elektriksel alan yalnız oran/yön/yorum düzeyinde.
- **FİZ.11.2.3** Faraday kafesi ve Faraday kafesinin kullanım alanları ile ilgili bilgi toplayabilme — beceri `KB2.6` · ders kitabı 2.1.3 (s. 178)
  - a) Faraday kafesi ve Faraday kafesinin kullanım alanları ile ilgili bilgiye ulaşmak için kullanacağı kaynakları belirler. `[KB2.6.SB1]`
  - b) Belirlediği kaynağı kullanarak Faraday kafesi ve Faraday kafesinin kullanım alanları ile ilgili bilgileri bulur. `[KB2.6.SB2]`
  - c) Faraday kafesi ve Faraday kafesinin kullanım alanları ile ilgili ulaşılan bilgileri doğrular. `[KB2.6.SB3]`
  - ç) Faraday kafesi ve Faraday kafesinin kullanım alanları ile ilgili ulaşılan bilgileri kaydeder. `[KB2.6.SB4]`

### Manyetik Alan ve Manyetik Kuvvet

- **FİZ.11.2.4** Mıknatısların birbiriyle etkileşimine yönelik bilimsel gözlem yapabilme — beceri `FBAB1` · ders kitabı 2.2.1 (s. 186)
  - a) Mıknatısların birbiriyle etkileşimiyle ilgili nitelikleri tanımlar. `[FBAB1.SB1]`
  - b) Mıknatısların birbiriyle etkileşimiyle ilgili verileri toplayarak kaydeder. `[FBAB1.SB2]`
  - c) Mıknatısların birbiriyle etkileşimiyle ilgili verileri manyetik alan çizgileriyle açıklar. `[FBAB1.SB3]`
- **FİZ.11.2.5** Üzerinden akım geçen düz bir iletken telin oluşturduğu manyetik alana ilişkin tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 2.2.2 (s. 198)
  - a) Üzerinden akım geçen düz bir iletken telin oluşturduğu manyetik alana ilişkin matematiksel modeli bulur. `[FBAB10.SB1]`
  - b) Üzerinden akım geçen düz bir iletken telin oluşturduğu manyetik alana ilişkin matematiksel modeli geneller. `[FBAB10.SB2]`
  - ⚠️ `SCOPE_INCLUDED` _Manyetik alanın iletkene olan uzaklığı ve elektrik akımının büyüklüğünün değişimi hakkında öğrenci görüşleri alınarak hipotezler kurulur.Öğretmen manyetik alan katsayısı ve sağ el kuralı ile ilgili bilgi verir._ → Sağ el kuralı kapsamda.
  - ⚠️ `CALC_EXCLUDED` _Öğrenciler matematiksel hesaplamalara girmeden ulaştıkları matematiksel modelle ilgili problem çözümleri yaparak modeli geneller._ → Düz telin manyetik alanı oran/yön düzeyinde.
- **FİZ.11.2.6** Akım makarasının merkez ekseninde oluşan manyetik alanın matematiksel modeline ilişkin tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 2.2.3 (s. 207)
  - a) Akım makarasının merkez ekseninde oluşan manyetik alana ilişkin keşfettiği ilişkiyi matematiksel olarak modeller. `[FBAB10.SB1]`
  - b) Akım makarasının merkez ekseninde oluşan manyetik alanın matematiksel modeli üzerinden genelleme yapar. `[FBAB10.SB2]`
- **FİZ.11.2.7** Elektromıknatısların kullanım alanlarına ilişkin bilgi toplayabilme — beceri `KB2.6` · ders kitabı 2.2.4 (s. 213)
  - a) Elektromıknatısların kullanım alanlarıyla ilgili bilgiye ulaşmak için kullanacağı kaynakları belirler. `[KB2.6.SB1]`
  - b) Belirlediği kaynağı kullanarak elektromıknatısların kullanım alanlarıyla ilgili bilgileri bulur. `[KB2.6.SB2]`
  - c) Elektromıknatısların kullanım alanlarıyla ilgili ulaştığı bilgilerin doğru olup olmadığını belirler. `[KB2.6.SB3]`
  - ç) Elektromıknatısların günlük hayattaki kullanım alanlarıyla ilgili ulaştığı bilgileri kaydeder. `[KB2.6.SB4]`
- **FİZ.11.2.8** Manyetik alanda akım geçen düz bir tele etki eden kuvvete ilişkin matematiksel modele yönelik tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 2.2.5 (s. 218)
  - a) Manyetik alanda akım geçen düz bir tele etki eden kuvvetin etmenleri arasındaki keşfettiği ilişkiyi matematiksel olarak modeller. `[FBAB10.SB1]`
  - b) Manyetik alanda akım geçen düz bir tele etki eden kuvvete ilişkin matematiksel model üzerinden genelleme yapar. `[FBAB10.SB2]`
  - ⚠️ `SCOPE_INCLUDED` _Öğretmen manyetik alan içerisindeki akım geçen tele etki eden manyetik kuvvetin telin içerisinde hareketli yüklü parçacıklara etki eden kuvvetten kaynaklandığını vurgular._ → Tele etki eden kuvvetin kaynağı yüklü parçacıklar olarak kavramsal anılır; yüke etki eden kuvvet ayrı bir çıktı değildir.
  - ⚠️ `SCOPE_INCLUDED` _Öğrenciler her bir değişkeni ayrı ayrı değiştirerek çözdüğü problemler üzerinden, manyetik kuvvet ile değişkenler arasındaki ilişkiyi geneller._ → F = BIL modeliyle değişken bazlı problem çözümü; açık hesap yasağı yok.
- **FİZ.11.2.9** Manyetik alanda akım geçen düz bir tele etki eden kuvvet ile ilgili deneyimini elektrik motorlarının çalışma prensibine yansıtabilme — beceri `KB2.15` · ders kitabı 2.2.6 (s. 229)
  - a) Manyetik alanda akım geçen düz bir tele etki eden kuvvet ile ilgili deneyimini gözden geçirir. `[KB2.15.SB1]`
  - b) Deneyimine dayalı olarak manyetik alanda akım geçen dikdörtgen telin bir eksen etrafında dönmesi hakkında çıkarım yapar. `[KB2.15.SB2]`
  - c) Yaptığı çıkarımları elektrik motorlarının çalışma prensibi açısından değerlendirir. `[KB2.15.SB3]`

### İndüksiyon Akımı

- **FİZ.11.2.10** Manyetik akıya etki eden etmenleri çözümleyebilme — beceri `KB2.4` · ders kitabı 2.3.1 (s. 236)
  - a) Manyetik akıya etki eden etmenleri belirler. `[KB2.4.SB1]`
  - b) Manyetik akıya etki eden etmenler arasındaki ilişkiyi belirler. `[KB2.4.SB2]`
  - ⚠️ `CONCEPTUAL_ONLY` _Öğretmen manyetik akı kavramını kavramsal olarak açıklar._ → Manyetik akı kavramsal tanıtılır; B ve yüzey alanıyla ilişkisi belirlenir.
- **FİZ.11.2.11** İndüksiyon geriliminin matematiksel modeline ilişkin tümevarımsal akıl yürütebilme — beceri `FBAB10` · ders kitabı 2.3.2 (s. 242)
  - a) İndüksiyon geriliminin oluşmasında keşfettiği etmenler arasındaki ilişkiyi matematiksel olarak modeller. `[FBAB10.SB1]`
  - b) İndüksiyon geriliminin matematiksel modeli üzerinden genellemeler yapar. `[FBAB10.SB2]`
- **FİZ.11.2.12** İndüklenme sonucu oluşan alternatif (değişken) akım hakkında bilimsel çıkarım yapabilme — beceri `FBAB8` · ders kitabı 2.3.3 (s. 253)
  - a) İndüklenme sonucu oluşan alternatif akımı etkileyen etmenleri belirler. `[FBAB8.SB1]`
  - b) İndüklenme sonucu oluşan alternatif akımı etkileyen etmenler arasındaki ilişkiyi belirlemek üzere veri toplayarak kaydeder. `[FBAB8.SB2]`
  - c) İndüklenme sonucu oluşan alternatif akımı topladığı verilerden yola çıkarak yorumlayıp değerlendirir. `[FBAB8.SB3]`

### Transformatörler

- **FİZ.11.2.13** Transformatörün yapısı ve kullanım alanlarına yönelik bilimsel çıkarım yapabilme — beceri `FBAB8` · ders kitabı 2.4 (s. 263)
  - a) Transformatörün niteliklerini deney yaparak tanımlar. `[FBAB8.SB1]`
  - b) Transformatörlerin kullanım alanlarına yönelik topladığı verileri kaydeder. `[FBAB8.SB2]`
  - c) Elde ettiği verilerden yola çıkarak transformatörün kullanım alanlarındaki rolünü yorumlar ve değerlendirir. `[FBAB8.SB3]`
  - ⚠️ `CALC_EXCLUDED` _Transformatörlerin nitelikleri arasındaki ilişkilere yönelik yorumlamalarla sınırlı kalınır._ → Transformatör nitelikleri yalnız yorumlanır.
  - ⚠️ `CALC_EXCLUDED` _Matematiksel işlemlerden kaçınılır._ → Sarım-gerilim-akım sayısal hesabı yok.

**Zenginleştirme (resmî; öğrenme çıktısı eklemez, ders kitabında yer almaz):**

- Ferromanyetik, diyamanyetik ve paramanyetik maddelerin özellikleri ve manyetik alanla etkileşimleri araştırılabilir. Yüksek gerilim hatları ve trafoların etrafında oluşan manyetik alanın veya elektrikli cihazlar kullanılırken oluşan manyetik alanın sağlığa etkileri araştırılabilir.
- Elektrik jeneratörlerinde manyetik akı değişimiyle elektrik elde edilmesine ve cevher tespitinde metal dedektörlerin kullanılmasına yönelik uygulamalara yer verilebilir. **[* fen liselerinde zorunlu]**
- STEM basamaklarını uygulayarak transformatörlerde elektrik gerilimini yükseltip alçaltma işlemine dayalı bir düzenek kurulabilir. **[* fen liselerinde zorunlu]**

**Destekleme (resmî):**

- Deney tasarlama, veri toplama, veri işleme ve sonuca varma süreçlerinde deneyin yapılışına dönük adım adım yönergeler ve hazır veri toplama şablonları kullanılabilir.

---

## Ünite 3: OPTİK (36 ders saati)

**Amaç (resmî):** Bu ünitede öğrencilerin ışık şiddeti, ışık akısı ve aydınlanma kavramlarını tanımlamaları, düzlem aynaları kullanarak model oluşturmaları, küresel aynaların ve merceklerin yapılarını karşılaştırmaları, küresel aynalarda ve merceklerde görüntü oluşumu ile ilgili deney yapmaları, ışığın saydam ortamlardaki davranışını kullanarak deney düzeneği oluşturmaları, görünür derinliği gözlemlemeleri, fiber optik malzemelerin yapısı, çalışma prensibi ve kullanım alanlarına ilişkin bilgi toplamaları, prizmalar ve prizmalar ile kurulan optik sistemler hakkında çıkarım yapmaları amaçlanmaktadır.

**Temel kabuller (resmî, bağlayıcı):** Öğrencilerin fen bilimleri dersinde geçen ışın, ışık ve aydınlanma kavramlarını bildiği, düzlem ayna, küresel ayna ve mercekleri temel özelliklerine göre sınıflandırabildiği ve yansıma, kırılma ve odak noktası kavramlarını bildiği kabul edilmektedir.

**Beceriler (resmî):**

- Alan becerileri: FBAB1. Bilimsel Gözlem, FBAB7. Deney Yapma, FBAB8. Bilimsel Çıkarım Yapma, FBAB9. Bilimsel Model Oluşturma, FBAB11. Tümdengelimsel Akıl Yürütme
- Kavramsal beceriler: KB2.6. Bilgi Toplama, KB2.7. Karşılaştırma
- Eğilimler: E1.1. Merak, E1.3. Azim ve Kararlılık, E1.5. Kendine Güvenme (Öz Güven), E3.1. Muhakeme, E3.3. Yaratıcılık, E3.4. Gerçeği Arama, E3.5. Açık Fikirlilik, E3.6. Analitiklik, E3.7. Sistematiklik, E3.8. Soru Sorma
- Sosyal-duygusal: SDB1.1. Kendini Tanıma (Öz Farkındalık), SDB1.2. Kendini Düzenleme (Öz Düzenleme), SDB2.1. İletişim, SDB2.2. İş Birliği, SDB3.1. Uyum, SDB3.2. Esneklik, SDB3.3. Sorumlu Karar Verme
- Değerler: D1. Adalet, D3. Çalışkanlık, D16. Sorumluluk, D17. Tasarruf, D19. Vatanseverlik
- Okuryazarlık: OB1. Bilgi Okuryazarlığı, OB4. Görsel Okuryazarlık, OB7. Veri Okuryazarlığı
- Disiplinler arası: Görsel Sanatlar, Matematik
- Beceriler arası: KB2.11. Gözleme Dayalı Tahmin Etme, KB2.12. Mevcut Bilgiye/Veriye Dayalı Tahmin Etme, KB2.14. Yorumlama, KB2.15. Yansıtma, KB3.1. Karar Verme, KB3.2. Problem Çözme

**Anahtar kavramlar (resmî):** ışık şiddeti, ışık akısı, aydınlanma, merkez, tepe noktası, asal eksen, ortamın ışığı kırma indisi, Snell Yasası, tam yansıma, sınır açısı, görünür derinlik, fiber optik

### Işık Şiddeti, Işık Akısı ve Aydınlanma

- **FİZ.11.3.1** Işık şiddeti, ışık akısı ve aydınlanma kavramlarına ilişkin bilimsel çıkarım yapabilme — beceri `FBAB8` · ders kitabı 3.1 (s. 302)
  - a) Işık şiddeti, ışık akısı ve aydınlanma kavramlarının tanımlarını yapar. `[FBAB8.SB1]`
  - b) Işık şiddeti, ışık akısı ve aydınlanma kavramları ile ilgili veri setlerini inceler. `[FBAB8.SB2]`
  - c) Veri setlerini kullanarak ışık şiddeti, ışık akısı ve aydınlanma kavramlarını yorumlayarak değerlendirir. `[FBAB8.SB3]`

### Düzlem Aynalar

- **FİZ.11.3.2** Düzlem aynaları kullanarak bilimsel model oluşturabilme — beceri `FBAB9` · ders kitabı 3.2 (s. 312)
  - a) Düzlem aynaları kullanarak bir model önerir. `[FBAB9.SB1]`
  - b) Düzlem aynaları kullanarak önerdiği modeli yeni durumlara uyarlayarak geliştirir. `[FBAB9.SB2]`

### Küresel Aynalar

- **FİZ.11.3.3** Küresel aynaların özelliklerine ilişkin karşılaştırma yapabilme — beceri `KB2.7` · ders kitabı 3.3.1 (s. 323)
  - a) Küresel aynaların fiziksel özelliklerini ve ışınların küresel aynalarda yansıdıktan sonra izlediği yolu belirler. `[KB2.7.SB1]`
  - b) Çukur ve tümsek aynaların benzer özelliklerini listeler. `[KB2.7.SB2]`
  - c) Çukur ve tümsek aynaların farklı özelliklerini listeler. `[KB2.7.SB3]`
- **FİZ.11.3.4** Küresel aynalarda görüntü oluşumu ile ilgili deney yapabilme — beceri `FBAB7` · ders kitabı 3.3.2 (s. 333)
  - a) Küresel aynalarda görüntü oluşumu ile ilgili bir deney tasarlar. `[FBAB7.SB1]`
  - b) Küresel aynalarda görüntü oluşumu ile ilgili tasarladığı deney düzeneğinden veri toplayarak analiz eder. `[FBAB7.SB2]`

### Kırılma

- **FİZ.11.3.5** Işığın saydam ortamlardaki davranışını kullanarak deney yapabilme — beceri `FBAB7` · ders kitabı 3.4 (s. 343)
  - a) Işığın saydam ortamlardaki davranışı ile ilgili deney tasarlar. `[FBAB7.SB1]`
  - b) Işığın saydam ortamlardaki davranışı ile ilgili tasarladığı deney düzeneğinden veri toplayarak analiz eder. `[FBAB7.SB2]`

### Görünür Derinlik

- **FİZ.11.3.6** Saydam ortamlarda görünür derinliğin, gerçek derinlik ve ortamların ışığı kırma indislerine bağlı olarak değiştiğine ilişkin bilimsel gözlem yapabilme — beceri `FBAB1` · ders kitabı 3.5 (s. 354)
  - a) Görünür derinliği etkileyen gerçek derinlik ve ortamların ışığı kırma indisini tanımlar. `[FBAB1.SB1]`
  - b) Görünür derinliğin gerçek derinlik ve ortamların ışığı kırma indisine bağlı olarak değiştiğini gözlemleyerek kaydeder. `[FBAB1.SB2]`
  - c) Gözlemlerine dayalı olarak görünür derinliğin gerçek derinlik ve ortamların ışığı kırma indisine bağlı olarak değişimini açıklar. `[FBAB1.SB3]`
  - ⚠️ `CALC_EXCLUDED` _Görünür derinliğe ilişkin matematiksel model ve işlemlerden kaçınılır._ → Görünür derinlik yalnız nitel.

### Fiber Optik

- **FİZ.11.3.7** Fiber optik malzemelerin yapısı, çalışma prensibi ve kullanım alanlarına ilişkin bilgi toplayabilme — beceri `KB2.6` · ders kitabı 3.6 (s. 361)
  - a) Fiber optik malzemelerin yapısı, çalışma prensibi ve kullanım alanları ile ilgili bilgiye ulaşmak için kullanacağı kaynakları belirler. `[KB2.6.SB1]`
  - b) Fiber optik malzemelerin yapısı, çalışma prensibi ve kullanım alanları ile ilgili bilgiye ulaşmak için belirlediği araçları kullanarak bilgi toplar. `[KB2.6.SB2]`
  - c) Fiber optik malzemelerin yapısı, çalışma prensibi ve kullanım alanları hakkında toplanan bilgiyi doğrular. `[KB2.6.SB3]`
  - ç) Fiber optik malzemelerin yapısı, çalışma prensibi ve kullanım alanları hakkında ulaşılan bilgileri kaydeder. `[KB2.6.SB4]`

### Prizmalar

- **FİZ.11.3.8** Prizmalar ve prizmalar ile kurulan birleşik sistemlerde ışığın izlediği yola ilişkin tümdengelimsel akıl yürütebilme — beceri `FBAB11` · ders kitabı 3.7 (s. 367)
  - a) Kırılma yasalarının prizmalar için kullanılabilir olduğuna dair hipotez kurarak test eder. `[FBAB11.SB1]`
  - b) Geçerli hipotezleri kullanarak prizmalar ile oluşturulmuş birleşik sistemlerde tek renkli ışığın izleyeceği yolu açıklar. `[FBAB11.SB2]`

### Mercekler

- **FİZ.11.3.9** Merceklerin özelliklerine ilişkin karşılaştırma yapabilme — beceri `KB2.7` · ders kitabı 3.8.1 (s. 373)
  - a) Merceklerin fiziksel özelliklerini ve ışınların merceklerde kırıldıktan sonra izlediği yola ilişkin özellikleri belirler. `[KB2.7.SB1]`
  - b) Yakınsak ve ıraksak merceklerin benzer özelliklerini listeler. `[KB2.7.SB2]`
  - c) Yakınsak ve ıraksak merceklerin farklı özelliklerini listeler. `[KB2.7.SB3]`
- **FİZ.11.3.10** Merceklerde görüntü oluşumu ile ilgili deney yapabilme — beceri `FBAB7` · ders kitabı 3.8.2 (s. 381)
  - a) Yakınsak ve ıraksak merceklerde görüntü oluşumu ile ilgili deney tasarlar. `[FBAB7.SB1]`
  - b) Yakınsak ve ıraksak merceklerde görüntü oluşumu ile ilgili tasarladığı deney düzeneğinden veri toplayarak analiz eder. `[FBAB7.SB2]`

**Zenginleştirme (resmî; öğrenme çıktısı eklemez, ders kitabında yer almaz):**

- Kırılma olayında paralel ortamlarda kayma miktarını belirleyen değişkenler incelenebilir. Aydınlatma sistemlerinde kırılmanın kullanımı, refraktometre cihazının çalışma prensibi ve kullanım alanları araştırılabilir. Fiber optik hatlarda yaşanan sorunlara ilişkin araştırma yaparak çözüm önerileri geliştirilebilir. İbnülheysem'in optik bilimi adına yapmış olduğu çalışmalar ve “optik ve mekanik analojisi” araştırılabilir.
- Mercek ve ayna sistemlerinin bütünleşik kullanıldığı sistemler araştırılarak bu sistemlere ilişkin bir model geliştirilebilir. **[* fen liselerinde zorunlu]**
- Teleskop, mikroskop, dürbün gibi optik sistemlerden birini belirleyerek bunların tarihsel serüvenleri, diğer bilim alanlarındaki kullanımları ve çalışma ilkeleri hakkında sunum hazırlanabilir. Sunumlarda Kemâleddin el-Fârisî ile Freibergli Theodoric'in yaptıkları çalışmalara yer vermeleri istenebilir. **[* fen liselerinde zorunlu]**

**Destekleme (resmî):**

- Küresel aynalarda hazır verilen model üzerinde incelemeler yapılabilir. Kırılma yasalarına ilişkin hazır deney düzeneği verilebilir. Fiber optik sistemler için bilgiler öğretmen tarafından verilebilir. Prizmalar ve merceklerde hazır modeller üzerinden incelemeler yapılabilir.

---

## Sınıflar arası bağlam (yalnız ünite düzeyi, aynı PDF)

| Sınıf | Üniteler (öğrenme çıktısı / ders saati) |
|---|---|
| 9 | Fizik Bilimi ve Kariyer Keşfi (4/8), Kuvvet ve Hareket (7/24), Akışkanlar (7/18), Enerji (6/18) |
| 10 | Kuvvet ve Hareket (3/14), Enerji (5/16), Elektrik (7/22), Dalgalar (7/16) |
| **11** | **Kuvvet ve Hareket (10/54), Elektrik ve Manyetizma (13/48), Optik (10/36)** |
| 12 | Kuvvet ve Hareket (6/46), Enerji (6/36), Dalgalar (7/22), Madde ve Doğası (8/34) |

Her sınıfa ayrıca 6 saat okul temelli planlama eklenir (toplam 72 / 72 / 144 / 144).
