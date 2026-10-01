# İlk Denetim — 11. Sınıf Fizik (STEP 1–3)

- **Tarih:** 2026-10-01
- **Kapsam:** STEP 1 Repository audit · STEP 2 MEB/TYMM müfredat araştırması · STEP 3 Master curriculum map
- **Müfredat sürümü:** `TYMM-FIZIK-OP-2026-08-19`
- **Durum:** STEP 1–3 tamamlandı. STEP 4 ve sonrası **onay bekliyor**.

---

## 1. Repository denetimi (STEP 1)

### Başlangıç durumu

| Konu | Bulgu |
|---|---|
| Konum | `/Users/mirzayildiran/projeler/yks` |
| Sürüm kontrolü | **Git yok.** Değişiklik geçmişi tutulmuyor. |
| Paket / bağımlılık dosyası | Yok (`package.json`, `pyproject.toml`, `requirements.txt` yok). |
| Ortam | Python 3.9.6, `pypdf` 6.19.0. `jsonschema` kurulu değil. |
| Mevcut içerik | Önceki oturumda üretilmiş `fizik-11/` klasörü (aşağıda). |

### Önceki taslakların durumu (`legacy-taslak-fizik-11/`)

Bu klasör yeni mimariden önce üretildi. **Bilgi tabanının parçası değildir**; kaynak sistemi ve güven seviyesi yoktur.

| Dosya | İçerik | Değerlendirme |
|---|---|---|
| `mufredat/fizik11_ogretim_programi.json` | Web sayfalarından ayrıştırılmış müfredat | Yerini `learning-outcomes.json` aldı. |
| `kapsam-sinirlari.md` | Resmî sınırlar ve bizim yorumlarımız | Resmî alıntılar doğru; yorumlar doğrulanmamış. STEP 4'te gözden geçirilecek. |
| `ayt-analiz/ayt_fizik_dagilim_2018_2024.csv` | 2018–2024 AYT konu dağılımı | **Tier 4** blog verisi, ÖSYM'den doğrulanmadı. STEP 10'a kadar kullanılmamalı. |
| `kaynaklar/piyasa-kaynaklari.{md,csv}` | 72 piyasa kaynağı | Alt ajan çıktısı, kısmen doğrulanmış. "11. sınıfta Madde ve Doğası" hatası düzeltildi. STEP 9 girdisi. |
| `ciktilar/FIZ.11.1.1.md` | Soru tipleri ve örnekler taslağı | Durdurulan alt ajandan kalan kısmi taslak, doğrulanmadı. |
| `soru-tipleri/`, `pedagoji/` | Boş | — |

### Yapılan değişiklikler

- `knowledge-base/` yapısı kuruldu (bkz. `docs/knowledge-base-architecture.md`).
- Resmî ham kaynaklar taşındı (silme yok):
  - `fizik-11/kaynaklar/pdf/` → `knowledge-base/physics-11/sources/raw/pdf/`
  - `fizik-11/mufredat/meb-ham/` → `knowledge-base/physics-11/sources/raw/tymm-web/`
- Eski klasörün adı değişti: `fizik-11/` → `legacy-taslak-fizik-11/`.
- Boş `performans-gelisim-cercevesi.pdf` (0 bayt) silindi.
- `scripts/build_curriculum.py` ve `scripts/validate_curriculum.py` eklendi.

**Öneri:** `git init` ile sürüm kontrolüne başlanmalı (senin onayınla).

---

## 2. Müfredat araştırması (STEP 2)

### Kullanılan kaynaklar (tamamı Tier 1)

| ID | Kaynak | Rol |
|---|---|---|
| `src-meb-fizik-op-2026` | MEB TYMM Fizik Dersi Öğretim Programı PDF, 9–12, 19.08.2026, 104 sayfa | **Birincil**: ünite, saat, öğrenme çıktısı, süreç bileşeni, içerik çerçevesi, anahtar kavram |
| `src-tymm-fiz11-unite1..3` | tymm.meb.gov.tr ünite sayfaları, güncelleme 05.08.2026 | İkincil: öğretme uygulamaları, temel kabuller, ölçme, zenginleştirme, destekleme |
| `src-tymm-fiz11-index` | tymm.meb.gov.tr 11. sınıf sayfası | Ünite listesi teyidi |
| `src-tymm-fiz-other-grades` | 9, 10, 12. sınıf ünite sayfaları | Sınıflar arası bağlam, STEP 6 için toplandı |

### Yöntem

