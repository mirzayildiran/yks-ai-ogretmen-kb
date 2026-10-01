# 11. Sınıf Fizik — Kapsam Sınırları (Yapay Zekâ İçin Kurallar)

Kaynak: MEB TYMM 11. sınıf fizik ünite sayfaları, güncelleme 05.08.2026.
Ham metin: `mufredat/meb-ham/`, yapılandırılmış hâli: `mufredat/fizik11_ogretim_programi.json`.

Bu dosya, öğretmen yapay zekânın **neyi hesaplatabileceğini, neyi yalnızca yorumlatacağını ve hangi terimleri kullanmayacağını** belirler.
"MEB metni" sütunu programdan alıntıdır; "Yapay zekâ kuralı" bizim yorumumuzdur.

## Genel çerçeve

| Ünite | Ders saati | Çıktı sayısı |
|---|---|---|
| 1. Kuvvet ve Hareket | 54 | 10 (FİZ.11.1.1–10) |
| 2. Elektrik ve Manyetizma | 48 | 13 (FİZ.11.2.1–13) |
| 3. Optik | 36 | 10 (FİZ.11.3.1–10) |
| **Toplam** | **138** | **33** |

Not: Bazı blog siteleri 11. sınıfta "Madde ve Doğası" ünitesi (yarı iletkenlik, süper iletkenlik) listeliyor. MEB'in güncel sayfasında bu konu **12. sınıfta** (FİZ.12.4.4–5). 11. sınıfta yalnız üç ünite var.

## Ünite 1 — Kuvvet ve Hareket

**Ön bilgi (temel kabul):** hız, ivme, ağırlık, periyot, frekans. 10. sınıftan bir boyutta sabit hızlı/sabit ivmeli hareket ve grafik dönüşümleri (FİZ.10.1.1–3), 9. sınıftan vektörler (FİZ.9.2.3–4).

| Çıktı | MEB metni (sınır) | Yapay zekâ kuralı |
|---|---|---|
| 11.1.1–2 Serbest düşme | "Yer çekimi ivmesi sabit kabul edilir." Hava direnci ihmal. "'Düşey atış hareketi' şeklinde hareket türü tanımından kaçınılır." Serbest düşme = yalnız yer çekimi etkisindeki tüm hareketlerin ortak adı. | İlk hızı sıfır olan ve olmayan düşey hareketlerin hepsine "serbest düşme" de. "Aşağı/yukarı düşey atış" deme; öğrenci eski kaynaktan bu terimi getirirse eşleştirip açıkla. x-t, v-t, a-t grafikleri ve hesap serbest. |
| 11.1.3 İki boyutta sabit ivmeli hareket | "'Yatay atış' ve 'eğik atış' şeklinde hareket türü tanımından kaçınılır." Yalnız yer çekimi ivmesi etkisinde. Trigonometriyle bileşenlere ayırma var. | Hareketi yatayda sabit hız + düşeyde sabit ivme olarak ayrıştır. Hesap ve grafik yorumu serbest. Eski kaynaklardaki "yatay atış/eğik atış" soruları içerik olarak geçerli, yalnız adlandırma farklı. |
| 11.1.4–5 Newton yasaları, serbest cisim diyagramı | "Farklı büyüklükteki ivmeyle hareket eden cisimlerin bir arada olduğu sistemlerle ilgili matematiksel hesaplamalardan kaçınılır. Sabit ivmeli hareket ile sınırlı kalınır." | Bağlı sistemlerde tüm cisimler aynı ivmeyle hareket etmeli (ip-makara, üst üste bloklar birlikte). Farklı ivmeli sistem (ör. kayan blok üstünde kayan blok) hesaplatma. |
| 11.1.6–7 Statik/kinetik sürtünme | Sürtünme–uygulanan kuvvet grafiği, matematiksel model (f = k·N). Destekleme düzeyinde: yatay zeminde ek düşey kuvvet yok. | Hesap serbest. Eğik düzlem ve ek düşey kuvvet içeren sorular ileri düzey. Kayarak ve dönerek öteleme hareketinde sürtünmenin yönü kavramsal. |
| 11.1.8 Limit hız | "Limit hızın bağlı olduğu değişkenlerin ilişkilerine yönelik yorumlamalarla sınırlı kalınır." | Yalnız kavram ve orantı yorumu (kesit alanı, şekil, kütle, ortam). Sayısal limit hız hesabı yok. Tipik örnekler: yağmur damlası, paraşütçü. |
| 11.1.9–10 Düzgün çembersel hareket | "Ray sisteminde çembersel hareketle ilgili matematiksel işlemlerden kaçınılır." Kapsam: yatay düzlem, düşey düzlem, yatay ve eğimli virajlar. | v = ωr, a = v²/r, F = mv²/r hesapları serbest. Açısal ivme yalnız anahtar kavram olarak geçiyor. Ray/lunapark rayı hesabı yok. |

