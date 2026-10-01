# 11. Sınıf Fizik — Formül Veritabanı

> Otomatik üretildi: `scripts/build_formulas.py` (kaynak: `scripts/data_formulas.py`). Elle düzenleme yapma.

Her formül MEB 11. sınıf ders kitabının **sayfa görüntüsünden** doğrulandı (metin çıkarımı sembolleri bozuyor). Kitap gösterimi: hız **ϑ**, akım **i**, manyetik alan katsayısı **K**, Coulomb sabiti **k**.

- Formül: **53** · boyut analizi: **53/53** · kitapta doğrulanan: **48**
- Kitap–program çelişkisi (kitap formül veriyor, program hesaplamayı dışlıyor): **12**

## Kaynak hataları ve çelişkiler

- **Akışkan direnç kuvveti** — KAYNAK HATASI: Kitap Tablo 1.2 (s. 90) k'yı 'boyutsuz bir katsayı' olarak tanımlıyor. Boyut analizi k'nın birimini kg/m³ verir; k boyutsuz olamaz. Bu kayıt boyut testinde ayrıca doğrulanır (DIM_OVERRIDES).
- **Sürtünmesiz eğimli virajda güvenli hız** — KAYNAK TUTARSIZLIĞI: Kitap s. 116'da metin N_x'i yatay (merkezcil), N_y'yi düşey bileşen olarak tanımlıyor; hemen altındaki denklemlerde alt indisler ters (N_y = N·sinθ = F_m, N_x = N·cosθ = m·g). Sonuç formülü doğru.
- **İdeal transformatör** — KAYNAK ÇELİŞKİSİ (Tier 1 – Tier 1): Program 'Matematiksel işlemlerden kaçınılır' derken kitap bu bağıntıyı ve sayısal alıştırma (47a, s. 272) veriyor.
- Boyut testi: 'k boyutsuz (ders kitabı Tablo 1.2, s. 90)' varsayımı **rejected** (F_d ≠ k·A·ϑ² boyutları: L M T^-2, L^4 T^-2).

## Ünite 1

