# Bilgi Tabanı Mimarisi

Hedef: 2028 YKS öğrencisinin müfredattaki konumunu, eksik kavram ve ön koşullarını, karşılaştığı soru ailesini ve yaptığı hatanın türünü belirleyip uygun pedagojik müdahaleyi seçebilen bir yapay zekâ öğretmenin bilgi çekirdeği.

Bu belge yapıyı ve kuralları tanımlar. İlk modül: **11. sınıf fizik**.

## Klasör yapısı

```
yks/
├── knowledge-base/
│   ├── schemas/                      Ortak JSON şemaları (tüm dersler)
│   └── physics-11/                   Ders + sınıf modülü
│       ├── curriculum/               curriculum.json (ünite, içerik başlığı), master-map.md
│       ├── learning-outcomes/        learning-outcomes.json
│       ├── concepts/                 STEP 5
│       ├── prerequisites/            STEP 6
│       ├── formulas/                 STEP 7
│       ├── question-families/        STEP 8
│       ├── question-patterns/        STEP 9
│       ├── osym-analysis/            STEP 10
│       ├── solution-methods/         STEP 11
│       ├── shortcuts/                STEP 12
│       ├── error-taxonomy/           STEP 13
│       ├── pedagogy/                 STEP 14
│       ├── sources/                  sources.json + raw/ (resmî ham dosyalar, SHA-256 ile)
│       └── audits/                   denetim ve boşluk analizi raporları
├── scripts/                          build_* (üretim), validate_* (doğrulama)
├── docs/
└── legacy-taslak-fizik-11/           Mimariden önceki taslaklar; bilgi tabanının parçası değil
```

**Düzen kararı:** Görev tanımında iki düzen vardı: `knowledge-base/<katman>/physics-11/` (madde 5) ve `knowledge-base/physics-11/<katman>/` (madde 29). İkincisi seçildi. Gerekçe: her ders-sınıf modülü kendi içinde bütün; yeni modül (ör. `math-11/`) eklemek ya da bir modülü ayrı sürümlemek tek klasör işi. Şemalar tüm modüller için ortak olduğundan `knowledge-base/schemas/` altında.

## Varlık zinciri

```
Ünite ─┬─ İçerik başlığı ─── Öğrenme çıktısı ─── Süreç bileşeni
       │                          │
       │                          ├── Beceri (FBAB / KB)
       │                          ├── Kavram ──(REQUIRES, PART_OF, ...)── Kavram
       │                          ├── Ön koşul (9–10. sınıf çıktıları, matematik)
       │                          └── Formül (geçerlilik + geçersizlik koşulları)
       │
Soru ailesi ── varyasyon ── çözüm yöntemi ── kısa yol (geçerlilik + başarısızlık durumları)
     │
     └── yaygın hata ── hata türü (taksonomi) ── teşhis sorusu ── pedagojik müdahale
```

Öğrenci modeli için her soru nesnesi şu kimlikleri taşıyacak: `learning_outcome_id`, `concept_id`, `question_family_id`, `skill_id`, `error_type_id`, `difficulty`. Böylece şu zincir kurulabilir: yanlış soru → hata türü → eksik beceri / kavram → öğrenme çıktısı → ön koşul.

## Kimlik (ID) kuralları

| Varlık | Biçim | Örnek |
|---|---|---|
| Ünite | `phys11-unit-<n>` | `phys11-unit-2` |
| İçerik başlığı | `phys11-topic-<ünite>-<n>` | `phys11-topic-1-6` |
| Öğrenme çıktısı | `phys11-lo-<nnn>` + **ayrıca** `official_code` | `phys11-lo-011` / `FİZ.11.2.1` |
| Süreç bileşeni | `<lo-id>-<harf>` | `phys11-lo-011-a` |
| Kaynak | `src-<kurum>-<kısa-ad>` | `src-meb-fizik-op-2026` |
| Sonraki varlıklar | `phys11-<tür>-<nnn>` | `phys11-concept-001`, `phys11-formula-001`, `phys11-qf-001` |

Resmî kodlar (FİZ.11.x.y, FBAB10, KB2.7) asla bizim ID'lerimizle değiştirilmez; ayrı alanda saklanır.

## Ortak alanlar

Her veri nesnesi şunları taşır:
- `id`
- `curriculum_version` (şu an `TYMM-FIZIK-OP-2026-08-19`)
- `sources`: kaynak ID'si ve o kaynağın hangi alanları desteklediği
- `confidence`: `HIGH` | `MEDIUM` | `LOW` | `UNVERIFIED`
- `created_at`, `updated_at`

Türetilmiş eşlemeler ayrıca `mapping_method` taşır: `official`, `derived_from_titles` ya da `explicit_in_outcome_text`.

**Resmî metin ve yorum ayrımı:** `official_*` ile başlayan alanlar resmî metni birebir taşır. Parafraz, özet ve yorumlar ayrı alanlara yazılır ve kendi güven seviyesini taşır.

## Kaynak hiyerarşisi

| Tier | Tür | Kural |
|---|---|---|
| 1 | MEB / ÖSYM resmî | Müfredat kararlarının tek dayanağı |
| 2 | Akademik / üniversite | Kavram yanılgıları ve pedagoji |
| 3 | Yayıncı / eğitim kurumu | Soru ailesi yapısı. Telifli metin kopyalanmaz. |
| 4 | Blog / forum | Hiçbir kritik kararın tek kaynağı olamaz |

Çelişen kaynaklar `sources.json` içinde `conflicting_rejected` durumuyla ve nedeniyle saklanır. Belirsizlik silinmez, veri olarak tutulur.

## Telif ilkesi

Yayınevi ve ÖSYM sorularının metni veri tabanına toplu olarak kopyalanmaz. Yalnız yapısal bilgi çıkarılır: soru ailesi, ölçülen beceri, zorluk, çeldirici mantığı, çözüm yaklaşımı. Örnek sorular özgün yazılır.

## Üretim ve doğrulama

- Veri, mümkün olduğunca **betikle ve resmî ham dosyadan** üretilir (`scripts/build_*.py`). Böylece MEB programı güncellendiğinde yeniden üretilebilir.
- `master-map.md` üretilen bir dosyadır; elle düzenlenmez.
- `scripts/validate_*.py` her çalıştırmada şunları kontrol eder:
  - JSON geçerliliği, yinelenen ID
  - kırık referans, sahipsiz kayıt
  - sürüm tutarlılığı, ham dosya hash'leri
  - resmî PDF ile birebir karşılaştırma
- Hata varsa çıkış kodu 1 olur.
- Her adımın sonunda `audits/` altına rapor yazılır.

## Sesli öğretmene hazırlık

STEP 5'te her kavram nesnesine şu alanlar eklenecek: `short_explanation`, `normal_explanation`, `deep_explanation`, `teacher_dialogue`, `common_student_question`. Bu aşamada ses teknolojisi geliştirilmeyecek.
