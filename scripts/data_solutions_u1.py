"""STEP 11–12 — Ünite 1 (Kuvvet ve Hareket): soru ailesi çözüm yöntemleri ve kısa yolları.

Her ailede: standard (normal çözüm), conceptual (fiziksel mantık), fast (sınav hızı) ve alternative (ikinci yol).
Çözümlü örnekler özgündür; `python_check` cevabı bağımsız (genellikle sayısal simülasyon / farklı formül ile) doğrular.
Sabitler: g = 10 m/s²; sin37° = cos53° = 0,6; cos37° = sin53° = 0,8.
Terimler: programa uygun olarak 'yatay atış / eğik atış / düşey atış' yerine 'iki boyutlu hareket' ve 'serbest düşme' kullanılır.
Kapsam dışı (CORE olmayan) iki aile çözümlenmez: 2d-moving-reference-launch (ENRICHMENT), rail-system-circular (OUT_OF_SCOPE_CALC).
"""


def M(steps, validity, limits, risks):
    return {"steps": steps, "validity": validity, "limits": limits, "risks": risks}


def S(standard, conceptual, fast, alternative, insight, problem, steps, answer, check):
    return {"standard": standard, "conceptual": conceptual, "fast": fast, "alternative": alternative,
            "expert_insight": insight,
            "worked_example": {"problem": problem, "steps": steps, "answer": answer, "python_check": check}}


SOLUTIONS = {}
SHORTCUTS = []

# ============================ FİZ.11.1.1 – FİZ.11.1.2 ============================
SOLUTIONS["ff-mass-independence"] = S(
    M(["Cisme etki eden kuvvetleri yaz: yalnız ağırlık G = m·g (hava direnci ihmal).",
       "Newton'un 2. yasası: m·g = m·a.",
       "Kütle sadeleşir: a = g. Tüm cisimler için ivme aynıdır.",
       "Aynı h ve ϑ₀ = 0 için t = √(2h/g), ϑ = √(2gh) olduğundan süre ve çarpma hızı da kütleden bağımsızdır."],
      ["Hava direnci ihmal edilebilir ya da cisimler için aynı etkiyi yapıyor", "Yer çekimi alanı düzgün (g sabit)"],
      ["Hava direnci ihmal edilmiyorsa sonuç geçersizdir (kâğıt-taş, tüy-çekiç havada)"],
      ["Havalı ortamda da kütle bağımsızlığını uygulamak", "'Ağır olan önce düşer' sezgisine kapılmak"]),
    M(["Ağırlık kütle ile orantılı artar; ama ivmeyi veren, kuvvetin eylemsizliğe (kütleye) oranıdır.",
       "Kütle iki kat olunca hem itme (ağırlık) hem direnç (eylemsizlik) iki kat olur; oran değişmez.",
       "Hava direnci varsa direnç ağırlıkla aynı oranda büyümez; bu yüzden hafif cisim yavaşlar."],
      ["Yalnız yer çekimi etkisi", "Aynı konumdaki cisimler"],
      ["Niceliksel hesap gerekmez; yalnız karşılaştırma"],
      ["Eylemsizlik ile ağırlık arasındaki ilişkiyi bilmemek"]),
    M(["Seçeneklerde 'hava direnci ihmal' ifadesini ara.",
       "Varsa ivme, süre ve çarpma hızı tüm cisimler için eşittir; kütleyi içeren seçenekleri ele."],
      ["'Havasız / hava direnci ihmal' koşulu açıkça verilmiş"],
      ["Koşul belirtilmemişse havalı ortam olabilir; metni oku"],
      ["Koşulu atlayıp hızlı cevap vermek"]),
    None,
    "Soruda farklı kütleli cisimler + 'hava direnci ihmal' varsa cevap hep 'eşit ivme, eşit süre, eşit hız'; 'ağır önce düşer' seçeneği tuzaktır. Havalıysa kesit alanı ve şekle bak.",
    "Havasız bir ortamda 1 kg ve 4 kg kütleli iki cisim 20 m yükseklikten aynı anda bırakılıyor. Düşme sürelerini ve ivmelerini karşılaştırınız. Aynı cisimlere havalı ortamda 2 N'luk sabit bir direnç etki etseydi hangisi önce yere ulaşırdı?",
    ["a = G/m = m·g/m = g = 10 m/s² (iki cisim için de).",
     "t = √(2h/g) = √(2·20/10) = 2 s (iki cisim için de); yere aynı anda ulaşırlar.",
     "Direnç varsa a = g − F_d/m: 1 kg için 8, 4 kg için 9,5 m/s²; 4 kg'lık cisim önce ulaşır."],
    "Havasızda ikisi de a = 10 m/s², t = 2 s (aynı anda). 2 N dirençte 4 kg'lık cisim önce yere ulaşır.",
    """
g = 10.0
h = 20.0
def a_free(m, drag=0.0):
    return (m * g - drag) / m
def fall_time(a):
    return (2 * h / a) ** 0.5
for m in (0.1, 1.0, 4.0, 100.0):
    assert abs(a_free(m) - g) < 1e-9
assert abs(fall_time(a_free(1.0)) - 2.0) < 1e-9 and abs(fall_time(a_free(4.0)) - 2.0) < 1e-9
# direnç varsa kütle bağımsızlığı bozulur
assert a_free(4.0, 2.0) > a_free(1.0, 2.0)
assert fall_time(a_free(4.0, 2.0)) < fall_time(a_free(1.0, 2.0))
assert abs(a_free(1.0, 2.0) - 8.0) < 1e-9 and abs(a_free(4.0, 2.0) - 9.5) < 1e-9
""")

SOLUTIONS["ff-data-pattern-g"] = S(
    M(["Tabloda ardışık eşit zaman aralıklarında hız farklarını al: Δϑ.",
       "İvme a = Δϑ/Δt; farklar sabitse ivme sabittir.",
       "Hız sıfırdan başlıyorsa a = ϑ/t oranı da aynı değeri verir (ϑ-t grafiği orijinden geçer).",
       "İstenirse yer değiştirme ϑ-t grafiği altındaki alandan (ya da h = ½at²) bulunur."],
      ["Zaman aralıkları eşit", "Hız farkları sabit (sabit ivme)"],
      ["Konum tablosu verilmişse önce ikinci farklar alınır (hız değil konum farkları sabit olmaz)"],
      ["Hız değerini ivme sanmak", "Farklı zaman aralıklarını eşit sanıp fark almak"]),
    M(["Eşit sürelerde hız eşit miktarda artıyorsa net kuvvet sabit, dolayısıyla ivme sabittir.",
       "Hız arttığı için ivmenin arttığını düşünmek yanlıştır: ivme hızın değişim hızıdır.",
       "Başka gezegende aynı örüntü daha küçük ya da büyük fark verir; fark o gezegenin g'sidir."],
      ["Cisim yalnız yer çekimi etkisinde"],
      ["Sabit olmayan farklar sabit ivme olmadığını gösterir (örn. hava direnci)"],
      ["Farkların sabitliğini kontrol etmeden genelleme yapmak"]),
    M(["ϑ(t₂) − ϑ(t₁) bölü (t₂ − t₁) hesapla; bir kez yeter, sabit olduğundan emin olmak için ikinci aralığı da gözle."],
      ["Hız farkları sabit olduğu doğrulanmış"],
      ["Tek aralığa bakıp sabitlik varsaymak risklidir"],
      ["Sabitlik kontrolünü atlamak"]),
    M(["ϑ-t grafiğinin eğimini üçgen kuralıyla oku: Δϑ/Δt.", "Eğim doğrusalsa ivme sabit, eğimin değeri g'dir."],
      ["Grafik doğrusal"], ["x-t grafiğinin eğimi hızdır, ivme değil"], ["Eksenleri karıştırmak"]),
    "Tabloda 'her saniye hız aynı miktar artıyorsa' ivme sabittir; ivme = o artış. Konum tablosu ise önce ikinci fark (Δ²x = a·Δt²) ister.",
    "Başka bir gezegende serbest bırakılan bir cismin hızı 1 s aralıklarla ölçülüyor: t = 0, 1, 2, 3, 4 s için ϑ = 0; 3,7; 7,4; 11,1; 14,8 m/s. İvmeyi ve 4 s'de düşülen yolu bulunuz.",
    ["Ardışık farklar: 3,7 m/s her saniye (sabit) → a = 3,7 m/s².",
     "Yol = ϑ-t grafiği altındaki alan = ½·4·14,8 = 29,6 m (ya da ½·3,7·16)."],
    "a = 3,7 m/s² (sabit); h = 29,6 m.",
    """
t = [0, 1, 2, 3, 4]
v = [0, 3.7, 7.4, 11.1, 14.8]
diffs = [v[i + 1] - v[i] for i in range(4)]
assert all(abs(d - diffs[0]) < 1e-9 for d in diffs)
a = diffs[0] / (t[1] - t[0])
assert abs(a - 3.7) < 1e-9
# alan (yamuk toplamı) ve h = a t^2 / 2
area = sum((v[i] + v[i + 1]) / 2 * (t[i + 1] - t[i]) for i in range(4))
assert abs(area - 29.6) < 1e-9 and abs(0.5 * a * 4 ** 2 - 29.6) < 1e-9
""")

SOLUTIONS["ff-reaction-time-ruler"] = S(
    M(["Cetvel serbest düşer: ϑ₀ = 0, h = ½·g·t².", "h'yi metreye çevir (cm / 100).",
       "t = √(2h/g) hesapla.", "Karşılaştırmada küçük h → küçük tepki süresi."],
      ["Cetvel bırakıldığı anda ilk hız sıfır", "Hava direnci ihmal"],
      ["Cetvelin tutuş noktasındaki başlangıç okuması çıkarılmalıdır (sıfır çizgisi parmak hizasında)"],
      ["cm'yi m'ye çevirmemek", "h = g·t veya h = ϑt kullanmak"]),
    M(["Yakalama mesafesi arttıkça cetvel daha uzun süre düşmüş demektir.", "Mesafe süre ile doğrusal değil, karesel artar: süre iki kat → mesafe dört kat."],
      ["Serbest düşme"], ["Sayısal süre için formül gerekir"], ["Doğrusal orantı kurmak"]),
    M(["Oran sorusunda t ∝ √h: mesafe 4 katına çıkarsa süre 2 katına çıkar; mesafe 9 katına çıkarsa süre 3 katına çıkar."],
      ["İki ölçümde de ϑ₀ = 0"], ["Mesafe farkı toplamdan alınmaz; her biri sıfırdan ölçülür"], ["Oranı karekök almadan kullanmak"]),
    None,
    "Cetvel, ölçüm, 'tepki süresi' ifadeleri → h = ½gt². Mesafe-süre orantısı karekök: yakalama mesafesi 4 katsa süre 2 kat.",
    "Bir öğrenci düşen cetveli, cetvel 20 cm düştükten sonra yakalıyor. Arkadaşı aynı cetveli 80 cm düştükten sonra yakalıyor. İki öğrencinin tepki sürelerini ve oranını bulunuz.",
    ["h₁ = 0,20 m: t₁ = √(2·0,2/10) = 0,2 s.", "h₂ = 0,80 m: t₂ = √(2·0,8/10) = 0,4 s.", "t₂/t₁ = 2 (mesafe 4 kat, süre 2 kat)."],
    "t₁ = 0,2 s, t₂ = 0,4 s; ikincinin tepki süresi iki kat uzundur.",
    """
g = 10.0
t = lambda h: (2 * h / g) ** 0.5
assert abs(t(0.20) - 0.2) < 1e-9 and abs(t(0.80) - 0.4) < 1e-9
assert abs(t(0.80) / t(0.20) - 2.0) < 1e-9
# geri doğrulama: h = g t^2 / 2
assert abs(0.5 * g * 0.2 ** 2 - 0.20) < 1e-9
""")

SOLUTIONS["ff-kinematics-v0zero"] = S(
    M(["ϑ₀ = 0 olduğunu not et; bilinen iki nicelik ve istenen nicelikten bağıntı seç.",
       "Süre var, yükseklik isteniyorsa h = ½gt²; süre var, hız isteniyorsa ϑ = gt; süre yoksa ϑ² = 2gh.",
       "Gerekirse ikinci bağıntıyla kalan niceliği bul.",
       "'Son 1 saniyede alınan yol' için h(t) − h(t−1) farkını al."],
      ["ϑ₀ = 0", "Hava direnci ihmal", "g sabit"],
      ["İlk hız varsa ϑ₀'lı bağıntılar gerekir", "Uzun düşmelerde (limit hız) geçerli değil"],
      ["ϑ² = 2gh'de karekökü unutmak", "½ katsayısını atlamak", "Son saniye yolunu toplam yolun yarısı sanmak"]),
    M(["ϑ = g·t: hız her saniye 10 m/s artar.", "Ortalama hız ϑ/2 olduğundan h = (ϑ/2)·t = ½gt².",
       "Süre iki katına çıkarsa hız iki, yol dört katına çıkar."],
      ["Sabit ivme, ϑ₀ = 0"], ["Nicel sonuç için formül gerekir"], ["Yol-süre ilişkisini doğrusal sanmak"]),
    M(["g = 10 için ϑ'yi t'nin 10 katı, h'yi t² nin 5 katı olarak oku (t=1→5 m, 2→20 m, 3→45 m, 4→80 m).",
       "Süresiz sorularda h = ϑ²/20."],
      ["g = 10 m/s²", "ϑ₀ = 0"], ["g farklı verilirse (ör. başka gezegen) katsayılar değişir"], ["Tam sayı olmayan sürede tablo ezberi"]),
    M(["Ortalama hız yöntemi: h = (0 + ϑ)/2 · t.", "Enerji bakışı (12. sınıf ya da ileride): ϑ² = 2gh aynı sonucu verir."],
      ["Sabit ivme"], ["Enerjiyi kullanmak programda bu ünite dışındadır"], ["Ortalama hızı son hızın tamamı almak"]),
    "'Bırakılıyor' (ϑ₀ = 0) + iki bilgi + bir istenen → üç bağıntıdan uygununu seç. 'Son t saniyede' ifadesi görünce fark al: h(T) − h(T−t).",
    "Bir cisim yerden 45 m yükseklikten serbest bırakılıyor. Yere düşme süresini, çarpma hızını ve son 1 saniyede aldığı yolu bulunuz. (g = 10 m/s²)",
    ["45 = ½·10·t² → t = 3 s.", "ϑ = g·t = 30 m/s (kontrol: √(2·10·45) = 30).",
     "2 s'de alınan yol = 5·2² = 20 m; son 1 s yolu = 45 − 20 = 25 m."],
    "t = 3 s, ϑ = 30 m/s, son saniyedeki yol 25 m.",
    """
g = 10.0
h = 45.0
t = (2 * h / g) ** 0.5
v = g * t
assert abs(t - 3.0) < 1e-9 and abs(v - 30.0) < 1e-9
assert abs((2 * g * h) ** 0.5 - v) < 1e-9
last = 0.5 * g * t ** 2 - 0.5 * g * (t - 1) ** 2
assert abs(last - 25.0) < 1e-9
# 1:3:5 örüntüsü ile çapraz kontrol (45 m = 5 + 15 + 25)
assert abs(last - 5 * 5) < 1e-9
""")

SOLUTIONS["ff-upward-throw"] = S(
    M(["Pozitif yönü (örn. yukarı) seç; ϑ₀ yukarı ise +, ivme her zaman −g.",
       "Tepe noktası: ϑ = ϑ₀ − g·t = 0 → t_çıkış = ϑ₀/g; h_max = ϑ₀²/(2g).",
       "Aynı seviyeye dönüşte toplam süre 2ϑ₀/g; yerden yüksek atışta tek denklem: Δy = ϑ₀·t − ½gt² (Δy = −H zemin seviyesi için).",
       "İkinci derece denklemin fiziksel (pozitif) kökünü al; çarpma hızı ϑ = ϑ₀ − g·t (işaretiyle)."],
      ["Hava direnci ihmal", "g sabit", "İvme işareti tüm hareket boyunca aynı"],
      ["Hava direnci varsa çıkış-iniş süreleri eşit değildir"],
      ["Yön değişince ivme işaretini değiştirmek", "Negatif kökü seçmek", "ϑ² = ϑ₀² ± 2gh'de h yerine toplam yolu koymak (h yer değiştirmedir)"]),
    M(["Yukarı çıkarken hız her saniye 10 m/s azalır; tepede anlık sıfır olur ve hareket tersine döner.",
       "Tepede ivme hâlâ g'dir (net kuvvet ağırlık); cisim dengede değildir.",
       "Hareket ϑ_tepe'ye göre simetrik: aynı seviyede hız büyüklükleri eşit, yönler zıt."],
      ["Serbest düşme"], ["Nicel sonuç için bağıntı gerekir"], ["Tepe noktasında ivmeyi sıfır sanmak"]),
    M(["Aynı seviyeye dönüşte: t_çıkış = t_iniş, h_max = ϑ₀²/20 (g=10), toplam süre = ϑ₀/5.",
       "Yerden yüksek atışta önce tepe, sonra tepeden serbest düşme gibi iki parça düşün: tepeden yere yükseklik H + h_max."],
      ["Atış seviyesinde ya da bilinen seviyede dönüş"], ["Yüksek atışta tek simetri toplam süre için yetmez"], ["Toplam süreyi 2ϑ₀/g sanmak (yüksekten atışta yanlış)"]),
    M(["Tepeden serbest düşme yöntemi: tepe yüksekliği = H + h_max; t_iniş = √(2(H+h_max)/g); toplam = ϑ₀/g + t_iniş."],
      ["Atış yüksekliği ve tepe biliniyor"], ["Adım sayısı daha fazla"], ["h_max'ı yerden değil atış noktasından ölçülmüş yüksekliğe eklemeyi unutmak"]),
    "'Yukarı fırlatılıyor' + tepe/toplam süre/çarpma hızı → önce ϑ=0 (tepe), sonra simetri ya da tek denklem. Yerden yüksekten atışta kuvvetli seçenek: tepeden serbest düşme.",
    "Yerden 25 m yüksekteki balkondan bir cisim 20 m/s hızla düşey yukarı fırlatılıyor. Maksimum yüksekliği (yerden), yere çarpma süresini ve çarpma hızını bulunuz. (g = 10 m/s²)",
    ["h_max (atıştan) = 20²/(2·10) = 20 m; yerden yükseklik 45 m.",
     "Yukarı pozitif, zemin Δy = −25: −25 = 20t − 5t² → t² − 4t − 5 = 0 → t = 5 s (t = −1 s alınmaz).",
     "ϑ = 20 − 10·5 = −30 m/s: çarpma hızı 30 m/s aşağı yönlü (kontrol: tepeden 45 m serbest düşme → √(2·10·45) = 30)."],
    "h_max = 45 m (yerden); t = 5 s; ϑ = 30 m/s (aşağı).",
    """
g = 10.0
v0, H = 20.0, 25.0
h_up = v0 ** 2 / (2 * g)
assert abs(h_up - 20.0) < 1e-9
# ikinci derece: 0.5 g t^2 - v0 t - H = 0
a, b, c = 0.5 * g, -v0, -H
disc = b * b - 4 * a * c
t = (-b + disc ** 0.5) / (2 * a)
assert abs(t - 5.0) < 1e-9
v = v0 - g * t
assert abs(v + 30.0) < 1e-9
# bağımsız kontrol: tepeden serbest düşme
t_peak = v0 / g
t_fall = (2 * (H + h_up) / g) ** 0.5
assert abs(t_peak + t_fall - t) < 1e-9 and abs(g * t_fall - 30.0) < 1e-9
# simetri: aynı seviyede hız büyüklüğü eşit
y = 10.0
vy = (v0 ** 2 - 2 * g * y) ** 0.5
assert abs((v0 - g * ((v0 - vy) / g)) - vy) < 1e-9
""")

SOLUTIONS["ff-downward-throw-or-moving-carrier"] = S(
    M(["Taşıyıcının hızını cismin ilk hızı al: ϑ₀ = taşıyıcının hızı (yön dahil).",
       "Yönü seç (örn. aşağı +). Aşağı hareket eden taşıyıcıda ϑ₀ pozitif, yukarıda negatif.",
       "Aşağı + için: h = ϑ₀t + ½gt² (ϑ₀ yukarıysa negatif işaretle yazılır).",
       "İkinci derece denklemin pozitif kökünü al; çarpma hızı ϑ = ϑ₀ + gt."],
      ["Bırakılan cisim taşıyıcıyla birlikte hareket ediyordu", "Hava direnci ihmal"],
      ["Asansör ivmeliyse bırakma anındaki hız ilk hız alınır, sonraki ivme yine g'dir"],
      ["İlk hızı sıfır almak", "Yukarı çıkan balondan bırakılanın hemen aşağı gittiğini sanmak", "Yön işaretlerini karıştırmak"]),
    M(["Bırakma anında cisim, taşıyıcının hızını 'miras' alır; kuvvet etkisi yoksa hızı korumak ister (eylemsizlik).",
       "Bırakıldıktan sonra yalnız ağırlık etkiler: ivme g aşağı.", "Yukarı giden taşıyıcıdan bırakılan cisim önce yükselir, sonra düşer."],
      ["Serbest düşme"], ["Hesap için bağıntı gerekir"], ["Bırakıldığı anda hızını sıfır sanmak"]),
    M(["ϑ₀ ve h verilince: aşağı hareket için ϑ² = ϑ₀² + 2gh ile çarpma hızını doğrudan bul (süre sorulmuyorsa).",
       "Yukarı giden taşıyıcı için de aynı: ϑ² = ϑ₀² + 2gh (ϑ₀ büyüklüğü), çünkü yükseklik farkı yönden bağımsız."],
      ["Sadece çarpma hızı isteniyor"], ["Süre isteniyorsa yetmez"], ["h yerine alınan yolu koymak"]),
    None,
    "'Hareket eden … bırakılıyor' ifadesi ilk hızın sıfır olmadığını söyler. İlk hızın yönünü seç, ivmeyi g al, ikinci dereceden denklemi pozitif kökle bitir.",
    "60 m yükseklikte 5 m/s hızla alçalan bir balondan bir kum torbası bırakılıyor. Aynı yükseklikte 5 m/s hızla yükselen balondan bırakılsaydı ne olurdu? İki durumda yere ulaşma süresini ve çarpma hızını bulunuz.",
    ["Aşağı (+): 60 = 5t + 5t² → t² + t − 12 = 0 → t = 3 s; ϑ = 5 + 30 = 35 m/s.",
     "Yukarı çıkan balon: ϑ₀ = −5 (aşağı +): 60 = −5t + 5t² → t² − t − 12 = 0 → t = 4 s; ϑ = −5 + 40 = 35 m/s aşağı.",
     "Önce 0,5 s yükselir; iki durumda çarpma hızı aynı (aynı yükseklik fark, aynı ϑ₀ büyüklüğü)."],
    "Alçalan: t = 3 s, ϑ = 35 m/s. Yükselen: t = 4 s, ϑ = 35 m/s.",
    """
g = 10.0
H = 60.0
def solve(v0):
    # aşağı +: H = v0 t + 0.5 g t^2
    a, b, c = 0.5 * g, v0, -H
    return (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
t1 = solve(5.0)
t2 = solve(-5.0)
assert abs(t1 - 3.0) < 1e-9 and abs(t2 - 4.0) < 1e-9
assert abs((5.0 + g * t1) - 35.0) < 1e-9 and abs((-5.0 + g * t2) - 35.0) < 1e-9
# ϑ² = ϑ₀² + 2gH ile bağımsız çapraz kontrol
assert abs((25 + 2 * g * H) ** 0.5 - 35.0) < 1e-9
""")

SOLUTIONS["ff-passing-point-twice"] = S(
    M(["Cisim L noktasından t₁ ve t₂ anlarında geçiyor: yukarı pozitif, Δy = ϑ₀t − ½gt² aynı yükseklik için iki kök verir.",
       "Köklerin toplamı: t₁ + t₂ = 2ϑ₀/g → ϑ₀ = g(t₁ + t₂)/2.",
       "Köklerin çarpımı: t₁·t₂ = 2y/g → y = ½·g·t₁·t₂ (L noktasının atış seviyesinden yüksekliği).",
       "Tepe: t_tepe = ϑ₀/g = (t₁ + t₂)/2; h_max = ϑ₀²/2g."],
      ["Atış seviyesi t = 0 anına karşılık gelir; t₁, t₂ atıştan itibaren geçen süreler", "Hava direnci ihmal"],
      ["t₁, t₂ farklı bir andan (ör. başka bir kronometre başlangıcıyla) ölçülmüşse önce zamanı atıştan başlat"],
      ["Tepe süresini t₂ − t₁ sanmak", "t'leri atıştan değil başka bir andan okumak"]),
    M(["Yörünge tepeye göre simetrik: aynı noktaya çıkış ve inişin ortası tepe anıdır.", "Tepe anı = iki geçişin tam ortası: (t₁ + t₂)/2.",
       "İki geçiş arasındaki süre t₂ − t₁, L'den tepeye gidip dönme süresidir; L'nin tepeden uzaklığı ½g((t₂ − t₁)/2)² olur."],
      ["Serbest düşme simetrisi"], ["Sadece aynı noktadan iki geçiş bilgisinde"], ["Aralığı (t₂ − t₁) tepeye çıkış süresi sanmak"]),
    M(["Tepe süresi (t₁+t₂)/2 ile ϑ₀ = g(t₁+t₂)/2 yaz.", "h_L = ½g·t₁·t₂ ile noktanın yüksekliğini anında bul; h_max = (g/8)(t₁+t₂)²."],
      ["Aynı noktadan iki geçiş (atış seviyesinden ölçülen süre)"], ["Zaman atıştan ölçülmeli"], ["Atış anını hesaba katmamak"]),
    M(["Tepeden serbest düşme yöntemi: L tepeden d = ½g((t₂−t₁)/2)² aşağıda; h_max = d + h_L yüksekliklerini topla."],
      ["Tepe anı bulunmuş"], ["Fazladan adım gerekir"], ["h_L'yi ayrıca bulmayı unutmak"]),
    "'Aynı noktadan 2. kez geçiyor' → simetri: tepe anı iki anın ortalaması. Atış seviyesinden yükseklik h = 5·t₁·t₂ (g = 10), ϑ₀ = 5(t₁+t₂).",
    "Düşey yukarı fırlatılan bir cisim, atıldıktan 2 s ve 6 s sonra aynı L noktasından geçiyor. İlk hızını, tepe noktasının yüksekliğini ve L noktasının atış noktasından yüksekliğini bulunuz. (g = 10 m/s²)",
    ["t_tepe = (2 + 6)/2 = 4 s → ϑ₀ = g·t_tepe = 40 m/s.", "h_max = ϑ₀²/(2g) = 1600/20 = 80 m.",
     "h_L = ½·g·t₁·t₂ = 5·2·6 = 60 m (kontrol: 40·2 − 5·4 = 60)."],
    "ϑ₀ = 40 m/s, h_max = 80 m, h_L = 60 m.",
    """
g = 10.0
t1, t2 = 2.0, 6.0
v0 = g * (t1 + t2) / 2
assert abs(v0 - 40.0) < 1e-9
h = lambda t: v0 * t - 0.5 * g * t * t
assert abs(h(t1) - h(t2)) < 1e-9          # gerçekten aynı nokta
assert abs(h(t1) - 0.5 * g * t1 * t2) < 1e-9 and abs(h(t1) - 60.0) < 1e-9
assert abs(v0 ** 2 / (2 * g) - 80.0) < 1e-9
assert abs(h((t1 + t2) / 2) - 80.0) < 1e-9   # tepe anı
""")

SOLUTIONS["ff-equal-interval-ratios"] = S(
    M(["Birim süre τ seç; ilk aralıkta alınan yol h₁ = ½gτ² olsun.",
       "n. aralıkta alınan yol h_n = ½gτ²[n² − (n−1)²] = (2n − 1)·h₁.",
       "Yollar 1 : 3 : 5 : 7 … ; ilk n aralıkta toplam yol n²·h₁.",
       "Verilen yol ya da oranla n'yi bul; toplam süre = n·τ."],
      ["ϑ₀ = 0 (durgun bırakılıyor)", "Aralıklar eşit ve ilk aralık bırakma anında başlıyor", "Hava direnci ihmal"],
      ["Aralıklar bırakma anından başlamıyorsa (ör. 1,5 s sonra) oran değişir", "İlk hız varsa geçerli değil"],
      ["Toplam yolu (1:4:9) aralık yolu (1:3:5) sanmak", "Eşit sürede eşit yol almış gibi düşünmek"]),
    M(["Hız sürekli arttığından her eşit zamanda alınan yol artar.", "Her aralıkta ortalama hız, bir öncekine göre sabit miktarda artar; yollar arasındaki fark sabit (2h₁) olur → tek sayılar."],
      ["Sabit ivme"], ["Yalnız nitel ilişki"], ["Sabit hız sanmak"]),
    M(["Yolları h₁ cinsinden 1, 3, 5, 7 … yaz.", "Verilen aralık yolundan h₁ = yol/(2n−1) hesapla; toplam yol = n²·h₁."],
      ["Bırakma anından itibaren eşit aralıklar"], ["Aralık tam sayı katı olmalı"], ["Aralık bırakma anından başlamıyorsa tablo uygulamak"]),
    None,
    "'Eşit zaman aralıklarında alınan yollar' + durgun bırakma → 1:3:5:7. Toplam yol sorusunda 1:4:9:16'ya geç.",
    "Durgun bırakılan bir cisim yere çarpmadan önceki son 1 saniyede 45 m yol alıyor. Cisim kaç saniyede ve kaç metreden düşmüştür? (g = 10 m/s²)",
    ["Birim süre 1 s: ilk saniyede h₁ = 5 m; n. saniyede 5(2n − 1) m.",
     "5(2n − 1) = 45 → n = 5 s.", "Toplam yol = n²·h₁ = 25·5 = 125 m."],
    "Düşme süresi 5 s, yükseklik 125 m.",
    """
g = 10.0
h = lambda t: 0.5 * g * t * t
n = 5
assert abs((h(n) - h(n - 1)) - 45.0) < 1e-9
assert abs(h(n) - 125.0) < 1e-9
# 1:3:5:7:9 örüntüsü
steps = [h(k) - h(k - 1) for k in range(1, 6)]
base = steps[0]
assert all(abs(steps[k] / base - (2 * (k + 1) - 1)) < 1e-9 for k in range(5))
""")

SOLUTIONS["ff-motion-graphs"] = S(
    M(["Pozitif yönü seç ve bütün grafiklerde aynı tut.",
       "a-t: ivme tüm hareket boyunca sabit −g (yukarı pozitif ise).",
       "ϑ-t: eğimi −g olan doğru; tepe noktasında eksenden geçer (ϑ = 0), kırılma yoktur.",
       "x-t: parabol; tepede eğim sıfır. ϑ-t altındaki alan yer değiştirmedir (eksen altı alan negatif)."],
      ["Serbest düşme; hava direnci ihmal", "Yön seçimi tutarlı"],
      ["Sekmeli harekette çarpma anında hız ani işaret değiştirir (ϑ-t'de düşey sıçrama)"],
      ["Yön seçimini grafikler arasında değiştirmek", "Eğim ile değeri karıştırmak", "Tepede a = 0 çizmek"]),
    M(["İvme sabit olduğu için ϑ-t grafiği tek bir doğrudur; yön değişse de eğim aynıdır.",
       "Hız işaret değiştirir ama ivme değişmez.", "Konum-zaman grafiğinin eğimi hızdır: tepede 0."],
      ["Serbest düşme"], ["Yalnız nitel okuma"], ["Hızın yön değişimini ivme yön değişimi sanmak"]),
    M(["Önce ϑ-t doğrusunu bul: ϑ₀ ve eğim −g. Sonra a-t'yi sabit yatay doğru olarak, x-t'yi ϑ-t'den (eğim = hız) çıkar.",
       "Alan: sıfır çizgisinin üstündeki alan yukarı yer değiştirme, altındaki aşağı."],
      ["Grafik doğrusal ϑ-t ile veriliyor"], ["Sekmede ayrı parçalar halinde çiz"], ["Alanı işaretsiz toplamak"]),
    None,
    "Grafik sorularında önce yön seçimini sabitle: ϑ-t = eğimi −g olan tek doğru; a-t = sabit; x-t = parabol. 'Tepede ivme sıfır / ϑ-t kırılır' = tuzak.",
    "Yukarı yönü pozitif seçerek yerden 20 m/s hızla düşey yukarı atılan cismin ϑ-t grafiğini çiziniz; tepeye çıkış süresini, grafikten tepe yüksekliğini ve 0–4 s aralığındaki toplam yer değiştirmeyi bulunuz.",
    ["ϑ(t) = 20 − 10t: eğim −10, t = 2 s'de ϑ = 0.",
     "0–2 s arasındaki alan = ½·2·20 = 20 m (tepe yüksekliği).",
     "2–4 s arasındaki alan = −20 m; toplam yer değiştirme 20 − 20 = 0 (cisim atış noktasına döner)."],
    "t_tepe = 2 s; h_max = 20 m; 0–4 s yer değiştirmesi 0; ivme tüm süre −10 m/s² sabit.",
    """
g = 10.0
v0 = 20.0
N = 40000
dt = 4.0 / N
v = lambda t: v0 - g * t
disp = sum(v((i + 0.5) * dt) * dt for i in range(N))
assert abs(disp) < 1e-6                     # 0-4 s toplam yer değiştirme 0
first = sum(v((i + 0.5) * dt) * dt for i in range(N // 2))
assert abs(first - 20.0) < 1e-6              # 0-2 s alan = tepe yüksekliği
# eğim her yerde -g (a-t sabit)
for t in (0.1, 1.0, 1.9, 2.0, 3.5):
    assert abs((v(t + 1e-3) - v(t)) / 1e-3 + g) < 1e-6
assert abs(v(2.0)) < 1e-12
""")

