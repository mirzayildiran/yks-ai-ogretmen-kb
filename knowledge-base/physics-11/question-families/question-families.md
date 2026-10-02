# 11. Sınıf Fizik — Soru Aileleri

> Otomatik üretildi: `scripts/build_question_families.py`. Elle düzenleme yapma.

Soru ailesi = aynı fiziksel durum + aynı ölçülen süreç bileşeni + aynı çözüm mantığı. Sayılar ve bağlam değişince aile değişmez.
Her ailenin ölçtüğü süreç bileşeni MEB Soru Yazım Kılavuzu'ndaki gibi beceri koduyla etiketlidir (ör. `FBAB10.SB1`).
Piyasa (STEP 9) ve ÖSYM (STEP 10) kanıtları henüz eklenmedi.

## FİZ.11.1.1

### 001 · Serbest düşmede ivmenin kütleden bağımsızlığı

- **Ölçülen:** FİZ.11.1.1 a `FBAB10.SB1`, FİZ.11.1.1 b `FBAB10.SB2`
- **Yapı:** Hava direncinin ihmal edildiği (ya da edilmediği) bir ortamda farklı kütleli cisimler aynı yükseklikten bırakılır; düşme süreleri, hızları ya da ivmeleri karşılaştırılır.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Ağır cisim daha büyük ivmeyle düşer / önce yere ulaşır” (Ağırlık arttıkça serbest düşme ivmesi artar (Aristotelesçi yanılgı)); “Hafif cisim hava direnci yokken de daha yavaş düşer” (Hava direnci ile kütle etkisini karıştırma); “Kütle iki katına çıkınca düşme süresi yarıya iner” (İvmeyi kütleyle doğru orantılı sanma)
- **Öğrenci hataları:** İvmeyi kütleye bağlı sanmak `CONCEPTUAL_ERROR`; 'Hava direnci ihmal' koşulunu gözden kaçırmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “serbest düşen farklı kütleli cisimlere örnek olaca…”; kitap s.16 1. Etkinlik

### 002 · Serbest düşme verisinden ivmenin bulunması

- **Ölçülen:** FİZ.11.1.1 a `FBAB10.SB1`, FİZ.11.1.1 b `FBAB10.SB2`
- **Yapı:** Serbest düşen cismin eşit zaman aralıklarındaki hız (ya da konum) değerleri verilir; hız değişiminin sabit olduğu örüntüsünden ivme bulunur ya da genellenir.
- **Uyarıcı:** TABLE, GRAPH, DATA_SET, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Hızlar arttığı için ivme de artıyor” (Hız ile ivmeyi karıştırma); “Konum farklarının sabit olduğunu varsayıp ivmeyi sıfır bulma” (Konum ve hız tablosunu karıştırma)
- **Öğrenci hataları:** ϑ-t yerine x-t grafiğinin eğimini ivme sanmak `GRAPH_READING_ERROR`; Ardışık farklar yerine değerlerin kendisini kullanmak `TABLE_READING_ERROR`
- **Kanıt:** kitap s.122 ÖD-4; program “Serbest düşme hareketi yapan cisimlerin ivmeleriyl…”
- **Kapsam notu:** Farklı gezegenler programda zenginleştirme önerisi; kitap ölçme sorusunda (ÖD-4) kullanıyor.

## FİZ.11.1.2

### 003 · Düşen cetvelle tepki süresinin ölçülmesi

- **Ölçülen:** FİZ.11.1.2 a `FBAB12.SB1`, FİZ.11.1.2 c `FBAB12.SB3`
- **Yapı:** Bir kişi cetveli bırakır, diğeri yakalar; cetvelin düştüğü uzunluktan tepki süresi (ya da tersi) bulunur.
- **Uyarıcı:** EXPERIMENT, DAILY_LIFE_CONTEXT, TABLE · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Yakalama mesafesi iki katsa tepki süresi de iki kat” (h ∝ t² yerine h ∝ t sanma)
- **Öğrenci hataları:** h = ½gt² yerine h = g·t kullanmak `FORMULA_SELECTION_ERROR`; cm'yi m'ye çevirmemek `UNIT_ERROR`
- **Kanıt:** kitap s.120 ÖD-1

### 004 · İlk hızsız serbest düşmede hız-yükseklik-süre hesabı

- **Ölçülen:** FİZ.11.1.2 c `FBAB12.SB3`
- **Yapı:** Durgun bırakılan cismin yüksekliği, süresi ya da yere çarpma hızından ikisi bilinmeyen üçüncüsü sorulur.
- **Uyarıcı:** TEXT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Yükseklik iki katına çıkınca süre de iki kat” (h ∝ t² ilişkisini doğrusal sanma); “Son 1 saniyedeki yolu toplam yolun yarısı sanma” (Eşit sürelerde eşit yol alındığını sanma)
- **Öğrenci hataları:** ϑ² = 2gh'de karekök almayı unutmak `ALGEBRA_ERROR`; ½ katsayısını unutmak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.29 Kontrol Noktası; kitap s.24 Örnek

### 005 · Yukarı yönlü serbest düşme: tepe noktası, çıkış ve iniş

- **Ölçülen:** FİZ.11.1.2 c `FBAB12.SB3`
- **Yapı:** Yukarı ilk hızla fırlatılan cismin maksimum yüksekliği, çıkış süresi, havada kalma süresi ya da belirli bir andaki hızı sorulur.
- **Uyarıcı:** TEXT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Tepe noktasında ivme sıfırdır” (Hız sıfır olunca ivmenin de sıfır olduğunu sanma); “İniş süresi çıkış süresinden uzundur (aynı seviyeye dönüşte)” (Simetriyi bilmeme); “Tepe noktasında cisim dengededir” (Anlık durmayı dengeyle karıştırma)
- **Öğrenci hataları:** Yönü değişince ivmenin işaretini de değiştirmek `SIGN_ERROR`; Toplam süreyi tek denklemle bulurken kökün negatif/pozitif seçimini yanlış yapmak `ALGEBRA_ERROR`
- **Kanıt:** kitap s.28 6. Alıştırma; program “ilk hızı sıfırdan farklı olan serbest düşen cisiml…”

### 006 · Aşağı ilk hızlı düşme ve hareketli taşıyıcıdan bırakma

- **Ölçülen:** FİZ.11.1.2 c `FBAB12.SB3`
- **Yapı:** Cisim aşağı yönlü ilk hızla atılır ya da düşey hareket eden bir taşıyıcıdan (kuş, balon, asansör) bırakılır; ilk hız taşıyıcının hızıdır.
- **Uyarıcı:** TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Bırakılan cismin ilk hızı sıfırdır” (Taşıyıcının hızını cisme aktarmama); “Yukarı çıkan balondan bırakılan cisim hemen aşağı düşer” (İlk hız yönünü yok sayma)
- **Öğrenci hataları:** İlk hızı sıfır almak `CONCEPTUAL_ERROR`; İlk hızın yönünü işaretle göstermemek `SIGN_ERROR`
- **Kanıt:** kitap s.127 ÖD-10

### 007 · Aynı noktadan iki kez geçiş süreleri

- **Ölçülen:** FİZ.11.1.2 c `FBAB12.SB3`
- **Yapı:** Yukarı atılan cismin belirli bir noktadan çıkarken ve inerken geçme anları verilir; ilk hız, tepe yüksekliği ya da noktalar arası uzaklık sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** zor–AYT-üstü
- **Çeldiriciler:** “Tepeye çıkış süresi t₂ − t₁ kadardır” (Simetri ortasını yanlış bulma (doğrusu (t₁+t₂)/2))
- **Öğrenci hataları:** Simetri merkezini yanlış belirlemek `METHOD_SELECTION_ERROR`
- **Kanıt:** kitap s.120 ÖD-2

### 008 · Ardışık eşit zaman aralıklarında alınan yolların oranı

- **Ölçülen:** FİZ.11.1.2 b `FBAB12.SB2`, FİZ.11.1.2 c `FBAB12.SB3`
- **Yapı:** Durgun bırakılan cismin ardışık eşit sürelerde aldığı yollar (h, 3h, 5h, 7h ...) üzerinden yükseklik ya da süre sorulur.
- **Uyarıcı:** DIAGRAM, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Eşit sürelerde eşit yollar alınır” (Sabit hızlı hareket sanma); “Yollar 1:2:3:4 oranında artar” (Toplam yol ile aralık yolunu karıştırma)
- **Öğrenci hataları:** Toplam yolu (1:4:9) aralık yolu (1:3:5) sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.29 Kontrol Noktası; kitap s.121 ÖD-3

### 009 · Serbest düşmenin konum-hız-ivme grafikleri

- **Ölçülen:** FİZ.11.1.2 b `FBAB12.SB2`, FİZ.11.1.2 c `FBAB12.SB3`
- **Yapı:** Serbest düşen (ya da yukarı atılan) cismin x-t, ϑ-t, a-t grafiklerinden biri verilir ya da çizilmesi istenir; grafikler arası dönüşüm yapılır.
- **Uyarıcı:** GRAPH · **Zorluk:** orta–zor
- **Çeldiriciler:** “a-t grafiğinde tepe noktasında ivme sıfıra iner” (Tepe noktasında ivmenin sıfır olduğunu sanma); “Yukarı atışın ϑ-t grafiği tepe noktasında kırılır” (İvmenin yön değiştirdiğini sanma); “x-t grafiği doğrusal çizilir” (Sabit hızlı hareketle karıştırma)
- **Öğrenci hataları:** Pozitif yön seçimini grafik boyunca tutarlı uygulamamak `SIGN_ERROR`; Grafik eğimi ile grafik değerini karıştırmak `GRAPH_READING_ERROR`
- **Kanıt:** program “hız-zaman, ivme-zaman ve konum-zaman grafiklerini …”; kitap s.122 ÖD-3e

### 010 · Serbest düşme veri setinden kanıta dayalı açıklama

- **Ölçülen:** FİZ.11.1.2 a `FBAB12.SB1`, FİZ.11.1.2 b `FBAB12.SB2`, FİZ.11.1.2 c `FBAB12.SB3`
- **Yapı:** Bir deneyin (fotokapı, video analizi, sensör) zaman-konum ya da zaman-hız verisi verilir; hangi verinin hangi sonucu desteklediği, eksik verinin ne olması gerektiği ya da hatalı ölçüm sorulur.
- **Uyarıcı:** TABLE, EXPERIMENT, DATA_SET · **Zorluk:** orta
- **Çeldiriciler:** “Konumlar eşit arttığı için hareket sabit hızlıdır” (Konum farklarını incelemeden yargıya varma)
- **Öğrenci hataları:** Tabloda konum ile yer değiştirmeyi karıştırmak `TABLE_READING_ERROR`
- **Kanıt:** kitap s.21 2. Etkinlik; program “Serbest düşme hareketi ile ilgili verileri toplaya…”; kılavuz s.114

## FİZ.11.1.3

### 011 · Yatay ilk hızla iki boyutlu hareket (eski adı: yatay atış)

- **Ölçülen:** FİZ.11.1.3 a `FBAB10.SB1`
- **Yapı:** Belli yükseklikten yatay hızla fırlatılan cismin uçuş süresi, menzili ya da çarpma hızı sorulur; süre düşey hareketten bulunur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Yatay hızı büyük olan cisim daha geç yere düşer” (Bileşenlerin bağımsızlığını bilmeme); “Çarpma hızı yalnız düşey hızdır” (Yatay bileşeni unutma)
- **Öğrenci hataları:** Uçuş süresini yatay hareketten bulmaya çalışmak `METHOD_SELECTION_ERROR`; Çarpma hızında bileşenleri skaler toplamak `VECTOR_ERROR`
- **Kanıt:** kitap s.123 ÖD-5; kitap s.124 ÖD-6; program “yalnızca yer çekimi ivmesi etkisi altında iki boyu…”

### 012 · Yatayla açılı ilk hızla iki boyutlu hareket (eski adı: eğik atış)

- **Ölçülen:** FİZ.11.1.3 a `FBAB10.SB1`, FİZ.11.1.3 b `FBAB10.SB2`
- **Yapı:** Yatayla α açısıyla atılan cismin tepe yüksekliği, uçuş süresi, menzili ya da tepe noktasındaki hızı sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Tepe noktasında hız sıfırdır” (Yatay bileşeni unutma); “Tepe noktasında ivme sıfırdır” (İvmeyi hıza bağlı sanma); “sin ve cos'un yeri değişmiş seçenek” (Açının hangi eksenle ölçüldüğüne bakmama)
- **Öğrenci hataları:** Bileşenlerde sin/cos'u karıştırmak `VECTOR_ERROR`; Menzili ϑ₀·t ile hesaplamak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.125 ÖD-8; kitap s.130 ÖD-13; kitap s.39 Kontrol Noktası

### 013 · İki boyutlu harekette bir noktadaki hız vektörü

- **Ölçülen:** FİZ.11.1.3 a `FBAB10.SB1`
- **Yapı:** Hareketin bir anındaki hızın büyüklüğü ya da yatayla yaptığı açı sorulur (bileşenlerin vektörel toplamı).
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** orta
- **Çeldiriciler:** “Bileşke hız, bileşenlerin toplamıdır” (Vektörleri skaler toplama)
- **Öğrenci hataları:** Pisagor yerine düz toplama `VECTOR_ERROR`
- **Kanıt:** kitap s.133 ÖD-14d

### 014 · İki boyutlu hareketin bileşenlerinin veriden ayrıştırılması

- **Ölçülen:** FİZ.11.1.3 a `FBAB10.SB1`
- **Yapı:** Video ya da stroboskopik fotoğraftan alınan x(t), y(t) verilerinden yatay bileşenin sabit hızlı, düşey bileşenin sabit ivmeli olduğu örüntüsü bulunur; eksik değer ya da ivme sorulur.
- **Uyarıcı:** TABLE, EXPERIMENT, DATA_SET · **Zorluk:** orta
- **Çeldiriciler:** “Yatay konum farkları da artar” (Yatayda ivme olduğunu sanma); “Düşey konum farkları eşittir” (Düşeyde sabit hız sanma)
- **Öğrenci hataları:** Konum değerlerini fark almadan yorumlamak `TABLE_READING_ERROR`
- **Kanıt:** program “hareket bileşenlerini eksenlere göre sabit hızlı v…”

### 015 · Eğik düzlem ya da basamaklara düşen iki boyutlu hareket

- **Ölçülen:** FİZ.11.1.3 b `FBAB10.SB2`
- **Yapı:** Cisim bir eğik düzlemden ya da basamaklardan atılır; hangi basamağa düşeceği ya da eğik düzlemin neresine çarpacağı sorulur.
- **Uyarıcı:** DIAGRAM · **Zorluk:** zor–AYT-üstü
- **Çeldiriciler:** “Cisim ilk basamağa düşer” (Yatay ve düşey yer değiştirme ilişkisini kurmama)
- **Öğrenci hataları:** Yatay ve düşey yer değiştirmeyi aynı denkleme yanlış bağlamak `METHOD_SELECTION_ERROR`
- **Kanıt:** kitap s.128 ÖD-11

### 016 · İki boyutlu hareketin bileşen grafikleri

- **Ölçülen:** FİZ.11.1.3 a `FBAB10.SB1`, FİZ.11.1.3 b `FBAB10.SB2`
- **Yapı:** Hareketin yatay ve düşey bileşenleri için x-t, ϑ-t, a-t grafiklerinden doğru olanlar seçilir ya da çizilir.
- **Uyarıcı:** GRAPH · **Zorluk:** orta
- **Çeldiriciler:** “Yatay ϑ-t grafiği azalan doğru” (Yatayda da ivme olduğunu sanma)
- **Öğrenci hataları:** Yatay ve düşey grafikleri karıştırmak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.129 ÖD-11e; program “matematiksel hesaplamalar ve grafiklere dayalı yor…”

### 017 · Hareketli referanstan açılı atış · **zenginleştirme**

- **Ölçülen:** FİZ.11.1.3 b `FBAB10.SB2`
- **Yapı:** Hareket eden araç ya da kişi tarafından atılan cismin yere göre hareketi sorulur.
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** zor–AYT-üstü
- **Çeldiriciler:** “Top atıldığı noktanın gerisine düşer” (Taşıyıcı hızının cisme aktarıldığını bilmeme)
- **Öğrenci hataları:** Yere göre ve taşıyıcıya göre hızları karıştırmak `CONCEPTUAL_ERROR`
- **Kanıt:** program “Öğrenciler, yalnızca yer çekimi ivmesi etkisi altı…”
- **Kapsam notu:** Programda zenginleştirme önerisi ('Hareketli referanslardan farklı açılarla atılan cisimler'); temel kapsam dışı.

## FİZ.11.1.4

### 018 · Eylemsizlik durumlarının yorumlanması

- **Ölçülen:** FİZ.11.1.4 a `FBAB10.SB1`, FİZ.11.1.4 b `FBAB10.SB2`
- **Yapı:** Günlük bir durumda (fren yapan otobüs, emniyet kemeri, masa örtüsü çekme) cisimlerin davranışı eylemsizlikle açıklanır.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Hareket eden cismin hareketini sürdürmesi için kuvvet gerekir” (Hareket–kuvvet yanılgısı (impetus)); “Yolcuyu öne iten bir kuvvet vardır” (Eylemsizliği kuvvet sanma)
- **Öğrenci hataları:** Sabit hızlı harekette bileşke kuvveti sıfırdan farklı sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.40 4. Etkinlik; program “Bileşke kuvvet ile cisimlerin hareketi arasındaki …”

### 019 · Kuvvet–kütle–ivme ilişkisi (tablo ve grafik)

- **Ölçülen:** FİZ.11.1.4 a `FBAB10.SB1`, FİZ.11.1.4 b `FBAB10.SB2`
- **Yapı:** Farklı kuvvet ve kütleler için ölçülen ivme değerlerinden ilişki kurulur, eksik değer bulunur ya da F-a / a-m grafiği yorumlanır.
- **Uyarıcı:** TABLE, GRAPH, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Kütle iki katına çıkınca ivme de iki kat olur” (Ters orantıyı doğru orantı sanma); “Sürtünmeli ortamda F-a grafiği orijinden geçer” (Sürtünmenin eşik etkisini bilmeme)
- **Öğrenci hataları:** Uygulanan kuvveti bileşke kuvvet sanmak `CONCEPTUAL_ERROR`; Grafik eğiminin fiziksel anlamını yanlış okumak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.134 ÖD-15; kitap s.43 Etkinlik

### 020 · Etki-tepki kuvvet çiftlerinin belirlenmesi

- **Ölçülen:** FİZ.11.1.4 a `FBAB10.SB1`, FİZ.11.1.4 b `FBAB10.SB2`
- **Yapı:** Etkileşen cisimlerde hangi kuvvetlerin etki-tepki çifti olduğu, büyüklükleri ve neden birbirini dengelemedikleri sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Ağırlık ve normal kuvvet etki-tepki çiftidir” (Dengeleyen kuvvetlerle etki-tepkiyi karıştırma); “Büyük kütleli cisim daha büyük kuvvet uygular” (Etki-tepkinin eşitliğini bilmeme); “Etki-tepki kuvvetleri birbirini dengeler” (Farklı cisimlere etki ettiğini gözden kaçırma)
- **Öğrenci hataları:** Kuvvetin hangi cisme etki ettiğini belirtmemek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.50 17. Alıştırma

### 021 · Bileşke kuvvet ile hareket durumunun ilişkisi

- **Ölçülen:** FİZ.11.1.4 a `FBAB10.SB1`
- **Yapı:** İlk hız ve kuvvet vektörleri verilen cisimlerin hızlanıp yavaşlayacağı ya da yön değiştireceği belirlenir.
- **Uyarıcı:** DIAGRAM, TABLE · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Cisim her zaman kuvvet yönünde hareket eder” (Hız yönünü ivme yönüyle karıştırma)
- **Öğrenci hataları:** Kuvvet ile hız yönünü özdeşleştirmek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.140 ÖD-26

## FİZ.11.1.5

### 022 · Serbest cisim diyagramı çizme / doğru diyagramı seçme

- **Ölçülen:** FİZ.11.1.5 a `KB2.14.SB1`, FİZ.11.1.5 b `KB2.14.SB2`
- **Yapı:** Bir ya da birkaç cisme etki eden tüm kuvvetler belirlenip vektörlerle gösterilir; doğru diyagram seçilir.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Hareket yönünde ayrı bir 'hareket kuvveti' oku” (Hareket–kuvvet yanılgısı); “Merkezcil kuvvet ayrı bir kuvvet olarak çizilmiş” (Merkezcil kuvveti ayrı kuvvet sanma); “Cismin başka cisme uyguladığı kuvvet diyagrama eklenmiş” (Kuvvetin hangi cisme etki ettiğini karıştırma)
- **Öğrenci hataları:** Diyagrama tepki kuvvetlerini ekleyerek çift sayım yapmak `CONCEPTUAL_ERROR`; Kuvveti eksik çizmek (normal ya da sürtünme) `CARELESS_ERROR`
- **Kanıt:** kitap s.53 5. Etkinlik; program “Bir cisme etki eden kuvvetleri belirler…”

### 023 · Dengedeki asılı sistemlerde ip gerilmeleri

- **Ölçülen:** FİZ.11.1.5 b `KB2.14.SB2`, FİZ.11.1.5 c `KB2.14.SB3`
- **Yapı:** İplerle asılı, dengedeki cisimlerde ip gerilmeleri ya da kuvvetölçer değerleri bulunur.
- **Uyarıcı:** DIAGRAM · **Zorluk:** orta–zor
- **Çeldiriciler:** “Kuvvetölçer iki ucundaki ağırlıkların toplamını gösterir” (İpin her yerindeki gerilmenin aynı olduğunu bilmeme)
- **Öğrenci hataları:** Bileşenlere ayırmada sin/cos karıştırmak `VECTOR_ERROR`
- **Kanıt:** kitap s.141 ÖD-27
- **Kapsam notu:** Kuvvet dengesi; tork içermeyen (noktasal cisim) dengeyle sınırlı. Tork 12. sınıf.

### 024 · Sürtünmesiz eğik düzlemde hareket

- **Ölçülen:** FİZ.11.1.5 c `KB2.14.SB3`
- **Yapı:** Sürtünmesiz eğik düzlemde serbest bırakılan ya da itilen cismin ivmesi, normal kuvveti ya da hızı sorulur.
- **Uyarıcı:** DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “Normal kuvvet ağırlığa eşittir” (Eğik düzlemde N = mg cosθ olduğunu bilmeme); “Ağır cisim daha büyük ivmeyle kayar” (İvmenin kütleden bağımsızlığını bilmeme)
- **Öğrenci hataları:** sin ile cos'u karıştırmak `VECTOR_ERROR`
- **Kanıt:** kitap s.60 Örnek

### 025 · Aynı ivmeli bağlı cisimler (ip-makara, birlikte itilen bloklar)

- **Ölçülen:** FİZ.11.1.5 b `KB2.14.SB2`, FİZ.11.1.5 c `KB2.14.SB3`
- **Yapı:** İple ya da temasla bağlı, aynı ivmeyle hareket eden cisimlerin ortak ivmesi ve ip gerilmesi/temas kuvveti sorulur.
- **Uyarıcı:** DIAGRAM, EXPERIMENT · **Zorluk:** orta–zor
- **Çeldiriciler:** “İp gerilmesi asılı cismin ağırlığına eşittir” (Sistem ivmeli iken dengede gibi düşünme); “Temas kuvveti uygulanan kuvvete eşittir” (Kütle payını hesaba katmama)
- **Öğrenci hataları:** İç kuvveti (ip gerilmesi) dış kuvvet gibi toplamak `CONCEPTUAL_ERROR`; Tek cisim denkleminde yanlış kütle kullanmak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.142 ÖD-28; kitap s.61 Örnek
- **Kapsam notu:** Programa göre yalnız aynı ivmeli sistemler; farklı ivmeli (kayan üst blok, hareketli makara) sistem hesapları kapsam dışı.

### 026 · İvmeli araçta asılı cismin sapması

