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