1. Ünite sayfalarının metni çekildi.
2. Resmî program PDF'i indirildi; 11. sınıf bölümü (s. 58–83) ayrıştırıldı.
3. Web ve PDF **birebir karşılaştırıldı**:
   - 33 öğrenme çıktısı ve 85 süreç bileşeninde **0 fark**.
   - Uzun anlatı metinleri cümle düzeyinde PDF'te arandı: **341/341 cümle** bulundu. Bunun için web sayfasındaki 6 yazım hatası PDF'teki doğru hâline göre düzeltildi.
4. Veri, tekrar üretilebilir betikle (`build_curriculum.py`) PDF'ten üretildi.

---

## 3. Bulgular (STEP 3 — master map)

| Ünite | Ders saati | İçerik başlığı | Öğrenme çıktısı | Süreç bileşeni | Anahtar kavram |
|---|---|---|---|---|---|
| 1. Kuvvet ve Hareket | 54 | 6 | 10 | 25 | 15 |
| 2. Elektrik ve Manyetizma | 48 | 4 | 13 | 34 | 9 |
| 3. Optik | 36 | 8 | 10 | 26 | 12 |
| Okul temelli planlama | 6 | — | — | — | — |
| **Toplam** | **144** | **18** | **33** | **85** | **36** |

Bu sayılar PDF'teki resmî "Ünite, öğrenme çıktısı sayısı ve süre tablosu" (s. 10) ile aynı: 10 + 13 + 10 = 33 çıktı, toplam 144 saat.

**Öğrenme çıktılarının beceri dağılımı** (beceri, çıktı metninde açıkça adlandırılıyor):

| Beceri | Kod | Çıktı sayısı |
|---|---|---|
| Tümevarımsal akıl yürütme | FBAB10 | 11 |
| Bilimsel çıkarım | FBAB8 | 4 |
| Karşılaştırma | KB2.7 | 3 |
| Bilgi toplama | KB2.6 | 3 |
| Deney yapma | FBAB7 | 3 |
| Bilimsel gözlem | FBAB1 | 2 |
| Diğer 7 beceri (FBAB9, FBAB11, FBAB12, KB2.4, KB2.14, KB2.15, KB2.16.3) | — | 1'er |

**Resmî kapsam sınırları:** 11 çıktıda toplam 17 sınır cümlesi var (ör. "matematiksel hesaplamalara girmeden", "kaçınılır", "sınırlı kalınır"). Bunlar her çıktının `official_scope_constraints` alanında **resmî metin olarak** saklanıyor.

**Zenginleştirme:** Her ünitede 3 paragraf var; 2'si "*" ile işaretli. Programa göre "*" işaretli uygulamalar fen liselerinde zorunlu ve ders kitabında yer almıyor.

**Programın genel ilkelerinden bilgi tabanına doğrudan etkisi olanlar:**
- Matematiksel hesaplama sınırlamalarına dikkat edilmesi (s. 7).
- Temel kabullerin bağlayıcı olması; ön değerlendirme ve köprü kurmanın öneri niteliğinde olması (s. 8).
- Zenginleştirmenin öğrenme çıktısı eklememesi (s. 9).
- Kavram yanılgılarının tespit edilip giderilmesi (s. 7).

---

## 4. Çelişkiler ve belirsizlikler

### Çözülen çelişkiler

| Konu | Çelişki | Karar |
|---|---|---|
| Ünite sayısı | Tier 4 bloglar (kitapsec, askakitap): 4 ünite, Madde ve Doğası dahil, saatler 46/46/10/36 | Tier 1 PDF ve web: **3 ünite, 54/48/36**. Madde ve Doğası 12. sınıfta (FİZ.12.4.x). Bloglar `conflicting_rejected`. |
| İçerik başlığı adları | Web: "Newton Hareket Yasaları", "Çembersel Hareket" | PDF (daha yeni): "Newton'ın Hareket Yasaları", "Düzgün Çembersel Hareket". **PDF esas.** |
| Kod yazım hatası | Web sayfası FİZ.11.3.10 uygulamasını "FİZ.11.4.10" başlığıyla veriyor | PDF'e göre FİZ.11.3.10. |
| Web yazım hataları | "vve", "TTasarladığı", "İİndüksiyon", "IIşığı", "ğretmen", "derle nen" | PDF'e göre düzeltildi, `build_curriculum.py` içinde listelendi. |

### Açık belirsizlikler

