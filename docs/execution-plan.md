# Yürütme Planı — 11. Sınıf Fizik Bilgi Tabanı (STEP 8–16)

- **Sahibi:** Claude (kullanıcı 2026-10-02'de planlama ve alt ajan görevlendirmesini devretti)
- **İlke:**
  - Her katman önce bir veri dosyasına (`scripts/data_*.py`) yazılır.
  - Ardından bir derleyici + doğrulayıcı (`scripts/build_*.py`) ile JSON'a dönüştürülür.
  - Son olarak `run_all_audits.py`'ye eklenir.
  - Alt ajanlar yalnız kendi veri dosyalarına yazar; derleme, doğrulama ve commit ana oturumda yapılır.
- **Kural:** Eşzamanlı en fazla 3 alt ajan çalışır.

## Bağımlılıklar

```
STEP 8 (soru aileleri) ──┬──> STEP 11 çözüm yöntemleri ──> STEP 12 kısa yollar
                         ├──> STEP 9 piyasa analizi (aile eşleme)
                         └──> STEP 10 ÖSYM analizi (aile eşleme)
STEP 13 hata taksonomisi + kavram yanılgıları ──> STEP 14 pedagoji
Hepsi ──> STEP 15 QA ──> STEP 16 boşluk analizi
```

## Dalgalar

| Dalga | Alt ajan görevleri | Ana oturum |
|---|---|---|
| 1 | Ünite 3 soru ailelerini bitir (3.5–3.10) · ÖSYM yapısal analizi · Hata taksonomisi + kavram yanılgıları (Tier 2 akademik) | ÖSYM ve hata katmanlarının derleyici/doğrulayıcıları |
| 2 | Piyasa kaynak analizi · Çözüm yöntemleri + kısa yollar (Ünite 1 ve 2'ye birer ajan) | Piyasa ve çözüm katmanlarının derleyicileri, Ünite 3 aile derlemesi |
| 3 | Çözüm yöntemleri + kısa yollar (Ünite 3) · Pedagoji davranış modeli | Pedagoji derleyicisi, kavramlara yanılgı ve hata bağlantıları |
| 4 | — | STEP 15 kapsamlı QA, STEP 16 boşluk analizi, son rapor |

## Ajan sözleşmesi
- Yalnız kendi `scripts/data_*.py` dosyasına yaz; commit yapma.
- Dosyayı parça parça yaz (limit kesintisine karşı).
- Yalnız var olan slug ve kodları kullan (kavram, formül, aile, çıktı).
- Kaynak gösterilemeyen iddia yazma; okunamayan sayfayı okunmuş gibi gösterme.
- Telifli soru metni kopyalama; yalnız yapısal özet yaz.
- İş, verilen `--check` komutu HATA vermeden geçene kadar bitmiş sayılmaz.
