# İlerleme Kaydı

Otomatik devam görevinin ve ana oturumun nerede kalındığını bildiği tek kaynak. Her önemli adımdan sonra güncellenir.

## Durum (2026-10-02)

| Adım | Durum | Not |
|---|---|---|
| STEP 1–7 | ✅ commit'li | |
| STEP 8 Ünite 1 | ✅ commit'li | 57 aile |
| STEP 8 Ünite 2 | ✅ commit'li | 56 aile |
| STEP 8 Ünite 3 | ✅ commit'li | 65 aile. Toplam 178 aile, 85/85 süreç bileşeni, 392/392 kitap + 140/140 program kanıtı |
| STEP 10 ÖSYM | 🔄 parça parça | ✅ AYT 2018–2019 (28 soru, resmî PDF) commit'li · 🔄 ajan AYT 2020–2022 · ⏳ AYT 2023–2025 · ⏳ TYT 2018–2025 optik. Doğrulama `build_osym.py --check` |
| STEP 13 Hata + yanılgı | 🔄 parça parça | ✅ 17 hata türü commit'li · 🔄 ajan Ünite 1 yanılgıları · ⏳ Ünite 2 · ⏳ Ünite 3. Doğrulama `build_errors.py --check` |
| STEP 11–12 Çözüm + kısa yol | 🔄 parça parça | Derleyici `build_solutions.py` hazır · 🔄 ajan Ünite 1 (`data_solutions_u1.py`) · ⏳ Ünite 2 · ⏳ Ünite 3 |
| STEP 9 Piyasa, STEP 14 Pedagoji | ⏳ | Derleyicileri yazılacak (`build_market.py`, `build_pedagogy.py`) |
| STEP 15–16 | ⏳ dalga 4 | |

## Devam protokolü
1. `git status` ve `git log` ile durumu gör.
2. Bu tablodaki 🔄 satırın veri dosyasını `--check` ile doğrula.
   - Eksikse: o satırın görevini yeni bir alt ajanla sürdür.
   - Tamamsa: derle, `run_all_audits.py` çalıştır ve commit'le.
3. Bir sonraki ⏳ satıra geç (`docs/execution-plan.md`).
4. Bu tabloyu güncelle.

## Notlar
- Otomatik devam görevi: bu oturumda her saat :17'de çalışır, oturum kapanınca ya da 7 gün sonra biter.
- Derleyiciler hazır: `build_osym.py`, `build_errors.py` (ortak: `kb_common.py`). `run_all_audits.py`'ye ancak veri dosyaları tamamlanınca eklenecekler.
- Limit kesintileri sık: ajan görevleri küçük parçalara bölündü (yıl grupları, üniteler). Yarım kalan dosya `--check`'ten geçiyorsa önce commit'le, sonra kalan parçayı yeni ajana ver.
- Tüm katmanlar bitince `run_all_audits.py`'ye `build_osym`, `build_errors`, `build_solutions` eklenecek.
- GitHub: https://github.com/mirzayildiran/yks-ai-ogretmen-kb (herkese açık). `.git/hooks/post-commit` her commit'i otomatik gönderir; hata kaydı `.git/auto-push.log`. Commit yazarı GitHub noreply adresi (git config yerel).
