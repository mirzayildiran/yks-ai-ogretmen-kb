# Denetim — STEP 4–6 (Öğrenme çıktısı → Kavram → Ön koşul)

- **Tarih:** 2026-10-01
- **Müfredat sürümü:** `TYMM-FIZIK-OP-2026-08-19`
- **Yeniden üretme ve doğrulama:** `python3 scripts/run_all_audits.py` → ✓ tüm adımlar başarılı, 0 hata.

## STEP 4 — Öğrenme çıktısı veritabanı

| Eklenen | Kaynak | Sonuç |
|---|---|---|
| Beceri sözlüğü (`skills.json`) | TYMM Ortak Metin (EK-3 ve kavramsal beceriler) | 14 beceri; resmî tanım ve süreç bileşenleri. KB2.16 şemsiye beceri, kendi bileşeni yok. |
| Süreç bileşeni → beceri bileşeni | Ortak metin + program | **33/33 çıktıda** bileşen sayısı ve sırası becerinin resmî bileşenleriyle birebir örtüşüyor (ör. FİZ.11.1.9 a/b/c = KB2.16.3.SB1/SB2/SB3). |
| `measurable_behaviors` | Resmî süreç bileşenleri | 85 davranış; her biri beceri bileşeni koduna bağlı. |
| Ders kitabı bölümü | MEB 11. sınıf ders kitabı, içindekiler | 33/33; her başlık ilgili sayfada otomatik doğrulandı. Önceki denetimdeki 4 MEDIUM içerik başlığı eşlemesi **HIGH oldu**. |
| Kapsam sınırları (elle gözden geçirildi) | Öğretme uygulamaları | 15 çıktıda 28 madde ve 2 genel ilke. Türler: ASSUMPTION, TERMINOLOGY, SCOPE_INCLUDED, CALC_INCLUDED, CALC_LIMITED, CALC_EXCLUDED, CONCEPTUAL_ONLY. Her alıntı resmî metinde birebir doğrulandı; "implication" alanı bizim yorumumuz (MEDIUM). |
| `assessment_implications` | Öğretme uygulamaları | 31 resmî ölçme önerisi cümlesi. |

**Ders kitabında bulunan, programda adı geçmeyen içerik:**
- Eğik düzlem (s. 60, 82–83)
- Lenz Yasası (s. 247–262)
- Alternatif akımda etkin değer (s. 261–262)

**Ders kitabında hiç geçmeyenler:**
- Tork
- Ayna denklemi, mercek denklemi
- Düzlem aynalarda "görüntü sayısı" formülü

**Ders kitabı hatası:** 1.6 bölümünün alt başlıkları "1.4.1 / 1.4.2" diye numaralanmış.

**Telif:** Ders kitabında "Kitabın metin, soru ve şekilleri kısmen de olsa hiçbir surette alınıp yayımlanamaz" notu var. Kitaptan yalnız yapısal bilgi alındı: bölüm, sayfa, terim varlığı. Çıkarılan metin `.gitignore` ile depoya konmadı.

## STEP 5 — Kavram grafiği

| Ölçüt | Değer |
|---|---|
| Kavram | 137: 104 11. sınıf + 33 ön koşul (9. sınıf, 10. sınıf, ortaokul, matematik) |
| Resmî anahtar kavram eşlemesi | **36/36**, her biri tam bir kavrama |
| İlişki | 220: REQUIRES 154, PART_OF 24, RELATED_TO 15, SPECIAL_CASE_OF 14, USED_IN 9, CAUSES 4 |
| Kavram–çıktı bağlantısı | 247: 196 resmî metinde, 51 ders kitabı bölümünde kanıtlı, **0 kanıtsız** |
| REQUIRES döngüsü | Yok (negatif testle doğrulandı) |
| Yetim kavram | Yok |

**Güven:**
- 36 resmî anahtar kavram HIGH.
- Diğer kavramların listesi, tanımları ve 220 ilişkinin tamamı tarafımızdan yazıldı: MEDIUM, `ai_authored_pending_expert_review`. Bir fizik öğretmeninin incelemesi gerekiyor.

**Grafik sayesinde bulunup düzeltilen modelleme hataları:**
1. "Hava direnci" serbest düşme çıktılarına bağlanmıştı. Orada yalnızca ihmal edilen bir varsayım; bağlantı FİZ.11.1.8'e taşındı.
2. "Kinetik sürtünme REQUIRES sürtünme katsayısı" ilişkisi, programın nitelden (11.1.6) nicele (11.1.7) sırasıyla döngü oluşturuyordu. İlişki "katsayı USED_IN kinetik sürtünme" olarak değiştirildi.

## STEP 6 — Ön koşul grafiği

| Ölçüt | Değer |
|---|---|
| 9–10. sınıf resmî çıktı kataloğu | 46 (24 + 22; PDF süre tablosuyla aynı) |
| Ön koşul kavramı → önceki çıktı eşlemesi | 28: 18 resmî çıktı metninde (HIGH), 10 öğretme uygulamasında (MEDIUM) |
| 11. sınıf içi çıktı bağımlılığı | 42 kenar, kavram grafiğinden türetildi. Program sırasına ters kenar yok, döngü yok. |
| 9–10. sınıfa bağlanan 11. sınıf çıktısı | 17/33. Kalanlar ortaokul fen bilgisine (temel kabuller) ya da yalnız 11. sınıf içi ön koşullara dayanıyor. |
| Temel kabul ifadeleri | 3 ünitede 20 ifade; her biri resmî cümlede doğrulandı |

## Kalite kontrol özeti

| Kontrol | Sonuç |
|---|---|
| Müfredat: 3 ünite, 33 çıktı, 85 bileşen, PDF ile birebir | ✓ |
| Yinelenen ID (çıktı, kavram, ilişki, beceri, kaynak) | ✓ yok |
| Kırık referans (dosyalar arası) | ✓ yok |
| Yetim kavram / çıktı / içerik başlığı | ✓ yok |
| Döngü (REQUIRES, hiyerarşi, çıktı düzeyi) | ✓ yok |
| Kanıtsız kavram–çıktı bağlantısı | ✓ yok |
| Müfredat sürümü tutarlılığı (5 dosya) | ✓ |
| Kaynak dosya hash'leri | ✓ |
| Negatif testler | ✓ Doğrulayıcı; değiştirilmiş resmî metni, yinelenen ID'yi, kırık kaynağı, eksik bileşeni, yinelenen kavramı ve döngüyü yakaladı. |