- **Ölçülen:** FİZ.11.1.5 c `KB2.14.SB3`
- **Yapı:** Hızlanan/yavaşlayan araçta asılı cismin düşeyle yaptığı açı ile aracın ivmesi ilişkilendirilir.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta–zor
- **Çeldiriciler:** “Cisim ivme yönünde sapar” (Sapma yönünü yanlış belirleme); “Açı kütleye bağlıdır” (tanθ = a/g'de kütlenin sadeleştiğini görmeme)
- **Öğrenci hataları:** tanθ yerine sinθ kullanmak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.63 Örnek; kitap s.64 25. Alıştırma

### 027 · İvmeli sistemde görünür ağırlık (asansör, g-kuvveti)

- **Ölçülen:** FİZ.11.1.5 c `KB2.14.SB3`
- **Yapı:** İvmeli hareket eden asansörde tartının gösterdiği değer ya da pilotun hissettiği 'g-kuvveti' sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, TEXT, GRAPH · **Zorluk:** orta
- **Çeldiriciler:** “Sabit hızla yukarı çıkan asansörde tartı daha büyük gösterir” (Hız ile ivmeyi karıştırma); “Tartı her zaman ağırlığı gösterir” (Tartının normal kuvveti ölçtüğünü bilmeme)
- **Öğrenci hataları:** İvme yönünü hareket yönü sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.148 ÖD-38

## FİZ.11.1.6

### 028 · Sürtünme türünün belirlenmesi (statik / kinetik)

- **Ölçülen:** FİZ.11.1.6 a `KB2.7.SB1`
- **Yapı:** Durgun ama harekete zorlanan, kayan ve kaymadan dönen cisimlerde sürtünmenin türü belirlenir.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Hareket eden her cisme kinetik sürtünme etki eder” (Dönerek ötelemede sürtünmenin statik olduğunu bilmeme)
- **Öğrenci hataları:** Hareketi kaymayla özdeşleştirmek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.65 6. Etkinlik; program “dönerek öteleme hareketi yapmakta olan cisimlere e…”

### 029 · Sürtünme kuvvetinin yönü

- **Ölçülen:** FİZ.11.1.6 a `KB2.7.SB1`
- **Yapı:** Yürüyen insan, hızlanan araç tekerleği, duvara bastırılan kitap, bant üzerindeki kutu gibi durumlarda sürtünmenin yönü sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “Sürtünme her zaman hareket yönüne zıttır” (Sürtünmenin bağıl harekete/eğilime zıt olduğunu bilmeme)
- **Öğrenci hataları:** Hareket yönüne göre değil kayma eğilimine göre yön belirlememek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.138 ÖD-23

### 030 · Statik ve kinetik sürtünmenin karşılaştırılması

- **Ölçülen:** FİZ.11.1.6 b `KB2.7.SB2`, FİZ.11.1.6 c `KB2.7.SB3`
- **Yapı:** Statik ve kinetik sürtünmenin benzer ve farklı özellikleri (bağlı oldukları değişkenler, büyüklük ilişkisi) yargılarla sorulur.
- **Uyarıcı:** TEXT, TABLE · **Zorluk:** kolay
- **Çeldiriciler:** “Statik sürtünme her zaman sabittir” (Statik sürtünmenin uygulanan kuvvetle değiştiğini bilmeme); “Kinetik sürtünme maksimum statikten büyüktür” (Büyüklük ilişkisini ters bilme)
- **Öğrenci hataları:** Maksimum statik ile anlık statik sürtünmeyi karıştırmak `CONCEPTUAL_ERROR`
- **Kanıt:** program “statik ve kinetik sürtünme kuvvetinin benzerlikler…”

## FİZ.11.1.7

### 031 · Sürtünme kuvveti – uygulanan kuvvet grafiği

- **Ölçülen:** FİZ.11.1.7 a `FBAB10.SB1`, FİZ.11.1.7 b `FBAB10.SB2`
- **Yapı:** f–F grafiğinde statik bölge, harekete geçme eşiği ve kinetik bölge yorumlanır; katsayılar ya da cismin durumu sorulur.
- **Uyarıcı:** GRAPH · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Statik bölgede sürtünme sabittir” (Grafiğin eğimli kısmını yanlış okuma); “Cisim harekete geçince sürtünme artar” (Kinetik değerin maksimum statikten küçük olduğunu bilmeme)
- **Öğrenci hataları:** Eşik noktası ile kinetik değeri karıştırmak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.139 ÖD-25; kitap s.85 Kontrol Noktası; program “sürtünme kuvveti-uygulanan kuvvet grafiğini…”

### 032 · Uygulanan kuvvete göre hareket durumu ve sürtünmenin değeri

- **Ölçülen:** FİZ.11.1.7 b `FBAB10.SB2`
- **Yapı:** Maksimum statik ve kinetik sürtünme değerleri bilinen cisme farklı kuvvetler uygulanır; her durumda sürtünmenin değeri ve ivme sorulur.
- **Uyarıcı:** TABLE, TEXT · **Zorluk:** orta
- **Çeldiriciler:** “Cisim durgunken sürtünme her zaman maksimum statik değerdedir” (f_s = f_s,max sanma); “Uygulanan kuvvet kinetik değeri aşınca cisim harekete geçer” (Eşiğin maksimum statik olduğunu bilmeme)
- **Öğrenci hataları:** Durgun cisimde ivmeyi F − f_s,max ile hesaplayıp negatif bulmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.138 ÖD-22

### 033 · Yatay zeminde sürtünmeli hareketin ivmesi

- **Ölçülen:** FİZ.11.1.7 b `FBAB10.SB2`
- **Yapı:** Yatay kuvvetle çekilen/itilen ya da ilk hızla kaymaya bırakılan cismin ivmesi, durma süresi veya yolu sorulur.
- **Uyarıcı:** TEXT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Cisim durana kadar sürtünme uygulanan kuvvete eşittir” (Kinetik sürtünmenin sabit olduğunu bilmeme)
- **Öğrenci hataları:** Normal kuvveti yanlış almak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.135 ÖD-16

### 034 · Açılı kuvvetin normal kuvvete ve sürtünmeye etkisi

- **Ölçülen:** FİZ.11.1.7 b `FBAB10.SB2`
- **Yapı:** Yatayla açı yapan kuvvetle çekilen/itilen cisimde normal kuvvet ve sürtünmenin değişimi sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Normal kuvvet her durumda mg'dir” (Kuvvetin düşey bileşenini hesaba katmama)
- **Öğrenci hataları:** Düşey bileşeni normal kuvvete eklemek yerine çıkarmak (ya da tersi) `SIGN_ERROR`
- **Kanıt:** kitap s.137 ÖD-20; kitap s.135 ÖD-17
- **Kapsam notu:** Program destekleme önerisinde ek düşey kuvvet olmayan örnekler önerir; çekirdek kapsam ve ders kitabı açılı kuvveti içerir.

### 035 · Eğik düzlemde sürtünme katsayısının deneyle bulunması

- **Ölçülen:** FİZ.11.1.7 a `FBAB10.SB1`, FİZ.11.1.7 b `FBAB10.SB2`
- **Yapı:** Eğimi ayarlanabilen düzlemde cismin kaymaya başladığı ya da sabit hızla kaydığı açıdan katsayı bulunur; farklı yüzeyler karşılaştırılır.
- **Uyarıcı:** EXPERIMENT, DIAGRAM, TABLE · **Zorluk:** orta–zor
- **Çeldiriciler:** “Katsayı cismin kütlesine bağlıdır” (k'nın yüzey çiftine bağlı olduğunu bilmeme); “Kaymaya başlama açısı kinetik katsayıyı verir” (Statik ve kinetik eşiklerini karıştırma)
- **Öğrenci hataları:** tanθ yerine sinθ almak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.136 ÖD-18; kitap s.82 Örnek

### 036 · Duvara bastırılarak dengede tutulan cisim

- **Ölçülen:** FİZ.11.1.7 b `FBAB10.SB2`
- **Yapı:** Düşey duvara yatay kuvvetle bastırılan cismin düşmemesi için gereken en küçük kuvvet ya da sürtünmenin değeri sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Bastırma kuvveti artınca sürtünme de artar (cisim dengedeyken)” (Statik sürtünmenin ağırlığa eşit kaldığını görmeme)
- **Öğrenci hataları:** Normal kuvveti ağırlık sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.84 Örnek; kitap s.138 ÖD-23

### 037 · Üst üste konmuş blokların birlikte hareketi

- **Ölçülen:** FİZ.11.1.7 b `FBAB10.SB2`
- **Yapı:** Üst üste konmuş bloklardan birine kuvvet uygulanır; blokların birlikte hareket edebileceği en büyük kuvvet ya da üst bloğa etki eden sürtünme sorulur.
- **Uyarıcı:** DIAGRAM · **Zorluk:** zor
- **Çeldiriciler:** “Üst bloğa etki eden sürtünme her zaman maksimum değerdedir” (Statik sürtünmenin gerektiği kadar olduğunu bilmeme)
- **Öğrenci hataları:** Ortak ivmeyi bulmadan üst blok için sürtünmeyi hesaplamak `METHOD_SELECTION_ERROR`
- **Kanıt:** kitap s.139 ÖD-24
- **Kapsam notu:** Bloklar birlikte (aynı ivmeyle) hareket ettiği sürece kapsamda; kayma sonrası farklı ivmeli hesap kapsam dışı.

### 038 · Sürtünmenin bağlı olduğu değişkenlerin veriden bulunması

- **Ölçülen:** FİZ.11.1.7 a `FBAB10.SB1`
- **Yapı:** Farklı kütle, yüzey alanı ve yüzey türleriyle yapılan deney verilerinden sürtünmenin hangi değişkenlere bağlı olduğu çıkarılır.
- **Uyarıcı:** TABLE, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Temas yüzey alanı büyüdükçe sürtünme artar” (Alan-sürtünme yanılgısı)
- **Öğrenci hataları:** Birden fazla değişkenin değiştiği satırları karşılaştırmak `TABLE_READING_ERROR`
- **Kanıt:** kitap s.70 7. Etkinlik; kılavuz s.85

## FİZ.11.1.8

### 039 · Limit hıza ulaşan cismin hız-zaman grafiği

- **Ölçülen:** FİZ.11.1.8 c `FBAB8.SB3`
- **Yapı:** Paraşütçü ya da yağmur damlasının ϑ-t grafiği verilir; ivmenin değişimi, paraşütün açıldığı an ve kuvvetlerin büyüklük ilişkisi yorumlanır.
- **Uyarıcı:** GRAPH, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Paraşüt açılınca paraşütçü yukarı doğru hareket eder” (Hız azalmasını yön değişimi sanma); “Limit hızda ivme g'dir” (Net kuvvetin sıfır olduğunu görmeme); “Limit hıza ulaşınca hava direnci ağırlıktan büyüktür” (Dengeyi yanlış kurma)
- **Öğrenci hataları:** Grafiğin eğiminin azalmasını hızın azalması sanmak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.149 ÖD-39; program “Profesyonel bir paraşütçünün uçaktan atlama deneyi…”

### 040 · Limit hızı etkileyen değişkenlerin karşılaştırılması · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.1.8 a `FBAB8.SB1`, FİZ.11.1.8 c `FBAB8.SB3`
- **Yapı:** Farklı kütle, boyut ve şekildeki cisimlerin limit hızları sıralanır ya da oranlanır.
- **Uyarıcı:** DIAGRAM, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Kütlesi büyük olanın limit hızı küçüktür” (Ağırlık arttıkça daha büyük direnç gerektiğini görmeme); “Limit hız yükseklikle artar” (Limit hızın yükseklikten bağımsız olduğunu bilmeme)
- **Öğrenci hataları:** ϑ ∝ √(m/A) yerine ϑ ∝ m/A almak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.144 ÖD-31
- **Kapsam notu:** Program: yorumlamalarla sınırlı (CALC_EXCLUDED). Ders kitabı oran içeren ölçme sorusu kullanıyor; sayısal oran program–kitap çelişkisi kapsamında.

### 041 · Limit hızın günlük hayat ve doğadaki örnekleri

- **Ölçülen:** FİZ.11.1.8 a `FBAB8.SB1`, FİZ.11.1.8 c `FBAB8.SB3`
- **Yapı:** Yağmur damlası, karahindiba tohumu, tohum topu, bisikletçi gibi bağlamlarda limit hızın rolü ve değişkenleri yorumlanır.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Hava direnci olmasaydı yağmur damlası yere aynı hızla ulaşırdı” (Limit hızın koruyucu rolünü görmeme)
- **Öğrenci hataları:** Bağlamdaki değişkeni (kesit alanı, şekil) fiziksel niceliğe bağlayamamak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** kitap s.143 ÖD-30; kitap s.145 ÖD-33; kitap s.149 ÖD-40

### 042 · Direnç kuvvetinin değişkenlerinin veri setinden çıkarılması · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.1.8 b `FBAB8.SB2`, FİZ.11.1.8 c `FBAB8.SB3`
- **Yapı:** Simülasyon ya da deneyden elde edilen kesit alanı–hız–direnç verilerinden ilişki kurulur.
- **Uyarıcı:** TABLE, EXPERIMENT, DATA_SET · **Zorluk:** orta
- **Çeldiriciler:** “Direnç hızla doğru orantılı artar” (Karesel ilişkiyi doğrusal sanma)
- **Öğrenci hataları:** Kontrol değişkenini sabit tutmadan karşılaştırma `TABLE_READING_ERROR`
- **Kanıt:** program “limit hıza etki eden değişkenlerle ilgili veri top…”; kitap s.90 Tablo 1.2; kılavuz s.115
- **Kapsam notu:** Sayısal model yerine veri tablosu üzerinden orantı — kılavuzun 'veriden çıkarım' yaklaşımıyla programın hesap sınırına uygun.

## FİZ.11.1.9

### 043 · Düzgün çembersel harekette hız vektörünün yönü

- **Ölçülen:** FİZ.11.1.9 b `KB2.16.3.SB2`, FİZ.11.1.9 c `KB2.16.3.SB3`
- **Yapı:** Çembersel yörüngenin farklı noktalarında hız vektörünün yönü ve yarıçap vektörüyle ilişkisi sorulur.
- **Uyarıcı:** DIAGRAM · **Zorluk:** kolay
- **Çeldiriciler:** “Hız vektörü merkeze doğrudur” (Hız ile ivme yönünü karıştırma); “Sürat sabit olduğundan hız da sabittir” (Hızın vektör olduğunu unutma)
- **Öğrenci hataları:** Dönme yönünü hesaba katmadan teğet yön çizmek `VECTOR_ERROR`
- **Kanıt:** kitap s.95 9. Etkinlik; kitap s.119 Kontrol Noktası

### 044 · İp koptuğunda cismin yörüngesi

- **Ölçülen:** FİZ.11.1.9 c `KB2.16.3.SB3`
- **Yapı:** Çembersel dönen cismin ipi (ya da bağlantısı) koptuğunda izleyeceği yol sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Cisim merkezden dışa doğru (radyal) uçar” (Merkezkaç kuvvet yanılgısı); “Cisim kopma anından sonra eğri yol izlemeye devam eder” (Eylemsizliği bilmeme)
- **Öğrenci hataları:** Merkezkaç kuvvetini gerçek kuvvet sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.108 Alıştırma; kitap s.38 12. Alıştırma

### 045 · Farklı düzgün çembersel hareketlerin ortak özellikleri

- **Ölçülen:** FİZ.11.1.9 a `KB2.16.3.SB1`, FİZ.11.1.9 b `KB2.16.3.SB2`, FİZ.11.1.9 c `KB2.16.3.SB3`
- **Yapı:** Uydu, dönme dolap, saat akrebi gibi farklı hareketlerin ortak özelliklerinden düzgün çembersel hareket hakkında genelleme yapılır.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Düzgün çembersel harekette ivme yoktur” (Sabit süratle ivmesizliği özdeşleştirme)
- **Öğrenci hataları:** Sürat ile hızı karıştırmak `CONCEPTUAL_ERROR`
- **Kanıt:** program “Türksat uydularının Dünya etrafındaki dolanımı…”

## FİZ.11.1.10

### 046 · Periyot, frekans, çizgisel ve açısal hız hesabı

- **Ölçülen:** FİZ.11.1.10 a `FBAB10.SB1`, FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Dönen sistemin periyot/frekansı ile çizgisel ve açısal hızları arasında hesap yapılır.
- **Uyarıcı:** TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Merkeze yakın noktanın açısal hızı daha küçüktür” (Aynı cisimde ω'nin aynı olduğunu bilmeme); “Frekans iki katına çıkınca periyot da iki kat olur” (Ters orantıyı bilmeme)
- **Öğrenci hataları:** Dakikadaki devri saniyeye çevirmemek `UNIT_ERROR`; Çap ile yarıçapı karıştırmak `CARELESS_ERROR`
- **Kanıt:** kitap s.104 Örnek

### 047 · Kayış, dişli ya da ortak milli tekerleklerde hız ilişkisi

- **Ölçülen:** FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Kayışla ya da dişliyle bağlı (çizgisel süratler eşit) veya ortak mile bağlı (açısal hızlar eşit) tekerlerde frekans, periyot ya da hız oranı sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Kayışla bağlı tekerlerin açısal hızları eşittir” (Bağlantı türüne göre eşit niceliği karıştırma); “Büyük tekerleğin frekansı büyüktür” (f ∝ 1/r ilişkisini ters kurma)
- **Öğrenci hataları:** Eşit olan niceliği yanlış seçmek `METHOD_SELECTION_ERROR`
- **Kanıt:** kitap s.105 39. Alıştırma

### 048 · Yatay düzlemde düzgün çembersel hareket (ip, yay, normal)

- **Ölçülen:** FİZ.11.1.10 a `FBAB10.SB1`, FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Yatay sürtünmesiz düzlemde ipe/yaya bağlı dönen cismin merkezcil ivmesi, ip gerilmesi ya da hızı sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “İp gerilmesi ağırlığa eşittir” (Yatay düzlemde ağırlığın merkezcil kuvvete katılmadığını görmeme); “Yarıçap iki katına çıkınca (aynı hızda) kuvvet iki katına çıkar” (1/r ilişkisini bilmeme)
- **Öğrenci hataları:** ϑ ve ω ile yazılan bağıntılarda r'nin üssünü karıştırmak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.108 Yatay Düzlemde; kitap s.109 Örnek

### 049 · Dönen platformda kaymadan durma

- **Ölçülen:** FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Dönen platformdaki cismin kaymadan dönebileceği en büyük açısal hız ya da en uzak konum sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “Cisim kütlesi büyükse daha erken kayar” (Kütlenin sadeleştiğini görmeme); “Merkeze yakın cisim önce kayar” (a = ω²r'de r etkisini ters kurma)
- **Öğrenci hataları:** Kinetik katsayıyı kullanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.109 41. Alıştırma

### 050 · Düşey düzlemde çembersel harekette ip gerilmesi

- **Ölçülen:** FİZ.11.1.10 a `FBAB10.SB1`, FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** İpe bağlı cismin tepe, dip ve yan noktalarında ip gerilmesi ya da ipin kopacağı nokta sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Tepe noktasında gerilme en büyüktür” (Ağırlığın tepede merkeze yönelik olduğunu yanlış yorumlama); “Tüm noktalarda gerilme eşittir” (Ağırlığın katkısını hesaba katmama)
- **Öğrenci hataları:** Tepede ağırlığın yönünü yanlış almak `SIGN_ERROR`
- **Kanıt:** kitap s.110 Tablo 1.3; kitap s.111 42. Alıştırma

### 051 · Düşey çemberin tepesinden geçebilme koşulu

- **Ölçülen:** FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Kovadaki suyun dökülmemesi ya da ipe bağlı cismin tepeden geçebilmesi için gereken en küçük hız sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “Su, merkezkaç kuvveti nedeniyle dökülmez” (Merkezkaç kuvvet yanılgısı); “En küçük hız kovadaki suyun kütlesine bağlıdır” (Kütlenin sadeleştiğini görmeme)
- **Öğrenci hataları:** Koşulu T = 0 yerine T = mg kurmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.111 Cevap

### 052 · Tümsek ya da çukur yolun tepesinde/dibinde normal kuvvet

- **Ölçülen:** FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Tümsek köprünün tepesinden ya da çukurun dibinden geçen aracın zemine uyguladığı kuvvet ya da yolu terk etme hızı sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “Tümsek tepesinde normal kuvvet ağırlıktan büyüktür” (Merkezcil ivmenin yönünü (aşağı) bilmeme)
- **Öğrenci hataları:** mg − N yerine N − mg yazmak `SIGN_ERROR`
- **Kanıt:** kitap s.145 ÖD-34

### 053 · Yatay virajda kaymadan dönme

- **Ölçülen:** FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Yatay virajda merkezcil kuvveti statik sürtünmenin sağladığı aracın kaymadan dönebileceği en büyük hız sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “Ağır araç daha düşük hızda kayar” (Kütlenin sadeleştiğini görmeme); “Virajda araca dışa doğru kuvvet etki eder” (Merkezkaç kuvvet yanılgısı)
- **Öğrenci hataları:** Kinetik katsayı kullanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.117 45. Alıştırma

### 054 · Eğimli virajda güvenli dönme

- **Ölçülen:** FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Sürtünmesiz eğimli virajda güvenli hız, eğim açısı ya da yarıçap sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta–zor
- **Çeldiriciler:** “Güvenli hız aracın kütlesine bağlıdır” (Kütlenin sadeleştiğini görmeme); “Merkezcil kuvveti normal kuvvetin düşey bileşeni sağlar” (Bileşenleri karıştırma)
- **Öğrenci hataları:** tanθ yerine sinθ almak `VECTOR_ERROR`
- **Kanıt:** kitap s.116 Eğimli Virajda; kitap s.146 ÖD-36

### 055 · Dönen silindir ve düzeneklerde merkezcil kuvvet kaynağının belirlenmesi

- **Ölçülen:** FİZ.11.1.10 a `FBAB10.SB1`
- **Yapı:** Dönen silindir (rotor), asansör hız düzenleyici gibi düzeneklerde merkezcil kuvveti hangi kuvvetin sağladığı ve koşullar sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta–zor
- **Çeldiriciler:** “Merkezcil kuvvet ayrı bir kuvvettir” (Merkezcil kuvveti ayrı kuvvet sanma)
- **Öğrenci hataları:** Merkezcil kuvveti sağlayan kuvveti yanlış belirlemek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.143 ÖD-29; kitap s.146 ÖD-35

### 056 · Düzgün çembersel hareket değişkenlerinin veri setinden modellenmesi

- **Ölçülen:** FİZ.11.1.10 a `FBAB10.SB1`, FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Merkezcil kuvvetin kütle, sürat ve yarıçapla değişimini gösteren deney verisi ya da grafiği verilir; ilişki kurulur, eksik değer bulunur ya da hangi grafiğin doğrusal olacağı sorulur.
- **Uyarıcı:** TABLE, GRAPH, EXPERIMENT, DATA_SET · **Zorluk:** orta–zor
- **Çeldiriciler:** “F_m sürat ile doğru orantılıdır” (Karesel ilişkiyi doğrusal sanma); “F_m yarıçapla doğru orantılıdır (sabit süratte)” (1/r ilişkisini ters kurma)
- **Öğrenci hataları:** İki değişkenin birlikte değiştiği satırları karşılaştırmak `TABLE_READING_ERROR`; Doğrusallaştırılmış grafikte ekseni yanlış okumak `GRAPH_READING_ERROR`
- **Kanıt:** program “Farklı veri setleri ile hesaplamalar yaparak düzgü…”; kılavuz s.115

### 057 · Ray sisteminde çembersel hareket (lunapark rayı, viraj rayı) · **hesap kapsam dışı**

- **Ölçülen:** FİZ.11.1.10 b `FBAB10.SB2`
- **Yapı:** Ray üzerinde düşey çemberde dönen vagonun normal kuvveti ya da gerekli hızı hesaplanır.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** zor
- **Çeldiriciler:** “Vagon merkezkaç kuvveti sayesinde düşmez” (Merkezkaç kuvvet yanılgısı)
- **Öğrenci hataları:** Raydan normal kuvvetin yönünü yanlış almak `SIGN_ERROR`
- **Kanıt:** program “Ray sisteminde çembersel hareketle ilgili matemati…”
- **Kapsam notu:** Program ray sistemlerinde matematiksel işlemi açıkça dışlıyor; yalnız nitel yorum kapsamda. Eski kaynaklarda sık görülür.

## FİZ.11.2.1

### 058 · Elektriksel kuvvetin bağlı olduğu değişkenlerin veri tablosu ve grafikten bulunması · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.1 a `FBAB10.SB1`
- **Yapı:** Simülasyon ya da deneyle elde edilen F–q₁, F–q₂, F–d verileri (tablo ya da grafik) verilir; hangi değişkenle doğru, hangisiyle ters (kareyle) orantılı olduğu, eksik tablo değeri ya da doğrusal çıkacak grafik sorulur. Formül kullanılmaz; kontrol edilen değişken dışındaki niceliklerin sabit tutulduğu satırlar karşılaştırılır.
- **Uyarıcı:** TABLE, GRAPH, EXPERIMENT, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “F, uzaklıkla doğru orantılıdır (uzaklaştıkça artar)” (Kuvvet–uzaklık ilişkisini ters kurma); “F, d ile ters orantılıdır (d iki katına çıkınca yarıya iner)” (Ters kare ilişkisini ters (doğrusal) orantıya indirgeme); “F, yüklerin toplamıyla doğru orantılıdır” (Çarpım ile toplamı karıştırma); “Satırlarda q ve d birlikte değiştiği halde yalnız q'nun etkisi yorumlanır” (Kontrol değişkeni ilkesini uygulamama)
- **Öğrenci hataları:** İki değişkenin birlikte değiştiği satırları karşılaştırmak `TABLE_READING_ERROR`; Doğrusal olmayan F–d grafiğini doğrusal orantı sanmak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.158 10. adım; kitap s.157 5. adım; program “Gruplar etkileşimli bir simülasyon aracılığıyla ve…”; program “Gruplardan tablodaki verilere dayalı olarak grafik…”; kılavuz s.114
- **Kapsam notu:** Program Coulomb Yasası'nı hesapsız (oran/yön) ele alır; bu aile formül değil veri örüntüsü üzerinden ilişkiyi ölçer.

### 059 · Coulomb modeli üzerinden genelleme: yük, uzaklık ve ortam değişince kuvvetin kaç katı olduğu · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.1 b `FBAB10.SB2`
- **Yapı:** Bir referans durumda kuvvet F olarak verilir; yüklerden biri/ikisi, uzaklık ya da ortam (Coulomb sabiti) değiştirilir; yeni kuvvet 'kaç F' olarak sorulur ya da birden çok durum tablosu sıralanır. Sayısal hesap yok, yalnız çarpansal (oran) akıl yürütme.
- **Uyarıcı:** TABLE, DIAGRAM, EXPERIMENT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “d iki katına çıkınca kuvvet yarıya iner” (Ters kare yerine ters orantı); “Yüklerin ikisi de 2 katına çıkınca kuvvet 2 katına çıkar” (Çarpımsal bağımlılığı toplamsal sanma); “Ortam değişince yükler değiştiği için kuvvet değişir” (Ortamın etkisini Coulomb sabiti ile ilişkilendirememe); “Yükü işaret değiştirince kuvvetin büyüklüğü azalır” (Yön ile büyüklüğü karıştırma)
- **Öğrenci hataları:** Çarpanları toplamak (2 + 2 = 4 yerine 2 · 2 = 4 mantığını kurmamak ya da tersi) `CONCEPTUAL_ERROR`; d'nin 2 katında F'yi 1/2 almak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.159 14. adım tablosu; kitap s.163 1. Alıştırma; program “Öğrenciler, Coulomb Yasası ile ilgili farklı probl…”; program “Gruplar elektrik yüklü bir yalıtkanı belli mesafel…”
- **Kapsam notu:** Program–kitap uyumlu: kitap da 'kaç F' oran sorularıyla ilerler. Ünite sonu ÖD-3'teki 16 N gibi sayısal verilerin yer aldığı sorular için 'coulomb-collinear-net-force' ailesine bak.

### 060 · İki yük arasındaki elektriksel kuvvetin yönü ve karşılıklı eşitliği · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.1 b `FBAB10.SB2`
- **Yapı:** Aynı ya da zıt cinsli, farklı büyüklükte noktasal yüklerin birbirine uyguladığı kuvvetlerin yönü çizilir; büyüklüklerinin karşılaştırılması ya da bir yükün hangi yöne hareket edeceği sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Büyük yük, küçük yüke daha büyük kuvvet uygular” (Etki–tepki ilkesinin elektriksel kuvvete uygulanabilirliğini bilmeme); “Zıt işaretli yükler arasındaki kuvvet itmedir” (Aynı cins itme / zıt cins çekme kuralını karıştırma); “Yükler birbirine temas etmediği için aralarında kuvvet yoktur” (Temassız kuvvet kavramını bilmeme)
- **Öğrenci hataları:** Yük işaretini değil büyüklüğünü esas alıp yönü çizmek `VECTOR_ERROR`; Kuvveti uygulayan ve maruz kalan cisimleri karıştırmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** kitap s.162 Örnek; kitap s.164 3. Alıştırma; program “Öğretmen elektriksel kuvvetin günlük hayattaki rol…”

### 061 · Doğrusal dizilmiş yüklerde bileşke kuvvet ve denge koşulu · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.1 b `FBAB10.SB2`
- **Yapı:** Aynı doğru üzerinde üç (ya da dört) noktasal yükten birine etki eden bileşke kuvvet, bir referans kuvvet (F) cinsinden istenir; ya da bir yükün dengede kalması için gereken yük oranı / konum / işaret sorulur.
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Bileşke kuvvet, kuvvetlerin büyüklüklerinin toplamıdır” (Yönleri hesaba katmadan skaler toplama); “Daha uzaktaki yük, daha yakındakinden daha büyük kuvvet uygular” (Ters kare bağımlılığını tersine çevirme); “Dengede bırakılan yükün iki yanındaki yükler eşit büyüklükte olmalıdır” (Uzaklık farkını denge koşuluna katmama)
- **Öğrenci hataları:** Kuvvetleri yön işareti vermeden toplamak `SIGN_ERROR`; d, 2d uzaklıklarında F ∝ 1/d yazmak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.163 1. Alıştırma; kitap s.276 ÖD-3; kitap s.274 ÖD-1; program “Öğrenciler, Coulomb Yasası ile ilgili farklı probl…”
- **Kapsam notu:** Program–kitap çelişkisi: kitap ÖD-3'te 16 N gibi sayısal değer ve 'kaç N' hesap istiyor; programa uygun biçim yalnız oran / F cinsinden ifadedir. Soruların ana akışı F cinsinden kurulmuştur.

### 062 · Serbest yüklerin hareketi: kuvvet, ivme ve kütle ilişkisi · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.1 b `FBAB10.SB2`
- **Yapı:** Boşlukta serbest bırakılan iki yük (ya da iplerle asılı yüklü cisimler) için kuvvetin zamanla değişimi, ivme karşılaştırması, çarpışma/buluşma noktası ya da denge konumundaki ip açıları sorulur.
- **Uyarıcı:** TEXT, DIAGRAM, EXPERIMENT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Hafif parçacığa uygulanan kuvvet daha büyüktür” (Etki–tepki ve ivme–kuvvet ayrımını yapamama); “Yükler yaklaşırken kuvvet sabit kalır” (Mesafe bağımlılığını dinamik duruma uygulayamama); “Yükler orta noktada buluşur” (Eşit kuvvetin eşit ivme anlamına geldiğini sanma)
- **Öğrenci hataları:** Kuvvet eşitliğinden ivme eşitliği çıkarmak `CONCEPTUAL_ERROR`; İvmeyi sabit kabul edip kinematik denklem kullanmak `METHOD_SELECTION_ERROR`
- **Kanıt:** kitap s.165 4. Alıştırma; kitap s.164 3. Alıştırma
- **Kapsam notu:** Kuvvet–hareket birleşimi; Ünite 1'in Newton yasaları bilgisini ön koşul alır. Hesap yok, nitel/oran düzeyinde.

## FİZ.11.2.2

### 063 · Elektriksel alan büyüklüğünün yük ve uzaklıkla ilişkisinin veri tablosu ve grafikten bulunması · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.2 a `FBAB10.SB1`
- **Yapı:** Simülasyondaki sensör ve mezura ile toplanmış E–q ve E–d verileri (tablo ya da grafik) verilir; E'nin hangi niceliklerle doğru/ters orantılı olduğu, eksik değer ya da hangi grafiğin doğrusal olacağı sorulur; test yükünün alana etkisi de yorumlanır.
- **Uyarıcı:** TABLE, GRAPH, EXPERIMENT, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “E, uzaklıkla ters orantılıdır (1/d)” (Ters kare yerine ters orantı); “Yük büyüdükçe E azalır” (Alan–yük ilişkisini ters kurma); “E, alandaki test yüküne bağlıdır” (E'nin kaynak yüke ait olduğunu, test yükünden bağımsız olduğunu bilmeme)
- **Öğrenci hataları:** Çok değişkenli satırlarda etkiyi ayırmadan yorumlamak `TABLE_READING_ERROR`; E–d grafiğini doğrusal sanmak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.167 9.–10. adım; kitap s.167 10. adım; program “Öğrenciler hipotezlerini test edebilecekleri bir s…”; program “Öğrenciler, toplanan verilerle oluşturulan grafikl…”; kılavuz s.115
- **Kapsam notu:** Program yalnız hesapsız (oran/yön) düzeyi ister; veri örüntüsünden ilişki bulma bu düzeydedir.

### 064 · Elektriksel alan yönü ve alan çizgileri: yük işareti, yük büyüklüğü ve çizgi sıklığı yorumu · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.2 b `FBAB10.SB2`
- **Yapı:** Alan çizgisi şeması (ya da yağ üzerindeki irmik/tane dizilimi görüntüsü) verilir; yüklerin işaretleri, büyüklükleri, belirli noktalarda alanın yönü ve çizgi sıklığına göre alanın büyüklüğü sorulur.
- **Uyarıcı:** DIAGRAM, EXPERIMENT, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Alan çizgileri negatif yükten dışarı doğrudur” (Alan yönü kuralını ters bilme); “Alan çizgileri birbirini kesebilir” (Her noktada tek alan yönü olduğunu bilmeme); “Çizgiler seyrek bölgede alan büyüktür” (Çizgi sıklığı–alan büyüklüğü ilişkisini ters kurma); “Alan çizgisi yüklü cismin hareket yolunu gösterir” (Alan çizgisini yörünge sanma)
- **Öğrenci hataları:** Yüklerin işaretini çizgi yönüne bakmadan söylemek `CONCEPTUAL_ERROR`; Çizgi sayısı farkını yük büyüklüğü oranına çevirmeye çalışmak `METHOD_SELECTION_ERROR`
- **Kanıt:** kitap s.173 6. Alıştırma; kitap s.185 Özet; program “Gruplar elektrik yüklü yalıtkan çubuğu belli mesaf…”

### 065 · Noktasal yüklerin bir noktada oluşturduğu bileşke alanın yönü ve büyüklük karşılaştırması · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.2 b `FBAB10.SB2`
- **Yapı:** İki ya da daha çok noktasal yükün bulunduğu düzenekte seçilen noktalarda bileşke alanın yönü çizilir; büyüklükler E cinsinden karşılaştırılır; alan değerinin sıfır olduğu nokta aranır.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Alanlar skaler toplanır; iki eşit yükün ortasında alan 2E'dir” (Alanın vektörel olduğunu unutma); “Zıt işaretli yüklerin ortasında alan sıfırdır” (Yönleri karşılaştırmadan 'zıt yük = sıfır' sanma); “Yüke daha yakın noktada alan her zaman sıfırdır” (Alan ile potansiyeli/yük kuvvetini karıştırma); “Bileşke alan sıfırsa orada hiç alan çizgisi yoktur” (Alan çizgisi kavramını yanlış yorumlama)
- **Öğrenci hataları:** Alan yönlerini işaretsiz toplamak `SIGN_ERROR`; Uzaklığı ikiye katlayınca alanı yarıya indirmek `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.172 Örnek; kitap s.174 7. Alıştırma; kitap s.173 6. Alıştırma ç; program “matematiksel hesaplara girmeden elektriksel alanla…”
- **Kapsam notu:** Program yalnız oran/yön düzeyi ister; bu aile yük/uzaklık oranlarıyla E cinsinden karşılaştırma ve yön üzerine kuruludur.

### 066 · Noktasal yük alanının yük, uzaklık ve ortam değişince oranı; E'nin test yükünden bağımsızlığı · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.2 b `FBAB10.SB2`
- **Yapı:** Bir noktadaki alan E olarak verilir; kaynak yük, uzaklık ya da ortam değişir; yeni alan 'kaç E' olarak ya da E'yi artırma yolları sorulur. Doğru-yanlış ifadelerin değerlendirilmesi ve elektroskop yapraklarının uzaklıkla değişimi de bu ailededir.
- **Uyarıcı:** TEXT, TABLE, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Yükten uzaklaşınca alan artar” (Alan–uzaklık ilişkisini ters kurma); “Test yükü büyürse alan da büyür” (Alan ile test yüküne etki eden kuvveti karıştırma); “Alan yalnızca yük miktarına bağlıdır, ortamdan bağımsızdır” (Ortamın etkisini (k) dikkate almama); “Negatif yükün alanı yüke doğru olduğu için uzaklaştıkça artar” (Yönü büyüklükle karıştırma)
- **Öğrenci hataları:** Kare alma yerine uzaklığı doğrusal oranlamak `FORMULA_APPLICATION_ERROR`; E ile F'yi aynı nicelik saymak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.169 Değerlendirme 3; kitap s.169 Değerlendirme 2; program “Öğrenciler gözlemlerini elektriksel alan ile matem…”
- **Kapsam notu:** Kitap E = kq/d² ve E = F/q₀ formüllerini verir (Kontrol Noktası s.185); program hesapsız ele alır. Aile oran/yorum düzeyindedir.

### 067 · Paralel levhalar arasında düzgün alan: mesafe ve gerilim değişince alanın şekli ve büyüklüğü · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.2 b `FBAB10.SB2`
- **Yapı:** Zıt yüklü paralel levha sistemi için alan çizgileri çizilir; levhalar arası mesafe (d) ya da üretecin potansiyel farkı (V) değiştirildiğinde alanın büyüklüğü ve alan çizgilerinin sıklığı sorulur; bulut–yer sisteminin paralel levha modeli yorumlanır.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Levhalar arasındaki alan, pozitif levhaya yaklaştıkça artar” (Düzgün alanın her yerde aynı olduğunu bilmeme); “d artınca alan çizgileri sıklaşır” (Çizgi sıklığı–alan ilişkisini yanlış yorumlama); “Alan çizgileri negatif levhadan pozitif levhaya doğrudur” (Alan yönü kuralını ters bilme)
- **Öğrenci hataları:** E = V·d yazmak `FORMULA_SELECTION_ERROR`; V sabitken d büyüyünce E'nin de büyüyeceğini söylemek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.178 10. Alıştırma a; kitap s.176 Paralel levha; kitap s.177 9. Alıştırma
- **Kapsam notu:** Program–kitap çelişkisi: kitap 10. Alıştırma b'de q, V, d, m cinsinden sembolik ivme ve süre ifadesi istiyor (hesap); aile yalnız E = V/d'nin oran/yön yorumunu kapsar, sembolik türetim programın dışında tutulmuştur.

### 068 · Düzgün alan içinde sapan yüklü parçacık: levha ve yük işaretleri · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.2 b `FBAB10.SB2`
- **Yapı:** Düzgün alan bölgesine giren yüklü parçacıkların izlediği yollar ya da sapma yönleri verilir; levhaların yük cinsleri, parçacıkların yük işaretleri ve hangisinin q/m değerinin ya da yük miktarının daha büyük olduğu sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Elektron pozitif levhadan uzağa sapar” (Zıt işaretli çekme/itme kuralını yanlış uygulama); “Daha çok sapan parçacığın yük işareti daha büyüktür (pozitiftir)” (Sapma miktarını yük işaretiyle karıştırma); “Alana dik giren ve hiç sapmayan parçacık pozitif yüklüdür” (Sapmama ile yüksüzlük ilişkisini bilmeme)
- **Öğrenci hataları:** Kuvvetin yönünü alan yönüyle aynı almak (negatif yük için) `SIGN_ERROR`; Sapma miktarını yalnız yüke bağlamak, kütleyi göz ardı etmek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.176 Elektron tabancası; kitap s.275 ÖD-2
- **Kapsam notu:** Program yüklü parçacığa etki eden kuvveti ayrı bir çıktı yapmaz; burada yalnız alan yönü ve yük işareti ilişkisi (nitel) ölçülür.

### 069 · Düzgün alanda yüklü damla: ağırlık–elektriksel kuvvet dengesi ve hareket yorumu · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.2 b `FBAB10.SB2`
- **Yapı:** Düzgün elektriksel alan içindeki yüklü damla/parçacık için serbest cisim diyagramı çizilir; sabit hızla ya da askıda kalma koşulunda alanın yönü, yük işareti ve net kuvvet sorulur; elektriksel kuvvet ağırlıktan büyük/küçükse hareket yorumlanır.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Sabit hızla düşen damlada elektriksel kuvvet ağırlıktan küçüktür” (Sabit hız = net kuvvet sıfır ilkesini uygulayamama); “Damla yukarı hareket ediyorsa net kuvvet yukarıdır” (Hız yönü ile net kuvvet yönünü karıştırma); “Askıda kalan damlada yer çekimi sıfırlanmıştır” (Dengeyi kuvvetin yokluğu sanma)
- **Öğrenci hataları:** Serbest cisim diyagramında elektriksel kuvveti alan yönünde çizmek (negatif yük için) `SIGN_ERROR`; Sabit hızı ivmeli hareket sanıp net kuvveti sıfırdan farklı yazmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.277 ÖD-5; kitap s.177 9. Alıştırma
- **Kapsam notu:** Program–kitap: kitap damlanın dengesi için yük–kütle–alan sembolik bağıntılarını kullanır; program E hesabını kapsam dışı tutar, aile yalnız denge koşulu (kuvvet karşılaştırması) ve yön/işaret çıkarımıyla sınırlıdır.

## FİZ.11.2.3

### 070 · Faraday kafesi hakkında bilgiye ulaşmak için kaynak belirleme ve bilgiyi bulma

- **Ölçülen:** FİZ.11.2.3 a `KB2.6.SB1`, FİZ.11.2.3 b `KB2.6.SB2`
- **Yapı:** Bir araştırma sorusu (ör. asansörde cep telefonunun çekmemesi) ve aday kaynaklar (bilimsel makale, ders kitabı, forum yazısı, reklam sitesi, öğretmen) verilir; hangi kaynağın uygun ve güvenilir olduğu ya da verilen bir metin parçasından soruyu yanıtlayan bilginin hangisi olduğu sorulur.
- **Uyarıcı:** TEXT, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “En çok beğeni alan sosyal medya paylaşımı” (Popülerliği güvenilirlik sanma); “Yazarı ve tarihi belirtilmemiş ama özlü anlatılan site” (Anlaşılırlık ile doğruluğu karıştırma); “Reklam amaçlı ürün sayfası” (Kaynağın amacını (tarafsızlık) sorgulamama)
- **Öğrenci hataları:** Kaynağın niteliğine bakmadan ilk arama sonucunu seçmek `METHOD_SELECTION_ERROR`; Soruyla ilgisiz ama doğru bilgi içeren metni seçmek `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** kitap s.178 3. Etkinlik yönergesi; kitap s.179 3. Etkinlik 3.–4. adım; program “Öğrenciler konu hakkındaki bilgilere ulaşabilmek i…”
- **Kapsam notu:** Nitel çıktı (KB2.6): GRAPH uyarıcısı yapay kalacağından eklenmemiştir.

### 071 · Faraday kafesi bilgilerinin doğrulanması: çelişkili iddia ve uygulama yorumu

- **Ölçülen:** FİZ.11.2.3 c `KB2.6.SB3`
- **Yapı:** İki ya da daha çok kaynaktan alınmış, birbiriyle çelişen ya da kısmen yanlış Faraday kafesi iddiaları verilir; fizik ilkesi (iletken kapalı yapının iç bölgesini dış elektriksel alandan koruması) kullanılarak doğru/yanlış belirlenir; kafes içine konulan cisim ya da cihazın (küre, cep telefonu, kişi) durumu yorumlanır.
- **Uyarıcı:** TEXT, EXPERIMENT, DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “Faraday kafesinin içindeki cismin üzerinde net yük birikir” (Kafesin iç kısmında alanın sıfır olduğunu bilmeme); “Kafes yalıtkan malzemeden de yapılabilir” (Kafesin iletken olması gerektiğini bilmeme); “Kafesteki boşluklar büyüdükçe koruma artar” (Boşluk büyüklüğünün koruma düzeyini düşürdüğünü bilmeme); “Faraday kafesi yalnız statik yükler için etkilidir, yıldırım gibi ani yük boşalmalarında iç bölgeyi korumaz” (Kafesin yıldırım ve elektromanyetik dalgalara karşı da koruduğunu bilmeme)
- **Öğrenci hataları:** Kafesin içinde alan sıfır olduğunu, dışarıdaki yüklü cismin kafese de kuvvet uygulamadığı biçiminde genellemek `CONCEPTUAL_ERROR`; İki kaynaktaki çelişkide daha uzun metni doğru saymak `METHOD_SELECTION_ERROR`
- **Kanıt:** kitap s.182 Örnek; kitap s.183 11.–12. Alıştırma; kitap s.184 13. Alıştırma; program “Öğrenciler tartışma ortamında topladıkları bilgile…”
- **Kapsam notu:** Doğrulama bileşeni (KB2.6.SB3) kitapta fizik gerekçeli uygulama soruları ve tartışma etkinliğiyle işlenir.

### 072 · Faraday kafesi bilgilerinin kaydedilmesi: tablo, kaynak atfı ve özet

- **Ölçülen:** FİZ.11.2.3 ç `KB2.6.SB4`
- **Yapı:** Öğrencinin tuttuğu not/tablo (bilgi, kaynak adı, tarih, doğrulama durumu) ya da hazırlanacak sunu için bilgi kayıtları verilir; hangi kaydın eksiksiz, kaynağı belirtilmiş ve doğrulanmış bilgiyi içerdiği ya da kayıtta eksik ögenin ne olduğu sorulur.
- **Uyarıcı:** TEXT, TABLE · **Zorluk:** kolay
- **Çeldiriciler:** “Kaynak adı yazılmadan kaydedilen bilgi de aynı değerdedir” (Kaynak atfının önemini bilmeme); “Doğrulanmamış ama ilgi çekici bilgi de sunuya alınır” (Doğrulama ve kayıt basamaklarını ayırt edememe); “Bilgi kendi cümleyle yazıldığında kaynak yazmak gerekmez” (Atıf ilkesini bilmeme)
- **Öğrenci hataları:** Doğrulama basamağını atlayıp doğrudan kaydetmek `METHOD_SELECTION_ERROR`; Tabloda sütun anlamlarını karıştırmak `TABLE_READING_ERROR`
- **Kanıt:** kitap s.179 3. Etkinlik 4.–7. adım; program “Faraday kafesi ve Faraday kafesinin kullanım alanl…”

## FİZ.11.2.4

### 073 · Mıknatıs kutuplarının etkileşimi: kuvvet yönü, uzaklık ve kutup şiddeti etkisi

- **Ölçülen:** FİZ.11.2.4 a `FBAB1.SB1`
- **Yapı:** İki mıknatıs yaklaştırıldığında aynı/zıt kutupların etkileşimi (itme/çekme), tek kutuplu mıknatıs olmaması, mesafe ve kutup şiddetiyle kuvvetin değişimi terazi okuması, hareket yönü ya da serbest cisim diyagramı üzerinden sorulur.
- **Uyarıcı:** EXPERIMENT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Aynı kutuplar birbirini çeker” (Kutup etkileşim kuralını ters bilme); “Mıknatısları ikiye kesersek N ve S ayrı iki tek kutuplu parça elde edilir” (Tek kutuplu mıknatıs olmadığını bilmeme); “Uzaklık arttıkça manyetik kuvvet artar” (Mesafe–kuvvet ilişkisini ters kurma); “Mıknatıslar arasına demir konulursa etkileşim aynı kalır” (Ortam/madde etkisini göz ardı etme)
- **Öğrenci hataları:** Terazi okumasını artıran/azaltan kuvvet yönünü ters kurmak `SIGN_ERROR`; Mıknatısa etki eden kuvveti yalnız çeken mıknatısa bağlamak, etki–tepkiyi göz ardı etmek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.192 Örnek; kitap s.279 ÖD-8; program “Öğrenciler pusulanın çalışma prensibinden yola çık…”

### 074 · Mıknatıs etkileşiminde veri toplayıp kaydetme: ölçüm tablosu ve grafikten alan–çizgi sıklığı ilişkisi

- **Ölçülen:** FİZ.11.2.4 b `FBAB1.SB2`
- **Yapı:** Mıknatısın çevresinde demir tozu / pusula / terazi / kuvvetölçer kullanılan bir deneyin ölçüm tablosu ya da grafiği verilir; verilerin doğru kaydı (birim, sütun), mesafe ya da kutup şiddeti ile ölçülen niceliğin ilişkisi, hatalı ölçüm ya da eksik değer sorulur.
- **Uyarıcı:** TABLE, GRAPH, EXPERIMENT, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Çizgilerin seyrek olduğu yerde alan daha büyüktür” (Çizgi sıklığı–alan ilişkisini ters kurma); “Mesafe arttıkça pusula sapması da artar” (Uzaklık–etki ilişkisini ters kurma); “Tek bir ölçüm yeterlidir; tekrarlanan ölçüm gereksizdir” (Veri toplama ilkesini (tekrar, kontrol) bilmeme)
- **Öğrenci hataları:** Tablo sütunlarını (mesafe/etki) karıştırmak `TABLE_READING_ERROR`; Eğri grafiği doğru orantı olarak yorumlamak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.188 5.–7. adım; kitap s.193 14. Alıştırma; program “Öğrenciler, tasarladıkları deney düzeneği üzerinde…”

### 075 · Manyetik alan çizgisi şeklinden kutup cinsi, alan büyüklüğü ve etkileşim yorumu

- **Ölçülen:** FİZ.11.2.4 c `FBAB1.SB3`
- **Yapı:** Çubuk mıknatıs(lar)ın çevresindeki demir tozu ya da alan çizgisi görüntüsü verilir; kutupların cinsi, alanın en büyük/en küçük olduğu bölge, çizgilerin yönü ve mıknatısların itme/çekme durumu çizgi desenine göre yorumlanır.
- **Uyarıcı:** DIAGRAM, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Alan çizgileri S kutbundan çıkıp N kutbuna girer” (Çizgi yönü kuralını ters bilme); “Aynı kutuplar arasında çizgiler birbirine en yakındır, alan en büyüktür” (Aynı/zıt kutup deseni ayrımını yapamama); “Demir tozları alan çizgisini kendileri oluşturur” (Çizginin gözlemlenebilir model olduğunu bilmeme)
- **Öğrenci hataları:** Çizgilerin sık/seyrek olduğu bölgeyi alan büyüklüğüne bağlayamamak `CONCEPTUAL_ERROR`; Çizgi yönünü mıknatıs içinde de N→S almak `SIGN_ERROR`
- **Kanıt:** kitap s.193 14. Alıştırma; kitap s.191 Alan çizgisi özellikleri; program “Öğrenciler mıknatısların birbirleriyle etkileşimiy…”

### 076 · Mıknatıs(lar) ve Dünya'nın manyetik alanı: bileşke yön, pusula yönelimi ve yön bulma

- **Ölçülen:** FİZ.11.2.4 a `FBAB1.SB1`, FİZ.11.2.4 c `FBAB1.SB3`
- **Yapı:** Bir noktada iki mıknatısın (ve gerekirse Dünya'nın) alanı birleştirilir; bileşke yön çizilir, pusula iğnesinin N ucunun yönelimi ve yakındaki cismin hareket yönü sorulur; Dünya'nın alanı ihmal edilen ve edilmeyen durumlar karşılaştırılır; harita üzerinde pusulayla yön bulunur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, EXPERIMENT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Pusulanın N ucu mıknatısın S kutbundan uzağı gösterir” (Pusula–alan yönü ilişkisini ters kurma); “Dünya'nın alanı zayıf olduğu için her zaman ihmal edilebilir” (Alan büyüklüklerini karşılaştırmadan ihmal etme); “Bileşke alan, iki alanın büyüklüklerinin toplamı yönündedir” (Alanın vektörel olduğunu unutma); “Pusulanın N ucu coğrafi Güney Kutbu'nu gösterir” (Dünya'nın manyetik kutup düzenini yanlış bilme)
- **Öğrenci hataları:** Alan vektörlerini bileşenlerine ayırmadan toplamak `VECTOR_ERROR`; Pusula N ucunu alanın tersine yönlendirmek `SIGN_ERROR`
- **Kanıt:** kitap s.194 15. Alıştırma; kitap s.197 17. Alıştırma; kitap s.196 Örnek; program “Öğrenciler pusulanın çalışma prensibinden yola çık…”

## FİZ.11.2.5

### 077 · Akım taşıyan düz telin alanında i ve d ile ilişkinin deney/veri ile bulunması (Ørsted düzeneği) · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.5 a `FBAB10.SB1`
- **Yapı:** Ørsted düzeneğinde reosta/pil değişimi ve pusulanın telden uzaklığı (takoz yüksekliği) ile pusula sapmasını gösteren deney ya da simülasyon verisi (tablo, grafik) verilir; telin alanının akımla doğru, uzaklıkla ters orantılı olduğu veriden çıkarılır ya da deney değişikliklerinin etkisi sıralanır.
- **Uyarıcı:** TABLE, GRAPH, EXPERIMENT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Alan, tele uzaklaştıkça artar” (Alan–uzaklık ilişkisini ters kurma); “Akım yönü değişince pusula sapma miktarı azalır” (Yön değişimi ile büyüklük değişimini karıştırma); “Reosta direncini artırmak pusula sapmasını artırır” (Direnç–akım–alan zincirini yanlış kurma); “Alan, telin kalınlığıyla doğru orantılıdır” (İdeal (sonsuz ince) tel modelinde kalınlığın rolünü yanlış yorumlama)
- **Öğrenci hataları:** Direnç–akım ilişkisini (i = V/R) gözden kaçırıp zinciri ters kurmak `FORMULA_SELECTION_ERROR`; Birden çok değişkenin değiştiği satırlardan tek değişken etkisi çıkarmak `TABLE_READING_ERROR`
- **Kanıt:** kitap s.204 Örnek cevabı; kitap s.199 7.–9. adım; kitap s.278 ÖD-7; program “Manyetik alanın, iletkene olan uzaklığı ve elektri…”
- **Kapsam notu:** Program–kitap: kitap B = 2K·i/d modelini yazar; program model oran/yön düzeyinde genelleme ister (CALC_EXCLUDED). Sapma miktarı ve oran sorularıyla sınırlı tutuldu.

### 078 · Sağ el kuralı ile düz telin manyetik alanının yönü: sayfa içi/dışı, pusula ve ters akım · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.5 b `FBAB10.SB2`
- **Yapı:** Düz telden geçen akımın yönü verilir; telin çevresinde (üstten görünüşte çember) belirli noktalarda alanın yönü sayfa içi/dışı ya da yatay-düşey olarak, pusula N ucunun yönelimi olarak sorulur; akım yönü ters çevrilince ya da pusula telin üstüne/altına konunca yön değişimi yorumlanır.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Alan çizgileri tele paralel (telin boyunca) uzanır” (Alan çizgilerinin tele dik düzlemde çember olduğunu bilmeme); “Sağ el kuralında baş parmak alan yönünü gösterir” (Tel için baş parmak = akım, dört parmak = alan kuralını karıştırma); “Telin iki yanında alanın yönü aynıdır” (Telin zıt yanlarında yönün zıt olduğunu bilmeme)
- **Öğrenci hataları:** Baş parmağı alan yönünde tutarak kuralı uygulamak `VECTOR_ERROR`; Akım ters çevrilince büyüklüğü de değişir sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.203 Şekil 2.22; kitap s.205 19. Alıştırma a; program “Öğretmen manyetik alan katsayısı ve sağ el kuralı …”
- **Kapsam notu:** Sağ el kuralı programda açıkça kapsamdadır (SCOPE_INCLUDED); yön soruları hesap gerektirmez.

### 079 · Düz telin alanında i, d ve ortam değişince oran: B ∝ K·i/d · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.5 b `FBAB10.SB2`
- **Yapı:** Referans alan B verilir; akım, telden uzaklık ya da ortam (manyetik alan katsayısı) değiştirilir; yeni alan 'kaç B' olarak, ya da hangi değişimin alanı artıracağı sorulur. Veri tablosundan formülsüz orantı çıkarımı da bu ailedendir.
- **Uyarıcı:** TEXT, TABLE, DIAGRAM · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Akım iki katına çıkınca alan dört katına çıkar” (Doğrusal ilişkiyi karesel sanma); “d iki katına çıkınca alan dörtte bire iner” (Düz tel için d ile ters orantı yerine ters kare uygulama (noktasal yük karışıklığı)); “Ortamın etkisi yoktur” (Manyetik alan katsayısının ortama bağlı olduğunu bilmeme)
- **Öğrenci hataları:** Elektriksel alan (1/d²) ile düz tel alanı (1/d) bağıntısını karıştırmak `FORMULA_SELECTION_ERROR`; Çarpanları toplamak `ARITHMETIC_ERROR`
- **Kanıt:** kitap s.202 Düz telin alanı; kitap s.200 9.–10. adım; program “Öğrenciler matematiksel hesaplamalara girmeden ula…”; kılavuz s.115
- **Kapsam notu:** Program–kitap: kitap B = 2K·i/d ifadesini açıkça verir; program 'matematiksel hesaplamalara girmeden' genelleme ister. Aile oran/orantı düzeyindedir.

### 080 · Birden çok düz telin bir noktada oluşturduğu bileşke alan: yön, büyüklük karşılaştırması ve sıfır alan noktası · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.5 b `FBAB10.SB2`
- **Yapı:** Paralel iki (ya da üç) uzun telden aynı ya da zıt yönlü akımlar geçer; telleri birleştiren hat üzerindeki noktalarda her telin alanı sağ el kuralıyla bulunur; bileşke alanın yönü ve B cinsinden büyüklüğü, alanın sıfır olduğu nokta ve noktalar arası sıralama sorulur; Dünya alanı eklenebilir.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Aynı yönlü akımlı tellerin ortasında alan en büyüktür” (Aynı yönlü akımlarda alanların zıt yönlü olduğunu bilmeme); “Bileşke alan, iki alanın büyüklüklerinin her zaman toplamıdır” (Vektörel toplamı yönlere bakmadan yapma); “Telden uzaklaştıkça alanın değişmediği için K ve M noktalarında bileşke eşit olmak zorundadır” (Akımlar farklıyken simetriyi yanlış uygulama)
- **Öğrenci hataları:** Tellerin alan yönünü ters belirlemek (sayfa içi/dışı karışması) `SIGN_ERROR`; d ve 2d uzaklıklarında alanı 1/d² ile ilişkilendirmek `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.205 19. Alıştırma; kitap s.290 ÖD-20; kitap s.295 ÖD-25; program “Öğrenciler matematiksel hesaplamalara girmeden ula…”
- **Kapsam notu:** Program yalnız oran/yön düzeyi ister; kitaptaki i, 2i, d, 2d tabanlı karşılaştırma soruları bu düzeydedir. Dünya alanıyla toplam B cinsinden verilir, sayısal SI hesap yoktur.

## FİZ.11.2.6

### 081 · Akım makarası merkez ekseninde alanın i, N ve L ile ilişkisinin veriden modellenmesi

- **Ölçülen:** FİZ.11.2.6 a `FBAB10.SB1`
- **Yapı:** Akım makarasıyla yapılan deney ya da simülasyon verisi (i, N, L, B) tablo/grafik olarak verilir; B'nin akımla ve sarım sayısıyla doğru, makara boyuyla ters orantılı olduğu ve B ∝ i·N/L biçiminde birleştiği çıkarılır; eksik değer ve doğrusal grafik sorulur.
- **Uyarıcı:** TABLE, GRAPH, EXPERIMENT, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “B, makara uzunluğuyla doğru orantılıdır” (Uzunluk–alan ilişkisini ters kurma); “N iki katına çıkarılınca B dört katına çıkar” (Doğrusal ilişkiyi karesel sanma); “B yalnız akıma bağlıdır; sarım sayısı etkili değildir” (Sarım sayısı etkisini bilmeme)
- **Öğrenci hataları:** N ve L'yi birlikte değiştiren satırlarda etkiyi ayırmamak `TABLE_READING_ERROR`; B–L grafiğini doğrusal sanmak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.208 6.–7. adım; kitap s.210 Alan modeli; program “Öğrenciler veri analizine dayalı olarak manyetik a…”

### 082 · Akım makarası alanının oranı: i, N, L ve çekirdek değişimi; ideal makarada etkisiz değişkenler

- **Ölçülen:** FİZ.11.2.6 b `FBAB10.SB2`
- **Yapı:** Referans B verilir; akım, sarım sayısı, makara boyu (ya da birim uzunluktaki sarım sayısı), çekirdek maddesi değişir; yeni B 'kaç B' olarak ya da tablodaki sapma/raptiye miktarı olarak sorulur; yarıçap gibi etkisiz değişkenler ayıklanır.
- **Uyarıcı:** TEXT, TABLE, EXPERIMENT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Yarıçap artınca merkez eksenindeki alan azalır” (İdeal makarada yarıçapın etkisiz olduğunu bilmeme); “L artınca N sabitken B artar” (Uzunluk–alan ilişkisini ters kurma); “Akım yönü değişince alan büyüklüğü azalır” (Yön ile büyüklüğü karıştırma); “Çekirdeğe demir konunca alan değişmez” (Demirin alanı güçlendirdiğini bilmeme)
- **Öğrenci hataları:** N ve L'yi ayrı değişken sayıp N/L oranını kullanmamak `METHOD_SELECTION_ERROR`; Çarpan hesabında L'nin ters orantısını atlamak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.209 11. adım; kitap s.211 Örnek; kitap s.281 ÖD-10; program “Matematiksel modele dayanarak akım makarasının mer…”

### 083 · Akım makarasında alan yönü, kutuplar ve pusula: tek makara ve iki makaranın bileşkesi

- **Ölçülen:** FİZ.11.2.6 b `FBAB10.SB2`
- **Yapı:** Akım makarasında akım yönü verilir; makaranın N ve S uçları, merkez eksenindeki alan yönü, alan çizgilerinin çizimi ve pusula yönelimi sorulur; birbirine dik iki makaranın kesişim noktasında bileşke alanın yönü ve (reosta/pil değişince) yönelimdeki değişim yorumlanır.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, EXPERIMENT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Makaranın içindeki alan, akım yönünden bağımsız olarak hep aynı yöndedir” (Akım yönü–alan yönü ilişkisini bilmeme); “Alan çizgileri makaranın içinde N'den S'ye doğrudur” (İç/dış çizgi yönünü karıştırma); “İki makaranın bileşke alanı büyüklüklerinin toplamı yönündedir” (Dik iki alanı vektörel toplamayı bilmeme); “Pusula iğnesi akım makarasının ekseninden dik bir yöne hizalanır” (Pusulanın alana paralel hizalandığını bilmeme)
- **Öğrenci hataları:** Sağ elin parmaklarını akım yönüne değil teli saran yöne dik tutmak `VECTOR_ERROR`; Bileşke alanı iki alanın büyüklüklerinin toplamı olarak almak `VECTOR_ERROR`
- **Kanıt:** kitap s.209 Değerlendirme 1; kitap s.296 ÖD-26; kitap s.297 ÖD-26 c, ç; program “düz bir iletken yerine akım makarası kullanılması …”

## FİZ.11.2.7

### 084 · Elektromıknatısların kullanım alanları için kaynak belirleme ve bilgiyi bulma

- **Ölçülen:** FİZ.11.2.7 a `KB2.6.SB1`, FİZ.11.2.7 b `KB2.6.SB2`
- **Yapı:** Elektromıknatıs uygulamaları (hurda vinci, manyetik tren, kapı zili, hoparlör, MR, selenoid vana) hakkında bilgi aranırken aday kaynaklar (kitap, hakemli dergi, üretici kataloğu, forum) ve kaynaklardan alıntılar verilir; hangi kaynağın uygun olduğu ya da hangi bilginin soruya yanıt verdiği sorulur.
- **Uyarıcı:** TEXT, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Üreticinin reklam broşürü en güvenilir kaynaktır” (Kaynağın tarafsızlığını sorgulamama); “Adı en çok geçen site doğru bilgi verir” (Görünürlük ile doğruluğu karıştırma); “Metin uzunsa daha güvenilirdir” (Uzunluk ile güvenilirliği karıştırma)
- **Öğrenci hataları:** Kaynak ölçütlerini uygulamadan ilk bulunan bilgiyi almak `METHOD_SELECTION_ERROR`; Aranan uygulamayla ilgisiz paragraftan bilgi çıkarmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** kitap s.213 4. Etkinlik 1.–2. adım; kitap s.216 Çalışma Yaprağı 1; program “Gruplar elektromıknatıslar hakkındaki bilgilere ul…”
- **Kapsam notu:** Nitel çıktı (KB2.6): GRAPH uyarıcısı yapay kalacağından eklenmemiştir.

### 085 · Elektromıknatıs bilgilerinin doğrulanması ve uygulama ilkesi yorumu

- **Ölçülen:** FİZ.11.2.7 c `KB2.6.SB3`
- **Yapı:** Elektromıknatıs uygulaması hakkında kaynaklardan gelen iddialar (ör. 'elektromıknatıs akım kesilince de mıknatıs kalır', 'vinç akımı artırınca daha çok hurda çeker') verilir; fizik ilkesiyle doğru/yanlış belirlenir; vinç, elektromanyetik kilit, kapı zili ve manyetik asansörde ilke ve yöntem yorumlanır.
- **Uyarıcı:** TEXT, DAILY_LIFE_CONTEXT, EXPERIMENT, DIAGRAM · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Elektromıknatıs akım kesilince de mıknatıslığını korur” (Elektromıknatısın geçici mıknatıs olduğunu bilmeme); “Vinç, akım ters çevrilince hurdayı bırakır” (Akım yönü ile akım büyüklüğünü karıştırma); “Çekirdek olarak bakır kullanılırsa alan çok artar” (Ferromanyetik çekirdek (demir/nikel/kobalt) ayrımını bilmeme); “Elektromıknatıs, doğal mıknatısa göre her açıdan üstündür” (Gerekçesiz genelleme (enerji gereksinimi ve ısınma gibi dezavantajları gözden kaçırma))
- **Öğrenci hataları:** İddiayı kaynağına değil sezgiye göre değerlendirmek `METHOD_SELECTION_ERROR`; Alanı artıran etmenleri (i, N/L, çekirdek, d) karıştırmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.215 Örnek; kitap s.216 22. Alıştırma; kitap s.282 ÖD-11; program “Öğrenciler toplanan bilgilerin doğru olup olmadıkl…”
- **Kapsam notu:** Doğrulama bileşeni (KB2.6.SB3) kitapta uygulama temelli fizik gerekçeli sorularla ve kaynak sorgulama sorularıyla (güncel mi, hakemli mi) işlenir.

### 086 · Elektromıknatısların günlük hayattaki kullanımları: bilgilerin kaydı ve çalışma ilkesi eşleştirme tablosu

- **Ölçülen:** FİZ.11.2.7 ç `KB2.6.SB4`
- **Yapı:** Kullanım alanı – çalışma ilkesi – kaynak sütunlu bir kayıt tablosu ya da yapılandırılmış grid verilir; doğru eşleştirme, eksik ya da yanlış kayıt, hangi kayıtların sunuya alınacağı sorulur.
- **Uyarıcı:** TABLE, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Su arıtma cihazı ve mikrofon elektromıknatıs kullanmaz” (Günlük kullanım alanlarını bilmeme); “Nikel ve kobalt akım makarasının içine konunca alanı azaltır” (Ferromanyetik çekirdeğin alanı artırdığını bilmeme); “Halkaların yarıçapı ideal makara merkezindeki alanı belirler” (Etkisiz değişkenleri ayıklayamama)
- **Öğrenci hataları:** Tablo satırı ile sütunu karıştırmak `TABLE_READING_ERROR`; İdeal makara modelinde etkili olmayan değişkeni işaretlemek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.217 Çalışma Yaprağı 3; kitap s.214 5.–6. adım; program “Elektromıknatısların günlük hayattaki kullanım ala…”

## FİZ.11.2.8

### 087 · Manyetik alandaki akımlı tele etki eden kuvvetin B, i, L ve açıyla ilişkisinin veriden modellenmesi

- **Ölçülen:** FİZ.11.2.8 a `FBAB10.SB1`
- **Yapı:** U mıknatıs/kuvvetölçer düzeneği ya da simülasyondan elde edilen veri tablosu verilir; F'nin B, i, L ile doğru orantılı, tel ile alan arasındaki açının sinüsüyle doğru orantılı olduğu ve alanla tel paralelken kuvvetin sıfır olduğu çıkarılır; eksik değer ve grafik yorumu sorulur.
- **Uyarıcı:** TABLE, GRAPH, EXPERIMENT, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “F, tel ile B arasındaki açı küçüldükçe artar” (Açı bağımlılığını (sinθ) ters kurma); “Tel B'ye paralel iken F en büyüktür” (Paralel durumda kuvvetin sıfır olduğunu bilmeme); “F, B ve i'nin toplamıyla doğru orantılıdır” (Çarpım–toplam karışıklığı)
- **Öğrenci hataları:** sinθ yerine cosθ kullanmak `FORMULA_SELECTION_ERROR`; Açı değişen satırlarda doğrusal ilişki aramak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.220 7.–9. adım; kitap s.219 1. adım c; program “Gruplar manyetik alanda akım geçen tele etki eden …”

### 088 · Akımlı tele etki eden manyetik kuvvetin yönü: sağ el kuralı, tel hareketi ve AC kaynak

- **Ölçülen:** FİZ.11.2.8 b `FBAB10.SB2`
- **Yapı:** Akım ve alan yönü verilir (ya da U mıknatısın kutupları), tele etki eden kuvvetin yönü sağ el kuralıyla bulunur; akım/kutup değişince tel mıknatısın içine mi dışına mı bükülür; mıknatıs kutupları ve kuvvet yönü verilip akım yönü ya da kutup cinsi sorulur; akım AC olunca kuvvetin yönünün zamanla değiştiği yorumlanır.
- **Uyarıcı:** DIAGRAM, GRAPH, EXPERIMENT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Kuvvet, alan yönündedir” (Kuvvetin alan ve akıma dik olduğunu bilmeme); “Akım yönü ters çevrilirse kuvvetin büyüklüğü de ters işaretli azalır” (Yön değişimi ile büyüklüğü karıştırma); “AC kaynakta tel sürekli aynı yöne itilir” (Kuvvetin akımla birlikte yön değiştirdiğini bilmeme); “Hem akım hem alan ters çevrilirse kuvvet ters çevrilir” (İki işaret değişiminin birbirini götürdüğünü bilmeme)
- **Öğrenci hataları:** Sağ el kuralında alan ile akımın rollerini değiştirmek `VECTOR_ERROR`; Pozitif–negatif yön seçimini tutarlı uygulamamak `SIGN_ERROR`
- **Kanıt:** kitap s.225 Şekil 2.26; kitap s.226 26. Alıştırma; kitap s.289 ÖD-19; program “Öğretmen manyetik kuvvetin vektörel olduğundan bah…”

### 089 · Akımlı tele etki eden kuvvetin büyüklüğü: değişken değişimi ve açı

- **Ölçülen:** FİZ.11.2.8 b `FBAB10.SB2`
- **Yapı:** Referans durumda F = B·i·L verilir; B, i, L ve tel–alan açısı birer birer ya da birlikte değiştirilir; yeni kuvvet B·i·L cinsinden ya da 'kaç F' olarak sorulur; farklı açılarda yerleştirilmiş teller için kuvvet büyüklükleri sıralanır.
- **Uyarıcı:** TABLE, DIAGRAM, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Tel alana paralel iken kuvvet en büyüktür” (Paralel durumda sıfır olduğunu bilmeme); “30°'de kuvvet cos30° ile orantılıdır” (sin–cos seçimini karıştırma); “L iki katına çıkarılırsa kuvvet yarıya iner” (Doğru orantıyı ters orantı sanma)
- **Öğrenci hataları:** Açıyı B ile tel arasında değil, telin normaliyle almak `FORMULA_APPLICATION_ERROR`; sin30° değerini 0,87 almak `ARITHMETIC_ERROR`
- **Kanıt:** kitap s.227 27. Alıştırma; kitap s.225 Model; program “Öğrenciler her bir değişkeni ayrı ayrı değiştirere…”

### 090 · Akımlı telde kuvvet dengesi ve ivme: kuvvetölçer okuması ve raylı çubuk

- **Ölçülen:** FİZ.11.2.8 b `FBAB10.SB2`
- **Yapı:** Düzgün alan içindeki akımlı çubuk için serbest cisim diyagramı çizilir; kuvvetölçer okuması (mg ± BiL) ya da okumanın sıfır olması için gereken akım sorulur; ray üzerindeki çubuk için ivme, rayı terk süresi ve sürat istenir.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Alan hangi yönde olursa olsun okuma mg'den büyük olur” (Kuvvetin yönünü hesaba katmama); “Okuma sıfırsa tel üzerinden akım geçmiyordur” (Dengeyi kuvvetlerin yokluğu sanma); “Çubuk raylar üzerinde sabit hızla gider” (Sabit kuvvetin sabit ivme verdiğini bilmeme); “Çubuğun ivmesi çubuk kütlesinden bağımsızdır” (F = ma bağlantısını kuramama)
- **Öğrenci hataları:** mg ile BiL'yi yönlerine bakmadan toplamak `SIGN_ERROR`; a = BiL/m yerine a = BiL yazmak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.284 ÖD-13; kitap s.228 29. Alıştırma; program “Öğrenciler her bir değişkeni ayrı ayrı değiştirere…”

### 091 · Paralel akımlı teller arasındaki kuvvet: yön, karşılıklılık ve büyüklük · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.8 b `FBAB10.SB2`
- **Yapı:** Birbirine paralel iki uzun telden aynı ya da zıt yönlü akım geçer; her telin diğerine uyguladığı kuvvetin yönü sağ el kuralıyla çizilir, büyüklüğü akımların çarpımı ve uzaklıkla ilişkilendirilir; 'aynı yönlü akımlar çeker, zıt yönlüler iter' ifadesinin doğruluğu gerekçelendirilir.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Aynı yönlü akımlı teller birbirini iter” (Aynı/zıt akım kuralını ters bilme); “Büyük akımlı tel, küçük akımlı tele daha büyük kuvvet uygular” (Etki–tepkiyi manyetik kuvvete uygulayamama); “Teller arasındaki kuvvet uzaklıkla ters kare orantılıdır” (Düz telin 1/d ilişkisini karıştırma)
- **Öğrenci hataları:** Bir telin alanının diğerinin yerinde yönünü ters bulmak `VECTOR_ERROR`; Kuvvet yönünü alan yönüyle aynı almak `SIGN_ERROR`
- **Kanıt:** kitap s.228 28. Alıştırma; program “Öğretmen manyetik alan içerisindeki akım geçen tel…”
- **Kapsam notu:** Kitapta 28. Alıştırma'da kuvvetin matematiksel modeli (yönü ve büyüklüğü) istenir; program F = BIL ile değişken bazlı problemleri açıkça kapsar.

## FİZ.11.2.9

### 092 · Akımlı dikdörtgen çerçevenin kenarlarına etki eden kuvvetlerin yönleri (önceki bilginin gözden geçirilmesi)

- **Ölçülen:** FİZ.11.2.9 a `KB2.15.SB1`
- **Yapı:** Düzgün alan içinde akımlı dikdörtgen tel çerçevenin dört kenarı için sağ el kuralıyla kuvvet yönleri çizilir; alanla paralel akım taşıyan kenarlarda kuvvetin sıfır olduğu, zıt kenarlarda kuvvetlerin zıt yönlü ve eşit büyüklükte olduğu belirlenir.
- **Uyarıcı:** DIAGRAM, TABLE · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Alana paralel kenara da kuvvet etki eder” (Paralel durumda kuvvetin sıfır olduğunu bilmeme); “Karşılıklı iki kenara aynı yönde kuvvet etki eder” (Zıt akım yönlerinden kuvvetlerin zıt olduğunu bilmeme); “Çerçeveye etki eden bileşke kuvvet büyüktür, bu yüzden öteleme hareketi yapar” (Bileşke kuvvetin sıfır olup tork oluştuğunu bilmeme)
- **Öğrenci hataları:** Kenarlardaki akım yönünü yanlış belirlemek `VECTOR_ERROR`; Sağ el kuralında alan ve akım yönünü karıştırmak `VECTOR_ERROR`
- **Kanıt:** kitap s.231 Değerlendirme 1; kitap s.232 Şekil 2.28; program “Manyetik alandaki akım geçen düz tele etki eden ku…”

### 093 · Çerçevenin dönme durumu ve döndürme etkisini belirleyen etmenler (galvanometre, uydu manyetik burucusu)

- **Ölçülen:** FİZ.11.2.9 b `KB2.15.SB2`
- **Yapı:** Kuvvet yönleri bilinen çerçevenin dönme yönü (saat yönü / tersi), dengede durma konumu, düzlem alana paralel/dik iken döndürme etkisi ve döndürme etkisini artırmak için i, B, çerçeve alanı ve sarım sayısının nasıl değiştirileceği sorulur.
- **Uyarıcı:** DIAGRAM, TABLE, DAILY_LIFE_CONTEXT, EXPERIMENT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Çerçeveye etki eden bileşke kuvvet sıfır olduğundan çerçeve dönmez” (Bileşke kuvvet sıfır olsa da torkun olabileceğini bilmeme); “Döndürme etkisi çerçeve düzlemi alana dik iken en büyüktür” (Düzlem alana paralelken en büyük, dik iken sıfır olduğunu bilmeme); “Sarım sayısı artarsa döndürme etkisi azalır” (Sarım sayısı–döndürme etkisi ilişkisini ters kurma); “Alanın yönü kuvvetin döndürme yönünü etkilemez” (Alan yönünün tork yönünü belirlediğini bilmeme)
- **Öğrenci hataları:** Kuvvet yönlerinden dönme yönünü (saat/ters) yanlış çıkarmak `VECTOR_ERROR`; Tork değişkenlerinden (alan, akım) birini unutmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.233 30. Alıştırma; kitap s.234 31. Alıştırma; kitap s.293 ÖD-23; program “Öğrenciler inceledikleri görsellere ve deneyimine …”

### 094 · Elektrik motorunun çalışma prensibi açısından çıkarımların değerlendirilmesi

- **Ölçülen:** FİZ.11.2.9 c `KB2.15.SB3`
- **Yapı:** Basit elektrik motoru modeli ve elektrikli/hibrit araç metni verilir; hangi çıkarımın motorun çalışma ilkesiyle tutarlı olduğu, enerji dönüşümünün yönü ve motorun parçalarının görevi sorulur; dönmenin sürmesi için akım yönünün yarım turda değişmesi gerektiği gibi gerekçeli yargılar değerlendirilir.
- **Uyarıcı:** TEXT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Elektrik motoru, mekanik enerjiyi elektrik enerjisine dönüştürür” (Motor ile jeneratörün enerji dönüşüm yönünü karıştırma); “Motorun dönmesi için alan içinde akımın sıfır olması gerekir” (Akım–kuvvet ilişkisini bilmeme); “Elektrikli araç her koşulda içten yanmalıdan daha uzun menzillidir” (Metinden çıkarılamayacak genelleme yapma); “Motorda dönme, çerçevenin bir kenarına etki eden tek kuvvetten kaynaklanır” (Kuvvet çiftini (zıt kenarlar) bilmeme)
- **Öğrenci hataları:** Metinde olmayan bir bilgiyi çıkarım sanmak `QUESTION_INTERPRETATION_ERROR`; Motor–jeneratör enerji dönüşümünü ters yazmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.231 Değerlendirme 2; kitap s.292 ÖD-22; kitap s.230 Fizik Gazetesi; program “Görsellerden faydalanarak veya yaptıkları tasarımı…”
- **Kapsam notu:** Programda motor yalnız çalışma ilkesi düzeyindedir; komütatör/fırça gibi ayrıntılar kitapta yer almaz, yalnız 'akım yönü değişmeli' gerekçesi ek bilgi olarak kullanılır.

## FİZ.11.2.10

### 095 · Manyetik akıya etki eden etmenlerin belirlenmesi: analoji ve simülasyon · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.10 a `KB2.4.SB1`
- **Yapı:** Püskürtme boya – kâğıt, şemsiye – yağmur ya da pencere – rüzgâr analojisi verilir; analojideki ögelerin manyetik alan, yüzey alanı, açı ve akı karşılıkları eşleştirilir; akıya etki eden etmenler (B, A, açı) belirlenir; analojinin sınırı (alan taneciklerden oluşmaz) yorumlanır.
- **Uyarıcı:** TEXT, DAILY_LIFE_CONTEXT, EXPERIMENT, DIAGRAM · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Manyetik alan tanecik akışıdır, bu yüzden analoji birebir geçerlidir” (Analojinin sınırlarını bilmeme (alan taneciklerden oluşmaz)); “Akı yalnız manyetik alanın büyüklüğüne bağlıdır” (Yüzey alanı ve açı etkisini bilmeme); “Yüzey, alana paralel konunca akı en büyüktür” (Yüzey normali ile alan arasındaki açı kavramını yanlış kurma)
- **Öğrenci hataları:** Analojideki ögeleri yanlış eşleştirmek (alan çizgisi – kâğıt) `CONCEPTUAL_ERROR`; Açıyı yüzey ile alan arasında değil normal ile alan arasında almamak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.237 10. Etkinlik 3. adım; kitap s.291 ÖD-21; program “Öğrenciler analojiden yola çıkarak manyetik akıya …”
- **Kapsam notu:** Program manyetik akıyı yalnız kavramsal tanıtır (CONCEPTUAL_ONLY); bu aile formül gerektirmez.

### 096 · Manyetik akı ile etmenler arasındaki ilişki: B, yüzey alanı ve açı değişince akının artıp azalması · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.10 a `KB2.4.SB1`, FİZ.11.2.10 b `KB2.4.SB2`
- **Yapı:** Düzgün manyetik alan içindeki bir yüzeye yapılan işlemler (alanı büyütme, yüzeyi alana yaklaştırma, normal ekseni etrafında ya da başka eksen etrafında döndürme, mıknatısları yaklaştırma) için akının artar/azalır/değişmez yargıları değerlendirilir; veri tablosunda B, A ve açı ile akı arasındaki ilişki (formülsüz) çıkarılır; bobinin içindeki ve dışındaki konumlarda akı karşılaştırılır.
- **Uyarıcı:** TEXT, DIAGRAM, TABLE, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Düzgün alanda yüzeyi mıknatısa yaklaştırmak akıyı artırır” (Düzgün alanda B'nin konumdan bağımsız olduğunu bilmeme); “Yüzeyi normali etrafında döndürmek akıyı azaltır” (Normal etrafındaki dönüşün açıyı değiştirmediğini bilmeme); “Yüzey alana paralel olduğunda akı en büyüktür” (Açı bağımlılığını (cosθ) ters kurma); “Akı, alan çizgilerinin yüzeye toplam uzunluğuyla ilgilidir” (Yüzeyden geçen çizgi sayısı kavramını yanlış yorumlama)
- **Öğrenci hataları:** Açıyı yüzeyle alan arasında almak (θ yerine 90° − θ) `CONCEPTUAL_ERROR`; Düzgün alanda konum değişimini alan değişimi sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.240 Örnek cevap; kitap s.239 Model; kitap s.241 34. Alıştırma; program “Öğrenciler manyetik akının manyetik alanın büyüklü…”; kılavuz s.115
- **Kapsam notu:** Program–kitap çelişkisi: kitap Φ = B·A·cosθ modelini verir ve 32.–33. Alıştırma ile ÖD-15'te akıyı sayısal olarak hesaplatır; program akıyı kavramsal ele alır. Aile nitel/oran düzeyinde kurulmuştur.

### 097 · Hareket eden halkada akı değişimi: öteleme, dönme ve salınım · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.10 b `KB2.4.SB2`
- **Yapı:** Düzgün manyetik alan içinde farklı biçimlerde hareket eden özdeş halkalar (basit sarkaç, yay sarkacı, ekseni etrafında dönen halka) verilir; bir periyotluk sürede hangi halkada akının değiştiği, değişim büyüklüklerinin karşılaştırılması ya da akı–zaman grafiğinin yorumu sorulur; alan dışına çıkma durumunda akı değişimi tartışılır.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, GRAPH · **Zorluk:** orta–zor
- **Çeldiriciler:** “Halka hareket ettiği için her durumda akı değişir” (Öteleme ile açı/alan değişimini ayıramama); “Alan düzgün olduğundan dönen halkada da akı sabittir” (Açı değişiminin akıyı değiştirdiğini bilmeme); “Halka düzgün alan içinde kaldığı sürece her hareket türünde akı sabittir” (Düzgün alanda akının yalnız B'ye bağlı olduğunu sanma (A ve θ etkisini unutma))
- **Öğrenci hataları:** Hareketi akı değişimi ile özdeşleştirmek `CONCEPTUAL_ERROR`; Φ–t grafiğini hareketin x–t grafiği sanmak `GRAPH_READING_ERROR`
- **Kanıt:** kitap s.241 35. Alıştırma; kitap s.240 Sinek; program “Öğrenciler manyetik akının manyetik alanın büyüklü…”
- **Kapsam notu:** Program–kitap: akı programda kavramsal; hareket eden halkada akı değişimi nitel (var/yok/karşılaştırma) olarak ele alınmıştır.

## FİZ.11.2.11

### 098 · İndüksiyon akımını oluşturan ve etkileyen etmenler: mıknatıs–bobin ve iki devre deneyleri

- **Ölçülen:** FİZ.11.2.11 a `FBAB10.SB1`
- **Yapı:** Mıknatıs–bobin–ampermetre düzeneğinde mıknatısın yaklaşması, durması, uzaklaşması, hızı ve gücü ile ampermetre ibresinin sapması; ya da iki devrenin (birincil devre anahtarı, direnç) bulunduğu Faraday düzeneğinde ibrenin davranışı verilir; hangi durumda ve ne yönde/ne kadar indüksiyon akımı oluştuğu, ilişkinin tablodan çıkarımı sorulur.
- **Uyarıcı:** EXPERIMENT, TABLE, DIAGRAM, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Mıknatıs bobinin yanında durduğu sürece akım sürer” (Akım için akı değişiminin gerektiğini bilmeme); “Anahtar kapalı kaldıkça ikinci devredeki ibre sapmış kalır” (Sürekli (kararlı) akımın indüksiyon oluşturmadığını bilmeme); “İkinci devre direnci artınca indüksiyon gerilimi azalır” (ε'nun devre direncinden bağımsız olduğunu bilmeme); “Mıknatıs yaklaşırken ve uzaklaşırken ibre aynı yöne sapar” (Akı artışı/azalışına göre yön değişimini bilmeme)
- **Öğrenci hataları:** Akım için mıknatısın varlığını yeterli saymak `CONCEPTUAL_ERROR`; Direnç etkisini gerilim etkisiyle karıştırmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.246 Şekil 2.31; kitap s.250 38. Alıştırma; program “Tasarladığı düzenek üzerinden indüksiyon akımı olu…”; program “Öğrenciler birim zamandaki manyetik akı değişimini…”

### 099 · Faraday Yasası ile indüksiyon gerilimi ve akımı: ΔΦ, Δt, N ve R ile çözüm · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.11 b `FBAB10.SB2`
- **Yapı:** B, yüzey alanı, sarım sayısı ve değişim süresi verilen halka/bobin için ilk ve son akı, akı değişimi, ortalama indüksiyon gerilimi ve (devre direnci verilirse) indüksiyon akımı sorulur; alan/alan-içi-dışı değişim durumları tabloda karşılaştırılır; N ve Δt çarpanlarının etkisi oranla da sorulur.
- **Uyarıcı:** TABLE, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “ε = ΔΦ·Δt” (Zamanla orantıyı çarpma biçiminde kurma); “Alan değişmese bile halka hareket ettirildiği sürece ε oluşur” (Akı değişimi koşulunu bilmeme); “N iki katına çıkınca ε yarıya iner” (Sarım sayısı etkisini ters kurma); “Akı değişimi yerine son akı değeri kullanılır” (Δ'yı (değişimi) ilk–son farkı olarak almama)
- **Öğrenci hataları:** ΔΦ yerine Φ_son kullanmak `FORMULA_APPLICATION_ERROR`; Alan birimi (T), alan (m²), süre (s) dönüşümlerini hatalı yapmak (cm → m) `UNIT_ERROR`; Akımı ε = i/R yazarak bulmak `FORMULA_SELECTION_ERROR`
- **Kanıt:** kitap s.248 Örnek; kitap s.246 2. soru tablosu; kitap s.249 37. Alıştırma; kitap s.252 41. Alıştırma; program “Oluşturduğu matematiksel modeli örnekler üzerinden…”

### 100 · Φ–t, B–t grafiklerinden indüksiyon geriliminin zamana bağlı grafiğine (eğim yorumu) · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.11 b `FBAB10.SB2`
- **Yapı:** Düzgün alan içindeki sabit yüzey için B–t (ya da Φ–t) grafiği parçalı doğrusal biçimde verilir; her zaman aralığındaki eğimden ε–t grafiği çizilir/seçilir; ε'nun sıfır, sabit, pozitif/negatif olduğu aralıklar belirlenir.
- **Uyarıcı:** GRAPH, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Φ en büyük olduğu anda ε da en büyüktür” (Akının değerini akının değişim hızıyla karıştırma); “Φ–t grafiği sabitse ε sabit ve sıfırdan farklıdır” (Sabit akıda ε = 0 olduğunu bilmeme); “Grafiğin altında kalan alan ε'dur” (Eğim ile alan yorumunu karıştırma)
- **Öğrenci hataları:** Grafiğin eğimi yerine değerini ε saymak `GRAPH_READING_ERROR`; Φ ile B ekseni birimlerini karıştırmak (Φ = B·A) `UNIT_ERROR`
- **Kanıt:** kitap s.251 40. Alıştırma; kitap s.252 41. Alıştırma; program “Oluşturduğu matematiksel modeli örnekler üzerinden…”

### 101 · Lenz Yasası ile indüksiyon akımının yönü

- **Ölçülen:** FİZ.11.2.11 b `FBAB10.SB2`
- **Yapı:** Halkadan/bobinden mıknatıs yaklaştırılır ya da uzaklaştırılır; halkanın içinden geçen alanın büyüklüğü artırılır/azaltılır (ya da bitişik devredeki akım artar/azalır); indüksiyon akımının yönü (saat yönü / tersi, ibre sapma yönü) Lenz Yasası ve sağ el kuralıyla bulunur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, EXPERIMENT · **Zorluk:** orta–zor
- **Çeldiriciler:** “İndüksiyon akımı, akı artışını destekleyecek yöndedir” (Lenz yasasının 'karşı koyma' ilkesini ters yorumlama); “Alan aşağı yönlü artıyorsa akım halkaya üstten bakıldığında saat yönündedir” (Sağ el kuralı ile yön tayini yanlışı); “Alan sabit olsa da akı büyükse akım yönü Lenz yasasına göre belirlenir” (Akı değişiminin yönü yerine akının büyüklüğüne bakma)
- **Öğrenci hataları:** İndüksiyon alanını dış alanla aynı yönde almak `SIGN_ERROR`; Akım yönünü sağ el yerine sol el ile bulmak `VECTOR_ERROR`
- **Kanıt:** kitap s.247 Lenz Yasası; kitap s.249 37. Alıştırma c; kitap s.286 ÖD-16; program “Oluşturduğu matematiksel modeli örnekler üzerinden…”
- **Kapsam notu:** Lenz Yasası programda Faraday Yasası'ndaki eksi işaretinin anlamı olarak yer alır (kitap s.247).

### 102 · Mıknatısın iletken halkadan düşmesi: sürükleme (frenleme) kuvveti, kesikli halka ve düşme süresi

- **Ölçülen:** FİZ.11.2.11 b `FBAB10.SB2`
- **Yapı:** Bir mıknatıs kapalı iletken bir bileziğin ve boşluklu (kesik) bir bileziğin üstünden bırakılır; halkalarda akım oluşup oluşmadığı, mıknatısa etki eden kuvvetler, ivme ve hangi mıknatısın bileziğe ya da yere daha erken ulaşacağı sorulur.
- **Uyarıcı:** DIAGRAM, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Kesik bilezikte de akım oluşur çünkü akı değişir” (Akım için kapalı devre koşulunu bilmeme); “Kapalı bilezikte oluşan akım mıknatısı hızlandırır” (Lenz yasası–enerji korunumu ilişkisini bilmeme); “Mıknatıs bileziğe ulaşana kadar bilezikte akım yoktur” (Mıknatıs yaklaşırken akının değiştiğini görememe); “İki mıknatıs aynı anda yere ulaşır” (Frenleme kuvvetinin ivmeyi azalttığını göz ardı etme)
- **Öğrenci hataları:** Akımın var olduğu durumda frenleme kuvvetinin yönünü aşağı çizmek `SIGN_ERROR`; Akım olmasını yalnız akı değişimine bağlayıp devrenin kapalı olmasını unutmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.287 ÖD-17; program “Öğrenciler birim zamandaki manyetik akı değişimini…”

### 103 · İndüksiyon ilkesinin uygulamalarında akı değişimini bulma: elektrogitar, loop dedektörü, kablosuz şarj, TMS

- **Ölçülen:** FİZ.11.2.11 b `FBAB10.SB2`
- **Yapı:** Günlük bir cihazın (elektrogitar manyetiği, trafik kavşağı loop dedektörü, kablosuz şarj, TMS, kontak lensli sakkad ölçümü, dinamo) çalışma ilkesi anlatılır; akı değişiminin nerede, neden oluştuğu, ε'yu artırmanın yolları (sarım ↑, yaklaştırma, hız ↑) ve yargıların doğruluğu sorulur.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, TEXT, DIAGRAM · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Gitar teli sabitken de bobinde ε oluşur” (Akı değişimi koşulunu bilmeme); “Şarj ünitesi ile telefon arasındaki mesafe artınca ε artar” (Mesafe–akı ilişkisini ters kurma); “İndüksiyon yalnız metal olmayan cisimlerde gözlenir” (İndüksiyonun iletken kapalı devre koşulunu bilmeme); “Sarım sayısı artarsa ε azalır” (Sarım sayısı etkisini ters kurma)
- **Öğrenci hataları:** Akı değişimi yerine akının varlığını ε kaynağı saymak `CONCEPTUAL_ERROR`; Cihazın çalışma ilkesini manyetik kuvvet ile karıştırmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.248 36. Alıştırma; kitap s.249 37. Alıştırma; kitap s.252 41. Alıştırma; program “Oluşturduğu matematiksel modeli örnekler üzerinden…”

## FİZ.11.2.12

### 104 · Alternatif akımı etkileyen etmenlerin belirlenmesi: dönme hızı, B, yüzey alanı, sarım sayısı

- **Ölçülen:** FİZ.11.2.12 a `FBAB8.SB1`
- **Yapı:** Düzgün alanda dönen N sarımlı çerçeve (basit jeneratör) için çerçevenin dönme hızı, alanın büyüklüğü, yüzey alanı ve sarım sayısı değiştirildiğinde alternatif akımın en büyük değerinin ve frekansının nasıl değiştiği sorulur; hangi değişikliklerin yalnız büyüklüğü, hangisinin frekansı etkilediği ayrılır.
- **Uyarıcı:** TEXT, DIAGRAM, DAILY_LIFE_CONTEXT, TABLE · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Sarım sayısı artarsa alternatif akımın frekansı da artar” (Büyüklük ile frekans bağımlılığını karıştırma); “Yüzey alanı arttıkça frekans azalır” (Alanın yalnızca büyüklüğü etkilediğini bilmeme); “Çerçeve daha hızlı dönerse yalnızca frekans artar, büyüklük değişmez” (Hızın akı değişim hızını da artırdığını bilmeme)
- **Öğrenci hataları:** Frekansı belirleyen tek etmenin dönme sıklığı olduğunu unutmak `CONCEPTUAL_ERROR`; En büyük değerin etmenlerle doğru orantısını kurmamak `PREREQUISITE_GAP`
- **Kanıt:** kitap s.255 6. adım a–ç; kitap s.262 Kontrol Noktası; program “Öğrenciler alternatif akımı etkileyen etmenleri öğ…”

### 105 · Dönen çerçevede akımın büyüklük ve yönü: Φ–t, ε–t, i–t grafikleri ve osiloskop görüntüsü · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.12 c `FBAB8.SB3`
- **Yapı:** Düzgün alanda sabit hızla dönen çerçevenin bir periyotluk beş konumu verilir; akımın büyüklük ve yön değişimi, akının en büyük/sıfır olduğu anlar, Φ–t ve ε–t grafiklerinin birbirine göre durumu ve (osiloskop ekranında) iki dalga biçiminin en büyük değer ve frekans karşılaştırması sorulur.
- **Uyarıcı:** GRAPH, DIAGRAM, DATA_SET · **Zorluk:** orta–zor
- **Çeldiriciler:** “Akı en büyük olduğunda akım da en büyüktür” (Akı ile akı değişim hızını karıştırma); “Yarım turda akımın yönü değişmez” (Yön değişimini (Lenz) bilmeme); “Frekansı büyük olan dalga, aynı ekranda daha geniş görünür” (Periyot–frekans ilişkisini ters kurma); “Dalganın tepe yüksekliği frekansı belirler” (Genlik ile frekansı karıştırma)
- **Öğrenci hataları:** Φ–t grafiğini ε–t grafiği sanmak `GRAPH_READING_ERROR`; Osiloskopta periyodu bulurken kare sayısını yanlış okumak `TABLE_READING_ERROR`
- **Kanıt:** kitap s.254 2. adım; kitap s.256 Çalışma Yaprağı 1; kitap s.261 43. Alıştırma; program “Öğrencilerin manyetik alandaki tel çerçeve bir tam…”

### 106 · Jeneratör deneyi verilerinden alternatif akım yorumu: LED parlaklığı ve AC–DC ayrımı

- **Ölçülen:** FİZ.11.2.12 b `FBAB8.SB2`, FİZ.11.2.12 c `FBAB8.SB3`
- **Yapı:** Döndürülen çerçeve ve LED/lamba düzeneğinden elde edilen veriler (dönme hızı, B, sarım sayısı, parlaklık/en büyük gerilim) tablo olarak verilir; verilerden etmen–etki ilişkisi yorumlanır, hatalı kayıt belirlenir; komşu devrede DC ve AC kaynak durumlarında akının değişip değişmediği ve lambanın yanıp yanmayacağı sorulur.
- **Uyarıcı:** TABLE, EXPERIMENT, DATA_SET, DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “DC kaynak bağlı devrede de bitişik devrede sürekli indüksiyon akımı oluşur” (Sabit akının indüksiyon yapmadığını bilmeme); “AC kaynakta lambanın parlaklığı sabittir” (AC'nin zamanla değiştiğini görememe); “LED sürekli yanıyorsa akım doğru akımdır” (Gözle ayırt edilemeyen hızlı yanıp sönmeyi bilmeme)
- **Öğrenci hataları:** Veri tablosunda tek satırla genelleme yapmak `TABLE_READING_ERROR`; Akıyı AC kaynakta sabit saymak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.255 9.–11. adım; kitap s.286 ÖD-16 a; program “Deney sırasında LED lambanın parlaklığını gözlemle…”; program “Kaydettikleri verilere dayalı olarak öğrenciler in…”

### 107 · Alternatif akımda etkin ve maksimum değerler: V_maks = √2 V_etkin, ısı eşdeğerliği

- **Ölçülen:** FİZ.11.2.12 c `FBAB8.SB3`
- **Yapı:** Direnç üzerinde aynı sürede aynı ısıyı açığa çıkaran DC ve AC devreleri verilir; DC değerinin AC'nin etkin değerine karşılık geldiği kullanılarak AC'nin maksimum gerilim/akımı, etkin akım ya da şebeke değerleri sorulur; ampermetre ve voltmetrenin hangi değeri ölçtüğü yorumlanır.
- **Uyarıcı:** TEXT, DIAGRAM, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Etkin gerilim, maksimum gerilimden büyüktür” (Etkin–maksimum ilişkisini ters kurma); “V_maks = V_etkin / √2” (Dönüşüm çarpanını ters uygulama); “Etkin değer, maksimum değerin yarısıdır” (√2 yerine 2 kullanma); “Ampermetre AC'de maksimum akımı gösterir” (Ölçü aletlerinin etkin değeri gösterdiğini bilmeme)
- **Öğrenci hataları:** V_maks hesabında √2 yerine 2 çarpmak `FORMULA_APPLICATION_ERROR`; DC'deki 20 V'u maksimum değer sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.259 Örnek; kitap s.294 ÖD-24 e; program “Kaydettikleri verilere dayalı olarak öğrenciler in…”
- **Kapsam notu:** AA devre elemanları (reaktans, empedans) programda yoktur; yalnız etkin/maksimum değer ve ısı eşdeğerliği vardır.

### 108 · AA frekansı ve periyodu: yön değişimi, en büyük değer ve lambanın sönme sayısı; şebeke tablosu

- **Ölçülen:** FİZ.11.2.12 c `FBAB8.SB3`
- **Yapı:** Bir ülkenin şebeke frekansı (50 ya da 60 Hz) verilir; periyodu, bir saniyede akımın yön değiştirme sayısı, mutlak değerce en büyük değere ulaşma sayısı, sıfır olma sayısı ve lambanın söndüğü an sayısı sorulur; frekansı 50 Hz'den 120 Hz'e değiştirince grafikteki değişim yorumlanır; şebekeler arası uyum tablosundan yorum yapılır.
- **Uyarıcı:** TEXT, TABLE, GRAPH, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “50 Hz'de akım saniyede 50 kez yön değiştirir” (Bir periyotta iki yön değişimini bilmeme); “50 Hz'de lamba saniyede 50 kez en büyük parlaklığa ulaşır” (Mutlak değerce tepe sayısını (iki tepe/periyot) bilmeme); “Frekans artınca tepe gerilim de artar” (Frekans ile genliği karıştırma); “T = f yazıldığında 50 Hz için T = 50 s” (Periyot–frekans ters ilişkisini bilmeme)
- **Öğrenci hataları:** T = 1/f yerine T = f kullanmak `FORMULA_SELECTION_ERROR`; Bir periyottaki sıfır geçiş sayısını bir sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.294 ÖD-24 ç–d; kitap s.288 ÖD-18; kitap s.260 42. Alıştırma; program “Kaydettikleri verilere dayalı olarak öğrenciler in…”

## FİZ.11.2.13

### 109 · Transformatörün yapısı ve nitelikleri: deney verisiyle sarım sayısı–gerilim ilişkisi, DC/AC farkı · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.13 a `FBAB8.SB1`
- **Yapı:** 600 ve 1200 sarımlı bobin, demir çekirdek ve alçak gerilim kaynağıyla yapılan deneyin verileri (birincil/ikincil gerilim, sarım sayıları) tablo olarak verilir; sarım oranı ile gerilim oranının ilişkisi, AC yerine DC bağlandığında ikincil gerilimin (kararlı durumda) sıfır olması, birincil/ikincil bobin ve demir çekirdeğin görevi sorulur; sayısal hesap yok, oran yorumlanır.
- **Uyarıcı:** TABLE, EXPERIMENT, DIAGRAM, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Transformatör doğru akımla da çalışır” (Değişken akı koşulunu bilmeme); “İkincil gerilim, birincil gerilimden her zaman büyüktür” (Yükseltici/alçaltıcı ayrımını bilmeme); “Sarım sayısı arttıkça gerilim azalır” (Gerilim–sarım ilişkisini ters kurma); “Demir çekirdek, ikincil bobine elektrik akımını doğrudan iletir” (Çekirdeğin manyetik akıyı taşıdığını, akımı iletmediğini bilmeme)
- **Öğrenci hataları:** Oran okurken birincil–ikincil sütunlarını karıştırmak `TABLE_READING_ERROR`; DC'de ilk anda ölçülen kısa süreli değeri kararlı değer sanmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** kitap s.265 13. Etkinlik 12.–16. adım; kitap s.268 Yapı; program “Öğrenciler bu nitelikler arasındaki ilişkileri den…”; kılavuz s.114
- **Kapsam notu:** Program–kitap çelişkisi yok (veri örüntüsü düzeyi); ancak kitap s.268'de Vp/Vs = Np/Ns formülünü açıkça verir, program 'matematiksel işlemlerden kaçınılır' der.

### 110 · Yükseltici/alçaltıcı transformatör: sarım, gerilim ve akım ilişkisinin oran yorumu · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.13 a `FBAB8.SB1`
- **Yapı:** Ideal transformatörde birincil ve ikincil sarım sayısı / gerilim bilgisinden türü (yükseltici/alçaltıcı), gerilimlerin, akımların ve güçlerin karşılaştırması, ikincil akımın birincilden büyük/küçük olması sorulur; ideal olmayan transformatörde giriş gücünün çıkış gücünden büyük olduğu yorumlanır.
- **Uyarıcı:** TEXT, DIAGRAM, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Gerilimi yükselten transformatörde akım da yükselir” (Güç korunumunu (V·i sabit) bilmeme); “Alçaltıcı transformatörde ikincil sarım sayısı birinciden büyüktür” (Sarım–gerilim ilişkisini ters kurma); “Transformatör enerji üretir, çıkış gücü girişten büyük olabilir” (Enerji korunumunu bilmeme); “İdeal olmayan transformatörde verim %100'dür” (İdeal–gerçek ayrımını bilmeme)
- **Öğrenci hataları:** Akım oranını sarım oranıyla düz orantılı almak `FORMULA_APPLICATION_ERROR`; Birincil–ikincil bobinleri karıştırmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** kitap s.270 45. Alıştırma; kitap s.271 46. Alıştırma; kitap s.288 ÖD-18; program “Transformatörlerin nitelikleri arasındaki ilişkile…”
- **Kapsam notu:** Program–kitap çelişkisi: program matematiksel işlemlerden kaçınılmasını ister; kitap 46. Alıştırma b–c'de sarım oranı ve güç hesaplatır, ÖD-18 c'de sarım sayıları oranı ister. Aile oran/yön/yorum düzeyindedir, sayısal hesap (V, W) örnek varyasyonu olarak işaretlenmemiştir.

### 111 · Birden çok transformatörün zincirlenmesi ve lamba parlaklığı karşılaştırması · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.13 a `FBAB8.SB1`
- **Yapı:** Aynı AC kaynağa bağlı, farklı sarım oranlı ideal transformatörlere bağlanan özdeş lambaların parlaklıkları karşılaştırılır; iki transformatörün ardışık bağlandığı sistemde son gerilimin ilk gerilime oranı; hedef gerilime ulaşmak için hangi sarım oranının değiştirileceği ve (yapı farkı: çekirdeksiz, açık çekirdek, DC kaynak) hangi transformatörde ikincil gerilim oluşacağı sorulur.
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Sarım sayısı en büyük transformatörün lambası en parlaktır” (Oran yerine mutlak sarım sayısına bakma); “Ardışık transformatörlerde gerilim oranları toplanır” (Oranların çarpılması gerektiğini bilmeme); “DC kaynaklı transformatörün ikincil bobininde de sürekli gerilim oluşur” (Değişken akı koşulunu bilmeme)
- **Öğrenci hataları:** Çarpma yerine toplama yapmak `ARITHMETIC_ERROR`; Oranı (Ns/Np) ters kurmak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.272 47. Alıştırma; program “Transformatörlerin nitelikleri arasındaki ilişkile…”
- **Kapsam notu:** Program–kitap çelişkisi: kitap 47. Alıştırma a'da 270 V gibi sayısal değerler verir; program matematiksel işlemlerden kaçınır. Aile oran düzeyinde kurulmuş, sayısal çözüm 'çarpan' olarak ele alınmıştır.

### 112 · Elektriğin iletiminde enerji kaybı ve transformatörün rolü: yüksek gerilim–düşük akım · ⚠️ kitap–program çelişkili formül

- **Ölçülen:** FİZ.11.2.13 c `FBAB8.SB3`
- **Yapı:** Santralden şehre uzanan iletim hattı modeli (yükseltici, ara ve alçaltıcı transformatörler) verilir; iletim tellerinde enerji kaybının nedeni (Joule ısınması), kaybı azaltma yolu (akımı düşürme → gerilimi yükseltme) ve her transformatörün görevi yorumlanır; aynı güç iletilirken akım azalınca kaybın nasıl değiştiği oran düzeyinde sorulur.
- **Uyarıcı:** TEXT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Kayıp, gerilim yükseldikçe artar” (Güç–akım–kayıp zincirini yanlış kurma); “Enerji kaybını azaltmanın tek yolu kalın tel kullanmaktır, transformatör gerekmez” (Transformatörün temel rolünü bilmeme); “Kayıp akımla doğru orantılıdır (P = i·R)” (P = i²R ile P = iR karıştırma); “Alçaltıcı transformatör iletim kaybını azaltır” (Yükseltici/alçaltıcı görevlerini (iletim, kullanım) karıştırma)
- **Öğrenci hataları:** P = i²R yerine P = iR yazmak `FORMULA_SELECTION_ERROR`; Yükseltici ve alçaltıcı transformatörün konumunu ters yerleştirmek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.269 Örnek; kitap s.294 ÖD-24 c; program “toplum yararına en verimli yolun, elektriğin en dü…”
- **Kapsam notu:** Program–kitap çelişkisi: kitap P = V·i ve P = i²R modellerini verir; program 'matematiksel işlemlerden kaçınılır' der. Aile yorum/oran düzeyindedir.

### 113 · Transformatörün kullanım alanları ve rolü: bilgilerin kaydı ve yorumu

- **Ölçülen:** FİZ.11.2.13 b `FBAB8.SB2`, FİZ.11.2.13 c `FBAB8.SB3`
- **Yapı:** Kullanım alanı – rolü sütunlu bir kayıt tablosu (cep telefonu şarjı, mikrodalga fırın, tıraş makinesi, elektrikli araç şarjı, santral–şehir hattı) verilir; kayıtların doğruluğu, eksik/yanlış hücre ve her cihazdaki transformatörün rolü (gerilimi yükseltme/alçaltma) yorumlanır; gerilim dönüştürücü gereksinimi (110 V cihazın 220 V şebekede kullanımı) değerlendirilir.
- **Uyarıcı:** TABLE, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Dizüstü bilgisayar şarj aletindeki transformatör gerilimi yükseltir” (Alçaltıcı/yükseltici rolünü yanlış belirleme); “110 V'luk cihaz 220 V'a bağlanınca daha verimli çalışır” (Cihaz–şebeke uyumunu bilmeme); “Transformatör, doğru akım pillerinin gerilimini de değiştirir” (AC koşulunu bilmeme)
- **Öğrenci hataları:** Kayıt tablosunda uygulama ile rolünü karıştırmak `TABLE_READING_ERROR`; Cihaz etiketindeki gerilim değerini şebeke gerilimi sanmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** kitap s.265 13. Etkinlik 18. adım; kitap s.263 Gerilim dönüştürücü; program “Öğrenciler transformatörlerin kullanım alanlarını …”

## FİZ.11.3.1

### 114 · Işık şiddeti, ışık akısı ve aydınlanmanın tanımı, birimi ve bağlı olduğu etmen

- **Ölçülen:** FİZ.11.3.1 a `FBAB8.SB1`
- **Yapı:** Bir bağlamda (ampul kutusu, püskürtme boya analojisi, sulama sistemi benzetimi) üç niceliğin hangi tanıma, hangi SI birimine (cd, lm, lx) ve hangi etmene (kaynak, yüzey alanı, uzaklık) karşılık geldiği eşleştirilir ya da doğru/yanlış olarak değerlendirilir.
- **Uyarıcı:** TEXT, DAILY_LIFE_CONTEXT, DIAGRAM · **Zorluk:** kolay
- **Çeldiriciler:** “Işık şiddeti, ışığın yüzeye düşen miktarıdır” (Işık şiddeti ile ışık akısını karıştırma); “Aydınlanma kaynağın özelliğidir, yüzeyin konumundan bağımsızdır” (Aydınlanmayı kaynağa ait büyüklük sanma); “Lümen ampulün harcadığı elektrik gücünü gösterir” (Lümen ile watt (güç) kavramlarını karıştırma)
- **Öğrenci hataları:** cd, lm, lx birimlerini niceliklerle yanlış eşleştirmek `UNIT_ERROR`; Akıyı 'yüzeye düşen miktar' değil 'kaynağın yaydığı güç' diye tanımlamak `CONCEPTUAL_ERROR`
- **Kanıt:** program “Öğrenciler ışık şiddeti, ışık akısı ve aydınlanma …”; kitap s.304 1. Etkinlik 7. adım (analoji); kitap s.306 Işık akısı tanımı; kitap s.310 2. Alıştırma
- **Kapsam notu:** Kavram tanımı ailesi: hesap içermez; kapalı yüzey akısı ve nokta kaynak aydınlanması sayısal ailelerde ele alınır.

### 115 · Işık niceliklerinin bağlı olduğu etmenlerin nitel yorumu (parlaklık, uzaklık, yüzey, eğim)

- **Ölçülen:** FİZ.11.3.1 a `FBAB8.SB1`, FİZ.11.3.1 c `FBAB8.SB3`
- **Yapı:** Bir ışık düzeneğinde bir etmen (kaynağın parlaklığı, kaynak–yüzey uzaklığı, yüzey alanı, yüzeyin eğimi, oda büyüklüğü) değiştirilir; ışık şiddeti, toplam ışık akısı ve bir noktadaki aydınlanmanın artıp azalmadığı ya da değişmediği gerekçeyle sorulur.
- **Uyarıcı:** TEXT, DAILY_LIFE_CONTEXT, TABLE, GRAPH · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Avize alçaldığında ışık şiddeti artar” (Işık şiddetini kaynak–yüzey uzaklığına bağlı sanma); “Küçük odada toplam ışık akısı artar” (Kapalı yüzeyin toplam akısının yüzeye değil yalnız şiddete bağlı olduğunu bilmeme); “Kâğıt yatırıldığında aydınlanma değişmez çünkü kaynak aynıdır” (Aydınlanmanın dik düşen miktara bağlı olduğunu bilmeme)
- **Öğrenci hataları:** Kaynağın niceliği (şiddet) ile yüzey niceliğini (aydınlanma) aynı sayıp tek tek değerlendirmemek `CONCEPTUAL_ERROR`; Paralel ışıkta uzaklık artınca aydınlanmanın azalacağını varsaymak (nokta kaynak kuralını uygulamak) `CONCEPTUAL_ERROR`
- **Kanıt:** program “bağlı oldukları etmenlere göre yorumlar ve değerle…”; kitap s.309 1. Alıştırma; kitap s.310 Çalışma Yaprağı 1; kılavuz s.114

### 116 · Noktasal kaynakta aydınlanmanın uzaklıkla değişimi (ters kare) ve veri/grafik yorumu

- **Ölçülen:** FİZ.11.3.1 b `FBAB8.SB2`, FİZ.11.3.1 c `FBAB8.SB3`
- **Yapı:** Noktasal kaynağın farklı uzaklıklardaki yüzeylerde (dik gelen ışınlar) oluşturduğu aydınlanma değerleri tablo, grafik ya da küre yüzeyi şekliyle verilir; E·r² sabitliği, eksik değer, kaynağın şiddeti ya da aydınlanma oranı sorulur.
- **Uyarıcı:** TABLE, GRAPH, DATA_SET, DIAGRAM, TEXT, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Uzaklık iki katına çıkınca aydınlanma yarıya iner” (Ters kare ilişkisini ters orantı sanma); “Büyük küre yüzeyinde aydınlanma daha büyüktür çünkü alan büyüktür” (Alan ile aydınlanmayı doğru orantılı sanma); “Aynı kürenin farklı noktalarında aydınlanma farklıdır” (Küre yüzeyinde dik gelen ışınlarda r sabit olduğunu görememe)
- **Öğrenci hataları:** E = I/r yazmak ya da r² yerine 2r kullanmak `FORMULA_APPLICATION_ERROR`; Tablodan E·r² yerine E·r çarpımının sabit olup olmadığına bakmak `TABLE_READING_ERROR`; Santimetre uzaklığı metreye çevirmemek `UNIT_ERROR`
- **Kanıt:** program “Öğrenciler simülasyon veya deney düzenekleri kulla…”; kitap s.305 1. Etkinlik 9. adım tablo; kitap s.307 Aydınlanma modeli; kitap s.311 2. Alıştırma Enis; kılavuz s.115

### 117 · Işınların yüzeye eğik gelmesi: açı ile aydınlanmanın değişimi

- **Ölçülen:** FİZ.11.3.1 b `FBAB8.SB2`, FİZ.11.3.1 c `FBAB8.SB3`
- **Yapı:** Noktasal kaynağın ışınları yüzeye normalle α açısı yapacak biçimde gelir; farklı α ve r için aydınlanma değerleri verilir ya da sorulur; α = 0° maksimum, α = 90° (ışınlar yüzeye paralel) sıfır aydınlanma sonuçları kullanılır.
- **Uyarıcı:** DIAGRAM, TABLE, DATA_SET, TEXT · **Zorluk:** orta
- **Çeldiriciler:** “Yüzeyi yatırınca ışık akısı değişmez, aydınlanma da değişmez” (Dik düşen ışık miktarına bağlılığı bilmeme); “Aydınlanma açıyla doğru orantılıdır (açı büyüdükçe artar)” (cosα bağıntısını açıyla doğru orantı sanma); “Yüzeyle yapılan açı normalle yapılan açıdır, o hâlde sin kullanılır” (Gelme açısını yüzeyle ölçme karışıklığı)
- **Öğrenci hataları:** Yüzeyle yapılan açının cosinüsünü almak (normalle yapılan açı yerine) `FORMULA_APPLICATION_ERROR`; Eğik gelişte r yerine yüzeye iz düşümü uzaklığı kullanmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “ışık şiddetinin ışık akısı ve aydınlanma kavramlar…”; kitap s.307 Eğik gelen ışın modeli; kitap s.305 1. Etkinlik tablo
- **Kapsam notu:** cosα ile bağıntı kitabın anlatımındadır; programda açık bir sınır yoktur (NO_EXPLICIT_LIMIT).

### 118 · Kapalı yüzeyde toplam ışık akısı (Φ = 4πI) ve yüzeyin ışığı çevreleme oranı

- **Ölçülen:** FİZ.11.3.1 b `FBAB8.SB2`, FİZ.11.3.1 c `FBAB8.SB3`
- **Yapı:** Merkezinde (ya da içinde) noktasal ışık kaynağı bulunan küre, yarım küre, çeyrek küre ya da başka kapalı yüzeylerin toplam akıları karşılaştırılır; yüzeyin şekli ve büyüklüğünün toplam akıyı etkilemediği, kaynağı ne kadarının çevrelediği ve kaynak şiddeti ile ilişkisi kullanılır.
- **Uyarıcı:** DIAGRAM, TEXT, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Büyük kürenin toplam akısı daha büyüktür” (Toplam akıyı yüzey alanına bağlı sanma); “Kaynak yüzeyden uzaklaştıkça toplam akı azalır” (Kapalı yüzeyde akının yalnız şiddete bağlı olduğunu bilmeme); “Yarım kürenin akısı tam kürenin akısına eşittir” (Yüzeyin kaynağı çevreleme oranını yok sayma)
- **Öğrenci hataları:** Φ = 4πI yerine Φ = I/r² kullanmak `FORMULA_SELECTION_ERROR`; π değerini katmadan oran kurmak ya da r² ile çarpmak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** program “Öğrenciler ışık şiddeti, ışık akısı ve aydınlanma …”; kitap s.306 Kapalı yüzeyde ışık akısı; kitap s.311 2. Alıştırma

### 119 · Filtre, birden çok kaynak ve akı yüzdesi ile aydınlanma değişimi

- **Ölçülen:** FİZ.11.3.1 b `FBAB8.SB2`, FİZ.11.3.1 c `FBAB8.SB3`
- **Yapı:** Kaynak ile perde arasına ışık akısının belirli yüzdesini geçiren filtreler konur (ya da çıkarılır) ya da aynı noktayı aydınlatan birden fazla kaynak vardır; perdedeki bir noktanın aydınlanması başlangıç değerinin katı olarak sorulur.
- **Uyarıcı:** DIAGRAM, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “İki filtre birlikte %70 geçirir (yüzdeler toplanır)” (Ardışık filtrelerde geçirme oranlarının çarpıldığını bilmeme); “Filtre kaldırılınca aydınlanma bir kat artar” (Katı oran olarak hesaplamama); “Aydınlanma yüzey alanı artınca artar” (Eşit akı, farklı alan durumunda aydınlanma ilişkisini ters kurma)
- **Öğrenci hataları:** Filtre oranlarını toplamak ya da çıkarmak (çarpmak yerine) `ARITHMETIC_ERROR`; Filtre sonrası akıyı kaynağın şiddeti sanıp r² ile bölmemek `FORMULA_APPLICATION_ERROR`
- **Kanıt:** program “bağlı oldukları etmenlere göre yorumlar ve değerle…”; kitap s.392 ÖD-3; kitap s.391 ÖD-1

### 120 · Ampul tablosundan lümen/watt verimliliği ve aydınlatma planlaması

- **Ölçülen:** FİZ.11.3.1 b `FBAB8.SB2`, FİZ.11.3.1 c `FBAB8.SB3`
- **Yapı:** Ampul çeşitlerinin güç (W), toplam ışık akısı (lm) ve ömür değerleri tablo olarak verilir; verimlilik (lm/W) karşılaştırılır; verilen ortam büyüklüğü ve alan başına gerekli lümen değerine göre ampul sayısı ve toplam güç bulunur.
- **Uyarıcı:** TABLE, DATA_SET, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Gücü büyük ampul her zaman daha parlaktır” (Güç ile ışık akısını (lm) karıştırma); “Daha uzun ömürlü ampul daha verimlidir” (Ömür ile lm/W verimliliğini karıştırma); “Ampul sayısı yuvarlanırken aşağı yuvarlanır” (Yeterli aydınlanma koşulunu yok sayma)
- **Öğrenci hataları:** Gerekli lümeni alan ile çarpmadan ampul sayısını bölmek `QUESTION_INTERPRETATION_ERROR`; Kesirli ampul sayısını yukarı yuvarlamamak `ARITHMETIC_ERROR`
- **Kanıt:** program “ampulün gücü ile enerjisi arasındaki ilişkiye…”; kitap s.308 Örnek (ampul tablosu); kitap s.303 1. Etkinlik 4–5. adım
- **Kapsam notu:** E = P·t elektrik ön bilgisine dayanır; kitap bu planlamayı Örnek olarak sayısal işler.

## FİZ.11.3.2

### 121 · Düzlem aynalarda yansıma yasalarıyla ışının izlediği yol (tek ve çok aynalı düzenek)

- **Ölçülen:** FİZ.11.3.2 a `FBAB9.SB1`
- **Yapı:** Bir ya da birden çok düzlem aynaya gelen ışının yansıma yasalarına (gelme açısı = yansıma açısı, gelen–yansıyan–normal aynı düzlem) göre izlediği yol çizilir; verilen giriş–çıkış doğrultusuna uygun ayna konumu ve eğimi ya da ışının çıkacağı nokta bulunur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Işın aynaya gelme açısına eşit açıyla yüzeyle ölçülerek yansır (normal yerine yüzey kullanılır)” (Gelme ve yansıma açılarını normalle değil yüzeyle ölçme); “Dik gelen ışın yüzeyde saparak yansır” (Dik gelişte yansıma yönünü bilmeme); “İki aynalı düzenekte ışın yönü ayna açısına bağlı değildir” (Ardışık yansımalarda her aynanın normalini ayrı çizmeme)
- **Öğrenci hataları:** Normali çizmeden yansıyan ışını yüzeyin simetriği olarak çizmek `METHOD_SELECTION_ERROR`; Gelme açısını yüzeyle ölçmek `QUESTION_INTERPRETATION_ERROR`; İkinci aynada gelme açısını birinci aynadaki değerle aynı almak `CONCEPTUAL_ERROR`
- **Kanıt:** program “düzlem aynada yansıma ve görüntü oluşumunun kurall…”; kitap s.315 Yansıma yasaları; kitap s.320 3. Alıştırma (HUD); kitap s.405 ÖD-25 periskop; kitap s.393 ÖD-5

### 122 · Düzlem aynada görüntünün özellikleri (sanal, düz, eşit boy, simetrik) ve ayna yazısı

- **Ölçülen:** FİZ.11.3.2 a `FBAB9.SB1`
- **Yapı:** Düzlem aynadaki cisim, harf-sözcük ya da uzuv için görüntünün sanal/gerçek, düz/ters, boy ve aynaya uzaklık özellikleri; aynanın eğimi, cismin hareketi ya da yazının ayna yazısı olarak çizimi sorulur.
- **Uyarıcı:** DIAGRAM, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Düzlem aynadaki görüntü cisimden küçüktür” (Uzaklıkla görüntü boyunun azaldığı yanılgısı); “Düzlem aynadaki görüntü gerçektir çünkü gözle görülür” (Görülmeyi gerçek görüntüyle özdeşleştirme); “Ayna döndürülünce görüntünün boyu da değişir” (Simetri modelini ayna eğimine uygulayamama)
- **Öğrenci hataları:** Görüntü uzaklığını aynadan göze (cisim–göz) ölçmek `QUESTION_INTERPRETATION_ERROR`; Ayna yazısında yalnız satır sırasını ters çevirip harfleri çevirmemek `CARELESS_ERROR`
- **Kanıt:** program “düzlem aynada yansıma ve görüntü oluşumunun kurall…”; kitap s.317 Görüntü özellikleri; kitap s.320 4. Alıştırma; kitap s.393 ÖD-6; kitap s.391 ÖD-2
- **Kapsam notu:** Eski programlarda çok görülen 'açılı aynalarda görüntü sayısı' kapsam dışıdır (pm-angled-image-count).

### 123 · Düzlem aynada görüş alanı: hangi cisimler görülür, uzaklık ve konum değişimi

- **Ölçülen:** FİZ.11.3.2 a `FBAB9.SB1`, FİZ.11.3.2 b `FBAB9.SB2`
- **Yapı:** Gözün aynadaki görüntüsünden aynanın uçlarına çizilen doğrularla görüş alanı bulunur; ayna önünde bulunan cisimlerden hangilerinin görülebildiği, gözlemci aynaya yaklaşınca/uzaklaşınca ya da yana kayınca görüş alanının nasıl değiştiği veya hareketli cismin ne kadar süre görüldüğü sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Aynadan uzaklaşınca görüş alanı büyür” (Görüş alanının aynaya uzaklıkla büyüdüğü yanılgısı); “Cismin önünde başka cisim olsa da aynadan her cisim görülür” (Saydam olmayan cisimlerin ardının görünmediğini yok sayma); “Göz aynaya paralel yana kayınca görüş alanı ortadan kalkar/aynı kalır” (Görüş alanının konumu ile büyüklüğünü karıştırma)
- **Öğrenci hataları:** Görüş alanını gözden aynanın uçlarına çizilen ışınların yansıması yerine doğrudan doğrular olarak çizmek `METHOD_SELECTION_ERROR`; Gözün görüntüsünü aynaya göre simetrik almamak `CONCEPTUAL_ERROR`; Birimkare sayarken ayna ucunu eksik ya da fazla sayarak süreyi yanlış bulmak `CARELESS_ERROR`
- **Kanıt:** program “Öğrenciler günlük hayatta veya geçmiş öğrenmelerin…”; kitap s.317 Görüş alanı yöntemleri; kitap s.321 5. Alıştırma; kitap s.318 Örnek (göl); kitap s.391 ÖD-2
- **Kapsam notu:** Yana (aynaya paralel) kayma görüş alanının konumunu kaydırır, büyüklüğünü değiştirmez; kitabın ölçme sorusu (ÖD-2) bu ayrıma dayanır.

### 124 · Kişinin kendini tam görmesi için gereken ayna boyu ve konumu

- **Ölçülen:** FİZ.11.3.2 b `FBAB9.SB2`
- **Yapı:** Boyu verilen bir kişi düşey duran düzlem aynada kendini baştan ayağa görmek ister; ayna boyunun en az kaç kat olması gerektiği, aynanın alt/üst kenarının yerden yüksekliği ve kişi aynadan uzaklaşınca durumun değişip değişmeyeceği sorulur.
- **Uyarıcı:** DIAGRAM, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Kendini tam görmek için ayna boyu kişinin boyuna eşit olmalıdır” (Görüş alanı ve simetri ilişkisini kurmadan tam boy gerektiğini sanma); “Aynadan uzaklaşınca daha büyük ayna gerekir” (Gerekli ayna boyunun uzaklığa bağlı olduğunu sanma); “Ayna boyu göz ile ayak arasındaki mesafenin yarısı olmalıdır” (Baş ile ayak yerine göz–ayak/göz–tepe parçalarını karıştırma)
- **Öğrenci hataları:** Gözü boyun yarısında varsayıp ayna kenar yüksekliklerini yanlış hesaplamak `ARITHMETIC_ERROR`; Işın yolunu çizmeden sezgiyle sonuç vermek `METHOD_SELECTION_ERROR`
- **Kanıt:** program “Öğrenciler günlük hayatta veya geçmiş öğrenmelerin…”; kitap s.391 ÖD-2; kitap s.317 Görüş alanı
- **Kapsam notu:** Kitapta yalnız ölçme sorusunda ifade olarak geçer; ayna boyunun boy/2 olduğu sonucu görüş alanı + simetri modelinin yeni duruma uyarlanmasıdır.

### 125 · Cisim ya da ayna hareket ederken görüntünün hareketi (göreli hız) · **zenginleştirme**

- **Ölçülen:** FİZ.11.3.2 b `FBAB9.SB2`
- **Yapı:** Düzlem aynaya dik doğrultuda sabit hızla yaklaşan ya da uzaklaşan cismin (veya hareket eden aynanın) görüntüsünün hızı ve cisim ile görüntü arasındaki göreli hız sorulur.
- **Uyarıcı:** TEXT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Görüntü cisimle aynı hızla aynadan uzaklaştığı için aralarındaki hız v'dir” (Göreli hızı ayna referansında bırakma); “Ayna hareket ederse görüntü hareket etmez” (Simetri düzleminin kaydığını göz ardı etme); “Ayna v hızıyla hareket edince görüntü de v hızıyla hareket eder” (Aynanın hareketinde görüntü yer değiştirmesinin iki katına çıktığını bilmeme)
- **Öğrenci hataları:** Göreli hızı iki hızın farkı yerine tek hız olarak almak `VECTOR_ERROR`; Başlangıç uzaklığını cisim–görüntü yerine cisim–ayna olarak kullanmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “yeni durumlara uyarlayarak…”; kitap s.317 Görüntü özellikleri
- **Kapsam notu:** Kitapta işlenmemiştir; düzlem ayna simetri modelinin yeni duruma (hareketli cisim) uyarlanması olarak türetilir. Eski kaynaklarda sık görülür.

### 126 · Düzlem ayna ile bilgi temelli problem çözümü için model önerme ve yeni duruma uyarlama

- **Ölçülen:** FİZ.11.3.2 a `FBAB9.SB1`, FİZ.11.3.2 b `FBAB9.SB2`
- **Yapı:** Bir gereksinim (köşedeki kör noktayı görme, mağazada belirli bölgeyi izleme, görüntüyü başka yöne iletme) ve kısıtlar verilir; öğrenciden uygun ayna yerleşimini kuran modeli seçmesi, modelin hangi koşulda yetersiz kaldığını belirlemesi ya da yeni bir duruma uygun şekilde uyarlaması istenir.
- **Uyarıcı:** TEXT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Aynayı büyütmek görüntünün boyunu büyütür ve sorunu çözer” (Düzlem ayna görüntü boyunun cisme eşit olduğunu bilmeme); “Tek düzlem ayna her köşede ve her uzaklıkta aynı görüş alanını sağlar” (Görüş alanının ayna ve gözün konumuna bağlı olduğunu görememe); “Ayna sayısı arttıkça ışın kaybolmaz, görüntü daha parlak olur” (Yansıma kayıplarını ve görüntü yönünü yok sayma)
- **Öğrenci hataları:** Tasarımı yansıma yasasıyla sınamadan çizmek `METHOD_SELECTION_ERROR`; Görüş alanı sınırlılığını modelde dikkate almamak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “STEM yaklaşımına uygun bilgi temelli hayat problem…”; kitap s.313 2. Etkinlik 3–4. adım; kitap s.315 1. Performans Görevi; kılavuz s.114
- **Kapsam notu:** Program açık uçlu performans görevi önerir; çoktan seçmeli karşılığı bir modelin uygunluğunu/sınırını seçtirme biçimindedir.

### 127 · Birbirine dik aynalar (köşe yansıtıcı) ve geri yansıma

- **Ölçülen:** FİZ.11.3.2 b `FBAB9.SB2`
- **Yapı:** Birbirine dik iki (ya da üç) düzlem aynaya gelen ışının ardışık yansımalarla izlediği yol çizilir; çıkan ışının gelen ışına paralel ve zıt yönlü olduğu ve bu özelliğin bir uygulamada (reflektör, retroreflektör) kullanımı değerlendirilir.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Dik aynalardan yansıyan ışın gelen ışına dik çıkar” (Ardışık yansımalarda açı toplamını hesaplamama); “Işın dik aynalarda yalnız bir kez yansır” (Yansıma sayısını yanlış belirleme); “Işın geri dönmez, çünkü yansıma yasası geri dönüşe izin vermez” (Yansıma yasasını geri dönüşle çelişkili sanma)
- **Öğrenci hataları:** İkinci aynada normali yanlış çizmek `METHOD_SELECTION_ERROR`; Gelme açısını θ yerine 90° − θ almak `CARELESS_ERROR`
- **Kanıt:** program “yeni durumlara uyarlayarak…”; kitap s.406 ÖD-26; kitap s.312 Giriş (reflektör)

### 128 · Düzgün ve dağınık yansıma ile görünürlük

- **Ölçülen:** FİZ.11.3.2 a `FBAB9.SB1`
- **Yapı:** Düz ve pürüzlü yüzeylere gelen paralel ışınların yansıması karşılaştırılır; mikro ayna dizisi, mat yüzey ya da cilalı yüzey gibi bağlamda yansıma türü ve cismin görülebilirliği, ekranda aydınlık/karanlık oluşumu sorulur.
- **Uyarıcı:** DIAGRAM, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Dağınık yansımada yansıma yasası uygulanmaz” (Dağınık yansımada yasanın geçerliliğini yok sayma); “Cisimleri görmemiz için cismin ışık yayması gerekir” (Görmenin yansıyan ışıkla olduğunu bilmeme); “Mat yüzeyde görüntü oluşur, cilalı yüzeyde oluşmaz” (Düzgün yansıma ile görüntü oluşumunu karıştırma)
- **Öğrenci hataları:** Pürüzlü yüzeyde tüm normalleri paralel çizmek `CONCEPTUAL_ERROR`; 0/1 sinyal dizilimini yansıma türüne yanlış eşlemek `TABLE_READING_ERROR`
- **Kanıt:** program “düzlem aynada yansıma ve görüntü oluşumunun kurall…”; kitap s.316 Düzgün/dağınık yansıma; kitap s.404 ÖD-24

### 129 · Açılı iki düzlem aynada oluşan görüntü sayısı · **hesap kapsam dışı**

- **Ölçülen:** FİZ.11.3.2 b `FBAB9.SB2`
- **Yapı:** Aralarındaki açı verilen iki düzlem aynanın önündeki cismin kaç görüntüsü oluştuğu, ya da görüntü sayısından aynalar arasındaki açı sorulur (n = 360°/α − 1).
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** orta
- **Çeldiriciler:** “Görüntü sayısı 360°/α'dır (−1 unutulur)” (Formülde −1 terimini unutma); “Aynalar paralelse iki görüntü oluşur” (Paralel aynalarda çoklu yansımayı bilmeme)
- **Öğrenci hataları:** 360/α bölmesinin tam sayı olmadığı durumlarda kuralı yanlış uygulamak `FORMULA_APPLICATION_ERROR`
- **Kanıt:** kitap s.393 ÖD-6b (ayna eğimi, görüntü sayısı değil)
- **Kapsam notu:** Görüntü sayısı formülü ne programda ne kitapta vardır (formül: plane-mirror-image-count, OUT_OF_CURRICULUM). Eski program kaynaklarında çok görülür; öğrenci karşılaşırsa yalnız nitel bilgi (iki aynada çoklu görüntü) verilir, formül işletilmez.

## FİZ.11.3.3

### 130 · Küresel aynanın temel elemanları (M, T, F, f, r = 2f) ve konum belirleme

- **Ölçülen:** FİZ.11.3.3 a `KB2.7.SB1`
- **Yapı:** Birimli zemin ya da şekil üzerinde küresel aynanın bir elemanı (tepe noktası, odak, merkez, eğrilik yarıçapı) verilir; diğer elemanların yeri, odak uzaklığı–eğrilik yarıçapı ilişkisi (r = 2f), konumların sıralaması ya da küresel ve silindirik yüzey farkı sorulur.
- **Uyarıcı:** DIAGRAM, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Odak noktası aynanın merkezidir” (Odak ile eğrilik merkezini karıştırma); “Eğrilik yarıçapı odak uzaklığının yarısıdır” (r = 2f bağıntısını ters kurma); “Küresel ve silindirik yüzeyler ışığı aynı biçimde tek noktada toplar” (Küresel yüzeyin nokta, silindirik yüzeyin doğru üzerinde odakladığını bilmeme)
- **Öğrenci hataları:** Merkez ile odak arasındaki uzaklığı odak uzaklığı sanmak `CONCEPTUAL_ERROR`; Birimkareli şekilde f ve r'yi ters sayarak konum belirlemek `CARELESS_ERROR`
- **Kanıt:** program “asal eksen, tepe noktası, odak noktası ve merkez n…”; kitap s.326 Temel kavramlar; kitap s.323 3. Etkinlik 1. adım; kitap s.395 ÖD-9

### 131 · Çukur aynada özel ışınların yansıma yolu

- **Ölçülen:** FİZ.11.3.3 a `KB2.7.SB1`
- **Yapı:** Çukur aynaya asal eksene paralel, odaktan, merkezden ya da tepe noktasına gönderilen ışının yansıdıktan sonra izlediği yol çizilir ya da hangi özel ışının çizildiği/yansıma doğrultusu belirlenir.
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Asal eksene paralel gelen ışın merkezden geçecek şekilde yansır” (Odak ile merkezi karıştırma); “Tepe noktasına gelen ışın kendi üzerinden döner” (Normal yönünü (merkez yerine tepe) yanlış belirleme); “Odaktan gelen ışın odaktan geçerek yansır” (Tersinirlik ilkesini yanlış uygulama)
- **Öğrenci hataları:** Yansıyan ışını normali çizmeden odaktan geçirmek `METHOD_SELECTION_ERROR`; Tepe noktasındaki yansımada eşit açıları aynı tarafa çizmek `CARELESS_ERROR`
- **Kanıt:** program “Öğrenciler ışınların küresel aynalardan yansıdıkta…”; kitap s.327 Tablo 3.1; kitap s.325 3. Etkinlik 10. adım tablo; kitap s.341 Kontrol Noktası

### 132 · Tümsek aynada özel ışınların yansıma yolu ve uzantıları

- **Ölçülen:** FİZ.11.3.3 a `KB2.7.SB1`
- **Yapı:** Tümsek aynaya asal eksene paralel gelen ya da uzantısı odak/merkezden geçen ya da tepe noktasına çarpan ışının yansıması çizilir; yansıyan ışının uzantısının asal ekseni kestiği noktalar belirlenir.
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Tümsek aynada paralel ışınlar yansıyınca odakta gerçekten kesişir” (Tümsek aynada odağın sanal olduğunu bilmeme); “Tümsek aynada paralel demet toplanarak aynanın önünde bir noktaya gider” (Tümsek aynanın dağıtıcı olduğunu bilmeme); “Uzantısı merkezden geçen ışın odaktan geçecek şekilde yansır” (Merkez ve odak özel ışınlarını karıştırma)
- **Öğrenci hataları:** Yansıyan ışını aynanın önünde odaktan geçirmek (uzantıyı çizmemek) `METHOD_SELECTION_ERROR`; Gelen ışının uzantısını aynanın arkasında çizmeyi unutmak `CARELESS_ERROR`
- **Kanıt:** program “Öğrenciler ışınların küresel aynalardan yansıdıkta…”; kitap s.328 Tablo 3.2; kitap s.332 8. Alıştırma; kitap s.341 Kontrol Noktası

### 133 · Asal ekseni kesen keyfî ışının ve iki ayna sisteminde ışının yansıması

- **Ölçülen:** FİZ.11.3.3 a `KB2.7.SB1`
- **Yapı:** Özel ışın olmayan, asal ekseni belirli bir noktada (3f, f/2, merkezin dışı, odak–tepe arası) kesen ışının yansımasının asal ekseni hangi bölgeden keseceği ya da asal ekseni çakışık iki aynadan oluşan sistemde ışının izlediği yol ve gereken mesafe sorulur.
- **Uyarıcı:** DIAGRAM, TEXT, TABLE · **Zorluk:** orta–zor
- **Çeldiriciler:** “Asal ekseni 3f'de kesen ışın aynadan yansıyınca yine 3f'de keser” (Kesim noktasının yansımada korunduğunu sanma); “Tümsek aynada asal ekseni kesen ışın yansıyınca aynanın önünde asal ekseni keser” (Tümsek aynada yansıyan ışının uzantı ile kesişeceğini bilmeme); “Işın kendi üzerinden dönmek için odaktan geçmelidir” (Merkez (dik gelme) ile odağı karıştırma)
- **Öğrenci hataları:** Keyfî ışına özel ışın kuralı uygulamak `METHOD_SELECTION_ERROR`; Birimleri f cinsinden ölçeklerken M ve F'yi karıştırmak `CARELESS_ERROR`
- **Kanıt:** program “Öğrenciler ışınların küresel aynalardan yansıdıkta…”; kitap s.327 Tablo 3.1 kural 4–5; kitap s.331 7. Alıştırma; kitap s.341 Kontrol Noktası
- **Kapsam notu:** Kural 4–5 kitapta sayısal örneklerle (3f→1,5f, f/2→f) verilir; sonuçlar ayna denklemini anmadan kural/ölçekli çizim ile bulunur.

### 134 · Yansıyan ışının yolundan ayna türü ve nokta konumlarının çıkarımı

- **Ölçülen:** FİZ.11.3.3 a `KB2.7.SB1`
- **Yapı:** Gelen ve yansıyan ışın (ya da ışın demeti) şekilde verilir; aynanın çukur mu tümsek mi olduğu, işaretli noktalardan hangisinin odak ya da merkez olduğu, noktalar arası uzaklıkların büyüklük ilişkisi ya da bir sistemde hangi parçanın hangi ayna türü olduğu sorulur.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Yansıyınca ışın dağılıyorsa ayna çukurdur” (Dağıtan/toplayan davranışı ayna türüyle ters eşleme); “Işın kendi üzerinden dönüyorsa çarptığı nokta odaktır” (Merkez (dik gelme) ile odağı karıştırma); “Aynanın türü yalnızca görüntünün büyük ya da küçük olmasından anlaşılır” (Tek bir görüntü özelliğiyle ayna türü belirleme)
- **Öğrenci hataları:** Tümsek aynada uzantı çizgilerinin kesişimini odak yerine merkez saymak `CONCEPTUAL_ERROR`; Noktalar arası uzaklıkları karşılaştırırken ölçeği tutarsız kullanmak `CARELESS_ERROR`
- **Kanıt:** program “Öğrenciler küresel aynaların yapılarına ve küresel…”; kitap s.331 7. Alıştırma; kitap s.329 6. Alıştırma; kitap s.340 12. Alıştırma; kitap s.330 6. Alıştırma

### 135 · Çukur ve tümsek aynaların benzer ve farklı özelliklerinin karşılaştırılması

- **Ölçülen:** FİZ.11.3.3 b `KB2.7.SB2`, FİZ.11.3.3 c `KB2.7.SB3`
- **Yapı:** Çukur ve tümsek aynaların yapı, odak noktası, ışınları toplama/dağıtma, görüntü türleri, görüş alanı ve kullanım alanı özellikleri bir sınıflandırma tablosu, ifade listesi ya da günlük hayat bağlamında karşılaştırılır; benzer özellik ve farklı özellik ayrıştırılır.
- **Uyarıcı:** TABLE, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Çukur ve tümsek aynaların ikisi de gerçek odak noktasına sahiptir” (Tümsek aynada odağın sanal olduğunu bilmeme); “Tümsek aynada yansıma yasası geçerli değildir” (Yansıma yasasının yalnız düz yüzeye özgü olduğunu sanma); “Çukur aynada oluşan görüntü her zaman büyük ve düzdür” (Cismin konumuna bağlılığı yok sayma)
- **Öğrenci hataları:** Farklı özelliği benzer özellik listesine yazmak (yansıma yasasını farklı saymak) `CONCEPTUAL_ERROR`; Tabloda çukur–tümsek sütunlarını yer değiştirmek `TABLE_READING_ERROR`
- **Kanıt:** program “Nitelik sıralama, anlam çözümleme veya sınıflandır…”; kitap s.326 3. Etkinlik 12. adım; kitap s.336 Değerlendirme 2; kitap s.332 8. Alıştırma

### 136 · Küresel aynanın odak uzaklığının bağlı olduğu ve olmadığı etmenler

- **Ölçülen:** FİZ.11.3.3 a `KB2.7.SB1`, FİZ.11.3.3 b `KB2.7.SB2`
- **Yapı:** Aynaya gönderilen ışının rengi, şiddeti, aynanın bulunduğu ortam ya da aynanın eğrilik yarıçapı değiştirilir; odak uzaklığının ve yansıma şeklinin değişip değişmediği, farklı odak uzaklıklı aynalara aynı noktadan ışın gönderilince yansımanın nasıl olacağı sorulur.
- **Uyarıcı:** TEXT, DIAGRAM, TABLE · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Mavi ışığın odak uzaklığı kırmızıdan farklıdır” (Aynada renge bağlı odak uzaklığı (mercekteki renk sapmasını aynaya taşıma)); “Su ortamında yansıma açısı değişir” (Yansıma ile kırılmayı karıştırma); “Işık şiddeti arttıkça odak noktası aynaya yaklaşır” (Işık şiddeti ile odak uzaklığını ilişkilendirme)
- **Öğrenci hataları:** Mercekteki odak uzaklığı etmenlerini (ortam, renk) aynaya taşımak `CONCEPTUAL_ERROR`; Verilen uzaklığı f cinsinden ifade etmeden çizime başlamak `METHOD_SELECTION_ERROR`
- **Kanıt:** program “Öğrenciler küresel aynaların yapılarına ve küresel…”; kitap s.326 Odak uzaklığının bağlılığı; kitap s.394 ÖD-7; kitap s.395 ÖD-9

## FİZ.11.3.4

### 137 · Küresel aynada cismin konumuna göre görüntünün yeri ve özellikleri (konum–özellik tablosu ve değişim yönü)

- **Ölçülen:** FİZ.11.3.4 b `FBAB7.SB2`
- **Yapı:** Cismin çukur ya da tümsek aynaya göre bölgesi (sonsuz, M dışı, M, M–F arası, F, F–T arası) verilir; görüntünün yeri, gerçek/sanal, düz/ters ve boyu sorulur. Cisim bir bölgeden diğerine hareket ederken görüntünün boyunun ve yerinin değişim yönü ya da çoklu ifade (D/Y, öncüllü) değerlendirilir.
- **Uyarıcı:** TEXT, TABLE, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Çukur aynada oluşan görüntü her zaman gerçektir” (Çukur aynada F–T arasında sanal görüntü oluştuğunu bilmeme); “Tümsek aynada görüntü, odak ile merkez arasında oluşur” (Tümsek aynada görüntünün aynanın arkasında (T–F arası) olduğunu bilmeme); “Çukur aynada odaktan aynaya yaklaşan cismin görüntü boyu artar” (Odak–tepe arasında görüntü boyunun cisme yaklaşarak azaldığını bilmeme); “Çukur aynadaki görüntü her zaman cisimden büyüktür” (Görüntü boyunu ayna türüyle özdeşleştirme, konumu yok sayma)
- **Öğrenci hataları:** Cismin M noktasında olduğu durumu M dışı sanmak ve görüntüyü küçük bulmak `TABLE_READING_ERROR`; Gerçek görüntüyü cisimle aynı tarafta (aynanın önünde değil arkasında) çizmek `CONCEPTUAL_ERROR`; 'Her zaman' ifadesindeki istisnayı (F, F–T arası) denetlememek `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “küresel aynalarda cismin yerine göre görüntünün ye…”; kitap s.337 Tablo 3.3 ve 3.4; kitap s.336 Değerlendirme 1; kitap s.336 Değerlendirme 3; kitap s.342 Çukur/tümsek özet tablosu
- **Kapsam notu:** Görüntü yeri ve özellikleri yalnız bölge tablosu ve özel ışın çiziminden bulunur; ayna denklemi kapsam dışıdır.

### 138 · Görüntü özelliklerinden ayna türü ve cismin bölgesinin çıkarımı

- **Ölçülen:** FİZ.11.3.4 b `FBAB7.SB2`
- **Yapı:** Görüntünün özellikleri ya da bir cihazın çalışma ilkesi (geniş görüş alanı, büyütme, odaklama, aynı boyda iletme) verilir; kullanılan ayna türü (düzlem, çukur, tümsek), cismin hangi bölgede olduğu ve görüntünün istenen biçime getirilmesi için yapılması gerekenler belirlenir.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT, TABLE · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Küçük sanal düz görüntü veren ayna çukur aynadır” (Tümsek aynanın görüntü özelliğini çukura atfetme); “Görüntü büyüdüğü için ayna tümsektir” (Büyütmeyi tümsek aynaya atfetme); “Görüntüyü küçültmek için çukur aynada cisim aynaya yaklaştırılır” (Cisim yaklaştıkça görüntü boyunun artacağını bilmeme)
- **Öğrenci hataları:** Ters görüntüyü sanal sanıp ayna türünü yanlış çıkarmak `CONCEPTUAL_ERROR`; Birden çok özelliği birlikte değerlendirmeden tek özellikle karar vermek `METHOD_SELECTION_ERROR`
- **Kanıt:** program “küresel aynalarda cismin yerine göre görüntünün ye…”; kitap s.338 9. Alıştırma Örnek; kitap s.340 12. Alıştırma; kitap s.333 3.3.2 giriş

### 139 · Birimkareli zeminde özel ışınlarla görüntü çizimi, uzaklık ve boy karşılaştırması (tek ve çift aynalı sistem)

- **Ölçülen:** FİZ.11.3.4 b `FBAB7.SB2`
- **Yapı:** Asal ekseni çakışık, f ya da r değerleri birimkare ya da metre cinsinden verilen aynaların önüne konan cismin görüntüsü iki özel ışınla çizilir; görüntünün yeri, boyu ve iki görüntü arasındaki uzaklık ya da boyların oranı bulunur; iki aynalı sistemde ilk görüntüler karşılaştırılır.
- **Uyarıcı:** DIAGRAM, TABLE, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Görüntü yeri çizimle değil, cismin ayna uzaklığıyla aynı bulunur” (Görüntü uzaklığını cisim uzaklığına eşit alma (düzlem ayna kuralının taşınması)); “Görüntü boyu cisim boyu ile aynıdır, yalnız ters döner” (Büyütmeyi her konumda 1 sanma); “İki aynadaki görüntüler arasındaki uzaklık cisimden aynalara olan uzaklıkların toplamıdır” (Görüntü konumları yerine cisim konumlarını kullanma)
- **Öğrenci hataları:** Odak ve merkezi yanlış birim sayısıyla işaretleyip çizime başlamak `CARELESS_ERROR`; Boy oranını uzaklık oranının tersi almak `FORMULA_APPLICATION_ERROR`; Sanal görüntünün konumunu aynanın önünde göstermek `CONCEPTUAL_ERROR`
- **Kanıt:** program “Öğrenciler deney düzeneklerindeki cisim ve görüntü…”; kitap s.338 9. Alıştırma; kitap s.395 ÖD-8; kitap s.340 12. Alıştırma; kitap s.339 10. Alıştırma
- **Kapsam notu:** Sayısal sonuçlar birimkareli ölçekli çizimle (ışın kesişimi) bulunur; ayna denklemi kullanılmaz. Kitap s.339 Mirascope metni görüntüyü 'sanal' diye adlandırır; fiziksel olarak alt aynanın odağındaki cisimden çıkan paralel demet üst çukur aynanın odağında GERÇEK görüntü verir (emin olunmayan nokta: kitap ifadesi sorunludur).

### 140 · Küresel aynada görüntü oluşumu deneyi tasarımı: değişkenler, düzenek ve hata ayıklama

- **Ölçülen:** FİZ.11.3.4 a `FBAB7.SB1`
- **Yapı:** Araştırma sorusu (cismin yerine göre görüntünün yeri ve özellikleri) ve araç gereç (çukur ayna, tümsek ayna, mum, ekran, cetvel) verilir; bağımsız, bağımlı ve kontrol edilen değişkenlerin belirlenmesi, gerçek ve sanal görüntünün ekranla ayırt edilmesi, ölçüm yöntemi ya da hatalı kurulmuş düzenekteki sorunun bulunması istenir.
- **Uyarıcı:** TEXT, DIAGRAM, EXPERIMENT · **Zorluk:** orta
- **Çeldiriciler:** “Cisim konumu ve ayna türü aynı anda değiştirilerek veri toplanmalıdır” (Tek seferde birden fazla bağımsız değişkeni değiştirme (kontrol hatası)); “Görüntünün sanal olduğu ekranda net görüntü alınarak anlaşılır” (Gerçek–sanal ayrımında ekranın rolünü ters kurma); “Ayna ne kadar büyükse görüntünün yeri o kadar değişir” (Ayna boyutunun odak uzaklığını belirlediğini sanma)
- **Öğrenci hataları:** Kontrol değişkeni (aynanın f'si, cisim boyu) olarak ölçülen niceliği listelemek `METHOD_SELECTION_ERROR`; Aracı ya da ölçme yöntemini ölçülecek niceliğe uygun seçmemek (ör. ekransız ölçüm) `METHOD_SELECTION_ERROR`; Araştırma sorusunu bağımsız ve bağımlı değişkenlerle eşlemeden yazmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “görüntünün yeri ve özelliklerini belirleyebilecekl…”; kitap s.333 4. Etkinlik 2. adım; kitap s.334 4. Etkinlik 3. adım; kılavuz s.114

### 141 · Küresel ayna deney verisinin analizi: tablo, simülasyon ölçümü ve tutarsız ölçüm

- **Ölçülen:** FİZ.11.3.4 b `FBAB7.SB2`
- **Yapı:** Cismin aynaya uzaklığı, görüntünün aynaya uzaklığı, cisim ve görüntü boyu ve görüntü özelliklerini içeren ölçüm tablosu (ya da simülasyon verisi) verilir; verilerden aynanın türü, odak uzaklığı, hangi satırın tutarsız olduğu, boy–uzaklık orantısı ve gerçek/sanal sonucu çıkarılır.
- **Uyarıcı:** TABLE, DATA_SET, EXPERIMENT, GRAPH · **Zorluk:** orta–zor
- **Çeldiriciler:** “Cisim uzaklığı iki katına çıkınca görüntü uzaklığı da iki katına çıkar” (Uzaklıkları doğru orantılı sanma); “d_g > d_c olan satırda görüntü cisimden küçüktür” (Boy oranını uzaklık oranının tersi alma); “Ölçümde görüntü ekranda alınamıyorsa ölçüm hatalıdır” (Sanal görüntünün ekranda alınamayacağını bilmeme)
- **Öğrenci hataları:** Uzaklıkları ayna merkezinden değil tepe noktasından ölçülmüş saymak `QUESTION_INTERPRETATION_ERROR`; Tabloda cisim ve görüntü sütunlarını karıştırmak `TABLE_READING_ERROR`; cm ve m birimlerini karıştırmak `UNIT_ERROR`
- **Kanıt:** program “küresel aynalarda cismin yerine göre görüntünün ye…”; kitap s.335 4. Etkinlik 17–18. adımlar; kitap s.337 Boy–uzaklık oranı; kılavuz s.114

## FİZ.11.3.5

### 142 · Ortam değiştiren ışının yolundan ortamların kırıcılık indislerinin sıralanması

- **Ölçülen:** FİZ.11.3.5 b `FBAB7.SB2`
- **Yapı:** Tek renkli ışının K, L, M, N, P gibi saydam ortamlar arasında izlediği yol (normale yaklaşma, normalden uzaklaşma, eğik gelmesine rağmen sapmama, tam yansıma ya da dik gelip sapmama) şekille verilir; her geçişten ortamların kırıcılık indisleri arasındaki büyüklük ilişkisi çıkarılır ve gerekirse indis tablosundaki maddelerle eşleştirilir.
- **Uyarıcı:** DIAGRAM, TABLE, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Işın kırılmadan düz geçtiyse iki ortamın indisi eşittir” (Dik gelen ışının sapmamasını indis eşitliğiyle karıştırma); “Işın normale yaklaştığı ortamın kırıcılık indisi daha küçüktür” (Normale yaklaşma/uzaklaşma yönünü indis büyüklüğüyle ters eşleştirme); “Işın geçemeyip tam yansıma yaptığı için o iki ortamın indisleri eşittir” (Tam yansımanın çok kırıcıdan az kırıcıya geçişte olduğunu bilmeme); “Açısı büyük olan ışının bulunduğu ortam daha çok kırıcıdır” (Açıyı yüzeyle ölçme ve normalle ölçme karışıklığı)
- **Öğrenci hataları:** Açıları normal yerine ayırıcı yüzeyle ölçmek `QUESTION_INTERPRETATION_ERROR`; Zincirleme karşılaştırmada ortamların sırasını yanlış birleştirmek (n_P > n_N > n_M = n_L > n_K gibi) `METHOD_SELECTION_ERROR`; Normale yaklaşma/uzaklaşmayı indisle eşleştirirken yönü ters almak `CONCEPTUAL_ERROR`
- **Kanıt:** program “ortamın ışığı kırma indisini tanımlayabilir…”; kitap s.348 Örnek (K, L, M, N, P); kitap s.353 Özet şeması (dik gelen ışın); kitap s.397 ÖD-13; kitap s.402 ÖD-22 Defne, Bilgesu

### 143 · Snell yasası ve n·ϑ = c ile açı, kırıcılık indisi ve ışık sürati hesapları

- **Ölçülen:** FİZ.11.3.5 b `FBAB7.SB2`
- **Yapı:** Işık iki saydam ortam arasında kırılırken açılardan biri, indislerden biri ya da ışığın bir ortamdaki sürati bilinmez; sinüs değerleri verilerek (ör. sin37° = 0,6; sin53° = 0,8) diğer nicelik Snell yasasıyla ya da n = c/ϑ ile bulunur; frekansın ortam değişince sabit kaldığı kullanılır.
- **Uyarıcı:** DIAGRAM, TABLE, TEXT, DATA_SET · **Zorluk:** kolay–orta
- **Çeldiriciler:** “n₁/n₂ oranı î/r̂ oranına eşittir” (Açıların kendisiyle sinüslerini karıştırma); “İndis oranı sinüs oranıyla doğru orantılıdır (n₁/n₂ = sin î / sin r̂)” (Snell yasasındaki ters orantıyı bilmeme); “Kırıcılık indisi büyük ortamda ışığın sürati daha büyüktür” (Kırma indisi–sürat ilişkisini ters kurma); “Işık ortam değiştirince frekansı da değişir” (Kırılmada frekansın sabit kaldığını bilmeme)
- **Öğrenci hataları:** sin yerine açının kendisini oranlamak `FORMULA_APPLICATION_ERROR`; Açıları yüzey normali yerine ayırıcı yüzeyle ölçmek `QUESTION_INTERPRETATION_ERROR`; n₁ sin î = n₂ sin r̂ içinde indisleri yer değiştirmek `ALGEBRA_ERROR`
- **Kanıt:** kitap s.346 Snell Yasası; kitap s.347 Frekans sabit; kitap s.402 ÖD-22 Derin; kitap s.345 5. Etkinlik 8. adım tablo

### 144 · Sınır açısı ve tam yansıma: koşullar, sınır açısı bulma ve sudaki ışık kaynağının aydınlık dairesi

- **Ölçülen:** FİZ.11.3.5 b `FBAB7.SB2`
- **Yapı:** Işın çok kırıcı ortamdan az kırıcı ortama farklı gelme açılarıyla (sınır açısından küçük, eşit, büyük) gönderilir; ışının kırılıp kırılmadığı, ayırıcı yüzeyi sıyırıp sıyırmadığı ya da tam yansıma yapıp yapmadığı karar verilir; indislerden sınır açısı (ya da tersi) bulunur ve su altındaki noktasal kaynağın yüzeyde oluşturduğu aydınlık dairenin yarıçapı yorumlanır.
- **Uyarıcı:** DIAGRAM, TABLE, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Işığın geldiği ortam hangisi olursa olsun yeterince büyük açıyla gelirse tam yansıma yapar” (Tam yansımanın her geçişte olabileceğini sanma); “Gelme açısı sınır açısına eşitken ışın tam yansıma yapar” (Sınır açısındaki sıyırma durumu ile tam yansımayı karıştırma); “İndis farkı arttıkça sınır açısı büyür” (Sınır açısı–indis farkı ilişkisini ters kurma); “Kaynak derine inince su yüzeyinde ışığın çıktığı daire küçülür” (Aydınlık dairenin r = h·tanθs ile büyüdüğünü kavrayamama)
- **Öğrenci hataları:** Sınır açısını yüzeyle yapılan açı olarak almak `QUESTION_INTERPRETATION_ERROR`; sinθs = n₁/n₂ (ters) yazmak `FORMULA_APPLICATION_ERROR`; Aydınlık dairenin yarıçapını kaynağın derinliğinden bağımsız saymak `CONCEPTUAL_ERROR`
- **Kanıt:** program “sınır açısı ve tam yansıma olaylarını açıklar…”; kitap s.347 Şekil 3.21 yollar; kitap s.350 16. Alıştırma; kitap s.366 22. Alıştırma tablo; kitap s.344 5. Etkinlik 3. ç ve d adımları
- **Kapsam notu:** Sınır açısı formülü (critical-angle) kitapta tanım olarak verilir, formül kutusu yoktur (Snell'den r̂ = 90° konarak türetilir); program sınır belirtmediği için hesaplı kullanım serbesttir.

### 145 · Cam küre ve yarım kürede ışının yolu: yüzey normali yarıçap yönündedir

- **Ölçülen:** FİZ.11.3.5 b `FBAB7.SB2`
- **Yapı:** Merkezi O olan cam küre ya da yarım küreye hava ortamından çeşitli doğrultularda tek renkli ışın gönderilir; küre yüzeyindeki normalin merkezden o noktaya çizilen yarıçap olduğu kullanılarak ışının giriş, çıkış ve tam yansıma yolları (düz yüzeyde sınır açısı verilerek) çizilir ya da doğru çizilmiş olanlar seçilir.
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Küre yüzeyindeki normal, ışının geldiği doğrultuya paralel bir doğrudur” (Küresel yüzeyde normali merkez-yarıçap doğrultusu olarak belirleyememe); “Merkeze yönelen ışın küreye girerken normale yaklaşacak şekilde kırılır” (Normal üzerinden gelen ışının sapmayacağını bilmeme); “Camdan havaya geçen ışın her zaman çıkış yapar, tam yansıma yalnız sudan havaya olur” (Sınır açısı kıyasını yalnız su–hava ile sınırlama); “Işın yarım kürenin düz yüzeyine geldiğinde gelme açısı yarıçapa göre ölçülür” (Düz yüzeyde normali yarıçapla karıştırma)
- **Öğrenci hataları:** Küresel yüzeyde normali yüzeye teğet çizmek `CONCEPTUAL_ERROR`; Camdan havaya geçişte ışını normale yaklaştırmak `CONCEPTUAL_ERROR`; Gelme açısını 42° ile karşılaştırmadan kırıldığını varsaymak `METHOD_SELECTION_ERROR`
- **Kanıt:** program “kırılma olayı ve Snell Yasası ile sınır açısı ve t…”; kitap s.348 Şekil 3.24 küresel yüzeyler; kitap s.349 14. Alıştırma; kitap s.402 ÖD-22 Atlas

### 146 · Paralel yüzeyli levha ve katmanlı ortamlarda açı ilişkileri: giriş–çıkış eşitliği ve ara katmanın etkisizliği

- **Ölçülen:** FİZ.11.3.5 b `FBAB7.SB2`
- **Yapı:** Hava–cam–hava ya da hava–yağ–su gibi paralel ayırıcı yüzeyli ortamlardan geçen ışının a, b, c, ç açıları (ya da son ortamdaki kırılma açısı) karşılaştırılır; levhanın indisi ya da ara katman değişince hangi açıların ve yanal kaymanın değiştiği sorulur.
- **Uyarıcı:** DIAGRAM, TABLE, TEXT, EXPERIMENT · **Zorluk:** orta
- **Çeldiriciler:** “Camdan çıkan ışının açısı ilk gelme açısından farklıdır, çünkü cam ışını kalıcı olarak saptırır” (Paralel levhadan çıkan ışının gelen ışına paralel olduğunu bilmeme); “Yağ katmanı bulunduğunda suya giren ışının kırılma açısı yağsız duruma göre farklıdır” (Ardışık geçişte yalnız ilk ve son ortamın belirleyici olduğunu bilmeme); “Camın indisi artınca a ve ç açıları da büyür” (Gelme açısının değişmediğini, kırılma açılarının küçüldüğünü bilmeme); “Camın indisi artınca ışının yanal kayması (x) azalır” (İndis arttıkça sapmanın arttığını bilmeme)
- **Öğrenci hataları:** c açısını a açısına eşitlemek (b = c yerine) `CONCEPTUAL_ERROR`; İki ardışık Snell denklemini birleştirmeden her katmanı bağımsız hesaplamak `METHOD_SELECTION_ERROR`
- **Kanıt:** program “Farklı saydam ortamlar için gelme açısı ve kırılma…”; kitap s.350 15. Alıştırma; kitap s.352 18. Alıştırma

### 147 · Serap, günbatımı, yıldız konumu gibi doğa olaylarında kırılma ve tam yansımanın açıklanması

- **Ölçülen:** FİZ.11.3.5 b `FBAB7.SB2`
- **Yapı:** Sıcaklığa bağlı olarak kademeli değişen indisli hava katmanlarında ya da atmosferden geçen ışığın yolu verilir; sıcak asfaltta serap, ufuk çizgisinin altındaki Güneş'in görülmesi, yıldızların gerçek konumlarından farklı görünmesi ve soğuk günde yelkenlinin havada görünmesi kırılma ve tam yansımayla açıklanır.
- **Uyarıcı:** DAILY_LIFE_CONTEXT, DIAGRAM, TEXT, EXPERIMENT · **Zorluk:** orta
- **Çeldiriciler:** “Serap, ışığın sıcak yer yüzeyinde yansıyıp dağılmasıyla oluşur; kırılmayla ilgisi yoktur” (Serabı yalnız yansıma sanma; hava katmanlarında kırılma ve tam yansımayı görememe); “Hava ısındıkça kırıcılık indisi artar, o yüzden yer yüzeyindeki hava çok kırıcıdır” (Sıcaklık–kırıcılık indisi ilişkisini ters kurma); “Yıldızlar gerçek konumlarında görülür çünkü atmosfer ışığın yolunu değiştirmez” (Atmosferin ışığı kırdığını kavrayamama); “Güneş ufkun altında ise ışınları bize ulaşamaz, görünen görüntü yansımadır” (Atmosferdeki kademeli kırılmayı yansımayla karıştırma)
- **Öğrenci hataları:** Işının yolunu çizerken katmanlar arasındaki geçişte normale göre yönü yanlış belirlemek `CONCEPTUAL_ERROR`; Gözün cismi gelen ışının son doğrultusunda gördüğünü gözden kaçırıp gerçek konumunu görünür konum saymak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “Serap olayı ve su dolu bardağın içindeki kaşığın k…”; kitap s.347 Serap olayı; kitap s.349 14. Alıştırma a; kitap s.359 20. Alıştırma; kitap s.343 5. Etkinlik 1. adım

### 148 · Kırılma deneyi tasarımı: araştırma sorusu, değişkenler, düzenek, tek renkli ışık ve güvenlik

- **Ölçülen:** FİZ.11.3.5 a `FBAB7.SB1`
- **Yapı:** Optik daire, yarım daire kesitli cam ve lazer kaynağı ile farklı saydam ortamlarda (su, tuzlu su) tek renkli ışığın kırılmasını inceleyen bir araştırma kurgulanır; araştırma sorusunda bağımsız, bağımlı ve kontrol değişkenleri, uygun araç gereç, ışının yarım daire camın merkezine gönderilmesinin gerekçesi, tek renkli ışık seçimi ve güvenlik önlemleri sorulur ya da hatalı bir düzenek eleştirilir.
- **Uyarıcı:** TEXT, DIAGRAM, EXPERIMENT, TABLE · **Zorluk:** orta
- **Çeldiriciler:** “Işının ortam ve gelme açısı birlikte değiştirilerek daha çok veri elde edilir” (Tek seferde yalnız bir değişkeni değiştirme ilkesini bilmeme); “Beyaz ışık kullanmak ölçümü kolaylaştırır çünkü her renk aynı açıyla kırılır” (Renklerin farklı kırıldığını ve tek renkli ışığın gerekçesini bilmeme); “Işın yarım daire camın eğrisel yüzeyine merkezden uzak bir noktaya dik olmayacak biçimde gönderilmelidir” (Merkeze gönderilen ışının eğrisel yüzeyden sapmadan çıktığını bilmeme); “Kırılma açısı bağımsız, ortamın indisi bağımlı değişkendir” (Bağımsız ve bağımlı değişkeni ters eşleme)
- **Öğrenci hataları:** Ölçülen niceliği (kırılma açısı) kontrol değişkeni olarak listelemek `METHOD_SELECTION_ERROR`; Lazer ışığının göze zarar verebileceğini güvenlik önlemlerine yazmamak `QUESTION_INTERPRETATION_ERROR`; Araştırma sorusunu bağımsız ve bağımlı değişkenle eşlemeden genel bir cümleyle yazmak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “Işığın saydam ortamlardaki davranışı ile ilgili de…”; program “Oluşturulan deney düzeneğinde saydam ortamın özell…”; kitap s.345 5. Etkinlik 5. adım; kitap s.344 5. Etkinlik 3. adım; kılavuz s.114

### 149 · Kırılma deneyi verisinin analizi: gelme–kırılma açısı tablosu, sinüs oranı ve değişkenlerin etkisi

- **Ölçülen:** FİZ.11.3.5 b `FBAB7.SB2`
- **Yapı:** Farklı saydam ortamlar için ölçülmüş gelme açısı–kırılma açısı tabloları (ya da sin î–sin r̂ grafiği) verilir; sin î / sin r̂ oranının ortam için sabit çıkması, hangi ortamın daha kırıcı olduğu, tutarsız bir ölçüm, kırılma açısının hangi değişkenlere bağlı olduğu (ortam, gelme açısı, sıcaklık) ve açıların normalle ölçüldüğü analiz edilir.
- **Uyarıcı:** TABLE, DATA_SET, GRAPH, EXPERIMENT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Gelme açısı iki katına çıkınca kırılma açısı da iki katına çıkar” (Kırılma açısını gelme açısıyla doğru orantılı sanma); “Ortamın kırıcılık indisi gelme açısı büyüdükçe artar” (İndisin ortama ait olup açıdan bağımsız olduğunu bilmeme); “î/r̂ oranı her ölçümde sabit çıkar” (Açıların oranı ile sinüslerin oranını karıştırma); “Kırılma açısı yalnız gelme açısına bağlıdır, ortamın cinsi etkili değildir” (Kırılma açısının ortamın indisine de bağlı olduğunu bilmeme)
- **Öğrenci hataları:** sin î / sin r̂ yerine î / r̂ oranının sabitliğine bakmak `TABLE_READING_ERROR`; Grafikte eksenlere bakmadan eğimi doğrudan indis sanmak `GRAPH_READING_ERROR`; Açıları yüzeyle ölçülmüş olarak okumak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “Kırılma açısının bağlı olduğu değişkenler tablodak…”; program “Işığın saydam ortamlardaki davranışı ile ilgili ta…”; kitap s.345 5. Etkinlik 8. adım tablo; kitap s.345 5. Etkinlik 12. adım

### 150 · Kırılmada beyaz ışığın renklerine ayrılması ve renge göre kırılma ile sınır açısı farkı · **zenginleştirme**

- **Ölçülen:** FİZ.11.3.5 b `FBAB7.SB2`
- **Yapı:** Beyaz ya da farklı renkli ışınlar çok kırıcı bir ortama (ya da ortamdan) geçerken mor ışığın kırmızıya göre daha çok kırıldığı, kırmızı için sınır açısının en büyük, mor için en küçük olduğu kullanılarak her rengin tam yansıma yapıp yapmadığı ya da kırılma açısı değişimi sorulur.
- **Uyarıcı:** DIAGRAM, TEXT · **Zorluk:** orta
- **Çeldiriciler:** “Kırmızı ışık mor ışıktan daha çok kırılır” (Renk–kırılma sıralamasını ters kurma); “Her renk için sınır açısı aynıdır” (Sınır açısının renge bağlı olduğunu bilmeme); “Kırmızı ışığın sınır açısı en küçüktür, bu yüzden ilk tam yansıyan renk kırmızıdır” (Sınır açısı–renk sıralamasını ters kurma)
- **Öğrenci hataları:** Renk sıralamasını (kırmızı → mor) kırılma miktarıyla ters eşleştirmek `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.347 Şekil 3.22–3.23; kitap s.345 5. Etkinlik 10. adım; kitap s.351 17. Alıştırma b
- **Kapsam notu:** Program–kitap farkı: FİZ.11.3.5 öğretme uygulaması yalnız 'tek renkli ışık'tan söz eder; kitap beyaz ışığın renklerine ayrılmasını anlatım (s.347), etkinlik (5. Etkinlik 10. adım) ve alıştırmada (17. Alıştırma b) işler. Çekirdek aile olarak tek renkli ışıkla çalışılır; renge göre ayrışma zenginleştirme olarak ayrıştırılmıştır.

## FİZ.11.3.6

### 151 · Görünür derinliği etkileyen değişkenlerin ve görünür derinliğin tanımlanması

- **Ölçülen:** FİZ.11.3.6 a `FBAB1.SB1`
- **Yapı:** Havuz, akvaryum ya da bardak gibi bir düzenekte gözlemcinin ve cismin bulunduğu ortamlar, cismin ayırıcı yüzeye uzaklığı (gerçek derinlik) ve gözlemcinin gördüğü uzaklık (görünür derinlik) tanıtılır; hangi niceliğin bağımsız değişken olduğu, tanımların doğru eşleştirilmesi ve görünür derinliği etkileyen/etkilemeyen etmenlerin ayrımı sorulur.
- **Uyarıcı:** TEXT, TABLE, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Gözlemci yüzeyden uzaklaştıkça görünür derinlik de değişir” (Görünür derinliğin gözlemcinin ayırıcı yüzeye uzaklığına bağlı olmadığını bilmeme); “Görünür derinlik cismin gerçek derinliğidir, yalnız gözümüzün bir algısı değildir” (Görünür ve gerçek derinliği özdeş sayma); “Görünür derinliği yalnız cismin bulunduğu ortamın kırıcılık indisi belirler” (İki ortamın indis farkının etkili olduğunu bilmeme); “Cismin boyutu büyüdükçe görünür derinliği de büyür” (İlişkisiz bir niceliği değişken sanma)
- **Öğrenci hataları:** Gözlemcinin ortamını ve cismin ortamını karıştırmak `QUESTION_INTERPRETATION_ERROR`; Gerçek derinliği ölçülen, görünür derinliği verilen nicelik olarak ters eşlemek `CONCEPTUAL_ERROR`
- **Kanıt:** program “Öğrenciler görünür derinliği etkileyen ortamların …”; kitap s.355 6. Etkinlik 4. adım; kitap s.357 Görünür derinlik tanımı; kitap s.357 Bağlı olduğu etmenler
- **Kapsam notu:** CALC_EXCLUDED: yalnız nitel tanım ve ilişki; matematiksel model yok.

### 152 · Görünür derinlik deneyinde gözlemin kaydedilmesi: artar / azalır / değişmez tablosu

- **Ölçülen:** FİZ.11.3.6 b `FBAB1.SB2`
- **Yapı:** Porselen bardağın dibindeki bozuk para (ya da kalem) üzerine su, sıvı yağ ya da cam konarak yapılan gözlemler anlatılır; gerçek derinlik, görünür derinlik ve sıvı miktarı arttığında görünür derinlikteki değişim için gözlem tablosunun satırları 'artar / azalır / değişmez' ile doldurulur.
- **Uyarıcı:** TABLE, EXPERIMENT, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Boş bardakta bile para gerçek derinliğinden farklı bir derinlikte görünür” (Aynı ortamda gözlemci ve cismin görünür derinliğin gerçeğe eşit olduğunu bilmeme); “Bardağa su eklendikçe görünür derinlik azalır” (Gerçek derinlik arttıkça görünür derinliğin de arttığını kavrayamama); “Aynı yükseklikteki su ve sıvı yağda para aynı derinlikte görünür” (İndis farkının görünür derinliği etkilediğini bilmeme); “Su eklenince para gerçekten yukarı kalkmıştır” (Görünür derinlik olayını cismin gerçek yer değiştirmesi sanma)
- **Öğrenci hataları:** Tablodaki 'gerçek derinlik' ile 'görünür derinlik' satırlarını birbirine karıştırmak `TABLE_READING_ERROR`; Gözlemi değil beklentiyi yazmak (tahmini gözlem sonucu sanmak) `CONCEPTUAL_ERROR`; Sıvı yağ ve su sütunlarını yer değiştirerek doldurmak `CARELESS_ERROR`
- **Kanıt:** program “Öğrenciler bu düzeneklerdeki cismin bulunduğu gerç…”; kitap s.356 6. Etkinlik 14. adım tablo; kitap s.355 6. Etkinlik 6–13. adımlar; kitap s.355 6. Etkinlik 3. adım tahminler
- **Kapsam notu:** CALC_EXCLUDED: yalnız nitel gözlem tablosu; nicel ölçüm ya da bağıntı yok.

### 153 · Gözlemcinin ve cismin ortamına göre cismin yakın/uzak görünmesinin ışın çizimiyle açıklanması

- **Ölçülen:** FİZ.11.3.6 c `FBAB1.SB3`
- **Yapı:** Işığın bir cisimden gözlemciye geçerken ortam değiştirdiği bir durumda (havadan suya bakış, sudan havadaki cisme bakış, cam küre içindeki cisme farklı yönlerden bakış, atmosfer) cismin gerçek konumuna göre yakın mı uzak mı görüleceği, ışının normalden uzaklaşması/yaklaşması ve gözün ışının geri uzantısında görmesiyle gerekçelendirilir.
- **Uyarıcı:** DIAGRAM, DAILY_LIFE_CONTEXT, TEXT · **Zorluk:** orta
- **Çeldiriciler:** “Havadan suya bakan kişi balığı gerçek konumundan daha derinde görür” (Işığın sudan havaya çıkarken normalden uzaklaştığını görememe); “Sudan havadaki kuşa bakan balık kuşu yüzeye daha yakın görür” (Çok kırıcı ortamdan az kırıcı ortama bakışta yönü ters kurma); “Cismi her zaman gerçek konumunda görürüz, çünkü ışık doğrusal yayılır” (Gözün ışığı kırılmış doğrultusunda algıladığını bilmeme); “Cam kürenin merkezindeki cisim yandan bakıldığında da yüzeye daha yakın görünür” (Yüzeye dik gelen ışının sapmayacağını bilmeme)
- **Öğrenci hataları:** Gözün cismi kırılan ışının geri uzantısında gördüğünü çizimde uygulamamak (gerçek ışını izleyip kesişim aramak) `METHOD_SELECTION_ERROR`; Işının geçişte normale göre yönünü yanlış çizmek `CONCEPTUAL_ERROR`; Gözlemcinin bakış doğrultusunu normale yakın almamak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “Yapılan gözlemler üzerinden öğrenciler ortamların …”; kitap s.357 Şekil 3.25–3.26; kitap s.359 19. Alıştırma; kitap s.398 ÖD-15; kitap s.358 Örnek cam küre; kitap s.359 20. Alıştırma
- **Kapsam notu:** CALC_EXCLUDED: h' = h·n₂/n₁ gibi bir bağıntı kullanılmaz; yalnız yönü (yakın/uzak) belirleyen ışın çizimi ve gerekçe. Cam küre ve atmosfer örnekleri kitabın uygulamasıdır; programda düz ayırıcı yüzey esastır.

### 154 · Görünür derinliğin indis farkına ve gerçek derinliğe bağlılığının gözleme dayanarak açıklanması

- **Ölçülen:** FİZ.11.3.6 c `FBAB1.SB3`
- **Yapı:** Farklı kırıcılık indisli sıvılardaki (ya da aynı sıvının farklı derinliklerindeki) özdeş cisimlerin aynı noktadan bakıldığında görünür derinlikleri karşılaştırılır; görünür derinliğin ortamların indis farkına ve gerçek derinliğe nasıl bağlı olduğu sonucu çıkarılır ya da gözlemden ortamlar sıralanır.
- **Uyarıcı:** TEXT, TABLE, DIAGRAM, DAILY_LIFE_CONTEXT, EXPERIMENT · **Zorluk:** orta
- **Çeldiriciler:** “Sıvının kırıcılık indisi arttıkça cisim daha derinde görünür” (İndis–görünür derinlik ilişkisini ters kurma); “Cismin gerçek derinliği arttıkça görünür derinliği azalır” (Görünür derinliğin gerçek derinlikle birlikte arttığını bilmeme); “İki sıvıda görünür derinlik farkı yalnız gözlemcinin bakış uzaklığından kaynaklanır” (Gözlemci uzaklığını etkili sanma); “En derin görünen cisim en kırıcı ortamdadır, aynı derinliklerde bile” (Aynı gerçek derinlikte karşılaştırma gerektiğini gözden kaçırma)
- **Öğrenci hataları:** İki değişkeni aynı anda değiştirip sonucu tek bir değişkene bağlamak `METHOD_SELECTION_ERROR`; İndis farkı arttıkça görünür derinlik ile gerçek derinlik arasındaki farkın azaldığını söylemek `CONCEPTUAL_ERROR`; Görünür derinliği gerçek derinlik sanarak sıralamak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “Işığı kırma indisleri farklı olan ortamlardaki cis…”; kitap s.397 ÖD-11; kitap s.356 6. Etkinlik değerlendirme 3–4; kitap s.360 Kontrol Noktası
- **Kapsam notu:** CALC_EXCLUDED: nicel bağıntı yok. ÖD-11'deki 'balığı daha büyük/küçük görür' ifadeleri program kapsamı dışı bırakıldı: düzlem ayırıcı yüzeyde yanal büyütme 1'dir; ifadeler açık uçlu ölçmede nitel gerekçeyle değerlendirilir, aile yalnız derinlik ilişkisini kapsar.

## FİZ.11.3.7

### 155 · Fiber optik araştırması için uygun ve güvenilir kaynakların belirlenmesi

- **Ölçülen:** FİZ.11.3.7 a `KB2.6.SB1`
- **Yapı:** Fiber optik kablonun yapısı, çalışma prensibi ya da kullanım alanı ile ilgili bir araştırma sorusu ve aday kaynakların (kütüphane kitabı/dergi, üniversite ya da standart kuruluşu sayfası, uzman kişi/kurum, reklam sayfası, sosyal medya paylaşımı) özellikleri verilir; araştırma sorusuna ve güvenilirlik ölçütlerine uygun kaynak ya da kaynaklar belirlenir.
- **Uyarıcı:** TEXT, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Sosyal medyada çok beğenilen paylaşım güvenilir bir kaynaktır” (Popülerliği güvenilirlik ölçütü sayma); “Arama motorunda ilk sırada çıkan sayfa en doğru bilgiyi verir” (Arama sırasını doğruluk ölçütü sayma); “Bir ürünün satış sayfası çalışma prensibini en nesnel biçimde anlatır” (Kaynağın amacını (ticari) gözden kaçırma); “Her konu için tek bir güvenilir kaynak yeterlidir” (Kaynak çeşitliliği ve karşılaştırma gereğini bilmeme)
- **Öğrenci hataları:** Araştırma sorusunun kapsamına (yapı/ilke/kullanım) uygun olmayan kaynak türünü seçmek `METHOD_SELECTION_ERROR`; Kaynağın yazarı, tarihi ve amacı gibi ölçütleri okumadan seçmek `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “Öğrenciler uygun düşünme ve öğrenme stratejisi seç…”; kitap s.361 7. Etkinlik 2. adım; kitap s.361 7. Etkinlik 2. adım; kılavuz s.19
- **Kapsam notu:** Bu bölümdeki aileler bilgi toplama becerisini (KB2.6) ölçer; fiziksel bilgi düzeyi kitabın s.363–366 içeriğiyle sınırlıdır.

### 156 · Fiber optik kablonun yapısı, görevleri, tek/çok modlu ayrımı ve bilgi iletim zinciri

- **Ölçülen:** FİZ.11.3.7 b `KB2.6.SB2`
- **Yapı:** Toplanan bilgiler arasından fiber optik kablonun kısımları (çekirdek, cam örtü, kılıf), her kısmın görevi ve indis ilişkisi, tek modlu–çok modlu fiberin özellikleri ve bilginin vericiden alıcıya (elektrik → ışık → fiber → foto dedektör → elektrik) iletim sırası doğru eşleştirilir ya da sıralanır.
- **Uyarıcı:** DIAGRAM, TABLE, TEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Cam örtünün kırıcılık indisi çekirdekten büyüktür” (Tam yansıma için çekirdeğin daha kırıcı olması gerektiğini bilmeme); “Kılıf, ışığın çekirdekte kalmasını sağlayan kısımdır” (Cam örtü ile kılıfın görevini karıştırma); “Kısa mesafeli binalar arası ağlarda tek modlu fiber tercih edilir” (Tek modlu ve çok modlu fiberin özelliklerini karıştırma); “Fiber optik kabloda bilgi elektrik akımı olarak çekirdek içinde iletilir” (Fiber optikte ışık sinyalinin taşıyıcı olduğunu bilmeme)
- **Öğrenci hataları:** Cam örtü ile kılıfı tek parça saymak `CONCEPTUAL_ERROR`; İletim zincirinde dönüştürme sırasını (elektrik → ışık → elektrik) karıştırmak `METHOD_SELECTION_ERROR`
- **Kanıt:** program “Öğrenciler fiber optik malzemelerin yapısı, çalışm…”; kitap s.363 Şekil 3.27; kitap s.364 Şekil 3.29–3.30; kitap s.364 Bilgi iletimi; kitap s.366 22. Alıştırma Kontrol Noktası
- **Kapsam notu:** KB2.6.SB2 (araçları kullanarak bilgi toplama) toplanmış bilginin doğru kullanımıyla ölçülür; kitapta ayrı bir 'araç kullanma' sorusu yoktur.

### 157 · Fiber optikte çalışma ilkesi: sınır açısı, sürekli tam yansıma ve kayıp

- **Ölçülen:** FİZ.11.3.7 b `KB2.6.SB2`
- **Yapı:** Çekirdek ve cam örtü arasındaki sınır açısı verilen ya da indislerinden bulunan bir fiber (ya da su dolu şişedeki lazer gösterisi) içinde ışının gelme açısına göre sürekli tam yansıma yapıp yapmadığı, cam örtüye geçip kaybolup kaybolmadığı, havadan çekirdeğe girişte nasıl kırıldığı ve (dereceli indisli fiberde) yolun nasıl eğrildiği belirlenir.
- **Uyarıcı:** DIAGRAM, TABLE, EXPERIMENT, TEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Işın cam örtüyle sınır açısından küçük bir açıyla gelirse tam yansıma yapar” (Tam yansıma koşulunu (gelme açısı > sınır açısı) ters kurma); “Çekirdeğin indisi cam örtünün indisinden küçük olmalıdır ki ışık dışarı sızmasın” (Tam yansıma için ışığın çok kırıcı ortamda olması gerektiğini bilmeme); “Gelme açısı arttıkça aynı uzunlukta ışın daha çok yansıma yapar” (Yansıma sayısı–gelme açısı ilişkisini ters kurma); “Havadan çekirdeğe dik gelen ışın da normale yaklaşacak şekilde kırılır” (Dik gelen ışının sapmadan geçtiğini bilmeme)
- **Öğrenci hataları:** Gelme açısını yüzeyle (ışının eksenle) yaptığı açı olarak almak `QUESTION_INTERPRETATION_ERROR`; Sınır açısı eşitliğinde (θ = θs) tam yansımayı var saymak `CONCEPTUAL_ERROR`; Havadan çekirdeğe girişteki kırılmayı (normale yaklaşma) çizimde atlamak `METHOD_SELECTION_ERROR`
- **Kanıt:** program “Gruplar fiber optik malzemelerin tam yansıma olayı…”; kitap s.364 Şekil 3.28; kitap s.366 22. Alıştırma; kitap s.365 Örnek I ve II numaralı ışın; kitap s.400 ÖD-19
- **Kapsam notu:** Yansıma sayısı–gelme açısı ilişkisi (gelme açısı arttıkça aynı uzunlukta yansıma azalır) kitapta açık yazılı değildir; 22. Alıştırma b tablosunun beklenen cevabı geometrik olarak türetilmiştir ve kitabın cevap anahtarıyla doğrulanmamıştır.

### 158 · Fiber optik malzemelerin kullanım alanları ve avantaj/dezavantajlarının sınıflandırılması

- **Ölçülen:** FİZ.11.3.7 b `KB2.6.SB2`
- **Yapı:** Fiber optik kablolar ile ilgili toplanan bilgiler arasından kullanım alanları (genel ağ, telefon, televizyon, endoskopi, endüstriyel kamera, askerî sistem) ve bakır kabloya göre özellikler (manyetik alandan etkilenmeme, hafiflik, düşük kayıp, yüksek bant genişliği, bakım gereksinimi) avantaj–dezavantaj ya da alan–özellik biçiminde eşleştirilir.
- **Uyarıcı:** TABLE, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Fiber optik kablolar elektrik ve manyetik alanlardan bakır kablolar kadar etkilenir” (Işık sinyalinin elektrik/manyetik alandan etkilenmediğini bilmeme); “Fiber optik yalnız iletişimde kullanılır” (Tıp ve sanayi kullanımlarını bilmeme); “Fiber optik kabloların ışığı iletme ilkesi yansıma yerine soğurmadır” (Çalışma ilkesini (tam yansıma) bilmeme)
- **Öğrenci hataları:** Kullanım alanı ile özelliği (avantajı) aynı sütuna yazmak `METHOD_SELECTION_ERROR`; Dezavantaj ifadesini avantaj sayması (ör. bakım ihtiyacı) `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “Öğrenciler fiber optik malzemelerin yapısı, çalışm…”; kitap s.365 Kullanım alanları; kitap s.397 ÖD-12; kitap s.362 7. Etkinlik Değerlendirme 1

### 159 · Fiber optik bilgilerinin doğrulanması: çelişen bilgiler, bağımsız kaynak ve fizik ilkesiyle sınama

- **Ölçülen:** FİZ.11.3.7 c `KB2.6.SB3`
- **Yapı:** Gruplar farklı kaynaklardan fiber optik hakkında bilgi toplamıştır; bazı bilgiler birbiriyle çelişir. Hangi bilginin doğru olduğu, çelişkinin fizik ilkesiyle (tam yansıma için n_çekirdek > n_cam örtü ve gelme açısı > sınır açısı), birden çok bağımsız ve güvenilir kaynakla karşılaştırarak ve kaynağın güncelliğiyle nasıl giderileceği sorulur.
- **Uyarıcı:** TEXT, TABLE, DATA_SET · **Zorluk:** orta
- **Çeldiriciler:** “Bir kaynakta yazan bilgi, başka kaynakla karşılaştırmaya gerek kalmadan doğrudur” (Tek kaynağa güvenme); “Birçok sitede aynı yazıyorsa bilgi kesin doğrudur” (Çoğunluğu doğruluk ölçütü sayma (bağımsızlık)); “Cam örtünün indisi çekirdekten büyük yazan bilgi, fizik ilkesine aykırı olsa da doğrulanır” (Bilgiyi fizik ilkesiyle sınamama); “Eski tarihli bir kaynak, güncel veriler için de her zaman geçerlidir” (Güncelliği değerlendirmeyi bilmeme)
- **Öğrenci hataları:** Çelişen iki bilgiden yalnız daha çok bulunanı seçmek `METHOD_SELECTION_ERROR`; Doğrulama için fizik ilkesine (tam yansıma koşulu) başvurmamak `CONCEPTUAL_ERROR`
- **Kanıt:** program “Grupların ulaştıkları bilgiler tartışma sırasında …”; kitap s.363 2. Performans Görevi; kitap s.361 7. Etkinlik 2. adım

### 160 · Fiber optik bilgilerinin kaydedilmesi: araştırma planı, tablo ve kaynaklı not

- **Ölçülen:** FİZ.11.3.7 ç `KB2.6.SB4`
- **Yapı:** Toplanan bilgi notları yapısı, çalışma ilkesi ve kullanım alanları sütunlu tabloya yerleştirilir; kaynak bilgisiyle düzenleme, araştırma planı adımlarının sıralanması, poster ya da slayt için özetleme ve eksik/yanlış yerleştirilmiş notun bulunması istenir.
- **Uyarıcı:** TABLE, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay
- **Çeldiriciler:** “Telefon ve televizyon çalışma ilkesi sütununa yazılır” (Kullanım alanı ile çalışma ilkesini karıştırma); “Notlar kaynaksız tutulabilir, önemli olan bilginin kendisidir” (Kaynak bilgisiyle kaydetmeyi gereksiz sayma); “Kaynaktaki paragraf aynen kopyalanarak kaydedilmelidir” (Özetleme ve kendi cümleleriyle kayıt becerisini bilmeme)
- **Öğrenci hataları:** Tabloda sütun başlıklarını (yapı / ilke / kullanım) karıştırmak `TABLE_READING_ERROR`; Plan adımlarını (kaydetme–bilgi toplama) ters sıralamak `METHOD_SELECTION_ERROR`
- **Kanıt:** program “Öğrenciler fiber optik malzemelerin yapısı, çalışm…”; kitap s.362 7. Etkinlik 4. adım tablo; kitap s.361 7. Etkinlik 2. adım; kitap s.363 2. Performans Görevi

## FİZ.11.3.8

### 161 · Kırılma yasalarının prizmalar için geçerli olduğuna dair hipotezin kurulması ve test sonucunun yorumlanması

- **Ölçülen:** FİZ.11.3.8 a `FBAB11.SB1`
- **Yapı:** Öğrenciler prizmaları şekil, büyüklük ve malzemelerine göre incelemiş ve ışığın prizmadaki yolu için hipotezler kurmuştur (ör. hava–cam yüzeyinde normale yaklaşma, yüzeye dik gelen ışının sapmaması, prizma büyüklüğünün yolu değiştirip değiştirmediği); simülasyon ya da deney verileri verilir; hangi hipotezin destekleneceği, hangisinin çürütüleceği ve hipotezi sınamak için nasıl bir düzenek/veri gerektiği sorulur.
- **Uyarıcı:** TEXT, TABLE, DIAGRAM, EXPERIMENT, DATA_SET · **Zorluk:** orta
- **Çeldiriciler:** “Prizma büyüdükçe çıkan ışının sapması artar” (Sapmayı prizmanın boyutuna bağlama; açı ve indisin belirleyici olduğunu bilmeme); “Prizmada ışık kırılma yasalarına uymaz, çünkü yüzeyler düzlemdir” (Kırılma yasalarının her saydam yüzeyde geçerli olduğunu bilmeme); “Bir deneyde hipotez desteklendiyse hipotez her koşulda kanıtlanmış olur” (Hipotezin test sonucuyla desteklenme–kanıtlanma ayrımını yapamama); “Işık cama girerken normalden uzaklaşır, camdan çıkarken normale yaklaşır” (Normale yaklaşma/uzaklaşma yönünü ters kurma)
- **Öğrenci hataları:** Hipotezi gözlenen veriyle karşılaştırmadan kendi beklentisine göre değerlendirmek `METHOD_SELECTION_ERROR`; Tabloda yalnız bir değişkeni değiştiren satırları seçmeden hipotezi sınamak `TABLE_READING_ERROR`; Açıları yüzey normali yerine yüzeyle ölçülmüş okumak `QUESTION_INTERPRETATION_ERROR`
- **Kanıt:** program “Gruplar ekip çalışması ile ışığın prizma içinde iz…”; program “Öğrenciler hipotezlerini simülasyon veya deney düz…”; kitap s.368 8. Etkinlik 6–9. adımlar; kitap s.369 Şekil 3.32; kılavuz s.114

### 162 · Tek bir prizmada tek renkli ışığın yolu: kırılma yönleri, sınır açısı ve tam yansıma kararı

- **Ölçülen:** FİZ.11.3.8 a `FBAB11.SB1`, FİZ.11.3.8 b `FBAB11.SB2`
- **Yapı:** Dik üçgen, ikizkenar ya da genel üçgen kesitli cam prizmaya hava ortamından tek renkli ışın gönderilir (dik kenara dik, hipotenüse belirli açıyla vb.); her yüzeyde normale göre yön, gelme açısının sınır açısıyla (cam–hava 42° ya da verilen değer) karşılaştırılması ve tam yansıma kararıyla ışının yolu çizilir; yolundan ortamların indisleri ya da sınır açısı çıkarılır.
- **Uyarıcı:** DIAGRAM, TEXT, TABLE · **Zorluk:** orta–zor
- **Çeldiriciler:** “Prizma içinde ışık hiçbir zaman doğrultu değiştirmez, yalnız dışarı çıkarken kırılır” (Kırılmanın girişte de olduğunu bilmeme); “Cam–hava yüzeyine 30° ile gelen ışın sınır açısı 42° olsa da tam yansıma yapar” (Gelme açısı–sınır açısı kıyasını yapmama (θ < θs → kırılma)); “Havadan cam prizmaya giren ışın normalden uzaklaşır” (Az kırıcıdan çok kırıcıya geçişte normale yaklaşmayı bilmeme); “Prizmanın yüzeyine dik gelen ışın da normale yaklaşacak biçimde kırılır” (Dik gelen ışının sapmayacağını bilmeme)
- **Öğrenci hataları:** Hipotenüse gelme açısını yüzeyle yapılan açı (60°) olarak okumak `QUESTION_INTERPRETATION_ERROR`; Sınır açısını yanlış ortam çiftinden (hava–cam) hesaplamak `FORMULA_SELECTION_ERROR`; Normali yüzeye dik çizmek yerine ışın doğrultusuna dik çizmek `CONCEPTUAL_ERROR`
- **Kanıt:** program “Öğrenciler hipotezlerini simülasyon veya deney düz…”; kitap s.370 Örnek 1; kitap s.371 Örnek 2; kitap s.401 ÖD-21; kitap s.369 Şekil 3.32
- **Kapsam notu:** Yağmur damlası (23. Alıştırma) ve beyaz ışığın ayrışması ayrı ailede (pr-color-dispersion) ele alınır.

### 163 · Tam yansımalı (45°–45°–90°) prizmada ışının yönü: dik yüzeye dik, hipotenüse dik ve hipotenüse paralel gelişler

- **Ölçülen:** FİZ.11.3.8 b `FBAB11.SB2`
- **Yapı:** İkizkenar dik üçgen kesitli cam prizmada (camdan havaya sınır açısı 42°) ışının dik kenarlardan birine dik, hipotenüse dik ya da hipotenüse paralel gelmesi durumlarında kaç tam yansıma yapacağı, hangi yüzeyden çıkacağı ve çıkış doğrultusunun gelen doğrultuyla ilişkisi (90° dönme, 180° dönme, paralel çıkış) kural olarak kullanılır.
- **Uyarıcı:** DIAGRAM, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Tam yansımalı prizmaya giren ışın her durumda 90° çevrilerek çıkar” (Hipotenüse dik gelişte 180° dönüşü bilmeme); “Hipotenüse dik gelen ışın tam yansıma yapmadan prizmadan geçer” (Dik gelen ışının içeride dik kenarlara 45° ile geldiğini görememe); “Dik kenara dik gelen ışın hipotenüste kırılarak havaya çıkar” (45° > 42° kıyasını yapmayıp tam yansımayı atlama); “Prizma aynadan daha çok ışık kaybettirir” (Prizmanın parlaklık ve netlik açısından aynaya göre avantajını bilmeme)
- **Öğrenci hataları:** Hipotenüse gelme açısını 45° yerine 90° almak `QUESTION_INTERPRETATION_ERROR`; İki ardışık tam yansımada çıkış yüzeyinin hipotenüs olduğunu ve yönün ters döndüğünü atlamak `VECTOR_ERROR`
- **Kanıt:** program “Öğrenciler geçerli hipotezlerden yola çıkarak bird…”; kitap s.369 Tam yansımalı prizma; kitap s.369 Şekil 3.33; kitap s.372 24. Alıştırma Kontrol Noktası
- **Kapsam notu:** Kural kitapta Şekil 3.33 üzerinden verilir; sınır açısı 42° bağlamında 45° gelme açısı tam yansımayla sonuçlanır.

### 164 · Birden çok prizmadan oluşan birleşik sistemlerde tek renkli ışığın yolu (dürbün, periskop, tam yansımalı prizma dizileri)

- **Ölçülen:** FİZ.11.3.8 b `FBAB11.SB2`
- **Yapı:** Birbirine göre farklı yönlerde yerleştirilmiş tam yansımalı ya da genel prizmalardan kurulu bir sistemde tek renkli ışınların yolu, her prizmada geçerli kuralların ardışık uygulanmasıyla çizilir; ışının hangi prizmadan çıkacağı, çıkış doğrultusunun giriş doğrultusuna göre durumu ya da belirli bir yönde çıkış için gereken prizma yerleşimi sorulur.
- **Uyarıcı:** DIAGRAM, TABLE, DAILY_LIFE_CONTEXT, EXPERIMENT · **Zorluk:** orta–zor
- **Çeldiriciler:** “Birleşik sistemde ışının yolunu yalnız son prizma belirler” (Ardışık uygulama (her prizmada çıkış doğrultusu bir sonrakinin giriş doğrultusudur) ilkesini bilmeme); “Tam yansımalı iki prizmadan geçen ışın her zaman ilk doğrultusunda çıkar” (Prizmaların yönelimine göre dönmenin değişeceğini bilmeme); “Işın birinci prizmadan çıkarken kırılır, sonraki prizmalarda artık kırılmaz” (Her yüzeyde kırılma yasalarının geçerli olduğunu bilmeme); “Paralel gelen ışınlar prizma dizisinden de tek bir noktada toplanır” (Düzlemsel yüzeylerin eğrisel yüzey gibi odaklama yapacağını sanma)
- **Öğrenci hataları:** Bir prizmadaki çıkış doğrultusunu sonraki prizmanın gelme doğrultusu olarak aktarmamak `METHOD_SELECTION_ERROR`; Çıkış yönünü (180° ters) tam kavrayamayıp yönü yanlış çizmek `VECTOR_ERROR`
- **Kanıt:** program “Öğrenciler geçerli hipotezlerden yola çıkarak bird…”; kitap s.368 8. Etkinlik 10–11. adım; kitap s.398 ÖD-16; kitap s.372 24. Alıştırma; kitap s.399 ÖD-17

### 165 · Prizmada beyaz ışığın renklerine ayrılması ve renge göre farklı sınır açısı · **zenginleştirme**

- **Ölçülen:** FİZ.11.3.8 b `FBAB11.SB2`
- **Yapı:** Beyaz ışık (ya da farklı renkli tek renkli ışınlar) prizmaya gönderilir; kırmızının en az, morun en çok kırıldığı, renge göre sınır açısının değiştiği (kırmızı için en büyük, mor için en küçük) bilgisiyle ışınların yolu, tam yansıma yapan renkler ve çıkış sırası belirlenir.
- **Uyarıcı:** DIAGRAM, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Kırmızı ışık mavi ışıktan daha çok kırılır” (Renk–kırılma sıralamasını ters kurma); “Aynı prizmada tüm renkler için sınır açısı aynıdır” (Sınır açısının renge bağlı olduğunu bilmeme); “Kırmızı ışık tam yansıma yapıyorsa mavi ışık da aynı biçimde yansır, sıralama değişmez” (Sınır açısı küçüldükçe tam yansıma olasılığının arttığını bilmeme)
- **Öğrenci hataları:** Renk sıralamasını sınır açısına yanlış eşlemek (kırmızı → en küçük) `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.369 Görsel 3.22; kitap s.371 Örnek 2; kitap s.372 Kontrol Noktası
- **Kapsam notu:** Program–kitap farkı: FİZ.11.3.8 yalnız tek renkli ışığın prizmalardaki yolunu kapsar; kitap beyaz ışığın renklerine ayrılmasını anlatım (s.369, 372), örnek (s.371) ve ölçme (ÖD-21 ç) düzeyinde işler. Kitaptaki yağmur damlası alıştırmasındaki (23. Alıştırma, s.371) 'tam yansıma' ifadesi fiziksel olarak sorgulanabilir (damla içindeki yansıma kısmidir); bu alıştırma aileye alınmamıştır.

## FİZ.11.3.9

### 166 · Merceğin yapısı ve temel elemanları (asal eksen, optik merkez, iki odak, eğrilik) ile odak uzaklığını belirleyen etmenler

- **Ölçülen:** FİZ.11.3.9 a `KB2.7.SB1`
- **Yapı:** Yakınsak (ince kenarlı) ve ıraksak (kalın kenarlı) merceğin şeklinde eğrilik yarıçapı ve merkezleri, asal eksen, optik merkez ve merceğin iki yanındaki odak noktaları gösterilir ya da simülasyonda bulunur; odak uzaklığının hangi niceliklere (yüzeylerin eğrilik yarıçapı, merceğin ve ortamın kırıcılık indisi, ışığın rengi) bağlı olduğu ve değişim yönü sorulur.
- **Uyarıcı:** DIAGRAM, TABLE, TEXT, DAILY_LIFE_CONTEXT, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Merceğin yalnız bir odak noktası vardır” (Merceğin iki yanında birer odak bulunduğunu bilmeme); “Merceğin eğrilik yarıçapı arttıkça odak uzaklığı azalır” (Eğrilik yarıçapı–odak uzaklığı ilişkisini ters kurma); “Merceğin çapı büyütülürse odak uzaklığı küçülür” (Odak uzaklığını mercek boyutuna bağlama); “Optik merkez, merceğin odak noktasıdır” (Optik merkez ile odak noktasını karıştırma)
- **Öğrenci hataları:** Asal ekseni merceğin kenarlarından geçen doğru sanmak `CONCEPTUAL_ERROR`; Odak uzaklığını merceğin kenarından ölçmek `QUESTION_INTERPRETATION_ERROR`; Mercek ile ortamın indis farkının etkisini yok saymak `CONCEPTUAL_ERROR`
- **Kanıt:** program “Merceklerin asal ekseni, optik merkezi ve odak nok…”; kitap s.375 Mercek tanımı; kitap s.376 Odak uzaklığı etmenleri; kitap s.403 ÖD-23 b; kitap s.373 Görsel 3.23
- **Kapsam notu:** Odak uzaklığının ışığın rengine bağlılığı kitapta (s.376, ÖD-23) vardır; program tek renkli ışıkla sınırlıdır — renk bileşeni lens-chromatic ailesinde zenginleştirme olarak ayrıştırılmıştır, burada yalnız etmen listesi olarak geçer.

### 167 · Merceklerde özel ışınlar ve keyfî ışın: birimkareli zeminde ışının yolu, çıkış noktası ve odak uzaklığı oranı

- **Ölçülen:** FİZ.11.3.9 a `KB2.7.SB1`
- **Yapı:** Birimkareli zeminde odak uzaklıkları verilen yakınsak ve ıraksak mercekler asal eksenleri çakışık yerleştirilir; asal eksene paralel, odağa yönelen (ya da odaktan geçen), 2F'ye yönelen ve optik merkeze giden özel ışınların ve yardımcı eksen–yardımcı odak yöntemiyle keyfî bir ışının mercek(ler)deki yolu çizilir, ışının asal ekseni kestiği nokta ya da odak uzaklıkları oranı sorulur.
- **Uyarıcı:** DIAGRAM, TEXT, TABLE · **Zorluk:** orta–zor
- **Çeldiriciler:** “Yakınsak merceğe asal eksene paralel gelen ışın optik merkezden geçer” (Paralel ışının odağa gittiğini bilmeme); “Iraksak merceğe asal eksene paralel gelen ışın asal ekseni keser” (Iraksak mercekte kırılan ışının kendisinin değil uzantısının odaktan geçtiğini bilmeme); “Optik merkezden geçen ışın kırılarak asal eksene yaklaşır” (Optik merkezden geçen ışının sapmadığını bilmeme); “Odak uzaklığı, merceğin üzerinde ışının girdiği noktadan odaklandığı noktaya kadardır” (Odak uzaklığını optik merkezden ölçmeyi unutma)
- **Öğrenci hataları:** Birimkareli zeminde ışının asal ekseni kestiği noktayı yanlış sayarak bulmak `ARITHMETIC_ERROR`; Iraksak mercekte kırılan ışını gerçekmiş gibi asal eksene doğru çizmek `CONCEPTUAL_ERROR`; Keyfî ışın için yardımcı ekseni gelen ışına paralel çizmeyi atlamak `METHOD_SELECTION_ERROR`
- **Kanıt:** program “Öğrenciler ışınların merceklerde kırıldıktan sonra…”; kitap s.377 Tablo 3.6–3.7; kitap s.378 Şekil 3.41 yardımcı eksen; kitap s.378 Soru kartları; kitap s.390 Özel ışınlar özeti

### 168 · Kırılan ışının yolundan merceğin türünün ve odak uzaklığının çıkarılması

- **Ölçülen:** FİZ.11.3.9 a `KB2.7.SB1`
- **Yapı:** Hava ortamındaki bir ya da birden fazla merceğe gönderilen ışının kırıldıktan sonraki yolu şekille verilir; ışının asal eksene yaklaşıp yaklaşmadığına bakılarak mercek türü, ışının ya da uzantısının asal ekseni kestiği noktadan odak uzaklığı ve (paralel giren paralel çıkan sistemlerde) mercek sırası çıkarılır.
- **Uyarıcı:** DIAGRAM, TEXT, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Işını asal eksene yaklaştıran mercek ıraksak mercektir (hava ortamında)” (Yakınsak–ıraksak ayrımını kırılma yönüyle yapamama); “Iraksak merceğin odak noktası yoktur çünkü ışınlar hiçbir noktada toplanmaz” (Iraksak mercekte odak noktasını ışınların uzantısının kesişimi olarak tanımlayamama); “Paralel giren ışının paralel çıkması için iki mercek de yakınsak olmalıdır” (Galileo tipi sistemde yakınsak ve ıraksak merceğin birlikte kullanıldığını bilmeme); “Odak uzaklığı, kırılan ışının merceğin kenarındaki giriş noktasından asal ekseni kestiği noktaya kadar ölçülür” (Odak uzaklığını optik merkezden ölçmeyi bilmeme)
- **Öğrenci hataları:** Birimkareli zeminde kesişim noktasını optik merkezden saymak yerine merceğin kenarından saymak `ARITHMETIC_ERROR`; Işının asal ekseni kesmesine bakıp ıraksak merceği yakınsak sanmak `CONCEPTUAL_ERROR`
- **Kanıt:** program “Merceklerin fiziksel özelliklerini ve ışınların me…”; kitap s.379 Burcu kartı; kitap s.379 25. Alıştırma Galileo; kitap s.407 ÖD-27; kitap s.380 26. Alıştırma

### 169 · Merceğin ve ortamın kırıcılık indisinin karşılaştırılması: karakter değiştirme ve odak uzaklığına etkisi

- **Ölçülen:** FİZ.11.3.9 a `KB2.7.SB1`
- **Yapı:** Aynı geometrik biçimli (ince ya da kalın kenarlı) mercek, indisi farklı ortamlarda (hava, su, daha kırıcı sıvı) gösterilir; ışınların kırıldıktan sonra yaklaşıp uzaklaşmasına bakarak merceğin ve ortamın indis ilişkisi ya da merceğin hangi ortamda yakınsak/ıraksak davrandığı belirlenir; ortam indisi değişince odak uzaklığının nasıl değiştiği sorulur.
- **Uyarıcı:** DIAGRAM, TEXT, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** orta–zor
- **Çeldiriciler:** “İnce kenarlı mercek hangi ortamda olursa olsun yakınsak mercektir” (Mercek karakterinin yalnız şekle bağlı olduğunu sanma); “Merceği suya batırınca odak uzaklığı değişmez” (Ortamın indisinin odak uzaklığını etkilediğini bilmeme); “Merceğin indisi ortamın indisinden küçükse mercek karakter değiştirmez” (Karakter değiştirme koşulunu bilmeme); “Ortamın indisi büyüdükçe odak uzaklığı her zaman küçülür” (Odak uzaklığının mercek–ortam indis farkına bağlı olduğunu görememe)
- **Öğrenci hataları:** Mercek ve ortam indislerinin yerini karıştırıp eşitsizliği ters yazmak `QUESTION_INTERPRETATION_ERROR`; Karakter değişimini yalnız kalın–ince kenar şekliyle belirlemek `CONCEPTUAL_ERROR`
- **Kanıt:** program “Merceklerin yapılarına ve merceklerde kırılma yasa…”; kitap s.376 Şekil 3.40; kitap s.379 Tuğçe kartı; kitap s.403 ÖD-23 b 3
- **Kapsam notu:** Merceğin indisi ortamın indisine eşit olduğunda merceğin ışığı hiç kırmayacağı (kitapta yazılı değil) kırılma yasasından türetilen ek durumdur.

### 170 · Yakınsak ve ıraksak merceklerin benzer özelliklerinin listelenmesi

- **Ölçülen:** FİZ.11.3.9 b `KB2.7.SB2`
- **Yapı:** Yakınsak ve ıraksak merceklerin ortak yönleri (iki yüzeyinden en az biri küresel, saydam maddeden yapılma, kırılma yasalarına uyma, asal eksen–optik merkez–iki odak, optik merkezden geçen ışının sapmaması, özel ışınlarla görüntü çizimi, odak uzaklığının aynı etmenlere bağlı olması) listeden seçilir ya da sınıflandırma tablosunun 'benzer yönleri' bölümüne yazılır; yanlış ortak özellik ifadeleri elenir.
- **Uyarıcı:** TABLE, TEXT, DIAGRAM, EXPERIMENT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Her iki mercek de ışınları asal eksene yaklaştırır” (Yalnız yakınsağa ait özelliği ortak sanma); “Her iki merceğin odak noktası, ışınların kendisinin kesiştiği noktadır” (Iraksak mercekte odağın ışınların uzantılarıyla bulunduğunu bilmeme); “Her iki mercekte de her konumdaki cisim için gerçek ve ters görüntü oluşur” (Görüntü özelliklerini mercek türüne göre ayıramama); “Yalnız yakınsak merceğin optik merkezi vardır” (Optik merkezin her merceğe ait olduğunu bilmeme)
- **Öğrenci hataları:** Ortak özellik isterken yalnız birine ait özelliği listelemek `QUESTION_INTERPRETATION_ERROR`; Sınıflandırma tablosunda benzer ve farklı sütunlarını karıştırmak `TABLE_READING_ERROR`
- **Kanıt:** program “Öğrenciler nitelik sıralama, anlam çözümleme tablo…”; kitap s.375 9. Etkinlik 13. adım; kitap s.389 Kontrol Noktası; kitap s.374 9. Etkinlik 4–5. adım

### 171 · Yakınsak ve ıraksak merceklerin farklı özelliklerinin listelenmesi ve uygulamaya yansıması

- **Ölçülen:** FİZ.11.3.9 c `KB2.7.SB3`
- **Yapı:** Yakınsak ve ıraksak merceklerin ayırt edici özellikleri (kenar kalınlığı, paralel ışını toplama/dağıtma, odağın gerçek/sanal oluşu, ışını asal eksene yaklaştırma/uzaklaştırma, oluşturabildikleri görüntü türleri) 'farklı yönleri' bölümüne yazılır ya da ifadelerden ayırt edici olanlar seçilir; bu farklar göz kusuru düzeltme, büyüteç, kapı dürbünü gibi uygulamalarda mercek türü seçimine bağlanır.
- **Uyarıcı:** TABLE, TEXT, DIAGRAM, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Büyüteç ıraksak mercektir, çünkü cismi büyük gösterir” (Büyütme–mercek türü ilişkisini yanlış kurma); “Iraksak mercek de yeterince yaklaştırılırsa cismi büyük gösterir” (Iraksak mercekte görüntünün her zaman küçük olduğunu bilmeme); “Miyop göz kusuru yakınsak mercekli gözlükle düzeltilir” (Göz kusuru–mercek türü eşleşmesini ters kurma); “Yakınsak mercek yalnız sanal görüntü verir” (Yakınsak mercekte gerçek ve sanal görüntünün konuma göre değiştiğini bilmeme)
- **Öğrenci hataları:** Ayırt edici özellik isterken iki merceğin ortak özelliğini yazmak `QUESTION_INTERPRETATION_ERROR`; Kenar kalınlığını ışığın toplanmasıyla ters eşlemek `CONCEPTUAL_ERROR`; Uygulamada gerekçeyi yazarken yalnız görüntü büyüklüğüne bakıp kırılma yönünü yok saymak `METHOD_SELECTION_ERROR`
- **Kanıt:** program “Öğrenciler nitelik sıralama, anlam çözümleme tablo…”; kitap s.375 9. Etkinlik 13. adım; kitap s.380 26. Alıştırma; kitap s.387 27. Alıştırma; kitap s.407 ÖD-27

### 172 · Odak uzaklığının ışığın rengine bağlılığı: beyaz ışığın yakınsak mercekte, magenta ışığın ıraksak mercekte kırılması · **zenginleştirme**

- **Ölçülen:** FİZ.11.3.9 a `KB2.7.SB1`
- **Yapı:** Yakınsak mercekte yeşil ışının odak noktası belirtilir; beyaz ışıktaki renklerin mercekteki yolu, mor için odak uzaklığının en küçük, kırmızı için en büyük olduğu ve magenta (kırmızı + mavi) ışığın ıraksak mercekte renklerine nasıl ayrıldığı sorulur; yeşil ışının odağını uzaklaştırmak için ışığın rengi, eğrilik yarıçapı ve indis farkı değişkenleri yorumlanır.
- **Uyarıcı:** DIAGRAM, TABLE, TEXT · **Zorluk:** orta
- **Çeldiriciler:** “Mor ışığın odak uzaklığı kırmızı ışığınkinden büyüktür” (Renge göre odak uzaklığı sıralamasını ters kurma); “Beyaz ışıktaki tüm renkler yakınsak mercekte aynı noktada odaklanır” (Odak uzaklığının renge bağlılığını bilmeme); “Iraksak mercek renkleri ayırmaz, çünkü ışığı yalnız dağıtır” (Dağılmanın (kırılmanın) renge göre farklı olabileceğini görememe)
- **Öğrenci hataları:** Mavi ve kırmızı ışığın kırılma sıralamasını (mavi daha çok) ters almak `CONCEPTUAL_ERROR`
- **Kanıt:** kitap s.403 ÖD-23 c, d; kitap s.376 Odak uzaklığı etmenleri
- **Kapsam notu:** Program–kitap farkı: FİZ.11.3.9 öğretme uygulamasında ışığın rengine ve renge göre odak uzaklığına değinilmez; kitap odak uzaklığının ışığın rengine bağlılığını anlatımda (s.376) verir ve ÖD-23 (s.403) ile ölçer. Bu nedenle zenginleştirme olarak ayrıştırılmıştır.

## FİZ.11.3.10

### 173 · Mercekte cismin konumuna göre görüntünün yeri ve özellikleri (konum–özellik tablosu ve değişim yönü)

- **Ölçülen:** FİZ.11.3.10 b `FBAB7.SB2`
- **Yapı:** Yakınsak merceğin önünde sonsuz–2F, 2F, 2F–F, F ve F–mercek bölgelerinden birindeki cismin (ya da ıraksak merceğin önündeki cismin) görüntüsünün yeri, gerçek/sanal, düz/ters ve boy özellikleri en az iki özel ışınla çizilerek ya da tablodan belirlenir; cisim bir bölgeden diğerine hareket ederken görüntünün yeri ve boyunun nasıl değiştiği sorulur.
- **Uyarıcı:** TABLE, DIAGRAM, TEXT, DAILY_LIFE_CONTEXT · **Zorluk:** kolay–orta
- **Çeldiriciler:** “Yakınsak mercekte oluşan görüntü her zaman gerçektir” (Cisim F–O arasındayken sanal görüntüyü bilmeme); “Cisim F'den merceğe yaklaşırken yakınsak mercekteki görüntünün boyu artar” (Sanal görüntünün boyunun F'den merceğe yaklaşırken azaldığını (F'de sonsuz → merceğe yakın ≈ cisim boyu) bilmeme); “Mercekte görüntü gerçekse mercek ıraksaktır” (Gerçek görüntünün yalnız yakınsak merceğe özgü olduğunu bilmeme); “Cisim yakınsak merceğin F noktasındayken görüntü F'de, nokta şeklinde oluşur” (Cisim F'deyken ışınların paralel çıktığını (görüntünün sonsuzda olduğunu) bilmeme)
- **Öğrenci hataları:** Tabloda 'cisimle aynı taraf' ile 'karşı taraf'ı gerçek–sanal ayrımıyla eşleştirmemek `TABLE_READING_ERROR`; F ve 2F noktalarını karıştırarak bölge belirlemek `CARELESS_ERROR`; Cisim hareket ederken görüntü boyunun yönünü sürekli artar diye genellemek `CONCEPTUAL_ERROR`
- **Kanıt:** program “Öğretmen merceklerde asal eksen üzerinde ve herhan…”; kitap s.385 Tablo 3.8; kitap s.386 Tablo 3.9; kitap s.384 Değerlendirme 1–2; kitap s.388 29. Alıştırma
- **Kapsam notu:** ÖD s.384 ifade III ('F'den merceğe yaklaşan cismin görüntü boyu artar') geometrik olarak yanlıştır: büyütme m = f/(f − d_c) cisim merceğe yaklaşırken azalır; ifade çeldirici/doğrulama sorusu olarak değerlendirilmelidir (kitabın cevap anahtarıyla doğrulanmadı).

### 174 · Görüntünün özelliklerinden mercek türünün ve cismin bulunduğu bölgenin çıkarılması

- **Ölçülen:** FİZ.11.3.10 b `FBAB7.SB2`
- **Yapı:** Görüntünün özellikleri (düz/ters, gerçek/sanal, cisimden büyük/küçük/eşit, ekranda alınıp alınmadığı) bir bağlamda (böcek-büyüteç, kapı dürbünü, ekran) verilir; hangi mercek türünün kullanıldığı, cismin hangi bölgede olduğu ve görüntünün büyümesi için ne yapılması gerektiği çıkarılır.
- **Uyarıcı:** DIAGRAM, TEXT, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Cismi büyük ve düz gösteren mercek ıraksak mercektir” (Büyüteç davranışını ıraksak mercekle eşleme); “Ekranda net alınan görüntü sanaldır” (Gerçek–sanal ve ekran ilişkisini ters kurma); “Yakınsak ve ıraksak merceklerde görüntüyü büyütmek için cismi her zaman mercekten uzaklaştırmak gerekir” (Cismin konumu–görüntü boyu ilişkisinin yönünü (yakınsakta F'ye yaklaşma, ıraksakta merceğe yaklaşma) genelleyememe); “Küçük, düz ve sanal görüntü yalnız ayna ile elde edilir” (Iraksak merceğin de aynı özelliği verdiğini bilmeme)
- **Öğrenci hataları:** Yalnız boy bilgisine bakıp (büyük → yakınsak) görüntü düz/ters bilgisini yok saymak `METHOD_SELECTION_ERROR`; Cismin bölgesini yalnız sanal–gerçek bilgisinden bulmaya çalışmak `CONCEPTUAL_ERROR`
- **Kanıt:** program “Öğrenciler deney düzenekleri, simülasyon, animasyo…”; kitap s.399 ÖD-18; kitap s.384 Değerlendirme 3; kitap s.387 27. Alıştırma

### 175 · Birimkareli zeminde özel ışınlarla mercek görüntüsü çizimi: görüntü yeri, uzaklık ve boy karşılaştırması

- **Ölçülen:** FİZ.11.3.10 b `FBAB7.SB2`
- **Yapı:** Odak uzaklığı birim olarak verilen yakınsak ve/veya ıraksak mercek, asal eksen üzerindeki iki cisim ve noktalar birimkareli zeminde gösterilir; özel ışınlarla görüntüler çizilerek görüntülerin yeri, aralarındaki uzaklık, boy oranları ve (cisim salınırken) görüntünün gerçek/sanal oluşu belirlenir.
- **Uyarıcı:** DIAGRAM, TEXT, TABLE · **Zorluk:** orta–zor
- **Çeldiriciler:** “Iraksak merceğin F noktasındaki cisminin görüntüsü merceğin diğer tarafında oluşur” (Iraksak mercekte görüntünün cisimle aynı tarafta, sanal oluştuğunu bilmeme); “Görüntü cismin iki katı uzaklıktaysa görüntü boyu da yarısıdır” (Boy oranı = uzaklık oranı (h_g/h_c = d_g/d_c) ilişkisini ters kurma); “Odağa yönelen ışın kırıldıktan sonra asal eksene dik çıkar” (Odaktan geçen (odağa yönelen) ışının asal eksene paralel kırıldığını yanlış hatırlama); “Cisim F ile 2F arasından 2F'nin ötesine geçerken görüntü sanal olur” (Gerçek–sanal geçişinin F noktasında olduğunu bilmeme)
- **Öğrenci hataları:** Birimkareli zeminde görüntü yerini özel ışınların kesişimiyle bulmak yerine tahmin etmek `METHOD_SELECTION_ERROR`; Görüntü uzaklığını optik merkezden değil cismin bulunduğu noktadan saymak `QUESTION_INTERPRETATION_ERROR`; Boy oranı yerine uzaklık oranını tersine almak `ARITHMETIC_ERROR`
- **Kanıt:** program “Öğrenciler deney düzeneklerindeki cisimlerin bulun…”; kitap s.386 Örnek; kitap s.388 28. Alıştırma; kitap s.400 ÖD-20; kitap s.385 Boy–uzaklık oranı
- **Kapsam notu:** Kitap örnekleri cismi 3F gibi özel olmayan noktalara koyar (s.386–387); görüntü yeri çizimle bulunabilir ancak ölçme sorusu yazılırken cisim konumları F, 2F ve bunların orta noktalarıyla sınırlı kalmalıdır. Mercek denklemi kullanılmaz.

### 176 · Merceklerde görüntü oluşumu deneyi tasarımı: değişkenler, odak uzaklığını belirleme, düzenek, gerçek–sanal görüntünün gözlenmesi ve güvenlik

- **Ölçülen:** FİZ.11.3.10 a `FBAB7.SB1`
- **Yapı:** Cismin yerine göre görüntünün yeri ve özelliklerini bulmak için optik sıra üzerinde ışıklı cisim, mercek ve ekranla (ya da simülasyonla) deney kurgulanır; araştırma sorusu, değişkenlerin sınıflaması, önce odak uzaklığının belirlenip F ve 2F'nin işaretlenmesi, cismin altı bölgeye getirilmesi, gerçek görüntünün ekranda yakalanması/sanal görüntünün ekranda yakalanamaması, veri tablosunun başlıkları ve güvenlik önlemleri sorulur ya da hatalı düzenek eleştirilir.
- **Uyarıcı:** TEXT, DIAGRAM, EXPERIMENT, TABLE, DAILY_LIFE_CONTEXT · **Zorluk:** orta
- **Çeldiriciler:** “Cismi farklı konumlara getirirken her seferinde merceği de değiştirmek gerekir” (Tek değişkeni (cismin konumu) değiştirme ilkesini bilmeme); “Odak uzaklığı ölçülmeden F ve 2F noktaları rastgele işaretlenebilir” (Cismin bölgelerinin f'ye göre tanımlandığını bilmeme); “Sanal görüntü ekranı kaydırarak net olana kadar aranırsa ekranda bulunur” (Sanal görüntünün ekranda yakalanamayacağını bilmeme); “Bağımsız değişken görüntünün boyu, bağımlı değişken cismin konumudur” (Bağımsız ve bağımlı değişkeni ters eşleme)
- **Öğrenci hataları:** Ölçülen nicelikleri (görüntü uzaklığı, boyu) kontrol değişkeni olarak yazmak `METHOD_SELECTION_ERROR`; Güvenlik önlemlerinde güneşe doğrudan bakmamayı ve mercekle odaklanan ışığın yakıcılığını yazmamak `QUESTION_INTERPRETATION_ERROR`; Veri tablosunda cismin konumunu F/2F cinsinden yazarken ölçülen uzaklık sütununu atlamak `TABLE_READING_ERROR`
- **Kanıt:** program “Yakınsak ve ıraksak merceklerde görüntü oluşumu il…”; program “Öğrenciler öğretmen rehberliğinde gruplara ayrılar…”; kitap s.381 10. Etkinlik 2. adım; kitap s.383 10. Etkinlik 7–9. adımlar; kılavuz s.114

### 177 · Mercek deney verisinin analizi: tablo, simülasyon ölçümü, boy–uzaklık oranı ve tutarsız ölçüm

- **Ölçülen:** FİZ.11.3.10 b `FBAB7.SB2`
- **Yapı:** Cismin merceğe uzaklığı, görüntünün merceğe uzaklığı, cisim ve görüntü boyu ve görüntü özelliklerini içeren ölçüm tablosu (ya da simülasyon verisi, d_g–d_c grafiği) verilir; verilerden mercek türü, odak uzaklığı, hangi satırın tutarsız olduğu, boy–uzaklık orantısı ve cismin bölgesi analiz edilir.
- **Uyarıcı:** TABLE, DATA_SET, EXPERIMENT, GRAPH · **Zorluk:** orta–zor
- **Çeldiriciler:** “Cisim merceğe yaklaştıkça yakınsak mercekte görüntü her zaman küçülür” (Görüntü boyunun cismin konumuna göre değişim yönünü genellemek); “d_g > d_c olan satırda görüntü cisimden küçüktür” (Boy oranının uzaklık oranına eşit olduğunu ters kurma); “Görüntüsü ekranda alınamayan satırdaki ölçüm hatalıdır” (Sanal görüntünün ekranda alınamayacağını bilmeme); “Iraksak merceğin verisinde görüntü uzaklığı cisim uzaklığından büyük çıkar” (Iraksak mercekte görüntünün her zaman cisimle mercek arasında oluştuğunu bilmeme)
- **Öğrenci hataları:** Uzaklıkları optik merkezden değil cismin ya da ekranın kenarından okumak `QUESTION_INTERPRETATION_ERROR`; Tabloda cisim ve görüntü sütunlarını karıştırmak `TABLE_READING_ERROR`; cm ve m birimlerini karıştırmak `UNIT_ERROR`
- **Kanıt:** program “Öğrenciler deney düzenekleri, simülasyon, animasyo…”; program “Yakınsak ve ıraksak merceklerde görüntü oluşumu il…”; kitap s.383 10. Etkinlik 17–18. adımlar; kitap s.383 10. Etkinlik 10–11. adım; kitap s.385 Boy–uzaklık oranı

### 178 · Mercek denklemiyle (1/f = 1/d_c + 1/d_g) sayısal görüntü uzaklığı hesabı · **hesap kapsam dışı**

- **Ölçülen:** FİZ.11.3.10 b `FBAB7.SB2`
- **Yapı:** Odak uzaklığı cm cinsinden verilen yakınsak merceğin iki yanındaki asal eksen üzerinde bulunan, f'nin katı olmayan uzaklıklardaki cisimlerin görüntülerinin merceğe uzaklıkları ve aralarındaki mesafe sorulur.
- **Uyarıcı:** TEXT, DIAGRAM · **Zorluk:** orta
- **Çeldiriciler:** “Cisim 60 cm'deyse görüntü de 60 cm'dedir” (Görüntü uzaklığını cisim uzaklığına eşit alma (2F'ye özgü durumu genelleme)); “İki görüntünün aralarındaki uzaklık, görüntü uzaklıklarının farkıdır” (Görüntülerin merceğin zıt taraflarında olduğunu gözden kaçırma)
- **Öğrenci hataları:** 1/f = 1/d_c + 1/d_g bağıntısında terimleri toplayıp ters çevirmeyi atlamak `ALGEBRA_ERROR`; Görüntü uzaklığının işaretini (gerçek/sanal) yanlış almak `SIGN_ERROR`
- **Kanıt:** kitap s.398 ÖD-14
- **Kapsam notu:** Kitap–program çelişkisi: mercek denklemi ne FİZ.11.3.10 programında ne de kitabın anlatımında bulunur (formül: mirror-lens-equation, OUT_OF_CURRICULUM) ancak s.398 ÖD-14 bunu gerektirir (60 cm = 1,5f ve 120 cm = 3f özel olmayan konumlardır). Öğrenciye beklenen yöntem olarak sunulmaz; programa uygun yol, f'ye göre ölçekli birimkareli zeminde özel ışınlarla çizimdir (bkz. lens-grid-image-construction).