SOLUTIONS["ff-data-evidence"] = S(
    M(["Tabloyu eşit zaman aralıklarıyla oku; ardışık konum farklarını (Δy) hesapla.",
       "Farkların farkını (ikinci fark) al: sabit ise sabit ivmeli hareket; a = Δ²y/Δt².",
       "İlk fark sabit çıkarsa sabit hız, ikinci fark sabit çıkarsa sabit ivme olduğuna karar ver.",
       "Örüntüyü bozan değer varsa ikinci farkları sabitleyen değerle hatalı ölçümü belirle."],
      ["Zaman aralıkları eşit", "Yalnız yer çekimi etkisi varsayımı"],
      ["Ölçüm hatası küçükse ikinci fark tam sabit çıkmaz; tolerans içinde değerlendirilir"],
      ["Konum ile yer değiştirmeyi karıştırmak", "Birinci farkları sabit sanmak"]),
    M(["Konumlar eşit artmıyorsa hareket sabit hızlı değildir.", "Her aralıkta artışın aynı miktarda büyümesi hızın düzgün arttığını gösterir.",
       "Bir değeri çok farklı olan satır, ölçüm hatasının adayıdır."],
      ["Aynı deney koşulu"], ["Nitel yargı"], ["Tek bir satırdan genelleme yapmak"]),
    M(["Satırları h ∝ n² ile karşılaştır: y/n² sabit olmalı; sabit olmayan satır hatalıdır."],
      ["t = nΔt, ϑ₀ = 0"], ["Başlangıç anı sıfır değilse çalışmaz"], ["Başlangıç ölçümü sıfır olmayan tabloya uygulamak"]),
    M(["Grafik yöntemi: y-t² grafiği doğrusal olmalı; eğimi g/2'dir. Doğrunun dışında kalan nokta hatalıdır."],
      ["ϑ₀ = 0"], ["Grafik çizim zaman alır"], ["Eksen ölçeklerini yanlış seçmek"]),
    "Tabloda 'konum' görüyorsan ikinci farkı (veya y/n²'yi) hesapla; hatalı satır bu örüntüyü bozan satırdır.",
    "Bir fotokapı düzeneğinde 0,1 s aralıklarla ölçülen düşey konum değerleri (cm): 0; 4,9; 19,6; 44,1; 76,4; 122,5. Bir ölçüm hatalıdır. Hatalı değeri bulup doğrusunu yazınız ve g'yi hesaplayınız.",
    ["Birinci farklar: 4,9; 14,7; 24,5; 32,3; 46,1 → sabit değil, artıyor.",
     "İkinci farklar: 9,8; 9,8; 7,8; 13,8 → sabit olması gereken 9,8 yalnız ilk iki fark için sağlanıyor; 4. değer (76,4) bozuyor.",
     "Doğru değer 4,9·n² = 78,4 cm. g = Δ²y/Δt² = 9,8 cm / 0,01 s² = 980 cm/s² = 9,8 m/s²."],
    "Hatalı ölçüm 76,4 cm; doğrusu 78,4 cm; g = 9,8 m/s².",
    """
y = [0, 4.9, 19.6, 44.1, 76.4, 122.5]
d1 = [round(y[i + 1] - y[i], 6) for i in range(5)]
d2 = [round(d1[i + 1] - d1[i], 6) for i in range(4)]
assert d2 == [9.8, 9.8, 7.8, 13.8]
fixed = list(y); fixed[4] = 78.4
f1 = [fixed[i + 1] - fixed[i] for i in range(5)]
f2 = [f1[i + 1] - f1[i] for i in range(4)]
assert all(abs(x - 9.8) < 1e-9 for x in f2)
g = f2[0] / 100 / 0.1 ** 2   # cm -> m
assert abs(g - 9.8) < 1e-9
# y/n^2 sabit mi?
assert all(abs(fixed[n] / n ** 2 - 4.9) < 1e-9 for n in range(1, 6))
""")

# ============================ FİZ.11.1.3 ============================
SOLUTIONS["2d-horizontal-launch"] = S(
    M(["Hareketi iki bileşene ayır: yatayda sabit hız ϑₓ = ϑ₀, düşeyde ilk hızsız serbest düşme.",
       "Süreyi düşey hareketten bul: h = ½gt² → t = √(2h/g).",
       "Menzil x = ϑₓ·t.",
       "Çarpma hızı: ϑᵧ = g·t; ϑ = √(ϑₓ² + ϑᵧ²), yatayla açısı tanα = ϑᵧ/ϑₓ."],
      ["Başlangıç hızı tam yatay", "Hava direnci ihmal", "Yatayda ivme yok"],
      ["Rüzgâr ya da yatay kuvvet varsa yatayda ivme olur", "Başlangıç hızı yatay değilse (açılı) farklı çözüm"],
      ["Süreyi yatay hareketten bulmaya çalışmak", "Çarpma hızını yalnız düşey bileşen almak", "Bileşenleri skaler toplamak"]),
    M(["Yatay ve düşey hareketler birbirinden bağımsızdır: yatay hız düşme süresini etkilemez.",
       "Aynı yükseklikten yatay atılan ve serbest bırakılan cisimler aynı anda yere düşer.", "Menzil, hızın büyümesi ve düşme süresinin uzamasıyla artar."],
      ["Bileşenlerin bağımsızlığı"], ["Nicel sonuç için bağıntı gerekir"], ["Yatay hızı büyük olanın geç düştüğünü sanmak"]),
    M(["g = 10 için t = √(h/5): h = 5, 20, 45, 80 m → t = 1, 2, 3, 4 s.", "x = ϑ₀t; çarpma hızı için ϑᵧ = 10t, Pisagor; (3-4-5, 5-12-13 üçlülerine dikkat)."],
      ["g = 10 m/s²"], ["h bu değerlerde değilse tablo doğrudan uygulanmaz"], ["Üçlüyü yanlış eşleştirmek"]),
    None,
    "'Yatay hızla fırlatılıyor / masadan düşüyor' → t yalnız h'den: t = √(2h/g). Çarpma hızı sorusunda Pisagor + açı.",
    "20 m yüksekliğindeki bir platformdan bir top 15 m/s yatay hızla fırlatılıyor. Havada kalma süresini, menzili ve yere çarpma hızının büyüklüğünü bulunuz. (g = 10 m/s²)",
    ["t = √(2h/g) = √(2·20/10) = 2 s.", "x = ϑ₀·t = 15·2 = 30 m.", "ϑᵧ = g·t = 20 m/s; ϑ = √(15² + 20²) = 25 m/s."],
    "t = 2 s; menzil 30 m; çarpma hızı 25 m/s (yatayla tanα = 4/3).",
    """
g = 10.0
h, vx = 20.0, 15.0
# adım adım sayısal simülasyon (dt küçük)
dt = 1e-5
x = y = 0.0; vy = 0.0; t = 0.0
while y < h:
    vy += g * dt
    y += vy * dt
    x += vx * dt
    t += dt
assert abs(t - 2.0) < 1e-3
assert abs(x - 30.0) < 1e-2
assert abs((vx ** 2 + vy ** 2) ** 0.5 - 25.0) < 1e-2
# kapalı form
assert abs((2 * h / g) ** 0.5 - 2.0) < 1e-12
""")

SOLUTIONS["2d-angled-launch"] = S(
    M(["Hızı bileşenlerine ayır: ϑₓ = ϑ₀cosα, ϑᵧ = ϑ₀sinα (açı yatayla ölçülüyorsa).",
       "Düşey hareket: t_çıkış = ϑᵧ/g, h_max = ϑᵧ²/(2g); aynı seviyeye dönüşte t_uçuş = 2ϑᵧ/g.",
       "Yatay hareket: menzil = ϑₓ·t_uçuş.",
       "Tepe noktasında ϑᵧ = 0, hız yatay ve ϑₓ'e eşit (minimum hız); ivme hâlâ g aşağı."],
      ["Yer çekimi ivmesinden başka kuvvet yok", "Hava direnci ihmal", "Açı yatayla ölçülmüş (düşeyle ise sin/cos yer değiştirir)"],
      ["Yüksekten atışta t_uçuş ≠ 2ϑᵧ/g; tek denklem Δy = ϑᵧt − ½gt² kullanılır", "Rüzgârlı ortamda yatayda ivme olur"],
      ["sin ile cos'u karıştırmak", "Menzili ϑ₀·t almak", "Tepede hızı sıfır sanmak"]),
    M(["Düşey hareket yukarı atışla, yatay hareket sabit hızlı hareketle aynıdır; ikisi aynı sürede gerçekleşir.",
       "Tepe noktasında yalnız yatay hız kalır; ivme değişmez."],
      ["Bileşenlerin bağımsızlığı"], ["Nicel sonuç için bağıntı gerekir"], ["Tepede ivme sıfır demek"]),
    M(["Özel açıda hazır değerler: 37° → ϑₓ = 0,8ϑ₀, ϑᵧ = 0,6ϑ₀; 53° → ϑₓ = 0,6ϑ₀, ϑᵧ = 0,8ϑ₀; 30° → 0,87/0,5; 45° → eşit.",
       "Aynı seviyeye dönüşte: h_max = ϑᵧ²/20, t_uçuş = ϑᵧ/5, menzil = ϑₓ·ϑᵧ/5; tanα = 4h_max/menzil kontrolü."],
      ["Aynı seviyeye dönüş", "g = 10 m/s²"], ["Yerden yüksek atışta geçerli değil"], ["Açıyı düşeyden okumak"]),
    M(["Menzil formülüyle: menzil = ϑ₀²sin2α/g; tepe yüksekliği = ϑ₀²sin²α/(2g) — program dışı kısayol olarak yalnız doğrulama için."],
      ["Aynı seviyeye dönüş"], ["Programda bileşen yöntemi öğretilir; formül ezberi önerilmez"], ["Formülü yüksekten atışta kullanmak"]),
    "Açılı hız + 'tepe / menzil / uçuş süresi' → bileşenlere ayır. Tepe: ϑᵧ = 0; menzil: yatay hız × uçuş süresi. Açı yatayla mı düşeyle mi ölçülmüş, bak.",
    "Bir cisim yerden yatayla 53° açı yapacak şekilde 50 m/s hızla fırlatılıyor. Tepe noktasındaki hızı, maksimum yüksekliği, uçuş süresini ve menzili bulunuz. (g = 10 m/s², sin53° = 0,8, cos53° = 0,6)",
    ["ϑₓ = 50·0,6 = 30 m/s; ϑᵧ = 50·0,8 = 40 m/s.", "Tepede hız = ϑₓ = 30 m/s (yatay).", "t_çıkış = 40/10 = 4 s; h_max = 40²/20 = 80 m; t_uçuş = 8 s.",
     "Menzil = 30·8 = 240 m."],
    "Tepe hızı 30 m/s; h_max = 80 m; t = 8 s; menzil 240 m.",
    """
g = 10.0
v0, s, c = 50.0, 0.8, 0.6
vx, vy = v0 * c, v0 * s
assert abs(vx - 30) < 1e-9 and abs(vy - 40) < 1e-9
t_up = vy / g
assert abs(t_up - 4) < 1e-9
hmax = vy * t_up - 0.5 * g * t_up ** 2
assert abs(hmax - 80) < 1e-9
T = 2 * t_up
y_end = vy * T - 0.5 * g * T ** 2
assert abs(y_end) < 1e-9
assert abs(vx * T - 240) < 1e-9
# tanα = 4 h_max / menzil
assert abs(4 * hmax / (vx * T) - s / c) < 1e-9
""")

SOLUTIONS["2d-velocity-at-point"] = S(
    M(["Hareketin istenen anındaki ϑₓ'i bul: sabit, ϑ₀cosα.",
       "ϑᵧ'yi bul: ϑᵧ = ϑ₀sinα − g·t (yukarı pozitif); ya da konumdan ϑᵧ² = ϑ₀ᵧ² − 2g·y.",
       "Büyüklük: ϑ = √(ϑₓ² + ϑᵧ²).",
       "Yön: tanφ = |ϑᵧ|/ϑₓ (yatayla açı); ϑᵧ > 0 ise yukarı, < 0 ise aşağı doğru."],
      ["Yalnız yer çekimi etkisi", "Bileşenler eksenler boyunca"],
      ["Hız vektörü her an yörüngeye teğettir; büyüklük aynı seviyelerde eşit"],
      ["Bileşenleri doğrudan toplamak (Pisagor gerekir)", "ϑᵧ işaretini karıştırmak"]),
    M(["Hız vektörü yörüngeye teğettir; yatay bileşeni değişmez, düşey bileşeni her saniye 10 m/s azalır.",
       "Hızın yatayla 45° yapması, ϑᵧ'nin büyüklükçe ϑₓ'e eşit olduğu an demektir."],
      ["Serbest düşme bileşenleri"], ["Nitel yorum"], ["Düşey hızı sabit sanmak"]),
    M(["Yatayla belirli açı koşulunda |ϑᵧ| = ϑₓ·tanφ yaz; zamanı bu eşitlikten bul.", "Aynı seviyelerde hız büyüklüğü eşit: yukarıda da aşağıda da √(ϑₓ² + ϑᵧ²) aynı."],
      ["Aynı seviye karşılaştırması"], ["Farklı seviyede büyüklük değişir"], ["Seviye farkını gözardı etmek"]),
    None,
    "Hız soruları 'bileşenler + Pisagor'. 'Yatayla 45°' = |ϑᵧ| = ϑₓ. Yatay bileşeni her an sabit tut.",
    "Yerden yatayla 53° açıyla 50 m/s hızla fırlatılan cismin hızı hareketin hangi anlarında yatayla 45° yapar? O anlardaki hızın büyüklüğü nedir? (g = 10 m/s², sin53° = 0,8, cos53° = 0,6)",
    ["ϑₓ = 30 m/s, ϑᵧ₀ = 40 m/s.", "45° için |ϑᵧ| = 30 m/s: 40 − 10t = ±30 → t = 1 s (yükselirken) ve t = 7 s (inerken).",
     "ϑ = √(30² + 30²) = 30√2 ≈ 42,4 m/s (iki anda da)."],
    "t = 1 s ve t = 7 s; hız büyüklüğü 30√2 ≈ 42,4 m/s.",
    """
import math
g = 10.0
vx, vy0 = 30.0, 40.0
for t in (1.0, 7.0):
    vy = vy0 - g * t
    assert abs(abs(vy) - vx) < 1e-9
    assert abs(math.degrees(math.atan2(abs(vy), vx)) - 45.0) < 1e-9
    assert abs(math.hypot(vx, vy) - 30 * math.sqrt(2)) < 1e-9
# aynı seviyede (y eşit) hız büyüklükleri eşit
y = lambda t: vy0 * t - 0.5 * g * t * t
assert abs(y(1.0) - y(7.0)) < 1e-9
""")

SOLUTIONS["2d-component-data"] = S(
    M(["x(t) tablosunda ardışık farkları (Δx) al: eşitse yatay hareket sabit hızlıdır, ϑₓ = Δx/Δt.",
       "y(t) tablosunda birinci farklar artıyor, ikinci farklar sabit (Δ²y) ise düşey hareket sabit ivmelidir: a = Δ²y/Δt².",
       "Eksik değeri örüntüyü sürdürerek (x'te aynı fark, y'de ikinci farkı koruyarak) bul.",
       "g'yi hesaplayıp bileşke hareketin yatayda sabit hızlı + düşeyde serbest düşme olduğunu yorumla."],
      ["Eşit aralıklı zaman", "Konumlar aynı eksen sisteminde"],
      ["Ölçüm belirsizliği varsa tam sabit çıkmaz; yaklaşık eşitlik aranır"],
      ["Konumu fark almadan yorumlamak", "Yatayda da ivme olduğunu sanmak"]),
    M(["Eşit sürede eşit yatay yer değiştirme → ivme yok; yatay kuvvet yok.", "Düşey yer değiştirmeler 1:3:5 gibi artıyorsa düşeyde ilk hızsız serbest düşme vardır."],
      ["Bileşenlerin bağımsızlığı"], ["Nitel okuma"], ["Hareketi tek eksenli düşünmek"]),
    M(["x sütununda farkın sabit olduğunu bir bakışta kontrol et; y sütununda y/n² sabit mi (ϑᵧ₀ = 0 ise) bak."],
      ["Düşeyde ilk hız sıfır"], ["Düşey ilk hız varsa y/n² sabit olmaz"], ["Başlangıç durumunu bilmeden uygulamak"]),
    None,
    "Veride 'x farkı sabit, y ikinci farkı sabit' görürsen yatay: sabit hız, düşey: sabit ivme. Eksik hücre = örüntüyü sürdür.",
    "Stroboskopik fotoğrafta 0,2 s aralıklarla çekilen bir topun konumları (x; y düşey aşağı ölçülmüş, m): (0; 0), (1,2; 0,2), (2,4; 0,8), (3,6; 1,8), (4,8; 3,2), (?; ?). Yatay hızı, düşey ivmeyi ve eksik konumu bulunuz.",
    ["Δx = 1,2 m her aralıkta (sabit) → ϑₓ = 1,2/0,2 = 6 m/s.",
     "Δy: 0,2; 0,6; 1,0; 1,4 → ikinci fark 0,4 m sabit → a = 0,4/0,2² = 10 m/s² (g).",
     "Sonraki Δy = 1,4 + 0,4 = 1,8 → y = 5,0 m; x = 4,8 + 1,2 = 6,0 m."],
    "ϑₓ = 6 m/s (sabit), düşey a = 10 m/s²; eksik konum (6,0; 5,0) m.",
    """
dt = 0.2
x = [0, 1.2, 2.4, 3.6, 4.8]
y = [0, 0.2, 0.8, 1.8, 3.2]
dx = [x[i + 1] - x[i] for i in range(4)]
assert all(abs(d - 1.2) < 1e-9 for d in dx)
assert abs(dx[0] / dt - 6.0) < 1e-9
dy = [y[i + 1] - y[i] for i in range(4)]
d2 = [dy[i + 1] - dy[i] for i in range(3)]
assert all(abs(d - 0.4) < 1e-9 for d in d2)
assert abs(d2[0] / dt ** 2 - 10.0) < 1e-9
x5, y5 = x[-1] + dx[-1], y[-1] + dy[-1] + d2[-1]
assert abs(x5 - 6.0) < 1e-9 and abs(y5 - 5.0) < 1e-9
# kapalı form: y = 5 t^2, t = 5 dt
assert abs(5 * (5 * dt) ** 2 - y5) < 1e-9
""")

SOLUTIONS["2d-launch-onto-incline-or-steps"] = S(
    M(["Eğik düzlemin tepesinden yatay ϑ₀ ile atılan cisim için yatay x = ϑ₀t, düşey y = ½gt² (aşağı).",
       "Çarpma koşulu: cisim düzlem üzerinde, yani y/x = tanθ.",
       "½gt²/(ϑ₀t) = tanθ → t = 2ϑ₀tanθ/g.",
       "x ve y'yi bul; düzlem boyunca uzaklık d = x/cosθ. Basamaklarda aynı mantıkla her basamağın kenar koşulunu sına."],
      ["Başlangıç hızı yatay", "Düzlem eğimi sabit", "Hava direnci ihmal"],
      ["Başlangıç hızı yatay değilse koşul y = ϑᵧt − ½gt² biçiminde değişir", "Basamaklarda hangi basamağın koşulu sağlandığı iteratif sınanır"],
      ["Düşey ve yatay yer değiştirmeyi aynı bağıntıya karıştırmak", "Açıyı yanlış ölçmek"]),
    M(["Yörünge parabol, düzlem doğru: kesişimleri bulunur.", "Düzlem dikse (θ→90°) süre sonsuza gitmez ama doğrudan yere düşer; koşul tanθ ile uyumludur.",
       "Basamakta cisim, yatay yer değiştirmesi kenar mesafesini geçmeden önce düşey olarak basamak yüksekliğini geçmişse bir sonraki basamağa gider."],
      ["Geometrik koşul"], ["Nitel kontrol"], ["Hep ilk basamağa düşeceğini düşünmek"]),
    M(["37° için tanθ = 3/4: t = 1,5ϑ₀/g; 45° için t = 2ϑ₀/g. Süreyi buradan hızlı bul."],
      ["İlk hız yatay, düzlem sürekli"], ["Düzlem yetmeyecek kadar kısa ise yere düşer"], ["Düzlem uzunluğunu kontrol etmemek"]),
    None,
    "Eğik düzleme çarpma = y/x = tanθ koşulu. Süre: t = 2ϑ₀tanθ/g. Basamaklarda kenar mesafelerini sınayarak ilerle.",
    "37° eğimli uzun bir düzlemin tepesinden bir top yatay olarak 15 m/s hızla atılıyor. Topun düzleme çarpma süresini ve çarptığı noktanın atış noktasına olan uzaklığını bulunuz. (g = 10 m/s², tan37° = 0,75, cos37° = 0,8)",
    ["y/x = tanθ: 5t²/(15t) = 0,75 → t = 2,25 s.", "x = 15·2,25 = 33,75 m; y = 5·2,25² = 25,3125 m.",
     "Düzlem boyunca uzaklık d = x/cos37° = 33,75/0,8 = 42,1875 m (kontrol: √(x² + y²))."],
    "t = 2,25 s; d ≈ 42,19 m.",
    """
import math
g = 10.0
v0, tan_t, cos_t = 15.0, 0.75, 0.8
t = 2 * v0 * tan_t / g
assert abs(t - 2.25) < 1e-12
x, y = v0 * t, 0.5 * g * t * t
assert abs(y / x - tan_t) < 1e-12
d1 = x / cos_t
d2 = math.hypot(x, y)
assert abs(d1 - d2) < 1e-9 and abs(d1 - 42.1875) < 1e-9
""")

SOLUTIONS["2d-component-graphs"] = S(
    M(["Yatay bileşen: ϑₓ-t yatay doğru (sabit), a = 0, x-t eğimi sabit doğru.",
       "Düşey bileşen: ϑᵧ-t eğimi −g (yukarı pozitif) olan doğru; aᵧ-t sabit −g; y-t parabol.",
       "Tepede ϑᵧ = 0 (ϑᵧ-t eksenini keser), ϑₓ yine aynı değerde kalır.",
       "Seçeneklerde yatay ve düşey grafikleri ayrı değerlendir."],
      ["Yatayda kuvvet yok", "Hava direnci ihmal"],
      ["Rüzgâr ya da direnç varsa yatay ϑ-t sabit olmaz"],
      ["Yatay grafiğe de eğim koymak", "Yön seçimini grafikler arasında tutarsız yapmak"]),
    M(["Yatayda net kuvvet sıfır → hız sabit; düşeyde net kuvvet ağırlık → sabit ivme.", "Bileşenler bağımsız olduğundan grafikler de bağımsız çizilir."],
      ["Bileşenlerin bağımsızlığı"], ["Nitel okuma"], ["Tepede yatay hızın sıfır olduğunu sanmak"]),
    M(["Yatay: 'sabit doğru' — varsa bu seçeneği ara; düşey: eğimi −g olan düz çizgi. Diğer seçenekleri ele."],
      ["Standart iki boyutlu hareket"], ["Sekme ya da başka kuvvet yoksa"], ["Eğimi kontrol etmeden seçmek"]),
    None,
    "ϑₓ-t: yatay doğru; ϑᵧ-t: −g eğimli doğru; aₓ = 0, aᵧ = −g. Tepede yalnız ϑᵧ sıfır olur.",
    "Yerden ϑ₀ = 50 m/s hızla yatayla 53° açıyla atılan cismin ϑₓ-t, ϑᵧ-t ve aᵧ-t değerlerini 0, 2, 4, 6, 8 s için hesaplayıp grafiklerin türünü yorumlayınız. (sin53° = 0,8, cos53° = 0,6)",
    ["ϑₓ = 30 m/s her an sabit (grafik yatay doğru).", "ϑᵧ = 40 − 10t: 40, 20, 0, −20, −40 (eğim −10, t = 4 s'de ekseni keser).",
     "aᵧ = −10 m/s² her an sabit; aₓ = 0."],
    "ϑₓ sabit (yatay doğru); ϑᵧ doğrusal azalan, tepede (4 s) sıfır; aᵧ = −10 sabit.",
    """
g = 10.0
vx0, vy0 = 30.0, 40.0
ts = [0, 2, 4, 6, 8]
vx = [vx0 for _ in ts]
vy = [vy0 - g * t for t in ts]
ay = [(vy[i + 1] - vy[i]) / (ts[i + 1] - ts[i]) for i in range(4)]
assert vx == [30.0] * 5
assert vy == [40.0, 20.0, 0.0, -20.0, -40.0]
assert all(abs(a + g) < 1e-12 for a in ay)
assert vy[2] == 0 and vx[2] != 0   # tepede yalnız düşey bileşen sıfır
""")

# ============================ FİZ.11.1.4 ============================
SOLUTIONS["newton1-inertia"] = S(
    M(["Durumu aracın (zeminin) gözlemcisine göre tanımla; cisme etki eden kuvvetleri belirle.",
       "Net kuvvet sıfırsa cisim durumunu korur (durgun ya da sabit hızlı): Newton'un 1. yasası.",
       "Araç ani fren yaparsa cisimlere ek kuvvet etki etmez; araç yavaşlar, cisim eski hızını korumaya çalışır → araca göre öne gider.",
       "Sonuç: 'itme' değil, 'eylemsizlik' (hareket durumunu koruma isteği)."],
      ["Eylemsiz (ivmesiz) gözlemciye göre değerlendirme", "Net kuvvet sıfır ya da etkisi bilinen"],
      ["Sayısal çözüm gerektirmez; ivmeli çerçevede 'sanal kuvvet' anlatımı müfredat dışıdır"],
      ["Eylemsizliği bir kuvvet sanmak", "Hareket için kuvvet gerektiğini düşünmek"]),
    M(["Hareketin sürmesi için kuvvet gerekmez; hızın değişmesi için kuvvet gerekir.", "Kütle büyükse eylemsizlik büyüktür: aynı kuvvet daha küçük ivme verir.",
       "Masa örtüsü çekilince tabaklar kısa temas süresinde hız kazanamaz, yerinde kalır."],
      ["Newton'un 1. yasası"], ["Nitel"], ["Impetus (itki) yanılgısı"]),
    M(["Seçenekte 'cismi öne iten kuvvet' ya da 'hareketi sürdüren kuvvet' görürsen ele; doğru seçenek net kuvvet = 0 ya da eylemsizlik ifadesidir."],
      ["Kavramsal sorular"], ["Hesaplı sorulara uygulanmaz"], ["Hızlı eleme yapıp ifadeyi okumamak"]),
    None,
    "'Savruluyor / yerinde kalıyor / sabit hızla gidiyor' → eylemsizlik ve net kuvvet sıfır. Hareketi sürdüren kuvvet diye bir şey yoktur.",
    "Düz yolda bir araç 10 m/s hızla giderken ani fren yapıp 1 s'de 2 m/s hıza düşüyor. Aracın sürtünmesiz zeminindeki kutu araç içinde nasıl hareket eder? 1 s sonunda araca göre ne kadar öne gider? Sabit hızla giden aracta bileşke kuvvet nedir?",
    ["Kutuya yatay kuvvet etki etmez (sürtünmesiz) → hızı 10 m/s kalır.", "Araç hızı 10'dan 2'ye düşüyor (a = −8 m/s²); araca göre kutunun hızı 8 m/s.",
     "1 s'de araca göre kayma = ½·8·1² = 4 m.", "Araç sabit hızla gidiyorsa a = 0 → bileşke kuvvet 0."],
    "Kutu hızını korur, araca göre 4 m öne gider; sabit hızlı araçta bileşke kuvvet sıfırdır.",
    """
v0, v1, T = 10.0, 2.0, 1.0
a_car = (v1 - v0) / T
x_car = v0 * T + 0.5 * a_car * T ** 2
x_box = v0 * T            # net kuvvet yok -> hız sabit
assert abs((x_box - x_car) - 4.0) < 1e-9
# sabit hız -> a = 0 -> F_net = m a = 0
m = 3.0
assert m * 0.0 == 0.0
""")

SOLUTIONS["newton2-f-m-a-relations"] = S(
    M(["Tablo ya da grafikte bilinen satırlardan a = F_net/m ile ilişki türünü belirle (F∝a, m∝1/a).",
       "Kütle sabitken a ∝ F; kuvvet sabitken a ∝ 1/m. İki değişken birlikte değişiyorsa oranla.",
       "Eksik değeri oran-orantıyla ya da a = F_net/m ile bul. Sürtünme varsa uygulanan kuvvet değil F_net kullanılır.",
       "F-a grafiğinde eğim m (a-F grafiğinde 1/m); sürtünmeli grafik a = 0 aralığını ve eksen kesişimini gösterir."],
      ["Sabit kütle ve sabit kuvvet ayrı ayrı değiştirilmiş veriler", "Kuvvet doğrultusunda hareket"],
      ["Sürtünmeli ortamda F-a grafiği orijinden geçmez (eşik)"],
      ["Uygulanan kuvveti bileşke kuvvet sanmak", "Kütle artınca ivmenin arttığını düşünmek", "Eğimin anlamını yanlış okumak"]),
    M(["Aynı kuvvet daha büyük kütleye daha küçük ivme verir (eylemsizlik).", "Sürtünme uygulanan kuvvetin bir kısmını harcar; ivmeyi bileşke belirler."],
      ["Newton'un 2. yasası"], ["Nitel yorum"], ["Kütle-ivme doğrusal sanmak"]),
    M(["Tabloda a/F ya da a·m değerlerini sabit mi diye bak: a·m = F_net sabit kalıyorsa sürtünmesiz; kaymıyorsa eşik değerini çıkar."],
      ["Tablo verisi"], ["Kuvvet-ivme birlikte değişen satırlarda oran bakılır"], ["Satırları karıştırmak"]),
    M(["Grafik yöntemi: F-a doğrusunun eğimi m, a eksenini kestiği noktaya göre sürtünme kuvveti ya da eşik değeri."],
      ["Doğrusal grafik"], ["Eğrisel grafiklerde farklı yorum"], ["Eksenleri karıştırmak"]),
    "F, m, a üçlüsünde 'iki değişkenin biri sabit' arar: oranla. Sürtünme varsa a = (F − f)/m ve a = 0 aralığı vardır.",
    "Yatay zeminde bir cisme uygulanan F kuvveti ve ölçülen ivme değerleri: F = 2, 4, 6, 8, 10 N için a = 0, 0, 1, 2, 3 m/s². Cismin kütlesini ve kinetik sürtünme kuvvetini bulunuz. F = 14 N için ivme ne olur?",
    ["Hareket F > 4 N'dan sonra başlıyor: maksimum statik sürtünme ≈ kinetik 4 N (6 N'da a = 1: (6 − f)/m = 1).",
     "F: 6 → 8 → 10 için a: 1 → 2 → 3; ΔF/Δa = 2 N/(m/s²) = m → m = 2 kg.",
     "6 = f + 2·1 → f_k = 4 N. F = 14: a = (14 − 4)/2 = 5 m/s²."],
    "m = 2 kg; f_k = 4 N; F = 14 N için a = 5 m/s².",
    """
F = [6, 8, 10]
a = [1, 2, 3]
m = (F[2] - F[0]) / (a[2] - a[0])
assert abs(m - 2.0) < 1e-12
fk = F[0] - m * a[0]
assert abs(fk - 4.0) < 1e-12
assert all(abs((F[i] - fk) / m - a[i]) < 1e-12 for i in range(3))
assert abs((14 - fk) / m - 5.0) < 1e-12
# eşik: F <= 4 N için hareket yok
assert all(f <= fk for f in (2, 4))
""")

