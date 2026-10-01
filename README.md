# YKS Yapay Zekâ Öğretmen — Bilgi Tabanı

Hedef: 2028 YKS öğrencileri. İlk modül: **11. sınıf fizik (Türkiye Yüzyılı Maarif Modeli)**.

- Mimari: [docs/knowledge-base-architecture.md](docs/knowledge-base-architecture.md)
- Müfredat haritası: [knowledge-base/physics-11/curriculum/master-map.md](knowledge-base/physics-11/curriculum/master-map.md)
- Denetimler: [initial-audit](knowledge-base/physics-11/audits/initial-audit.md) · [step-4-6-audit](knowledge-base/physics-11/audits/step-4-6-audit.md) · [gap-analysis](knowledge-base/physics-11/audits/gap-analysis.md)

## Komutlar

```bash
python3 scripts/run_all_audits.py
```

Tüm katmanları resmî kaynaklardan baştan üretir ve doğrular; hata varsa çıkış kodu 1. Resmî PDF'ler depoda değildir; URL ve SHA-256 kayıtları `knowledge-base/physics-11/sources/sources.json` içindedir.

| Katman | Dosya |
|---|---|
| Müfredat | `knowledge-base/physics-11/curriculum/` |
| Öğrenme çıktıları, beceriler, kapsam sınırları | `knowledge-base/physics-11/learning-outcomes/` |
| Kavram grafiği | `knowledge-base/physics-11/concepts/` |
| Ön koşul grafiği | `knowledge-base/physics-11/prerequisites/` |
| Denetimler | `knowledge-base/physics-11/audits/` |

`legacy-taslak-fizik-11/` mimariden önce üretilmiş taslakları içerir; bilgi tabanının parçası değildir.