| ID | Formül | Çıktı | Kitap | Program | Ne zaman kullanılmaz (ilk madde) |
|---|---|---|---|---|---|
| 001 | `h = ½·g·t²` | 1.2 | s. 29 | · açık sınır yok | İlk hızı sıfırdan farklı cisimlerde (h = ϑ₀t ± ½gt² kullanılır) |
| 002 | `ϑ = g·t` | 1.1, 1.2 | s. 29 | · açık sınır yok | İlk hızlı hareketlerde |
| 003 | `ϑ² = 2·g·h` | 1.2 | s. 29 | · açık sınır yok | İlk hızlı hareketlerde (ϑ² = ϑ₀² ± 2gh) |
| 004 | `h = ϑ₀·t ± ½·g·t²` | 1.2 | s. 29 | · açık sınır yok | Yatayda ilk hız bileşeni varken düşey bileşen yerine toplam hız konursa |
| 005 | `ϑ = ϑ₀ ± g·t` | 1.2 | s. 29 | · açık sınır yok | Hava direncinin önemli olduğu durumlarda |
| 006 | `ϑ² = ϑ₀² ± 2·g·h` | 1.2 | s. 29 | · açık sınır yok | h yerine toplam alınan yol konursa (yukarı çıkıp inen cisimde) |
| 007 | `x = ϑₓ·t ;  x_menzil = ϑₓ·t_uçuş` | 1.3 | s. 39 | ✓ hesap açıkça var | Yatayda bir kuvvet/ivme varsa (ör. rüzgâr) |
| 008 | `ϑₓ = ϑ₀·cosα ;  ϑᵧ = ϑ₀·sinα` | 1.3 | — | ✓ hesap açıkça var | Açı düşeyle verilmişse sin ve cos yer değiştirir |
| 009 | `h = ϑᵧ·t − ½·g·t² ;  ϑᵧ₁ = ϑᵧ − g·t ;  ϑ² = ϑᵧ² − 2·g·h` | 1.3 | s. 39 | ✓ hesap açıkça var | Toplam hız (ϑ₀) düşey bileşen yerine konursa |
| 010 | `F⃗_net = m·a⃗` | 1.4, 1.5 | s. 64 | ◑ sınırlı | Tek bir kuvvet (bileşke değil) konursa |
| 011 | `G = m·g` | 1.5, 1.10 | s. 116 | ◑ sınırlı | Kütle ile ağırlığın aynı nicelik olarak kullanılması |
| 012 | `a = g·sinθ` | 1.5 | s. 60 | ◑ sınırlı | Sürtünmeli eğik düzlemde |
| 013 | `tanθ = a/g` | 1.5 | s. 63 | ◑ sınırlı | Araç sabit hızla gidiyorsa (θ = 0) |
| 014 | `a = ΣF_dış / Σm` | 1.5, 1.7 | s. 80 | ◑ sınırlı | Cisimler farklı ivmeyle hareket ediyorsa (program: kapsam dışı) |
| 015 | `f = k·N  (statik: f_s ≤ k_s·N ;  kinetik: f_k = k_k·N)` | 1.7 | s. 85 | ✓ hesap açıkça var | Cisim kaymıyorken f_s = k_s·N almak (yalnız harekete geçme sınırında geçerli) |
| 016 | `k_k = tanθ` | 1.7 | s. 82 | ✓ hesap açıkça var | Cisim ivmeli kayıyorsa |
| 017 | `F_d = k·A·ϑ²` | 1.8 | s. 90 | ⛔ program hesaplamayı dışlıyor ⚠️ | Programda sayısal hesap istenmez: FİZ.11.1.8 'yorumlamalarla sınırlı kalınır' |
| 018 | `ϑ_limit = √( m·g / (k·A) )` | 1.8 | s. 90 | ⛔ program hesaplamayı dışlıyor ⚠️ | Programda sayısal hesap istenmez; yalnız orantı yorumu (m↑ → ϑ_limit↑, A↑ → ϑ_limit↓) |
| 019 | `T·f = 1` | 1.10, 2.12 | s. 104 | ✓ hesap açıkça var | Periyodik olmayan harekette |
| 020 | `ϑ = 2·π·r / T = 2·π·r·f` | 1.10 | s. 104 | ✓ hesap açıkça var | Sürat değişiyorsa (düzgün olmayan çembersel hareket) |
| 021 | `ω = 2·π / T = 2·π·f` | 1.10 | s. 104 | ✓ hesap açıkça var | Açı derece cinsinden kullanılırsa |
| 022 | `ϑ = ω·r` | 1.10 | s. 104 | ✓ hesap açıkça var | Kayışla ya da temasla bağlı farklı tekerleklerde ω'nin eşit sanılması (bu durumda çizgisel süratler eşittir) |
| 023 | `a = ϑ²/r = ω²·r = 4·π²·f²·r` | 1.10 | s. 109 | ✓ hesap açıkça var | Teğetsel ivmenin olduğu (sürati değişen) harekette toplam ivme yerine kullanılması |
| 024 | `F_m = m·ϑ²/r = m·ω²·r` | 1.10 | s. 108 | ✓ hesap açıkça var | Serbest cisim diyagramına ayrı bir 'merkezcil kuvvet' oku eklenirse (çift sayım) |
| 025 | `Tepe: F_m = T + G ;  Dip: F_m = T − G ;  Yan: F_m = T` | 1.10 | s. 110 | ✓ hesap açıkça var | Gerçekte sürat tepe ve dipte farklıysa her noktada aynı ϑ kullanılması (kitap s. 112 bunu enerji korunumuyla ayrıca ele alır) |
| 026 | `ϑ_min = √(g·r)` | 1.10 | s. 111 | ✓ hesap açıkça var | Çubuğa bağlı cisimde (çubuk itebilir, ϑ_min = 0 olabilir) |
| 027 | `ϑ = √(tanθ·g·r)` | 1.10 | s. 116 | ✓ hesap açıkça var | Sürtünmeli eğimli virajda (hız aralığı değişir) |
| 028 | `ϑ_max = √(k_s·g·r)` | 1.10 | — | ✓ hesap açıkça var | Eğimli virajda |

## Ünite 2