**Programda olmayan (eski 11. sınıf konuları):** tork, denge, kütle merkezi, itme-momentum, açısal momentum → **12. sınıfa** taşındı (FİZ.12.1.x). İş-enerji → 10. ve 12. sınıf. Bağıl hareket ve hareketli referanstan atış yalnız **zenginleştirmede**.

## Ünite 2 — Elektrik ve Manyetizma

**Ön bilgi:** elektriklenme çeşitleri, elektroskop, mıknatıs kutupları, pusula (ortaokul fen). 10. sınıftan Ohm yasası, devreler (FİZ.10.3.x).

| Çıktı | MEB metni (sınır) | Yapay zekâ kuralı |
|---|---|---|
| 11.2.1 Coulomb yasası | "Coulomb Yasası ile ilgili farklı problem durumlarında **matematiksel hesaplamalara girmeden** uygulamalar yaparak matematiksel modeli geneller." | F = kq₁q₂/d² modelini **orantı ve yorum** düzeyinde kullan (d iki katına çıkarsa F dörtte birine iner vb.). Sayısal hesap sorusu üretme. |
| 11.2.2 Elektriksel alan | "**matematiksel hesaplara girmeden** elektriksel alanla ilgili farklı problem türleri" | Alan yönü, bileşke alan yönü, orantısal karşılaştırma. Sayısal hesap yok. |
| 11.2.3 Faraday kafesi | Bilgi toplama. | Kavramsal ve günlük hayat örnekleri (uçağa yıldırım düşmesi, asansörde sinyal kesilmesi, MR odası). |
| 11.2.4 Mıknatıs etkileşimi | Manyetik alan çizgileri, çizgi sıklığı ile büyüklük ilişkisi, Dünya'nın manyetik alanı. | Kavramsal. |
| 11.2.5 Düz telin manyetik alanı | "**matematiksel hesaplamalara girmeden** ulaştıkları matematiksel modelle ilgili problem çözümleri" Sağ el kuralı var. | B ∝ I/d orantısı ve sağ el kuralıyla yön. Sayısal hesap yok. |
| 11.2.6 Akım makarası | Akım, sarım sayısı, makara boyu ile B ilişkisi. Açık sınır cümlesi yok. | Orantı ve yön soruları güvenli. Sayısal hesap için dikkatli ol; ÖSYM'nin tavrı belli değil. |
| 11.2.7 Elektromıknatıs | Bilgi toplama. | Kavramsal. |
| 11.2.8 Tele etki eden manyetik kuvvet | F = BIL modeli, sağ el kuralı, "her bir değişkeni ayrı ayrı değiştirerek çözdüğü problemler". Açık hesap yasağı yok. | Yön ve orantı soruları temel; basit hesap mümkün. **Yüklü parçacığa etki eden kuvvet (qvB) programda açıkça yok.** |
| 11.2.9 Elektrik motoru | Dikdörtgen çerçevenin dönmesi, motorun çalışma ilkesi. | Kavramsal. |
| 11.2.10 Manyetik akı | Kavramsal açıklanır; B ve yüzey alanı ile ilişki. | Φ = B·A ilişkisi, açı etkisi ileri düzey. |
| 11.2.11 İndüksiyon gerilimi | Birim zamandaki akı değişimi → indüksiyon gerilimi modeli. | ε = −ΔΦ/Δt modeli ve yön (Lenz) soruları. |
| 11.2.12 Alternatif akım | Tel çerçevenin bir tam turunda akımın büyüklük ve yön değişimi, grafik yorumu. | Grafik ve kavram. Etkin değer, reaktans, rezonans **programda yok**. |
| 11.2.13 Transformatör | "Transformatörlerin nitelikleri arasındaki ilişkilere yönelik **yorumlamalarla sınırlı kalınır. Matematiksel işlemlerden kaçınılır.**" | Yalnız nitel ilişki (sarım sayısı ↔ gerilim/akım, yükseltici/düşürücü, iletimde kayıp). Sayısal trafo hesabı üretme. |

