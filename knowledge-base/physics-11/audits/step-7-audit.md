# Denetim — STEP 7 (Formül Veritabanı)

- **Tarih:** 2026-10-01
- **Dosyalar:** `formulas/formulas.json`, `formulas/formulas.md`
- **Kaynak veri:** `scripts/data_formulas.py`
- **Üretim:** `scripts/build_formulas.py`
- **Doğrulama:** `python3 scripts/run_all_audits.py` → ✓ 0 hata

## Yöntem
1. Ders kitabından çıkarılan metinde formül sembolleri bozuluyor: hız sembolü ϑ "θ" olarak çıkıyor, kesirler dağılıyor (ör. "E = r2").
2. Bu yüzden formüller, 30 sayfanın **sayfa görüntüsü** tek tek incelenerek doğrulandı. İncelenen sayfalar: bölüm sonu "Kontrol Noktası" özetleri, formül kutuları ve çözümlü örnekler.
3. Her formül otomatik **boyut analizinden** geçirildi. Temel boyutlar M, L, T, I, J; açı ve π boyutsuz.
4. Her formüle programdaki hesap durumu, ilgili çıktıların resmî kapsam sınırlarından türetildi. Sınırların kapsamı "tüm çıktı" ya da "kısmi" olarak ayrıldı.

## Sonuçlar

| Ölçüt | Değer |
|---|---|
| Formül | 53 |
| Boyut analizi | 53/53 geçti |
| Sayfa görüntüsünden doğrulanan | 48 |
| Kitapta doğrulanamayan (türetilmiş) | 3: ilk hız bileşenleri, yatay virajda azami hız, sınır açısı formülü. Hepsi programın ya da kitabın sorularında kullanılıyor. |
| Müfredat dışı olarak işaretlenen | 2: ayna/mercek denklemi, görüntü sayısı formülü. İkisi de kitapta yok. |
| "Ne zaman kullanılmaz" alanı dolu | 53/53 (zorunlu, doğrulayıcı denetliyor) |
| Formülü olan öğrenme çıktısı | 25/33. Kalan 8 çıktı nitel: Faraday kafesi, mıknatıs etkileşimi, elektromıknatıs, motor, fiber optik, prizma, görüntü oluşumu, görünür derinlik. |

**Programdaki hesap durumuna göre dağılım:**
- Hesap açıkça var: 15
- Açık sınır yok: 19
- Sınırlı: 5
- Hesaplama dışlanmış: 11
- Yalnız kavramsal: 1
- Müfredat dışı: 2

## Kaynak hataları ve çelişkiler

### 1. Ders kitabı fizik hatası
Tablo 1.2 (s. 90), F_d = k·A·ϑ² bağıntısındaki k'yı "boyutsuz bir katsayı" olarak tanımlıyor. Boyut analizine göre k'nın birimi kg/m³ olmalı. Bu varsayım otomatik boyut testinde **reddedildi**: sol taraf L·M·T⁻², sağ taraf L⁴·T⁻² çıkıyor. Formül kaydında `notes` alanına yazıldı.

### 2. Ders kitabı iç tutarsızlığı
Eğimli viraj türetmesinde (s. 116) metin N_x'i yatay bileşen olarak tanımlıyor, denklemlerde ise alt indisler ters yazılmış. Sonuç formülü ϑ = √(tanθ·g·r) doğru.

### 3. Kitap ve program çelişkisi (iki kaynak da Tier 1): 12 formül
Program bu çıktılarda hesaplamayı dışlıyor ("matematiksel hesaplamalara girmeden", "matematiksel işlemlerden kaçınılır"). Ders kitabı ise formülü veriyor ve çoğunda sayısal örnek ya da alıştırma var.

| Çıktı | Formüller |
|---|---|
| FİZ.11.1.8 Limit hız | F_d = k·A·ϑ², ϑ_limit = √(mg/kA) |
| FİZ.11.2.1 Coulomb | F = k·q₁q₂/d², k = 1/(4πε₀) |
| FİZ.11.2.2 Elektriksel alan | E = F/q₀, E = k·q/d², E = V/d |
| FİZ.11.2.5 Düz tel | B = 2·K·i/d |
| FİZ.11.2.10 Manyetik akı | Φ = B·A·cosθ (program: "kavramsal olarak açıklar") |
| FİZ.11.2.13 Transformatör | Vp/Vs = Np/Ns = is/ip, verim, P = V·i, P = i²R (47. Alıştırma'da sayısal soru, s. 272) |

**Yapay zekâ için sonuç:** Bu formüller bilinmeli ve öğrenciye gösterilebilir. Ancak ÖSYM'nin bu konularda sayısal soru sorup sormayacağı **doğrulanamaz** (STEP 10'da incelenecek). Formül kayıtlarında `textbook_vs_program_conflict: true` işareti var.

### 4. Programda adı geçmeyip kitapta olan içerik
- E = V/d ve paralel levhalar (s. 176, 185)
- Alternatif akımda etkin değer (s. 259)
- Lenz Yasası (s. 262)
- Beyaz ışığın renklere ayrılması (s. 353, 372). Programda prizma çıktısı "tek renkli ışık" ile sınırlı, renkler 12. sınıf konusu.
- Yay sabiti F = k·x (s. 109, çözümlü örnek). Bu bir 12. sınıf kavramı.

### 5. Kitapta olmayan, eski kaynaklarda sık görülen formüller
- Ayna ve mercek denklemi
- Açılı aynalarda görüntü sayısı

Yapay zekâ bunları beklenen yöntem olarak öğretmemeli; kayıtlarda `OUT_OF_CURRICULUM` olarak işaretli.

## Sonraki adımlar için notlar
- **Kısa yol kaynağı (STEP 12):** Kitap, serbest düşmede ardışık eşit sürelerde alınan yolların h : 3h : 5h : 7h oranında olduğunu resmî olarak veriyor (s. 29). Kısa yollar veritabanında bu, "resmî kaynaklı" olarak işaretlenecek.
- **Sesli öğretmen hazırlığı:** Her formülün `spoken_tr` alanında Türkçe sesli okunuşu var.
- **İnceleme:** Formül kayıtları uzman incelemesi bekliyor (`review_status: ai_authored_pending_expert_review`).
