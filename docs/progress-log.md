# İlerleme Kaydı

Otomatik devam görevinin ve ana oturumun nerede kalındığını bildiği tek kaynak. Her önemli adımdan sonra güncellenir.

## Durum (2026-10-02)

| Adım | Durum | Not |
|---|---|---|
| STEP 1–7 | ✅ commit'li | |
| STEP 8 Ünite 1 | ✅ commit'li | 57 aile |
| STEP 8 Ünite 2 | ✅ commit'li | 56 aile |
| STEP 8 Ünite 3 | ✅ commit'li | 65 aile. Toplam 178 aile, 85/85 süreç bileşeni, 392/392 kitap + 140/140 program kanıtı |
| STEP 10 ÖSYM | 🔄 alt ajan çalışıyor | Ajan `scripts/data_osym.py` yazıyor; doğrulama `build_osym.py --check`. Bitince derle ve commit'le. |
| STEP 13 Hata + yanılgı | 🔄 alt ajan çalışıyor | Ajan `scripts/data_errors.py` yazıyor; doğrulama `build_errors.py --check`. Bitince derle ve commit'le. |
| STEP 9, 11, 12, 14 | ⏳ dalga 2–3 | `docs/execution-plan.md` |
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
- Dalga 2 (Ünite 3 bitince): piyasa analizi + çözüm/kısa yol ajanları; önce `build_solutions.py` ve `build_market.py` yazılacak.
- GitHub: https://github.com/mirzayildiran/yks-ai-ogretmen-kb (herkese açık). `.git/hooks/post-commit` her commit'i otomatik gönderir; hata kaydı `.git/auto-push.log`. Commit yazarı GitHub noreply adresi (git config yerel).