| ID | Formül | Çıktı | Kitap | Program | Ne zaman kullanılmaz (ilk madde) |
|---|---|---|---|---|---|
| 019 | `T·f = 1` | 1.10, 2.12 | s. 104 | ✓ hesap açıkça var | Periyodik olmayan harekette |
| 029 | `F = k·q₁·q₂ / d²` | 2.1 | s. 160 | ⛔ program hesaplamayı dışlıyor ⚠️ | PROGRAM: FİZ.11.2.1 'matematiksel hesaplamalara girmeden'; sayısal hesap yerine oran/yön yorumu beklenir |
| 030 | `k = 1/(4·π·ε₀) ≈ 9·10⁹ N·m²/C²` | 2.1 | s. 161 | ⛔ program hesaplamayı dışlıyor ⚠️ | Yalıtkan ortamda boşluk değeri kullanılırsa (k küçülür) |
| 031 | `E = F / q₀` | 2.2 | s. 185 | ⛔ program hesaplamayı dışlıyor ⚠️ | PROGRAM: FİZ.11.2.2 hesaplamasız |
| 032 | `E = k·q / d²` | 2.2 | s. 185 | ⛔ program hesaplamayı dışlıyor ⚠️ | PROGRAM: FİZ.11.2.2 hesaplamasız; oran ve yön yorumu beklenir |
| 033 | `E = V / d` | 2.2 | s. 185 | ⛔ program hesaplamayı dışlıyor ⚠️ | Noktasal yük alanında |
| 034 | `B = 2·K·i / d` | 2.5 | s. 235 | ⛔ program hesaplamayı dışlıyor ⚠️ | PROGRAM: FİZ.11.2.5 'matematiksel hesaplamalara girmeden'; oran/yön yorumu beklenir |
| 035 | `B = 4·π·K·i·N / L` | 2.6 | s. 235 | · açık sınır yok | Demir çekirdekli makarada (alan çok artar) |
| 036 | `F = B·i·L·sinθ` | 2.8 | s. 235 | · açık sınır yok | Tel alana paralelse (θ = 0, F = 0) |
| 037 | `Φ = B·A·cosθ` | 2.10 | s. 262 | ◐ program kavramsal ⚠️ | θ yüzeyle ölçülen açı alınırsa (cos yerine sin gerekir) |
| 038 | `ε = −N·ΔΦ / Δt` | 2.11 | s. 262 | · açık sınır yok | Akı sabitse (alan büyük olsa bile ε = 0) |
| 039 | `ε = i·R` | 2.11 | s. 248 | · açık sınır yok | Devre açıksa (akım yok, gerilim var) |
| 040 | `V_max = V_etkin·√2 ;  i_max = i_etkin·√2` | 2.12 | s. 259 | · açık sınır yok | Kare/üçgen dalgada |
| 041 | `P = V·i ;  P_kayıp = i²·R` | 2.13 | s. 263 | ⛔ program hesaplamayı dışlıyor ⚠️ | P_kayıp = V²/R'de V olarak hattın iki ucu arası değil şebeke gerilimi konursa |
| 042 | `V_p / V_s = N_p / N_s = i_s / i_p` | 2.13 | s. 273 | ⛔ program hesaplamayı dışlıyor ⚠️ | PROGRAM: FİZ.11.2.13 'Matematiksel işlemlerden kaçınılır'; yalnız nitel ilişki |
| 043 | `verim = (V_s·i_s) / (V_p·i_p)` | 2.13 | s. 273 | ⛔ program hesaplamayı dışlıyor ⚠️ | PROGRAM: FİZ.11.2.13 hesaplamasız |

## Ünite 3

| ID | Formül | Çıktı | Kitap | Program | Ne zaman kullanılmaz (ilk madde) |
|---|---|---|---|---|---|
| 044 | `E = Φ / A` | 3.1 | s. 311 | · açık sınır yok | Işınlar yüzeye eğik geliyorsa (dik bileşen gerekir) |
| 045 | `Φ = 4·π·I` | 3.1 | s. 311 | · açık sınır yok | Kaynak yönlüyse (el feneri) |
| 046 | `E = I / r²` | 3.1 | s. 311 | · açık sınır yok | Paralel ışık veren kaynakta (el feneri: uzaklıkla değişmez) |
| 047 | `n = c / ϑ` | 3.5 | s. 352 | · açık sınır yok | n < 1 sonucu çıkarsa (sıradan ortamlarda olmaz) |
| 048 | `n₁·sin î = n₂·sin r̂` | 3.5, 3.8 | s. 352 | · açık sınır yok | Açılar yüzeyle ölçülmüşse |
| 049 | `sin θ_s = n₂ / n₁   (n₁ > n₂)` | 3.5, 3.7 | — | · açık sınır yok | Işık az kırıcıdan çok kırıcıya gidiyorsa (sınır açısı ve tam yansıma yok) |
| 050 | `r = 2·f` | 3.3 | s. 341 | · açık sınır yok | Asal eksenden uzak ışınlarda (küresel sapınç) |
| 051 | `d_görüntü = d_cisim ;  h_görüntü = h_cisim` | 3.2 | s. 322 | · açık sınır yok | Küresel aynalarda |
| 052 | `1/f = 1/d_c + 1/d_g` | 3.4, 3.10 | — | ✗ müfredat dışı | 11. sınıf Maarif programı ve ders kitabında YOK: görüntü konumu özel ışın çizimi ve konum tablosuyla bulunur |
| 053 | `n = 360°/α − 1` | 3.2 | — | ✗ müfredat dışı | 11. sınıf Maarif ders kitabında YOK |
