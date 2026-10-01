# YKS Yapay Zekâ Öğretmen — Bilgi Tabanı

Hedef: 2028 YKS öğrencileri. İlk modül: **11. sınıf fizik (Türkiye Yüzyılı Maarif Modeli)**.

- Mimari: [docs/knowledge-base-architecture.md](docs/knowledge-base-architecture.md)
- Müfredat haritası: [knowledge-base/physics-11/curriculum/master-map.md](knowledge-base/physics-11/curriculum/master-map.md)
- Son denetim: [knowledge-base/physics-11/audits/initial-audit.md](knowledge-base/physics-11/audits/initial-audit.md)

## Komutlar

```bash
python3 scripts/build_curriculum.py      # müfredat verisini resmî PDF'ten yeniden üretir
python3 scripts/validate_curriculum.py   # doğrular; hata varsa çıkış kodu 1
```

`legacy-taslak-fizik-11/` mimariden önce üretilmiş taslakları içerir; bilgi tabanının parçası değildir.