SOLUTIONS["newton3-action-reaction"] = S(
    M(["Etkileşimi 'A cismi B cismine kuvvet uygular' diliyle yaz; çift = 'B cismi A'ya aynı büyüklükte zıt yönlü kuvvet uygular'.",
       "Çiftin iki kuvveti farklı cisimlere etki eder; aynı türdendir (ağırlığın tepkisi Dünya'ya uygulanan çekim kuvvetidir).",
       "Büyüklükleri her zaman eşit; ivmeleri kütlelerine ters orantılıdır.",
       "Aynı cisme etki eden zıt kuvvetler (ör. ağırlık–normal kuvvet) denge kuvvetidir, etki-tepki çifti değildir."],
      ["Temaslı ya da uzaktan etkileşim (kütle çekimi dahil)"],
      ["Çiftin kuvvetleri farklı cisimlere uygulandığı için birbirini dengelemez"],
      ["Ağırlık ve normal kuvveti etki-tepki sanmak", "Büyük kütleli cisme daha büyük kuvvet atamak", "Kuvvetin hangi cisme etki ettiğini belirtmemek"]),
    M(["Kuvvet tek cisimli bir şey değil, iki cisim arasındaki etkileşimdir; her etkileşimde iki kuvvet doğar.", "Çarpışmada kamyon da otomobil de birbirine eşit kuvvet uygular; sonucu kütleler (ivmeler) belirler."],
      ["Newton'un 3. yasası"], ["Nitel"], ["Kuvvet-ivme-kütle karıştırmak"]),
    M(["Çift testi: 'aynı büyüklük, zıt yön, farklı cisim, aynı tür' dörtlüsünü sına; biri tutmuyorsa çift değildir."],
      ["Seçenekler arasında eleme"], ["Karmaşık sistemlerde cisimleri dikkatli adlandır"], ["Dörtlü testi yarım yapmak"]),
    None,
    "Çift sorularında 'kim kime' cümlesini kur. Aynı cisme etki eden iki kuvvet asla etki-tepki çifti değildir.",
    "10 000 kg kütleli bir kamyon ile 1 000 kg kütleli bir otomobil çarpışıyor. Çarpışma anında birbirlerine uyguladıkları kuvvetleri ve ivmelerinin oranını karşılaştırınız. Masada duran kitabın ağırlığının tepki kuvveti nedir?",
    ["Etki-tepki: F(kamyon→otomobil) = F(otomobil→kamyon) = F (zıt yönlü).", "a = F/m: a_otomobil/a_kamyon = m_kamyon/m_otomobil = 10.",
     "Kitabın ağırlığı Dünya'nın kitaba çekimidir; tepkisi kitabın Dünya'yı çekmesidir. Masanın kitaba normal kuvveti ağırlığın tepkisi değildir; ikisi aynı cisme etki eder."],
    "Kuvvetler eşit büyüklükte; otomobilin ivmesi kamyonunkinin 10 katı. Ağırlığın tepkisi: kitabın Dünya'ya uyguladığı çekim kuvveti.",
    """
F = 5.0e5
m_truck, m_car = 10000.0, 1000.0
a_truck, a_car = F / m_truck, F / m_car
assert abs(a_car / a_truck - 10.0) < 1e-9
# momentumun korunumuyla uyumlu: m1 a1 = m2 a2 (eşit büyüklükte kuvvet)
assert abs(m_truck * a_truck - m_car * a_car) < 1e-6
# kitap masada: ağırlık ve normal kuvvet aynı cisme etki eder -> toplam bileşke 0
m, g = 2.0, 10.0
N, G = m * g, m * g
assert abs(N - G) < 1e-12
""")

SOLUTIONS["net-force-motion-state"] = S(
    M(["Cismin ilk hız yönünü ve bileşke kuvvet yönünü karşılaştır; ivme yönü bileşke kuvvet yönündedir.",
       "Hız ile ivme aynı yöndeyse cisim hızlanır; zıt yöndeyse yavaşlar (ve gerekirse durup geri döner); dik ise yön değiştirir.",
       "Bileşke kuvvet sıfırsa sabit hızla (ya da durgun) kalır.",
       "Gerekirse ϑ(t) = ϑ₀ + a·t ile duruş anını bul."],
      ["Bileşke kuvvet sabit", "Doğrusal hareket"],
      ["Değişken kuvvette anlık hareket yorumu yapılır"],
      ["Cismin her zaman kuvvet yönünde gittiğini sanmak", "Hız yönünü ivme yönüyle karıştırmak"]),
    M(["Kuvvet hızı değiştirir; hızın yönünü belirlemez.", "Zıt yönlü kuvvet hızı önce azaltır, sıfır olunca cisim ters yönde hızlanmaya başlar."],
      ["Newton'un 2. yasası"], ["Nitel"], ["Kuvveti hız gibi düşünmek"]),
    M(["İşaret testi: v·a > 0 → hızlanma; v·a < 0 → yavaşlama; dik → doğrultu değişimi."],
      ["Doğrusal hareket ya da vektör bileşenleri"], ["Vektörlerde bileşen bazında düşünmek gerekir"], ["Bileşenleri karıştırmak"]),
    None,
    "Tablo/vektör sorularında 'kuvvet yönü = ivme yönü'; hız yönüyle aynıysa hızlanır, zıtsa yavaşlar. Durma sonrası yön değişir.",
    "Kütlesi 1 kg olan bir cisim +x yönünde 3 m/s hızla hareket ederken ona −x yönünde 2 N'luk sabit bileşke kuvvet uygulanıyor. Cisim nasıl bir hareket yapar? Ne zaman durur, 3. saniyedeki hızı nedir?",
    ["a = F/m = −2 m/s²; v ile a zıt → yavaşlar.", "Duruş: 3 − 2t = 0 → t = 1,5 s.", "t = 3 s'de ϑ = 3 − 6 = −3 m/s: cisim −x yönünde hareket ediyor (hızlanıyor)."],
    "1,5 s'ye kadar yavaşlar, 1,5 s'de durur, sonra −x yönünde hızlanır; ϑ(3 s) = −3 m/s.",
    """
m, F, v0 = 1.0, -2.0, 3.0
a = F / m
t_stop = -v0 / a
assert abs(t_stop - 1.5) < 1e-12
v = lambda t: v0 + a * t
assert v(3.0) == -3.0
state = lambda t: 'hızlanıyor' if v(t) * a > 0 else 'yavaşlıyor'
assert state(1.0) == 'yavaşlıyor' and state(2.0) == 'hızlanıyor'
""")

# ============================ FİZ.11.1.5 ============================
SOLUTIONS["fbd-identify-forces"] = S(
    M(["Sistemi (cismi) seç ve diğer her şeyden zihinsel olarak ayır.",
       "Uzaktan etki eden kuvveti çiz: ağırlık (Dünya'nın çekimi), cismin merkezinden aşağı.",
       "Cismin temas ettiği her yüzey/ip için ayrı kuvvet ara: normal kuvvet (yüzeye dik), sürtünme (yüzeye paralel), gerilme (ip boyunca, ip cismi kendi yönünde çeker).",
       "Hareket yönünde ya da merkezcil 'ayrı kuvvet' çizme; cismin başka cisme uyguladığı kuvvetleri ve tepkileri diyagrama koyma."],
      ["Cisim tek başına çizilmiş", "Temas ve uzaktan etkiler tek tek sayılmış"],
      ["Çok cisimli sistemde her cisim için ayrı diyagram gerekir"],
      ["Tepki kuvvetini ekleyip çift saymak", "Normal ya da sürtünmeyi unutmak", "Hareket yönünde ayrı 'hareket kuvveti' çizmek"]),
    M(["Her kuvvetin bir 'uygulayıcısı' (Dünya, yüzey, ip, el) olmalıdır; uygulayıcısı olmayan ok çizilmez.", "Hız ve ivme kuvvet değildir; ok olarak çizilmez."],
      ["Temas/alan kuvvetleri"], ["Nitel"], ["Uygulayıcısı olmayan kuvvet çizmek"]),
    M(["Temas taraması: cismin etrafını dolaş, değdiği her nesneyi say; üstüne ağırlığı ekle. Seçeneklerde kuvvet sayısını karşılaştır."],
      ["Standart çizimler"], ["Alan kuvvetleri (ör. elektrik) bu ünitede yok"], ["Taramayı yarıda bırakmak"]),
    None,
    "Diyagramda toplam kuvvet sayısı = (temas edilen nesne sayısı) + ağırlık. 'Hareket yönünde kuvvet' ya da 'merkezcil kuvvet' oku ekleyen seçenek yanlıştır.",
    "Yatay pürüzlü bir zeminde bir kutu, yatay bir iple çekilerek sabit hızla sürükleniyor. Kutuya etki eden kuvvetleri sayınız ve büyüklükleri arasındaki ilişkiyi yazınız (m = 4 kg, ip gerilmesi 12 N).",
    ["Temas: zemin (normal + sürtünme), ip (gerilme); uzaktan: ağırlık → toplam 4 kuvvet.",
     "Düşey: N = G = m·g = 40 N.", "Sabit hız → net kuvvet sıfır: yatayda f = T = 12 N (hareket yönünde ayrı kuvvet yok)."],
    "Dört kuvvet: ağırlık 40 N (aşağı), normal 40 N (yukarı), gerilme 12 N (ileri), sürtünme 12 N (geri).",
    """
m, g, T = 4.0, 10.0, 12.0
forces = {'agirlik': (0.0, -m * g), 'normal': (0.0, m * g), 'gerilme': (T, 0.0), 'surtunme': (-T, 0.0)}
assert len(forces) == 4
fx = sum(f[0] for f in forces.values())
fy = sum(f[1] for f in forces.values())
assert abs(fx) < 1e-12 and abs(fy) < 1e-12      # sabit hız: net kuvvet sıfır
""")

SOLUTIONS["fbd-equilibrium-tension"] = S(
    M(["Düğüm noktasını (ya da cismi) seç ve üzerindeki ip kuvvetlerini ve ağırlığı çiz.",
       "Her ip kuvvetini yatay ve düşey bileşenlerine ayır (açı yatayla ise yatay = T·cosα, düşey = T·sinα).",
       "Denge: ΣFₓ = 0 ve ΣFᵧ = 0 yaz.",
       "İki bilinmeyenli denklem takımını çöz; makaradan geçen ipin her yerinde gerilme aynıdır."],
      ["Cisim dengede (ivme sıfır)", "İp kütlesiz, makara sürtünmesiz", "Kuvvetler noktasal cisimde kesişiyor (tork yok)"],
      ["Çubuk/kaldıraç içeren tork dengesi 12. sınıf konusudur"],
      ["sin ile cos'u karıştırmak", "Kuvvetölçerin iki ucundaki ağırlıkları toplamak", "Açıyı düşeyle ölçülmüş sanmak"]),
    M(["Yatay bileşenler birbirini götürmeli; düşey bileşenlerin toplamı ağırlığı taşımalı.", "İp yatay yakına yaklaştıkça gerilme çok büyür (açı küçüldükçe T = G/(2sinα))."],
      ["Denge"], ["Nitel"], ["Gerilmenin ağırlıktan hep küçük olduğunu sanmak"]),
    M(["Lami teoremi (üç kuvvet dengesi): her kuvvet, karşısındaki iki kuvvet arasındaki açının sinüsüyle orantılı. 37°–53° gibi özel açılarda oranlar 3:4:5'tir.", "3-4-5 düzeninde gerilmeler ağırlığın 0,6 ve 0,8 katıdır."],
      ["Üç kuvvet, dengede, eş düzlemli"], ["Üçten fazla kuvvet varsa uygulanmaz"], ["Açıları yanlış eşleştirmek"]),
    None,
    "Dengede asılı → bileşen denklemleri. 37–53–90 özel üçgeni ya da simetrik iplerde T = G/(2sinα) kısayolu aranır.",
    "5 kg'lık bir lamba, yatayla soldan 37°, sağdan 53° açı yapan iki iple tavana asılıdır. İp gerilmelerini bulunuz. (g = 10 m/s², sin37° = 0,6, cos37° = 0,8)",
    ["Yatay: T₁cos37° = T₂cos53° → 0,8T₁ = 0,6T₂ → T₂ = (4/3)T₁.",
     "Düşey: T₁sin37° + T₂sin53° = m·g → 0,6T₁ + 0,8·(4/3)T₁ = 50 → (5/3)T₁ = 50 → T₁ = 30 N.", "T₂ = 40 N."],
    "T₁ = 30 N, T₂ = 40 N.",
    """
import math
m, g = 5.0, 10.0
s37, c37, s53, c53 = 0.6, 0.8, 0.8, 0.6
T1 = m * g * 0.6          # çözüm: 3/5 mg
T2 = m * g * 0.8
assert abs(T1 * c37 - T2 * c53) < 1e-9
assert abs(T1 * s37 + T2 * s53 - m * g) < 1e-9
assert abs(T1 - 30) < 1e-9 and abs(T2 - 40) < 1e-9
# Lami: T1/sin(90+53) ... açılar: ağırlığın karşısındaki açı 90°, T1'in karşısındaki 90+53=143°? kontrol 3-4-5
assert abs(T1 / (m * g) - 0.6) < 1e-12 and abs(T2 / (m * g) - 0.8) < 1e-12
# makara: aynı ip her yerde aynı gerilme -> iki cisim dengede
m1, m2 = 3.0, 3.0
assert abs(m1 * g - m2 * g) < 1e-12
""")

SOLUTIONS["frictionless-incline"] = S(
    M(["Eğik düzleme paralel ve dik eksenler seç; ağırlığı mg·sinθ (paralel) ve mg·cosθ (dik) bileşenlerine ayır.",
       "Dik eksen dengede: N = m·g·cosθ (ek dik kuvvet yoksa).",
       "Paralel eksen: m·g·sinθ = m·a → a = g·sinθ (kütle sadeleşir). Ek kuvvet varsa net paralel kuvvet kullanılır.",
       "Hız/süre için sabit ivmeli hareket bağıntıları: ϑ² = 2a·s, s = ½at²."],
      ["Sürtünme yok", "Düzlem sabit ve sert", "θ yatayla ölçülür"],
      ["Ek bir kuvvet (ip, itme) varsa a = g·sinθ geçersiz", "Sürtünmeli düzlemde farklı"],
      ["sin ile cos'u karıştırmak", "N = mg sanmak", "İvmeyi kütleye bağımlı sanmak"]),
    M(["Düzleme paralel bileşen, ağırlığın yalnız 'kaydıran' kısmıdır; dik bileşeni düzlem taşır.", "θ = 0 → a = 0; θ = 90° → a = g (serbest düşme) uç durumları sezgisel kontrol sağlar.",
       "Aynı yükseklikten eğik düzlemlerde kayan cisimlerin çarpma hızı eğimden bağımsız (ϑ² = 2gh)."],
      ["Sürtünmesiz düzlem"], ["Nitel"], ["a ∝ cosθ sanmak"]),
    M(["θ = 30° için a = 5, 37° için 6, 45° için 7,07, 53° için 8, 60° için 8,66, 90° için 10 m/s²; N = mg·cosθ için tersini kullan."],
      ["g = 10 m/s²"], ["Özel açı dışında hesap makinesi gerektirir"], ["37°/53° değerlerini yer değiştirmek"]),
    M(["Yükseklik yöntemi: ϑ² = 2g·h (h düşey yükseklik farkı); yol s = h/sinθ olduğundan ϑ² = 2a·s ile aynı sonucu verir."],
      ["Yalnız ağırlık iş yapıyor (sürtünmesiz)"], ["Sürtünme ya da ek kuvvet varsa çalışmaz"], ["h yerine yolu yazmak"]),
    "Eğik düzlem: paralel ⇒ mg·sinθ, dik ⇒ mg·cosθ. Sürtünmesiz + ek kuvvet yok ⇒ a = g·sinθ, kütleden bağımsız.",
    "Sürtünmesiz, 37° eğimli bir düzlemde 4 kg'lık bir cisim serbest bırakılıyor. İvmesini, düzlemin tepki (normal) kuvvetini ve düzlem boyunca 3 m kaydığında hızını bulunuz. (g = 10 m/s², sin37° = 0,6, cos37° = 0,8)",
    ["a = g·sin37° = 6 m/s².", "N = m·g·cos37° = 4·10·0,8 = 32 N.", "ϑ² = 2·a·s = 2·6·3 = 36 → ϑ = 6 m/s (kontrol: h = 3·0,6 = 1,8 m, ϑ = √(2·10·1,8) = 6)."],
    "a = 6 m/s²; N = 32 N; ϑ = 6 m/s.",
    """
g, m, s = 10.0, 4.0, 3.0
sin_t, cos_t = 0.6, 0.8
a = g * sin_t
N = m * g * cos_t
v = (2 * a * s) ** 0.5
assert abs(a - 6.0) < 1e-12 and abs(N - 32.0) < 1e-12 and abs(v - 6.0) < 1e-12
h = s * sin_t
assert abs((2 * g * h) ** 0.5 - v) < 1e-12
# kütle bağımsızlığı
for mm in (1.0, 4.0, 40.0):
    assert abs(mm * g * sin_t / mm - a) < 1e-12
""")

SOLUTIONS["connected-bodies-same-acceleration"] = S(
    M(["Cisimler ip gergin/temas halinde aynı ivmeyle hareket ediyorsa tüm sistemi tek cisim say.",
       "Dış kuvvetleri (iç kuvvetler: ip gerilmesi, temas kuvveti toplamda sıfır) ayır: a = ΣF_dış/Σm.",
       "Sonra bir cisim seç; tek cisim için F_net = m·a yaz ve ip gerilmesini ya da temas kuvvetini bul.",
       "Sonucu başka cisimle çapraz kontrol et."],
      ["Tüm cisimler aynı büyüklükte ivmeyle hareket eder (ip gergin ve uzamıyor)", "İp kütlesiz, makara sürtünmesiz ve kütlesiz"],
      ["Farklı ivmeli (hareketli makara, üst blok kayıyor) sistemler kapsam dışı", "İp gevşerse sonuç geçersiz"],
      ["İç kuvveti dış kuvvet gibi sistem denklemine yazmak", "İp gerilmesini asılı cismin ağırlığı sanmak", "Tek cisim denkleminde yanlış kütle kullanmak"]),
    M(["İp gerilmesi iki cisim için de aynı büyüklükte ama zıt yöndedir (etki-tepki).", "Asılı cisim ivmeli düşüyorsa gerilme ağırlıktan küçüktür; ivme 'g'den küçüktür çünkü diğer cisim de hızlanmak zorunda."],
      ["Aynı ivme"], ["Nitel"], ["Sistemin dengede olduğunu düşünmek"]),
    M(["a = (hareketi doğuran kuvvet farkı)/(toplam kütle); gerilme için hızlandırılan cismin kütlesi × a (ya da asılı cismin m·(g − a)).",
       "Temas kuvveti: öndeki blokların toplam kütlesi × a."],
      ["Aynı ivme, sürtünmesiz ya da net sürtünme bilinen"], ["Sürtünme varsa onu F_net'e ekle"], ["Sürtünmeyi unutmak"]),
    None,
    "Aynı ivme → önce a = ΣF_dış/Σm, sonra tek cisimde T ya da temas kuvveti. Asılı kütle ivmeliyse T ≠ mg.",
    "Sürtünmesiz yatay masada 3 kg'lık bir blok, makaradan geçen kütlesiz iple masa kenarından sarkan 2 kg'lık cisme bağlıdır. Sistemin ivmesini ve ip gerilmesini bulunuz. Ayrıca 2 kg ve 3 kg'lık iki bloğu yatay zeminde yan yana 30 N'luk kuvvet itiyorsa (sürtünmesiz), aralarındaki temas kuvveti kaçtır? (g = 10 m/s²)",
    ["Sistem: a = m_asılı·g/(m₁ + m₂) = 20/5 = 4 m/s².", "Blok için T = m₁·a = 3·4 = 12 N (kontrol: asılı için 20 − T = 2·4 → T = 12).",
     "İtilen iki blok: a = 30/5 = 6 m/s²; ön blok (3 kg) için temas kuvveti N = 3·6 = 18 N (kontrol: arkadaki 2 kg'lık blok için F − N = 2·6 → N = 18 N)."],
    "a = 4 m/s²; T = 12 N; temas kuvveti 18 N.",
    """
g = 10.0
m1, m2 = 3.0, 2.0
a = m2 * g / (m1 + m2)
T = m1 * a
assert abs(a - 4.0) < 1e-12 and abs(T - 12.0) < 1e-12
assert abs((m2 * g - T) - m2 * a) < 1e-12            # asılı cisimle çapraz kontrol
# yan yana bloklar: arkadaki 2 kg itiyor, öndeki 3 kg
F = 30.0
a2 = F / (2.0 + 3.0)
N = 3.0 * a2
assert abs(a2 - 6.0) < 1e-12 and abs(N - 18.0) < 1e-12
assert abs((F - N) - 2.0 * a2) < 1e-12
""")

SOLUTIONS["accelerating-frame-pendulum"] = S(
    M(["Aracın ivmesi a yönünde (ivme yönü hızlanma ise hareket yönü, yavaşlama ise zıt yön); asılı cisim araca göre durgun, yere göre a ile ivmeli.",
       "Cisme etki eden kuvvetler: ağırlık (aşağı) ve ip gerilmesi T (ip boyunca, düşeyle θ açı).",
       "Düşey: T·cosθ = m·g; yatay: T·sinθ = m·a.",
       "Oranla: tanθ = a/g; gerilme T = m·√(g² + a²). Sapma, ivmenin ters yönündedir (cisim araca göre geriye)."],
      ["Araç sabit ivmeli, cisim araca göre durgun", "İp kütlesiz, cisim noktasal"],
      ["Araç sabit hızlıysa θ = 0", "Cisim salınıyorsa bağıntı denge açısı için geçerlidir"],
      ["tanθ yerine sinθ yazmak", "Sapmanın yönünü ivme yönü sanmak", "Açının kütleye bağlı olduğunu sanmak"]),
    M(["Cismin yatayda ivmelenmesi için ip bir yatay bileşen sağlamalı: ip ivme yönünde eğilir, cisim araca göre arkada kalır.", "Kütle sadeleşir: açı yalnız a/g oranına bağlıdır."],
      ["Aynı ivme"], ["Nitel"], ["Kütle etkisini beklemek"]),
    M(["tan θ = a/g: g = 10 için a = 7,5 → tanθ = 0,75 → θ = 37°; a = 10 → 45°; a = 40/3 → 53°.", "T/(mg) = 1/cosθ = √(1 + (a/g)²)."],
      ["g = 10 m/s²", "Özel açılar"], ["Özel açı değilse hesap makinesi"], ["Açının düşeyden mi yataydan mı ölçüldüğünü karıştırmak"]),
    None,
    "Aynı ip + ivmeli araç → tanθ = a/g. Açı düşeyle ölçülür; kütle ve ip uzunluğu önemsiz.",
    "Yatay yolda ivmesi 7,5 m/s² olan bir aracın aynasına 0,2 kg kütleli bir kolye ipiyle asılıdır. Kolyenin düşeyle yaptığı açıyı ve ip gerilmesini bulunuz. (g = 10 m/s², tan37° = 0,75)",
    ["tanθ = a/g = 7,5/10 = 0,75 → θ = 37° (ivmenin ters yönünde, geriye doğru).",
     "T = m·√(g² + a²) = 0,2·√(100 + 56,25) = 0,2·12,5 = 2,5 N.", "Kontrol: T·cosθ = 2,5·0,8 = 2 N = m·g."],
    "θ = 37°; T = 2,5 N.",
    """
import math
m, g, a = 0.2, 10.0, 7.5
theta = math.atan(a / g)
T = m * math.hypot(g, a)
assert abs(math.degrees(theta) - 36.8699) < 1e-3
assert abs(T - 2.5) < 1e-12
# bileşen kontrolleri
assert abs(T * math.cos(theta) - m * g) < 1e-12
assert abs(T * math.sin(theta) - m * a) < 1e-12
# kütleden bağımsızlık
for mm in (0.05, 1.0):
    assert abs(math.atan((mm * a) / (mm * g)) - theta) < 1e-12
""")

SOLUTIONS["apparent-weight-elevator"] = S(
    M(["Yukarı yönü pozitif seç; cisme etki eden kuvvetler: tartıdan normal kuvvet N (yukarı), ağırlık mg (aşağı).",
       "Newton'un 2. yasası: N − mg = m·a (a yukarı yönlü ise +, aşağı yönlü ise −).",
       "N = m(g + a): tartının gösterdiği değer ya da görünür ağırlık N'dir; hız yönü değil ivme yönü belirler.",
       "ϑ-t grafiği verilmişse her aralıkta ivmeyi (eğimi) bul ve N'yi hesapla."],
      ["Cisim asansörle birlikte aynı ivmeyle hareket ediyor", "Tartı normal kuvveti ölçer"],
      ["Serbest düşen asansörde N = 0 (ağırsızlık hissi) olur ama ağırlık yok olmaz"],
      ["İvme yönünü hız yönü sanmak", "Sabit hızda tartı değerinin değişeceğini sanmak", "Tartıyı ağırlığı ölçüyor sanmak"]),
    M(["İvme yukarıysa (hızlanarak yukarı ya da yavaşlayarak aşağı) zemin seni daha çok iter: N > mg.", "İvme aşağıysa N < mg; a = g ise N = 0 (serbest düşme).", "Sabit hızda N = mg."],
      ["Newton'un 2. yasası"], ["Nitel"], ["Hareket yönüne göre karar vermek"]),
    M(["Her aralık için: ivme yukarı → N = m(g + a); ivme aşağı → N = m(g − a). İvme yönünü ϑ-t eğiminin işaretinden bul (yukarı pozitif)."],
      ["Yön seçimi tutarlı"], ["Eğim işaretini yanlış okumak sonucu tersine çevirir"], ["Yönü karıştırmak"]),
    None,
    "Tartı sorusu = N = m(g ± a). Önce ivmenin yönü (hız yönü değil). Sabit hızda ya da hareketsizken N = mg; a = g'de N = 0.",
    "60 kg kütleli bir kişi asansörde tartıya çıkıyor. Asansör ϑ-t grafiğine göre yukarı doğru 3 s'de 0'dan 6 m/s'ye hızlanıyor, 4 s sabit hızla gidiyor, 2 s'de durana kadar yavaşlıyor. Her aralıkta tartının gösterdiği kuvveti bulunuz. (g = 10 m/s²)",
    ["0–3 s: a = +2 m/s² → N = 60(10 + 2) = 720 N.", "3–7 s: a = 0 → N = 600 N.", "7–9 s: a = −3 m/s² (aşağı) → N = 60(10 − 3) = 420 N."],
    "720 N, 600 N, 420 N.",
    """
m, g = 60.0, 10.0
segs = [(0.0, 6.0, 3.0), (6.0, 6.0, 4.0), (6.0, 0.0, 2.0)]    # (v_baş, v_son, süre)
expected = [720.0, 600.0, 420.0]
for (v1, v2, T), e in zip(segs, expected):
    a = (v2 - v1) / T
    N = m * (g + a)
    assert abs(N - e) < 1e-9
# N - mg = m a  doğrulaması
assert abs(720.0 - m * g - m * 2.0) < 1e-9
# serbest düşme: N = 0
assert m * (g + (-g)) == 0.0
""")

# ============================ FİZ.11.1.6 – FİZ.11.1.7 ============================
SOLUTIONS["friction-type-identification"] = S(
    M(["Cismin temas noktasının yüzeye göre hızını incele.",
       "Temas noktası yüzeye göre kayıyorsa (bağıl hareket var) → kinetik sürtünme.",
       "Temas noktası yüzeye göre durgunsa (cisim durgun ya da kaymadan yuvarlanıyor) → statik sürtünme.",
       "Kaymadan dönen tekerlekte temas noktasının hızı sıfırdır: ϑ_cm = ω·R. Kilitlenmiş tekerlekte ω = 0, temas noktası kayar."],
      ["Temas yüzeyleri belirli", "Hareket durumu açık verilmiş"],
      ["Temas noktasının bağıl hızı anlık olarak değerlendirilir; hareketin kendisi değil"],
      ["Hareketi kaymayla özdeşleştirmek", "Dönerek ötelemede kinetik sürtünme sanmak"]),
    M(["Sürtünme türü 'cisim hareket ediyor mu' ile değil 'yüzeyler birbirine göre kayıyor mu' ile belirlenir.", "Yürürken ayağın zemine değen kısmı kaymaz → statik sürtünme sizi ileri iter."],
      ["Temas var"], ["Nitel"], ["Hareketli = kinetik sanmak"]),
    M(["Tek soru: 'temas noktası yüzeye göre kayıyor mu?' Evet → kinetik; hayır → statik."],
      ["Düz yüzeyler"], ["Yüzeyler arası bağıl hareketi yanlış okumak"], ["Cismin hareketine bakıp karar vermek"]),
    None,
    "'Kaymadan yuvarlanma / durgun / yürüme' → statik; 'kayıyor / fren izi / kilitlenmiş tekerlek' → kinetik.",
    "Yarıçapı 0,3 m olan bir tekerlek yatay yolda öteleme hızı 6 m/s ile hareket ediyor. (a) Tekerlek kaymadan yuvarlanıyorsa açısal hızı ve temas noktasının yere göre hızı nedir? Sürtünme türü? (b) Fren kilitlenip tekerlek dönmüyorsa temas noktasının hızı ve sürtünme türü nedir?",
    ["(a) Kaymadan yuvarlanma: ω = ϑ/R = 6/0,3 = 20 rad/s; temas noktasının hızı ϑ_cm − ωR = 0 → statik sürtünme.",
     "(b) ω = 0: temas noktasının hızı 6 m/s (araçla birlikte) → yüzeye göre kayıyor → kinetik sürtünme."],
    "(a) ω = 20 rad/s, temas noktası hızı 0, statik sürtünme; (b) temas noktası hızı 6 m/s, kinetik sürtünme.",
    """
R, v = 0.3, 6.0
def contact_speed(v_cm, omega, R):
    return abs(v_cm - omega * R)
def friction_type(v_cm, omega, R):
    return 'statik' if contact_speed(v_cm, omega, R) < 1e-9 else 'kinetik'
omega = v / R
assert abs(omega - 20.0) < 1e-12
assert friction_type(v, omega, R) == 'statik'
assert friction_type(v, 0.0, R) == 'kinetik' and abs(contact_speed(v, 0.0, R) - 6.0) < 1e-12
""")