**Programda olmayan (eski 11. sınıf konuları):** elektriksel potansiyel, potansiyel enerji, iş, düzgün elektrik alanda yüklü parçacık hareketi, sığaçlar, öz-indüksiyon, AA devreleri (reaktans, empedans, rezonans).

## Ünite 3 — Optik (eski programda 10. sınıf / TYT konusuydu)

**Ön bilgi:** ışın, ışık, aydınlanma; düzlem ayna, küresel ayna, mercek sınıflaması; yansıma, kırılma, odak noktası (ortaokul fen).

| Çıktı | MEB metni (sınır) | Yapay zekâ kuralı |
|---|---|---|
| 11.3.1 Işık şiddeti, akı, aydınlanma | Tanım ve veri seti yorumu; lümen. | Tanımlar ve veri yorumu; E = I/d² orantısı. |
| 11.3.2 Düzlem ayna | Model oluşturma; yansıma ve görüntü kuralları. | Görüntü yeri, görüş alanı, ayna sistemleri (klasik soru tipleri). |
| 11.3.3–4 Küresel aynalar | Asal eksen, tepe, odak, merkez; özel ışınlar; cismin yerine göre görüntü. | Çizim ve görüntü özellikleri. Programda ayna denklemi (1/f = 1/d₀ + 1/dᵢ) açıkça adlandırılmamış; nitel çözüm öncelikli, formül ileri düzey. |
| 11.3.5 Kırılma | Kırma indisi, Snell yasası, sınır açısı, tam yansıma. | Snell hesabı ve tam yansıma koşulu serbest. |
| 11.3.6 Görünür derinlik | "Görünür derinliğe ilişkin **matematiksel model ve işlemlerden kaçınılır**." | Yalnız nitel (daha yakın ya da uzak görünür, kırma indisine bağlılık). h' = h·n₂/n₁ hesaplatma. |
| 11.3.7 Fiber optik | Bilgi toplama, tam yansıma ile çalışma. | Kavramsal. |
| 11.3.8 Prizmalar | Kırılma yasalarının prizmaya uygulanması, birleşik prizma sistemlerinde **tek renkli** ışığın yolu. | Işın izleme. Renklere ayrılma / tayf bu çıktıda değil (ışık renkleri 12. sınıfta, FİZ.12.3.6). |
| 11.3.9–10 Mercekler | Asal eksen, optik merkez, odak; yakınsak ve ıraksak mercekte görüntü. | Çizim ve görüntü özellikleri. Mercek denklemi ve gücü ileri düzey. |

**Zenginleştirme (sınav dışı sayılabilir):** paralel ortamlarda kayma miktarı, refraktometre, ayna-mercek bileşik sistemleri, teleskop ve mikroskop.

## Terim sözlüğü (eski → yeni)

| Eski kaynaklarda | Maarif programında |
|---|---|
| Serbest düşme / aşağı düşey atış / yukarı düşey atış | Hepsi **serbest düşme** (ilk hızı sıfır olan ya da olmayan) |
| Yatay atış, eğik atış | **İki boyutta sabit ivmeli hareket** |
| Kazanım | **Öğrenme çıktısı** |
| Ünite | **Tema** |

## Ölçme tarzı

MEB her çıktıda poster, rapor, çıkış kartı, açık uçlu test, yapılandırılmış grid ve performans görevi öneriyor. Çıktıların fiilleri (tümevarımsal akıl yürütme, kanıt kullanma, veri setinden çıkarım) sınav sorularının **veri tablosu, grafik, deney düzeneği ve bağlam** üzerinden kurulacağını gösteriyor. Soru üretirken yalnız işlem sorusu değil, veri yorumlama ve deney analizi soruları da üret.