| # | Belirsizlik | Güven | Etki | Çözüm önerisi |
|---|---|---|---|---|
| 1 | Öğrenme çıktısı → içerik başlığı eşlemesi programda açıkça yok; başlık adlarından türetildi. 4 eşleme MEDIUM: FİZ.11.2.3 (Faraday kafesi), 11.2.7 (elektromıknatıs), 11.2.9 (elektrik motoru), 11.2.12 (alternatif akım). | MEDIUM | Düşük; çıktılar etkilenmez | Ders kitabının bölüm yapısıyla doğrula. |
| 2 | **Ders kitabı incelenmedi.** Alt başlıklar, verilen formüller ve terminoloji bilinmiyor. | — | **Yüksek**: STEP 7 (formüller) buna dayanmalı | Ders kitabından metin çıkarılacak (91 MB; ayrıştırma uzun sürüyor, önceki deneme senin isteğinle durduruldu). |
| 3 | Beceri kodlarının (FBAB, KB, E, SDB, D, OB) resmî tanımları alınmadı; fizik programı yalnız kod ve ad veriyor. | — | Orta: beceri ontolojisi için gerekli | `tymm-ortak-metin.pdf` incelenecek. |
| 4 | Kapsam sınırı cümleleri anahtar kelimeyle seçildi. Az sayıda yöntem cümlesi de girmiş olabilir (ör. FİZ.11.1.1'deki "hava direncinin ihmal edildiği..." cümlesi). Açık sınır içermeyen sınırlamalar kaçmış olabilir. | MEDIUM (seçim) | Orta | STEP 4'te 33 çıktı elle gözden geçirilecek. |
| 5 | 2025 (mufredat.meb.gov.tr) ve 2026 program sürümleri arasındaki fark analiz edilmedi. | — | Düşük | Gerekirse karşılaştırılacak. |
| 6 | ÖSYM'nin 2028 YKS'de 11. sınıf fiziğini nasıl kapsayacağı. Tier 4 kaynaklar "Temmuz 2026 itibarıyla açıklama yok" diyor; ÖSYM'nin kendisinden doğrulanmadı. | UNVERIFIED | Yüksek (uzun vade) | STEP 10'da ÖSYM resmî duyuruları taranacak. |
| 7 | Performans Gelişim Çerçevesi indirilemedi (0 bayt). | — | Düşük | Yeniden denenecek. |

Müfredat, öğrenme çıktısı, süreç bileşeni ve ünite saatlerinde **LOW veya UNVERIFIED veri yok**.

---

## 5. Kalite kontrol (`python3 scripts/validate_curriculum.py`)

**Sonuç: 24 kontrol geçti · 10 uyarı · 0 hata.**

| Kontrol | Sonuç |
|---|---|
| JSON geçerliliği (3 dosya) | ✓ |
| Yinelenen ID / resmî kod | ✓ Yok |
| Kod dizisi kesintisiz (1–10, 1–13, 1–10) | ✓ |
| Kırık referans (ünite, içerik başlığı, kaynak) | ✓ Yok |
| Sahipsiz öğrenme çıktısı / içerik başlığı | ✓ Yok |
| Müfredat sürümü tutarlılığı | ✓ |
| PDF ile ünite sayısı, saatler, anahtar kavramlar, içerik başlıkları | ✓ Aynı |
| PDF ile 33 çıktı metni + 85 süreç bileşeni | ✓ Birebir aynı |
| PDF'teki resmî tablo (33 çıktı, 144 saat) | ✓ Aynı |
| master-map.md'nin tüm kodları içermesi | ✓ |
| Kaynak dosya SHA-256 hash'leri | ✓ 7 dosya |
| Tier 4 kaynağın kritik veride kullanılmaması | ✓ |

**Negatif test:** Geçici bir kopyada 4 hata bilerek eklendi: resmî metin değişikliği, yinelenen ID, kırık kaynak, eksik süreç bileşeni. Doğrulayıcı 4'ünü de yakaladı ve çıkış kodu 1 döndü.

**Uyarılar:**
- 4 MEDIUM içerik başlığı eşlemesi (yukarıda 1. madde).
- Sonraki adımların alanları henüz boş: `concepts`, `prerequisites`, `mathematical_prerequisites`, `measurable_behaviors`, `common_misconceptions`, `assessment_implications`.
- 5 kaynak henüz işlenmedi: ders kitabı, ortak metin, soru yazım kılavuzu, performans gelişim çerçevesi, 2025 program sürümü.

---

## 6. Sonraki adım (onay bekliyor)

STEP 4–6: Learning Outcome → Concept → Prerequisite. Önerilen sıra:

1. Ders kitabını ve ortak metni işle (belirsizlik 2 ve 3).
2. 33 çıktının kapsam sınırlarını elle gözden geçir (belirsizlik 4).
3. Kavram grafiği: resmî 36 anahtar kavramdan başlayarak.
4. Ön koşul grafiği: temel kabuller ve 9–10. sınıf çıktılarına bağlantılar.