SOLUTIONS["friction-direction"] = S(
    M(["Sürtünmesiz olsaydı temas yüzeylerinin birbirine göre hangi yönde kayacağını (kayma eğilimini) belirle.",
       "Sürtünme kuvveti bu bağıl hareket/eğilime zıt yöndedir (yüzeye paralel).",
       "Cisme etki eden sürtünmenin yönünü, o cismin kaydığı yüzeyi referans alarak yaz.",
       "Gerekirse Newton'un 2. yasasıyla doğrula: ivme yönünü sağlayan kuvvet sürtünme olabilir (yürüme, hızlanan araç)."],
      ["Temas eden yüzeyler", "Kayma eğiliminin yönü belirlenebilir"],
      ["Sürtünme hareket yönüne zıt demek her zaman doğru değildir (yürürken ve hızlanan tekerlekte hareket yönündedir)"],
      ["Sürtünmeyi hep hareket yönüne zıt sanmak", "Kayma eğilimini belirlemeden yön vermek"]),
    M(["Sürtünme 'bağıl hareketi' önler: cismi kaydıracak olan eğilimin tersine çalışır.", "Yürürken ayak geri kayacak olur, sürtünme ileri; böylece sürtünme hareketi doğurur."],
      ["Temas var"], ["Nitel"], ["Sürtünmeyi hareketin engeli sanmak"]),
    M(["Eğilim testi: 'Sürtünme olmasaydı cisim yüzeyde ne tarafa kayardı?' Cevabın tersi sürtünmenin yönüdür."],
      ["Düz yüzeyler"], ["Dönerek ötelemede temas noktasının eğilimi incelenir"], ["Cismin hareket yönüne bakmak"]),
    None,
    "'Sürtünme hep harekete zıt' tuzağı: yürüyen insan, hızlanan araba, bant üzerindeki kutuda sürtünme hareket yönündedir. Eğilime zıt yönü seç.",
    "Duvara yatay kuvvetle bastırılıp tutulan 0,5 kg'lık bir kitapta ve yatay hızlanan bir konveyör bandı üzerinde bantla birlikte hızlanan bir kutuda sürtünmenin yönü ve büyüklüğü nedir? (kutu kütlesi 2 kg, bant ivmesi 1,5 m/s², g = 10 m/s²)",
    ["Kitap: sürtünmesiz olsa aşağı kayacak → sürtünme yukarı, büyüklüğü m·g = 5 N (dengede).",
     "Kutu bantla birlikte hızlanıyor: kutuya etki eden tek yatay kuvvet sürtünme, ivme yönünde: f = m·a = 2·1,5 = 3 N bant hareketi yönünde (kutu banda göre geriye kayma eğiliminde)."],
    "Kitap: yukarı, 5 N. Kutu: bant hareketi yönünde, 3 N.",
    """
g = 10.0
m_book = 0.5
f_book_up = m_book * g                 # düşey denge
assert abs(f_book_up - 5.0) < 1e-12
m_box, a_belt = 2.0, 1.5
f_box = m_box * a_belt                 # yatayda tek kuvvet -> F_net
assert abs(f_box - 3.0) < 1e-12 and f_box > 0     # hareket yönünde (pozitif)
# kayma eğilimi: sürtünme olmasaydı kutu yerinde kalırdı (bant önde gider) -> eğilim geriye -> sürtünme ileri
tendency = -1.0
assert -tendency == 1.0
""")

SOLUTIONS["static-vs-kinetic-compare"] = S(
    M(["Yargıları tek tek sınadığın bir tablo kur: bağlı olduğu nicelikler (N, yüzey türü), yüzey alanından bağımsızlık, büyüklük ilişkisi.",
       "Statik sürtünme: 0 ile f_s,max = k_s·N arasında, uygulanan kuvvete göre değişir.",
       "Kinetik sürtünme: f_k = k_k·N sabit; hıza ve alana bağlı değil. Genellikle k_k < k_s → f_k < f_s,max.",
       "İki tür de N'ye ve yüzey çiftine bağlıdır, temas alanına bağlı değildir."],
      ["Temel (Coulomb) sürtünme modeli"],
      ["Çok yüksek hızlarda/çok farklı koşullarda model dışı davranışlar olabilir (program kapsamı dışı)"],
      ["Statik sürtünmeyi sabit sanmak", "Kinetik sürtünmenin maksimum statikten büyük olduğunu düşünmek", "Alana bağımlılık"]),
    M(["Statik sürtünme tepkidir: ne kadar itilirse o kadar karşı koyar (eşiğe kadar).", "Kaymayı başlatmak, kaymayı sürdürmekten zordur."],
      ["Genel model"], ["Nitel"], ["Statik sürtünme ile maksimum statiği özdeşleştirmek"]),
    M(["Ezber tablo: Statik değişken (0–max); kinetik sabit; ikisi N ve yüzeye bağlı; alan/hız bağımsız; max statik ≥ kinetik."],
      ["Standart sorular"], ["Özel yüzeylerde k_s ≈ k_k olabilir"], ["Eşitlik durumunu kaçırmak"]),
    None,
    "Yargı sorularında: statik 'değişken', kinetik 'sabit'; max statik ≥ kinetik; ikisi de alandan bağımsız, N'ye bağlı.",
    "Bir cisim k_s = 0,5 ve k_k = 0,3 olan yüzeyde duruyor, N = 100 N. F = 30 N ve F = 60 N uygulanırsa sürtünme kuvveti ne olur? Maksimum statik ile kinetik değeri karşılaştırınız.",
    ["f_s,max = 0,5·100 = 50 N; f_k = 0,3·100 = 30 N → f_s,max > f_k.",
     "F = 30 N < 50 N: cisim durgun, statik sürtünme f = F = 30 N.",
     "F = 60 N > 50 N: cisim kayar, f = f_k = 30 N (sürtünme azalır)."],
    "F = 30 N → f = 30 N (statik). F = 60 N → f = 30 N (kinetik); f_s,max = 50 N > f_k = 30 N.",
    """
ks, kk, N = 0.5, 0.3, 100.0
fs_max, fk = ks * N, kk * N
def friction(F):
    return F if F <= fs_max else fk
assert fs_max > fk
assert friction(30.0) == 30.0 and friction(60.0) == 30.0
assert friction(50.0) == 50.0
""")

SOLUTIONS["friction-applied-force-graph"] = S(
    M(["Grafiğin bölgelerini ayır: orijinden başlayan eğimli (eğim 1) doğru = statik bölge (f = F); en yüksek nokta = maksimum statik sürtünme (harekete geçme eşiği).",
       "Eşikten sonra düşen ve sabit kalan yatay kısım = kinetik sürtünme f_k.",
       "Katsayılar: k_s = f_s,max/N, k_k = f_k/N (N verilmişse ya da m·g'den).",
       "Verilen F değeri için: F ≤ eşik ise cisim durgun ve f = F; F > eşik ise cisim kayar ve f = f_k, ivme a = (F − f_k)/m."],
      ["Grafik f–F biçiminde", "Yatay zemin, N sabit"],
      ["f–F grafiği ile F–a ya da f–t grafiğini karıştırma; eksenleri oku"],
      ["Statik bölgede sürtünmeyi sabit sanmak", "Eşik noktası ile kinetik değeri karıştırmak", "Hareket başlayınca sürtünmeyi artıyor sanmak"]),
    M(["Statik bölgede sürtünme uygulanan kuvveti tam dengeler (f = F); eşikte statik 'biter', kinetik başlar.", "Kinetik değer eşikten küçük olduğundan grafik eşikte aşağı iner."],
      ["Genel model"], ["Nitel"], ["Doğrusal artışın sürdüğünü sanmak"]),
    M(["Grafikten iki sayıyı oku: tepe noktası (f_s,max) ve yatay kısım (f_k). Sonra yalnız bu iki sayıyla soruyu bitir."],
      ["Grafik açıkça verilmiş"], ["Eksen ölçeği okunmalı"], ["Eksen birimlerini karıştırmak"]),
    None,
    "f–F grafiğinde: eğimli kısım (f = F) statik; tepe = max statik; yatay kısım = kinetik. F tepeyi aşarsa a = (F − f_k)/m.",
    "4 kg'lık bir cisme uygulanan F kuvvetine karşılık sürtünme grafiği: F = 0'dan 10 N'a kadar f = F, 10 N'da en yüksek değer, sonra f = 8 N sabit. k_s, k_k'yı ve F = 12 N için ivmeyi bulunuz. F = 6 N için sürtünme nedir? (g = 10 m/s²)",
    ["N = m·g = 40 N.", "k_s = 10/40 = 0,25; k_k = 8/40 = 0,2.", "F = 12 N > 10 N: kayar, a = (12 − 8)/4 = 1 m/s².", "F = 6 N < 10 N: durgun, f = 6 N."],
    "k_s = 0,25; k_k = 0,2; F = 12 N için a = 1 m/s²; F = 6 N için f = 6 N (statik).",
    """
m, g = 4.0, 10.0
N = m * g
fs_max, fk = 10.0, 8.0
ks, kk = fs_max / N, fk / N
assert abs(ks - 0.25) < 1e-12 and abs(kk - 0.2) < 1e-12
def state(F):
    if F <= fs_max:
        return F, 0.0
    return fk, (F - fk) / m
assert state(12.0) == (8.0, 1.0)
assert state(6.0) == (6.0, 0.0)
assert state(10.0) == (10.0, 0.0)
""")

SOLUTIONS["friction-threshold"] = S(
    M(["Önce eşik kontrolü: uygulanan F ile f_s,max'ı karşılaştır.",
       "F ≤ f_s,max ise cisim durgun: statik sürtünme f = F, ivme a = 0.",
       "F > f_s,max ise cisim kayar: sürtünme f_k (kinetik), ivme a = (F − f_k)/m.",
       "Cisim zaten hareket ediyorsa (kayıyorsa) eşik kontrolü yapılmaz; doğrudan f_k kullanılır."],
      ["f_s,max ve f_k verilmiş", "Yatay zemin"],
      ["Cisim önceden hareket ediyorsa eşik anlamsızdır", "F eşiğe tam eşitse cisim hareketin sınırında: a = 0"],
      ["Durgun cisimde f = f_s,max almak", "Durgun cisimde ivmeyi F − f_s,max ile hesaplayıp negatif bulmak", "Eşiği kinetik değerle karıştırmak"]),
    M(["Sürtünme gerektiği kadar tepki verir ama bir tavanı vardır: f_s,max. Tavan aşılınca cisim kayar ve sürtünme düşer.", "Küçük F uygularsan cisim kıpırdamaz."],
      ["Genel model"], ["Nitel"], ["Sürtünmeyi hep maksimum sanmak"]),
    M(["Üç basamak: (1) F ≤ f_s,max? → a = 0, f = F; (2) değilse a = (F − f_k)/m; (3) cisim hareketliyse doğrudan (2)."],
      ["Tablo soruları"], ["Hareket geçmişi bilinmeli"], ["Eşiği kontrol etmeden doğrudan formül uygulamak"]),
    None,
    "Sürtünme + ivme sorusunda önce 'F eşiği aşıyor mu?' Aşmıyorsa a = 0, f = F. Aşıyorsa a = (F − f_k)/m.",
    "5 kg'lık bir cismin maksimum statik sürtünmesi 20 N, kinetik sürtünmesi 15 N'dur. Cisim durgunken sırayla F = 12 N, 20 N ve 30 N uygulanırsa her durumda sürtünmeyi ve ivmeyi bulunuz. Cisim 30 N altında kayarken F = 18 N'a düşürülürse ivmesi ne olur?",
    ["12 N ≤ 20 N: f = 12 N, a = 0.", "20 N = eşik: f = 20 N, a = 0 (sınırda).", "30 N > 20 N: f = 15 N, a = (30 − 15)/5 = 3 m/s².",
     "Hareket sürerken F = 18 N: f = f_k = 15 N, a = (18 − 15)/5 = 0,6 m/s² (durgun olsaydı kıpırdamazdı)."],
    "12 N: f = 12 N, a = 0; 20 N: f = 20 N, a = 0; 30 N: f = 15 N, a = 3 m/s². Hareket halinde 18 N: a = 0,6 m/s².",
    """
m, fs_max, fk = 5.0, 20.0, 15.0
def at_rest(F):
    if F <= fs_max:
        return F, 0.0
    return fk, (F - fk) / m
def moving(F):
    return fk, (F - fk) / m
assert at_rest(12.0) == (12.0, 0.0)
assert at_rest(20.0) == (20.0, 0.0)
assert at_rest(30.0) == (15.0, 3.0)
f, a = moving(18.0)
assert f == 15.0 and abs(a - 0.6) < 1e-12
assert at_rest(18.0) == (18.0, 0.0)     # durgunken aynı kuvvet cismi kıpırdatmaz
""")

SOLUTIONS["friction-horizontal-dynamics"] = S(
    M(["Düşey denge: N = m·g (ek düşey kuvvet yok).",
       "Kinetik sürtünme: f_k = k_k·N = k_k·m·g.",
       "Yatay: F_net = F − f_k = m·a → a = (F − k_k·m·g)/m.",
       "İlk hızla kayan (çekilmeyen) cisim: a = −k_k·g, durma süresi t = ϑ₀/(k_k·g), durma yolu x = ϑ₀²/(2k_k·g)."],
      ["Yatay zemin", "Cisim kayıyor (kinetik)", "k_k sabit"],
      ["F, f_s,max'ı aşmıyorsa cisim kıpırdamaz", "Eğik ya da açılı kuvvette N değişir"],
      ["N'yi yanlış almak", "Durana kadar sürtünmeyi uygulanan kuvvete eşit sanmak", "Kütleyi sadeleştirmeden bırakmak"]),
    M(["Sürtünme hareketi frenler: bileşke kuvvet uygulanan kuvvetten küçük olur.", "İlk hızla bırakılan cismi yalnız sürtünme durdurur; ivme kütleden bağımsızdır (a = k_k·g)."],
      ["Kinetik sürtünme"], ["Nitel"], ["Ağır cismin daha geç duracağını sanmak"]),
    M(["Durma problemlerinde doğrudan a = k_k·g al; x = ϑ₀²/(2k_k·g), t = ϑ₀/(k_k·g)."],
      ["Cisim yalnız sürtünmeyle yavaşlıyor"], ["Ek kuvvet varsa geçersiz"], ["Kütle ile çarpıp bölmeyi unutmamak"]),
    None,
    "'Kuvvetle çekilen' → a = (F − k·m·g)/m. 'İlk hızla kayıp duruyor' → a = k·g (kütle yok), x = ϑ₀²/(2kg).",
    "Yatay zeminde 10 kg'lık bir kızak 50 N'luk yatay kuvvetle çekiliyor (k_k = 0,2). İvmesini bulunuz. Aynı kızak 12 m/s hızla itilip bırakılırsa ne kadar sürede ve kaç metrede durur? (g = 10 m/s²)",
    ["N = 100 N, f_k = 0,2·100 = 20 N.", "a = (50 − 20)/10 = 3 m/s².", "Bırakılınca a = −k_k·g = −2 m/s²; t = 12/2 = 6 s; x = 12²/(2·2) = 36 m."],
    "a = 3 m/s²; durma süresi 6 s, durma yolu 36 m.",
    """
m, g, k, F, v0 = 10.0, 10.0, 0.2, 50.0, 12.0
N = m * g
fk = k * N
assert abs((F - fk) / m - 3.0) < 1e-12
a = -k * g
t = -v0 / a
x = v0 * t + 0.5 * a * t ** 2
assert abs(t - 6.0) < 1e-12 and abs(x - 36.0) < 1e-12
assert abs(v0 ** 2 / (2 * k * g) - x) < 1e-12
# kütle bağımsızlığı
for mm in (1.0, 10.0, 100.0):
    assert abs(-k * mm * g / mm - a) < 1e-12
""")

SOLUTIONS["friction-angled-force"] = S(
    M(["Kuvveti bileşenlerine ayır: F_x = F·cosα, F_y = F·sinα (α yatayla ölçülür).",
       "Düşey denge: çekme (yukarı) için N = m·g − F·sinα; itme (aşağı) için N = m·g + F·sinα.",
       "Kinetik sürtünme: f_k = k_k·N.",
       "Yatay: F·cosα − f_k = m·a → a = (F·cosα − k_k·N)/m. Cisim havaya kalkmıyorsa N ≥ 0 kontrol edilir."],
      ["Yatay zemin", "Kuvvet sabit büyüklük ve açıda", "Cisim zeminle temasta (N > 0)"],
      ["N < 0 çıkarsa cisim zeminden ayrılır; bu çözümler geçersizdir"],
      ["N'yi mg almak", "Düşey bileşeni N'ye yanlış işaretle eklemek", "Açıyı yanlış eksene göre almak"]),
    M(["Yukarı doğru çekme, normal kuvveti ve sürtünmeyi azaltır; aşağı doğru itme artırır.", "Bu yüzden çekmek itmeden kolaydır."],
      ["Aynı F ve α"], ["Nitel"], ["İtme–çekme farkını yok saymak"]),
    M(["37° (0,6/0,8) için: çekmede N = mg − 0,6F, itmede N = mg + 0,6F; yatay bileşen 0,8F. Doğrudan yaz."],
      ["Özel açılar"], ["Açı yatayla ölçüldüğünde"], ["Açıyı düşeyle verilmişse sin/cos yer değiştirir"]),
    None,
    "Açılı kuvvet = N değişir. Çekme: N = mg − F·sinα; itme: N = mg + F·sinα. Sürtünme ve ivme buna göre.",
    "10 kg'lık bir kutu yatayla 37° yukarı yönlü 50 N'luk kuvvetle çekiliyor. Kinetik sürtünme katsayısı 0,2 ise normal kuvveti, sürtünmeyi ve ivmeyi bulunuz. Aynı kuvvet yatayla 37° aşağı doğru itme olsaydı ivme ne olurdu? (g = 10 m/s², sin37° = 0,6, cos37° = 0,8)",
    ["Çekme: F_y = 30 N, F_x = 40 N; N = 100 − 30 = 70 N; f = 0,2·70 = 14 N; a = (40 − 14)/10 = 2,6 m/s².",
     "İtme: N = 100 + 30 = 130 N; f = 26 N; a = (40 − 26)/10 = 1,4 m/s²."],
    "Çekme: N = 70 N, f = 14 N, a = 2,6 m/s². İtme: N = 130 N, f = 26 N, a = 1,4 m/s².",
    """
m, g, k, F = 10.0, 10.0, 0.2, 50.0
s, c = 0.6, 0.8
def accel(sign):
    N = m * g + sign * F * s          # sign=-1 çekme (yukarı), +1 itme (aşağı)
    f = k * N
    return N, f, (F * c - f) / m
N1, f1, a1 = accel(-1)
N2, f2, a2 = accel(+1)
assert abs(N1 - 70) < 1e-9 and abs(f1 - 14) < 1e-9 and abs(a1 - 2.6) < 1e-9
assert abs(N2 - 130) < 1e-9 and abs(f2 - 26) < 1e-9 and abs(a2 - 1.4) < 1e-9
assert a1 > a2
# zeminden ayrılma sınırı: çekme için N>0 olması: F sinα < mg
assert F * s < m * g
""")

SOLUTIONS["friction-incline-coefficient"] = S(
    M(["Eğik düzlemde ağırlığı bileşenlerine ayır: paralel mg·sinθ, dik mg·cosθ; N = mg·cosθ, f = k·N = k·mg·cosθ.",
       "Kaymaya başlama (eşik) anında mg·sinθ = k_s·mg·cosθ → k_s = tanθ_s.",
       "Sabit hızla kayma anında net kuvvet sıfır: mg·sinθ = k_k·mg·cosθ → k_k = tanθ.",
       "İvmeli kayma: a = g(sinθ − k_k·cosθ). Farklı yüzeyler için eşik açısı büyük olan yüzeyin katsayısı büyüktür."],
      ["Yalnız ağırlık, normal ve sürtünme etkili", "Sabit hız (k_k) ya da kaymaya başlama (k_s)"],
      ["k = tanθ yalnız eşik ya da sabit hızda geçerli; ivmeli kaymada geçersiz", "Ek kuvvet varsa uygulanmaz"],
      ["tanθ yerine sinθ almak", "Kaymaya başlama açısını kinetik katsayı sanmak", "Katsayının kütleye bağlı olduğunu sanmak"]),
    M(["Eğim arttıkça kaydıran bileşen büyür, tutan sürtünme yeni bir yönde artar; tanθ = k noktasında dengelenirler.", "Katsayı yüzey çiftine ait bir özelliktir: kütle ve alan değiştirmez."],
      ["Genel model"], ["Nitel"], ["Kütleyi katsayıya katmak"]),
    M(["37° ise k = 0,75; 45° ise k = 1; 53° ise k = 4/3. Sabit hız/eşit açı verilince hemen tanθ yaz."],
      ["Sabit hız ya da eşik"], ["İvmeli kaymada kullanılmaz"], ["Hareketin türünü okumamak"]),
    M(["İvmeli kaymada: a = g(sinθ − k·cosθ); a = 0 koyunca k = tanθ'yı verir (özel hâl)."],
      ["Kinetik sürtünme"], ["Fazladan adım"], ["İşaret hatası"]),
    "Eğimli düzlemde 'sabit hızla kayıyor / tam kaymaya başladı' → k = tanθ. İvme varsa a = g(sinθ − k·cosθ).",
    "Ayarlanabilir bir eğik düzlemde bir cisim 37°'de sabit hızla kayıyor. Kinetik sürtünme katsayısını bulunuz. Aynı yüzeyde eğim 53° yapılırsa cismin ivmesi ne olur? Aynı eğimde (37°) katsayısı 0,5 olan başka yüzeyde ivme nedir? (g = 10 m/s²)",
    ["Sabit hız: k_k = tan37° = 0,75.", "53°'de a = g(sin53° − k·cos53°) = 10(0,8 − 0,75·0,6) = 3,5 m/s².", "k = 0,5, θ = 37°: a = 10(0,6 − 0,5·0,8) = 2 m/s²."],
    "k_k = 0,75; 53°'de a = 3,5 m/s²; k = 0,5 yüzeyde (37°) a = 2 m/s².",
    """
import math
g = 10.0
th = math.radians(37)
k = math.tan(th)
assert abs(k - 0.75) < 5e-3
# sabit hız kontrolü: a = g(sin - k cos) = 0
assert abs(g * (math.sin(th) - k * math.cos(th))) < 1e-9
k = 0.75
a53 = g * (0.8 - k * 0.6)
assert abs(a53 - 3.5) < 1e-9
a2 = g * (0.6 - 0.5 * 0.8)
assert abs(a2 - 2.0) < 1e-9
""")

SOLUTIONS["friction-wall-press"] = S(
    M(["Düşey denge: statik sürtünme ağırlığı taşır: f = m·g (yukarı).",
       "Yatay denge: N = F (duvara bastırma kuvveti).",
       "Düşmemesi için f ≤ f_s,max = k_s·N = k_s·F → k_s·F ≥ m·g → F_min = m·g/k_s.",
       "F, F_min'den büyükse sürtünme yine m·g'dir (f = F değil); fazlası yalnız f_s,max'ı artırır."],
      ["Cisim durgun (dengede)", "k_s verilmiş", "Kuvvet duvara dik"],
      ["Açılı kuvvette N ve düşey denge değişir", "Cisim kayıyorsa kinetik sürtünme kullanılır"],
      ["Normal kuvveti ağırlık sanmak", "Bastırma artınca sürtünmenin de arttığını sanmak (f = mg sabit kalır)"]),
    M(["Sürtünme ağırlığı dengelemek için 'gerektiği kadar' ortaya çıkar; üst sınırı N ile belirlenir.", "Daha sert bastırırsan tavan yükselir ama kullanılan değer değişmez."],
      ["Denge"], ["Nitel"], ["Maksimum değeri gerçek değer sanmak"]),
    M(["Tek satır: F_min = m·g/k_s. Sürtünmenin değeri soruluyorsa m·g."],
      ["Düşeyde başka kuvvet yok"], ["Eğik bastırmada geçersiz"], ["k_s yerine k_k kullanmak"]),
    None,
    "Duvara bastırma: f = mg (dengede), N = F, F_min = mg/k_s. F artınca f sabit kalır.",
    "2 kg'lık bir kitap, duvara yatay bir kuvvetle bastırılarak tutuluyor; k_s = 0,4. Kitabın düşmemesi için gerekli en küçük kuvveti bulunuz. Kuvvet 80 N'a çıkarılırsa sürtünme kuvveti kaç N olur? (g = 10 m/s²)",
    ["f = m·g = 20 N (dengede).", "k_s·F ≥ 20 → F_min = 20/0,4 = 50 N.", "F = 80 N: sürtünme yine f = 20 N (f_s,max = 0,4·80 = 32 N, ama kullanılan 20 N)."],
    "F_min = 50 N; F = 80 N iken sürtünme 20 N.",
    """
m, g, ks = 2.0, 10.0, 0.4
Fmin = m * g / ks
assert abs(Fmin - 50.0) < 1e-12
def friction_needed(F):
    fmax = ks * F
    assert fmax >= m * g - 1e-12      # düşmüyor
    return m * g
assert friction_needed(80.0) == 20.0
# eşiğin altında düşer
assert ks * 40.0 < m * g
""")

SOLUTIONS["friction-stacked-blocks-together"] = S(
    M(["Birlikte hareket: ortak ivme a. Tüm sistem: a = F_dış/Σm (zemin sürtünmesi varsa net dış kuvvet).",
       "Üst blok için ivmeyi sağlayan tek yatay kuvvet alt bloğun uyguladığı statik sürtünmedir: f = m_üst·a.",
       "Birlikte hareket koşulu: f ≤ k_s·m_üst·g → a ≤ k_s·g.",
       "En büyük kuvvet: F_max = (m_üst + m_alt)·k_s·g (kuvvet alt bloğa, zemin sürtünmesiz ise). Kuvvet üst bloğa uygulanıyorsa alt blok için f_s,max = k_s·m_üst·g ivme verir: a_max = k_s·m_üst·g/m_alt, F_max = (m_üst + m_alt)·a_max."],
      ["Bloklar birlikte (aynı ivmeyle) hareket ediyor", "Zeminle sürtünme verilmiş ya da ihmal"],
      ["Bloklar kaymaya başlarsa (farklı ivme) kapsam dışı", "Kuvvet hangi bloğa uygulanıyorsa f_s,max farklı bloktan hesaplanır"],
      ["Üst bloğa etki eden sürtünmeyi hep maksimum almak", "Ortak ivmeyi bulmadan sürtünme hesaplamak", "Yanlış bloğun N'sini kullanmak"]),
    M(["Üst bloğu hızlandıran tek kuvvet sürtünmedir; sürtünmenin üst sınırı üst bloğa verebileceği en büyük ivmeyi belirler: a ≤ k_s·g.", "Bu ivmeyi aşan kuvvette üst blok geride kalır (kayar)."],
      ["Birlikte hareket"], ["Nitel"], ["Sürtünmenin yön ve etkisini karıştırmak"]),
    M(["a_max = k_s·g; F_max = Σm·a_max. Gerçek F için: a = F/Σm, f_üst = m_üst·a, f_üst ≤ k_s·m_üst·g kontrolü."],
      ["Kuvvet alt bloğa, zemin sürtünmesiz"], ["Kuvvet üst bloğa ise formül değişir"], ["Kuvvetin uygulandığı bloğu karıştırmak"]),
    None,
    "Üst üste bloklar: üst bloğun ivmesini yalnız statik sürtünme verir → a_max = k_s·g. F_max = Σm·k_s·g (alt bloğa uygulanırsa).",
    "Sürtünmesiz yatay zeminde 3 kg'lık alt bloğun üstünde 2 kg'lık blok vardır; bloklar arası k_s = 0,5. Alt bloğa yatay F uygulanıyor. Bloklar kaymadan birlikte hareket edebilsin diye F en çok kaç N olmalıdır? F = 10 N iken üst bloğa etki eden sürtünme nedir? Kuvvet üst bloğa uygulansaydı F_max ne olurdu? (g = 10 m/s²)",
    ["a_max = k_s·g = 5 m/s²; F_max = (2 + 3)·5 = 25 N.", "F = 10 N: a = 10/5 = 2 m/s², f_üst = 2·2 = 4 N (≤ 0,5·20 = 10 N: kaymaz).",
     "Kuvvet üst bloğa: alt bloğu yalnız f_s,max = 10 N hızlandırır, a_max = 10/3 m/s²; F_max = 5·10/3 ≈ 16,67 N."],
    "F_max = 25 N; F = 10 N için f = 4 N; kuvvet üst bloğa uygulansaydı F_max ≈ 16,67 N.",
    """
g, ks = 10.0, 0.5
mu, ml = 2.0, 3.0
a_max = ks * g
Fmax = (mu + ml) * a_max
assert abs(Fmax - 25.0) < 1e-12
a = 10.0 / (mu + ml)
f_up = mu * a
assert abs(f_up - 4.0) < 1e-12 and f_up <= ks * mu * g
# kuvvet üst bloğa
a_max2 = ks * mu * g / ml
F2 = (mu + ml) * a_max2
assert abs(F2 - 50.0 / 3.0) < 1e-12
# F_max'ta f_üst tam sınırda
assert abs(mu * a_max - ks * mu * g) < 1e-12
""")

SOLUTIONS["friction-variables-data"] = S(
    M(["Tablodan hangi niceliklerin birlikte değiştiğini belirle.",
       "Bir değişkenin etkisini incelemek için yalnız o değişkenin değiştiği, diğerlerinin sabit kaldığı satırları karşılaştır (kontrol değişkeni ilkesi).",
       "f/N oranını hesapla: sabitse f ∝ N ve katsayı k = f/N; alan değişirken f değişmiyorsa sürtünme alandan bağımsızdır.",
       "Yüzey türü değişince f/N değişiyorsa sürtünme yüzey çiftine bağlıdır."],
      ["Sürtünme modeli (Coulomb)", "Veri tablosu kontrollü deneyden"],
      ["Birden çok değişken birlikte değişen satırlardan sonuç çıkarılamaz"],
      ["Birden çok değişkenin değiştiği satırları karşılaştırmak", "Alanın sürtünmeyi artırdığını sanmak"]),
    M(["Sürtünme normal kuvvetle orantılı; ağır cisim yüzeye daha çok bastırır.", "Alan artınca basınç azalır, toplam kuvvet değişmez: alan etkisiz."],
      ["Genel model"], ["Nitel"], ["Alan-sürtünme yanılgısı"]),
    M(["Sütun oranı: f/N sabit mi? Alan sütununda aynı N satırlarında f eşit mi?"],
      ["Tablo soruları"], ["Hatalı ölçümleri ayırmak gerekir"], ["Oranı hesaplamadan yargılamak"]),
    None,
    "Veri tablosu: aynı N, farklı alan → f aynıysa alandan bağımsız. f/N sabitse f ∝ N. Yüzey değişince f/N değişir.",
    "Aynı cisimle yapılan deneyin sonuçları: (1) 2 kg, 100 cm² yüzey, ahşap-ahşap, f = 6 N; (2) 2 kg, 200 cm², ahşap-ahşap, f = 6 N; (3) 4 kg, 100 cm², ahşap-ahşap, f = 12 N; (4) 2 kg, 100 cm², ahşap-cam, f = 4 N. Sürtünmenin bağlı olduğu ve olmadığı değişkenleri belirleyiniz. (g = 10 m/s²)",
    ["(1)–(2): yalnız alan değişiyor, f aynı → alandan bağımsız.", "(1)–(3): yalnız kütle (N) iki kat → f iki kat → f ∝ N.",
     "(1)–(4): yalnız yüzey çifti değişiyor, f değişiyor → yüzey türüne bağlı.", "k = f/N: ahşap-ahşap 6/20 = 0,3; ahşap-cam 4/20 = 0,2."],
    "Sürtünme N'ye ve yüzey çiftine bağlıdır; temas alanına bağlı değildir. k(ahşap-ahşap) = 0,3, k(ahşap-cam) = 0,2.",
    """
g = 10.0
rows = [dict(m=2, A=100, s='ahsap', f=6.0), dict(m=2, A=200, s='ahsap', f=6.0),
        dict(m=4, A=100, s='ahsap', f=12.0), dict(m=2, A=100, s='cam', f=4.0)]
k = [r['f'] / (r['m'] * g) for r in rows]
assert abs(k[0] - 0.3) < 1e-12 and abs(k[1] - 0.3) < 1e-12 and abs(k[2] - 0.3) < 1e-12 and abs(k[3] - 0.2) < 1e-12
assert rows[0]['f'] == rows[1]['f']        # alan bağımsız
assert abs(rows[2]['f'] / rows[0]['f'] - rows[2]['m'] / rows[0]['m']) < 1e-12   # f ∝ N
assert rows[3]['f'] != rows[0]['f']        # yüzey bağımlı
""")

