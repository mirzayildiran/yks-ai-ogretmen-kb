# Boşluk Analizi — 11. Sınıf Fizik

- **Güncelleme:** 2026-10-01
- **Durum:** STEP 1–7 tamamlandı. STEP 8 Ünite 1 için tamamlandı; Ünite 2–3 ve STEP 9–16 başlamadı.

## Missing curriculum data
- Yok. 3 ünite, 18 içerik başlığı, 33 çıktı ve 85 süreç bileşeni resmî PDF ile birebir.
- 2025 program sürümüyle (mufredat.meb.gov.tr) fark analizi yapılmadı.

## Missing learning outcomes
- Yok (33/33).
- Tüm çıktılarda yalnız `common_misconceptions` alanı boş; STEP 13'te dolacak.

## Missing concepts
- Sesli öğretmen alanları planlandı ama boş: `short/normal/deep_explanation`, `teacher_dialogue`, `common_student_question`.
- Kavram tanımları uzman incelemesinden geçmedi.
- Elektrik motorunun dönmesi tork kavramı kullanılmadan modellendi. Tork 12. sınıf konusu; kitapta da geçmiyor.

## Missing prerequisites
- **Ortaokul fen bilimleri programı toplanmadı.** Elektrik yükü, mıknatıs, ışık, yansıma, kırılma, odak gibi temel kabuller resmî kodsuz.
- **Matematik programı toplanmadı.** Trigonometri, oran-orantı ve ters kare ilişkisinin matematik programındaki yeri ve sınıfı doğrulanmadı.
- 16 çıktının 9–10. sınıf fizik çıktısına bağlantısı yok. Çoğu (Ünite 2'nin manyetizma kısmı, Ünite 3) ortaokul bilgisine dayanıyor.

## Missing formulas (STEP 7 — tamamlandı)
- 53 formül oluşturuldu; 48'i ders kitabının sayfa görüntüsünden doğrulandı, 53/53 boyut analizinden geçti (ayrıntı: `step-7-audit.md`).
- 3 türetilmiş formülün kitap sayfası doğrulanmadı: ilk hız bileşenleri, yatay virajda azami hız, sınır açısı formülü.
- 8 çıktı nitel olduğu için formülsüz: FİZ.11.2.3, 11.2.4, 11.2.7, 11.2.9, 11.3.4, 11.3.7, 11.3.8, 11.3.10.
- Ders kitabındaki çözümlü örneklerin tamamı taranmadı; az kullanılan ara bağıntılar eksik olabilir. Örnek: düşey çemberde enerji korunumu (s. 112), 10. sınıf mekanik enerji konusu.

## Missing question families / variations / solution methods / shortcuts (STEP 8, 9, 11, 12)
- **Ünite 1 tamamlandı:** 57 aile, 25/25 süreç bileşeni kapsanıyor (`step-8-unit1-audit.md`).
- **Ünite 2 (13 çıktı) ve Ünite 3 (10 çıktı):** soru ailesi yok.
- **Ünite 1'deki gerekçeli uyarıcı boşlukları:** 11.1.5 tablo, 11.1.6 grafik, 11.1.9 grafik, tablo ve deney.
- **Piyasa kanıtı (STEP 9) ve ÖSYM özellikleri (STEP 10):** boş.
- **Çözüm yöntemi ve kısa yol:** yalnız adlar var; ayrıntılar STEP 11–12'de.
- `legacy-taslak-fizik-11/` altında doğrulanmamış bir piyasa kaynakları envanteri (72 kayıt) ve kısmi bir FİZ.11.1.1 taslağı var. Yeni şemaya taşınmadılar.

## Missing error types / pedagogy (STEP 13, 14)
- Başlamadı.

## Missing sources
- MEB Çoktan Seçmeli Soru Yazım Kılavuzu indirildi ama işlenmedi (STEP 8 girdisi).
- Performans Gelişim Çerçevesi indirilemedi (sunucu 0 bayt döndürdü).
- ÖSYM çıkmış soruları ve 2028 YKS duyuruları kullanılmadı (STEP 10).
- Akademik kaynak (Tier 2) yok; kavram yanılgıları için gerekli (STEP 13).

## Conflicting sources
| Konu | Çelişki | Karar |
|---|---|---|
| 11. sınıf ünite sayısı | Tier 4 bloglar 4 ünite (Madde ve Doğası dahil) diyor | Tier 1: 3 ünite. Bloglar reddedildi. |
| İçerik başlığı adları | Web: "Newton Hareket Yasaları", "Çembersel Hareket" | PDF esas: "Newton'ın ...", "Düzgün Çembersel ...". |
| Kod | Web sayfasında "FİZ.11.4.10" | PDF: FİZ.11.3.10. |
| Kitap numaralandırması | 1.6 alt başlıkları "1.4.x" | 1.6.1 / 1.6.2 olarak kaydedildi. |
| Program ve ders kitabı (ikisi de Tier 1) | Program 6 çıktıda hesaplamayı dışlıyor, 1 çıktıyı kavramsal tutuyor; kitap bu 7 çıktıda 12 formül ve sayısal alıştırma veriyor | İkisi de kayıtlı: `program_calc_status` + `textbook_vs_program_conflict`. |
| Ders kitabı ve fizik | Tablo 1.2'de k "boyutsuz" | Boyut analiziyle reddedildi; doğru birim kg/m³. |
| Ders kitabı iç tutarlılığı | s. 116 eğimli viraj alt indisleri ters | Sonuç formülü doğru; not düşüldü. |

## Unverified claims
| İddia | Güven | Not |
|---|---|---|
| ÖSYM'nin 2028 YKS'de 11. sınıf fiziğini nasıl kapsayacağı | UNVERIFIED | Resmî duyuru aranmadı (STEP 10). |
| Kapsam sınırlarının sınav kapsamına etkisi ("CALC_EXCLUDED → ÖSYM sayısal sormaz") | UNVERIFIED | Program öğretimi sınırlar; ÖSYM'nin uyacağı varsayım. |
| Kavram tanımları ve 220 ilişki | MEDIUM | Yapay zekâ tarafından yazıldı; uzman incelemesi gerekli. |
| Etkin değer, Lenz, eğik düzlem, E = V/d, renklere ayrılma kapsamda mı? | MEDIUM | Ders kitabında var, programda adı geçmiyor. |
| Programın "hesaplamasız" dediği 12 formül için ÖSYM sayısal soru sorar mı? | UNVERIFIED | Kitap formülü ve sayısal alıştırmayı veriyor; program dışlıyor (STEP 10). |
