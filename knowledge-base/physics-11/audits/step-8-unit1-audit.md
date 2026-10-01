# Denetim — STEP 8 (Soru Ailesi Ontolojisi) · Ünite 1

- **Tarih:** 2026-10-01
- **Dosyalar:** `question-families/question-families.json`, `question-families.md`, `coverage.md`
- **Kaynak veri:** `scripts/data_question_families_u1.py`
- **Doğrulama:** `python3 scripts/run_all_audits.py` → ✓ 0 hata

## Yöntem

**1. Tasarım ilkeleri.** MEB *Bağlam Temelli Çoktan Seçmeli Soru Yazım Kılavuzu*ndan (Mart 2026, s. 16–24) alındı:
- Bağlam işlevsel olmalı: soru bağlam okunmadan çözülebiliyorsa bağlam işlevsizdir.
- Çeldiriciler kavram yanılgılarından seçilmeli.
- Aynı bağlamdaki sorular arasında ipucu zinciri olmamalı.
- "Hepsi" ve "hiçbiri" seçenekleri kullanılmamalı.
- Her soru bir süreç bileşenini ölçmeli. Kılavuz soruları "(FBAB8.SB1)" biçiminde etiketliyor; ailelerimiz de aynı kodlarla etiketli.

**2. Kanıt tabanı.** 11. sınıf ders kitabının Ünite 1 envanteri çıkarıldı (yalnız yapısal bilgi):
- yaklaşık 45 alıştırma
- 20 çözümlü örnek
- 40 ünite sonu ölçme sorusu

**3. Aile tanımı.** Bir soru ailesi şu üçünün birleşimidir: aynı fiziksel durum, aynı ölçülen süreç bileşeni ve aynı çözüm mantığı. Sayı, bağlam ve gösterim farkları aile değil varyasyondur.

**4. Otomatik doğrulama.**
- Her kitap kanıtında belirtilen anahtar kelime, o sayfanın metninde aranır.
- Her program alıntısı, ilgili çıktının resmî metninde aranır.
- Bütün referanslar (bileşen, kavram, formül) çözülmek zorundadır.

## Sonuçlar

| Ölçüt | Değer |
|---|---|
| Soru ailesi | 57: 55 çekirdek, 1 zenginleştirme, 1 hesap kapsam dışı |
| Süreç bileşeni kapsamı | 25/25 (Ünite 1'in tüm bileşenleri en az bir aileyle ölçülüyor) |
| Kitap kanıtı | 71/71 doğrulandı (anahtar kelime ilgili sayfada) |
| Program kanıtı | 19/19 doğrulandı |
| Zorluk | 5 kolay, 32 orta, 17 zor, 3 AYT-üstü (en yüksek uç) |
| Uyarıcı türleri | Günlük hayat 35, şekil 37, tablo 14, deney 11, grafik 8, veri seti 5 |

**Kapsam dışı işaretlenen iki aile:**
- **Hareketli referanstan açılı atış:** Programda zenginleştirme önerisi.
- **Ray sisteminde çembersel hareket:** Programda hesaplama açıkça dışlanmış ("matematiksel işlemlerden kaçınılır"). Eski kaynaklarda sık görüldüğü için tutuldu; yapay zekâ bu tür bir soruyu tanıyıp öğrenciye kapsam dışı olduğunu söyleyebilmeli.

## Gerekçeli boşluklar

| Çıktı | Eksik uyarıcı | Gerekçe |
|---|---|---|
| FİZ.11.1.5 | Tablo | Serbest cisim diyagramı çıktısı; tablo uyarıcısı doğal değil |
| FİZ.11.1.6 | Grafik | Nitel karşılaştırma; f–F grafiği FİZ.11.1.7'de |
| FİZ.11.1.9 | Grafik, tablo, deney | Hız yönü ve analoji çıktısı; tamamen nitel |

## Bilinçli olarak eklenmeyenler (bu aşamada)
- **Piyasa kanıtı** (STEP 9) ve **ÖSYM özellikleri** (STEP 10): Alanlar boş ve `pending` durumunda. "ÖSYM tarzı" etiketi kanıt olmadan verilmedi.
- **Çözüm yöntemleri ve kısa yollar:** Bu aşamada yalnız adlarıyla var; ayrıntılar STEP 11 ve 12'de.
- **Hata türleri:** Görev tanımındaki 14 kodla etiketlendi; tanımlar, teşhis soruları ve müdahaleler STEP 13'te.

## Güven
- Tüm aileler `MEDIUM` güvende ve uzman incelemesi bekliyor.
- Kanıtlar otomatik doğrulandı. Ancak çeldirici mantığı, zorluk tahmini ve aile sınırları bir fizik öğretmeninin değerlendirmesini gerektiriyor.