# ============================ FİZ.11.1.8 ============================
SOLUTIONS["terminal-velocity-graph"] = S(
    M(["ϑ-t grafiğinde eğim = ivme: başlangıçta eğim büyük (a ≈ g), eğim azalıyor (direnç artıyor).",
       "Eğim sıfır (yatay kısım) = ivme sıfır = net kuvvet sıfır → direnç kuvveti = ağırlık, hız sabit: limit hız.",
       "Paraşüt açılınca direnç aniden ağırlıktan büyük olur: net kuvvet yukarı, ivme yukarı (hız azalır), hız yeni, daha küçük limit hıza yaklaşır.",
       "Yön değişmez (paraşütçü hâlâ aşağı iniyor); yalnız hızın büyüklüğü azalır."],
      ["Hava direnci hıza bağlı artıyor", "Cisim yeterince yüksekten düşüyor"],
      ["Limit hız sayısal olarak hesaplanmaz (program: yorum düzeyi)", "Çok kısa düşmede limit hıza ulaşılmaz"],
      ["Paraşüt açılınca yukarı çıktığını sanmak", "Limit hızda ivmenin g olduğunu sanmak", "Eğimin azalmasını hızın azalması sanmak"]),
    M(["Düşerken hız arttıkça direnç artar; ağırlık sabittir. Net kuvvet = ağırlık − direnç azalır.", "Direnç ağırlığa eşit olunca net kuvvet sıfır olur ve hız artmayı keser.",
       "Limit hızdan hızlı gidiyorsan direnç ağırlıktan büyük, yavaşlarsın; limit hız bir 'denge hızıdır'."],
      ["Hıza bağlı direnç"], ["Nitel"], ["Limit hız = hızın sıfır olması sanmak"]),
    M(["Grafik tarama: (1) eğim azalan eğri = hâlâ hızlanıyor ama ivme küçülüyor; (2) yatay = limit; (3) eğri aşağı bükülüyorsa direnç ağırlığı aşıyor."],
      ["ϑ-t grafiği"], ["Ölçek ve eksenler okunmalı"], ["Eksen karışması"]),
    None,
    "Yatay kısım = limit hız (F_net = 0, direnç = ağırlık). Eğim = ivme. Paraşüt açılınca hız azalır ve yeni küçük limit hıza oturur; paraşütçü yukarı çıkmaz.",
    "Bir paraşütçünün ϑ-t grafiğinde hız 0'dan başlayıp artarak yaklaşık 50 m/s'de yatay hale geliyor; sonra paraşüt açılınca hız azalarak 6 m/s'de tekrar yatay oluyor. Hangi bölgelerde ivme sıfırdır, direnç kuvveti ile ağırlık ilişkisi nasıldır, paraşüt açıldığı anda ivmenin yönü nedir?",
    ["İlk yatay bölge (50 m/s) ve son yatay bölge (6 m/s): eğim 0 → ivme 0 → net kuvvet 0 → direnç = ağırlık.",
     "Paraşüt açılma anı: hız azalıyor, eğim negatif → ivme yukarı yönlü (hıza zıt); direnç > ağırlık.",
     "Yeni limit hız 6 m/s < 50 m/s çünkü kesit alanı arttıkça aynı direnç daha küçük hızda sağlanır."],
    "İvme iki yatay bölgede sıfırdır (direnç = ağırlık); paraşüt açılırken direnç > ağırlık ve ivme yukarı yönlüdür; yeni limit hız daha küçüktür.",
    """
# Niteliksel mantığı sınayan basit model (yalnız doğrulama amaçlı; sayısal hesap programın dışındadır)
m, g = 80.0, 10.0
def simulate(k_list, t_open, T=120.0, dt=0.001):
    v, t = 0.0, 0.0
    out = []
    while t < T:
        k = k_list[0] if t < t_open else k_list[1]
        a = g - (k / m) * v * v
        v += a * dt
        t += dt
        out.append((t, v, a))
    return out
data = simulate([0.31, 21.8], t_open=60.0)
# serbest düşüş sonunda limit hıza yakın, ivme ~ 0
t60 = [d for d in data if abs(d[0] - 59.9) < 5e-4][0]
assert abs(t60[2]) < 0.05 and abs(t60[1] - (m * g / 0.31) ** 0.5) < 0.5
# ivme sürekli azalıyor
before = [d for d in data if d[0] < 60.0]
assert all(before[i + 1][2] <= before[i][2] + 1e-9 for i in range(0, len(before) - 1, 500))
# paraşüt sonrası hız azalıyor, ivme negatif (yukarı) ve yeni limit hıza oturuyor
after = [d for d in data if d[0] > 60.0]
assert after[10][2] < 0
assert abs(after[-1][1] - (m * g / 21.8) ** 0.5) < 0.2 and after[-1][1] < t60[1]
""")

SOLUTIONS["terminal-velocity-variables"] = S(
    M(["Limit hızda net kuvvet sıfırdır: direnç = ağırlık (F_d = m·g).",
       "Direnç kesit alanı A ve hızın büyüklüğüyle artar (ϑ² ile); ağırlık m ile artar.",
       "Aynı F_d = mg koşulunu sağlayan hız: ϑ_limit ∝ √(m/A). Kütle artarsa limit hız artar; kesit alanı artarsa azalır; yükseklikten bağımsızdır.",
       "Sıralama: kütle ve kesit alanını birlikte karşılaştır; yalnız biri sabitse tek değişkene göre yorumla."],
      ["Hava direnci hızın karesiyle orantılı modeli (kitap Tablo 1.2)", "Aynı şekil faktörü/ortam yoğunluğu"],
      ["Program sayısal limit hız hesabını istemez; yalnız ilişki (daha büyük/küçük, kaç kat) yorumlanır", "Çok yavaş (viskoz) hareketlerde direnç hızla doğrusal olabilir"],
      ["ϑ ∝ m/A almak", "Kütle büyükse limit hız küçük sanmak", "Limit hızı düşme yüksekliğine bağlamak"]),
    M(["Ağır cismi durdurmak için daha büyük direnç gerekir; direnç hızla büyüdüğü için ağır cisim daha yüksek hızda dengeye gelir.",
       "Geniş yüzey havayı çok iter: aynı hızda daha çok direnç → küçük limit hızda denge."],
      ["Direnç hız ve alanla artıyor"], ["Nitel"], ["Direnç ile ağırlığı karıştırmak"]),
    M(["Oran: kütle aynıysa alan 4 kat → limit hız 1/2; alan aynıysa kütle 4 kat → limit hız 2 kat. Genel: ϑ₂/ϑ₁ = √((m₂/m₁)/(A₂/A₁)).", "Program yalnız 'kaç kat' mantığına kadar kullanılan yorum düzeyinde."],
      ["Direnç ∝ A·ϑ²"], ["Sayısal limit hız programda yok; yalnız oran mantığı"], ["Karekökü unutmak"]),
    None,
    "Limit hız: F_d = mg → ϑ ∝ √(m/A). Daha ağır → daha büyük limit hız; daha geniş → daha küçük. Yüksekliğe bağlı değil.",
    "Eşit kütleli K, L, M, N cisimlerinin kesit alanları sırasıyla A, 2A, 4A, 8A'dır. Limit hızlarını büyükten küçüğe sıralayınız. M'nin limit hızı K'ninkinin kaç katıdır? Kütlesi 4 katına çıkarılan K cisminin limit hızı kaç kat olur?",
    ["ϑ ∝ √(m/A): m eşit → ϑ ∝ 1/√A.", "Sıralama: K > L > M > N (alan büyüdükçe limit hız küçülür).",
     "M için A 4 kat → ϑ_M/ϑ_K = 1/√4 = 1/2.", "K için m 4 kat → ϑ 2 kat olur."],
    "K > L > M > N; ϑ_M = ϑ_K/2; kütle 4 katına çıkınca limit hız 2 katına çıkar.",
    """
import math
g = 10.0
k = 0.5                         # yalnızca oran testi için sembolik katsayı
vt = lambda m, A: math.sqrt(m * g / (k * A))
vK, vL, vM, vN = [vt(1.0, A) for A in (1.0, 2.0, 4.0, 8.0)]
assert vK > vL > vM > vN
assert abs(vM / vK - 0.5) < 1e-12
assert abs(vt(4.0, 1.0) / vt(1.0, 1.0) - 2.0) < 1e-12
# F_d = m g limit koşulunu doğrular
v = vt(1.0, 4.0)
assert abs(k * 4.0 * v ** 2 - 1.0 * g) < 1e-9
# yükseklikten bağımsız (formülde h yok)
assert vt(1.0, 4.0) == vt(1.0, 4.0)
""")

SOLUTIONS["terminal-velocity-daily-life"] = S(
    M(["Bağlamdaki cismi tanımla ve limit hıza etki eden değişkenleri belirle: kütle (ağırlık), kesit alanı, şekil.",
       "Limit hız koşulu: direnç = ağırlık. Kesit alanı büyük/yüzey geniş ise limit hız küçüktür; kütle büyük ise limit hız büyüktür.",
       "Yorum: küçük limit hız = yavaş düşme (karahindiba tohumu, paraşüt); büyük limit hız = hızlı düşme (taş, yoğun cisim).",
       "Havasız ortamda limit hız olmaz; hava direnci düşme hızını sınırlar (yağmur damlası yere zarar vermez)."],
      ["Hava direnci var", "Cisim yeterince yüksekten düşüyor"],
      ["Sayısal hesap programda yok", "Hava direncinin etkisiz olduğu kısa düşüşlerde serbest düşme gibi davranır"],
      ["Bağlamdaki değişkeni fiziksel niceliğe bağlayamamak", "Hava direnci olmasa da aynı hızla ineceğini sanmak"]),
    M(["Doğa ve teknoloji, kesit alanını büyüterek limit hızı düşürür (tohum tüyleri, paraşüt, yağmur damlasının küçülmesi).", "Limit hız sayesinde yağmur damlaları saniyede yüzlerce metre değil, birkaç m/s ile yere ulaşır."],
      ["Direnç-ağırlık dengesi"], ["Nitel"], ["Hava direncini yok saymak"]),
    M(["Anahtar: 'kesit alanı ↑ ⇒ limit hız ↓; kütle ↑ ⇒ limit hız ↑'. Soru metnini bu iki kurala göre eleyin."],
      ["Standart bağlam soruları"], ["İkisi birlikte değişirse oran bakılır"], ["Tek değişkene bakıp ötekini yok saymak"]),
    None,
    "Bağlam sorusu = 'hangi değişken (kesit/şekil/kütle) limit hızı nasıl etkiler?' Tohum, paraşüt, damla: geniş yüzey = yavaş düşüş; havasız ortamda limit hız yoktur.",
    "Aynı yükseklikten (kütleleri eşit) iki tohum bırakılıyor: birinin tüyleri geniş (A büyük), diğeri tüysüz (A küçük). Limit hızlarını karşılaştırınız ve hangisinin daha uzağa taşınabileceğini söyleyiniz. Yağmur damlası hava direnci olmasaydı 2000 m yükseklikten yere hangi hızla çarpardı?",
    ["Geniş yüzey → direnç aynı hızda daha büyük → daha küçük limit hızda denge: tüylü tohumun limit hızı küçük.",
     "Daha uzun havada kalır → rüzgârla daha uzağa taşınır.", "Hava direncisiz: ϑ = √(2gh) = √(2·10·2000) = 200 m/s (≈ 720 km/h); hava direnci bu hızı birkaç m/s'ye düşürür."],
    "Tüylü tohumun limit hızı daha küçüktür ve daha uzağa taşınır. Direncisiz çarpma hızı 200 m/s olurdu.",
    """
import math
g, h = 10.0, 2000.0
v_free = math.sqrt(2 * g * h)
assert abs(v_free - 200.0) < 1e-9
# kaba model: v_t = sqrt(m g / (k A)); A büyük -> v_t küçük -> havada kalma süresi uzun
m, k = 1.0, 0.1
vt = lambda A: math.sqrt(m * g / (k * A))
t_air = lambda A: h / vt(A)
assert vt(10.0) < vt(1.0)
assert t_air(10.0) > t_air(1.0)
""")

SOLUTIONS["drag-variables-data"] = S(
    M(["Tek değişkenin değiştiği satırları seç (diğerleri sabit).",
       "Hız-direnç ilişkisi için A sabit satırlarda F_d/ϑ² oranını hesapla: sabitse F_d ∝ ϑ².",
       "Alan-direnç ilişkisi için ϑ sabit satırlarda F_d/A oranına bak: sabitse F_d ∝ A.",
       "Eksik değeri bulunan orantıyla (ör. ϑ 3 katına çıkınca F_d 9 katına çıkar) hesapla."],
      ["Kontrollü deney verisi", "Direnç hıza göre artıyor"],
      ["Sayısal limit hız programda yok; veriden orantı çıkarma düzeyinde kalınır", "Birden fazla değişkenin değiştiği satırlar karşılaştırılamaz"],
      ["Kontrol değişkenini sabit tutmadan karşılaştırmak", "Hız ile direnci doğrusal orantılı sanmak"]),
    M(["Hız iki katına çıkarsa her saniyede çarpan hava miktarı iki, her parçacığa verilen çarpma etkisi iki kat olur → direnç dört kat.", "Alan iki katına çıkarsa çarpan hava miktarı iki katına çıkar → direnç iki kat."],
      ["Hava direnci"], ["Nitel"], ["Doğrusal sanmak"]),
    M(["Oran testi: F_d/ϑ² sabit mi? F_d/A sabit mi? Sabit olan orantıyı gösterir; hesap gerekmez."],
      ["Tablo soruları"], ["Ölçüm hatası olabilir"], ["Oranı almamak"]),
    None,
    "Direnç verisi: ϑ iki katı → F_d dört katı (karesel); A iki katı → F_d iki katı. Tek değişkenli satırları karşılaştır.",
    "Bir deneyde A = 2 m² için ϑ = 2, 4, 6 m/s hızlarında direnç 3, 12, 27 N ölçülüyor. Ayrıca ϑ = 4 m/s sabitken A = 1, 2, 3 m² için direnç 6, 12, 18 N'dur. Direncin ϑ ve A ile ilişkisini bulup ϑ = 8 m/s, A = 4 m² için direnci tahmin ediniz.",
    ["F_d/ϑ² = 3/4 = 12/16 = 27/36 = 0,75 → F_d ∝ ϑ².", "F_d/A = 6/1 = 12/2 = 18/3 = 6 → F_d ∝ A.",
     "F_d = c·A·ϑ²; 12 = c·2·16 → c = 0,375; ϑ = 8, A = 4: F_d = 0,375·4·64 = 96 N."],
    "F_d ∝ A·ϑ²; ϑ = 8 m/s ve A = 4 m² için F_d = 96 N.",
    """
v = [2, 4, 6]; F = [3, 12, 27]
assert all(abs(F[i] / v[i] ** 2 - 0.75) < 1e-12 for i in range(3))
A = [1, 2, 3]; F2 = [6, 12, 18]
assert all(abs(F2[i] / A[i] - 6.0) < 1e-12 for i in range(3))
# A = 2 satırından c: 12 = c*2*16
c = 12 / (2 * 16)
assert abs(c * 2 * 4 ** 2 - 12) < 1e-12
assert abs(c * 4 * 8 ** 2 - 96.0) < 1e-9
# tutarlılık: A=2 hız satırında c*A*v^2 = F
assert all(abs(0.375 * 2 * v[i] ** 2 - F[i]) < 1e-9 for i in range(3))
""")

# ============================ FİZ.11.1.9 ============================
SOLUTIONS["circular-velocity-direction"] = S(
    M(["Cismin bulunduğu noktadan yarıçap vektörünü (merkezden cisme) çiz.",
       "Hız vektörü yörüngeye teğettir, yani yarıçap vektörüne diktir; yönü dönme yönündedir (saat yönünde ya da tersi).",
       "Dört temel noktada (üst, sağ, alt, sol) teğet yönü dönme yönüne göre belirle.",
       "Sürat sabit, ama hız vektörünün yönü sürekli değişir; yarıçap vektörünün tarama açısı hız vektörünün dönme açısına eşittir."],
      ["Düzgün çembersel hareket", "Dönme yönü verilmiş"],
      ["Dönme yönü verilmemişse iki yön de mümkündür"],
      ["Hızı merkeze doğru çizmek", "Süratin sabit olmasını hızın sabit olması sanmak", "Dönme yönünü hesaba katmamak"]),
    M(["Cisim çemberden kopacak olsa teğet doğrultuda gider: bu yüzden hız teğettir.", "Yarıçap vektörü döndükçe hız vektörü de aynı açıyla döner."],
      ["Çembersel hareket"], ["Nitel"], ["Merkeze doğru hız çizmek"]),
    M(["Kural: ϑ ⟂ r ve dönme yönünde. Saat yönünde dönmede üstte → sağa, sağda → aşağı, altta → sola, solda → yukarı."],
      ["Saat yönünde dönme"], ["Ters yönde dönmede hepsi zıt"], ["Yönü karıştırmak"]),
    None,
    "Çembersel harekette hız = teğet + dönme yönünde. 'Hız sabit' ifadesi hep yanlıştır (sürat sabit olabilir).",
    "Saat yönünde düzgün çembersel hareket yapan bir cismin çemberin üst, sağ, alt ve sol noktalarındaki hız yönlerini yazınız. Cismin 90° taradığı sürede hız vektörü ne kadar döner?",
    ["Teğet ve dönme yönünde: üst → sağ, sağ → aşağı, alt → sol, sol → yukarı.", "Yarıçap vektörü 90° taradıysa hız vektörü de 90° döner (iki vektör hep dik)."],
    "Üst: sağa, sağ: aşağı, alt: sola, sol: yukarı; hız vektörü de 90° döner.",
    """
import math
def vel(phi, sign=-1.0, v=1.0):
    # sign=-1 saat yönü; konum (cos,sin); hız teğet
    return (sign * -math.sin(phi) * v, sign * math.cos(phi) * v)
pos = lambda phi: (math.cos(phi), math.sin(phi))
dirs = {}
for name, phi in (('sag', 0), ('ust', math.pi / 2), ('sol', math.pi), ('alt', 3 * math.pi / 2)):
    p, vv = pos(phi), vel(phi)
    assert abs(p[0] * vv[0] + p[1] * vv[1]) < 1e-12      # r ⟂ v
    dirs[name] = (round(vv[0]), round(vv[1]))
assert dirs['ust'] == (1, 0) and dirs['sag'] == (0, -1) and dirs['alt'] == (-1, 0) and dirs['sol'] == (0, 1)
# 90° taranınca hız açısı da 90° değişir
a1 = math.atan2(vel(0)[1], vel(0)[0]); a2 = math.atan2(vel(-math.pi / 2)[1], vel(-math.pi / 2)[0])
assert abs(abs(a1 - a2) - math.pi / 2) < 1e-12
""")

SOLUTIONS["string-cut-trajectory"] = S(
    M(["İp koptuğu anda cismin hızını belirle: bu an hız vektörü teğettir (yarıçapa dik).",
       "Kopmadan sonra merkezcil kuvvet ortadan kalkar; yatay masada (sürtünmesiz) net kuvvet sıfır: cisim teğet doğrultuda sabit hızla gider (Newton 1).",
       "Düşey düzlemde ya da yükseklikte kopmuşsa kopma anındaki hız bu iki boyutlu harekette ilk hızdır: yönü teğet, ivmesi g (iki boyutlu hareket çözümü).",
       "Yörüngeyi çiz: yatay masada doğru; düşeyde parabol (yalnız ağırlık etkili)."],
      ["Kopma anındaki hız teğet", "Kopmadan sonra ek kuvvet yok (yatay: sürtünmesiz; düşey: yalnız yer çekimi)"],
      ["Yatay masada sürtünme varsa yavaşlar", "Çember içinden kopan cismin rotası çember düzlemine göre kontrol edilir"],
      ["Merkezkaç kuvveti gerçek sanmak", "Cisim eğri yolda devam eder sanmak", "Radyal dışa uçar sanmak"]),
    M(["Cisim ipin çektiği için çemberde kalır; ip kopunca eylemsizliği nedeniyle hızını korur.", "Kopma anındaki hız yönünde, merkezden uzaklaşan ama radyal olmayan (teğet) bir yol izler."],
      ["Newton'un 1. yasası"], ["Nitel"], ["Merkezkaç kuvveti sanmak"]),
    M(["Yatay masada kopma = teğet doğru. Düşey düzlemde kopma + yükseklik → teğet yönde iki boyutlu hareket (tepe noktasında yatay ilk hızlı iki boyutlu hareket mantığı)."],
      ["Standart senaryolar"], ["Başka kuvvet varsa geçersiz"], ["Kopma noktasını yanlış belirlemek"]),
    None,
    "İp koptu → teğet doğrultuda (yatay masada doğru). Radyal dışa ya da eğri gidiş seçenekleri tuzaktır.",
    "Sürtünmesiz yatay masada r = 0,5 m yarıçaplı çemberde 4 m/s süratle dönen cismin ipi, cisim çemberin (0,5; 0) noktasındayken kopuyor. Cismin kopmadan 2 s sonra konumu nedir? Tepe noktası yerden 1,25 m yükseklikte olan düşey çemberde ip, cisim tepedeyken (3 m/s yatay hızla) koparsa cismin yere düştüğü yatay uzaklık nedir? (g = 10 m/s²)",
    ["Teğet yön: (0; ±4) m/s. Teğet yön +y alınırsa yatay masada sabit hızla 2 s'de 8 m yol alır → konum (0,5; 8); merkezden uzaklık √(0,25 + 64) ≈ 8,03 m (artar).",
     "Düşey düzlem: tepe noktasında hız yatay, 1,25 m yükseklikten yatay ilk hızlı hareket: t = √(2·1,25/10) = 0,5 s; menzil = 3·0,5 = 1,5 m."],
    "Yatay masada teğet doğru boyunca 8 m gider; düşey çemberin tepesinde kopmada menzil 1,5 m.",
    """
import math
r, v, T = 0.5, 4.0, 2.0
x, y = r, 0.0
# teğet yön +y (örnek): sabit hız
x2, y2 = x + 0.0 * T, y + v * T
assert abs(x2 - 0.5) < 1e-12 and abs(y2 - 8.0) < 1e-12
d0 = math.hypot(x, y); d1 = math.hypot(x2, y2)
assert d1 > d0                       # merkezden uzaklaşır
# doğru yol: hız yönü sabit
step = lambda t: (x, y + v * t)
dirs = [(step(t + 1e-3)[0] - step(t)[0], step(t + 1e-3)[1] - step(t)[1]) for t in (0.1, 1.0, 1.9)]
assert all(abs(d[0]) < 1e-12 and abs(d[1] - v * 1e-3) < 1e-9 for d in dirs)
# düşey çember tepesi: yatay ilk hızlı iki boyutlu hareket
g, h, v_top = 10.0, 1.25, 3.0
t = math.sqrt(2 * h / g)
assert abs(t - 0.5) < 1e-12 and abs(v_top * t - 1.5) < 1e-12
""")

SOLUTIONS["circular-analogies"] = S(
    M(["Verilen her harekette ortak özellikleri ara: yörünge çember, merkez sabit, sürat sabit, yarıçap sabit.",
       "Hız vektörü teğet ve sürekli yön değiştiriyor → hız değişiyor → merkeze doğru ivme var (merkezcil ivme).",
       "Net kuvvet merkeze yönelik ve büyüklüğü sabittir (düzgün çembersel hareket).",
       "Genellemeyi yaz: düzgün çembersel hareket = sabit süratli, hızı sürekli yön değiştiren ve ivmesi (merkezcil) sıfır olmayan harekettir."],
      ["Düzgün çembersel hareket"],
      ["Sürati değişen hareketlerde teğetsel ivme de vardır (müfredat dışı)"],
      ["Sabit sürat ile ivmesizliği özdeşleştirmek", "Sürat ile hızı karıştırmak"]),
    M(["İvme = hızın (vektör) değişimi. Hızın yönü değişiyorsa sürat sabit olsa da ivme vardır.", "Merkezcil ivme hızın büyüklüğünü değil yönünü değiştirir."],
      ["Genel"], ["Nitel"], ["İvme = sürat değişimi sanmak"]),
    M(["Seçenekte 'ivme sıfır' ya da 'hız sabit' ifadelerini ele; 'merkeze yönelik ivme', 'sabit sürat', 'teğet hız' doğru çıkar."],
      ["Kavramsal sorular"], ["Hesaplı sorulara uygulanmaz"], ["Tek kelimeye bakıp karar vermek"]),
    None,
    "Düzgün çembersel harekette sürat sabit ama hız ve ivme (merkeze doğru) değişen vektörlerdir. 'İvme yok' seçeneği tuzak.",
    "Düzgün çembersel hareket yapan bir cismin birbirinden çok az farklı iki anındaki hız vektörleri alınarak ortalama ivmesinin büyüklüğünü sayısal olarak yaklaşık hesaplayınız (r = 2 m, süratle 4 m/s). Beklenen merkezcil ivme nedir?",
    ["Merkezcil ivme a = ϑ²/r = 16/2 = 8 m/s² (merkeze doğru).", "Küçük Δt için |Δϑ|/Δt ≈ 8 m/s² (sürat sabit olmasına rağmen ivme sıfır değil)."],
    "a = 8 m/s², merkeze doğru; sürat sabit olsa da ivme sıfır değildir.",
    """
import math
r, v = 2.0, 4.0
w = v / r
dt = 1e-6
v1 = (-v * math.sin(0.0), v * math.cos(0.0))
v2 = (-v * math.sin(w * dt), v * math.cos(w * dt))
a_num = math.hypot(v2[0] - v1[0], v2[1] - v1[1]) / dt
assert abs(a_num - v ** 2 / r) < 1e-4
assert abs(math.hypot(*v1) - math.hypot(*v2)) < 1e-12     # sürat aynı
# ivme yönü: hız değişimi merkeze doğru (-x yönü, konum (r, 0))
assert (v2[0] - v1[0]) < 0
""")

# ============================ FİZ.11.1.10 ============================
SOLUTIONS["circular-kinematics"] = S(
    M(["Verilen nicelikten başla: periyot T (bir tur süresi) ya da frekans f = 1/T (birim zamanda tur).",
       "Birimleri SI'ya çevir: devir/dakika → devir/saniye (böl 60); cm → m.",
       "ω = 2π/T = 2πf; ϑ = 2πr/T = 2πrf = ω·r.",
       "Merkezcil ivme a = ϑ²/r = ω²r = 4π²f²r."],
      ["Düzgün çembersel hareket (sürat sabit)", "Çember yarıçapı r verilmiş (çap değil)"],
      ["Sürat değişiyorsa bu bağıntılar anlık değerler için kullanılamaz", "Açı radyan cinsinden"],
      ["Dakikadaki devri saniyeye çevirmemek", "Çapı yarıçap almak", "ω'yı derece/s almak"]),
    M(["Bir tur 2π radyandır; ω birim zamanda taranan açıdır. Bir tur boyunca çevre 2πr yol alınır.", "Aynı cisimde tüm noktalar aynı ω ile döner; ϑ yarıçapla artar."],
      ["Düzgün çembersel hareket"], ["Nitel"], ["ω ile ϑ karıştırmak"]),
    M(["Özet zinciri: T → f = 1/T → ω = 2πf → ϑ = ωr → a = ωϑ. Dakikada n devir ise f = n/60 Hz."],
      ["SI birimleri"], ["Birim hatası kaçırılabilir"], ["60'a bölmeyi unutmak"]),
    None,
    "Dönme sorularında önce f ve T'yi SI'ya çevir, sonra ω = 2πf, ϑ = ωr. Çapı yarıçap yapmayı unutma.",
    "Çapı 1 m olan bir tekerlek dakikada 120 devir yapıyor. Frekansını, periyodunu, açısal hızını, kenardaki bir noktanın çizgisel süratini ve merkezcil ivmesini bulunuz. (π = 3,14 yaklaşımı kullanılabilir)",
    ["f = 120/60 = 2 Hz; T = 1/f = 0,5 s.", "ω = 2πf = 4π rad/s ≈ 12,57 rad/s.", "r = 0,5 m: ϑ = ω·r = 2π ≈ 6,28 m/s.", "a = ω²r = 16π²·0,5 = 8π² ≈ 78,96 m/s²."],
    "f = 2 Hz; T = 0,5 s; ω = 4π rad/s; ϑ = 2π ≈ 6,28 m/s; a = 8π² ≈ 79 m/s².",
    """
import math
rpm, d = 120.0, 1.0
r = d / 2
f = rpm / 60
T = 1 / f
w = 2 * math.pi * f
v = w * r
a = w ** 2 * r
assert abs(f - 2.0) < 1e-12 and abs(T - 0.5) < 1e-12
assert abs(w - 4 * math.pi) < 1e-12
assert abs(v - 2 * math.pi * r / T) < 1e-12 and abs(v - 2 * math.pi) < 1e-12
assert abs(a - v ** 2 / r) < 1e-9 and abs(a - 8 * math.pi ** 2) < 1e-9
assert abs(a - 4 * math.pi ** 2 * f ** 2 * r) < 1e-9
""")

SOLUTIONS["coupled-wheels"] = S(
    M(["Bağlantı türünü belirle: kayış/zincir/dişli/temas → bağlantı noktalarındaki çizgisel süratler eşit (ϑ₁ = ϑ₂); aynı mil/eksen → açısal hızlar (ω, f, T) eşit.",
       "Kayışlı çiftte ϑ = 2πrf eşitliğinden f₁r₁ = f₂r₂ (yarıçap ile frekans ters orantılı), T₁/r₁ = T₂/r₂ (T ile r doğru orantılı).",
       "Ortak milli tekerlerde ω eşit: ϑ₁/r₁ = ϑ₂/r₂ (çizgisel sürat yarıçapla doğru orantılı).",
       "Zincirleme sistemlerde (kayış + ortak mil) sırayla uygula: eşit olan niceliği bir sonraki tekere taşı."],
      ["Kayış kaymıyor, dişliler tam oturuyor", "Ortak mil rijit"],
      ["Kayış kayıyorsa ϑ eşitliği bozulur", "Zıt dönme yönleri (dişli) hız yönünü değiştirir ama büyüklüğünü değiştirmez"],
      ["Eşit niceliği yanlış seçmek (kayışta ω eşit sanmak)", "f ∝ r sanmak (doğrusu f ∝ 1/r)", "Çap ile yarıçapı karıştırmak"]),
    M(["Kayışın kaç metre aktığı iki tekerde de aynıdır → çizgisel sürat eşit. Küçük tekerlek bir turu daha çabuk atar → frekansı büyük.",
       "Ortak milde iki tekerlek aynı anda aynı açıyı tarar → açısal hız eşit; dıştaki nokta daha uzun yol alır → çizgisel sürat büyük."],
      ["Kayış / ortak mil"], ["Nitel"], ["Büyük tekerleğin frekansı büyük sanmak"]),
    M(["Kayış/temas: f·r sabit (ϑ eşit). Aynı mil: ϑ/r sabit (ω eşit). Oranı bir satırda kur ve hemen cevapla."],
      ["Kaymayan kayış / ortak mil"], ["Kayma varsa geçersiz"], ["Hangi niceliğin eşit olduğunu okumamak"]),
    None,
    "Kayış, zincir, dişli, temas = çizgisel sürat eşit; aynı mil = açısal hız eşit. Küçük yarıçap = büyük frekans (kayışta).",
    "Yarıçapları r_A = 10 cm ve r_B = 40 cm olan A ve B tekerlekleri bir kayışla bağlıdır; yarıçapı r_C = 20 cm olan C tekeri B ile ortak milli. A tekeri 12 Hz ile dönüyorsa B'nin frekansını, C'nin çizgisel sürat ve frekansını bulunuz. C'nin çizgisel sürati B'ninkinin kaç katıdır?",
    ["Kayış: ϑ_A = ϑ_B → f_A·r_A = f_B·r_B → f_B = 12·10/40 = 3 Hz.", "Ortak mil: f_C = f_B = 3 Hz.",
     "ϑ_C = 2π·f_C·r_C = 2π·3·0,2 = 1,2π ≈ 3,77 m/s; ϑ_B = 2π·3·0,4 = 2,4π.", "ϑ_C/ϑ_B = r_C/r_B = 0,5."],
    "f_B = 3 Hz; f_C = 3 Hz; ϑ_C = 1,2π ≈ 3,77 m/s; ϑ_C = ϑ_B/2.",
    """
import math
rA, rB, rC = 0.10, 0.40, 0.20
fA = 12.0
vA = 2 * math.pi * fA * rA
fB = vA / (2 * math.pi * rB)
assert abs(fB - 3.0) < 1e-12
fC = fB
vB = 2 * math.pi * fB * rB
vC = 2 * math.pi * fC * rC
assert abs(vC - 1.2 * math.pi) < 1e-12
assert abs(vC / vB - 0.5) < 1e-12
assert abs(vA - vB) < 1e-12          # kayışta çizgisel sürat eşit
assert abs(fA * rA - fB * rB) < 1e-12
""")

