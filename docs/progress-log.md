# İlerleme Kaydı

Otomatik devam görevinin ve ana oturumun nerede kalındığını bildiği tek kaynak. Her önemli adımdan sonra güncellenir.

## Durum (2026-10-02)

| Adım | Durum | Not |
|---|---|---|
| STEP 1–7 | ✅ commit'li | |
| STEP 8 Ünite 1 | ✅ commit'li | 57 aile |
| STEP 8 Ünite 2 | ✅ commit'li | 56 aile |
| STEP 8 Ünite 3 | ✅ commit'li | 65 aile. Toplam 178 aile, 85/85 süreç bileşeni, 392/392 kitap + 140/140 program kanıtı |
| STEP 10 ÖSYM | ✅ commit'li | AYT 2018–2025 (112) + TYT 2018–2025 optik ve 11. sınıfa denk gelenler (20); 132 soru, hepsi resmî kitapçıktan. `run_all_audits.py`'ye eklendi |
| STEP 13 Hata + yanılgı | 🔄 parça parça | ✅ 17 hata türü, Ünite 1 (35), Ünite 2'nin 2.1–2.11'i (28) · 🔄 ajan 2.12–2.13 + Ünite 3 · Doğrulama `build_errors.py --check` |
| STEP 11–12 Çözüm + kısa yol | 🔄 parça parça | ✅ Ünite 1 (55 çözüm, 33 kısa yol) · 🔄 ajan Ünite 2 (46/56 var; 3 hata düzeltiliyor, kısa yollar yazılıyor) · ⏳ Ünite 3 |
| STEP 9 Piyasa | 🔄 | 5 kaynak commit'li · 🔄 ajan 20–30 kaynak daha |
| STEP 14 Pedagoji | ✅ commit'li | 9 protokol, ipucu merdiveni, 17 müdahale (`build_pedagogy.py`) |
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
- macOS'ta `timeout` komutu yok; doğrulama kodları `build_solutions.py` içinde 20 sn sınırlı alt süreçte çalışır.