SOLUTIONS["horizontal-circle"] = S(
    M(["Yatay, sürtünmesiz düzlemde ip (ya da yay) gerilmesi tek yatay kuvvettir ve merkeze yönelir: F_m = T.",
       "Düşey denge: N = m·g (merkezcil kuvvete katılmaz).",
       "F_m = m·ϑ²/r = m·ω²r = m·(2π/T)²r = 4π²mf²r.",
       "Orantı için: ϑ sabitse F_m ∝ 1/r; ω sabitse F_m ∝ r; r sabitse F_m ∝ ϑ²."],
      ["Düzgün çembersel hareket", "İp kütlesiz ve yatay", "Sürtünmesiz yatay düzlem"],
      ["Sürat değişiyorsa teğetsel kuvvet de vardır", "İp eğikse düşey bileşen merkezcil kuvvete katılmaz ama T ≠ F_m olur"],
      ["İp gerilmesini ağırlığa eşit sanmak", "ϑ ve ω ile yazılan bağıntılarda r'nin üssünü karıştırmak", "Merkezcil kuvveti ayrı kuvvet olarak çizmek"]),
    M(["Cismin çember çizmesi için merkeze bir kuvvet 'çekmeli'; bu kuvveti ip sağlar. Merkezcil kuvvet yeni bir kuvvet değil, mevcut kuvvetlerin merkeze yönelik bileşkesidir.",
       "Daha hızlı dönen ya da daha ağır cismi çembere zorlamak için daha büyük gerilme gerekir; yarıçap büyürse (aynı hızda) daha az kuvvet yeter."],
      ["Çembersel hareket"], ["Nitel"], ["Merkezkaç kuvveti"]),
    M(["Oran kuralı: hız 2 kat → kuvvet 4 kat; yarıçap 2 kat (aynı hızda) → kuvvet yarısı; aynı açısal hızda yarıçap 2 kat → kuvvet 2 kat; kütle 2 kat → kuvvet 2 kat."],
      ["Aynı ip, aynı cisim"], ["Sürat sabit olmayınca geçersiz"], ["Orantıyı hız-açısal hız karışıklığıyla kurmak"]),
    None,
    "Yatay düzlemde ip gerilmesi = merkezcil kuvvet = mϑ²/r. Ağırlık yok (dik dengelenir). Hız kare, yarıçap ters.",
    "Sürtünmesiz yatay masada 0,5 kg'lık bir cisim 0,8 m uzunluğunda iple 4 m/s süratle düzgün çembersel hareket yapıyor. İp gerilmesini bulunuz. Sürat aynı kalıp ip 1,6 m'ye uzatılsaydı, ya da aynı açısal hızla dönerken yarıçap 1,6 m olsaydı gerilme ne olurdu? (g = 10 m/s²)",
    ["T = m·ϑ²/r = 0,5·16/0,8 = 10 N.", "r = 1,6 m, ϑ aynı: T = 0,5·16/1,6 = 5 N (yarıya iner).",
     "ω = ϑ/r = 5 rad/s; ω aynı r = 1,6 m: T = m·ω²·r = 0,5·25·1,6 = 20 N (iki katına çıkar)."],
    "T = 10 N; aynı hızda r = 1,6 m için 5 N; aynı ω ile r = 1,6 m için 20 N.",
    """
m, v, r = 0.5, 4.0, 0.8
T = m * v ** 2 / r
assert abs(T - 10.0) < 1e-12
assert abs(m * v ** 2 / 1.6 - 5.0) < 1e-12
w = v / r
assert abs(w - 5.0) < 1e-12
assert abs(m * w ** 2 * 1.6 - 20.0) < 1e-12
assert abs(m * w ** 2 * r - T) < 1e-12
""")

SOLUTIONS["rotating-platform-friction"] = S(
    M(["Platformda dönen cismin merkezcil kuvvetini statik sürtünme sağlar: f_s = m·ω²·r.",
       "Kaymanın eşiği: f_s,max = k_s·N = k_s·m·g.",
       "Eşik koşulu: k_s·m·g = m·ω²·r → ω_max = √(k_s·g/r); ya da r_max = k_s·g/ω².",
       "Kütle sadeleşir; ω'nın çizgisel karşılığı ϑ_max = √(k_s·g·r)."],
      ["Cisim platformla birlikte dönüyor (kaymıyor)", "Yatay platform", "Düzgün dönme"],
      ["Kayma başladıktan sonra kinetik sürtünme geçerli, merkezcil hareket sürmez", "Platform ivmeleniyorsa teğetsel bileşen eklenir"],
      ["Kinetik katsayıyı kullanmak", "Kütlenin sonucu etkilediğini sanmak", "Merkeze yakın cismin önce kaydığını sanmak"]),
    M(["Merkezden uzakta aynı ω için gereken merkezcil kuvvet daha büyüktür; sürtünmenin tavanı aynı kalır; bu yüzden uzaktaki cisim ilk kayar.",
       "Kütle hem gerekli kuvveti hem sürtünme tavanını aynı oranda büyüttüğü için eşiği değiştirmez."],
      ["Statik sürtünme sınırı"], ["Nitel"], ["Merkeze yakın cismi önce kayar sanmak"]),
    M(["Kısa yol: ω_max² · r = k_s·g sabit. Yarıçap iki katına çıkınca ω_max √2 kat azalır; yarıçap 4 katsa ω yarıya iner."],
      ["Aynı yüzey çifti"], ["Kütle ya da yüzey değişirse k_s değişebilir"], ["Karekökü unutmak"]),
    None,
    "Platform/kayma eşiği: k_s·g = ω²·r (kütle yok). Uzaktaki cisim önce kayar. Statik katsayı kullanılır.",
    "Yatay dönen bir platformun merkezinden 0,2 m uzakta duran bir cismin yüzeyle statik sürtünme katsayısı 0,5'tir. Cismin kaymadan dönebileceği en büyük açısal hızı bulunuz. Cisim 0,8 m uzağa konsa bu değer ne olurdu? Kütle 3 katına çıkarsa değişir mi? (g = 10 m/s²)",
    ["ω_max = √(k_s·g/r) = √(0,5·10/0,2) = √25 = 5 rad/s.", "r = 0,8: ω_max = √(5/0,8) = 2,5 rad/s (yarıya iner).", "Kütle sadeleşir: değişmez."],
    "ω_max = 5 rad/s; r = 0,8 m için 2,5 rad/s; kütleden bağımsız.",
    """
import math
g, ks = 10.0, 0.5
w = lambda r: math.sqrt(ks * g / r)
assert abs(w(0.2) - 5.0) < 1e-12 and abs(w(0.8) - 2.5) < 1e-12
# kütle bağımsızlığı: m ks g = m w^2 r
for m in (0.1, 1.0, 3.0):
    assert abs(m * ks * g - m * w(0.2) ** 2 * 0.2) < 1e-12
# eşiğin ötesinde gerekli kuvvet sürtünme sınırını aşar
assert 1.0 * 5.1 ** 2 * 0.2 > 1.0 * ks * g
""")

SOLUTIONS["vertical-circle-tension"] = S(
    M(["Cismin bulunduğu noktada merkeze yönelen ekseni seç (merkeze doğru pozitif).",
       "Tepe noktasında hem ip gerilmesi hem ağırlık merkeze (aşağı) yönelir: T + mg = mϑ²/r → T = mϑ²/r − mg.",
       "Dip noktasında gerilme merkeze (yukarı), ağırlık dışa (aşağı): T − mg = mϑ²/r → T = mϑ²/r + mg. Yan noktalarda ağırlık teğet, merkeze dik: T = mϑ²/r.",
       "Karşılaştır: dip > yan > tepe (sabit sürat kabulüyle); ip dip noktasında kopar. Kopma sınırı verilmişse T_dip ile karşılaştır."],
      ["Program ve kitapta sabit süratle (düzgün) dönen cisim kabulü", "İp kütlesiz ve esnemez"],
      ["Gerçekte (serbest dönüşte) sürat tepe ve dipte farklıdır; enerji korunumu gerekir (kitap s. 112)", "Çubuğa bağlı cisimde T negatif olabilir (itme)"],
      ["Tepede ağırlığın yönünü yanlış almak (T = mϑ²/r + mg yazmak)", "Tepe noktasında gerilmenin en büyük olduğunu sanmak", "Tüm noktalarda gerilmeyi eşit sanmak"]),
    M(["Dipte ip hem ağırlığı taşımalı hem cismi merkeze çekmeli: gerilme en büyük. Tepede ağırlık merkezcil kuvvete katkı yapar: gerilme en küçük.",
       "Yan noktada ağırlık teğet olduğu için merkezcil kuvvetin tamamını ip sağlar."],
      ["Çembersel hareket"], ["Nitel"], ["Merkezkaç kuvvetle açıklamak"]),
    M(["Aynı ϑ için T_dip − T_tepe = 2mg (sabit sürat kabulü). Yan: T_yan = (T_dip + T_tepe)/2. Sadece birini hesaplayıp diğerini ekleyerek bul."],
      ["Sabit sürat"], ["Gerçek (serbest) hareketle fark 6mg olur"], ["Kısa yolu serbest salınıma uygulamak"]),
    None,
    "Düşey çember: her noktada 'merkeze yönelen bileşke = mϑ²/r'. Tepe: T + mg, dip: T − mg. Dip gerilme en büyük; kopma dipte.",
    "0,4 kg'lık bir cisim 0,5 m uzunluğundaki iple düşey düzlemde 5 m/s sabit süratle döndürülüyor (sabit sürat kabulü). Tepe, yan ve dip noktalarındaki ip gerilmelerini bulunuz. İp 22 N'a dayanıyorsa nerede kopar? (g = 10 m/s²)",
    ["m·ϑ²/r = 0,4·25/0,5 = 20 N; mg = 4 N.", "Tepe: T = 20 − 4 = 16 N. Yan: T = 20 N. Dip: T = 20 + 4 = 24 N.", "24 N > 22 N → ip dip noktasında kopar."],
    "Tepe 16 N, yan 20 N, dip 24 N; ip dipte kopar.",
    """
m, g, r, v = 0.4, 10.0, 0.5, 5.0
Fm = m * v ** 2 / r
T_top, T_side, T_bot = Fm - m * g, Fm, Fm + m * g
assert (T_top, T_side, T_bot) == (16.0, 20.0, 24.0)
assert T_bot > 22.0 >= T_side
assert abs((T_bot - T_top) - 2 * m * g) < 1e-12
# Sınır göstergesi: serbest (enerji korunumlu) harekette tepe hızı 5 ise dipte v^2 = 25 + 4 g r
v_bot2 = v ** 2 + 4 * g * r
T_bot_real = m * v_bot2 / r + m * g
T_top_real = m * v ** 2 / r - m * g
assert abs((T_bot_real - T_top_real) - 6 * m * g) < 1e-9     # gerçek harekette fark 6mg
""")

SOLUTIONS["vertical-circle-min-speed"] = S(
    M(["Tepe noktasında merkeze yönelen kuvvetler: ip gerilmesi (ya da kovanın tepki kuvveti) ve ağırlık: T + mg = mϑ²/r.",
       "En küçük hız koşulu: ip gergin kalsın, T ≥ 0; sınırda T = 0.",
       "T = 0: mg = mϑ²/r → ϑ_min = √(g·r) (kütle sadeleşir).",
       "Hız bundan küçükse T negatif olması gerekirdi: ip gevşer, cisim çemberden ayrılır; su kovadan dökülür."],
      ["İpe (esnemez, yalnız çeker) bağlı cisim ya da kova", "Tepe noktası koşulu"],
      ["Çubuğa bağlı cisimde (çubuk itebilir) ϑ_min = 0 olabilir", "Hız tepe noktasındaki hızdır, dip hızı değil"],
      ["Koşulu T = mg olarak kurmak", "Merkezkaç kuvvetle açıklamak", "Kütleye bağlı sanmak"]),
    M(["Tepede ağırlık tek başına cismi çembere zorlayabilir: yeterince hızlıysa ip gevşemeden geçer.", "Sınır durumda cismi çembere ağırlık tek başına tutar; yavaşlarsan ağırlık merkezcil için 'fazla' gelir ve cisim içe düşer."],
      ["Ağırlık ≥ gerekli merkezcil kuvvet"], ["Nitel"], ["Ağırlığı unutmak"]),
    M(["ϑ_min = √(g·r): g = 10 için r = 0,9 → 3 m/s; r = 2,5 → 5 m/s; r = 10 → 10 m/s. Yarıçap 4 katı → hız 2 katı."],
      ["g = 10 m/s²"], ["Çubuk, ray ya da ek kuvvette geçersiz"], ["Karekökü almamak"]),
    None,
    "Düşey çember tepesi 'en az hız' ⇒ T = 0 ⇒ ϑ = √(g·r). Kütle yok. Çubuk varsa geçersiz.",
    "Yarıçapı 0,9 m olan düşey çemberde döndürülen bir kovadaki suyun dökülmemesi için kovanın tepe noktasındaki en küçük hızı bulunuz. Yarıçap 3,6 m olsaydı ne olurdu? 2 m/s hızla geçmeye çalışılsaydı ne olurdu? (g = 10 m/s²)",
    ["ϑ_min = √(g·r) = √(10·0,9) = 3 m/s.", "r = 3,6 m: √36 = 6 m/s (r 4 kat → ϑ 2 kat).", "2 m/s < 3 m/s: gerekli merkezcil ivme ϑ²/r = 4,4 m/s² < g; ağırlık fazla gelir, su dökülür."],
    "ϑ_min = 3 m/s; r = 3,6 m için 6 m/s; 2 m/s ile geçilemez (su dökülür).",
    """
import math
g = 10.0
vmin = lambda r: math.sqrt(g * r)
assert abs(vmin(0.9) - 3.0) < 1e-12 and abs(vmin(3.6) - 6.0) < 1e-12
for m in (0.1, 1.0, 10.0):
    assert abs(m * g - m * vmin(0.9) ** 2 / 0.9) < 1e-12          # T=0 koşulu, kütleden bağımsız
v = 2.0
T_required = 1.0 * v ** 2 / 0.9 - 1.0 * g                          # T = m v^2/r - m g
assert T_required < 0                                              # ip itemez -> geçilemez
""")

SOLUTIONS["hump-bridge"] = S(
    M(["Aracı noktasal cisim say; merkeze yönelen ekseni seç.",
       "Tümsek tepesinde merkez aşağıdadır: mg − N = mϑ²/r → N = mg − mϑ²/r (ağırlıktan küçük).",
       "Çukur dibinde merkez yukarıdadır: N − mg = mϑ²/r → N = mg + mϑ²/r (ağırlıktan büyük).",
       "Yolu terk koşulu (tümsek): N = 0 → ϑ = √(g·r); hız bundan büyükse araç yoldan ayrılır."],
      ["Tümsek/çukur dairesel yay kabulü", "Sabit sürat", "Araç noktasal"],
      ["Sürat değişiyorsa teğetsel bileşen de olur", "Eğri yay çember değilse yarıçap anlık eğrilik yarıçapı alınır"],
      ["mg − N yerine N − mg yazmak", "Tümsekte normal kuvveti ağırlıktan büyük sanmak", "Merkezkaçla açıklamak"]),
    M(["Tümsekte aracın yörüngesi aşağıya doğru kıvrılıyor: ağırlığın bir kısmı bu kıvrılmayı sağlar, yol az iter. Çukurda yörünge yukarı kıvrılır: yol hem ağırlığı taşır hem kıvrılmayı sağlar → daha çok iter.",
       "Hız arttıkça tümsekte yolun itmesi azalır, sıfıra inince araç yoldan ayrılır."],
      ["Çembersel yay"], ["Nitel"], ["Hissedilen 'hafifleme'yi yanlış açıklamak"]),
    M(["Tümsek: N = m(g − ϑ²/r); çukur: N = m(g + ϑ²/r); ayrılma ϑ² = gr."],
      ["g = 10 m/s²"], ["Eğrilik yarıçapı bilinmeli"], ["Yarıçapı çapla karıştırmak"]),
    None,
    "Tümsek tepesi: N < mg (mg − N = mϑ²/r); çukur dibi: N > mg. N = 0 → ϑ = √(g·r).",
    "800 kg'lık bir araç 40 m yarıçaplı dairesel bir tümseğin tepesinden 10 m/s hızla geçiyor. Tepedeki normal kuvveti bulunuz. Aynı yarıçaplı çukurun dibinden aynı hızla geçseydi normal kuvvet ne olurdu? Tümsekte yolu terk eden hız nedir? (g = 10 m/s²)",
    ["mϑ²/r = 800·100/40 = 2000 N; mg = 8000 N.", "Tümsek: N = 8000 − 2000 = 6000 N.", "Çukur: N = 8000 + 2000 = 10 000 N.", "Terk hızı: ϑ = √(g·r) = √(10·40) = 20 m/s."],
    "Tümsek: 6000 N; çukur: 10 000 N; yolu terk hızı 20 m/s.",
    """
import math
m, g, r, v = 800.0, 10.0, 40.0, 10.0
Fm = m * v ** 2 / r
assert abs(Fm - 2000.0) < 1e-9
assert abs((m * g - Fm) - 6000.0) < 1e-9 and abs((m * g + Fm) - 10000.0) < 1e-9
vleave = math.sqrt(g * r)
assert abs(vleave - 20.0) < 1e-12
assert abs(m * g - m * vleave ** 2 / r) < 1e-9       # N = 0
# ϑ > ϑ_leave için N < 0 çıkar -> araç yoldan ayrılır
assert m * g - m * 21.0 ** 2 / r < 0
""")

SOLUTIONS["flat-curve"] = S(
    M(["Yatay viraj: merkezcil kuvveti yalnız tekerlek-yol arasındaki statik sürtünme sağlar: f_s = mϑ²/r.",
       "Düşey denge: N = mg → f_s,max = k_s·m·g.",
       "Kaymanın eşiği: k_s·m·g = mϑ²/r → ϑ_max = √(k_s·g·r) (kütle sadeleşir).",
       "Islak/buzlu yolda k_s küçülür, ϑ_max azalır; r büyükse (geniş viraj) ϑ_max artar."],
      ["Yatay yol", "Lastik kaymıyor (statik sürtünme)", "Sabit sürat"],
      ["Eğimli virajda formül farklıdır", "Aracın frenleme/hızlanması teğetsel sürtünme ister, ϑ_max değişir"],
      ["Kinetik katsayıyı kullanmak", "Kütleye bağlı sanmak", "Merkezkaç (dışa) kuvvet eklemek"]),
    M(["Aracı virajda 'döndüren' şey yoldan gelen sürtünmedir; yol yeterince tutmazsa araç eylemsizliğiyle düz gider (teğet).", "Hız iki kat artınca gerekli kuvvet dört kat olur; sürtünme tavanı aşılırsa kayar."],
      ["Çembersel hareket"], ["Nitel"], ["Dışa kuvvet vardır sanmak"]),
    M(["ϑ_max² = k_s·g·r. Oranla: k_s 4 kat azalırsa ϑ_max yarıya; r 4 kat artarsa 2 kat."],
      ["Aynı araç/yol"], ["k_s değişirse güncelle"], ["Karekökü unutmak"]),
    None,
    "Yatay viraj: sürtünme = merkezcil kuvvet. ϑ_max = √(k_s g r). Kütle sadeleşir; ıslak yol k_s'yi azaltır.",
    "Yarıçapı 100 m olan yatay bir virajda kuru yolda statik sürtünme katsayısı 0,4, ıslak yolda 0,1'dir. Araçların kaymadan dönebileceği en büyük hızı iki durumda bulunuz. Araç yüklenince (kütle 1,5 katına çıkınca) ϑ_max değişir mi? (g = 10 m/s²)",
    ["Kuru: ϑ_max = √(0,4·10·100) = 20 m/s.", "Islak: ϑ_max = √(0,1·10·100) = 10 m/s (yarıya iner).", "Kütle sadeleşir: değişmez."],
    "Kuru 20 m/s; ıslak 10 m/s; kütleden bağımsız.",
    """
import math
g, r = 10.0, 100.0
vmax = lambda ks: math.sqrt(ks * g * r)
assert abs(vmax(0.4) - 20.0) < 1e-12 and abs(vmax(0.1) - 10.0) < 1e-12
for m in (800.0, 1200.0):
    assert abs(m * 0.4 * g - m * vmax(0.4) ** 2 / r) < 1e-9
assert abs(vmax(0.4) / vmax(0.1) - 2.0) < 1e-12
""")

SOLUTIONS["banked-curve"] = S(
    M(["Sürtünmesiz eğimli viraj: araca yalnız ağırlık ve yola dik normal kuvvet etki eder; yatayla θ eğimli yolda N düşeyle θ açı yapar.",
       "Düşey denge: N·cosθ = m·g.",
       "Yatay (merkeze yönelik): N·sinθ = mϑ²/r.",
       "Oranla: tanθ = ϑ²/(g·r) → ϑ = √(g·r·tanθ) (kütle sadeleşir). Merkezcil kuvveti N'nin yatay bileşeni sağlar."],
      ["Sürtünme yok", "θ yatayla ölçülür", "Sabit sürat"],
      ["Sürtünmeli eğimli virajda güvenli hız aralığı vardır (bu formül yalnız sürtünmesiz durum)", "Gerçek hız bu değerden farklıysa araç kayma eğiliminde olur"],
      ["tanθ yerine sinθ almak", "Merkezcil kuvvetin normal kuvvetin düşey bileşeni olduğunu sanmak", "Kütleye bağımlılık"]),
    M(["Yol eğimli olduğu için yolun tepkisi aracı merkeze doğru da iter; bu yatay bileşen virajı döndürür, sürtünmeye gerek kalmaz.", "Tam doğru hızda araç yalnız yolun itişiyle döner; eğim arttıkça güvenli hız artar."],
      ["Sürtünmesiz"], ["Nitel"], ["Merkezkaçla anlatmak"]),
    M(["Oran: tanθ = ϑ²/(gr). 37° için tanθ = 3/4: ϑ² = 7,5r. 45° için ϑ² = 10r. Gerekirse N = mg/cosθ."],
      ["g = 10 m/s²", "Özel açılar"], ["Sürtünmeli ise geçersiz"], ["sin/cos eşleştirme hatası"]),
    None,
    "Eğimli viraj: N·cosθ = mg ve N·sinθ = mϑ²/r ⇒ tanθ = ϑ²/(gr). Kütle yok; yatayla açıyı kontrol et.",
    "Yarıçapı 30 m olan, sürtünmesiz eğimli bir virajın yatayla yaptığı açı 37°'dir. Güvenli dönüş hızını bulunuz. 1000 kg'lık araç için yolun normal kuvvetini ve merkezcil kuvveti hesaplayınız. (g = 10 m/s², tan37° = 0,75, sin37° = 0,6, cos37° = 0,8)",
    ["ϑ² = g·r·tanθ = 10·30·0,75 = 225 → ϑ = 15 m/s.", "N = mg/cosθ = 10 000/0,8 = 12 500 N.", "F_m = N·sinθ = 12 500·0,6 = 7500 N (= mϑ²/r = 1000·225/30)."],
    "ϑ = 15 m/s; N = 12 500 N; F_m = 7500 N.",
    """
import math
g, r, m = 10.0, 30.0, 1000.0
tan_t, sin_t, cos_t = 0.75, 0.6, 0.8
v = math.sqrt(g * r * tan_t)
assert abs(v - 15.0) < 1e-12
N = m * g / cos_t
Fm = N * sin_t
assert abs(N - 12500.0) < 1e-9 and abs(Fm - 7500.0) < 1e-9
assert abs(Fm - m * v ** 2 / r) < 1e-9
for mm in (500.0, 2000.0):
    assert abs(math.sqrt(g * r * tan_t) - v) < 1e-12   # kütle bağımsız
""")

SOLUTIONS["rotor-and-regulator"] = S(
    M(["Düzeneği çiz ve dönen cisme etki eden gerçek kuvvetleri yaz (ağırlık, normal kuvvet, ip gerilmesi, sürtünme).",
       "Merkeze yönelik doğrultuda bileşkeyi bul: merkezcil kuvveti hangi kuvvetin (ya da bileşenin) sağladığını belirle: rotorda duvarın normal kuvveti; asılı kütlede (regülatör) ipin yatay bileşeni.",
       "Düşey doğrultuda denge yaz: rotorda sürtünme ağırlığı taşır (k_s·N ≥ mg); regülatörde ipin düşey bileşeni ağırlığı taşır (T·cosθ = mg).",
       "Birleştir: rotor için N = mω²r ≥ mg/k_s → ω_min = √(g/(k_s·r)); regülatör için tanθ = ω²r/g."],
      ["Düzgün dönme", "Cisim düzeneğe göre durgun", "İp kütlesiz"],
      ["Sürtünmeli ya da eğik ip durumunda yatay/düşey bileşenler ayrı yazılır", "Hız dalgalanıyorsa geçerli değil"],
      ["Merkezcil kuvvetin ayrı bir kuvvet olduğunu sanmak", "Sürtünmenin merkezcil kuvvete katıldığını sanmak (rotorda düşeyde ağırlığı taşır)", "Kuvveti sağlayan cismi yanlış belirlemek"]),
    M(["Merkezcil kuvvet bir 'sonuç etiketidir': merkeze yönelik bileşkenin adıdır; kaynağı normal, gerilme, sürtünme ya da bileşenleri olabilir.", "Rotorda kişi duvara yapışır çünkü duvar onu içe iter (N) ve sürtünme ağırlığı dengeler."],
      ["Çembersel hareket"], ["Nitel"], ["Hissedilen dışa kuvveti gerçek sanmak"]),
    M(["Önce 'merkezcil kuvvet hangisi?' sorusunu yanıtla: yatay doğrultudaki kuvvet bileşkesi. Sonra düşey dengeyi yaz."],
      ["Standart düzenekler"], ["Karmaşık düzenekler tek tek analiz edilir"], ["Hızlıca formül uygulayıp kaynağı sorgulamamak"]),
    None,
    "Merkezcil kuvvet ayrı bir kuvvet değildir: merkeze yönelik bileşke. Rotor: N merkezcil, sürtünme ağırlığı taşır. Regülatör: tanθ = ω²r/g.",
    "Yarıçapı 2,5 m olan dönen bir silindirin (rotor) duvarına yaslanan 60 kg'lık kişinin, zemin çekilince düşmemesi için gereken en küçük açısal hızı bulunuz (k_s = 0,4). Bu ω'da kişiye duvarın uyguladığı normal kuvveti hesaplayınız. (g = 10 m/s²)",
    ["Düşey: f = mg ve f ≤ k_s·N → N ≥ mg/k_s = 600/0,4 = 1500 N.", "Yatay: N = mω²r → ω_min² = N/(m·r) = 1500/(60·2,5) = 10 → ω_min = √10 ≈ 3,16 rad/s.",
     "N = 1500 N (= mg/k_s); ω² = g/(k_s·r) = 10/(0,4·2,5) = 10 ile tutarlı."],
    "ω_min = √10 ≈ 3,16 rad/s; N = 1500 N.",
    """
import math
m, g, ks, r = 60.0, 10.0, 0.4, 2.5
N = m * g / ks
w = math.sqrt(N / (m * r))
assert abs(N - 1500.0) < 1e-9
assert abs(w - math.sqrt(10.0)) < 1e-12
assert abs(w - math.sqrt(g / (ks * r))) < 1e-12
assert abs(ks * (m * w ** 2 * r) - m * g) < 1e-9       # sürtünme tavanı = ağırlık
# regülatör (konik sarkaç): tanθ = ω² r / g, ip gerilmesi T = m g / cosθ
th = math.atan(w ** 2 * r / g)
T = m * g / math.cos(th)
assert abs(T * math.sin(th) - m * w ** 2 * r) < 1e-9
""")

SOLUTIONS["circular-variables-data"] = S(
    M(["Hangi değişkenin etkisi inceleniyorsa diğerlerinin sabit olduğu satırları seç.",
       "F_m/ϑ² sabit mi (r, m sabit)? Sabitse F_m ∝ ϑ². F_m·r sabit mi (ϑ, m sabit)? Sabitse F_m ∝ 1/r. F_m/m sabit mi? Sabitse F_m ∝ m.",
       "Birleşik ilişkiyi yaz: F_m = k·m·ϑ²/r (k = 1) ve eksik değeri bu ilişkiyle hesapla.",
       "Grafikte doğrusal olacak eksenleri bul: F_m–ϑ² doğrusal (orijinden), F_m–1/r doğrusal, F_m–ϑ eğrisel (parabol)."],
      ["Kontrollü deney verisi", "Düzgün çembersel hareket"],
      ["İki değişkenin birlikte değiştiği satırlar tek başına yorumlanamaz", "Ölçüm hatası nedeniyle tam sabit çıkmayabilir"],
      ["İki değişkenin birlikte değiştiği satırları karşılaştırmak", "F_m'yi ϑ ile orantılı sanmak", "Grafik ekseni yanlış okumak"]),
    M(["Hız iki katına çıkınca cisim hem iki kat hızlı gider hem de dönme eğriliği iki kat çabuk değişir → 4 kat kuvvet.", "Yarıçap büyüdükçe çember daha az kıvrıktır; aynı hızda daha az kuvvet yeter."],
      ["Çembersel hareket"], ["Nitel"], ["Doğrusal ilişki sanmak"]),
    M(["Orantı testi: F_m/ϑ² (r, m sabit) ve F_m·r (ϑ, m sabit) sütunlarını doldur; sabit olanı bul. Eksik hücreyi bu sabitle tamamla."],
      ["Tablo soruları"], ["Satır seçimi dikkat ister"], ["Oranı tek satır üzerinden varsaymak"]),
    M(["Grafik yöntemi: F_m–ϑ² grafiği çiz; eğim m/r olur. Doğrusal çıkan eksen çifti ilişkiyi belirler."],
      ["Doğrusal grafik çizilebiliyor"], ["Çok veri gerekir"], ["Eğimin anlamını karıştırmak"]),
    "Çembersel veri: F_m ∝ ϑ² (r, m sabit), ∝ 1/r (ϑ sabit), ∝ m. F_m–ϑ² grafiği doğrusaldır; F_m–ϑ değildir.",
    "r = 1 m ve m = 0,5 kg sabitken ϑ = 1, 2, 3 m/s için merkezcil kuvvet 0,5; 2; 4,5 N ölçülüyor. ϑ = 2 m/s ve m = 0,5 kg sabitken r = 1, 2, 4 m için F_m = 2; 1; 0,5 N. İlişkiyi bulup ϑ = 6 m/s, r = 3 m, m = 0,5 kg için F_m'yi tahmin ediniz. Hangi grafik doğrusaldır?",
    ["F_m/ϑ² = 0,5/1 = 2/4 = 4,5/9 = 0,5 → F_m ∝ ϑ².", "F_m·r = 2 = 1·2 = 0,5·4 → F_m ∝ 1/r.", "F_m = m·ϑ²/r (katsayı 1): 0,5·36/3 = 6 N.", "F_m–ϑ² grafiği orijinden geçen doğrudur (eğim m/r = 0,5)."],
    "F_m ∝ ϑ²/r; ϑ = 6 m/s, r = 3 m için F_m = 6 N; F_m–ϑ² grafiği doğrusal.",
    """
v = [1.0, 2.0, 3.0]; F = [0.5, 2.0, 4.5]
assert all(abs(F[i] / v[i] ** 2 - 0.5) < 1e-12 for i in range(3))
r = [1.0, 2.0, 4.0]; F2 = [2.0, 1.0, 0.5]
assert all(abs(F2[i] * r[i] - 2.0) < 1e-12 for i in range(3))
m = 0.5
assert abs(m * 36.0 / 3.0 - 6.0) < 1e-12
# F-v^2 doğrusal (eşit eğim), F-v değil
slopes = [(F[i + 1] - F[i]) / (v[i + 1] ** 2 - v[i] ** 2) for i in range(2)]
assert abs(slopes[0] - slopes[1]) < 1e-12 and abs(slopes[0] - 0.5) < 1e-12
slopes_v = [(F[i + 1] - F[i]) / (v[i + 1] - v[i]) for i in range(2)]
assert abs(slopes_v[0] - slopes_v[1]) > 0.5
""")


# ====================================================================================
#                                      KISA YOLLAR
# ====================================================================================
def SC(slug, name, fams, shortcut, why, validity, failure, risk, sources, check):
    return {"slug": slug, "name": name, "question_families": fams, "shortcut": shortcut, "why_it_works": why,
            "validity_conditions": validity, "failure_cases": failure, "risk_level": risk,
            "sources": sources, "numeric_check": check}


TB = lambda ref: {"type": "textbook", "ref": ref}
DV = lambda ref: {"type": "derivation", "ref": ref}

SHORTCUTS += [
    SC("consecutive-equal-intervals-1-3-5-7", "Ardışık eşit sürelerde yollar 1:3:5:7",
       ["ff-kinematics-v0zero", "ff-equal-interval-ratios"],
       "Durgun bırakılan cisim eşit τ sürelerinde sırayla h₁·(1, 3, 5, 7, …) yol alır; ilk n aralıkta toplam yol n²·h₁.",
       "h(t) = ½gt² olduğundan n. aralıkta h(nτ) − h((n−1)τ) = ½gτ²(2n − 1) = (2n − 1)·h₁.",
       ["ϑ₀ = 0 (durgun bırakılıyor)", "Aralıklar eşit ve ilki bırakma anında başlıyor", "Hava direnci ihmal"],
       ["İlk hız sıfır değilse oran 1:3:5 olmaz", "Zaman aralıkları bırakma anından başlamıyorsa (örn. 1,5 s sonra) oran bozulur", "Aralıklar eşit değilse uygulanmaz"],
       "LOW", [TB("s. 29 Kontrol Noktası")],
       """
g = 10.0
h = lambda t: 0.5 * g * t * t
for tau in (0.3, 1.0, 2.5):
    base = h(tau)
    for n in range(1, 21):
        assert abs((h(n * tau) - h((n - 1) * tau)) - (2 * n - 1) * base) < 1e-9
# başarısız durum 1: ilk hız var
v0 = 10.0
h2 = lambda t: v0 * t + 0.5 * g * t * t
seg = [h2(n) - h2(n - 1) for n in range(1, 4)]
assert abs(seg[1] / seg[0] - 3) > 0.5
# başarısız durum 2: aralıklar bırakma anından başlamıyor (1,5 s sonra)
seg3 = [h(1.5 + n) - h(1.5 + n - 1) for n in range(1, 4)]
assert abs(seg3[1] / seg3[0] - 3) > 1.0
"""),
    SC("peak-time-from-two-passes", "Tepe süresi (t₁+t₂)/2, h = ½g·t₁·t₂",
       ["ff-passing-point-twice", "ff-upward-throw"],
       "Aynı noktadan geçiş anları t₁, t₂ ise tepe anı (t₁+t₂)/2; ϑ₀ = g(t₁+t₂)/2; noktanın yüksekliği h = ½g·t₁·t₂; tepe yüksekliği (g/8)(t₁+t₂)².",
       "Δy = ϑ₀t − ½gt² denkleminin iki kökü t₁, t₂'dir: kökler toplamı 2ϑ₀/g, çarpımı 2y/g (Vieta).",
       ["Zamanlar atıştan itibaren ölçülmüş", "Aynı noktadan çıkış ve iniş geçişi", "Hava direnci yok"],
       ["Kronometre atıştan sonra başlatılmışsa (zaman kayması) formüller yanlış sonuç verir", "Farklı noktalardan geçişte uygulanmaz", "Yön işareti olan yerden yüksek atışta zamanlar atıştan değil de başka yerden okunursa geçersiz"],
       "MEDIUM", [TB("s. 120 ÖD-2"), DV("Vieta bağıntıları: kökler toplamı ve çarpımı")],
       """
import random
random.seed(1)
g = 10.0
for _ in range(300):
    v0 = random.uniform(5, 60)
    y = random.uniform(0.1, v0 ** 2 / (2 * g) * 0.999)
    d = (v0 ** 2 - 2 * g * y) ** 0.5
    t1, t2 = (v0 - d) / g, (v0 + d) / g
    assert abs((t1 + t2) / 2 - v0 / g) < 1e-9
    assert abs(0.5 * g * t1 * t2 - y) < 1e-9
    assert abs(g * (t1 + t2) / 2 - v0) < 1e-9
    assert abs(g / 8 * (t1 + t2) ** 2 - v0 ** 2 / (2 * g)) < 1e-9
# başarısız durum: zamanlar atıştan 0,5 s sonra başlayan kronometreyle okunursa
t1s, t2s = t1 - 0.5, t2 - 0.5
assert abs(g * (t1s + t2s) / 2 - v0) > 1.0
"""),
    SC("hmax-v0-squared-over-2g", "h_max = ϑ₀²/(2g)",
       ["ff-upward-throw", "ff-passing-point-twice"],
       "Yukarı atılan cismin atış noktasından tepe yüksekliği ϑ₀²/(2g); g = 10 için ϑ₀²/20.",
       "ϑ² = ϑ₀² − 2gh denkleminde tepede ϑ = 0.",
       ["Hava direnci yok", "Tepe, atış seviyesine göre ölçülüyor"],
       ["Yerden yüksekten atışta yerden yükseklik H + ϑ₀²/2g'dir (yalnız ϑ₀²/2g yerden yükseklik değil)", "Açılı ilk hızlı harekette ϑ₀ yerine düşey bileşen ϑ₀·sinα kullanılmalı", "Hava direncinde geçersiz"],
       "LOW", [TB("s. 28 6. Alıştırma"), DV("ϑ² = ϑ₀² − 2gh, ϑ = 0")],
       """
import math
g = 10.0
for v0 in (4.0, 12.5, 30.0, 55.0):
    dt = 1e-5
    y, v, ymax = 0.0, v0, 0.0
    while v > 0:
        y += v * dt
        v -= g * dt
        ymax = max(ymax, y)
    assert abs(ymax - v0 ** 2 / (2 * g)) < 1e-3
# başarısız durum: açılı ilk hızlı harekette toplam hız ϑ₀ ile hesaplamak yanlış
v0, a = 40.0, math.radians(37)
assert abs(v0 ** 2 / (2 * g) - (v0 * math.sin(a)) ** 2 / (2 * g)) > 10
# yerden yüksek atış
H = 25.0
assert abs((H + 20.0 ** 2 / (2 * g)) - 45.0) < 1e-12
"""),
    SC("symmetry-same-level-up-down", "Simetri: aynı seviyede çıkış-iniş süreleri ve hız büyüklükleri eşit",
       ["ff-upward-throw", "ff-passing-point-twice"],
       "Aynı seviyeye dönen cisimde çıkış süresi = iniş süresi; her seviyede hız büyüklüğü çıkışta ve inişte eşittir; toplam süre 2ϑ₀/g.",
       "Hareket ϑ = ϑ₀ − gt ve y = ϑ₀t − ½gt² tepe zamanına göre simetrik bir paraboldür.",
       ["Çıkış ve dönüş aynı seviyede", "Hava direnci yok"],
       ["Atış seviyesinin altına düşen cisimde (yerden yüksekten atış) toplam süre 2ϑ₀/g değildir", "Hava direncinde iniş süresi çıkıştan uzun olur"],
       "LOW", [DV("Parabolik hareketin tepeye göre simetrisi")],
       """
import random
random.seed(2)
g = 10.0
for _ in range(200):
    v0 = random.uniform(5, 50)
    y = random.uniform(0.0, v0 ** 2 / (2 * g) * 0.99)
    d = (v0 ** 2 - 2 * g * y) ** 0.5
    t1, t2 = (v0 - d) / g, (v0 + d) / g
    assert abs((v0 / g - t1) - (t2 - v0 / g)) < 1e-9                  # tepeden eşit uzaklık
    assert abs(abs(v0 - g * t1) - abs(v0 - g * t2)) < 1e-9            # hız büyüklükleri eşit
    assert abs((t1 + t2) - 2 * v0 / g) < 1e-9
# başarısız durum: yerden yüksek atışta toplam süre 2 v0/g değil
v0, H = 20.0, 25.0
t_total = (v0 + (v0 ** 2 + 2 * g * H) ** 0.5) / g
assert abs(t_total - 2 * v0 / g) > 0.5
"""),
    SC("free-fall-sqrt-ratios", "Serbest düşmede h ∝ t², t ∝ √h, ϑ ∝ √h",
       ["ff-kinematics-v0zero", "ff-reaction-time-ruler", "ff-equal-interval-ratios"],
       "Durgun bırakılan cisimde yükseklik k kat olursa süre ve çarpma hızı √k kat olur; süre k kat olursa yükseklik k² kat olur.",
       "t = √(2h/g), ϑ = √(2gh) = g·t.",
       ["ϑ₀ = 0", "Hava direnci ihmal", "İkisinde de g aynı"],
       ["İlk hızlı hareketlerde (ϑ₀ ≠ 0) oran bozulur", "Hava direncinin etkili olduğu uzun düşüşlerde geçersiz", "Farklı gezegenlerde g farklıysa g'yi de oranla"],
       "LOW", [TB("s. 29 Kontrol Noktası")],
       """
import math
g = 10.0
t = lambda h: math.sqrt(2 * h / g)
v = lambda h: math.sqrt(2 * g * h)
for h in (1.0, 5.0, 20.0):
    for k in (4.0, 9.0, 2.0, 0.25):
        assert abs(t(k * h) / t(h) - math.sqrt(k)) < 1e-12
        assert abs(v(k * h) / v(h) - math.sqrt(k)) < 1e-12
assert abs(t(0.8) / t(0.2) - 2.0) < 1e-12
# başarısız durum: ilk hız varsa oran bozulur
v0 = 10.0
th = lambda h: (-v0 + math.sqrt(v0 ** 2 + 2 * g * h)) / g       # aşağı ilk hızla düşme süresi
assert abs(th(80.0) / th(20.0) - 2.0) > 0.1
"""),
    SC("complementary-angles-equal-range", "Tümler açılarda menziller eşit",
       ["2d-angled-launch"],
       "Aynı seviyeye dönen aynı hızlı atışlarda α ve 90° − α açılarıyla atılan cisimlerin menzilleri eşittir.",
       "Menzil R = ϑ₀²·sin2α/g ve sin2α = sin(180° − 2α) = sin2(90° − α).",
       ["Aynı ϑ₀", "Atış ve iniş aynı seviyede", "Hava direnci yok"],
       ["Yerden yüksekten atışta (iniş seviyesi daha aşağı) menziller eşit olmaz", "Hava direnci ya da rüzgâr varsa geçersiz", "Farklı ϑ₀'da uygulanmaz"],
       "MEDIUM", [TB("s. 39 Kontrol Noktası"), DV("R = ϑ₀² sin2α / g")],
       """
import math
g = 10.0
def rng(v0, deg, H=0.0):
    a = math.radians(deg)
    vy, vx = v0 * math.sin(a), v0 * math.cos(a)
    T = (vy + math.sqrt(vy * vy + 2 * g * H)) / g       # y = H + vy t - 0.5 g t^2 = 0
    return vx * T
for v0 in (10.0, 25.0, 50.0):
    for a in (10, 20, 30, 37, 40, 44):
        assert abs(rng(v0, a) - rng(v0, 90 - a)) < 1e-9
assert abs(rng(50, 37) - rng(50, 53)) < 1e-9
# başarısız durum: yüksekten atış
assert abs(rng(25, 30, H=15.0) - rng(25, 60, H=15.0)) > 1.0
"""),
    SC("forty-five-degree-max-range", "45°'de menzil en büyük",
       ["2d-angled-launch"],
       "Aynı ϑ₀ ve aynı seviyeye dönüşte menzil α = 45°'de en büyüktür; R_max = ϑ₀²/g.",
       "R = ϑ₀²sin2α/g ve sin2α'nın maksimumu 2α = 90°'de 1'dir.",
       ["Aynı ϑ₀", "Atış ve iniş aynı seviyede", "Hava direnci yok"],
       ["Yerden yüksekten atışta en büyük menzil açısı 45°'den küçüktür", "Daha alçak seviyeye inişte 45° en iyi açı değildir", "Hava direnci varsa en iyi açı 45°'den küçük olur"],
       "MEDIUM", [DV("R(α) = ϑ₀² sin2α / g, dR/dα = 0")],
       """
import math
g = 10.0
def rng(v0, deg, H=0.0):
    a = math.radians(deg)
    vy, vx = v0 * math.sin(a), v0 * math.cos(a)
    return vx * (vy + math.sqrt(vy * vy + 2 * g * H)) / g
angles = [i * 0.25 for i in range(1, 360)]
best = max(angles, key=lambda a: rng(30.0, a))
assert abs(best - 45.0) < 0.3
assert abs(rng(30.0, 45.0) - 30.0 ** 2 / g) < 1e-9
# başarısız durum: H = 20 m yüksekten atış
best_h = max(angles, key=lambda a: rng(30.0, a, H=20.0))
assert best_h < 44.0 and best_h > 20.0
"""),
    SC("tan-alpha-4h-over-range", "tanα = 4·h_max / menzil",
       ["2d-angled-launch", "2d-velocity-at-point"],
       "Aynı seviyeye dönen açılı ilk hızlı harekette açı tanα = 4h_max/R ile bulunur; h_max ve menzil verilince açı hemen çıkar.",
       "h_max = ϑ₀²sin²α/(2g), R = 2ϑ₀²sinα·cosα/g → h_max/R = tanα/4.",
       ["Atış ve iniş aynı seviyede", "Hava direnci yok"],
       ["Yüksekten atışta geçersiz", "Menzil ya da h_max farklı seviyeye göre ölçülmüşse geçersiz"],
       "LOW", [DV("h_max / R oranı")],
       """
import math, random
random.seed(3)
g = 10.0
for _ in range(200):
    v0 = random.uniform(5, 60)
    a = random.uniform(5, 85)
    ar = math.radians(a)
    vy, vx = v0 * math.sin(ar), v0 * math.cos(ar)
    h = vy ** 2 / (2 * g)
    R = vx * 2 * vy / g
    assert abs(math.degrees(math.atan(4 * h / R)) - a) < 1e-9
# başarısız durum: 10 m yüksekten atış
H = 10.0
v0, ar = 20.0, math.radians(40)
vy, vx = v0 * math.sin(ar), v0 * math.cos(ar)
T = (vy + math.sqrt(vy ** 2 + 2 * g * H)) / g
assert abs(math.degrees(math.atan(4 * (vy ** 2 / (2 * g)) / (vx * T))) - 40) > 3
"""),
    SC("horizontal-launch-time-from-height", "Yatay hızla fırlatmada süre yalnız yükseklikten: t = √(2h/g)",
       ["2d-horizontal-launch", "2d-component-data"],
       "Yatay ilk hızı olan cismin havada kalma süresi, aynı yükseklikten serbest bırakılan cisimle aynıdır: t = √(2h/g); menzil = ϑ₀·t.",
       "Düşey hareket yatay hızdan bağımsızdır; düşeyde ϑ_y₀ = 0.",
       ["İlk hız tam yatay", "Yatayda ivme yok (rüzgâr yok)", "Hava direnci yok"],
       ["İlk hız yatay değilse (açılı ilk hız) süre değişir", "Yatay yüzeye değil eğik yüzeye düşüyorsa uçuş süresi başka koşuldan bulunur"],
       "LOW", [TB("s. 123 ÖD-5")],
       """
import math
g = 10.0
def fall_time_numeric(h, vy0=0.0, dt=1e-5):
    y, vy, t = 0.0, vy0, 0.0
    while y < h:
        vy += g * dt
        y += vy * dt
        t += dt
    return t
for h in (5.0, 20.0, 45.0):
    t0 = math.sqrt(2 * h / g)
    assert abs(fall_time_numeric(h) - t0) < 1e-3
    for vx in (1.0, 10.0, 100.0):
        assert abs(vx * t0 - vx * math.sqrt(2 * h / g)) < 1e-12     # menzil ϑ₀ t, süre vx'ten bağımsız
# başarısız durum: yukarı yönlü ilk düşey hız (açılı ilk hız) süreyi değiştirir
assert abs(fall_time_numeric(20.0, vy0=-10.0) - 2.0) > 0.5
"""),
    SC("incline-landing-time", "Eğik düzleme yatay ilk hızla fırlatmada süre: t = 2ϑ₀·tanθ/g",
       ["2d-launch-onto-incline-or-steps"],
       "Eğik düzlemin tepesinden ϑ₀ yatay hızıyla atılan cismin düzleme çarpma süresi t = 2ϑ₀tanθ/g; düzlem boyu d = x/cosθ.",
       "Çarpma anında y/x = tanθ: (½gt²)/(ϑ₀t) = tanθ.",
       ["Atış noktası düzlemin üstünde, ilk hız tam yatay", "Düzlem yeterince uzun", "Hava direnci yok"],
       ["Atış yatay değilse koşul y = ϑᵧt + ½gt² biçiminde değişir", "Düzlem kısaysa cisim düzlemi aşıp yere düşer", "Basamaklarda aynı formül kullanılmaz"],
       "MEDIUM", [TB("s. 128 ÖD-11"), DV("tanθ = y/x çarpma koşulu")],
       """
import math
g = 10.0
def hit_time(v0, theta):
    # y/x = tan(theta) koşulunu sayısal bisection ile çöz
    f = lambda t: 0.5 * g * t * t - math.tan(theta) * v0 * t
    lo, hi = 1e-9, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo
for v0 in (5.0, 15.0, 30.0):
    for deg in (20, 37, 45, 60):
        th = math.radians(deg)
        assert abs(hit_time(v0, th) - 2 * v0 * math.tan(th) / g) < 1e-6
# başarısız durum: ilk hız 20° aşağı yönlü (yatay değil) olunca aynı formül yanlış
v0, th, a0 = 15.0, math.radians(37), math.radians(20)
vx, vy0 = v0 * math.cos(a0), v0 * math.sin(a0)
lo, hi = 1e-9, 100.0
f = lambda t: vy0 * t + 0.5 * g * t * t - math.tan(th) * vx * t
for _ in range(200):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
assert abs(lo - 2 * v0 * math.tan(th) / g) > 0.1
"""),
    SC("belt-and-shaft-equalities", "Kayış/temas: çizgisel sürat eşit; aynı mil: açısal hız eşit",
       ["coupled-wheels", "circular-kinematics"],
       "Kayışla ya da dişliyle bağlı tekerlerde ϑ₁ = ϑ₂ ⇒ f₁r₁ = f₂r₂; aynı mile bağlı tekerlerde ω₁ = ω₂ ⇒ ϑ₁/r₁ = ϑ₂/r₂ ve f, T aynı.",
       "Kayış kaymıyorsa kayış üzerindeki her noktanın hızı eşit; rijit mil her noktayı aynı açıyla taratır.",
       ["Kayış kaymıyor, dişliler tam oturuyor", "Mil rijit"],
       ["Kayış kayıyorsa ϑ eşitliği bozulur", "Kayışla bağlı tekerlerde ω eşit değildir (yalnız yarıçaplar eşitse aynı)", "Dişlilerde dönme yönü zıt olur (büyüklük aynı)"],
       "LOW", [TB("s. 105 39. Alıştırma"), DV("ϑ = ω·r")],
       """
import math, random
random.seed(4)
for _ in range(200):
    r1, r2, r3 = (random.uniform(0.05, 1.0) for _ in range(3))
    f1 = random.uniform(0.5, 40)
    v1 = 2 * math.pi * r1 * f1
    f2 = v1 / (2 * math.pi * r2)               # kayış: ϑ eşit
    assert abs(f1 * r1 - f2 * r2) < 1e-9
    w2 = 2 * math.pi * f2
    v3 = w2 * r3                                # aynı mil: ω eşit
    assert abs(v3 / (2 * math.pi * f2 * r2) - r3 / r2) < 1e-9
# başarısız durum: kayışla bağlı tekerlerde ω eşit değildir
r1, r2, f1 = 0.1, 0.4, 12.0
f2 = f1 * r1 / r2
assert abs(f1 - f2) > 1.0
"""),
]

SHORTCUTS += [
    SC("system-acceleration-first", "Önce sistem ivmesi: a = ΣF_dış/Σm, sonra tek cisimde gerilme",
       ["connected-bodies-same-acceleration", "friction-stacked-blocks-together"],
       "Aynı ivmeli bağlı cisimlerde iç kuvvetler (ip gerilmesi, temas kuvveti) sistemde birbirini götürür: a = ΣF_dış/Σm; sonra tek cisim için F_net = m·a ile gerilme bulunur.",
       "Her cisim için Newton'un 2. yasası yazılıp toplanınca iç kuvvetler (etki-tepki) sadeleşir.",
       ["Tüm cisimler aynı büyüklükte ivmeli", "İp kütlesiz ve gergin, makara sürtünmesiz/kütlesiz"],
       ["Farklı ivmeli sistemlerde (hareketli makara, kayan üst blok) geçersizdir (program kapsamı dışı)", "İp gevşerse sonuç geçersiz", "Sürtünme dış kuvvet olarak toplama dahil edilmelidir"],
       "LOW", [TB("s. 80 sistem ivmesi bağıntısı"), DV("Newton 2. yasasının cisimlere toplanması")],
       """
def solve(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(n):
            if r != i:
                f = M[r][i] / M[i][i]
                M[r] = [x - f * y for x, y in zip(M[r], M[i])]
    return [M[i][n] / M[i][i] for i in range(n)]
import random
random.seed(5)
g = 10.0
for _ in range(100):
    m1, m2, m3 = (random.uniform(0.5, 10) for _ in range(3))
    F = random.uniform(5, 100)
    # bilinmeyenler: a, T1, T2 ; m1 a + T1 = F ; m2 a - T1 + T2 = 0 ; m3 a - T2 = 0
    a, T1, T2 = solve([[m1, 1, 0], [m2, -1, 1], [m3, 0, -1]], [F, 0, 0])
    assert abs(a - F / (m1 + m2 + m3)) < 1e-9
    assert abs(T2 - m3 * a) < 1e-9 and abs(T1 - (m2 + m3) * a) < 1e-9
# başarısız durum: hareketli makara (a_A = 2 a_B): sistem ivmesi kısayolu yanlış
mA, mB = 2.0, 3.0
aB = mB * g / (mB + 4 * mA)          # mB g - 2T = mB aB ; T = mA * 2 aB
assert abs(aB - mB * g / (mA + mB)) > 1.0
"""),
    SC("contact-force-two-blocks", "Temas kuvveti = F·(öndeki kütle)/(toplam kütle)",
       ["connected-bodies-same-acceleration"],
       "Arka arkaya itilen bloklarda ortak ivme a = F/Σm; bir bloğun önündeki bloklara uyguladığı temas kuvveti = (önündeki kütleler toplamı)·a.",
       "Önündeki cisimleri hızlandıran tek yatay kuvvet temas kuvvetidir: N = m_ön·a.",
       ["Aynı ivmeli, sürtünmesiz (ya da eşit sürtünme katsayılı) bloklar", "Kuvvet en arka bloğa uygulanıyor"],
       ["Bloklarla zemin arasındaki sürtünme katsayıları farklıysa formül değişir", "Kuvvet ortadaki bloğa uygulanıyorsa her iki yöndeki temas kuvveti farklı hesaplanır"],
       "MEDIUM", [TB("s. 61 Örnek"), DV("Önündeki blokların serbest cisim denklemi")],
       """
import random
random.seed(6)
for _ in range(100):
    m1, m2, m3 = (random.uniform(1, 8) for _ in range(3))
    F = random.uniform(10, 100)
    a = F / (m1 + m2 + m3)
    N12 = (m2 + m3) * a
    N23 = m3 * a
    assert abs(N12 - F * (m2 + m3) / (m1 + m2 + m3)) < 1e-9
    assert abs(F - N12 - m1 * a) < 1e-9          # 1. blok denklemi
    assert abs(N12 - N23 - m2 * a) < 1e-9        # 2. blok denklemi
# başarısız durum: bloklar farklı sürtünmeli ise kısa yol farklı sonuç verir
g, m1, m2, F = 10.0, 2.0, 3.0, 40.0
k1, k2 = 0.0, 0.5
a = (F - k1 * m1 * g - k2 * m2 * g) / (m1 + m2)
N = m2 * a + k2 * m2 * g            # 2. blok: N - f2 = m2 a
assert abs(N - F * m2 / (m1 + m2)) > 1.0
"""),
    SC("static-threshold-check-first", "Önce eşik kontrolü: F ≤ f_s,max ise f = F ve a = 0",
       ["friction-threshold", "friction-applied-force-graph", "friction-stacked-blocks-together"],
       "Sürtünmeli soruda önce uygulanan kuvveti f_s,max ile karşılaştır: aşmıyorsa cisim durgun, f = F; aşıyorsa f = f_k ve a = (F − f_k)/m.",
       "Statik sürtünme gerektiği kadar (0 ile f_s,max arasında) tepki verir; ancak tavan aşılınca cisim kaymaya başlar.",
       ["Yatay zeminde durgun cisim", "f_s,max ve f_k verilmiş"],
       ["Cisim zaten hareket ediyorsa eşik kontrolü yapılmaz (f = f_k alınır)", "F eşiğe eşitse sınır durumudur: a = 0", "Eğik düzlem ya da açılı kuvvette eşik N'ye göre yeniden bulunur"],
       "LOW", [TB("s. 138 ÖD-22"), TB("s. 85 Kontrol Noktası")],
       """
import random
random.seed(7)
def rule(F, m, fs, fk):
    return (F, 0.0) if F <= fs else (fk, (F - fk) / m)
def simulate(F, m, fs, fk, T=1.0, dt=1e-4):
    v, x = 0.0, 0.0
    for _ in range(int(round(T / dt))):
        if v == 0.0 and F <= fs:
            a = 0.0
        else:
            a = (F - fk) / m
        v += a * dt
        x += v * dt
    return v
for _ in range(100):
    m = random.uniform(1, 10)
    fk = random.uniform(2, 20)
    fs = fk + random.uniform(0, 10)
    F = random.uniform(0, 60)
    f, a = rule(F, m, fs, fk)
    v_end = simulate(F, m, fs, fk)
    assert abs(v_end - a * 1.0) < 1e-3
# başarısız durum: cisim zaten hareketliyken eşik kontrolü yapılırsa yanlış sonuç çıkar
m, fs, fk, F = 5.0, 20.0, 15.0, 18.0
assert rule(F, m, fs, fk)[1] == 0.0               # durgun cisim: kıpırdamaz
assert abs((F - fk) / m - 0.6) < 1e-12            # hareketliyken ivme 0,6
"""),
    SC("pendulum-tan-a-over-g", "Araçta asılı cisim: tanθ = a/g",
       ["accelerating-frame-pendulum"],
       "Sabit ivmeli araçta asılı cismin düşeyle açısı tanθ = a/g'dir (ivmenin ters yönünde sapar); T = m√(g² + a²).",
       "Düşey: T·cosθ = mg; yatay: T·sinθ = ma; oranlanınca kütle ve T sadeleşir.",
       ["Araç sabit ivmeli, cisim araca göre durgun (denge açısı)", "İp kütlesiz"],
       ["Araç sabit hızlıysa θ = 0", "Cisim salınım yapıyorsa bağıntı yalnız denge konumu için geçerlidir", "Araç ivmesi değişiyorsa anlık açı bu bağıntıyla bulunamaz"],
       "MEDIUM", [TB("s. 63 Örnek"), DV("Bileşen denklemlerinin oranı")],
       """
import math
g = 10.0
def equilibrium_angle(a, L=1.0, c=3.0, dt=1e-4, T=60.0):
    # yerdeki gözlemciye göre, pivotu a ile ivmelenen sönümlü sarkaç: L θ'' = -g sinθ - a cosθ - c θ'
    th, w = 0.0, 0.0
    for _ in range(int(T / dt)):
        w += (-g * math.sin(th) - a * math.cos(th) - c * w) / L * dt
        th += w * dt
    return th
for a in (2.0, 5.0, 7.5, 10.0):
    th = equilibrium_angle(a)
    assert abs(abs(th) - math.atan(a / g)) < 2e-3
    assert th < 0                                  # ivmenin ters yönünde (geriye) sapar
# başarısız durum: sönümsüz sarkaç denge açısında durmaz, 2θ_eq'ya kadar salınır
def amplitude(a, L=1.0, dt=1e-4, T=10.0):
    th, w, mx = 0.0, 0.0, 0.0
    for _ in range(int(T / dt)):
        w += (-g * math.sin(th) - a * math.cos(th)) / L * dt
        th += w * dt
        mx = max(mx, abs(th))
    return mx
assert amplitude(5.0) > 1.6 * math.atan(5.0 / g)
"""),
    SC("apparent-weight-m-g-plus-a", "Görünür ağırlık N = m(g + a)",
       ["apparent-weight-elevator"],
       "Yukarı yönlü ivmede (a > 0) tartı m(g + a), aşağı yönlü ivmede m(g − a) gösterir; sabit hızda mg, a = g'de 0.",
       "N − mg = m·a (yukarı pozitif).",
       ["İvme asansör ve cisim için aynı", "Tartı normal kuvveti ölçer"],
       ["İvme yönü hız yönüyle karıştırılırsa ters sonuç çıkar (yukarı çıkarken yavaşlamak = aşağı ivme)", "Sabit hızda tartı değişmez, hız ne kadar büyük olursa olsun", "g'den büyük aşağı ivme asansör zemini terk eder (N < 0 mümkün değil)"],
       "MEDIUM", [TB("s. 148 ÖD-38"), DV("N − mg = m·a")],
       """
m, g = 70.0, 10.0
pos = lambda t, x0, v0, a: x0 + v0 * t + 0.5 * a * t * t
h = 1e-3
for a in (-8.0, -3.0, 0.0, 2.0, 5.0):
    a_fd = (pos(1 + h, 0, 4.0, a) - 2 * pos(1, 0, 4.0, a) + pos(1 - h, 0, 4.0, a)) / h ** 2
    N = m * (g + a_fd)
    assert abs(N - m * (g + a)) < 1e-3
# sabit hız: N = m g, hız ne kadar büyük olursa olsun
assert 70.0 * (g + 0.0) == 700.0
# başarısız durum: hız yukarı, ama yavaşlıyor (ivme aşağı) ise N < mg
a = -2.0
assert m * (g + a) < m * g
# başarısız durum: g'den büyük aşağı ivme tartı değerini negatif yapar (fiziksel değil)
assert m * (g + (-12.0)) < 0
"""),
    SC("incline-a-g-sin-mass-free", "Sürtünmesiz eğik düzlemde a = g·sinθ ve ϑ = √(2gh)",
       ["frictionless-incline"],
       "Sürtünmesiz eğik düzlemde ivme g·sinθ'dır (kütleden bağımsız); düşey yükseklik farkı h kadar inen cismin hızı eğimden bağımsız √(2gh).",
       "Paralel bileşen mg·sinθ = ma; yol s = h/sinθ olduğundan ϑ² = 2as = 2gh.",
       ["Sürtünme yok", "Ek kuvvet yok", "θ yatayla ölçülür"],
       ["Sürtünmeli düzlemde a = g(sinθ − k·cosθ) olur", "Ek kuvvet (ip, itme) varsa geçersiz", "θ düşeyle verilmişse sin yerine cos kullanılır"],
       "LOW", [TB("s. 60 Örnek")],
       """
import math
g = 10.0
def accel(theta, m, k=0.0):
    # vektörlerle: yerçekimi (0, -mg), eğik düzlem birim vektörü (cos t, -sin t), normal (sin t, cos t)
    Fg = (0.0, -m * g)
    u = (math.cos(theta), -math.sin(theta))
    n = (math.sin(theta), math.cos(theta))
    along = Fg[0] * u[0] + Fg[1] * u[1]
    N = -(Fg[0] * n[0] + Fg[1] * n[1])
    return (along - k * N) / m
for deg in (10, 30, 37, 53, 80):
    th = math.radians(deg)
    for m in (0.5, 3.0, 40.0):
        assert abs(accel(th, m) - g * math.sin(th)) < 1e-9
    h = 2.0
    s = h / math.sin(th)
    assert abs(math.sqrt(2 * accel(th, 1.0) * s) - math.sqrt(2 * g * h)) < 1e-9
# başarısız durum: sürtünme varsa a < g sin θ
assert accel(math.radians(37), 2.0, k=0.3) < g * math.sin(math.radians(37)) - 1.0
"""),
    SC("k-equals-tan-theta", "Sabit hızla kayma ya da kaymaya başlama: k = tanθ",
       ["friction-incline-coefficient"],
       "Eğik düzlemde cisim sabit hızla kayıyorsa k_k = tanθ; tam kaymaya başladığı açı θ_s ise k_s = tanθ_s.",
       "mg·sinθ = k·mg·cosθ → k = tanθ.",
       ["Yalnız ağırlık, normal kuvvet ve sürtünme", "Sabit hız (ivme 0) ya da eşik anı"],
       ["İvmeli kaymada geçersiz (a = g(sinθ − k·cosθ) kullanılır)", "Ek kuvvet varsa geçersiz", "Kaymaya başlama açısı k_k'yı değil k_s'yi verir"],
       "MEDIUM", [TB("s. 82 Örnek"), DV("Paralel ve dik denge denklemleri")],
       """
import math
g = 10.0
def a_slide(theta, k):
    return g * (math.sin(theta) - k * math.cos(theta))
for k in (0.1, 0.35, 0.75, 1.2, 2.0):
    lo, hi = 0.0, math.pi / 2
    for _ in range(200):
        mid = (lo + hi) / 2
        if a_slide(mid, k) < 0:
            lo = mid
        else:
            hi = mid
    assert abs(math.tan(lo) - k) < 1e-9
# başarısız durum: ivmeli kayma
th, k = math.radians(53), 0.5
assert a_slide(th, k) > 1.0 and abs(math.tan(th) - k) > 0.5
"""),
    SC("wall-press-min-force", "Duvara bastırma: F_min = m·g/k_s ve f = m·g",
       ["friction-wall-press"],
       "Duvara yatay F ile bastırılan cisim dengedeyse sürtünme = mg (F'den bağımsız); düşmemesi için F ≥ mg/k_s.",
       "Düşey: f = mg; yatay: N = F; f ≤ k_s·N.",
       ["Kuvvet duvara dik", "Cisim dengede"],
       ["Kuvvet yatayla açı yapıyorsa N ve düşey denge değişir", "Cisim kayıyorsa kinetik sürtünme kullanılır", "F büyütülünce sürtünmenin de büyüdüğü sanılmamalı (sürtünme mg'de kalır)"],
       "LOW", [TB("s. 84 Örnek")],
       """
import math
g = 10.0
for m in (0.5, 2.0, 7.0):
    for ks in (0.2, 0.4, 0.8):
        Fmin = m * g / ks
        assert ks * Fmin >= m * g - 1e-9 and ks * (Fmin * 0.999) < m * g
        for F in (Fmin, 2 * Fmin, 5 * Fmin):
            f_used = min(m * g, ks * F)               # denge için gereken sürtünme hep mg
            assert abs(m * g - f_used) < 1e-9         # net düşey kuvvet 0
        assert m * g - min(m * g, ks * 0.5 * Fmin) > 0   # eşiğin altında cisim düşer
# başarısız durum: kuvvet yatayla 30° yukarı doğru ise gerekli kuvvet farklıdır
m, ks, a = 2.0, 0.4, math.radians(30)
F_inclined = m * g / (ks * math.cos(a) + math.sin(a))
assert abs(F_inclined - m * g / ks) > 10
"""),
    SC("friction-stop-distance", "Sürtünmeyle durma: x = ϑ₀²/(2·k·g), t = ϑ₀/(k·g)",
       ["friction-horizontal-dynamics"],
       "İlk hızla yatay zeminde kayan ve yalnız kinetik sürtünmenin yavaşlattığı cisim a = k·g ile durur; yol ϑ₀²/(2kg), süre ϑ₀/(kg), kütleden bağımsızdır.",
       "a = f_k/m = k·m·g/m = k·g (kütle sadeleşir).",
       ["Yatay zemin", "Yalnız kinetik sürtünme (başka kuvvet yok)", "k sabit"],
       ["Çekme/itme kuvveti ya da eğim varsa geçersiz", "Açılı kuvvette N değişir", "Cisim dönerek ilerliyorsa (statik sürtünme) geçerli değil"],
       "LOW", [TB("s. 135 ÖD-16")],
       """
g = 10.0
def stop_numeric(v0, k, m, extra=0.0, dt=1e-5):
    v, x = v0, 0.0
    while v > 0:
        a = -(k * m * g) / m + extra / m
        v += a * dt
        x += max(v, 0) * dt
    return x
for v0 in (5.0, 12.0, 20.0):
    for k in (0.1, 0.3, 0.6):
        for m in (1.0, 50.0):
            assert abs(stop_numeric(v0, k, m) - v0 ** 2 / (2 * k * g)) < 1e-2
# başarısız durum: cisme ters yönlü ek kuvvet etki ediyorsa yol daha uzun
assert stop_numeric(12.0, 0.3, 2.0, extra=2.0) > 12.0 ** 2 / (2 * 0.3 * g) + 1.0
"""),
    SC("angled-force-normal", "Açılı kuvvet: N = m·g ∓ F·sinα (çekme −, itme +)",
       ["friction-angled-force"],
       "Yatayla α açılı yukarı çekmede N = mg − F·sinα, aşağı itmede N = mg + F·sinα; sürtünme k·N, hareket ettiren bileşen F·cosα.",
       "Düşey denge: N + F·sinα = mg (çekme) ve N = mg + F·sinα (itme).",
       ["Yatay zemin", "α yatayla ölçülür", "Cisim zeminde (N ≥ 0)"],
       ["F·sinα > mg ise N < 0: cisim zeminden ayrılır, formül geçersiz", "Açı düşeyle verilmişse sin ve cos yer değiştirir", "Eğik zeminde farklı"],
       "MEDIUM", [TB("s. 137 ÖD-20"), TB("s. 135 ÖD-17")],
       """
import math, random
random.seed(8)
g = 10.0
for _ in range(200):
    m = random.uniform(1, 20)
    F = random.uniform(1, 60)
    al = random.uniform(5, 80)
    ar = math.radians(al)
    if F * math.sin(ar) >= m * g:
        continue
    # vektörlerle düşey denge
    Fy = F * math.sin(ar)
    N_pull = m * g - Fy
    N_push = m * g + Fy
    assert abs(N_pull - (m * g - F * math.sin(ar))) < 1e-12
    assert N_push > N_pull
# başarısız durum: F sinα > mg ise formül negatif N verir
m, F, ar = 2.0, 60.0, math.radians(60)
assert m * g - F * math.sin(ar) < 0
"""),
    SC("special-angle-components", "Özel açılar: sin37° = cos53° = 0,6; cos37° = sin53° = 0,8; 3-4-5 üçgeni",
       ["2d-angled-launch", "friction-angled-force", "frictionless-incline", "fbd-equilibrium-tension", "2d-launch-onto-incline-or-steps"],
       "37°–53°–90° üçgeninde kenar oranları 3:4:5'tir: karşı/hipotenüs 0,6 (37°), 0,8 (53°). Bileşen hesabı tam sayılarla yapılır.",
       "3-4-5 dik üçgeninde 37° karşısındaki kenar 3, komşu 4, hipotenüs 5'tir (yaklaşık: sin37° ≈ 0,6018).",
       ["Açı özel (30°, 37°, 45°, 53°, 60°) ve problemde değerler verilmiş", "Açı yatayla ölçülmüş"],
       ["37° ile 53° yer değiştirirse sonuç 4/3 kat bozulur", "Açı düşeyle verilmişse sin ve cos yer değişir", "Değerler yaklaşıktır (sin37° tam 0,6 değildir); sonuç ≈ ±%0,3 sapar"],
       "MEDIUM", [DV("3-4-5 dik üçgeni; sin37° ≈ 0,6")],
       """
import math
s37, c37 = math.sin(math.radians(37)), math.cos(math.radians(37))
s53, c53 = math.sin(math.radians(53)), math.cos(math.radians(53))
assert abs(s37 - 0.6) < 0.005 and abs(c37 - 0.8) < 0.005
assert abs(s37 - c53) < 1e-12 and abs(c37 - s53) < 1e-12
assert abs(math.tan(math.radians(37)) - 0.75) < 0.005
v0 = 50.0
assert abs(v0 * s53 - 40.0) < 0.3 and abs(v0 * c53 - 30.0) < 0.3
# başarısız durum: 37° ile 53° karışırsa düşey bileşen 4/3 kat yanlış
assert abs((v0 * 0.8) / (v0 * 0.6) - 4 / 3) < 1e-12
# özel açı yaklaşıklığı: tam değerle 0,6 arasındaki fark küçük ama sıfır değil
assert 0 < abs(s37 - 0.6) < 0.005
"""),
]

SHORTCUTS += [
    SC("min-speed-sqrt-gr", "Düşey çember tepesinden geçebilme: ϑ_min = √(g·r)",
       ["vertical-circle-min-speed", "hump-bridge"],
       "İpe bağlı cismin (ya da kovanın) çember tepesinden geçebilmesi için en küçük hız, gerilmenin sıfır olduğu durumdadır: ϑ_min = √(g·r). Tümsek tepesinde aracın yolu terk etme hızı da √(g·r)'dir.",
       "Tepede T + mg = mϑ²/r; T = 0 → mg = mϑ²/r.",
       ["İpe (yalnız çeken) bağlı cisim ya da kova", "Hız tepe noktasındaki hızdır", "Sürtünme/ray yok"],
       ["Çubuğa bağlı cisimde çubuk itebildiği için ϑ_min = 0 olabilir", "Dip noktasındaki hız verilmişse önce enerji korunumu gerekir (tepe hızına çevir)", "Ray sistemlerinde nitel yorum yapılır, hesap yok"],
       "MEDIUM", [TB("s. 111 Cevap"), DV("Tepede T = 0 koşulu")],
       """
import math
g = 10.0
def T_top(m, v, r):
    return m * v * v / r - m * g
for r in (0.5, 0.9, 2.5, 10.0):
    vmin = math.sqrt(g * r)
    for m in (0.1, 1.0, 7.0):
        assert abs(T_top(m, vmin, r)) < 1e-9                  # tam sınırda T = 0
        assert T_top(m, vmin * 1.01, r) > 0                  # biraz hızlıysa ip gergin
        assert T_top(m, vmin * 0.99, r) < 0                  # yavaşsa T < 0: ip itemez
assert abs(math.sqrt(g * 4 * 0.9) / math.sqrt(g * 0.9) - 2.0) < 1e-12     # r 4 kat -> ϑ_min 2 kat
# başarısız durum: çubukta v < √(gr) için negatif T "itme" olarak mümkündür, kısa yol yanlış kısıt verir
assert T_top(1.0, 0.5, 0.9) < 0
"""),
    SC("slip-threshold-ks-g-r", "Kayma eşiği: ϑ_max = √(k_s·g·r), ω_max = √(k_s·g/r)",
       ["flat-curve", "rotating-platform-friction"],
       "Merkezcil kuvveti yalnız statik sürtünme sağlıyorsa k_s·m·g = mϑ²/r = mω²r; kütle sadeleşir.",
       "f_s,max = k_s·N = k_s·m·g ve gereken merkezcil kuvvet mϑ²/r.",
       ["Yatay yol/platform", "Merkezcil kuvveti yalnız sürtünme sağlıyor", "Statik katsayı kullanılıyor"],
       ["Eğimli virajda formül farklıdır", "Kayma başlamışsa kinetik sürtünme geçerli; hareket çembersel olmaz", "Aracın teğetsel ivmesi (fren/gaz) varsa sürtünmenin bir kısmı ona gider, ϑ_max küçülür"],
       "MEDIUM", [TB("s. 117 45. Alıştırma"), TB("s. 109 41. Alıştırma")],
       """
import math, random
random.seed(9)
g = 10.0
for _ in range(200):
    ks = random.uniform(0.05, 1.0)
    r = random.uniform(0.1, 200)
    m = random.uniform(0.1, 2000)
    v = math.sqrt(ks * g * r)
    w = math.sqrt(ks * g / r)
    assert abs(m * v * v / r - ks * m * g) < 1e-6 * m
    assert abs(v - w * r) < 1e-9
    # eşiğin hemen altında kaymaz, üstünde kayar
    assert m * (0.99 * v) ** 2 / r < ks * m * g < m * (1.01 * v) ** 2 / r
# başarısız durum: aynı hızda teğetsel ivme varsa sürtünmenin bir kısmı ona gider
ks, r, m, v, a_t = 0.4, 100.0, 1000.0, 19.0, 2.0
f_needed = m * math.hypot(v * v / r, a_t)
assert f_needed > m * v * v / r          # teğetsel ivme sürtünme ihtiyacını artırır
"""),
    SC("banked-tan-theta", "Eğimli viraj: tanθ = ϑ²/(g·r)",
       ["banked-curve"],
       "Sürtünmesiz eğimli virajda güvenli hız ϑ = √(g·r·tanθ); N = mg/cosθ, merkezcil kuvvet N·sinθ = mg·tanθ.",
       "N·cosθ = mg ve N·sinθ = mϑ²/r denklemleri oranlanınca tanθ = ϑ²/(gr).",
       ["Sürtünme yok", "θ yatayla ölçülür", "Araç tasarım hızında"],
       ["Sürtünmeli virajda güvenli hız aralığı vardır (ϑ_min, ϑ_max)", "Hız tasarım hızından farklıysa araç kayma eğilimindedir", "Açı düşeyle verilmişse tan yerine cot kullanılır"],
       "MEDIUM", [TB("s. 116 Eğimli Virajda"), DV("Bileşen denklemlerinin oranı")],
       """
import math, random
random.seed(10)
g = 10.0
for _ in range(200):
    th = math.radians(random.uniform(5, 60))
    r = random.uniform(10, 200)
    m = random.uniform(500, 2000)
    v = math.sqrt(g * r * math.tan(th))
    N = m * g / math.cos(th)
    assert abs(N * math.sin(th) - m * v * v / r) < 1e-6
    assert abs(N * math.cos(th) - m * g) < 1e-9
# başarısız durum: tasarım hızından farklı hızda yanal sürtünme gerekir
th, r, m = math.radians(37), 30.0, 1000.0
v_design = math.sqrt(g * r * math.tan(th))
v = 1.3 * v_design
f_lateral = m * (v * v / r * math.cos(th) - g * math.sin(th))      # yol boyunca gereken sürtünme
assert abs(f_lateral) > 1000.0
assert abs(m * (v_design ** 2 / r * math.cos(th) - g * math.sin(th))) < 1e-6
"""),
    SC("centripetal-proportions", "Merkezcil kuvvet oranları: F ∝ m·ϑ²/r = m·ω²·r",
       ["horizontal-circle", "circular-kinematics", "circular-variables-data"],
       "ϑ sabitse F ∝ 1/r; ω sabitse F ∝ r; r sabitse F ∝ ϑ² (hız iki kat → kuvvet dört kat); m iki kat → F iki kat. Merkezcil ivme a = ϑ²/r = ω²r = ωϑ.",
       "F = mϑ²/r ve ϑ = ωr.",
       ["Düzgün çembersel hareket", "Karşılaştırılan büyüklükler dışındaki tüm nicelikler sabit"],
       ["Hangi niceliğin sabit tutulduğu (ϑ mı ω mı) yanlış seçilirse r etkisi ters çıkar", "Sürat değişiyorsa (teğetsel ivme) geçersiz", "F_m ayrı bir kuvvet değil bileşkedir; diyagrama ayrı çizilmez"],
       "LOW", [TB("s. 108 Yatay Düzlemde"), TB("s. 109 Örnek")],
       """
import math, random
random.seed(11)
F = lambda m, v, r: m * v * v / r
for _ in range(100):
    m, v, r = random.uniform(0.1, 5), random.uniform(1, 20), random.uniform(0.2, 5)
    w, f = v / r, v / (2 * math.pi * r)
    base = F(m, v, r)
    assert abs(base - m * w * w * r) < 1e-9
    assert abs(base - 4 * math.pi ** 2 * m * f * f * r) < 1e-9
    assert abs(base - m * w * v) < 1e-9
    assert abs(F(m, 2 * v, r) / base - 4) < 1e-9
    assert abs(F(2 * m, v, r) / base - 2) < 1e-9
    assert abs(F(m, v, 2 * r) / base - 0.5) < 1e-9                   # ϑ sabit
    assert abs(m * w * w * (2 * r) / base - 2) < 1e-9                # ω sabit
# başarısız durum: F ∝ ϑ sanmak
assert abs(F(1.0, 4.0, 1.0) / F(1.0, 2.0, 1.0) - 2) > 1
"""),
    SC("vertical-circle-tension-difference", "Düşey çember: T_dip − T_tepe = 2mg (sabit sürat kabulü)",
       ["vertical-circle-tension"],
       "Sabit süratle (programın/kitabın kabulü) dönen cisimde dip gerilmesi tepeden tam 2mg büyüktür; yan noktada T_yan = (T_dip + T_tepe)/2 = mϑ²/r.",
       "Tepede T = mϑ²/r − mg, dipte T = mϑ²/r + mg.",
       ["Sabit sürat kabulü (düzgün çembersel hareket)", "İp kütlesiz"],
       ["Gerçekte (serbest, enerji korunumlu) harekette tepe ve dipteki hızlar farklıdır; fark 6mg olur", "Çubuklu sistemlerde T negatif olabilir", "Ray sistemlerinde hesap yok"],
       "HIGH", [TB("s. 110 Tablo 1.3"), TB("s. 112 enerji korunumuyla ele alınış")],
       """
g = 10.0
for m in (0.2, 1.0, 5.0):
    for v, r in ((5.0, 0.5), (8.0, 2.0), (12.0, 4.0)):
        Fm = m * v * v / r
        top, side, bot = Fm - m * g, Fm, Fm + m * g
        assert abs((bot - top) - 2 * m * g) < 1e-9
        assert abs(side - (top + bot) / 2) < 1e-9
        # başarısız durum: serbest (enerji korunumlu) harekette tepe hızı v, dip hızı √(v² + 4 g r)
        v_bot2 = v * v + 4 * g * r
        bot_real = m * v_bot2 / r + m * g
        assert abs((bot_real - top) - 6 * m * g) < 1e-9
        assert abs((bot_real - top) - (bot - top)) > 1.0
"""),
    SC("hump-bridge-normal", "Tümsek tepesi N = m(g − ϑ²/r), çukur dibi N = m(g + ϑ²/r)",
       ["hump-bridge"],
       "Tümsekte araç ağırlığından hafif, çukurda ağır hisseder; tümsekte N = 0 olduğunda araç yoldan ayrılır (ϑ = √(g·r)).",
       "Merkez tümsekte aşağıda: mg − N = mϑ²/r; çukurda merkez yukarıda: N − mg = mϑ²/r.",
       ["Dairesel yay kabulü", "Sabit sürat", "Araç noktasal"],
       ["ϑ > √(g·r) olunca formül N < 0 verir: araç yolu terk eder, formül geçersiz", "Yarıçap çapla karıştırılırsa sonuç 2 kat yanlış", "Sürat değişiyorsa teğetsel bileşen eklenir"],
       "MEDIUM", [TB("s. 145 ÖD-34")],
       """
import math
g = 10.0
N_hump = lambda m, v, r: m * (g - v * v / r)
N_dip = lambda m, v, r: m * (g + v * v / r)
m, r = 800.0, 40.0
assert abs(N_hump(m, 10.0, r) - 6000.0) < 1e-9 and abs(N_dip(m, 10.0, r) - 10000.0) < 1e-9
vleave = math.sqrt(g * r)
assert abs(N_hump(m, vleave, r)) < 1e-9
# başarısız durum: ϑ > √(gr) ise N negatif (araç yolu terk eder)
assert N_hump(m, 1.1 * vleave, r) < 0
# başarısız durum: yarıçap yerine çap kullanmak sonucu iki kat bozar
assert abs((m * 100 / 80) - (m * 100 / 40)) > 1.0
"""),
    SC("terminal-velocity-sqrt-m-over-a", "Limit hız: ϑ_limit ∝ √(m/A)",
       ["terminal-velocity-variables", "terminal-velocity-daily-life", "terminal-velocity-graph"],
       "Direnç ∝ A·ϑ² modelinde limit hız ϑ ∝ √(m/A): kütle 4 kat → limit hız 2 kat; kesit alanı 4 kat → limit hız yarıya iner; yükseklikten bağımsızdır.",
       "Limit hızda net kuvvet 0: k·A·ϑ² = m·g.",
       ["Direnç hızın karesiyle orantılı (yüksek hızlı hareket)", "Aynı ortam, aynı şekil katsayısı"],
       ["Program sayısal limit hız hesaplamasını istemez: yalnız orantı/yorum (CALC_EXCLUDED)", "Çok yavaş (viskoz) hareketlerde direnç ∝ ϑ olur ve ϑ ∝ m çıkar", "Şekil katsayısı değişirse (paraşüt açma) k de değişir"],
       "HIGH", [TB("s. 90 Tablo 1.2"), TB("s. 144 ÖD-31")],
       """
import math
g, k = 10.0, 0.4
def vt_numeric(m, A, T=400.0, dt=0.002):
    v = 0.0
    for _ in range(int(T / dt)):
        v += (g - k * A * v * v / m) * dt
    return v
base = vt_numeric(1.0, 1.0)
assert abs(base - math.sqrt(1.0 * g / (k * 1.0))) < 1e-2
assert abs(vt_numeric(4.0, 1.0) / base - 2.0) < 1e-2
assert abs(vt_numeric(1.0, 4.0) / base - 0.5) < 1e-2
# başarısız durum: viskoz (doğrusal) direnç F = b v için limit hız ∝ m (kare kök değil)
b = 2.0
vt_lin = lambda m: m * g / b
assert abs(vt_lin(4.0) / vt_lin(1.0) - 4.0) < 1e-12 and abs(vt_lin(4.0) / vt_lin(1.0) - 2.0) > 1
"""),
    SC("control-variable-ratio-test", "Veri tablosunda kontrol değişkeni + oran testi (f/N, F/ϑ², F·r, Δ²y)",
       ["friction-variables-data", "drag-variables-data", "circular-variables-data", "newton2-f-m-a-relations", "ff-data-evidence"],
       "Tek değişkenin değiştiği satırları karşılaştır; ilişkiyi oran sabitliğiyle test et (f/N, F/ϑ², F·r, a·m).",
       "Doğru orantıda y/x sabit, ters orantıda y·x sabit, karesel ilişkide y/x² sabittir.",
       ["Kontrollü deney verisi", "Ölçüm hatası küçük"],
       ["İki değişkenin birlikte değiştiği satırları karşılaştırmak yanlış sonuç verir (alan ve kütle birlikte iki katına çıkınca f iki katına çıkar ama alan etkili değildir)", "Ölçüm belirsizliğinde oran tam sabit çıkmaz", "Tek satır çiftinden genelleme riskli"],
       "MEDIUM", [TB("s. 70 7. Etkinlik"), TB("s. 90 Tablo 1.2"), DV("Oran sabitliği testi")],
       """
g = 10.0
rows = [dict(m=2, A=100, f=6.0), dict(m=2, A=200, f=6.0), dict(m=4, A=100, f=12.0), dict(m=4, A=200, f=12.0)]
def effect(var, other):
    pairs = [(a, b) for a in rows for b in rows if a[var] != b[var] and a[other] == b[other]]
    return {round(b['f'] / a['f'], 6) for a, b in pairs}
assert effect('A', 'm') == {1.0}                                         # alan: f değişmiyor
assert effect('m', 'A') == {2.0, 0.5}                                    # kütle: f orantılı
# başarısız durum: iki değişkenin birlikte değiştiği satırlar
a, b = rows[0], rows[3]
assert b['f'] / a['f'] == 2.0 and b['A'] / a['A'] == 2.0                 # "alan 2 kat, f 2 kat" yanlış çıkarım (asıl neden kütle)
# oran sabitliği: karesel veri
v = [1, 2, 3, 4]; F = [0.75 * x * x for x in v]
assert len({round(F[i] / v[i] ** 2, 9) for i in range(4)}) == 1
assert len({round(F[i] / v[i], 9) for i in range(4)}) > 1
"""),
    SC("lami-three-forces", "Üç kuvvetin dengesi: Lami teoremi (özel açılarda 3-4-5)",
       ["fbd-equilibrium-tension"],
       "Dengede üç kuvvetten her biri, karşısındaki açının sinüsüyle orantılıdır: T₁/sinα₁ = T₂/sinα₂ = mg/sinα₃ (α_i: diğer iki kuvvet arasındaki açı). Yatayla 37°–53° iplerde T = 0,6mg ve 0,8mg.",
       "Üç kuvvetin vektör toplamı kapalı bir üçgen oluşturur; sinüs teoremi uygulanır.",
       ["Tam üç eş düzlemli kuvvet", "Denge (net kuvvet sıfır)", "Kuvvetler tek noktada kesişir"],
       ["Dört ve daha fazla kuvvette uygulanmaz (ör. ek yatay çekme kuvveti)", "Lami ders kitabında yoktur; program bileşen yöntemini öğretir, sonuç için bileşen denklemleri esastır", "Açılar iki kuvvet arasındaki açıdır; yatayla ölçülen açıyla karıştırılmamalı"],
       "MEDIUM", [DV("Sinüs teoremi, kapalı kuvvet üçgeni")],
       """
import math, random
random.seed(12)
g, m = 10.0, 5.0
W = m * g
for _ in range(200):
    a1, a2 = math.radians(random.uniform(10, 80)), math.radians(random.uniform(10, 80))   # iplerin yatayla açıları (sol, sağ)
    # bileşenlerden: T1 cos a1 = T2 cos a2 ; T1 sin a1 + T2 sin a2 = W
    T1 = W * math.cos(a2) / math.sin(a1 + a2)
    T2 = W * math.cos(a1) / math.sin(a1 + a2)
    assert abs(T1 * math.cos(a1) - T2 * math.cos(a2)) < 1e-9
    assert abs(T1 * math.sin(a1) + T2 * math.sin(a2) - W) < 1e-9
    # Lami: T1 / sin(açı(T2, W)) = T2 / sin(açı(T1, W)) = W / sin(açı(T1, T2))
    ang_T2_W = math.pi / 2 + a2          # T2 ile ağırlık arasındaki açı
    ang_T1_W = math.pi / 2 + a1
    ang_T1_T2 = math.pi - a1 - a2
    assert abs(T1 / math.sin(ang_T2_W) - W / math.sin(ang_T1_T2)) < 1e-9
    assert abs(T2 / math.sin(ang_T1_W) - W / math.sin(ang_T1_T2)) < 1e-9
assert abs(W * math.cos(math.radians(53)) / math.sin(math.radians(90)) - 0.6 * W) < 0.2
# başarısız durum: dört kuvvet (ek yatay çekme H) varsa üç kuvvetli Lami sonucu yanlış kalır
H = 20.0
a1 = a2 = math.radians(45)
T1_lami = W * math.cos(a2) / math.sin(a1 + a2)
# gerçek denge: T1 cos a1 + H = T2 cos a2 ; T1 sin a1 + T2 sin a2 = W  =>  T1 sin(a1+a2) = W cos a2 - H sin a2
T1s = (W * math.cos(a2) - H * math.sin(a2)) / math.sin(a1 + a2)
T2s = (T1s * math.cos(a1) + H) / math.cos(a2)
assert abs(T1s * math.cos(a1) + H - T2s * math.cos(a2)) < 1e-9 and abs(T1s * math.sin(a1) + T2s * math.sin(a2) - W) < 1e-9
assert abs(T1s - T1_lami) > 5.0
"""),
    SC("rotor-min-omega", "Rotor: N = mω²r merkezcil; düşmemek için ω ≥ √(g/(k_s·r))",
       ["rotor-and-regulator"],
       "Dönen silindirde duvarın normal kuvveti merkezcil kuvveti sağlar (N = mω²r); sürtünme ağırlığı taşır (k_s·N ≥ mg) → ω_min = √(g/(k_s·r)); kütle sadeleşir.",
       "Yatay: N = mω²r; düşey: f = mg ≤ k_s·N.",
       ["Kişi duvara yapışık, silindir düzgün dönüyor", "Statik sürtünme katsayısı biliniyor"],
       ["Sürtünme merkezcil kuvvete katılmaz (düşeydedir); yatay denklemde yer almaz", "Zemin çekilmeden önce sürtünme gerekmez", "Katsayı kinetik alınırsa yanlış"],
       "MEDIUM", [TB("s. 146 ÖD-35")],
       """
import math
g = 10.0
for r in (1.0, 2.5, 5.0):
    for ks in (0.2, 0.4, 0.8):
        w = math.sqrt(g / (ks * r))
        for m in (30.0, 60.0, 90.0):
            N = m * w * w * r
            assert abs(ks * N - m * g) < 1e-9                # tam eşikte sürtünme tavanı = ağırlık
            N2 = m * (0.95 * w) ** 2 * r
            assert ks * N2 < m * g                           # biraz yavaşsa düşer
assert abs(math.sqrt(g / (0.4 * 2.5)) - math.sqrt(10.0)) < 1e-12
# başarısız durum: sürtünmeyi merkezcil denkleme katmak ω'yı değiştirir
m, ks, r = 60.0, 0.4, 2.5
w_wrong = math.sqrt((m * g / ks + ks * (m * g / ks)) / (m * r))
assert abs(w_wrong - math.sqrt(g / (ks * r))) > 0.1
"""),
    SC("second-difference-rule", "Eşit aralıklı konum tablosunda ikinci fark: Δ²y = a·Δt²",
       ["ff-data-evidence", "2d-component-data", "ff-data-pattern-g"],
       "Eşit zaman aralıklı konum verisinde ardışık farkların farkı sabitse hareket sabit ivmelidir ve a = Δ²y/Δt²; ilk hızdan bağımsızdır. Eksik değer = bir önceki fark + Δ².",
       "y(t+Δt) − 2y(t) + y(t−Δt) = a·Δt² (sabit ivmede kesin).",
       ["Zaman aralıkları eşit", "İvme sabit", "Ölçüm hatası küçük"],
       ["Aralıklar eşit değilse ikinci fark sabit çıkmaz", "İvme değişiyorsa (hava direnci) sabit çıkmaz", "Ölçüm hatasında yaklaşık eşitlik aranmalı"],
       "LOW", [TB("s. 21 2. Etkinlik"), DV("Merkezî ikinci fark")],
       """
import random
random.seed(13)
for _ in range(100):
    a = random.uniform(-12, 12)
    v0 = random.uniform(-20, 20)
    y0 = random.uniform(-5, 5)
    dt = random.uniform(0.05, 0.5)
    y = [y0 + v0 * (i * dt) + 0.5 * a * (i * dt) ** 2 for i in range(8)]
    d1 = [y[i + 1] - y[i] for i in range(7)]
    d2 = [d1[i + 1] - d1[i] for i in range(6)]
    assert all(abs(x - a * dt * dt) < 1e-9 for x in d2)
    nxt = y[-1] + d1[-1] + d2[-1]
    assert abs(nxt - (y0 + v0 * (8 * dt) + 0.5 * a * (8 * dt) ** 2)) < 1e-9
# başarısız durum: eşit olmayan aralıklarda ikinci fark sabit çıkmaz
ts = [0, 0.1, 0.3, 0.4, 0.8]
y = [5 * t * t for t in ts]
d1 = [y[i + 1] - y[i] for i in range(4)]
d2 = [d1[i + 1] - d1[i] for i in range(3)]
assert max(d2) - min(d2) > 0.1
"""),
]
