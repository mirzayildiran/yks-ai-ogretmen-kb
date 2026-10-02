"""STEP 11–12 — Ünite 2 (Elektrik ve Manyetizma): soru ailesi çözüm yöntemleri ve kısa yolları.

Her ailede: standard (normal çözüm), conceptual (fiziksel mantık), fast (sınav hızı) ve alternative (ikinci yol).
Çözümlü örnekler özgündür; `python_check` cevabı bağımsız bir yolla (sayısal integral, elle çapraz çarpım,
Biot–Savart toplamı, simülasyon, farklı formül) doğrular.

KAPSAM KURALI: FİZ.11.2.1 (Coulomb), 11.2.2 (elektrik alan), 11.2.5 (düz tel), 11.2.13 (transformatör) programda
hesaplamasız; 11.2.10 (akı) kavramsal. Bu ailelerde `standard` yöntem oran / yön / yorum / veri tablosundan orantıdır.
Kitabın verdiği formülle sayısal yol yalnız `alternative` yöntemdedir ve `limits` alanında
"program hesaplamayı dışlar; kitapta var" notunu taşır.
Sabitler: g = 10 m/s²; k = 9·10⁹ N·m²/C²; K = 10⁻⁷ T·m/A (kitap gösterimi); ϑ = hız, i = akım.
Sağ el kuralı yönleri elle çapraz çarpımla (numpy yok) doğrulanır; Lenz yönü Biot–Savart toplamıyla sınanır.
"""


def M(steps, validity, limits, risks):
    return {"steps": steps, "validity": validity, "limits": limits, "risks": risks}


def S(standard, conceptual, fast, alternative, insight, problem, steps, answer, check):
    return {"standard": standard, "conceptual": conceptual, "fast": fast, "alternative": alternative,
            "expert_insight": insight,
            "worked_example": {"problem": problem, "steps": steps, "answer": answer, "python_check": check}}


def SC(slug, name, fams, shortcut, why, validity, failure, risk, sources, check):
    return {"slug": slug, "name": name, "question_families": fams, "shortcut": shortcut, "why_it_works": why,
            "validity_conditions": validity, "failure_cases": failure, "risk_level": risk,
            "sources": sources, "numeric_check": check}


TB = lambda ref: {"type": "textbook", "ref": ref}
DV = lambda ref: {"type": "derivation", "ref": ref}
PR = lambda ref: {"type": "program", "ref": ref}

# Doğrulama kodlarında kullanılan elle vektör işlemleri (numpy yok); kod dizgelerinin başına eklenir.
VEC = """
def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
def add(a, b):
    return tuple(x + y for x, y in zip(a, b))
def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))
def mul(k, a):
    return tuple(k * x for x in a)
def norm(a):
    return dot(a, a) ** 0.5
def close(a, b, tol=1e-9):
    return all(abs(x - y) < tol for x, y in zip(a, b))
def biot(path, P, I=1.0):
    # Biot-Savart toplami: B ~ I * sum( dl x (P - r) / |P - r|^3 ), mu0/4pi atildi (yalniz yon/oran)
    B = (0.0, 0.0, 0.0)
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        dl = sub(b, a)
        mid = mul(0.5, add(a, b))
        r = sub(P, mid)
        B = add(B, mul(I / norm(r) ** 3, cross(dl, r)))
    return B
import math
def circle(R, n=720, z=0.0, ccw=True):
    s = 1 if ccw else -1
    return [(R * math.cos(s * 2 * math.pi * i / n), R * math.sin(s * 2 * math.pi * i / n), z) for i in range(n + 1)]
def line(p0, p1, n=4000):
    return [tuple(p0[k] + (p1[k] - p0[k]) * i / n for k in range(3)) for i in range(n + 1)]
"""

SOLUTIONS = {}
SHORTCUTS = []

# ============================ FİZ.11.2.1 — Coulomb (hesaplamasız: oran / yön / yorum) ============================
SOLUTIONS["coulomb-data-table-graph"] = S(
    M(["Tablodan YALNIZ bir değişkenin değiştiği iki satır seç (diğerleri sabit olmalı); kontrol değişkeni ilkesi.",
       "O değişkenin çarpanını yaz (örn. q₁ 2 katına çıktı) ve F'nin çarpanını oku (F 2 katına çıktı → doğru orantı).",
       "Uzaklık değişen satırlarda: d 2 katında F 1/4, d 3 katında F 1/9 ise F ∝ 1/d² (ters kare).",
       "Eksik hücreyi, referans satırdan çarpanları zincirleyerek doldur (q₁ ×3, d ×2 → F ×3/4).",
       "Grafik: F–q orijinden geçen doğru, F–d azalan eğri, F–(1/d²) orijinden geçen doğru."],
      ["Karşılaştırılan satırlarda diğer nicelikler sabit", "Noktasal yükler, aynı ortam"],
      ["Program formül kullandırmaz; ilişki veri örüntüsünden çıkarılır", "İki değişken birlikte değiştiyse çarpanlar ayrı ayrı çarpılır"],
      ["İki değişkenin birlikte değiştiği satırlardan tek değişkenin etkisini okumak", "F–d eğrisini doğrusal orantı sanmak", "Ters kareyi ters orantı sanmak"]),
    M(["Kuvvet iki yükün her birinin 'kaynak' olması nedeniyle q₁·q₂ ile orantılıdır: biri iki katına çıkınca kuvvet iki katına çıkar.",
       "Etki uzaklık arttıkça yüzeye yayılır; yüzey d² ile büyüdüğü için etki 1/d² ile azalır.",
       "Bu yüzden F·d² / (q₁q₂) tüm satırlarda aynı çıkar; tablo bu 'sabit'in sınanmasıdır."],
      ["Noktasal (ya da küresel simetrik) yükler"], ["Yüklü cisimler birbirine çok yakınsa (boyut etkili) örüntü bozulur"], ["Toplamsal sanmak"]),
    M(["Her satırda F·d²/(q₁·q₂) hesapla; sabit çıkıyorsa model doğru, eksik hücreyi bu sabitle tamamla.",
       "Hızlı oran: q'lar çarpılır, d² bölünür."],
      ["Tüm satırlarda aynı ortam"], ["Sabit çıkmayan satır varsa o satır hatalı ölçümdür ya da başka değişken değişmiştir"], ["Birimleri (nC, cm) karıştırmak"]),
    M(["Kitap modeliyle: F = k·q₁·q₂/d², değerleri SI'ye çevirip yerine koy ve tabloyla karşılaştır."],
      ["Noktasal yükler, boşluk/hava"],
      ["Program hesaplamayı dışlar; kitapta var (kitap Coulomb Yasası s.160)"], ["nC → 10⁻⁹ C, cm → 10⁻² m dönüşümlerini unutmak"]),
    "Tabloda 'tek değişkenli satır çifti' bul. Yük çarpanı doğrudan, uzaklık çarpanı ters kare. 'Hangi grafik doğrusal?' sorusunun cevabı F–q ve F–(1/d²).",
    "Bir simülasyonda iki noktasal yük arasındaki kuvvet ölçülüyor: (q₁=2 nC, q₂=3 nC, d=3 cm) için F=60 µN; (4, 3, 3 cm) için 120 µN; (2, 6, 3 cm) için 120 µN; (2, 3, 6 cm) için 15 µN. Aynı simülasyonda q₁=6 nC, q₂=3 nC, d=6 cm iken kuvvet kaç µN okunur? Bu veri F–d ilişkisi hakkında ne söyler?",
    ["1. ve 2. satır: yalnız q₁ 2 katına çıkmış, F 2 katına çıkmış → F ∝ q₁. 1. ve 3.: q₂ için aynı → F ∝ q₂.",
     "1. ve 4. satır: yalnız d 2 katına çıkmış, F 60 → 15 (1/4) → F ∝ 1/d² (ters kare).",
     "Hedef satır: q₁ ×3, d ×2 → F = 60 × 3 × (1/4) = 45 µN.", "Kontrol: F·d²/(q₁q₂) tüm satırlarda sabit."],
    "45 µN; kuvvet uzaklığın karesiyle ters orantılıdır (F–d eğri, F–1/d² doğru).",
    """
import math
rows = [(2, 3, 3, 60.0), (4, 3, 3, 120.0), (2, 6, 3, 120.0), (2, 3, 6, 15.0)]
# kontrol değişkeni: tek değişkenli satır çiftlerinden üs bulma
p_q1 = math.log(rows[1][3] / rows[0][3]) / math.log(rows[1][0] / rows[0][0])
p_q2 = math.log(rows[2][3] / rows[0][3]) / math.log(rows[2][1] / rows[0][1])
p_d = math.log(rows[3][3] / rows[0][3]) / math.log(rows[3][2] / rows[0][2])
assert abs(p_q1 - 1) < 1e-9 and abs(p_q2 - 1) < 1e-9 and abs(p_d + 2) < 1e-9
c = [F * d * d / (a * b) for a, b, d, F in rows]
assert all(abs(x - c[0]) < 1e-9 for x in c)
target = c[0] * 6 * 3 / 6 ** 2
assert abs(target - 45.0) < 1e-9
# bağımsız yol: kitap formülü (SI) ile aynı sonuç
k = 9e9
F_si = k * (6e-9) * (3e-9) / (0.06 ** 2)
assert abs(F_si * 1e6 - 45.0) < 1e-6
# hatalı yöntem: iki değişkenin birlikte değiştiği satırlardan (1. ve 4.'ü q ile karıştırmak) üs çıkarmak yanlıştır
bad = math.log(rows[3][3] / rows[1][3]) / math.log(rows[3][0] / rows[1][0])
assert abs(bad - 1) > 0.5
""")

SOLUTIONS["coulomb-ratio-generalization"] = S(
    M(["Referans durumu F = (q₁·q₂·k)/d² ile 'çarpan çarpımı' olarak düşün: F ∝ q₁ · q₂ · k · (1/d²).",
       "Her değişimin çarpanını ayrı yaz: q₁ ×a, q₂ ×b, k ×c, d ×e.",
       "Yeni kuvvet = F · a · b · c / e².",
       "Ortam değişince yükler değil Coulomb sabiti k değişir (örn. su: k ≈ 1/80).",
       "Çok durumlu tabloda her satırı aynı biçimde hesapla ve sırala."],
      ["Noktasal yükler", "Çarpanlar referansa göre verilmiş"],
      ["Program hesaplamayı değil oranı ister; sayı yerine 'kaç F' yaz", "Yükler temas edip paylaşırsa q değişir (çarpan bu durumda yük paylaşımından gelir)"],
      ["Çarpanları toplamak", "d çarpanını karesiz almak", "Ortam değişince yükü değişmiş sanmak"]),
    M(["Kuvvet yüklerin çarpımıyla büyür: bir yük iki katına çıkınca kuvvet iki katına çıkar, ikisi birlikte dört katına.",
       "Uzaklık iki katına çıkınca etki dört kat seyrelir.", "Yük işareti kuvvetin yönünü belirler, büyüklüğünü değil."],
      ["Aynı ortam"], ["Sıralama sorularında yalnız büyüklük sıralanır"], ["Yön ile büyüklüğü karıştırmak"]),
    M(["Önce uzaklığın karesini al: d ×2 → ÷4, d ×3 → ÷9, d ×1/2 → ×4. Sonra yüklerin çarpımını ekle."],
      ["Her çarpan referansa göre"], ["Çarpanı tek adımda yazarken hesap hatası riski"], ["Karesiz uzaklık"]),
    M(["Sayısal ikinci yol: referans değerlerle F = k·q₁·q₂/d² hesapla, yeni değerlerle yeniden hesapla, oranı al."],
      ["Noktasal yükler"], ["Program hesaplamayı dışlar; kitapta var (s.159 14. adım tablosu, s.160 formül)"], ["Birim dönüşümü hatası"]),
    "'Kaç F olur?' → çarpan yöntemi: yük çarpanlarını çarp, uzaklık çarpanının karesine böl, ortam çarpanını (k) ekle. 'd iki katına çıkınca yarıya iner' seçeneği hep tuzaktır.",
    "İki noktasal yük arasındaki kuvvet F'dir. (a) q₁ 2 katına ve d 2 katına çıkarılırsa, (b) d yarıya indirilip q₂ 3 katına çıkarılırsa, (c) sistem k'si havadakinin 1/80'i olan suya daldırılırsa kuvvet kaç F olur?",
    ["(a) 2 · 1 / 2² = 1/2 → F/2.", "(b) 3 · 1 / (1/2)² = 12 → 12F.", "(c) Yükler ve d aynı; yalnız k çarpanı 1/80 → F/80."],
    "(a) F/2, (b) 12F, (c) F/80.",
    """
import random
k0, q1, q2, d = 9e9, 3e-9, 5e-9, 0.04
F = lambda k, a, b, r: k * a * b / r ** 2
F0 = F(k0, q1, q2, d)
assert abs(F(k0, 2 * q1, q2, 2 * d) / F0 - 0.5) < 1e-12
assert abs(F(k0, q1, 3 * q2, d / 2) / F0 - 12) < 1e-9
assert abs(F(k0 / 80, q1, q2, d) / F0 - 1 / 80) < 1e-12
# rastgele çarpanlarla çarpan yöntemi = tam hesap
random.seed(3)
for _ in range(200):
    a, b, c, e = [random.uniform(0.2, 5) for _ in range(4)]
    assert abs(F(k0 * c, a * q1, b * q2, e * d) / F0 - a * b * c / e ** 2) < 1e-9
# hatalı yöntemler: çarpanları toplamak ya da d çarpanını karesiz almak farklı (yanlış) sonuç verir
assert abs(F(k0, 2 * q1, 3 * q2, d) / F0 - 6) < 1e-12 and (2 + 3) != 6          # toplamsal sanmak: 5 ≠ 6
assert abs(F(k0, q1, q2, 2 * d) / F0 - 0.25) < 1e-12 and abs(F(k0, q1, q2, 2 * d) / F0 - 0.5) > 0.2   # 1/2 değil 1/4
""")

SOLUTIONS["coulomb-direction-newton3"] = S(
    M(["Yük işaretlerine bak: aynı cins → itme, zıt cins → çekme.",
       "Her yük için kuvvetin yönünü diğer yüke göre çiz (itmede uzağa, çekmede yüke doğru).",
       "Etki–tepki: iki yük birbirine EŞİT büyüklükte, ZIT yönlü kuvvet uygular; yük büyüklükleri farklı olsa da.",
       "Hareket yönünü sorulan yüke etki eden kuvvetten bul; ivme için kütleye bak."],
      ["Noktasal yükler", "Yüklerin temas etmesi gerekmez (alan kuvveti)"],
      ["Hesap yok; yön ve büyüklük karşılaştırması", "Üç yükte her yüke gelen kuvvetler ayrı çizilip toplanır"],
      ["Büyük yükün daha büyük kuvvet uyguladığını sanmak", "Yönü yük büyüklüğüne bakarak çizmek", "Temas yok diye kuvvet yok sanmak"]),
    M(["Kuvvet iki yükün ortak etkileşimidir; hangisi 'uyguluyor' diye ayrım yoktur, ikisi de uygular ve maruz kalır.",
       "Büyük yük büyük alan oluşturur ama küçük yükün oluşturduğu alan büyük yüke aynı büyüklükte kuvvet uygular (q₁q₂ simetrik).",
       "Poleni çeken iki arı örneği: zıt yükler çeker."],
      ["Elektriksel etkileşim"], ["Nitel"], ["Kuvvetin tek yönlü olduğunu düşünmek"]),
    M(["İşaret çarpımına bak: (+)(+) ve (−)(−) → itme; (+)(−) → çekme. Büyüklükler her zaman eşit: seçeneklerde 'büyük yük daha büyük kuvvet uygular' varsa ele."],
      ["İki yüklü cisim"], ["Üç yükte net kuvvet için ayrıca topla"], ["Net kuvvetle ikili kuvveti karıştırmak"]),
    None,
    "'Hangi yük hangisine daha büyük kuvvet uygular?' → eşit (Newton 3). Yön için yalnız işaret: aynı iter, zıt çeker. Net kuvvet sorusu varsa her çifti ayrı çiz.",
    "A cismi +3q, B cismi −q yüklüdür ve x ekseninde A x=0, B x=2d konumundadır. Sağ tarafta x=4d'de +q yüklü C bulunuyor. A'nın B'ye uyguladığı ile B'nin A'ya uyguladığı kuvvetin büyüklüğünü karşılaştırınız; B'ye etki eden net kuvvetin yönünü bulunuz.",
    ["A ile B zıt işaretli → çekim: B, A'ya doğru (−x) çekilir; A da B'ye doğru (+x) çekilir. Büyüklükler eşit (Newton 3).",
     "C (+q) ile B (−q) zıt işaretli → B, C'ye doğru (+x) çekilir.",
     "B'ye gelen iki kuvvette uzaklık aynı (2d); büyüklük yük çarpımıyla orantılı: A için 3q·q, C için q·q → A'nın çekimi 3 kat büyük.",
     "Net kuvvet −x yönünde (A'ya doğru)."],
    "Karşılıklı kuvvetler eşit büyüklükte ve zıt yönlüdür. B'ye etki eden net kuvvet −x yönünde (A'ya doğru) ve C'nin uyguladığı kuvvetin (3 − 1) = 2 katı büyüklüktedir.",
    """
k = 1.0
def force_on(i, charges, pos):
    # Coulomb vektörü: F_i = sum_j k qi qj (xi - xj)/|xi - xj|^3  (pozitif = itme yönü)
    f = 0.0
    for j in range(len(charges)):
        if j != i:
            r = pos[i] - pos[j]
            f += k * charges[i] * charges[j] * r / abs(r) ** 3
    return f
q = [3.0, -1.0, 1.0]
x = [0.0, 2.0, 4.0]
two = [q[0], q[1]]
fa = force_on(0, two, x[:2]); fb = force_on(1, two, x[:2])
assert fa > 0 and fb < 0 and abs(fa + fb) < 1e-12 and abs(abs(fa) - abs(fb)) < 1e-12   # çekim, eşit ve zıt
fnet_B = force_on(1, q, x)
assert fnet_B < 0                                     # A'ya doğru
fromA = k * 3 * 1 / 2 ** 2; fromC = k * 1 * 1 / 2 ** 2
assert abs(abs(fnet_B) - (fromA - fromC)) < 1e-12 and abs(fromA / fromC - 3) < 1e-12
# Newton 3 üç yükte: ikili kuvvetlerin toplamı sıfır
assert abs(sum(force_on(i, q, x) for i in range(3))) < 1e-12
""")

SOLUTIONS["coulomb-collinear-net-force"] = S(
    M(["Bir yük seç; diğer her yükün ona uyguladığı kuvvetin yönünü (itme/çekme) çiz.",
       "Büyüklüğü F cinsinden yaz: referans F = k·q²/d² ise çarpan = (yük çarpımı)/(uzaklık çarpanı)². Örn. 2q ile q arası 2d: 2/4 F = F/2.",
       "Yönü işaretle (sağ +, sol −) ve işaretli topla.",
       "Denge sorusunda: iki kuvvetin büyüklükleri eşit, yönleri zıt olsun; yük oranı ve uzaklık oranı birlikte kurulur.",
       "Kontrol: yalıtılmış sistemde tüm net kuvvetlerin toplamı sıfırdır (etki–tepki)."],
      ["Noktasal yükler aynı doğru üzerinde", "Kuvvetler vektörel (aynı doğru: işaretli) toplanır"],
      ["Program: oran/F cinsinden ifade; sayısal 'kaç N' kitapta ÖD-3'te var ama programda dışlanır", "Eğer yükler aynı doğru üzerinde değilse vektör bileşenleri gerekir"],
      ["Büyüklükleri işaretsiz toplamak", "Uzaklığı karesiz almak (1/d)", "Birden fazla yükün kuvvetini ayrı yük için hesaplamak yerine tek yüke bakmak"]),
    M(["Her yük, diğerlerinin kuvvetlerini bağımsız olarak hisseder (süperpozisyon).",
       "Zıt yönlü kuvvetler birbirini götürür; yakın yük genellikle baskındır (1/d²).",
       "Denge noktası, iki itme (ya da çekme) kuvvetinin eşitlendiği yerdir: büyük yükten uzakta, küçük yüke yakın."],
      ["Statik yükler"], ["Denge kararlı olmayabilir (kararlılık program dışı)"], ["Yakın–uzak etkisini yok saymak"]),
    M(["Tabloyu 'F birimi' ile doldur: komşu çiftler için çarpan (q_a·q_b), uzak çiftler için 1/4, 1/9 ile böl.",
       "Son olarak net kuvvetlerin toplamının 0 olduğunu hızla kontrol et."],
      ["Aynı doğru", "Yükler q'nun katları"], ["Yükler q'nun katı değilse F cinsinden yazım zor"], ["Yük çarpanını kuvvet çarpanıyla karıştırmak"]),
    M(["Kitap yöntemi: sayısal değerlerle F = k·q₁q₂/d²'yi her çift için hesapla (ÖD-3 gibi) ve topla."],
      ["Noktasal yükler"], ["Program hesaplamayı dışlar; kitapta var (ÖD-3, s.276)"], ["SI dönüşümü"]),
    "Üç yük + 'F cinsinden' → her çifti ayrı yaz: (yük çarpımı)/(d çarpanı)². Net kuvvetlerin toplamı sıfırdır — hesabın doğru olup olmadığını kontrol et.",
    "x ekseninde A(+q) x=0, B(−2q) x=d, C(+q) x=3d konumundadır. d uzaklığındaki iki q yükü arasındaki kuvvet F = k·q²/d² olsun. A, B ve C yüklerine etki eden net kuvvetleri F cinsinden ve yönleriyle bulunuz.",
    ["B'ye: A çeker (−x): 2q·q/d² → 2F; C çeker (+x): 2q·q/(2d)² → F/2. Net = −2F + F/2 = −3F/2 (A'ya doğru).",
     "A'ya: B çeker (+x): 2F; C iter (−x): q·q/(3d)² → F/9. Net = 2F − F/9 = +17F/9.",
     "C'ye: B çeker (−x): F/2; A iter (+x): F/9. Net = −F/2 + F/9 = −7F/18.",
     "Kontrol: −3/2 + 17/9 − 7/18 = 0."],
    "A: 17F/9 (+x), B: 3F/2 (−x), C: 7F/18 (−x); toplam sıfır.",
    """
from fractions import Fraction as Fr
q = [Fr(1), Fr(-2), Fr(1)]
x = [Fr(0), Fr(1), Fr(3)]
def net(i):
    s = Fr(0)
    for j in range(3):
        if j != i:
            r = x[i] - x[j]
            s += q[i] * q[j] * (1 if r > 0 else -1) / (r * r)    # F birimi, + = +x
    return s
assert net(0) == Fr(17, 9) and net(1) == Fr(-3, 2) and net(2) == Fr(-7, 18)
assert net(0) + net(1) + net(2) == 0
# hatalı yöntem: büyüklükleri işaretsiz toplamak B için 5F/2 verir
assert Fr(2) + Fr(1, 2) != abs(net(1))
# denge örneği: A(+4q) x=0, C(+q) x=3d; aradaki +q yük hangi x'te dengede? (karekök oranı)
xa, xc = 0.0, 3.0
qa, qc = 4.0, 1.0
x_eq = 3.0 * (qa ** 0.5) / (qa ** 0.5 + qc ** 0.5)
fa = qa / (x_eq - xa) ** 2; fc = qc / (xc - x_eq) ** 2
assert abs(fa - fc) < 1e-12 and abs(x_eq - 2.0) < 1e-12
""")

SOLUTIONS["coulomb-free-charge-dynamics"] = S(
    M(["Etki–tepki: iki yüke etki eden kuvvetin büyüklüğü eşittir (her an).",
       "Newton 2: a = F/m → ivme kütleyle ters orantılı; hafif yük daha büyük ivmeyle hareket eder.",
       "Yaklaştıkça d küçülür, F ∝ 1/d² artar; ivme sabit değildir (sabit ivmeli kinematik kullanılmaz).",
       "Buluşma noktası: kuvvetler iç kuvvettir, kütle merkezi sabit kalır: yer değiştirmeler kütleyle ters orantılı (hafif yük daha çok yol alır).",
       "Asılı yüklü cisimlerde denge: tanθ = F_e/mg; daha büyük kütleli cisim düşeyle daha küçük açı yapar (yük ve kuvvet eşitse)."],
      ["Yalnız iki yükün etkileşimi", "Başlangıçta durgun, dış kuvvet yok"],
      ["Program hesaplamayı dışlar; nitel/oran düzeyinde ele alınır", "İpli sistemde ip gerilmesi ve ağırlık eklenir"],
      ["Eşit kuvvetten eşit ivme çıkarmak", "İvmeyi sabit sanıp x = ½at² yazmak", "Yükleri orta noktada buluşturmak"]),
    M(["Kuvvet kütleden bağımsızdır (yüke ve uzaklığa bağlı); hareket tepkisi kütleye bağlıdır.",
       "Kütle eylemsizlik ölçüsüdür: aynı kuvvet ağır cismi az, hafif cismi çok hızlandırır.",
       "İç kuvvet sistemin kütle merkezini kıpırdatmaz."],
      ["Yalıtılmış iki cisim"], ["Dış kuvvet (yer çekimi, ip) varsa kütle merkezi sabit kalmaz"], ["Kuvveti ivmeyle karıştırmak"]),
    M(["Kontrol listesi: kuvvet=eşit, ivme=ters kütle, hız=hafif olan daha hızlı artar, buluşma=ağıra yakın, kuvvet zamanla artar (yaklaşırken)."],
      ["Başlangıçta durgun, iki cisim"], ["Dış kuvvet varsa uygulanmaz"], ["Buluşma noktasını ortada vermek"]),
    M(["Kütle merkezi yöntemi: x_cm = (m₁x₁ + m₂x₂)/(m₁+m₂) sabit; buluşma noktası x_cm'dir (11. sınıf Newton yasalarıyla)."],
      ["Yalıtılmış sistem"], ["Dış kuvvet yoksa"], ["Kütle merkezini ağır yükün yerinde sanmak"]),
    "İki serbest yük + kütle farkı → kuvvet eşit, ivme ters kütle, buluşma ağır olana yakın. Kuvvet yaklaştıkça artar; sabit ivme formülü kullanma.",
    "Boşlukta 1 m aralıkla durgun bırakılan zıt yüklü iki cismin kütleleri m ve 4m'dir (ağırlıklar ihmal). Başlangıçtaki ivmelerinin oranını, kuvvetler arasındaki ilişkiyi ve buluşma noktasının hafif cismin başlangıç konumundan uzaklığını bulunuz. Kuvvet zamanla nasıl değişir?",
    ["Kuvvetler eşit büyüklükte (etki–tepki); a ∝ 1/m → a_hafif/a_ağır = 4.",
     "Kütle merkezi sabit: x_cm = (m·0 + 4m·1)/5m = 0,8 m → buluşma, hafif cismin başlangıç noktasından 0,8 m uzakta (ağıra 0,2 m).",
     "Yaklaştıkça d küçülür, kuvvet büyür (ivme artar)."],
    "a_hafif/a_ağır = 4; buluşma hafif cisimden 0,8 m; kuvvet yaklaştıkça artar.",
    """
# sembolik birimler: k·q² = 1, m1 = 1, m2 = 4, başlangıç aralığı 1
m1, m2 = 1.0, 4.0
x1, x2 = 0.0, 1.0
v1 = v2 = 0.0
dt = 2e-5
def acc(x1, x2):
    d = x2 - x1
    F = 1.0 / d ** 2            # çekim: 1'i +x'e, 2'yi -x'e
    return F / m1, -F / m2, F
a1, a2, F0 = acc(x1, x2)
assert abs(a1 / abs(a2) - 4.0) < 1e-12
F_prev = F0
mono = True
steps = 0
while x2 - x1 > 0.02:
    a1, a2, F = acc(x1, x2)
    v1 += a1 * dt; v2 += a2 * dt
    x1 += v1 * dt; x2 += v2 * dt
    mono = mono and F >= F_prev - 1e-12
    F_prev = F
    steps += 1
assert mono                                  # kuvvet yaklaştıkça artar
xcm = (m1 * x1 + m2 * x2) / (m1 + m2)
assert abs(xcm - 0.8) < 1e-3                 # kütle merkezi sabit
assert abs(x1 - 0.8) < 0.02 and abs(x2 - 0.8) < 0.02
assert abs(m1 * v1 + m2 * v2) < 1e-6         # toplam momentum 0
""")

# ============================ FİZ.11.2.2 — Elektriksel alan (hesaplamasız: oran / yön / yorum) ============================
SOLUTIONS["efield-data-table-graph"] = S(
    M(["Tablodan yalnız bir değişkenin değiştiği satır çiftlerini seç (kontrol değişkeni).",
       "Kaynak yük q ×2 iken E ×2 ise E ∝ q; d ×2 iken E ×1/4 ise E ∝ 1/d².",
       "Test yükü q₀ değişirken E'nin değişmediğine (F/q₀ sabit) bak: E test yüküne değil kaynağa ve konuma bağlıdır.",
       "Eksik hücreyi referans satırdan çarpanlarla doldur (q ×3, d ×2 → E ×3/4).",
       "Grafik: E–q doğru (orijinden), E–d azalan eğri, E–(1/d²) doğru."],
      ["Tek değişkenli satır çifti", "Noktasal kaynak yük, aynı ortam"],
      ["Program formül kullandırmaz; veriden orantı çıkarılır", "Çok değişkenli satırlarda çarpanlar ayrı ayrı çarpılır"],
      ["E'yi 1/d ile orantılı sanmak", "Test yükü büyüdükçe E büyür sanmak", "Çok değişkenli satırlardan tek etkiyi okumak"]),
    M(["Alan, kaynak yükün uzaya yaydığı etkidir: yük arttıkça alan orantılı büyür.",
       "Etki küresel yüzeye yayılır (∝ d²), bu yüzden 1/d² ile zayıflar.",
       "Test yükü yalnızca alanı ölçer; kuvvet q₀ ile büyür, alan (kuvvet/q₀) değişmez."],
      ["Noktasal yük"], ["Test yükü alanı bozacak kadar büyük olmamalı"], ["Alan ile kuvveti karıştırmak"]),
    M(["Her satırda E·d²/q hesapla; sabit çıkıyorsa eksik hücre bu sabitle bulunur.", "Test yüklü ölçümlerde F/q₀ al; E aynıysa satırlar aynı noktadadır."],
      ["Aynı ortam"], ["Sabit çıkmayan satır hatalı ölçüm ya da başka değişken"], ["Birim hatası"]),
    M(["Kitap modeli: E = k·q/d² (s.185) ile SI'de hesap yapıp tabloyu doğrula."],
      ["Noktasal yük, boşluk/hava"], ["Program hesaplamayı dışlar; kitapta var"], ["nC, cm dönüşümleri"]),
    "E tablolarında tek değişkenli satır çifti bul: q için doğru, d için ters kare. 'Hangi grafik doğrusal?' → E–q ve E–(1/d²). Test yükü değişse de E değişmez.",
    "Bir simülasyonda noktasal bir yükün çevresinde alan ölçülüyor: (q=2 nC, d=3 cm) → 20 kN/C; (4 nC, 3 cm) → 40 kN/C; (2 nC, 6 cm) → 5 kN/C. Test yükü 1 nC iken 20 µN ölçülen noktada test yükü 2 nC yapılsa kuvvet ve alan ne olur? q=6 nC, d=6 cm noktasında E kaç kN/C okunur?",
    ["q ×2 → E ×2 (E ∝ q); d ×2 → E ×1/4 (E ∝ 1/d²).",
     "Aynı noktada q₀ ×2 → F = 40 µN olur, E = F/q₀ = 20 kN/C aynı kalır.",
     "q ×3, d ×2 → E = 20 × 3 × 1/4 = 15 kN/C."],
    "15 kN/C; test yükü 2 nC iken F = 40 µN, E değişmez (20 kN/C).",
    """
import math
rows = [(2, 3, 20.0), (4, 3, 40.0), (2, 6, 5.0)]
p_q = math.log(rows[1][2] / rows[0][2]) / math.log(rows[1][0] / rows[0][0])
p_d = math.log(rows[2][2] / rows[0][2]) / math.log(rows[2][1] / rows[0][1])
assert abs(p_q - 1) < 1e-9 and abs(p_d + 2) < 1e-9
c = rows[0][2] * rows[0][1] ** 2 / rows[0][0]
assert all(abs(E * d * d / q - c) < 1e-9 for q, d, E in rows)
assert abs(c * 6 / 6 ** 2 - 15.0) < 1e-9          # E = c·q/d²
k = 9e9
E_si = k * 6e-9 / 0.06 ** 2
assert abs(E_si / 1e3 - 15.0) < 1e-9                 # bağımsız SI hesabı
E_ref = k * 2e-9 / 0.03 ** 2
F1 = 1e-9 * E_ref; F2 = 2e-9 * E_ref
assert abs(F1 - 20e-6) < 1e-12 and abs(F2 - 40e-6) < 1e-12 and abs(F1 / 1e-9 - F2 / 2e-9) < 1e-6
""")

SOLUTIONS["efield-direction-and-lines"] = S(
    M(["Alan çizgisinin yönü: pozitif yükten çıkar (yükten dışarı), negatif yüke girer.",
       "Yük işaretini çizginin çıkış/giriş yönünden belirle; hangi yükten daha çok çizgi çıkıyorsa o yükün büyüklüğü daha büyüktür (çizgi sayısı ∝ |q|).",
       "Çizgi sıklığı (birim yüzeye düşen çizgi sayısı) alan büyüklüğüyle orantılıdır: sık → E büyük.",
       "Bir noktadaki alan yönü, o noktadan geçen çizgiye çizilen teğettir; çizgiler birbirini kesmez.",
       "Düzgün alanda çizgiler paralel ve eşit aralıklıdır."],
      ["Statik yükler", "Alan çizgisi gösterimi (model; yörünge değil)"],
      ["Çizgi sayısından yük oranı yalnız aynı çizim ölçeğinde okunur", "Uzayda çizgi sayısı sonsuz değildir, çizim modeldir"],
      ["Alan yönünü ters kurmak (negatiften dışarı)", "Sıklığı alan büyüklüğüne bağlamamak", "Alan çizgisini parçacık yolu sanmak"]),
    M(["Alan her noktada tek yönlüdür; bu yüzden çizgiler kesişemez.",
       "Pozitif yük kaynak (çizgiler çıkar), negatif yük kuyu (çizgiler girer).",
       "Sık çizgi, kuvvetin küçük bir test yükü üzerinde daha büyük olacağı bölgedir.",
       "Yük büyüklüğü iki katına çıkarsa çizgi sayısı iki katına çıkar; uzaklaştıkça çizgiler seyrekleşir."],
      ["Alan çizgisi modeli"], ["Nitel"], ["Çizgi sayısını mutlak ölçü sanmak"]),
    M(["Üç hızlı kural: (1) çıkıyor → +, giriyor → −; (2) çok çizgi → büyük |q|; (3) sık → E büyük."],
      ["Standart çizim"], ["Karmaşık çizimde (3 yük) komşu yüke bakıp karar ver"], ["Sonsuza giden çizgileri saymamak"]),
    None,
    "Alan çizgisi sorusunda önce yön (çıkıyor/giriyor) → işaret; sonra çizgi sayısı → büyüklük; sıklık → o noktadaki E. Kesişen çizgi içeren seçenek yanlıştır.",
    "Bir şekilde X yükünden dışarıya 16 alan çizgisi çıkıyor, Y yüküne 8 çizgi giriyor (kalan 8 çizgi dışarı uzaklaşıyor). Yüklerin işaretlerini ve büyüklüklerini karşılaştırınız. P noktasında birim alana 2, R noktasında birim alana 8 çizgi düşüyorsa E_R / E_P kaçtır?",
    ["X'ten çıkıyor → X pozitif; Y'ye giriyor → Y negatif.", "Çizgi sayısı ∝ |q|: |q_X| / |q_Y| = 16 / 8 = 2.",
     "Sıklık ∝ alan büyüklüğü: E_R / E_P = 8 / 2 = 4."],
    "X pozitif, Y negatif; |q_X| = 2|q_Y|; E_R = 4E_P.",
    """
import math
# çizgi sayısı ∝ |q|: küresel yüzeyden geçen çizgi yoğunluğu E ∝ q/r^2 ve yüzey 4πr^2 → toplam ∝ q (r'den bağımsız)
k = 1.0
for q in (1.0, 2.0, 5.0):
    totals = [k * q / r ** 2 * 4 * math.pi * r ** 2 for r in (0.5, 1.0, 3.0)]
    assert all(abs(t - totals[0]) < 1e-9 for t in totals)
assert abs((k * 2.0 * 4 * math.pi) / (k * 1.0 * 4 * math.pi) - 2.0) < 1e-12     # 16/8 = 2
# yön: pozitif yükte E radyal dışa, negatif yükte içe
def Evec(q, src, p):
    r = (p[0] - src[0], p[1] - src[1]); d = math.hypot(*r)
    return (k * q * r[0] / d ** 3, k * q * r[1] / d ** 3)
p = (1.0, 1.0)
Ep = Evec(+1.0, (0, 0), p); En = Evec(-1.0, (0, 0), p)
assert Ep[0] * p[0] + Ep[1] * p[1] > 0 and En[0] * p[0] + En[1] * p[1] < 0
# sıklık ∝ E: 2 → 8 çizgi/birim alan
assert abs(8 / 2 - 4) < 1e-12
""")

SOLUTIONS["efield-superposition-collinear"] = S(
    M(["İncelenen noktada her yükün alanını ayrı çiz: pozitif yükten uzağa, negatif yüke doğru.",
       "Büyüklüğü E₀ = kq/d² cinsinden yaz: çarpan = (|q|/q) / (uzaklık/d)².",
       "Yönlere işaret ver (sağ +, sol −) ve vektörel topla.",
       "Noktaları büyüklüğe göre sırala; sıfır noktası gerekiyorsa iki alanın eşit ve zıt olduğu bölgeyi ara.",
       "Sıfır noktası: aynı işaretli yüklerde yükler ARASINDA, zıt işaretli yüklerde yüklerin DIŞINDA ve küçük yüke yakın tarafta."],
      ["Noktasal yükler aynı doğru üzerinde", "Alan vektörel toplanır"],
      ["Program oran/yön düzeyi ister; sıfır noktasının tam konumu sayısal hesap gerektirir (kitapta nitel)", "Yükler aynı doğru üzerinde değilse bileşenler gerekir"],
      ["Alanları skaler toplamak", "Zıt yüklerin ortasında alanı sıfır sanmak", "Uzaklığı karesiz almak"]),
    M(["Alan, yükün kendi çevresindeki etkisidir; iki kaynağın etkileri üst üste biner (süperpozisyon).",
       "Zıt yüklerin arasında iki alan aynı yöne baktığı için toplanır; aynı işaretli yüklerin arasında zıt yöne baktığı için birbirini götürür.",
       "Sıfır noktası zayıf kaynağa yakındır: zayıf kaynağın alanı daha az olduğundan, onu dengelemek için yakın olunmalıdır."],
      ["Statik yükler"], ["Nitel"], ["Alanın yönünü karşılaştırmamak"]),
    M(["E₀ cinsinden tablo yap: her yük için (çarpan, yön) yaz; yönlere göre topla; üç noktayı ard arda tabloya yaz.",
       "Sıfır noktası için: aynı işaret → |q₁|/d₁² = |q₂|/d₂² ile oranı belirle; uzaklık oranı yük oranının karekökü."],
      ["Aynı doğru", "Yükler q'nun katı"], ["Yük aynı doğruda değilse işlemez"], ["Yön işaretini atlamak"]),
    M(["Sayısal ikinci yol: E = k·q/d² ile her noktada işaretli toplam; sıfır noktasını sayısal köklendir (kitap s.172 ve s.185)."],
      ["Noktasal yükler"], ["Program hesaplamayı dışlar; kitapta var"], ["Sıfır noktası denkleminde karekök dalı"]),
    "Alan bileşkesi sorusunda ilk iş yön tablosu: her yükten ayrı ok. Sonra E₀ cinsinden çarpan. Sıfır noktası = 'küçük yüke yakın': aynı işaret → arada, zıt işaret → dışarıda.",
    "x ekseninde +2q yükü x=0'da, −q yükü x=2d'de bulunuyor. E₀ = kq/d² olsun. K(x=−d), L(x=d), M(x=3d) noktalarındaki bileşke alanı E₀ cinsinden ve yönüyle bulunuz; büyüklük sıralamasını yapınız. Alanın sıfır olduğu nokta hangi bölgededir?",
    ["L'de: +2q'dan sağa (uzaklık d): 2E₀; −q'ya doğru sağa: E₀ → 3E₀ (+x).",
     "K'de: +2q'dan sola (d): 2E₀; −q'ya doğru sağa (3d): E₀/9 → net −17E₀/9 (sola).",
     "M'de: +2q'dan sağa (3d): 2E₀/9; −q'ya doğru sola (d): E₀ → net −7E₀/9 (sola).",
     "Sıralama: E_L (3) > E_K (17/9) > E_M (7/9). Sıfır noktası: yükler dışında, küçük yük (−q) tarafında x > 2d."],
    "E_L = 3E₀ (+x), E_K = 17E₀/9 (−x), E_M = 7E₀/9 (−x); sıfır nokta −q'nun sağ tarafında (x > 2d).",
    """
from fractions import Fraction as Fr
q = [Fr(2), Fr(-1)]; xs = [Fr(0), Fr(2)]
def E(p):
    s = Fr(0)
    for qi, xi in zip(q, xs):
        r = p - xi
        s += qi * (1 if r > 0 else -1) / (r * r)       # E₀ birimi, + = +x
    return s
assert E(Fr(1)) == 3 and E(Fr(-1)) == Fr(-17, 9) and E(Fr(3)) == Fr(-7, 9)
assert abs(E(Fr(1))) > abs(E(Fr(-1))) > abs(E(Fr(3)))
# sıfır noktası: ikiye bölme ile bul (x > 2 bölgesinde işaret değişimi)
lo, hi = 2.0001, 100.0
f = lambda x: float(E(Fr(x).limit_denominator(10 ** 12)))
assert f(lo) * f(hi) < 0
for _ in range(80):
    mid = (lo + hi) / 2
    if f(lo) * f(mid) <= 0: hi = mid
    else: lo = mid
x0 = (lo + hi) / 2
assert abs(x0 - (4 + 2 * 2 ** 0.5)) < 1e-6             # 4 + 2√2 ≈ 6,83 d
# arada ve solda sıfır yok (zıt işaretli yükler)
assert all(E(Fr(x, 10)) != 0 for x in list(range(-50, 0)) + list(range(1, 19)))
# hatalı yöntem: skaler toplam L için 2+1 = 3 verir ama K için 2 + 1/9 = 19/9 ≠ 17/9
assert Fr(2) + Fr(1, 9) != abs(E(Fr(-1)))
""")

SOLUTIONS["efield-point-charge-ratio"] = S(
    M(["E ∝ k·q/d² çarpan yöntemi: E_yeni = E · (q çarpanı) · (k çarpanı) / (d çarpanı)².",
       "E'yi artırma yolları: q'yu artırmak, noktaya yaklaşmak (d'yi küçültmek), k'si büyük ortam kullanmak.",
       "Test yükü q₀ değişince F = q₀E değişir, E değişmez (E = F/q₀).",
       "Doğru–yanlış ifadelerde uzaklık ilişkisi: pozitif ya da negatif yükten uzaklaştıkça |E| azalır (yön ayrı sorudur)."],
      ["Noktasal yük", "Aynı doğrultudaki karşılaştırma"],
      ["Program hesaplamayı dışlar; oran düzeyi", "Ortam değişince k değişir (yük değişmez)"],
      ["Alan–kuvvet karıştırma", "Test yükünü E'ye katmak", "Karesiz uzaklık"]),
    M(["Alan bir noktanın özelliğidir; oraya hangi yükün konduğundan bağımsızdır.",
       "Kaynak yükten uzaklaşınca alan seyrelir, ortam yükün etkisini zayıflatıyorsa (k küçük) alan küçülür.",
       "Negatif yükte alan büyüklüğü de uzaklıkla azalır; negatiflik yalnız yönü değiştirir."],
      ["Statik durum"], ["Nitel"], ["Negatif yükün alanının uzaklıkla arttığını sanmak"]),
    M(["Sırala: önce d (kare), sonra q, sonra k. 'Kaç E?' sorularında sayıyı tek satırda yaz: E·a·c/e²."],
      ["Çarpanlar verilmiş"], ["Çok adımda hata riski"], ["Çarpanları toplamak"]),
    M(["Sayısal ikinci yol: E = k·q/d² ve E = F/q₀ ile gerçek değerlerle iki durumu hesapla, oranla (kitap s.185)."],
      ["Noktasal yük"], ["Program hesaplamayı dışlar; kitapta var"], ["Birim dönüşümü"]),
    "'q ve d birlikte değişirse kaç E?' → q çarpanı / d çarpanının karesi. Test yükü değişirse E aynı, F değişir. Yükten uzaklaştıkça |E| azalır: işaret yalnızca yönü etkiler.",
    "Noktasal bir yükün P noktasında oluşturduğu alan E'dir. (a) Yük 3 katına, uzaklık 3 katına çıkarılırsa, (b) uzaklık yarıya inip ortamın k'si 2 katına çıkarsa alan kaç E olur? (c) P'ye konan test yükü 2 katına çıkarılırsa alan ve test yüküne etki eden kuvvet nasıl değişir?",
    ["(a) 3 / 3² = 1/3 → E/3.", "(b) 2 / (1/2)² = 8 → 8E.", "(c) E = F/q₀ sabit; F = q₀E 2 katına çıkar."],
    "(a) E/3, (b) 8E, (c) E değişmez, F iki katına çıkar.",
    """
k0, q, d, q0 = 9e9, 4e-9, 0.05, 1e-9
E = lambda k, qq, r: k * qq / r ** 2
E0 = E(k0, q, d)
assert abs(E(k0, 3 * q, 3 * d) / E0 - 1 / 3) < 1e-12
assert abs(E(2 * k0, q, d / 2) / E0 - 8) < 1e-9
F = lambda qt: qt * E0
assert abs(F(2 * q0) / F(q0) - 2) < 1e-12
assert abs(F(2 * q0) / (2 * q0) - E0) < 1e-9            # E = F/q0 değişmez
# negatif yükte de |E| uzaklıkla azalır
assert abs(E(k0, -q, 2 * d)) < abs(E(k0, -q, d))
# hatalı yöntem: uzaklık çarpanını karesiz almak
assert abs(E(k0, q, 2 * d) / E0 - 0.25) < 1e-12 and abs(E(k0, q, 2 * d) / E0 - 0.5) > 0.2
""")

SOLUTIONS["efield-uniform-plates"] = S(
    M(["Çizgiler pozitif levhadan negatif levhaya, levhalara dik, paralel ve eşit aralıklıdır (kenarlar hariç).",
       "E ∝ V/d: V ×a, d ×b ise E ×a/b.",
       "Çizgi sıklığı E ile orantılıdır: E büyürse çizgiler sıklaşır, küçülürse seyrekleşir; yön hep +'dan −'ye.",
       "Levhalar arasında alan her yerde aynıdır; levhalara yaklaşmak alanı değiştirmez."],
      ["Levhalar arası uzaklık, levha boyutlarına göre küçük", "Üreteç bağlı (V sabit) ya da V değişimi verilmiş"],
      ["Program hesaplamayı dışlar; oran düzeyi", "Üreteç bağlı değilse (yük sabit) d değişince E değişmez"],
      ["E = V·d yazmak", "V sabitken d büyüyünce E'nin büyüyeceğini sanmak", "Çizgi yönünü negatiften pozitife kurmak"]),
    M(["Gerilim, birim yük başına enerji farkı; uzaklık arttıkça aynı gerilim daha uzun bir yola yayılır, alan seyrelir.",
       "Alan çizgileri paralel olduğu için alan büyüklüğü levha arasında heryerde aynıdır."],
      ["İdeal paralel levha"], ["Kenar etkileri"], ["Gerilimle alanı karıştırmak"]),
    M(["E oranı = (V çarpanı)/(d çarpanı). Çizgileri sıklaştır/seyrekleştir."],
      ["V ve d çarpanları verilmiş"], ["Yük sabit durumda E = σ/ε₀ olur, d bağımsız"], ["Üretece bağlı mı kontrol etmemek"]),
    M(["Sayısal ikinci yol: E = V/d ile iki durumun E değerlerini hesapla (kitap s.176, s.185)."],
      ["Paralel levha"], ["Program hesaplamayı dışlar; kitapta var (10. Alıştırma b sembolik hesabı da kapsam dışı)"], ["cm → m dönüşümü"]),
    "'d iki katına çıkarsa' + üretece bağlı → E yarıya iner (çizgiler seyrekleşir). Gerilim artarsa E artar. Alan her yerde aynı; yön + → −.",
    "Gerilimi 20 V olan üretece bağlı, d = 4 cm aralıklı paralel levhalar arasındaki alan E'dir. (a) Üreteç gerilimi 30 V'a çıkarılır ve levhalar d = 2 cm'ye yaklaştırılırsa alan kaç E olur? (b) Yalnız levhalar 8 cm'ye uzaklaştırılırsa? Alan çizgileri nasıl değişir?",
    ["E ∝ V/d. (a) (30/20) / (2/4) = 1,5 / 0,5 = 3 → 3E, çizgiler sıklaşır.", "(b) V sabit, d ×2 → E ×1/2 → E/2, çizgiler seyrekleşir (yönleri aynı)."],
    "(a) 3E; (b) E/2 (çizgiler seyrek, paralel, + levhadan − levhaya).",
    """
E = lambda V, d: V / d
E0 = E(20.0, 0.04)
assert abs(E(30.0, 0.02) / E0 - 3) < 1e-12
assert abs(E(20.0, 0.08) / E0 - 0.5) < 1e-12
# bağımsız doğrulama: iki levha arasındaki alanı yüzey yük yoğunluğundan bul (sigma/eps0), V = E d ile tutarlı
eps0 = 8.854e-12
sigma = eps0 * E0                       # V sabit: E0 sağlayan yük yoğunluğu
assert abs(sigma / eps0 - E0) < 1e-6
# başarısız durum: üreteç çıkarılınca yük sabit kalır -> d değişse de E değişmez
E_const_charge = lambda d: sigma / eps0
assert abs(E_const_charge(0.08) - E_const_charge(0.04)) < 1e-9
assert abs(E(20.0, 0.08) - E_const_charge(0.08)) > 1.0
""")

SOLUTIONS["efield-charged-particle-deflection"] = S(
    M(["Levhalardan alanın yönünü belirle: pozitif levhadan negatif levhaya.",
       "Pozitif yüklü parçacık alanla AYNI yönde, negatif yüklü parçacık alana ZIT yönde saparır; yani pozitif parçacık negatif levhaya, negatif parçacık pozitif levhaya doğru sapar.",
       "Sapmayan parçacık yüksüzdür (F = qE = 0).",
       "Aynı giriş hızı ve aynı alan için sapma q/m ile orantılıdır: daha çok sapan parçacığın |q|/m değeri daha büyüktür.",
       "Kütleleri eşitse sapma yalnız |q| ile ölçülür."],
      ["Aynı giriş hızı, alana dik giriş", "Düzgün alan, ağırlık ihmal"],
      ["Program hesaplamayı değil işaret ilişkisini ölçer", "Giriş hızları farklıysa sapma karşılaştırılamaz (hızın etkisi eklenir)"],
      ["Elektronun pozitif levhadan uzağa saptığını sanmak", "Sapma miktarını yalnız yüke bağlamak", "Sapmayan parçacığı pozitif sanmak"]),
    M(["Kuvvet yüke işaretiyle bağlıdır: F = qE (işaretli). Pozitifte alan yönünde, negatifte zıt yönde.",
       "Aynı kuvvet hafif parçacıkta daha büyük ivme verir; q/m ivmenin ölçüsüdür.",
       "Yüksüz parçacık alanı 'hissetmez'."],
      ["Düzgün alan"], ["Nitel"], ["Kuvvetin yönünü alanla aynı almak (negatif için)"]),
    M(["Sapma yönü → işaret (pozitife yakın levhaya sapma negatif; negatif levhaya sapma pozitif).",
       "Sapma büyüklüğü → |q|/m sıralaması (aynı v için)."],
      ["Aynı v, aynı alan"], ["Farklı v'de geçersiz"], ["v'yi eşit saymak"]),
    None,
    "Sapma sorularında: negatif levhaya saparsa +, pozitif levhaya saparsa −, sapmazsa nötr; çok sapan = büyük q/m (aynı v ile).",
    "Üst levhası pozitif, alt levhası negatif yüklü paralel levhaların arasına aynı hızla, levhalara paralel giren X, Y ve Z parçacıklarından X alta doğru 2 cm, Y üste doğru 6 cm sapıyor, Z hiç sapmıyor. Parçacıkların yük işaretlerini ve |q|/m değerlerini karşılaştırınız.",
    ["Alan üstten alta (+ levhadan − levhaya). X alta (alan yönüne) saparsa pozitif; Y üste (alana zıt) saparsa negatif; Z hiç sapmazsa yüksüz.",
     "Aynı v ve aynı alan için sapma ∝ |q|/m: (|q|/m)_Y / (|q|/m)_X = 6/2 = 3."],
    "X pozitif, Y negatif, Z yüksüz; Y'nin |q|/m değeri X'inkinin 3 katıdır.",
    """
# düzgün alan: E = (0, -E0) (üst levha +). Parçacık x yönünde v ile girer; levha uzunluğu L
E0, v, L = 1000.0, 50.0, 0.1
def deflect(qm, vv=v, steps=10000):
    t_total = L / vv
    dt = t_total / steps
    y, vy = 0.0, 0.0
    for _ in range(steps):
        a = qm * (-E0)                 # a = (q/m) E
        vy += a * dt
        y += vy * dt
    return y
qm_X, qm_Y, qm_Z = 4.0, -12.0, 0.0
yX, yY, yZ = deflect(qm_X), deflect(qm_Y), deflect(qm_Z)
assert yX < 0 and yY > 0 and yZ == 0           # X alta (alan yönünde), Y üste, Z sapmaz
assert abs(abs(yY) / abs(yX) - 3.0) < 1e-6      # sapma oranı = |q|/m oranı
# sapma ∝ q/m (v sabit) ve v iki katına çıkarsa sapma 1/4'e iner (farklı v karşılaştırması geçersiz)
assert abs(deflect(qm_X, vv=2 * v) / yX - 0.25) < 1e-6
""")

SOLUTIONS["efield-force-balance-droplet"] = S(
    M(["Serbest cisim diyagramı çiz: ağırlık mg aşağı, elektriksel kuvvet qE (işaretiyle alan yönünde ya da zıt).",
       "Askıda kalma ya da sabit hız → net kuvvet sıfır: elektriksel kuvvet ağırlığı dengeler (aralarında direnç varsa onu da yaz).",
       "Elektriksel kuvvet yukarıysa yük işareti, alan yönüne göre belirlenir: alan aşağı ise yük negatiftir.",
       "Elektriksel kuvvet ağırlıktan büyükse net kuvvet yukarıdır; damla yukarı doğru ivmelenir (hız yönü ayrı bir şeydir).",
       "Alan ya da yük değişince denge bozulur; yeni net kuvvet = qE' − mg."],
      ["Düzgün alan", "Hava direnci sabit hız durumunda ayrıca yazılır"],
      ["Program hesaplamayı dışlar; denge koşulu kuvvet karşılaştırması olarak kullanılır", "Direnç hıza bağlıdır; ivmeli harekette sabit alınmaz"],
      ["Negatif yük için kuvveti alan yönünde çizmek", "Sabit hızı ivmeli sanmak", "Hız yönünü net kuvvet yönü sanmak"]),
    M(["Net kuvvet sıfırsa ivme sıfırdır (Newton 1): cisim durur ya da sabit hızla gider.",
       "Askıda kalan damlada ağırlık yok olmaz; elektriksel kuvvet ağırlığı dengeler.",
       "Hız yönü ile net kuvvet yönü birbirinden bağımsızdır."],
      ["Statik denge ya da sabit hız"], ["Nitel"], ["Yer çekimini sıfırlanmış sanmak"]),
    M(["Kuvvet karşılaştırması: qE = mg → askıda; qE > mg → yukarı ivme; qE < mg → aşağı ivme. İşaret: yukarı kuvvet + alan aşağı → yük negatif."],
      ["Dik doğrultuda iki kuvvet"], ["Direnç varsa üçüncü kuvvet"], ["Alan yönünü gözden kaçırmak"]),
    M(["Sayısal ikinci yol: q = mg/E değerini hesapla (kitap ÖD-5 Millikan düzeneği)."],
      ["Düzgün alan"], ["Program E hesabını dışlar; kitapta var"], ["Büyüklük–işaret karışıklığı"]),
    "Askıda / sabit hız → qE = mg (net sıfır). Kuvvet yukarı + alan aşağı → yük negatif. Alan 2 katına çıkarsa net kuvvet mg yukarı, ivme g yukarı. 'Askıda' ≠ 'ağırlık yok'.",
    "Düzgün, aşağı yönlü bir elektriksel alanda m kütleli bir yağ damlası havada askıda kalıyor. (a) Damlanın yük işareti nedir? (b) Alan 2 katına çıkarılırsa damla nasıl hareket eder? (c) Kütlesi 2m olan ve yük işareti aynı bir damlanın aynı alanda askıda kalması için yük büyüklüğü kaç katı olmalıdır?",
    ["Askıda kalma → elektriksel kuvvet yukarı ve mg'ye eşit; alan aşağı olduğundan kuvvetin yukarı olması için yük negatiftir.",
     "Alan 2E: elektriksel kuvvet 2mg yukarı, ağırlık mg aşağı → net mg yukarı → yukarı doğru, a = g ivmeyle hareket.",
     "qE = 2mg → q' = 2q: yük büyüklüğü 2 katı olmalıdır."],
    "(a) negatif; (b) yukarı doğru g ivmesiyle hızlanır; (c) 2 katı.",
    """
m, g, E0 = 2e-15, 10.0, 1e4
Ev = (0.0, -E0)                          # aşağı yönlü alan
q_mag = m * g / E0                       # askıda: |q| E = m g
q = -q_mag                               # negatif yük: F = qE yukarı
F_el = (q * Ev[0], q * Ev[1])
W = (0.0, -m * g)
assert F_el[1] > 0 and abs(F_el[1] + W[1]) < 1e-27            # net kuvvet sıfır, kuvvet yukarı
# pozitif yük olsaydı dengelenemezdi (kuvvet aşağı)
assert (q_mag * Ev[1]) < 0
# alan iki katına çıkınca net kuvvet ve ivme
net = q * 2 * Ev[1] + W[1]
assert abs(net - m * g) < 1e-27 and abs(net / m - g) < 1e-9 and net > 0
# 2m kütleli damla aynı alanda askıda: |q'| = 2|q|
q2 = 2 * m * g / E0
assert abs(q2 / q_mag - 2) < 1e-12
""")

# ============================ FİZ.11.2.3 — Faraday kafesi (nitel; bilgi toplama / doğrulama / kayıt) ============================
SOLUTIONS["fcage-source-and-search"] = S(
    M(["Araştırma sorusunu yaz ve anahtar sözcüklerini belirle (Faraday kafesi, iletken, elektrik alan, kullanım alanı).",
       "Her aday kaynağa ölçütleri sor: yazar/kurum belli mi, güncel mi, kaynakça var mı, hakemli/denetimli mi, amacı tarafsız mı, diğer kaynaklarla tutarlı mı.",
       "Ölçüt sayısına göre kaynakları puanla; popülerlik (beğeni, tıklanma) ölçüt değildir.",
       "En güvenilir kaynaktan, soruyu doğrudan yanıtlayan paragrafı anahtar sözcüklerle bul.",
       "Bilgiyi tek kaynağa dayandırma; en az bir bağımsız kaynakla karşılaştır."],
      ["Aday kaynakların bilgileri tabloda verilmiş"],
      ["Güvenilir kaynak da soruyla ilgisiz olabilir: önce soruyla ilgisine bak", "Ölçütlerin ağırlığı bağlama göre değişebilir"],
      ["Popüler paylaşımı güvenilir saymak", "Reklam sayfasını tarafsız sanmak", "Yazarı belirsiz kaynağı kısa ve anlaşılır diye seçmek"]),
    M(["Bilgi, kaynağın denetlenebilirliğiyle değer kazanır: yazar, kaynakça ve hakemlik yanlışı yakalama şansını artırır.",
       "Amaç (satış, görüş, bilgilendirme) içeriği çarpıtabilir; tarafsızlık bu yüzden ölçüttür."],
      ["Genel ağ kaynakları dahil"], ["Nitel"], ["Anlaşılırlıkla doğruluğu karıştırmak"]),
    M(["Tabloda 'yazar yok / kaynakça yok / reklam amaçlı' işaretlerini ele; kalanlar arasında hakemli ya da kurum onaylı olanı seç."],
      ["Tablo tam"], ["Hepsi eksikse en az eksikliği olanı al ve doğrulama ekle"], ["Tek ölçütle karar vermek"]),
    None,
    "Kaynak seçiminde tablodaki 'beğeni / tıklanma' sütunu tuzaktır; yazar + güncellik + kaynakça + hakemlik/kurum + tarafsızlık + tutarlılık ölçütlerini say.",
    "'Asansörde cep telefonu neden zor çeker?' sorusu için dört kaynak var: (A) üniversite yazarlı, 2022 tarihli, kaynakçalı hakemli makale; (B) MEB onaylı ders kitabı bölümü, 2023, kaynakçasız; (C) 5000 beğenili, yazarı belirsiz, 2019 tarihli forum yazısı; (D) bir firmanın reklam sayfası. Hangi kaynak tercih edilmeli?",
    ["Ölçütleri işaretle: yazar belli, güncel, kaynakça, hakemli/kurum onaylı, tarafsız, tutarlı.",
     "A: 6/6; B: 5/6 (kaynakça yok); C: 1/6 (yalnız tarafsız görünüyor); D: 2/6 (yazar/güncel, ama amaç reklam).",
     "Beğeni sayısı puanı etkilemez. En yüksek puan: A; B ikinci kaynak olarak çapraz doğrulama için kullanılır."],
    "A (hakemli makale); B ile çapraz doğrulama yapılabilir.",
    """
criteria = ["yazar", "guncel", "kaynakca", "hakem_kurum", "tarafsiz", "tutarli"]
sources = {
    "A": dict(yazar=1, guncel=1, kaynakca=1, hakem_kurum=1, tarafsiz=1, tutarli=1, begeni=0),
    "B": dict(yazar=1, guncel=1, kaynakca=0, hakem_kurum=1, tarafsiz=1, tutarli=1, begeni=10),
    "C": dict(yazar=0, guncel=0, kaynakca=0, hakem_kurum=0, tarafsiz=1, tutarli=0, begeni=5000),
    "D": dict(yazar=1, guncel=1, kaynakca=0, hakem_kurum=0, tarafsiz=0, tutarli=0, begeni=300),
}
score = lambda s: sum(sources[s][c] for c in criteria)
ranked = sorted(sources, key=score, reverse=True)
assert ranked[0] == "A" and ranked[1] == "B" and score("A") == 6 and score("B") == 5 and score("C") == 1 and score("D") == 2
# beğeni sayısı sıralamayı değiştirmemeli (popülerlik ölçüt değil)
sources["C"]["begeni"] = 10 ** 9
assert sorted(sources, key=score, reverse=True) == ranked
# bir kaynak kaynakça eklerse sıralama değişir: ölçüt gerçekten etkili
sources["B"]["kaynakca"] = 1
assert score("B") == 6
""")

SOLUTIONS["fcage-verify-claims"] = S(
    M(["Her iddiayı üç soruyla sına: (1) yapı iletken ve kapalı mı? (2) boşluklar küçük mü? (3) neyi koruyor (iç bölge) ve neyi korumuyor (kafesin kendisi / dış yüzey)?",
       "İlke: iletken kapalı yapıda serbest yükler yeniden dağılır, iç bölgede dış alanın etkisi ortadan kalkar; yük ve kıvılcım dış yüzeyde kalır.",
       "İddiayı ilkeyle karşılaştır: yalıtkan kafes, açık kafes, çok geniş boşluk ya da 'içerdeki cismin net yük biriktirdiği' iddiaları ilkeye aykırıdır.",
       "Çelişen iki kaynakta ilkeye uyanı seç ve ikinci bir bağımsız kaynakla doğrula.",
       "Uygulama yorumu: asansör/MR odası/uçak gövdesi/mikrodalga fırın = iletken kabuk; cep telefonu zayıflar ya da kesilir."],
      ["İletken ve kapalı (ya da küçük boşluklu) kafes", "Dış alan yalnızca kafesin dışındaki kaynaktan geliyor"],
      ["Program ayrıntılı alan hesabı istemez; fizik gerekçesi nitel", "Kafesin dış yüzeyi korunmaz; içerideki kaynaklar iç bölgede ayrı etki yapar", "Boşluk dalga boyu ile kıyaslanabilir olursa koruma azalır"],
      ["Kafesin yalıtkandan da olabileceğini sanmak", "İçeride net yük biriktiğini sanmak", "Boşluk büyüdükçe korumanın arttığını sanmak"]),
    M(["İletkende serbest yükler dış alan karşısında yer değiştirir; yeni yük dağılımının alanı iç bölgede dış alanı tam sönümler.",
       "Yük yeniden dağılımı dış yüzeyde olur; iç bölge dışarıdan 'görünmez'.",
       "Boşluk büyürse yükler iç bölgeyi tam kapatamaz; alan sızar."],
      ["Statik ya da yavaş değişen alan"], ["Nitel"], ["Kafesin içindeki alanı sıfır diye kafesin kuvvet almadığını sanmak"]),
    M(["Karar ağacı: yalıtkan → yanlış; açık/çok boşluklu → koruma zayıf; iletken + kapalı → iç bölge korunur; 'içeride yük birikir' → yanlış (yük dışta)."],
      ["Standart iddialar"], ["İddiada ayrıntı varsa (frekans, boşluk) ilkeyle ayrıca düşün"], ["Cümlenin yalnız bir kısmını kontrol etmek"]),
    None,
    "Faraday kafesi iddialarında anahtar: 'iletken + kapalı → iç bölge dış alandan korunur'. Yalıtkan, açık ya da geniş boşluklu kafes ve 'içerdeki cisim yüklenir' ifadeleri yanlıştır.",
    "Bir kaynak 'metal kafesin içindeki kişi yıldırımdan korunur', diğeri 'kafes içinde elektriksel alan hâlâ vardır, yalnız şiddeti azalır' diyor. Üçüncü kaynakta 'kafes yalıtkandan da yapılabilir' yazıyor. Hangisi fizik ilkesiyle uyumludur? Kafesin bir yüzünde büyük bir boşluk olsaydı ne olurdu?",
    ["İlke: kapalı iletken yapıda iç bölgede dış alan yoktur → 1. iddia doğru (yük dış yüzeyden boşalır), 2. iddia (alan azalır) kapalı iletkende yanlış (tam sıfırlanır; yalnız boşluklu kafeste kısmen sızabilir).",
     "3. iddia yanlış: yükler serbest hareket edemeyen yalıtkanda yeniden dağılım olmaz.",
     "Büyük boşluk: alan iç bölgeye sızar; koruma azalır."],
    "Yalnız 1. iddia doğrudur; 2. ve 3. yanlıştır. Boşluk büyükse koruma bozulur.",
    """
# Laplace denkleminin ardışık gevşetmesiyle (SOR) iletken kapalı halkanın iç alanı: 2B model
def interior_field(gap, gh=0, N=41):
    h = N // 2
    phi = [[-(i - h) * 1.0 for j in range(N)] for i in range(N)]       # başlangıç tahmini: dış alan her yere nüfuz etmiş
    fixed = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i in (0, N - 1) or j in (0, N - 1):
                fixed[i][j] = True                                       # dış sınır: düzgün dış alan potansiyeli
            x, y = i - h, j - h
            if 8 <= max(abs(x), abs(y)) <= 9:                            # iletken halka (potansiyeli sabit = 0)
                if gap and x <= -8 and abs(y) <= gh:
                    continue
                phi[i][j] = 0.0; fixed[i][j] = True
    for it in range(20000):
        diff = 0.0
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if fixed[i][j]:
                    continue
                d = 1.9 * (0.25 * (phi[i + 1][j] + phi[i - 1][j] + phi[i][j + 1] + phi[i][j - 1]) - phi[i][j])
                phi[i][j] += d; diff = max(diff, abs(d))
        if diff < 1e-10:
            break
    m = 0.0
    for i in range(h - 6, h + 7):
        for j in range(h - 6, h + 7):
            Ex = -(phi[i + 1][j] - phi[i - 1][j]) / 2; Ey = -(phi[i][j + 1] - phi[i][j - 1]) / 2
            m = max(m, (Ex * Ex + Ey * Ey) ** 0.5)
    return m
closed = interior_field(False)
small, mid, large = interior_field(True, 0), interior_field(True, 2), interior_field(True, 5)
E0 = 1.0
assert closed < 1e-6 * E0                        # kapalı iletken: iç bölgede alan yok
assert closed < small < mid < large              # boşluk büyüdükçe sızan alan artar
assert large > 0.3 * E0
""")

SOLUTIONS["fcage-record-information"] = S(
    M(["Kayıt tablosunun sütunlarını belirle: bilgi | kaynak (yazar/kurum, tarih) | doğrulama durumu.",
       "Her satırı eksiksiz doldur; kaynağı belirtilmeyen bilgi kayıt sayılmaz (atıf ilkesi).",
       "Doğrulanmamış bilgiyi 'doğrulanmadı' işaretiyle ayır; sunuya yalnız doğrulanmış ve kaynağı belli bilgileri al.",
       "Bilgiyi kendi cümlenle yazsan bile kaynağı yaz.",
       "Eksik öge sorusunda boş kalan hücreyi ya da atlanmış basamağı (doğrulama) bul."],
      ["Kayıt tablosu verilmiş"], ["Nitel; biçim ilkeleri bağlama göre sütun adı değiştirebilir"],
      ["Kaynak yazmadan kaydetmek", "Doğrulamayı atlayıp sunuya almak", "Sütun anlamlarını karıştırmak"]),
    M(["Kayıt, bilginin izlenebilirliğidir: kaynak ve doğrulama olmadan bilgi sınanamaz.",
       "Doğrulama, yeni bilginin kullanılabilir olması için gereken kapıdır."],
      ["Bilimsel çalışma"], ["Nitel"], ["Kaydı sunumdan ayırmamak"]),
    M(["Tabloda boş hücre ara: kaynak boş → eksik atıf, doğrulama boş → sunuya alma."],
      ["Standart 3 sütun"], ["Başka öge de istenirse tabloyu genişlet"], ["Tek sütuna bakmak"]),
    None,
    "Kayıt sorularında 'eksiksiz = bilgi + kaynak + doğrulama'. Sunuya yalnız üçü de dolu olan satır girer.",
    "Bir öğrenci üç kayıt tutmuş: (1) 'Kafes iletken olmalı' – Ders kitabı s.182 – doğrulandı; (2) 'Kafes içinde alan sıfırdır' – kaynak yok – doğrulandı; (3) 'Boşluk büyürse koruma azalır' – Makale (2022) – doğrulanmadı. Hangi kayıtlar sunuya alınabilir? Eksikler nedir?",
    ["Sunuya alma ölçütü: kaynak yazılı ve doğrulanmış.", "(1) iki ölçütü de sağlar; (2) kaynak yok → önce kaynak eklenmeli; (3) doğrulanmadı → önce doğrulanmalı."],
    "Yalnız (1) sunuya alınır; (2)'de kaynak, (3)'te doğrulama eksiktir.",
    """
records = [
    {"bilgi": "Kafes iletken olmalı", "kaynak": "Ders kitabı s.182", "dogrulandi": True},
    {"bilgi": "Kafes içinde alan sıfırdır", "kaynak": "", "dogrulandi": True},
    {"bilgi": "Boşluk büyürse koruma azalır", "kaynak": "Makale (2022)", "dogrulandi": False},
]
complete = lambda r: bool(r["bilgi"]) and bool(r["kaynak"]) and r["dogrulandi"]
ok = [r["bilgi"] for r in records if complete(r)]
assert ok == ["Kafes iletken olmalı"]
missing = {r["bilgi"]: ("kaynak" if not r["kaynak"] else "dogrulama") for r in records if not complete(r)}
assert missing == {"Kafes içinde alan sıfırdır": "kaynak", "Boşluk büyürse koruma azalır": "dogrulama"}
""")

# ============================ FİZ.11.2.4 — Mıknatıs etkileşimi ============================
SOLUTIONS["magnet-pole-interaction"] = S(
    M(["Kutupları yaz: aynı kutuplar iter, zıt kutuplar çeker; tek kutuplu mıknatıs yoktur (kesilince her parça iki kutuplu).",
       "Hangi cisme etki eden kuvveti soruyorsa o cismin serbest cisim diyagramını çiz (ağırlık, normal/ip, manyetik kuvvet).",
       "Etki–tepki: iki mıknatıs birbirine eşit büyüklükte, zıt yönde kuvvet uygular.",
       "Terazi okuması: R = (m·g ± F)/g. İtme aşağı yönlüyse okuma artar (+F), çekme yukarı yönlüyse azalır (−F).",
       "Kuvvet mesafe azaldıkça ve kutup şiddeti arttıkça büyür; okuma değişimi de büyür."],
      ["Mıknatıs çiftinde eksen düşey ve ikinci mıknatıs sabit tutuluyor", "Terazi durgun (denge)"],
      ["Mesafeye bağımlılık nitel (azalan eğri); bu ünitede formül yok", "Demir parçası ya da yüksüz madde ortama konulursa etki değişir"],
      ["Kutup kuralını ters kurmak", "Terazi okumasında artış–azalış yönünü ters kurmak", "Etki–tepkiyi unutmak"]),
    M(["Mıknatıs kutupları etkileşen 'yükler' gibi davranır ama ayrı bir kutup bulunamaz (kutuplar çift halinde var).",
       "Okuma, terazinin taşıdığı toplam düşey kuvveti gösterir: ağırlık artı aşağı doğru ek kuvvet.",
       "Kuvvet çiftinin parçalarından biri teraziye ek yük, diğeri ise sabit tutulan mıknatısa uygulanır."],
      ["Statik denge"], ["Nitel"], ["Kuvveti yalnız çeken mıknatısa bağlamak"]),
    M(["Önce kutup durumu: itme (aynı) → okuma ARTAR; çekme (zıt) → okuma AZALIR. Büyüklük: yaklaştıkça fark büyür."],
      ["Alttaki mıknatıs terazide, üstteki sabit"], ["Üstteki mıknatıs terazi üstünde de ise tüm sistemin okuması değişmez (iç kuvvetler)"], ["İki mıknatıs aynı terazide ise etkinin dışarıya yansıdığını sanmak"]),
    None,
    "Terazi okuması sorusu: aynı kutup yakın → R artar, zıt kutup yakın → R azalır; yaklaştıkça değişim büyür. 'Aynı kutuplar çeker' ve 'ikiye kesince tek kutup' seçenekleri tuzaktır.",
    "Terazinin üzerindeki 200 g'lık çubuk mıknatısın N ucu yukarıya bakıyor (okuma 200 g). Üzerine sabit tutulan özdeş bir mıknatıs, S ucu aşağıda olacak biçimde yaklaştırılınca manyetik kuvvet 0,5 N oluyor. Okuma kaç g olur? S yerine N ucu aşağıya bakacak biçimde yaklaştırılsaydı? (g = 10 m/s²)",
    ["Alttaki N, üstteki S: zıt kutuplar → çekme, kuvvet yukarı: terazinin yükü azalır.", "R = (mg − F)/g = (2 − 0,5)/10 = 0,15 kg = 150 g.",
     "N–N: itme, kuvvet aşağı: R = (2 + 0,5)/10 = 0,25 kg = 250 g."],
    "Zıt kutuplarda 150 g; aynı kutuplarda 250 g.",
    """
g = 10.0
m = 0.200
F = 0.5
def reading(sign):
    # statik denge: N = m g + sign * F (sign=+1 aşağı doğru ek kuvvet)
    N = m * g + sign * F
    return N / g * 1000.0
assert abs(reading(-1) - 150.0) < 1e-9 and abs(reading(+1) - 250.0) < 1e-9
# yaklaştıkça kuvvet artar (azalan kuvvet–uzaklık ilişkisi varsayımı, nitel): okuma farkı büyür
F_of_d = lambda d: 0.5 * (0.02 / d) ** 3
changes = [abs((m * g + F_of_d(d)) / g * 1000 - 200.0) for d in (0.04, 0.03, 0.02, 0.01)]
assert all(changes[i] < changes[i + 1] for i in range(3))
""")

SOLUTIONS["magnet-data-collection"] = S(
    M(["Tabloyu okumadan önce sütunları ve birimleri yaz (mesafe cm/m, sapma °, kuvvet N).",
       "Bağımsız değişkeni (mesafe) sırala; bağımlı değişkenin eğilimini belirle (azalan/artan).",
       "Eğilime uymayan satırı (yön değiştiren değer) 'hatalı ölçüm' diye işaretle; tekrar ölçüm gerektir.",
       "Eksik değeri komşu satırlar arasında eğilime uygun olacak biçimde tahmin et (azalan eğri: ara değer iki komşunun arasında).",
       "Alan çizgisi sıklığı ile alan büyüklüğü doğru orantılıdır; demir tozu yoğun bölge = güçlü alan."],
      ["Tek değişken (mesafe) değişiyor, diğerleri sabit", "Ölçümler aynı düzenekte alınmış"],
      ["Mıknatıs alanı mesafeyle doğrusal değil azalan eğri gibi değişir; doğru orantı kurma", "Çevredeki demir cisimler ölçümü etkiler"],
      ["Sütunları ya da birimi karıştırmak", "Eğri grafiği doğru orantı sanmak", "Tek ölçümle yetinmek"]),
    M(["Mıknatıs etkisi uzaklaştıkça hızla azalır; bu yüzden pusula sapması mesafeyle azalır.",
       "Tekrarlanan ölçüm tek bir hatalı değerin etkisini azaltır."],
      ["Veri toplama"], ["Nitel"], ["Rastgele hatayı gerçek eğilim sanmak"]),
    M(["Satırları sırayla bak: bir önceki satırdan büyük çıkan değer, azalan veride hatalıdır."],
      ["Monoton azalan beklenen eğilim"], ["Gerçek salınımlı veride işlemez"], ["Gürültüyü hata sanmak"]),
    None,
    "Mıknatıs veri tablosunda: mesafe arttıkça etki azalır. 'Yükselen' değer varsa hatalı satırdır. Çizgi sıklığı ↔ alan büyüklüğü ilişkisini hatırla.",
    "Bir öğrenci mıknatısı pusulaya 5, 10, 15, 20, 25 cm uzaklıklarda tutup iğnenin sapma açısını 83°, 45°, 16°, 26°, 4° ölçüyor. Hangi ölçüm eğilime uymuyor? Beklenen değer yaklaşık kaç derece olmalı? Uzaklık arttıkça çizgi sıklığı ve alan nasıl değişir?",
    ["Beklenen eğilim: mesafe arttıkça sapma azalır (83 > 45 > 16 > … > 4).", "20 cm'deki 26° değeri, 15 cm'deki 16°'den büyük: eğilime uymuyor, hatalı ölçüm.",
     "Komşular arasında (16° ile 4°) bir değer beklenir: yaklaşık 7° (ters-küp eğilimiyle tan θ ∝ 1/d³).", "Uzaklık arttıkça çizgiler seyrekleşir ve alan zayıflar."],
    "20 cm'deki 26° hatalıdır; beklenen yaklaşık 7° (16° ile 4° arasında); çizgi sıklığı ve alan azalır.",
    """
import math
d = [5, 10, 15, 20, 25]
theta = [83.0, 45.0, 16.0, 26.0, 4.0]
bad = [i for i in range(1, 5) if theta[i] > theta[i - 1]]
assert bad == [3]                                   # 20 cm satırı eğilime aykırı
# bağımsız model: iğne sapması tan(θ) = B_miknatis/B_dunya, B ∝ 1/d^3 (çubuk mıknatıs, uzak alan)
c = math.tan(math.radians(45.0)) * 10 ** 3        # 10 cm'deki ölçümden sabit
pred = [math.degrees(math.atan(c / x ** 3)) for x in d]
assert abs(pred[0] - 83.0) < 3 and abs(pred[2] - 16.0) < 2 and abs(pred[4] - 4.0) < 1
assert abs(pred[3] - 7.1) < 0.2 and abs(pred[3] - theta[3]) > 15           # beklenen ≈7°, ölçülen 26° çok farklı
# eğilim eşlemesi: mesafe arttıkça açı azalır (sütunlar karıştırılırsa bu çıkarım bozulur)
assert all(pred[i] > pred[i + 1] for i in range(4))
""")

SOLUTIONS["magnet-field-lines-pattern"] = S(
    M(["Çizgi yönü: dışarıda N → S, mıknatısın içinde S → N (kapalı eğriler); çıkış yapılan uç N, giriş yapılan uç S'dir.",
       "Zıt kutuplar arasında çizgiler birbirine doğru uzanır ve sıktır: çekim; aynı kutuplar arasında çizgiler birbirinden kaçar: itme ve ortada seyrek/alan sıfır bölge.",
       "Çizgi sıklığı = alan büyüklüğü: kutuplara yakın en sık, uzakta seyrek.",
       "Üç mıknatıslı desende her bölgeyi komşu iki ucun etkileşimiyle oku: eğri birleşiyorsa zıt, ayrılıyorsa aynı kutup.",
       "Çizgiler kesişmez."],
      ["Statik mıknatıs alanı", "Çizgi/demir tozu deseni verilmiş"],
      ["Demir tozu deseni gözlem modelidir; çizgiyi toz oluşturmaz", "Çok mıknatıslı desende her noktada bileşke düşün"],
      ["Çizgi yönünü mıknatıs içinde de N→S almak", "Aynı kutuplar arasında alanı en büyük sanmak", "Çizgi sıklığını ters yorumlamak"]),
    M(["Çizgiler alanın yönünü ve şiddetini gösteren modeldir; pusula iğnesi çizgiye teğet durur.",
       "Aynı kutuplar arasındaki orta bölgede iki alan zıt yönlü olduğundan toplam sıfırdır (nötr nokta).",
       "Zıt kutuplar arasında alanlar aynı yöne baktığı için toplanır."],
      ["İki özdeş mıknatıs"], ["Nitel"], ["Nötr noktayı alan çizgisi yok sanmak"]),
    M(["Deseni üç adımda oku: yön (N→S) → kutup cinsi; birleşen/ayrılan çizgi → çekme/itme; sık → güçlü."],
      ["Çizgi deseni net"], ["Karmaşık desende nötr noktalara dikkat"], ["Yönü atlamak"]),
    M(["Kutup modeli: her kutbu noktasal 'manyetik yük' say; bileşke alanı vektörel topla (ünite içi nitel model; bağıntı yok)."],
      ["Uzak alan, kutuplara göre aralık büyük"], ["Gerçek mıknatıs dipol; yakında model kaba"], ["Nötr noktanın tam yerini bu modelle ölçülü sanmak"]),
    "Alan çizgilerinde: çizgiler birleşiyorsa zıt kutup, ayrılıyorsa aynı kutup, ortada seyrek/sıfır alan = aynı kutuplar. Çıkan uç N.",
    "İki özdeş çubuk mıknatıs aynı kutuplarıyla (N–N) karşı karşıya, 2d aralıkla konmuştur. Aralarındaki orta noktada bileşke alan nedir? Orta noktadan eksene dik d uzaklıktaki bir noktada bileşke alan hangi yöndedir? Zıt kutuplar karşı karşıya olsaydı orta noktada alan nasıl olurdu? (yalnız karşılıklı iki kutbu hesaba kat.)",
    ["Aynı kutuplarda orta noktada iki alan zıt yönlü ve eşit: bileşke 0.",
     "Dik doğrultuda, iki alanın eksene paralel bileşenleri birbirini götürür, eksene dik bileşenleri toplanır: bileşke eksenden uzağa doğrudur.",
     "Zıt kutuplarda orta noktada alanlar aynı yönlüdür (N'den S'ye), toplam büyüktür."],
    "N–N: orta noktada alan sıfır, dik doğrultuda alan eksenden uzağa; N–S: orta noktada alan iki kat güçlü, N'den S'ye.",
    VEC + """
# kutup modeli: kutup alanı B = s * r / |r|^3 (N: s=+1, S: s=-1), yalnız yön/oran için
def B_pole(s, src, p):
    r = sub(p, src)
    return mul(s / norm(r) ** 3, r)
d = 1.0
N1, N2 = (-d, 0.0, 0.0), (d, 0.0, 0.0)
mid = (0.0, 0.0, 0.0)
# aynı kutuplar (N-N): orta noktada sıfır
Bmid = add(B_pole(+1, N1, mid), B_pole(+1, N2, mid))
assert norm(Bmid) < 1e-12
# dik doğrultuda (0, d): eksenden uzağa (+y), eksene paralel bileşen yok
p = (0.0, d, 0.0)
Bp = add(B_pole(+1, N1, p), B_pole(+1, N2, p))
assert Bp[1] > 0 and abs(Bp[0]) < 1e-12
# zıt kutuplar (N solda, S sağda): orta noktada alan N'den S'ye (+x) ve tek kutbun iki katı
Bopp = add(B_pole(+1, N1, mid), B_pole(-1, N2, mid))
assert Bopp[0] > 0 and abs(Bopp[0] - 2 * norm(B_pole(+1, N1, mid))) < 1e-12
""")

SOLUTIONS["magnet-vector-compass-earth"] = S(
    M(["Aranan noktada her kaynağın alan vektörünü çiz: mıknatıs için dışarıda N → S yönünde çizgiye teğet; Dünya alanı verilmişse onu da ekle.",
       "Bileşenlere ayır (x, y) ve vektörel topla; büyüklükler kenar uzunluğu olarak okunur.",
       "Pusulanın N ucu bileşke alan yönünü gösterir (iğne bileşke çizgiye teğet durur).",
       "Dünya alanı ihmal edilmiyorsa bileşke yön onun etkisiyle sapar; ihmal edilince yalnız mıknatısların alanı sayılır.",
       "Yön bulmada: pusulanın N ucu coğrafi kuzeyi gösterir (Dünya'nın coğrafi kuzeyindeki kutup manyetik S gibi davranır); haritaya göre hedefin yönünü sapma açısıyla ver."],
      ["Statik alanlar", "Pusula küçük (alanı bozmaz)"],
      ["Nitel/vektörel çizim; sayısal toplam gerekirse bileşenlerle", "Demir cisimler pusulayı saptırır"],
      ["Pusulanın N ucunu mıknatısın S kutbundan uzağı gösteren olarak çizmek", "Dünya alanını yok saymak (verildiyse)", "Alanları skaler toplamak"]),
    M(["Pusula, küçük bir mıknatıs gibi, bulunduğu noktadaki bileşke alana hizalanır: torku sıfırlayan denge.",
       "Dünya her yerde zayıf bir alan oluşturur; yakındaki güçlü mıknatıs ona baskın çıkar."],
      ["Pusula iğnesi serbest"], ["Nitel"], ["Alan çizgisini iğnenin yörüngesi sanmak"]),
    M(["Dik kenarlı üçgen yöntemi: iki alan dik ise bileşke 3-4-5 gibi; yönü tanθ = (dikey bileşen)/(yatay bileşen)."],
      ["Alanlar birbirine dik ya da bileşenlere ayrılmış"], ["Dik değilse bileşen yöntemi"], ["Açıyı yanlış eksenden ölçmek"]),
    None,
    "Pusula + iki mıknatıs sorularında önce her alan vektörünü çiz (N→S), sonra paralelkenar/bileşen. Pusulanın N ucu hep bileşke alan yönünde. Dünya alanı verildiyse bileşkeye ekle.",
    "K noktasında bir mıknatıs +x (doğu) yönünde 3 birim, diğeri +y (kuzey) yönünde 4 birimlik alan oluşturuyor; Dünya alanı +y yönünde 2 birimdir. Dünya alanı ihmal edilirse ve edilmezse pusulanın N ucu hangi yönde durur? (Açıları +x'ten ölç.)",
    ["İhmal: (3, 4) → bileşke 5 birim; açı = arctan(4/3) ≈ 53°.", "İhmal etmeden: (3, 4 + 2) = (3, 6) → büyüklük ≈ 6,7; açı = arctan(6/3) ≈ 63°.",
     "Pusulanın N ucu bu yönlerde (kuzeydoğu) durur; Dünya alanı iğneyi kuzeye doğru biraz daha çevirir."],
    "İhmal: ≈53° (+x'ten), 5 birim; ihmal etmeden ≈63°, ≈6,7 birim.",
    """
import math
B1, B2, BE = (3.0, 0.0), (0.0, 4.0), (0.0, 2.0)
net0 = (B1[0] + B2[0], B1[1] + B2[1]); net1 = (net0[0] + BE[0], net0[1] + BE[1])
ang = lambda v: math.degrees(math.atan2(v[1], v[0]))
assert abs(math.hypot(*net0) - 5.0) < 1e-12 and abs(ang(net0) - 53.130) < 1e-2
assert abs(ang(net1) - 63.435) < 1e-2 and abs(math.hypot(*net1) - 45 ** 0.5) < 1e-12
# bağımsız doğrulama: pusula iğnesinin dinamiği (sönümlü sarkaç): θ'' = -c sin(θ - φ) - γ θ'  → bileşke alan açısına yerleşir
def settle(phi, theta0=0.0):
    th, w, dt = theta0, 0.0, 1e-3
    for _ in range(60000):
        a = -50.0 * math.sin(th - phi) - 4.0 * w
        w += a * dt; th += w * dt
    return th
for v in (net0, net1):
    phi = math.atan2(v[1], v[0])
    assert abs(settle(phi) - phi) < 1e-3
# hatalı yöntem: büyüklükleri skaler toplamak (3 + 4 = 7) bileşke büyüklük değildir
assert abs((3 + 4) - math.hypot(*net0)) > 1
""")

# ============================ FİZ.11.2.5 — Düz tel (hesaplamasız: oran / yön / yorum) ============================
SOLUTIONS["wire-field-data-model"] = S(
    M(["Düzenekte neyin değiştirildiğini belirle: pil/direnç değişirse önce akım değişir (i = V/R), sonra alan.",
       "Tablodan tek değişkenli satır çifti seç: i ×2 iken B ×2 ise B ∝ i; d ×2 iken B ×1/2 ise B ∝ 1/d (kare yok!).",
       "Eksik hücre: çarpanları zincirle (i ×3, d ×1,5 → B ×2).",
       "Pusula sapmasını alan büyüklüğünün göstergesi olarak yorumla: sapma arttıkça tel alanı daha etkin (Dünya alanı sabit).",
       "Grafik: B–i doğru (orijinden), B–d azalan hiperbol, B–(1/d) doğru."],
      ["Tek değişkenli satır çifti", "Sonsuz uzun ince düz tel, aynı ortam"],
      ["Program formül kullandırmaz; B = 2K·i/d kitapta var (s.235)", "Telin ucuna yakın ya da kısa telde model geçerli değil"],
      ["B'yi 1/d² ile orantılı sanmak (ters kare ile karıştırma)", "Pusula sapmasını açıyla doğru orantılı sanmak", "Devre değişikliğinde akım değişimini atlamak"]),
    M(["Akım artarsa her yük akışı katkı yapar: alan akımla doğru orantılıdır.",
       "Alan telin çevresinde çember çizgilerle yayılır; çevre 2πd ile büyüdüğü için etki 1/d ile azalır (yüzeyle değil çevreyle, bu yüzden 1/d²'den farklı).",
       "Pusula sapması, tel alanının Dünya alanına oranının işaretidir."],
      ["Statik akım"], ["Nitel"], ["Küresel yayılma (1/d²) ile silindirik yayılmayı (1/d) karıştırmak"]),
    M(["Her satırda B·d/i hesapla; sabit çıkıyorsa eksik hücre bu sabitle bulunur."],
      ["Aynı ortam, düz tel"], ["Sabit çıkmayan satır hatalı ya da başka değişken"], ["B·d²/i hesaplamak"]),
    M(["Kitap modeli: B = 2K·i/d, K = 10⁻⁷ T·m/A ile SI hesabı yap."],
      ["Sonsuz uzun düz tel"], ["Program hesaplamayı dışlar; kitapta var (s.235)"], ["cm → m dönüşümü, µT dönüşümü"]),
    "Tel alanı tablosunda: i ile doğru, d ile ters (1/d), kare yok. 'Direnç yarıya iner' → i iki katı → B iki katı. Eksik hücrede çarpanları zincirle.",
    "Bir öğrenci düz bir telin çevresinde manyetik alan sensörüyle ölçüm yapıyor: (i=2 A, d=2 cm) → 20 µT; (4 A, 2 cm) → 40 µT; (2 A, 4 cm) → 10 µT. Aynı tel için i=6 A, d=3 cm noktasında alan kaç µT olur? Pil gerilimi sabitken devrenin direnci yarıya indirilirse alan ne olur?",
    ["i ×2 → B ×2 (B ∝ i); d ×2 → B ×1/2 (B ∝ 1/d).", "i ×3, d ×1,5 → B = 20 × 3 / 1,5 = 40 µT.",
     "V sabit, R ×1/2 → i ×2 (i = V/R) → B ×2."],
    "40 µT; direnç yarıya inince alan iki katına çıkar.",
    """
import math
rows = [(2, 2, 20.0), (4, 2, 40.0), (2, 4, 10.0)]
p_i = math.log(rows[1][2] / rows[0][2]) / math.log(rows[1][0] / rows[0][0])
p_d = math.log(rows[2][2] / rows[0][2]) / math.log(rows[2][1] / rows[0][1])
assert abs(p_i - 1) < 1e-9 and abs(p_d + 1) < 1e-9                # 1/d, 1/d² değil
c = rows[0][2] * rows[0][1] / rows[0][0]
assert all(abs(B * d / i - c) < 1e-9 for i, d, B in rows)
assert abs(c * 6 / 3 - 40.0) < 1e-9
# bağımsız: kitap modeli B = 2K i/d (SI) → µT
K = 1e-7
Bsi = lambda i, d_cm: 2 * K * i / (d_cm * 1e-2) * 1e6
assert abs(Bsi(2, 2) - 20.0) < 1e-9 and abs(Bsi(6, 3) - 40.0) < 1e-9
# Ohm: V sabit, R yarıya → i iki katı → B iki katı
V, R = 12.0, 6.0
assert abs(Bsi(V / (R / 2), 2) / Bsi(V / R, 2) - 2) < 1e-12
# başarısız model: 1/d² ile orantılı sanılsaydı d ×2 için B/4 çıkardı (tabloya uymaz)
assert abs(rows[2][2] / rows[0][2] - 0.25) > 0.2
""")

SOLUTIONS["wire-field-direction-rhr"] = S(
    M(["Sağ el kuralı: sağ elin baş parmağı akım yönünü, kıvrılan dört parmak alan çizgilerinin dönüş yönünü gösterir.",
       "Alan çizgileri telin çevresinde telle ortak merkezli çemberlerdir; bir noktadaki alan, o noktadaki çembere teğettir (yarıçapa dik).",
       "Sayfa düzleminde yatay tel, akım sağa: telin üstünde alan sayfa DIŞINA (⊙), altında sayfa İÇİNE (⊗) doğrudur.",
       "Akım yönü ters çevrilince tüm yönler tersine döner.",
       "Pusula: iğnenin N ucu o noktadaki alan yönünde durur."],
      ["Düz iletken tel", "Geleneksel akım yönü (+'dan −'ye)"],
      ["Elektron akışı yönü esas alınırsa sağ el yerine sol el gerekir; soru geleneksel akımı ister", "Dünya alanı ihmal edilmiyorsa pusula bileşke alana göre durur"],
      ["Elektron akışı yönünü akım sanmak", "Alanı tele paralel ya da radyal çizmek", "Telin iki yanında aynı yönü yazmak"]),
    M(["Akım çevresinde dönen bir alan oluşturur; alan telden uzaklaşmaz ya da yaklaşmaz, onu sarar.",
       "Bu yüzden alan çizgileri kapalı çemberlerdir ve kuvvet doğrultusu alanın ve akımın ikisine de diktir (ileride).",
       "Aynı akım yönünde telin karşı yanlarında alanlar zıt yönlüdür."],
      ["Statik akım"], ["Nitel"], ["Alan yönünü radyal sanmak"]),
    M(["Sayfa içi/dışı için kısa test: akım yukarıya doğruysa sağ taraf sayfa içine (⊗), sol taraf dışına (⊙); akım sağa doğruysa üst taraf dışına (⊙)."],
      ["Telin sayfa düzleminde olduğu çizim"], ["Telin sayfaya dik olduğu çizimde saat yönü kuralı: akım dışarı (⊙) → saat yönü tersi"], ["Saat yönünü karıştırmak"]),
    None,
    "Düz tel yön sorusu: baş parmak akım → parmaklar alan. Tel sayfada yatay + akım sağa → üst ⊙, alt ⊗. Akım sayfadan dışarı (⊙) ise çizgiler saat yönünün TERSİNE. Akım ters → hepsi ters.",
    "Sayfa düzleminde yatay bir telden akım sağa doğru akıyor. Telin 3 cm üstündeki P noktasında ve 3 cm altındaki Q noktasında alanın yönünü bulunuz. Akım sayfadan dışarıya (⊙) çıkan düşey bir telde ise telin sağında (doğusunda) bir pusulanın N ucu hangi yöne bakar? Akım ters çevrilirse ne olur?",
    ["P (üst): sağ el, baş parmak sağa → parmaklar üstte sayfa dışına döner: ⊙; Q (alt): ⊗.",
     "⊙ akım, saat yönünün tersi çemberler: telin sağında (+x) alan yukarı (+y); pusula N ucu yukarı.",
     "Akım ters olunca tüm yönler tersine döner: P ⊗, Q ⊙; sağdaki pusula aşağıyı gösterir."],
    "P: sayfa dışı (⊙), Q: sayfa içi (⊗); ⊙ akımda sağdaki pusula yukarı bakar; akım ters olunca yönler de ters.",
    VEC + """
x, y, z = (1, 0, 0), (0, 1, 0), (0, 0, 1)          # z: sayfa dışına (⊙)
# durum 1: akım +x, P üstte (+y), Q altta (-y): B yönü = I × r̂ (sağ el kuralı)
BP = cross(x, y); BQ = cross(x, (0, -1, 0))
assert BP == z and BQ == (0, 0, -1)                 # P: sayfa dışı, Q: sayfa içi
# bağımsız: sonlu uzun telin Biot–Savart toplamı aynı yönü verir
wire = line((-500.0, 0, 0), (500.0, 0, 0), n=20000)
Bp = biot(wire, (0.0, 3.0, 0.0)); Bq = biot(wire, (0.0, -3.0, 0.0))
assert Bp[2] > 0 and Bq[2] < 0 and abs(Bp[0]) < 1e-9 and abs(Bp[1]) < 1e-9
assert abs(Bp[2] + Bq[2]) < 1e-9                     # eşit büyüklük, zıt yön
# durum 2: akım +z (⊙), pusula telin sağında (+x): alan +y (yukarı)
assert cross(z, x) == y and cross(z, (-1, 0, 0)) == (0, -1, 0)
wz = line((0, 0, -500.0), (0, 0, 500.0), n=20000)
assert biot(wz, (2.0, 0, 0))[1] > 0 and abs(biot(wz, (2.0, 0, 0))[0]) < 1e-9
# akım ters: tüm yönler ters
assert cross(mul(-1, x), y) == (0, 0, -1)
assert biot(list(reversed(wz)), (2.0, 0, 0))[1] < 0
""")

SOLUTIONS["wire-field-ratio"] = S(
    M(["B ∝ K·i/d çarpan yöntemi: B_yeni = B · (i çarpanı) · (K çarpanı) / (d çarpanı).",
       "Uzaklık ters orantılı (1/d), KARESİ YOK; ortam K'yi değiştirir (demir/ferromanyetik ortamda K büyür).",
       "İki ayrı tel için karşılaştırmada her telin (i/d) oranını yaz ve oranla.",
       "Tablo: tek değişkenli satır çifti → çarpan; eksik hücre çarpan zinciri.",
       "Yön ayrı sorudur (sağ el); büyüklük ve yön birbirine karışmaz."],
      ["Sonsuz uzun ince düz tel", "Aynı ortam (ya da K çarpanı verilmiş)"],
      ["Program formülle hesap değil oran yorumu ister; B = 2K·i/d kitapta var (s.235)", "Çok yakın ya da kısa telde model geçersiz"],
      ["d çarpanını karesiyle almak", "Çarpanları toplamak", "Uzaklığı artınca B artar sanmak"]),
    M(["Akım ne kadar fazlaysa o kadar çok yüklü parçacık hareket eder, alan orantılı artar.",
       "Uzaklaştıkça alan çemberin çevresine yayılır: çevre d ile doğru artar, B 1/d ile azalır.",
       "Ortam, alanı ileten malzemenin özelliğidir (K)."],
      ["Düz tel"], ["Nitel"], ["Ters kare ile karıştırmak"]),
    M(["Önce (i/d) oranını al: i/d ne kadar değişti? Bunu K çarpanıyla çarp. Tek satırda bitir."],
      ["Çarpanlar verilmiş"], ["d'yi karelemek hataya yol açar"], ["Ters kareyi uygulamak"]),
    M(["Sayısal yol: B = 2K·i/d ile referans ve yeni durumu SI'de hesapla, oranla."],
      ["Düz tel"], ["Program hesaplamayı dışlar; kitapta var"], ["Birim dönüşümü"]),
    "Düz tel oranında d KARESİZ ters orantıdır. 'i 3 katına, d 3 katına' → B değişmez (ters karede 1/3 çıkardı). Ortam değişince K değişir.",
    "Bir düz telden i akımı geçerken d uzaklığındaki alan B'dir. (a) i 3 katına ve d 3 katına çıkarsa, (b) i yarıya ve d yarıya inerse, (c) aynı noktada tel ortamı K'si 5 katı olan bir ortama alınırsa alan kaç B olur?",
    ["(a) 3 / 3 = 1 → B (değişmez).", "(b) (1/2)/(1/2) = 1 → B (değişmez).", "(c) K ×5 → 5B."],
    "(a) B, (b) B, (c) 5B.",
    """
K = 1e-7
B = lambda i, d, k=K: 2 * k * i / d
i0, d0 = 4.0, 0.06
B0 = B(i0, d0)
assert abs(B(3 * i0, 3 * d0) / B0 - 1) < 1e-12 and abs(B(i0 / 2, d0 / 2) / B0 - 1) < 1e-12
assert abs(B(i0, d0, 5 * K) / B0 - 5) < 1e-12
# bağımsız: Biot–Savart sayısal integrali (sonlu uzun tel) 1/d yasasını verir
import math
def biot_mag(d, L=2000.0, n=200000):
    s = 0.0
    dz = 2 * L / n
    for i in range(n):
        z = -L + (i + 0.5) * dz
        r = math.hypot(d, z)
        s += d / r ** 3 * dz           # |dl × r̂|/r²  (μ0/4π ve i atıldı)
    return s
b1, b2 = biot_mag(1.0), biot_mag(2.0)
assert abs(b1 / b2 - 2.0) < 1e-3               # B ∝ 1/d (1/d² olsaydı oran 4 olurdu)
assert abs(b1 / b2 - 4.0) > 1.5
""")

SOLUTIONS["wire-field-superposition"] = S(
    M(["Her telin alanını ayrı belirle: yön sağ el kuralıyla (nokta telin hangi yanında), büyüklük B ∝ i/d ile (B₀ = referans).",
       "Büyüklükleri B₀ cinsinden yaz: çarpan = (i çarpanı)/(d çarpanı).",
       "Sayfa içi/dışı yönlere + / − işareti ver ve işaretli topla.",
       "Aynı yönlü akımlı iki telin ARASINDA alanlar zıt yönlü (büyüklükler eşitse sıfır); DIŞINDA aynı yönlü.",
       "Zıt yönlü akımlı iki telin arasında alanlar aynı yönlü (toplanır), dışında zıt yönlü."],
      ["Paralel uzun teller", "Sayfaya dik teller ya da yükseltilmiş düzlem çizimi"],
      ["Program oran/yön düzeyi ister; B = 2K·i/d'li sayısal hesap kitapta var", "Teller paralel değilse bileşenler gerekir"],
      ["Alanları skaler toplamak", "Telin hangi yanında olduğunu yön hesabında atlamak", "1/d² kullanmak"]),
    M(["Her tel bağımsız bir dönen alan oluşturur; noktadaki alan bu iki dönüşün üst üste binmesidir.",
       "Aralarda iki dönüş zıt yönde karşılaşır (aynı yönlü akım), dışta aynı yönde birleşir.",
       "Alan zayıf telin yakınında sıfırlanır: büyük akımlı tel daha uzakta olmalı (sıfır noktası zayıf akımlı tele yakın)."],
      ["Statik akım"], ["Nitel"], ["Sıfır noktasını tam ortada sanmak"]),
    M(["Tablo: nokta | tel1 (yön, çarpan) | tel2 (yön, çarpan) | toplam. Çarpanı i/d ile ver, yönü ± ile ver."],
      ["İki tel"], ["Üç tel için üç sütun"], ["Yönü işaretsiz bırakmak"]),
    M(["Vektör yöntemi: B = 2K·i/d × (ẑ × r̂ yönü) ile işaretli toplam; sayısal doğrulama (kitap s.235)."],
      ["Paralel teller"], ["Program hesaplamayı dışlar; kitapta var"], ["Birim vektör işareti"]),
    "İki paralel tel sorusunda her noktada ayrı ayrı: yön (sağ el, noktanın hangi yanda olduğu) ve i/d. Aynı yönlü akım: arada zıt, dışta aynı yönlü; i₂ = 2i₁ ise sıfır noktası zayıf tele daha yakın (uzaklık 1:2).",
    "Sayfaya dik iki uzun telden X, x=0'da ve i akımı sayfadan DIŞARIYA, Y ise x=3d'de ve 2i akımı sayfadan DIŞARIYA taşıyor. i akımının d uzaklıkta oluşturduğu alan B₀ olsun. x=d (arada), x=−d (X'in solu) ve x=4d (Y'nin sağı) noktalarındaki bileşke alanı B₀ cinsinden ve yönüyle bulunuz.",
    ["x=d: X'in alanı (sağında): yukarı (+y), büyüklük i/d → B₀; Y'nin alanı (solunda): aşağı, 2i/2d → B₀. Net 0.",
     "x=−d: X'in alanı (solunda): aşağı, B₀; Y (4d uzakta, solunda): aşağı, 2i/4d → B₀/2. Net 3B₀/2 aşağı.",
     "x=4d: X (4d, sağında): yukarı, B₀/4; Y (d, sağında): yukarı, 2i/d → 2B₀. Net 9B₀/4 yukarı."],
    "x=d: 0; x=−d: 3B₀/2 (aşağı); x=4d: 9B₀/4 (yukarı).",
    VEC + """
from fractions import Fraction as Fr
wires = [(Fr(0), Fr(1)), (Fr(3), Fr(2))]          # (konum, akım), akım +z (sayfa dışı)
z = (0, 0, 1)
def Bnet(xp):
    s = Fr(0)
    for xw, i in wires:
        r = xp - xw
        rhat = (1 if r > 0 else -1, 0, 0)
        By = cross(z, rhat)[1]                      # sağ el: ẑ × r̂ 
        s += By * i / abs(r)                        # B₀ birimi (+ = +y)
    return s
assert Bnet(Fr(1)) == 0 and Bnet(Fr(-1)) == Fr(-3, 2) and Bnet(Fr(4)) == Fr(9, 4)
# bağımsız: sonlu uzun tellerin Biot–Savart toplamı (B₀ = 2·1/1 = 2 birim)
def bs(xp):
    tot = (0.0, 0.0, 0.0)
    for xw, i in wires:
        w = line((float(xw), 0, -600.0), (float(xw), 0, 600.0), n=24000)
        tot = add(tot, biot(w, (float(xp), 0.0, 0.0), I=float(i)))
    return tot[1] / 2.0                             # B₀ cinsinden
for xp, expect in ((1, 0.0), (-1, -1.5), (4, 2.25)):
    assert abs(bs(xp) - expect) < 0.02
# aynı yönlü akımlar: arada zıt yönlü iki alan; zıt yönlü akım olsaydı toplanırdı
wires_opp = [(Fr(0), Fr(1)), (Fr(3), Fr(-2))]
wires_saved, wires = wires, wires_opp
assert Bnet(Fr(1)) == 2                              # B₀ + B₀ = 2B₀
""")

# ============================ FİZ.11.2.6 — Akım makarası ============================
SOLUTIONS["solenoid-data-model"] = S(
    M(["Tablodan tek değişkenli satır çifti seç: i ×2 → B ×2 (B ∝ i); N ×2 (L sabit) → B ×2 (B ∝ N); L ×2 (N sabit) → B ×1/2 (B ∝ 1/L).",
       "Üç ilişkiyi birleştir: B ∝ i·N/L = i·n (n = birim uzunluktaki sarım sayısı).",
       "Eksik hücre: i, N, L çarpanlarını zincirle (B_yeni = B · (i çarpanı)(N çarpanı)/(L çarpanı)).",
       "Doğrusallaştırma: B–n grafiği orijinden geçen doğrudur; B–L grafiği (N sabit) hiperboldür.",
       "Çekirdek (demir) değişince çarpan K değişir: B çok artar."],
      ["Uzun ince makara (L ≫ yarıçap), merkez eksende, makaranın ortasında", "Aynı çekirdek/ortam"],
      ["Makaranın uçlarında alan yarıya yakın azalır", "Kısa/kalın makarada yarıçap etkilidir", "Demir çekirdekte formül sabiti değişir"],
      ["N artınca L artsa da B artar sanmak (n önemli)", "L ile doğru orantı kurmak", "Uç noktada ölçüm"]),
    M(["Her sarım bir halka alanı ekler; halkalar sıklaştıkça (n) üst üste binen katkılar toplanır.",
       "Aynı N daha uzun gövdeye yayılırsa sarım sıklığı azalır, alan zayıflar."],
      ["Uzun makara"], ["Nitel"], ["N ile L'yi bağımsız düşünmemek"]),
    M(["Her satırda B·L/(i·N) hesapla; sabit çıkıyorsa model doğru ve eksik hücre bu sabitle tamamlanır."],
      ["Aynı çekirdek"], ["Demir çekirdekli satır varsa ayrı grup olur"], ["N yerine n kullanıp L'yi unutmak"]),
    M(["Kitap modeli: B = 4π·K·i·N/L ile SI hesabı (s.235): K = 10⁻⁷ T·m/A."],
      ["Uzun makara"], ["Program ayrı bir hesap sınırı koymaz; kitapta formül var (merkez ekseni)"], ["cm → m"]),
    "Makara tablosu: B ∝ i·N/L. N ve L birlikte değişiyorsa N/L oranına bak. Demir çekirdek: tablonun ayrı bir satır grubu.",
    "Hava çekirdekli uzun bir makarada merkez ekseninde ölçülen alan: (i=1 A, N=100, L=10 cm) → 1,26 mT; (2 A, 100, 10 cm) → 2,51 mT; (1 A, 200, 10 cm) → 2,51 mT; (1 A, 100, 20 cm) → 0,63 mT. (i=3 A, N=200, L=20 cm) satırında B kaç mT olur?",
    ["i ×2 → B ×2; N ×2 → B ×2; L ×2 → B ×1/2: B ∝ iN/L.", "i ×3, N ×2, L ×2: çarpan 3·2/2 = 3 → B = 1,26 × 3 = 3,77 mT."],
    "≈3,77 mT.",
    """
import math
rows = [(1, 100, 0.10, 1.26), (2, 100, 0.10, 2.51), (1, 200, 0.10, 2.51), (1, 100, 0.20, 0.63)]
lg = math.log
assert abs(lg(rows[1][3] / rows[0][3]) / lg(2) - 1) < 0.01 and abs(lg(rows[2][3] / rows[0][3]) / lg(2) - 1) < 0.01
assert abs(lg(rows[3][3] / rows[0][3]) / lg(2) + 1) < 0.01
c = rows[0][3] * rows[0][2] / (rows[0][0] * rows[0][1])
assert all(abs(B * L / (i * N) - c) < 0.01 * c for i, N, L, B in rows)
target = c * 3 * 200 / 0.20
assert abs(target - 3.77) < 0.02
# bağımsız: halkaların merkez alanının toplamı (Biot–Savart halka formülü), R << L
R, L = 0.002, 0.10
def Bcenter(i, N, L):
    s = 0.0
    for j in range(N):
        z = (j + 0.5) / N * L - L / 2
        s += 1e-7 * 2 * math.pi * i * R ** 2 / (R ** 2 + z ** 2) ** 1.5
    return s * 1e3          # mT
b0 = Bcenter(1, 100, 0.10)
assert abs(b0 - 1.26) < 0.01
assert abs(Bcenter(3, 200, 0.20) - target) < 0.02
assert abs(Bcenter(1, 100, 0.20) / b0 - 0.5) < 0.01
# N iki katı, L de iki katı → n aynı → B aynı (yalnız N'ye bakmak yanıltır)
assert abs(Bcenter(1, 200, 0.20) / b0 - 1) < 0.01
""")

SOLUTIONS["solenoid-ratio-generalization"] = S(
    M(["B ∝ K·i·(N/L) çarpan yöntemi: B_yeni = B · (i çarpanı) · (N çarpanı/L çarpanı) · (K çarpanı).",
       "Sarım yoğunluğu n = N/L'yi düşün: N ve L aynı oranda değişirse B değişmez.",
       "İdeal makarada yarıçap, tel kalınlığı ve makaranın kesit şekli B'yi etkilemez; içte alan düzgün, dışta ihmal edilir.",
       "Çekirdek: demir çekirdek K'yi çok artırır → B çok artar (elektromıknatıs).",
       "Yeni büyüklüğü 'kaç B' diye yaz, yönü ayrıca belirle."],
      ["Uzun ince makara (ideal), orta bölge", "Çarpanlar verilmiş"],
      ["Kısa ve kalın makarada yarıçap etkilidir", "Doyma: demir çekirdekte B sınırsız artmaz"],
      ["Yarıçapın etkili olduğunu sanmak", "N ve L'yi ayrı etkili saymak", "Demir çekirdekte K değişmez sanmak"]),
    M(["Alanı üreten, birim uzunluktaki akım çevrim sayısıdır (n·i); makaranın şekli değil.",
       "Çekirdek, ortamın alanı güçlendirmesini sağlar (ferromanyetik)."],
      ["İdeal makara"], ["Nitel"], ["Toplam telin uzunluğuna bakmak"]),
    M(["Önce n çarpanını bul (N çarpanı/L çarpanı), sonra i ve K ile çarp."],
      ["Standart soru"], ["Hem N hem L hem i değişirse dikkatli çarp"], ["Çarpanları toplamak"]),
    M(["Sayısal ikinci yol: B = 4π·K·i·N/L ile iki durumu SI'da hesapla ve oranla."],
      ["Uzun makara"], ["Kitapta formül var; program ek hesap sınırı koymaz"], ["Birim"]),
    "Makara oran sorusunda 'N/L'ye bak: N de L de iki katına çıkarsa B aynı. Yarıçap/tel kalınlığı etkisiz. Demir çekirdek → B artar.",
    "Hava çekirdekli uzun bir makaranın merkez ekseninde alan B'dir. (a) N 2 katına ve L 2 katına çıkarılırsa, (b) i 3 katına ve L yarıya indirilirse, (c) makara yarıçapı 2 katına çıkarılırsa (uzun makara), (d) içine demir çekirdek yerleştirilirse alan nasıl değişir?",
    ["(a) n = N/L değişmez → B.", "(b) i ×3, L ×1/2 → 3 / (1/2) = 6 → 6B.", "(c) İdeal uzun makarada yarıçap etkisiz → B.", "(d) K çok artar → B çok artar (kat sayısı çekirdeğe bağlı)."],
    "(a) B, (b) 6B, (c) B (değişmez), (d) B çok artar.",
    """
import math
K = 1e-7
R0 = 0.003
def Bloop_sum(i, N, L, R, K=K):
    # halka halka toplam (merkez): Biot–Savart halka formülü (μ0/4π = K)
    s = 0.0
    for j in range(N):
        z = (j + 0.5) / N * L - L / 2
        s += K * 2 * math.pi * i * R ** 2 / (R ** 2 + z ** 2) ** 1.5
    return s
B0 = Bloop_sum(1.0, 200, 0.2, R0)
assert abs(Bloop_sum(1.0, 400, 0.4, R0) / B0 - 1) < 2e-3                  # (a)
assert abs(Bloop_sum(3.0, 200, 0.1, R0) / B0 - 6) < 2e-2                  # (b)
assert abs(Bloop_sum(1.0, 200, 0.2, 2 * R0) / B0 - 1) < 2e-3              # (c) yarıçap etkisiz (R << L)
assert abs(Bloop_sum(1.0, 200, 0.2, R0, K=100 * K) / B0 - 100) < 1e-6     # (d) K çarpanı
# formül: 4πK i N / L
assert abs(B0 - 4 * math.pi * K * 1.0 * 200 / 0.2) / B0 < 2e-3
# kısa ve kalın makarada yarıçap etkilidir (model sınırı)
Bs = lambda R: Bloop_sum(1.0, 200, 0.02, R)
assert abs(Bs(0.04) / Bs(0.02) - 1) > 0.3
""")

SOLUTIONS["solenoid-direction-poles-compass"] = S(
    M(["Sağ el kuralı (makara): dört parmak makaranın sarımlarında akım yönünde kıvrılır, baş parmak merkez eksende alanın (ve N kutbunun) yönünü gösterir.",
       "N kutbu: alanın içeriden dışarıya çıktığı uç; S kutbu giriş ucu. Dışarıda çizgiler N → S, içeride S → N.",
       "Pusula: iğnenin N ucu o noktadaki bileşke alan yönünü gösterir (içte makara ekseni boyunca, dışta N ucundan uzağa).",
       "İki makara: alanlarını vektörel topla. N–N yüz yüze → aradaki orta noktada alan sıfır; N–S yüz yüze → alan toplanır.",
       "Akım yönü ters çevrilince kutuplar yer değiştirir."],
      ["Ortak eksenli, ideal makaralar", "Geleneksel akım yönü"],
      ["Sarım yönü (sağdan/soldan) görsel olarak kontrol edilmeli", "Dünya alanı ihmal edilmiyorsa bileşke alanda onu da say"],
      ["Parmakları akıma karşı kıvırmak", "Pusula N ucunu N kutbuna doğru çevirmek", "İçerideki yönü dışarıdaki gibi N→S almak"]),
    M(["Makara akım halkalarının dizisidir; her halka merkezinde kendi sağ el kuralıyla bir yön verir ve bu yönler eksende aynıdır, toplanır.",
       "Alan çizgileri kapalıdır: içte S→N, dışta N→S.",
       "İğne alana hizalanır; kutup yakınında pusulanın N ucu N kutbundan uzağı, S kutbuna doğru gösterir."],
      ["Statik akım"], ["Nitel"], ["Çizgileri N'den dışarı çıkıp S'de bitiyor sanıp içte kesmek"]),
    M(["Hızlı el: 'dört parmak akım yönünde kıvrılır, baş parmak N'. Pusula: N kutbunun önündeki iğnenin N ucu kutuptan uzağa bakar."],
      ["Sarımlar görünür"], ["Sarım yönü şekilde zor okunursa çizgi izleme gerekir"], ["Sarımın arka yüzü ile ön yüzünü karıştırmak"]),
    None,
    "Makara kutupları: parmaklar akım yönünde → baş parmak = N. Pusula: N kutbunun önünde iğnenin N ucu uzağa bakar. İki makara N–N karşı karşıyaysa orta nokta alanı sıfır.",
    "x ekseni üzerindeki bir makarada, sağ uçtan bakıldığında (+x tarafından, makaraya doğru bakılırken) akım saat yönünün TERSİNE akıyor. Makaranın N kutbu hangi uçtur? Sağ ucun hemen sağındaki eksen noktasına konan pusulanın N ucu nereye bakar? Aynı makaradan ikincisi sağ tarafa N–N yüz yüze konursa iki makaranın tam ortasında bileşke alan nedir?",
    ["Sağ uçtan bakınca akım saat yönünün tersine: parmaklar akımla kıvrılır, baş parmak bakan kişiye (+x) doğru → alan +x içte; N kutbu sağ uçtur.",
     "Sağ ucun sağında dışarıda alan N'den uzağa (+x): pusulanın N ucu +x'e (uzağa) bakar.",
     "N–N yüz yüze: ortada iki alan zıt yönlü ve eşit → bileşke 0."],
    "N kutbu sağ uç; pusulanın N ucu +x yönüne (makaradan uzağa) bakar; N–N yüz yüze iken orta noktada bileşke alan sıfır.",
    VEC + """
# eksen = x; halka noktaları (x, R cosφ, R sinφ): φ artarken +x tarafından bakınca saat yönünün tersi (y→z dönüşü)
def solenoid(x0, x1, nloops=20, R=0.05, flip=False):
    loops = []
    for k in range(nloops):
        x = x0 + (x1 - x0) * (k + 0.5) / nloops
        pts = [(x, R * math.cos(2 * math.pi * j / 360), R * math.sin(2 * math.pi * j / 360) * (-1 if flip else 1)) for j in range(361)]
        loops.append(pts)
    return loops
def Bsolenoid(loops, P):
    B = (0.0, 0.0, 0.0)
    for lp in loops:
        B = add(B, biot(lp, P))
    return B
S1 = solenoid(-1.0, 0.0)                              # sol makara, x in [-1, 0]
B_center = Bsolenoid(S1, (-0.5, 0.0, 0.0))
assert B_center[0] > 0 and abs(B_center[1]) < 1e-9    # içte +x: N kutbu +x ucunda
# sağ ucun hemen sağındaki eksen noktasında alan da +x (N'den uzağa): pusulanın N ucu +x'e bakar
assert Bsolenoid(S1, (0.3, 0.0, 0.0))[0] > 0
# sol ucun solunda alan +x (makaraya doğru, S'ye giriyor)
assert Bsolenoid(S1, (-1.3, 0.0, 0.0))[0] > 0
# ikinci makara sağda, N–N yüz yüze: ikinci makaranın N'si SOL ucunda olmalı → akım ters (flip)
S2 = solenoid(1.0, 2.0, flip=True)
Bmid = add(Bsolenoid(S1, (0.5, 0.0, 0.0)), Bsolenoid(S2, (0.5, 0.0, 0.0)))
assert abs(Bmid[0]) < 1e-9 * 1e3 and norm(Bmid) < 1e-6
# N–S dizilimi (aynı yönlü akım): orta noktada alan toplanır
S2b = solenoid(1.0, 2.0)
Bsum = add(Bsolenoid(S1, (0.5, 0.0, 0.0)), Bsolenoid(S2b, (0.5, 0.0, 0.0)))
assert Bsum[0] > 0 and abs(Bsum[0]) > 1e-3
# akım ters çevrilince kutuplar yer değiştirir
assert Bsolenoid(solenoid(-1.0, 0.0, flip=True), (-0.5, 0.0, 0.0))[0] < 0
""")

# ============================ FİZ.11.2.7 — Elektromıknatıslar (bilgi toplama / doğrulama / kayıt) ============================
SOLUTIONS["emag-source-and-search"] = S(
    M(["Araştırma sorusunu ve anahtar sözcükleri yaz (elektromıknatıs, kullanım alanı, vinç, kapı zili…).",
       "Kaynakları ölçütlerle değerlendir: yazar/kurum, güncellik, kaynakça, hakemli/denetimli, tarafsızlık, tutarlılık.",
       "Seçilen kaynakta anahtar sözcükleri tarayarak sorunun yanıtını içeren cümle/paragrafı bul.",
       "Aranan bilgiyi (kullanım alanı + çalışma ilkesi) kaynağın tamamına bakarak doğrula; tek cümleyi bağlamdan koparma.",
       "Bilgiyi ikinci bir bağımsız kaynakla karşılaştır."],
      ["Kaynak bilgileri ya da metin verilmiş"],
      ["Güvenilir kaynak sorunun dışına çıkabilir: ilgi de ölçüt", "Ölçütlerin ağırlığı bağlama göre değişir"],
      ["Popüler/reklam kaynağı seçmek", "Anahtar sözcüğü içeren ama soruyu yanıtlamayan paragrafı seçmek"]),
    M(["Bilginin güvenilirliği kaynağın denetlenebilirliğine dayanır; ilgili ve güvenilir kaynak birlikte aranır.",
       "Anahtar sözcük taraması aramayı hızlandırır ama anlamı kontrol edilmelidir."],
      ["Genel ağ ve kitap"], ["Nitel"], ["Başlığa bakıp içeriği okumamak"]),
    M(["Kaynak ele: yazarsız, kaynakçasız, reklam. Metinde: anahtar sözcük + 'çünkü/bu nedenle' içeren cümle çoğu zaman ilkeyi verir."],
      ["Standart soru"], ["Her zaman böyle olmayabilir"], ["Yalnız başlıkla karar vermek"]),
    None,
    "Elektromıknatıs bilgi toplama: önce kaynak ölçütleri, sonra anahtar sözcük taraması. Paragraf seçerken 'kullanım alanı' ve 'neden' birlikte geçmeli.",
    "'Elektromıknatıslar nerelerde kullanılır?' sorusu için (A) üniversite yazarlı 2021 derleme (kaynakçalı), (B) beğeni sayısı yüksek, yazarı belirsiz blog, (C) üretici firmanın ürün broşürü kaynakları var. Metin parçaları: P1 'Elektromıknatıs, akım kesilince alanı kaybettiği için vinçlerde hurda kaldırmada kullanılır.', P2 'Mıknatıslar renkli olur.', P3 'Elektromıknatıs, kapı zilinde ve hoparlörde kullanılır.' Hangi kaynak ve hangi paragraflar uygundur?",
    ["Kaynak: A (yazar, güncel, kaynakça, tarafsız).", "Anahtar sözcükler: 'elektromıknatıs' ve 'kullanılır'.", "P1 ve P3 ikisini de içerir ve ilke/uygulama verir; P2 ilgisiz."],
    "Kaynak A; paragraflar P1 ve P3.",
    """
sources = {"A": dict(yazar=1, guncel=1, kaynakca=1, tarafsiz=1, begeni=2),
           "B": dict(yazar=0, guncel=0, kaynakca=0, tarafsiz=1, begeni=9000),
           "C": dict(yazar=1, guncel=1, kaynakca=0, tarafsiz=0, begeni=40)}
crit = ["yazar", "guncel", "kaynakca", "tarafsiz"]
sc = {k: sum(v[c] for c in crit) for k, v in sources.items()}
assert max(sc, key=sc.get) == "A" and sc == {"A": 4, "B": 1, "C": 2}
sources["B"]["begeni"] = 10 ** 8
assert max(sc, key=sc.get) == "A"                 # popülerlik sıralamayı değiştirmez
paras = {"P1": "Elektromıknatıs, akım kesilince alanı kaybettiği için vinçlerde hurda kaldırmada kullanılır.",
         "P2": "Mıknatıslar renkli olur.",
         "P3": "Elektromıknatıs, kapı zilinde ve hoparlörde kullanılır."}
hits = [k for k, t in paras.items() if "elektromıknatıs" in t.lower() and "kullanılır" in t.lower()]
assert hits == ["P1", "P3"]
""")

SOLUTIONS["emag-verify-and-apply"] = S(
    M(["Elektromıknatısın gücü makara alanıyla orantılıdır: B ∝ K·i·N/L. Artırma yolları: i ↑ (pil/gerilim ↑ ya da direnç ↓), N ↑ (L sabit), L ↓ (N sabit), K ↑ (demir çekirdek).",
       "İddiayı bu bağıntıyla sına: 'akımı azaltınca güç artar' ya da 'tel rengi gücü etkiler' gibi ifadeleri ele.",
       "Etkisiz değişkenleri ayıkla: tel rengi/kaplaması, makara yarıçapı (ideal uzun makarada), pil markası.",
       "Çalışma ilkesi yorumu: akımla aç/kapa yapılabilen mıknatıs (vinç, zil, hoparlör, röle).",
       "Çelişen iki kaynakta ilkeye uyan iddiayı seç; kaynağın güncelliği ve hakemliğine de bak."],
      ["Uzun ince makara", "İdeal akım kaynağı ya da gerilim değişimi akım değişimine çevrilmiş"],
      ["Demir çekirdekte doyma vardır (sınırsız artmaz)", "Isınma ve tel direnci pratik sınırlardır", "Kaynak direnci varsa gerilim artınca akım orantılı artmayabilir"],
      ["Akımı azaltınca gücün artacağını sanmak", "Demir çekirdeğin etkisiz olduğunu sanmak", "Makara yarıçapını etkili saymak"]),
    M(["Elektromıknatıs 'akımla yapılan mıknatıs'tır: akım alan üretir, çekirdek alanı güçlendirir.",
       "Güç, sarım yoğunluğu ve akımla büyür; anahtarla açılıp kapanabilmesi uygulamayı mümkün kılar."],
      ["Statik akım"], ["Nitel"], ["Kalıcı mıknatıs ile karıştırmak"]),
    M(["Değişkenlere tek tek 'B'yi artırır mı?' diye sor: i evet, N evet, L ters, demir evet; renk, yarıçap hayır."],
      ["Standart sorular"], ["Birden çok değişken birlikte değişirse çarpanla"], ["Ters değişkeni (L) atlamak"]),
    M(["Sayısal ikinci yol: halka toplamıyla B'yi her değişiklik için hesaplayıp oranla (kitap B = 4πK·i·N/L)."],
      ["Uzun makara"], ["Program hesap sınırı koymaz; nicel yol yalnız doğrulama"], ["Doyma ihmal"]),
    "Elektromıknatıs sorusu: B ∝ iN/L ve demir çekirdek. 'Etkisiz' değişkenler: renk, yarıçap (ideal), marka. Akımı azaltmak/çekirdeği çıkarmak gücü düşürür.",
    "Bir öğrenci bir kaynakta 'elektromıknatısın kaldırma gücü tel sarımı sıklaştırılarak ve demir çekirdek konularak artar' diğerinde 'akım azaltılınca güç artar' görüyor. Hangi kaynak tutarlı? Gücü artırmak için hangileri etkilidir: (1) pil sayısını 2 katına çıkarmak (direnç sabit), (2) sarım sayısını 2 katına çıkarmak (uzunluk sabit), (3) makara yarıçapını 2 katına çıkarmak, (4) demir çekirdek koymak, (5) tel rengini değiştirmek?",
    ["B ∝ K·i·N/L: akım azalırsa B azalır; 2. kaynak ilkeyle uyumsuz.",
     "(1) V ×2 → i ×2 → B ×2 (etkili). (2) N ×2 → B ×2. (3) ideal uzun makarada etkisiz. (4) K artar → B çok artar. (5) etkisiz."],
    "1. kaynak tutarlıdır; (1), (2), (4) etkili; (3) ve (5) etkisiz.",
    """
import math
K0 = 1e-7
R = 0.003
def B(i=1.0, N=200, L=0.2, R=R, K=K0):
    s = 0.0
    for j in range(N):
        z = (j + 0.5) / N * L - L / 2
        s += K * 2 * math.pi * i * R ** 2 / (R ** 2 + z ** 2) ** 1.5
    return s
b0 = B()
eff = {}
eff["pil_x2"] = B(i=2.0) / b0                  # V iki katına: i iki katı
eff["sarim_x2"] = B(N=400) / b0                # L sabit
eff["yaricap_x2"] = B(R=2 * R) / b0
eff["demir"] = B(K=500 * K0) / b0
eff["renk"] = 1.0                               # tel rengi modelde yok
effective = {k for k, v in eff.items() if abs(v - 1) > 0.05}
assert effective == {"pil_x2", "sarim_x2", "demir"}
assert abs(eff["pil_x2"] - 2) < 1e-9 and abs(eff["sarim_x2"] - 2) < 5e-3
assert B(i=0.5) < b0                             # akım azalırsa güç azalır (2. kaynak yanlış)
""")

SOLUTIONS["emag-record-information"] = S(
    M(["Kayıt ögelerini belirle: uygulama | çalışma ilkesi (hangi değişkene dayandığı) | kaynak | doğrulama.",
       "Her uygulamayı doğru ilkeyle eşleştir: açılıp kapanabilen güçlü alan (vinç), alan–akım tepkisi (zil, hoparlör), anahtarlı kontak (röle).",
       "Etkili değişkenleri (i, N, L, çekirdek) ve etkisiz olanları (tel rengi, yarıçap) ayrı sütunlarda göster.",
       "Kaynağı belirtilmemiş ya da ilkesi yanlış eşleşen kaydı eksik say.",
       "Sunuya doğrulanmış, kaynağı belli kayıtları al."],
      ["Kayıt tablosu verilmiş"], ["Nitel"], ["İlkeyi yanlış eşleştirmek", "Kaynak yazmamak", "Etkisiz değişkeni etkili saymak"]),
    M(["Elektromıknatıs uygulamalarının ortak noktası, akımla alanı açıp kapama ve büyüklüğünü ayarlama imkânıdır.",
       "Kayıt, bu ilkeyi uygulamaya bağlayan tutarlı bir tablodur."],
      ["Elektromıknatıs uygulamaları"], ["Nitel"], ["Uygulama ile ilke sütunlarını karıştırmak"]),
    M(["Eşleştirme: 'akımla aç/kapa' → vinç/zil/röle; 'akımla değişen alan' → hoparlör."],
      ["Standart eşleştirme"], ["Yeni uygulamalarda ilkeyi ayrıca düşün"], ["Isı etkisiyle karıştırmak"]),
    None,
    "Elektromıknatıs kayıt sorusunda: uygulama → ilke → kaynak üçlüsü. Etkili değişken: i, N, L, çekirdek; etkisiz: renk, yarıçap (ideal).",
    "Tablo: vinç – akımla aç/kapa yapılabilir güçlü alan – (kaynak yok); zil – akım geçince demir çekirdek çekilir – Ders kitabı; hoparlör – değişen akımla değişen alan – Makale. Etkili değişkenler sütununda 'tel rengi' yazılmış. Hangi kayıtlar eksik/yanlıştır?",
    ["Vinç kaydında kaynak eksik.", "Tel rengi etkili değişken değildir: yanlış kayıt.", "Zil ve hoparlör kayıtları eksiksiz."],
    "Vinç kaydı (kaynak yok) ve 'tel rengi' girişi hatalıdır.",
    """
rows = [("vinç", "akımla aç/kapa yapılabilir güçlü alan", ""), ("zil", "akım geçince demir çekirdek çekilir", "Ders kitabı"),
        ("hoparlör", "değişen akımla değişen alan", "Makale")]
missing_src = [r[0] for r in rows if not r[2]]
assert missing_src == ["vinç"]
effective_vars = {"akım", "sarım sayısı", "makara boyu", "çekirdek"}
entry = {"tel rengi"}
assert entry - effective_vars == {"tel rengi"}      # etkisiz değişken etkili listesinde olamaz
""")

# ============================ FİZ.11.2.8 — Akımlı tele etki eden kuvvet ============================
SOLUTIONS["wire-force-data-model"] = S(
    M(["Tablodan tek değişkenli satır çifti seç: B ×2 → F ×2; i ×2 → F ×2; L ×2 → F ×2; sinθ değişkeni için açı değiştiren satırlar.",
       "Bağıntı: F ∝ B·i·L·sinθ (θ: akım ile alan arasındaki açı).",
       "Eksik hücre: çarpanları zincirle ve sinθ oranını ekle (30° → sin30° = 1/2 ; 90° → 1).",
       "Grafik: F–B, F–i, F–L orijinden geçen doğrular; F–θ sinüs eğrisi, F–sinθ doğrusu; θ = 0° ya da 180°'de F = 0.",
       "Birimler: B (T), i (A), L (m) → F (N)."],
      ["Tel alanda (L alandaki uzunluk)", "Düzgün alan, tek değişkenli satırlar"],
      ["Açı akım ile alan arasındadır; telin eksenle yaptığı açı değil", "Alan bölgesi dışındaki tel boyu sayılmaz"],
      ["F–θ grafiğini doğru sanmak", "Açıyı alan düzlemiyle ölçmek", "L'yi telin tamamı almak"]),
    M(["Akım taşıyan her yük alandan kuvvet görür: akım (yük sayısı/hızı) ya da tel boyu arttıkça toplam kuvvet orantılı artar.",
       "Yalnız alana dik bileşen etkilidir; paralel bileşen kuvvet vermez, bu yüzden sinθ gelir."],
      ["Düzgün alan"], ["Nitel"], ["Paralel bileşenin de kuvvet verdiğini düşünmek"]),
    M(["Her satırda F/(B·i·L·sinθ) hesapla; sabit çıkıyorsa model doğru, eksik hücreyi bu sabitle (=1) tamamla."],
      ["SI birimleri"], ["Birimler tutarsızsa sabit 1 olmaz"], ["cm kullanmak"]),
    M(["Vektör yolu: F = i·(L⃗ × B⃗) çapraz çarpımı; büyüklük i·L·B·sinθ (kitap s.235)."],
      ["Düzgün alan"], ["Program ek sınır koymaz"], ["Açıyı yanlış vektör çiftinden almak"]),
    "F tablosunda: B, i, L ile doğru orantılı; açıda sinθ (30° → 1/2). θ = 0 → F = 0. 'F–θ doğrusal' seçeneği tuzaktır; F–sinθ doğrusaldır.",
    "Düzgün alandaki akımlı telde ölçümler: (B=0,1 T, i=2 A, L=0,5 m, θ=90°) → 0,10 N; (0,2 T, 2 A, 0,5 m, 90°) → 0,20 N; (0,1 T, 4 A, 0,5 m, 90°) → 0,20 N; (0,1 T, 2 A, 0,5 m, 30°) → 0,05 N. Aynı telde B=0,3 T, i=2 A, L=0,5 m, θ=30° için F kaç N olur? θ=0° için ne olur?",
    ["Tek değişkenli çiftlerle F ∝ B, F ∝ i, F ∝ sin30° (0,05/0,10 = 1/2 = sin30°).", "Hedef: 0,10 × 3 (B) × 1/2 (sinθ) = 0,15 N.", "θ = 0° → sinθ = 0 → F = 0."],
    "0,15 N; θ = 0° için F = 0.",
    VEC + """
rows = [(0.1, 2, 0.5, 90, 0.10), (0.2, 2, 0.5, 90, 0.20), (0.1, 4, 0.5, 90, 0.20), (0.1, 2, 0.5, 30, 0.05)]
B, i, L, th, F = rows[0]
assert abs(rows[1][4] / F - 2) < 1e-9 and abs(rows[2][4] / F - 2) < 1e-9
assert abs(rows[3][4] / F - math.sin(math.radians(30))) < 1e-9
c = [F / (b * ii * l * math.sin(math.radians(t))) for b, ii, l, t, F in rows]
assert all(abs(x - 1.0) < 1e-9 for x in c)
target = 1.0 * 0.3 * 2 * 0.5 * math.sin(math.radians(30))
assert abs(target - 0.15) < 1e-9
# bağımsız: F = i L × B vektörüyle büyüklük
def Fvec(Bm, ii, l, theta_deg):
    t = math.radians(theta_deg)
    Lv = mul(l, (math.cos(t), math.sin(t), 0.0))            # tel, B (x yönünde) ile θ açısı yapıyor
    return mul(ii, cross(Lv, (Bm, 0.0, 0.0)))
assert abs(norm(Fvec(0.3, 2, 0.5, 30)) - 0.15) < 1e-9 and norm(Fvec(0.3, 2, 0.5, 0)) < 1e-12
# F–θ doğrusal değildir (sinüs): 30° → 60° için F oranı 2 değil √3
assert abs(norm(Fvec(0.3, 2, 0.5, 60)) / norm(Fvec(0.3, 2, 0.5, 30)) - 3 ** 0.5) < 1e-9
""")

SOLUTIONS["wire-force-direction-rhr"] = S(
    M(["Akım yönünü (dört parmak) ve alan yönünü belirle; kuvvet her ikisine de diktir.",
       "Sağ el kuralı: dört parmak akım yönünü gösterir, alan çizgileri avuç içinden dışarı çıkar (avuç içi alan yönüne bakar), açılan baş parmak kuvvet yönünü gösterir.",
       "Sayfaya dik alan: alan ⊙ (dışarı), akım sağa → kuvvet aşağı; alan ⊗ (içeri), akım sağa → kuvvet yukarı.",
       "Akım ya da alandan yalnız biri ters çevrilince kuvvet tersine döner; ikisi de ters çevrilirse kuvvet aynı kalır.",
       "AA kaynakta akım yönü periyodik değişir → kuvvet yönü de değişir → tel salınır (frekans = kaynak frekansı)."],
      ["Düz tel, düzgün alan", "Geleneksel akım yönü"],
      ["Tel alana paralel ise kuvvet yoktur", "Kitaptaki el tarifi (avuç/parmak) farklı anlatılabilir: ölçüt F = i·L⃗×B⃗ yönüdür"],
      ["Sol el kullanmak", "Kuvveti akım ya da alanla aynı doğrultuda çizmek", "Elektron yönünü akım almak"]),
    M(["Alan içindeki hareketli yük, hız ve alana dik bir yönde itilir; akım hareketli yükler demetidir, tel bu itmeyi toplu olarak hisseder.",
       "Kuvvet alanın ve akımın oluşturduğu düzleme diktir: bu yüzden üç vektör birbirine diktir.",
       "AA'da akım yönü değiştikçe kuvvet de yön değiştirir; tel ileri geri titreşir."],
      ["Statik alan, değişen akım"], ["Nitel"], ["Kuvvetin alan yönünde olduğunu düşünmek"]),
    M(["Sayfa düzleminde hızlı tablo: ⊙ + sağa akım → aşağı; ⊗ + sağa akım → yukarı. Akım sağa, alan sayfada yukarı ise kuvvet sayfa dışına (⊙), çünkü x̂ × ŷ = ẑ."],
      ["Eksenler sabit (x sağ, y yukarı, z sayfa dışı)"], ["Üç boyutta sıra önemli: i × B (B × i ters yön verir)"], ["Çapraz çarpım sırasını ters yazmak (B × i)"]),
    M(["Vektör yolu: F⃗ = i·L⃗ × B⃗; bileşenlerle çapraz çarpım (sağ el kuralının cebirsel karşılığı)."],
      ["Düzgün alan"], ["Program ek sınır koymaz"], ["İşaret hatası"]),
    "Yön sorusunda: üç vektör dik; akım ya da alandan biri ters → kuvvet ters, ikisi ters → aynı. Akım sağa ⊙ → aşağı; ⊗ → yukarı. AA kaynakta tel akım frekansında salınır.",
    "Sayfa düzleminde yatay bir tel boyunca akım sağa doğru akıyor. Alan sayfadan dışarı (⊙) ise telin üzerindeki kuvvet hangi yönde? Alan sayfa içine (⊗) olursa? Hem akım hem alan ters çevrilirse? Tel 50 Hz AA kaynağa bağlansa 1 saniyede kuvvet yönü kaç kez değişir?",
    ["⊙ ve sağa akım: sağ el kuralıyla kuvvet aşağı.", "⊗: kuvvet yukarı.", "İkisi de ters: kuvvet değişmez.", "50 Hz: saniyede 50 periyot, her periyotta 2 yön değişimi → 100 kez."],
    "⊙: aşağı; ⊗: yukarı; ikisi birden ters: aynı; AA'da saniyede 100 kez yön değişir.",
    VEC + """
x, y, z = (1, 0, 0), (0, 1, 0), (0, 0, 1)            # z: sayfa dışı (⊙)
Fdir = lambda i, B: cross(i, B)                     # F ∝ i × B
assert Fdir(x, z) == (0, -1, 0)                      # ⊙, akım sağa → aşağı
assert Fdir(x, (0, 0, -1)) == (0, 1, 0)              # ⊗ → yukarı
assert Fdir(mul(-1, x), (0, 0, -1)) == (0, -1, 0)    # ikisi ters → aynı
# sağ el tarifi tutarlı mı: avuç yönü (baş parmak × dört parmak) = alan yönü
F = Fdir(x, z)
palm_normal = cross(F, x)                           # baş parmak × parmaklar
assert palm_normal == z                              # alan avuç içinden çıkıyor
# F, i ve B'ye diktir
assert dot(F, x) == 0 and dot(F, z) == 0
# alan akıma paralelse kuvvet yok
assert cross(x, x) == (0, 0, 0)
# AA: 50 Hz'de akım işareti değişimi (1 s'de 100)
import math
f, N, T = 50.0, 400000, 10.0                           # 10 s boyunca say
sgn = [math.sin(2 * math.pi * f * (k + 0.5) * T / N) > 0 for k in range(N)]
changes = sum(1 for k in range(1, N) if sgn[k] != sgn[k - 1])
assert changes == 999 and (changes + 1) / T == 100.0   # saniyede 100 yön değişimi
assert Fdir(x, (0, 1, 0)) == (0, 0, 1)                 # akım sağa, alan yukarı → kuvvet sayfa dışı
""")

SOLUTIONS["wire-force-magnitude-angle"] = S(
    M(["F = B·i·L·sinθ yaz; θ akım (tel) ile alan arasındaki açıdır.",
       "Alana dik tel: θ = 90°, F = B·i·L (en büyük); alana paralel tel: F = 0.",
       "Çarpan yöntemi: F_yeni = F · (B çarpanı)(i çarpanı)(L çarpanı)(sinθ_yeni/sinθ_eski).",
       "L yalnız alan içindeki tel boyudur.",
       "Birimleri SI'ya çevir (cm → m)."],
      ["Düzgün alan, düz tel"], ["Alan dışı tel boyu sayılmaz", "Tel kıvrıksa etkin uzunluk uç noktaları birleştiren doğru parçasıdır (kitap kapsamında düz tel)"],
      ["Açıyı alan düzlemiyle ölçmek (cos yazmak)", "L'yi alanın dışındaki parçayla toplamak", "sinθ'yı unutmak"]),
    M(["Alana dik hareket eden yükler tam, paralel hareket edenler hiç kuvvet görmez; açı bunun ölçüsüdür.",
       "θ ile 180° − θ aynı sinüsü verir: aynı büyüklük, zıt yön."],
      ["Düzgün alan"], ["Nitel"], ["Açıyı yanlış çift arasından almak"]),
    M(["Önce açıya bak: 90° → 1, 30°/150° → 1/2, 0°/180° → 0. Sonra B·i·L çarpanlarını çarp."],
      ["Standart açılar"], ["Standart dışı açıda hesap gerekir"], ["30° ile 60°'yi karıştırmak"]),
    M(["Vektör yolu: |i·L⃗ × B⃗| büyüklüğünü bileşenlerle hesapla; açı gerekmez."],
      ["Düzgün alan"], ["Program ek sınır koymaz"], ["Bileşen hatası"]),
    "Akımlı tel oranında: dik → F = BiL; paralel → 0; 30° ve 150° aynı. 'Tel uzunluğu' = alandaki uzunluk. Çarpanlar çarpılır, açı çarpanı sinüsle.",
    "Düzgün B alanında alana dik duran, i akımı taşıyan L uzunluğundaki telde kuvvet F'dir. (a) i 2 katına çıkıp tel alanla 30° açı yapacak biçimde döndürülürse, (b) tel 150° yapacak biçimde döndürülürse, (c) L 3 katına çıkıp tel alana paralel hâle getirilirse, (d) alan 2 katı, L yarısı olursa kuvvet kaç F olur?",
    ["(a) 2 · sin30° = 2 · 1/2 = 1 → F.", "(b) 2 · sin150° = 1 → F.", "(c) sin0° = 0 → 0.", "(d) 2 · 1/2 = 1 → F."],
    "(a) F, (b) F, (c) 0, (d) F.",
    VEC + """
def F(Bm, i, L, theta_deg):
    t = math.radians(theta_deg)
    return norm(mul(i, cross(mul(L, (math.cos(t), math.sin(t), 0.0)), (Bm, 0.0, 0.0))))
B0, i0, L0 = 0.4, 3.0, 0.25
F0 = F(B0, i0, L0, 90)
assert abs(F0 - B0 * i0 * L0) < 1e-12
assert abs(F(B0, 2 * i0, L0, 30) / F0 - 1) < 1e-12
assert abs(F(B0, 2 * i0, L0, 150) / F0 - 1) < 1e-12
assert F(B0, i0, 3 * L0, 0) < 1e-12
assert abs(F(2 * B0, i0, L0 / 2, 90) / F0 - 1) < 1e-12
# hatalı yöntem: açıyı alan düzlemiyle ölçüp cos kullanmak 30° için √3/2 verir, yarı değil
assert abs(math.cos(math.radians(30)) - math.sin(math.radians(30))) > 0.3
""")

SOLUTIONS["wire-force-balance-dynamics"] = S(
    M(["Serbest cisim diyagramı çiz: ağırlık mg (aşağı), manyetik kuvvet BiL (yönü sağ el kuralıyla), gerilme/dinamometre/normal kuvvet/sürtünme.",
       "Denge ise ΣF = 0: dinamometre okuması D = mg − BiL (kuvvet yukarıysa) ya da D = mg + BiL (aşağıysa).",
       "Havada askıda kalma: BiL = mg → i = mg/(B·L).",
       "Raylı çubuk: manyetik kuvvet sürücüdür: a = (BiL − f)/m; sabit i için ivme sabit, d = ½at², ϑ = at.",
       "Yön: akım ya da alan ters çevrilince kuvvet ve ivme ters, dinamometre okuması mg'nin öbür tarafına geçer."],
      ["Düzgün alan, tel alana dik", "Akım sabit (rayda hareket ederken zıt EMK ünite sonuna ait olduğundan ihmal edilir)"],
      ["Çubuk hızlanınca indüksiyon etkileri doğar (bu aile onları kapsamaz)", "Sürtünme varsa fark alınır"],
      ["Kuvvet yönünü ters çizmek", "Dinamometreye kuvvetleri yanlış işaretle yazmak", "Raylı çubuğa sabit hız vermek (ivmelidir)"]),
    M(["Çubuk net kuvvet altında ivmelenir; sabit kuvvet sabit ivme demektir.",
       "Dinamometre, telin dengede olduğunu söyler: yukarı kuvvet aşağı kuvvetlere eşit.",
       "Alanın kuvveti ağırlığa eşitlenirse tel havada kalır."],
      ["Newton 1–2"], ["Nitel"], ["Kuvveti hızla karıştırmak"]),
    M(["Önce BiL'i sayısal bul, sonra mg ile karşılaştır: BiL > mg yukarı ivme; = mg dengede; < mg tele gerilme kalır."],
      ["Tek tel"], ["Birden çok tel varsa her teli ayrı"], ["Sıfırdan başlamayan ilk hız"]),
    M(["Enerji yolu (ünite 1'den): iş = F·d = ½mϑ² ile çubuğun hızı."],
      ["Sabit kuvvet, sürtünmesiz ray"], ["İvme yolu aynı sonucu verir"], ["Enerjiyi atlamak"]),
    "Dinamometre: D = mg ± BiL (yönü sağ el). Havada kalma: BiL = mg. Raylı çubuk: a = BiL/m (sürtünme varsa farkı al); sabit ivmeli kinematik.",
    "40 g kütleli, 20 cm uzunluğundaki yatay tel, B = 0,5 T'lık yatay ve tele dik bir alanda dinamometreden asılıyor; telden i = 2 A akım geçiyor ve manyetik kuvvet yukarı yönlü. Dinamometre kaç N gösterir? Akım ters çevrilirse? Telin havada asılı kalması için akım kaç A olmalı? Aynı alanda yatay, sürtünmesiz raylar üzerindeki 100 g'lık, 20 cm'lik çubuktan 2 A akım geçerse 3 s sonra çubuğun hızı ve aldığı yol kaç olur? (g = 10 m/s²)",
    ["BiL = 0,5·2·0,2 = 0,2 N; mg = 0,4 N.", "Kuvvet yukarı: D = 0,4 − 0,2 = 0,2 N; akım ters: kuvvet aşağı, D = 0,6 N.",
     "Askıda kalma: i = mg/(BL) = 0,4/(0,5·0,2) = 4 A.", "Raylı çubuk: a = 0,2/0,1 = 2 m/s²; ϑ = 2·3 = 6 m/s; d = ½·2·9 = 9 m."],
    "D = 0,2 N; ters akımda 0,6 N; i = 4 A; ϑ = 6 m/s, d = 9 m.",
    VEC + """
g = 10.0
B, L = 0.5, 0.2
m = 0.040
Fm = lambda i: B * i * L
assert abs(Fm(2) - 0.2) < 1e-12 and abs(m * g - 0.4) < 1e-12
assert abs((m * g - Fm(2)) - 0.2) < 1e-12 and abs((m * g + Fm(2)) - 0.6) < 1e-12
assert abs(m * g / (B * L) - 4.0) < 1e-12
# alan sayfa dışı (+z): akım −x ise F = i × B = +y (yukarı) — yukarı kuvvet için akımın yönü böyle seçilir
assert cross((-1, 0, 0), (0, 0, 1)) == (0, 1, 0)
# raylı çubuk: sayısal integrasyon
mr = 0.100
a = Fm(2) / mr
v = x = 0.0
dt, T = 1e-4, 3.0
for _ in range(int(T / dt)):
    v += a * dt; x += v * dt
assert abs(v - 6.0) < 1e-3 and abs(x - 9.0) < 1e-2
# enerji yolu: F·d = ½ m v²
assert abs(Fm(2) * 9.0 - 0.5 * mr * 36.0) < 1e-9
# sürtünme varsa a azalır
mu_f = 0.05
assert (Fm(2) - mu_f) / mr < a
""")

SOLUTIONS["parallel-wires-force"] = S(
    M(["Önce bir telin diğerinin yerinde oluşturduğu alanı bul: büyüklük ∝ i/d, yön sağ el kuralı (telin çevresinde dönen çemberlere teğet).",
       "Sonra bu alan içindeki ikinci telin kuvvetini bul: F = i·L·B, yönü sağ el kuralıyla (akım ve alana dik).",
       "Sonuç kuralı: AYNI yönlü akımlar birbirini ÇEKER, ZIT yönlü akımlar İTER.",
       "Etki–tepki: iki tel birbirine EŞİT büyüklükte, zıt yönde kuvvet uygular (akımlar farklı olsa da).",
       "Büyüklük: F ∝ i₁·i₂·L/d; bir akım ×2 → F ×2, uzaklık ×2 → F ×1/2 (1/d, kare yok)."],
      ["Uzun paralel teller", "Aynı ortam, tel uzunluğu L ortak"],
      ["Teller paralel değilse tork/bileşen gerekir", "Uzaklık tel boyuna göre küçük olmalı"],
      ["Aynı yönlü akımlarda iterler sanmak", "Büyük akımlı telin daha büyük kuvvet uyguladığını sanmak", "Uzaklık ilişkisini ters kare yapmak"]),
    M(["Her akım çevresinde dönen bir alan oluşturur; yan telin akımı bu alana dik olduğundan itilir ya da çekilir.",
       "Aynı yönlü akımlarda iki tel arasındaki bölgede alanlar zıt yönlü ve zayıflar: teller birbirine doğru itilir (çekim).",
       "Karşılıklı etki: her tel diğerinin alanına ve diğeri onun alanına bağlıdır; bu yüzden F₁₂ = F₂₁."],
      ["Statik akım"], ["Nitel"], ["Kuvveti tek yönlü sanmak"]),
    M(["Kısa kural: aynı yön = çekim (teller yaklaşır), zıt yön = itme (uzaklaşır); büyüklüklerde i₁·i₂/d çarpanı."],
      ["Paralel teller"], ["Ters akımlı iki tel arasında alan toplanır; yine de yön kuralı değişmez"], ["Alan ile kuvveti karıştırmak"]),
    M(["Vektör yolu: B₁ = 2K·i₁/d·(ẑ × r̂), F₂ = i₂·L·(ẑ × B₁) çapraz çarpımlarıyla sayısal doğrulama (kitap s.235)."],
      ["Uzun teller"], ["Program F = B·i·L değişken problemlerini kapsar"], ["İşaret"]),
    "Paralel teller: aynı yön çeker, zıt yön iter, kuvvetler her zaman eşit ve zıt. Büyüklükte i₁i₂/d: 'i iki katı, d iki katı' → F aynı.",
    "X ve Y telleri paralel, d aralıklı ve L uzunluğunda; X'ten i, Y'den 2i akım aynı yönde geçiyor. Teller arasındaki kuvvetin yönünü ve büyüklük karşılaştırmasını yapınız. X'in akımı 2 katına çıkarılıp d iki katına çıkarılırsa kuvvet ne olur? Y'nin akımı ters çevrilirse ne olur?",
    ["Aynı yönlü akım → teller birbirini çeker.", "Etki–tepki: X'in Y'ye uyguladığı kuvvet, Y'nin X'e uyguladığına eşit büyüklükte (akımlar farklı olsa da).",
     "i₁ ×2, d ×2 → F ∝ i₁i₂/d → 2/2 = 1 → değişmez.", "Y'nin akımı ters → zıt yönlü → teller birbirini iter (büyüklük aynı)."],
    "Aynı yönde çekim, karşılıklı kuvvetler eşit; F değişmez; Y ters olunca itme.",
    VEC + """
K = 1e-7
z = (0, 0, 1)
def forces(i1, s1, i2, s2, d, L):
    # tel1 x=0, tel2 x=d; akım yönü +z (s=+1) ya da -z; B1 = 2K i1/d (s1 ẑ × x̂); F2 = i2 L (s2 ẑ) × B1
    B1_at_2 = mul(2 * K * i1 / d, cross(mul(s1, z), (1, 0, 0)))
    F2 = mul(i2 * L, cross(mul(s2, z), B1_at_2))
    B2_at_1 = mul(2 * K * i2 / d, cross(mul(s2, z), (-1, 0, 0)))
    F1 = mul(i1 * L, cross(mul(s1, z), B2_at_1))
    return F1, F2
F1, F2 = forces(3.0, 1, 6.0, 1, 0.1, 2.0)
assert F2[0] < 0 and F1[0] > 0                         # aynı yön: çekim
assert close(F1, mul(-1, F2)) and abs(norm(F1) - 2 * K * 3.0 * 6.0 * 2.0 / 0.1) < 1e-15   # eşit ve zıt; 2K i1 i2 L/d
G1, G2 = forces(6.0, 1, 6.0, 1, 0.2, 2.0)             # i1 ×2, d ×2
assert abs(norm(G2) - norm(F2)) < 1e-15
H1, H2 = forces(3.0, 1, 6.0, -1, 0.1, 2.0)            # Y ters
assert H2[0] > 0 and H1[0] < 0 and abs(norm(H2) - norm(F2)) < 1e-15
# B ∝ 1/d: uzaklık iki katı, kuvvet yarı
assert abs(norm(forces(3.0, 1, 6.0, 1, 0.2, 2.0)[1]) / norm(F2) - 0.5) < 1e-12
""")

SOLUTIONS["loop-force-directions"] = S(
    M(["Çerçevenin her kenarı için akım yönünü ve alan yönünü yaz.",
       "Her kenara tel kuralını uygula: kuvvet yönü = akım × alan (sağ el); büyüklük i·L·B·sinθ.",
       "Alana PARALEL kenarda kuvvet yoktur (θ = 0° ya da 180°).",
       "Akım yönü ya da alan ters çevrilince tüm kenar kuvvetleri ters döner.",
       "Alan düzleme dik ise dört kenarın kuvveti çerçeve düzleminde ve ya hepsi dışa (germe) ya hepsi içe (sıkıştırma) doğrudur; net kuvvet sıfırdır."],
      ["Düzgün alan", "Dikdörtgen çerçeve, tek sarım"],
      ["Alan düzgün değilse net kuvvet sıfırdan farklı olabilir", "Çerçeve hareket ettikçe yönler değişebilir"],
      ["Paralel kenara da kuvvet yazmak", "Akım yönünü kenarlarda aynı almak (çerçevede karşılıklı kenarlarda zıttır)", "Kenar kuvvetlerini aynı yönlü çizmek"]),
    M(["Çerçeve, birbirine bağlı dört telden oluşur; karşılıklı kenarlarda akım zıt yönlü olduğundan kuvvetler zıt yönlüdür.",
       "Net kuvvet sıfır, ancak zıt kuvvetler aynı doğru üzerinde olmayabilir: döndürme etkisi oluşur (sonraki aile)."],
      ["Düzgün alan"], ["Nitel"], ["Net kuvvet sıfırsa tork da sıfırdır sanmak"]),
    M(["Önce paralel kenarları ele (kuvvet yok), sonra kalan iki kenara yön ver; karşılıkları zıt yönlüdür."],
      ["Alan çerçeve düzlemine paralel ya da dik"], ["Alan eğikse dört kenara da kuvvet olur"], ["Eğik alanı düz kabul etmek"]),
    M(["Tablo yöntemi: kenar | akım yönü | F = i × B yönü; her kenara çapraz çarpım uygulayıp tabloyu doldur."],
      ["Düzgün alan"], ["Çok sayıda durumda zaman alır"], ["Çapraz çarpım sırası"]),
    "Çerçeve kenar kuvvetleri: paralel kenar = 0; karşılıklı kenarlar zıt; alan dik → hepsi dışa ya da hepsi içe. Akım ters → hepsi ters.",
    "xy düzleminde, köşeleri (0,0), (a,0), (a,b), (0,b) olan dikdörtgen çerçeveden +z tarafından bakıldığında saat yönünün tersi akım geçiyor. (a) B +z yönünde (⊙) iken, (b) B +x yönünde iken, (c) (a)'da akım ters çevrilirse kenar kuvvetlerinin yönlerini ve kuvvetsiz kenarları belirleyiniz.",
    ["Kenarlardaki akım yönleri: alt +x, sağ +y, üst −x, sol −y.",
     "(a) B=+z: alt: x̂×ẑ = −ŷ; sağ: ŷ×ẑ = +x̂; üst: +ŷ; sol: −x̂. Dört kuvvet de çerçeveden dışa doğru; net sıfır.",
     "(b) B=+x: alt ve üst kenarlar B'ye paralel → kuvvet yok; sağ: ŷ×x̂ = −ẑ; sol: +ẑ.",
     "(c) Akım ters: (a)'daki dört kuvvet de içe doğru olur."],
    "(a) dört kenar da dışa; (b) alt ve üst kenar kuvvetsiz, sağ −z, sol +z; (c) hepsi içe.",
    VEC + """
x, y, z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
sides = {"alt": x, "sag": y, "ust": mul(-1, x), "sol": mul(-1, y)}          # saat yönünün tersi akım
def Fs(B, sign=1):
    return {k: cross(mul(sign, v), B) for k, v in sides.items()}
a = Fs(z)
assert a["alt"] == (0, -1, 0) and a["sag"] == (1, 0, 0) and a["ust"] == (0, 1, 0) and a["sol"] == (-1, 0, 0)
# dışa doğru: merkez (a/2, b/2) çerçeve kenarından uzaklaşma yönü
out = {"alt": (0, -1, 0), "sag": (1, 0, 0), "ust": (0, 1, 0), "sol": (-1, 0, 0)}
assert all(a[k] == out[k] for k in sides)
assert all(sum(a[k][j] for k in sides) == 0 for j in range(3))             # net kuvvet sıfır
b = Fs(x)
assert b["alt"] == (0, 0, 0) and b["ust"] == (0, 0, 0) and b["sag"] == (0, 0, -1) and b["sol"] == (0, 0, 1)
c = Fs(z, sign=-1)
assert all(c[k] == mul(-1, out[k]) for k in sides)                         # hepsi içe
""")

SOLUTIONS["loop-rotation-torque"] = S(
    M(["Çerçevenin her kenarındaki kuvveti bul (tel kuralı); karşılıklı kenarlarda kuvvetler eşit ve zıttır.",
       "Zıt kuvvetler aynı doğru üzerinde değilse (kol varsa) bir kuvvet çifti, yani döndürme etkisi oluşur.",
       "Döndürme etkisi: çerçeve düzlemi alana PARALEL iken en büyük (kollar maksimum), düzlem alana DİK iken sıfırdır (kuvvetler aynı doğru üzerinde, düzlemde).",
       "Etkiyi artıran etmenler: akım i, sarım sayısı N, alan B, çerçeve alanı A (τ_maks ∝ N·i·B·A).",
       "Dönme yönü: kuvvet çiftinin yönünden belirlenir; alan ya da akım ters → dönme ters."],
      ["Düzgün alan", "Çerçeve alana dik bir eksen etrafında dönebilir"],
      ["Program tork formülü kullandırmaz: nitel etmen ilişkisi; τ_maks = N·i·B·A kitapta yok ya da kapsamda sayısal değil", "Alan yoksa çerçeve kendiliğinden dönmez"],
      ["Net kuvvet sıfır olduğu için dönmeyeceğini sanmak", "Düzlem alana dikken döndürme etkisinin en büyük olduğunu sanmak", "Dönme eksenini alana paralel almak"]),
    M(["Kuvvet çifti, çerçeveyi öteleme yaptırmadan döndürür: iki zıt kuvvet farklı doğrular üzerindedir.",
       "Çerçeve alana dik düzleme geldiğinde kuvvetler çerçeve düzleminde ve aynı doğru üzerinde olur: döndürme sıfır.",
       "Galvanometrede yay, döndürme etkisini dengeler: sapma akımla orantılı."],
      ["Düzgün alan"], ["Nitel"], ["Kuvveti dönme eksenine uzaklıkla ilişkilendirmemek"]),
    M(["Kontrol: düzlem ∥ alan → en büyük; düzlem ⊥ alan → sıfır. Etmenlerin hepsi doğru orantılı artırır (N, i, B, A)."],
      ["Düzgün alan"], ["Eksen konumu önemli"], ["Konumu ters seçmek"]),
    M(["Vektör yolu: τ = m × B, m = N·i·A·n̂ (manyetik moment); τ büyüklüğü N·i·A·B·sinφ (φ: normal ile B arası)."],
      ["Düzgün alan"], ["Program hesaplamayı dışlayabilir; ikinci yol kontrol amaçlı"], ["φ ile düzlem açısını karıştırmak"]),
    "Çerçeve dönmesi: düzlem alana paralel → döndürme en büyük, dik → sıfır. Etkiyi N, i, B, A artırır. Alan sıfırsa dönme yok.",
    "Alan +x yönünde olan düzgün bölgede, xy düzleminde bulunan dikdörtgen çerçeveden (alanı A, sarım sayısı N) saat yönünün tersi (+z'den bakışla) i akımı geçiyor. Çerçeve hangi eksen etrafında döner? Çerçeve düzlemi alana dik hâle gelince döndürme etkisi nedir? Döndürme etkisini artırmak için ne yapılır? (N=50, i=0,2 A, A=4 cm², B=0,1 T için en büyük döndürme etkisi hesaplanabilir.)",
    ["Alana paralel kenarlar kuvvet görmez; kalan iki kenarda kuvvetler ±z yönlüdür → y ekseni etrafında kuvvet çifti.",
     "Düzlem alana dik olunca kuvvetler çerçeve düzleminde ve zıt: döndürme sıfır (denge).", "N, i, B, A artırılırsa etki artar.",
     "τ_maks = N·i·A·B = 50·0,2·4×10⁻⁴·0,1 = 4×10⁻⁴ N·m."],
    "y ekseni etrafında; düzlem alana dik olunca sıfır; etkiyi N, i, B, A artırır; τ_maks = 4×10⁻⁴ N·m.",
    VEC + """
def torque(N, i, a, b, B, phi_deg):
    # dikdörtgen çerçeve (kenarlar a ve b), merkezde; çerçeve normali (cosφ, ... ) alana (x) göre φ açısı yapıyor.
    phi = math.radians(phi_deg)
    n = (math.cos(phi), 0.0, math.sin(phi))                  # normal, x–z düzleminde; dönme ekseni y
    u = (0.0, 1.0, 0.0)                                      # çerçeve düzleminde y yönü (kenar b boyunca)
    v = cross(n, u)                                          # düzlemde diğer yön (kenar a boyunca)
    corners = [add(add(mul(a / 2, v), mul(b / 2, u)), (0, 0, 0)),
               add(add(mul(-a / 2, v), mul(b / 2, u)), (0, 0, 0)),
               add(add(mul(-a / 2, v), mul(-b / 2, u)), (0, 0, 0)),
               add(add(mul(a / 2, v), mul(-b / 2, u)), (0, 0, 0))]
    tau = (0.0, 0.0, 0.0)
    for k in range(4):
        p, q = corners[k], corners[(k + 1) % 4]
        dl = sub(q, p); mid = mul(0.5, add(p, q))
        F = mul(N * i, cross(dl, (B, 0.0, 0.0)))
        tau = add(tau, cross(mid, F))
    return tau, n
a, b = 0.02, 0.02           # A = 4 cm²
t0, n0 = torque(50, 0.2, a, b, 0.1, 90)        # normal alana dik → düzlem alana paralel
assert abs(norm(t0) - 4e-4) < 1e-12 and abs(t0[0]) < 1e-15 and abs(t0[2]) < 1e-15   # y ekseni etrafında, en büyük
t1, _ = torque(50, 0.2, a, b, 0.1, 0)          # normal alana paralel → düzlem alana dik
assert norm(t1) < 1e-15
# genel: |τ| = N i A B sin(φ), φ normal ile alan arası
for phi in (10, 30, 60, 90, 120, 170):
    t, _ = torque(50, 0.2, a, b, 0.1, phi)
    assert abs(norm(t) - 4e-4 * math.sin(math.radians(phi))) < 1e-12
# etmen ölçekleme
assert abs(norm(torque(100, 0.2, a, b, 0.1, 90)[0]) / norm(t0) - 2) < 1e-9
assert abs(norm(torque(50, 0.2, 2 * a, b, 0.1, 90)[0]) / norm(t0) - 2) < 1e-9
assert abs(norm(torque(50, 0.2, a, b, 0.0, 90)[0])) < 1e-15            # alan yoksa dönme yok
""")

SOLUTIONS["motor-principle-evaluation"] = S(
    M(["Metni ve modeli (şekil) oku; her çıkarım cümlesini 'metin/model bunu söylüyor mu?' diye sına.",
       "Çalışma ilkesi: akımlı çerçeve alanda kuvvet çifti görür → döner; elektrik enerjisi hareket enerjisine dönüşür (bir kısmı ısıya).",
       "Sürekli dönüş için çerçeve yarım tur döndüğünde akım yönü değişmelidir; değişmezse kuvvet çifti ters döner ve çerçeve salınır/denge konumunda kalır.",
       "Motor ile jeneratör ilkesi birbirinin tersidir (hareket enerjisi → elektrik); hibrit/elektrikli araçta frenleme sırasında motor jeneratör gibi çalışabilir.",
       "Karşılaştırma sorularında (elektrikli araç/içten yanmalı) verilen verilere dayanan yargıyı seç; veriyle desteklenmeyen genellemeyi ele."],
      ["Basit motor modeli", "Metin ya da tablodaki verilerle sınırlı çıkarım"],
      ["Program komütatör/fırça ayrıntılarına girmez; 'akım yönü değişmeli' gerekçesi yeterlidir", "Verim sayıları metinden okunur, hesaplanmaz"],
      ["Motorun elektrik ürettiğini sanmak", "Verimi %100 sanmak", "Veriyle desteklenmeyen genelleme yapmak"]),
    M(["Kuvvet çifti çerçeveyi alana dik düzleme getirir ve orada durdurur (denge). Dönüşü sürdürmek için kuvvet çiftinin yönü tam o anda tersine çevrilmelidir.",
       "Enerji korunur: giren elektrik enerjisi = mekanik enerji + ısı kaybı."],
      ["Basit motor"], ["Nitel"], ["Dengeyi dönmeye engel saymamak"]),
    M(["Üç hızlı test: (1) akım yönü değişiyor mu? (2) enerji hangi yönde dönüşüyor? (3) cümle veriye dayanıyor mu?"],
      ["Çıkarım soruları"], ["Her çıkarım için ayrı test"], ["Testleri atlamak"]),
    None,
    "Motor sorularında anahtar: yarım tur sonra akım yönü değişmeli (sürekli dönüş). Elektrik → hareket (+ısı). Veriye dayanmayan genellemeler yanlış.",
    "Alan içinde dönebilen bir çerçeveden geçen akımın yönü hiç değişmiyor. Çerçeve sürekli döner mi? Akım yönü her yarım turda değişirse ne olur? Bir öğrenci 'motor mekanik enerjiyi elektrik enerjisine çevirir' diyor; bu çıkarım doğru mudur?",
    ["Sabit yönlü akımda kuvvet çifti çerçeveyi alana dik denge konumuna getirir ve oraya yerleşir: sürekli dönmez, salınarak durur.",
     "Her yarım turda akım yönü değişirse kuvvet çifti hep aynı yönde döndürür: sürekli dönme.",
     "Motor elektrik enerjisini hareket enerjisine çevirir: öğrencinin çıkarımı yanlıştır (jeneratör ters işlem)."],
    "Sürekli dönmez; akım yönü her yarım turda değişince sürekli döner; çıkarım yanlış.",
    """
import math
def simulate(commutator, T=40.0, dt=1e-3):
    # θ: çerçeve normalinin alanla açısı; τ = -c sinθ (denge θ = 0: düzlem alana dik); sürtünme γ
    c, gamma = 20.0, 1.0
    th, w = math.pi / 2, 0.0         # başlangıç: düzlem alana paralel (en büyük tork)
    total = 0.0
    max_th = th; min_th = th
    for _ in range(int(T / dt)):
        s = abs(math.sin(th)) * (-1.0) if commutator else -math.sin(th)    # komütatör: tork hep aynı yönde
        a = c * s - gamma * w
        w += a * dt; th += w * dt
        total += w * dt
        max_th = max(max_th, th); min_th = min(min_th, th)
    return th, w, total, max_th, min_th
th, w, tot, mx, mn = simulate(False)
assert abs(th) < 1e-3 and abs(w) < 1e-3 and mx - mn < math.pi            # denge konumuna yerleşir, ≤ yarım tur salınım
th2, w2, tot2, mx2, mn2 = simulate(True)
assert tot2 < -20 * math.pi and w2 < -1                                  # sürekli aynı yönde döner (>10 tur)
# enerji dönüşümü: elektrik giriş = mekanik + ısı; verim < 1
P_el, P_heat = 100.0, 8.0
assert (P_el - P_heat) / P_el < 1
""")

# ============================ FİZ.11.2.10 — Manyetik akı (kavramsal: oran / nitel) ============================
SOLUTIONS["flux-factors-analogy"] = S(
    M(["Analojiyi eşleştir: boya (ya da macun/yağmur) = alan çizgileri; kâğıt (şemsiye/pencere) = yüzey; boya yoğunluğu = B; yüzeyden geçen boya miktarı = akı.",
       "Akı üç şeye bağlıdır: alan şiddeti (çizgi sıklığı), yüzey alanı ve yüzeyin alana göre konumu (açı).",
       "Alan şiddeti ve yüzey alanı arttıkça akı artar; yüzey alana paralel (çizgilere yan) olunca akı sıfırdır, dik tutulunca en büyüktür.",
       "Analojinin sınırı: gerçek alan çizgisi 'madde' değildir; hareket etmez, tükenmez.",
       "Simülasyonda B, alan ve açıyı tek tek değiştirerek hangisinin akıyı değiştirdiğini kaydet (kontrol değişkeni)."],
      ["Yüzey düz ve alan düzgün", "Analoji yüzeyden geçen çizgi sayısı fikrini aktarır"],
      ["Program akıyı yalnız kavramsal tanıtır (formülle hesap yok)", "Analoji nicel çıkarım için kullanılmaz"],
      ["Akıyı alan çizgisinin kendisi sanmak", "Yüzey alana paralelken akının en büyük olduğunu sanmak", "Yalnız B'ye bağlı sanmak"]),
    M(["Akı, yüzeyden 'kaç çizgi geçiyor?' sorusunun cevabıdır; çizgi sayısı yüzeyin alana dik izdüşümüne ve çizgi sıklığına bağlıdır.",
       "Yan duran yüzey (alana paralel) çizgileri kesmez, akı sıfırdır."],
      ["Düz yüzey"], ["Nitel"], ["Yüzeyi alan çizgisine paralel eğmenin akıyı artırdığını sanmak"]),
    M(["Sırala: B ↑ → akı ↑; A ↑ → akı ↑; yüzey alana dik → en büyük; paralel → sıfır."],
      ["Standart soru"], ["Yön işareti (akı +/−) program dışı"], ["Açıyı yanlış almak"]),
    M(["Sayma yolu: 2B modelde çizgileri sayarak yüzeyin kestiği çizgi sayısının B·ℓ·cosθ ile orantılı olduğunu gör (kitap Φ = B·A·cosθ, kavramsal)."],
      ["Düzgün alan"], ["Program akıyı hesaplatmaz; kitapta formül var"], ["θ'yı düzlemle ölçmek"]),
    "Analoji sorusunda: 'boya yoğunluğu = B, kâğıt = yüzey, kâğıdı rüzgâra çevirince boya azalır (açı)'. Akı: B, A, açı. Paralel yüzeyde akı sıfır.",
    "Püskürtme boya analojisinde tabancadan çıkan düzgün boya akışını alan çizgileri, kâğıdı yüzey, kâğıt üzerinde biriken boya miktarını akı olarak alalım. Boya miktarını artırmak için (a) kâğıdı büyütmek, (b) tabancanın boya yoğunluğunu artırmak, (c) kâğıdı akış yönüne paralel döndürmek, (d) kâğıdı akışa dik tutmak ne etki yapar? Analojinin sınırı nedir?",
    ["(a) Alan büyür, akı artar. (b) Yoğunluk (B) artar, akı artar.", "(c) Paralel tutulan kâğıt çizgileri kesmez: akı sıfır; (d) dik tutulan kâğıtta akı en büyük.",
     "Sınır: alan çizgileri gerçek madde değildir; modeldir."],
    "(a) artar, (b) artar, (c) sıfır, (d) en büyük; analoji çizgileri maddeleştirir (sınır).",
    """
import math
# yüzeyden geçen çizgi sayısı: düşey alan çizgileri x ekseninde yatay aralık s ile dizili; yüzey: uzunluğu ℓ, yatayla α açısı yapan doğru parçası
def crossings(B_density, ell, alpha_deg, x0=0.0):
    s = 1.0 / B_density                              # çizgiler arası yatay mesafe
    a = math.radians(alpha_deg)
    x1 = x0 + ell * math.cos(a)
    lo, hi = min(x0, x1), max(x0, x1)
    return math.floor(hi / s + 1e-12) - math.ceil(lo / s - 1e-12) + 1 if hi >= lo else 0
ell = 40.0
base = crossings(2.0, ell, 0.0)                      # yüzey alana dik (normal alanla paralel): α=0 yatay yüzey
assert abs(base - 2.0 * ell) <= 1                  # ≈ B·ℓ
assert abs(crossings(2.0, 2 * ell, 0.0) - 2 * base) <= 2          # (a) alan büyür
assert abs(crossings(4.0, ell, 0.0) - 2 * base) <= 2              # (b) yoğunluk artar
assert crossings(2.0, ell, 90.0) <= 1                              # (c) yüzey çizgilere paralel: ≈ sıfır (sınır çizgisi hariç)
assert crossings(2.0, ell, 0.0) > crossings(2.0, ell, 60.0) > crossings(2.0, ell, 85.0)   # eğildikçe azalır
# sayı ≈ B ℓ cosα
for a in (0, 30, 60):
    assert abs(crossings(2.0, ell, a) - 2.0 * ell * math.cos(math.radians(a))) <= 2
""")

SOLUTIONS["flux-relationship-qualitative"] = S(
    M(["Akı için üç etmeni yaz: alan B (çizgi sıklığı), yüzey alanı A ve yüzey normali ile alan arasındaki açı (yüzeyin duruşu).",
       "Her işlemi sorgula: B artıyor mu, A artıyor mu, yüzey çizgilere daha mı dik/daha mı paralel oluyor? Buna göre akı artar/azalır/değişmez.",
       "Yüzey normali ekseni etrafında dönmek akıyı değiştirmez; normali alandan uzaklaştıran eğme akıyı azaltır; alan çizgilerine paralel yüzeyde akı sıfırdır.",
       "Tablo sorularında tek değişkenli satır çiftlerinden orantı çıkar: B ×2 → akı ×2, A ×2 → akı ×2, açı büyüdükçe azalır.",
       "Alan dışında kalan yüzey parçası akıya katkı vermez."],
      ["Düz yüzey, düzgün alan"],
      ["Program akıyı kavramsal ele alır; Φ = B·A·cosθ (θ: normal–alan açısı) kitapta var, sayısal kullanım programda yok", "Alan düzgün değilse yüzeyin yeri de önemlidir"],
      ["Yüzeyi normali etrafında döndürmenin akıyı değiştirdiğini sanmak", "Açıyı yüzey ile alan arasında ölçüp cos kullanmak", "Yüzey alana paralelken akıyı en büyük sanmak"]),
    M(["Akı, yüzeyi kesen alan çizgilerinin sayısıyla orantılıdır; her işlemin bu sayıyı nasıl etkilediğini düşün.",
       "Yüzey normali etrafında dönünce yüzey aynı çizgileri keser; çizgilere göre eğilince keser sayı azalır."],
      ["Düz yüzey"], ["Nitel"], ["Dönmeyi eğme ile karıştırmak"]),
    M(["Beş sorulu liste: B↑ → ↑, A↑ → ↑, normal etrafında dönme → değişmez, normali alandan uzaklaştıran eğme → ↓, paralel → 0."],
      ["Standart yargılar"], ["Mıknatısa yaklaştırmada (çizgiler seyrekse) dikkat"], ["Yaklaşma ile alan artışını karıştırmak"]),
    M(["Formül yolu (kitap): Φ = B·A·cosθ ile her işlemde oranı hesapla; program bunu yalnız kontrol amaçlı kullanır."],
      ["Düz yüzey"], ["Program hesaplamayı dışlar; kitapta var (s.262)"], ["θ'nın tanımı"]),
    "Akı sorularında B, A ve açı: normal etrafında dönüş değişmez; eğme azaltır (normal–alan açısı büyür); paralel → sıfır. Tabloda tek değişkenli satır çifti.",
    "Düzgün alan içinde alana dik duran bir çerçevenin akısı Φ'dir. (I) Alan 2 katına çıkarılır, (II) yüzey alanı 3 katına çıkarılır, (III) çerçeve kendi normali etrafında döndürülür, (IV) çerçeve 60° eğilir (normal ile alan arası 60° olur), (V) çerçeve alan çizgilerine paralel getirilir. Akı nasıl değişir? Tablo: (B=2, A=1, θ=0°) için Φ=2; (4, 1, 0°) → 4; (2, 3, 0°) → 6; (2, 1, 60°) → 1 ise (4, 3, 60°) için Φ kaçtır?",
    ["(I) ×2; (II) ×3; (III) değişmez; (IV) ×1/2 (azalır); (V) sıfır.", "Tablodan: Φ ∝ B, Φ ∝ A; 60°'de faktör 1/2.", "(4, 3, 60°): 2 × 2 × 3 × 1/2 = 6."],
    "I: 2Φ, II: 3Φ, III: değişmez, IV: Φ/2, V: 0; tablo değeri 6.",
    VEC + """
flux = lambda B, A, th: B * A * math.cos(math.radians(th))
F0 = flux(1.0, 1.0, 0.0)
assert abs(flux(2.0, 1.0, 0) / F0 - 2) < 1e-12 and abs(flux(1.0, 3.0, 0) / F0 - 3) < 1e-12
assert abs(flux(1.0, 1.0, 60) / F0 - 0.5) < 1e-12 and abs(flux(1.0, 1.0, 90) / F0) < 1e-12
# normal etrafında dönme: kenar vektörlerini normal ekseni etrafında döndür (Rodrigues), normal ve akı değişmez
def rodrigues(v, axis, ang):
    c, sn = math.cos(ang), math.sin(ang)
    return add(add(mul(c, v), mul(sn, cross(axis, v))), mul(dot(axis, v) * (1 - c), axis))
th = math.radians(60)
n0 = (math.sin(th), 0.0, math.cos(th))                 # B = +z; normal ile alan arası 60°
e1 = (math.cos(th), 0.0, -math.sin(th)); e2 = (0.0, 1.0, 0.0)   # çerçeve düzleminde dik kenarlar
assert close(cross(e1, e2), n0)
Bv = (0.0, 0.0, 2.0)
phi0 = dot(Bv, cross(e1, e2))                          # akı = B · (alan vektörü)
for ang in (0.3, 1.0, 2.5, 4.0):
    f1, f2 = rodrigues(e1, n0, ang), rodrigues(e2, n0, ang)
    assert close(cross(f1, f2), n0, 1e-9)               # normal değişmedi
    assert abs(dot(Bv, cross(f1, f2)) - phi0) < 1e-9    # akı değişmedi
# eğme (normali alandan uzaklaştırma) akıyı azaltır
n_tilt = (math.sin(math.radians(80)), 0.0, math.cos(math.radians(80)))
assert dot(Bv, n_tilt) < phi0
# tablo
rows = [(2, 1, 0, 2.0), (4, 1, 0, 4.0), (2, 3, 0, 6.0), (2, 1, 60, 1.0)]
assert all(abs(flux(B, A, t) - v) < 1e-9 for B, A, t, v in rows)
assert abs(flux(4, 3, 60) - 6.0) < 1e-9
# hatalı yöntem: normal–alan açısı yerine sin kullanmak 60° için 0,87 verir (gerçek 0,5)
assert abs(math.sin(math.radians(60)) - flux(1, 1, 60)) > 0.3
""")

SOLUTIONS["flux-change-in-motion"] = S(
    M(["Her halka için üç niceliği izle: B (halkanın bulunduğu yerde), yüzey alanının alan içinde kalan kısmı ve yüzey normali ile alan arasındaki açı.",
       "Bu üçünden en az biri zamanla değişiyorsa akı değişir; hiçbiri değişmiyorsa akı sabittir.",
       "Düzgün alanda alan içinde ötelenen halka: B, A ve açı sabit → akı sabit. Alan içinde salınan sarkaç ya da yay sarkacı: normal alana göre dönmüyorsa sabit.",
       "Alan dışına çıkan/giren halka: alan içindeki alan değişir → akı değişir.",
       "Halka alana dik bir eksen etrafında dönüyorsa açı sürekli değişir: akı periyodik değişir (normal alana paralelken en büyük, dik iken sıfır)."],
      ["Düzgün alan", "Alan sınırları belli"],
      ["Düzgün olmayan alanda ötelenme de akıyı değiştirir", "Program akıyı kavramsal ele alır"],
      ["Hareket var diye akı değişir sanmak", "Dönmeyi yalnız eksene bakarak yorumlamak (eksen alana paralelse akı sabit)", "Alan dışına çıkışı atlamak"]),
    M(["Akı, yüzeyi kesen çizgi sayısı; hareket çizgi sayısını değiştirmiyorsa akı sabittir.",
       "Dönen halka sürekli farklı açıyla çizgileri keser: akı değişir."],
      ["Düzgün alan"], ["Nitel"], ["Hareket ile akı değişimini özdeşleştirmek"]),
    M(["Hızlı test: 'normal alana göre dönüyor mu? Halka alan sınırından geçiyor mu? Alan düzgün mü?' Üçü de 'hayır' ise akı sabit."],
      ["Standart soru"], ["Eksen konumu önemli"], ["Eksenin alana paralel olduğu özel durumu atlamak"]),
    None,
    "Hareket eden halka: akı değişmesi için B, A ya da açı değişmeli. Alan içinde ötelenme/salınım (normal sabit) → akı sabit; dönme (eksen ⊥ alan) → periyodik; alandan çıkış → azalma.",
    "Düzgün, sayfa içine bakan bir alanda üç özdeş halka hareket ediyor: (1) halka basit sarkaç gibi alan içinde salınıyor (yüzeyi sayfaya paralel kalıyor), (2) halka yay sarkacı gibi alan içinde düşeyde salınıyor, (3) halka sayfa düzleminde bir düşey eksen etrafında dönüyor. Bir periyotta hangisinde akı değişir? Halka alanın dışına çıkarsa ne olur?",
    ["(1) ve (2): halka alan içinde ötelenmekte, yüzey normali ve alan sabit → akı sabit.", "(3): yüzey normali alanla sürekli değişen açı yapıyor → akı periyodik değişir.",
     "Alandan çıkış: alan içindeki yüzey azalır → akı azalır."],
    "Yalnız (3)'te akı değişir; alandan çıkışta akı azalır.",
    """
import math
B0, A0 = 1.0, 0.01
# (1) ve (2): öteleme, normal sabit
def phi_translate(t):
    return B0 * A0 * 1.0
assert all(abs(phi_translate(t) - B0 * A0) < 1e-15 for t in (0.0, 0.1, 0.5, 1.0))
# (3) dönme: normal ile alan açısı θ = ωt
T = 2.0
w = 2 * math.pi / T
phi_rot = lambda t: B0 * A0 * math.cos(w * t)
vals = [phi_rot(T * k / 8) for k in range(9)]
assert max(vals) - min(vals) > 0.019                          # akı gerçekten değişiyor
assert abs(phi_rot(0) - B0 * A0) < 1e-15 and abs(phi_rot(T / 4)) < 1e-12 and abs(phi_rot(T / 2) + B0 * A0) < 1e-12
# alan sınırından çıkış: alan içinde kalan yüzey oranı azalır
def phi_exit(x, side=0.1):               # kare halka, sol kenar x konumunda; alan x<=0.1 tarafında (sağ yarı düzlem)
    inside = max(0.0, min(side, side - x)) if x > 0 else side
    return B0 * side * inside
assert phi_exit(0.0) > phi_exit(0.04) > phi_exit(0.1) and phi_exit(0.1) == 0.0
# periyot (kitap: f = 1/T) ve bir periyotta iki sıfır geçişi
zero_cross = sum(1 for k in range(1, 4001) if phi_rot(T * (k - 1) / 4000) * phi_rot(T * k / 4000) < 0)
assert zero_cross == 2
""")

# ============================ FİZ.11.2.11 — Elektromanyetik indüksiyon ============================
SOLUTIONS["induction-experiment-factors"] = S(
    M(["Deneyde akının nerede, nasıl değiştiğini belirle: mıknatıs–bobin hareketi ya da komşu devrede akım değişimi.",
       "Akı değişiyorsa indüksiyon gerilimi ve (devre kapalıysa) akım oluşur; akı sabitse (mıknatıs durunca, sabit akımda) ibre sapmaz.",
       "Yön: yaklaşırken bir yöne, uzaklaşırken ters yöne sapma; anahtar kapanırken bir yöne, açılırken ters yöne.",
       "Büyüklük birim zamandaki akı değişimiyle orantılıdır: daha hızlı hareket, daha güçlü mıknatıs, daha çok sarım → büyük sapma.",
       "Veri tablosunda tek değişkenli satır çifti seç ve çarpanları zincirle."],
      ["Kapalı devre (akım için)", "Birim zamandaki akı değişimi okunabiliyor"],
      ["Program tüm hesapları nitel tutabilir; ε = N·ΔΦ/Δt oran düzeyinde", "İki devreli düzenekte akı değişimi akımın değişmesine bağlıdır, büyüklüğüne değil"],
      ["Güçlü mıknatıs durduğunda da akım oluşur sanmak", "Sabit akımlı komşu devrede ε beklemek", "Sapma yönünün hareket yönünden bağımsız olduğunu sanmak"]),
    M(["İndüksiyon, değişimin tepkisidir: değişim olmazsa tepki olmaz.",
       "Değişim ne kadar hızlıysa (kısa sürede çok akı), tepki o kadar büyüktür.",
       "Yaklaşma ile uzaklaşma zıt değişimler olduğundan zıt tepkiler verir."],
      ["Kapalı iletken devre"], ["Nitel"], ["Akının büyüklüğü ile değişimini karıştırmak"]),
    M(["Ters kısayol: sapma var mı? → akı değişiyor mu? Yön ters mi? → değişim ters mi? Büyük sapma → hızlı/güçlü/çok sarım."],
      ["Standart deneyler"], ["Direnç değişimi sapma büyüklüğünü ayrıca etkiler"], ["Direnci hesaba katmamak"]),
    None,
    "İndüksiyon deneyi: değişim yoksa tepki yok; değişim hızı büyükse sapma büyük; yaklaşma/uzaklaşma ve açma/kapama zıt yönde. Tabloda hız × güç × sarım çarpımı.",
    "Bir bobine mıknatıs yaklaştırılıyor ve ibre sapmaları kaydediliyor: (hız 10 cm/s, normal mıknatıs, N=100) → 2 bölme; (20 cm/s, normal, 100) → 4; (10 cm/s, 2 kat güçlü, 100) → 4; (10 cm/s, normal, 200) → 4. (30 cm/s, 2 kat güçlü, 100) için sapma kaç bölme olur? Mıknatıs bobinin içinde durursa ne olur? Anahtarlı iki devreli düzenekte anahtar kapanırken, sabitken ve açılırken ibre ne yapar?",
    ["Tek değişkenli satırlar: sapma hızla, mıknatıs gücüyle ve N ile doğru orantılı.", "(30, 2×, 100): 2 × 3 × 2 = 12 bölme.", "Durunca akı sabit → sapma yok.",
     "Kapanırken akım artar → akı artar → bir yöne sapma; sabitken 0; açılırken ters yöne sapma."],
    "12 bölme; durunca 0; kapanırken bir yöne, sabitken 0, açılırken ters yöne.",
    """
import math
rows = [(10, 1, 100, 2.0), (20, 1, 100, 4.0), (10, 2, 100, 4.0), (10, 1, 200, 4.0)]
c = rows[0][3] / (rows[0][0] * rows[0][1] * rows[0][2])
assert all(abs(c * v * g * n - s) < 1e-9 for v, g, n, s in rows)
assert abs(c * 30 * 2 * 100 - 12.0) < 1e-9
# ε = −N dΦ/dt: mıknatıs bobine sabit hızla yaklaşırken (Φ doğrusal artıyor) ve durunca
def eps(Nt, phi, t, dt=1e-4):
    return -Nt * (phi(t + dt) - phi(t - dt)) / (2 * dt)
v = 0.10
phi_move = lambda t: 1e-3 * min(t * v / 0.05, 1.0)       # 5 cm'de doyar (içeri girince)
assert eps(100, phi_move, 0.2) < 0 and abs(eps(100, phi_move, 0.2) + 100 * 1e-3 * v / 0.05) < 1e-6
assert abs(eps(100, phi_move, 0.9)) < 1e-9                # durunca (akı sabit) ε = 0
assert abs(eps(200, phi_move, 0.2) / eps(100, phi_move, 0.2) - 2) < 1e-9
# iki devre: akım i(t) = I0 (1 - e^{-t/τ}) kapanırken, sonra sabit, sonra açılırken e^{-t/τ} ile sönüm: ε ∝ -di/dt
I0, tau = 1.0, 0.05
def i_t(t):
    if t < 1.0: return I0 * (1 - math.exp(-t / tau))
    if t < 2.0: return I0 * (1 - math.exp(-1.0 / tau))
    return I0 * (1 - math.exp(-1.0 / tau)) * math.exp(-(t - 2.0) / tau)
e = lambda t: -(i_t(t + 1e-5) - i_t(t - 1e-5)) / 2e-5
assert e(0.02) < 0 and abs(e(1.5)) < 1e-6 and e(2.02) > 0       # kapanırken −, sabitken 0, açılırken +
# R1 iki katı → son akım yarı → toplam akı değişimi (ibrenin toplam sapması) yarı
dt = 1e-4
tot = lambda I: sum(-(I * (1 - math.exp(-(k + 1) * dt / tau)) - I * (1 - math.exp(-k * dt / tau))) for k in range(int(1.0 / dt)))
assert abs(tot(0.5) / tot(1.0) - 0.5) < 1e-9
""")

SOLUTIONS["induction-emf-ratio-calc"] = S(
    M(["Akıyı bul: Φ = B·A (alana dik yüzey, cosθ = 1); A = yüzey alanı (daire için πr², kare için a²).",
       "Akı değişimi: ΔΦ = Φ_son − Φ_ilk (ya da B değişiminden ΔB·A).",
       "İndüksiyon gerilimi (büyüklük): ε = N·|ΔΦ|/Δt.",
       "Devre kapalıysa akım: i = ε/R.",
       "Oran sorularında çarpan: ε ∝ N·ΔΦ/Δt (N ×2 → ε ×2; Δt ×2 → ε ×1/2; ΔΦ ×3 → ε ×3).",
       "Alan yönü ters dönerse ΔΦ = 2·B·A olur (sıfır değil)."],
      ["Düzgün alan, tek sarımlı akı her sarıma aynı", "ΔΦ/Δt sabit ya da ortalama değer sorulur"],
      ["ε anlık değilse ortalama değerdir", "Akı sabitse ε = 0 (alan büyük olsa da)", "Alanın yüzeye dik bileşeni yoksa Φ = 0"],
      ["Φ yerine ΔΦ'yi atlamak", "N'yi unutmak", "Alanı ters çevirme durumunda ΔΦ = 0 sanmak", "cm²'yi m²'ye çevirmemek"]),
    M(["ε, birim sürede çerçeveden geçen akının değişimidir: hızlı değişim büyük gerilim.",
       "N sarım seri bağlı gerilim kaynakları gibi toplanır: ε ∝ N.",
       "Akım, devredeki gerilim ve dirençten Ohm yasasıyla gelir; ε olmasa akım olmaz."],
      ["Kapalı devre"], ["Açık devrede ε var, akım yok"], ["ε ile i'yi karıştırmak"]),
    M(["Oran kısayolu: ε_yeni = ε · (N çarpanı)(ΔΦ çarpanı)/(Δt çarpanı); i_yeni = ε_yeni/R."],
      ["Aynı devre"], ["R değişiyorsa akım ayrıca"], ["Δt'yi çarpan yerine bölen almamak"]),
    M(["Sayısal türev yolu: Φ(t) doğrusunun eğimi = ΔΦ/Δt; ε = N·eğim (grafik yolu)."],
      ["Doğrusal Φ(t)"], ["Eğrisel değişimde ortalama eğim"], ["Eğimin işaretini unutmak"]),
    "İndüksiyon hesabı: Φ → ΔΦ → ε = NΔΦ/Δt → i = ε/R. Oran: N doğru, Δt ters. Ters çevirme: ΔΦ = 2BA. Açık devrede ε var, i yok.",
    "Alanı 0,02 m² olan, 100 sarımlı bir bobin alana dik tutuluyor. Alan 0,1 T'den 0,4 T'ye 0,5 s'de düzgün artıyor. Bobinin direnci 15 Ω. ε ve i'yi bulunuz. Δt iki katına çıkarılırsa ve N yarıya indirilirse ε kaç katı olur? Bobin 0,1 T'lik alanda 180° çevrilirse (alan yönü bobine göre ters) ΔΦ kaçtır?",
    ["ΔΦ = (0,4 − 0,1)·0,02 = 6×10⁻³ Wb.", "ε = N·ΔΦ/Δt = 100·6×10⁻³/0,5 = 1,2 V; i = ε/R = 1,2/15 = 0,08 A.",
     "Δt ×2, N ×1/2 → ε ×1/4 → 0,3 V.", "180° çevirme: Φ_ilk = +BA, Φ_son = −BA → ΔΦ = 2BA = 2·0,1·0,02 = 4×10⁻³ Wb."],
    "ε = 1,2 V, i = 0,08 A; ε yeni 1/4 katı (0,3 V); ters çevirmede ΔΦ = 4×10⁻³ Wb.",
    """
N, A, R = 100, 0.02, 15.0
B1, B2, dt = 0.1, 0.4, 0.5
phi = lambda B: B * A
dphi = phi(B2) - phi(B1)
eps = N * dphi / dt
assert abs(dphi - 6e-3) < 1e-12 and abs(eps - 1.2) < 1e-9 and abs(eps / R - 0.08) < 1e-12
# bağımsız: sayısal türev (Φ(t) doğrusal)
Bt = lambda t: B1 + (B2 - B1) * t / dt
f = lambda t: -N * (phi(Bt(t + 1e-6)) - phi(Bt(t - 1e-6))) / 2e-6
assert abs(abs(f(0.25)) - eps) < 1e-6
# oran
assert abs((N / 2) * dphi / (2 * dt) - eps / 4) < 1e-12
# ters çevirme: ΔΦ = 2BA, sıfır değil
flip = phi(-0.1) - phi(0.1)
assert abs(abs(flip) - 4e-3) < 1e-12 and flip != 0
# başarısız model: akı sabitse (B sabit, büyük) ε = 0
assert abs(N * (phi(1.0) - phi(1.0)) / dt) == 0
""")

SOLUTIONS["induction-flux-time-graphs"] = S(
    M(["Φ–t (ya da B–t) grafiğini doğrusal aralıklara ayır.",
       "Her aralıkta eğimi bul: eğim = ΔΦ/Δt (B–t grafiğinde Φ = B·A önce hesaplanır).",
       "ε = −N·eğim: eğim pozitifse ε negatif, eğim negatifse ε pozitif, eğim sıfırsa ε = 0 (akı sabit ya da sıfır olsa da).",
       "En büyük |ε|: en dik aralık. Düz aralıkta ε sıfır.",
       "ε–t grafiği parçalı sabit basamaklar şeklindedir; tablo verilirse ardışık farklarla aynı yöntem."],
      ["Grafik parçalı doğrusal", "Sarım sayısı N bilinir"],
      ["Eğrisel Φ–t'de ε zamanla sürekli değişir (teğet eğimi)", "İşaret konvansiyonu yönle ilişkilidir (Lenz)"],
      ["Φ büyük diye ε büyük sanmak", "Eğim yerine değere bakmak", "Eksen birimlerini (ms, mWb) çevirmemek", "N'yi unutmak"]),
    M(["Gerilimi akının kendisi değil değişim hızı belirler: dik grafik hızlı değişim.",
       "Eksi işaret, indüklenen akımın değişime karşı koyduğunu gösterir (Lenz).",
       "Akı değişmediği aralıkta (yatay çizgi) tepki yoktur."],
      ["Her an için"], ["Nitel"], ["Akı sıfır olunca ε sıfır sanmak"]),
    M(["Üç hızlı kural: yatay → 0; dik artan → büyük negatif; dik azalan → büyük pozitif."],
      ["Parçalı doğrusal"], ["Eğrisel parçada geçersiz"], ["Eğimin işaretini ters almak"]),
    None,
    "Φ–t grafiğinde ε = −N × eğim. Yatay aralık → 0; azalan aralık → pozitif; dik → büyük. Akı sıfır geçerken eğim büyükse |ε| büyük olabilir.",
    "10 sarımlı bir bobinden geçen akı (s, mWb) noktalarında (0, 0), (2, 8), (5, 8), (7, −4) olan doğrusal parçalı bir grafik izliyor. ε–t grafiğini (her aralıkta değer) çiziniz. En büyük |ε| hangi aralıktadır? ε hangi aralıkta sıfırdır?",
    ["0–2 s: eğim = 8 mWb/2 s = 4 mWb/s → ε = −10·4×10⁻³ = −0,04 V.", "2–5 s: eğim 0 → ε = 0.", "5–7 s: eğim = −12 mWb/2 s = −6 mWb/s → ε = +0,06 V.",
     "En büyük |ε|: 5–7 s (0,06 V); sıfır: 2–5 s."],
    "0–2 s: −0,04 V; 2–5 s: 0; 5–7 s: +0,06 V; en büyük |ε| 5–7 s aralığında.",
    """
N = 10
pts = [(0.0, 0.0), (2.0, 8e-3), (5.0, 8e-3), (7.0, -4e-3)]          # (s, Wb)
phi = lambda t: next(p0[1] + (p1[1] - p0[1]) * (t - p0[0]) / (p1[0] - p0[0]) for p0, p1 in zip(pts, pts[1:]) if p0[0] <= t <= p1[0])
eps = lambda t, h=1e-6: -N * (phi(t + h) - phi(t - h)) / (2 * h)
assert abs(eps(1.0) + 0.04) < 1e-6 and abs(eps(3.0)) < 1e-9 and abs(eps(6.0) - 0.06) < 1e-6
assert max(range(1, 69), key=lambda k: abs(eps(k / 10))) in range(51, 69)    # en büyük |ε| 5–7 s aralığında
# B–t grafiğinden: Φ = B·A, A = 10⁻² m²  (B: 0 → 0,8 T ...)
A = 1e-2
B_pts = [(0.0, 0.0), (2.0, 0.8)]
assert abs(-N * A * (B_pts[1][1] - B_pts[0][1]) / (B_pts[1][0] - B_pts[0][0]) + 0.04) < 1e-12
# tablo yöntemi: ardışık farklar (1 s adım)
phis = [phi(float(t)) for t in range(8)]
eps_tab = [-N * (phis[k + 1] - phis[k]) / 1.0 for k in range(7)]
assert abs(eps_tab[0] + 0.02) < 1e-12 and abs(eps_tab[3]) < 1e-12 and abs(eps_tab[5] - 0.06) < 1e-12
""")

SOLUTIONS["lenz-induced-current-direction"] = S(
    M(["Dış alanın yönünü ve değişimini yaz (artıyor mu, azalıyor mu?).",
       "Lenz: indüksiyon akımı, değişime KARŞI KOYAN alan oluşturacak yöndedir: akı ARTIYORSA indüksiyon alanı dış alana ZIT; akı AZALIYORSA AYNI yönlüdür.",
       "İndüksiyon alanının yönünden sağ el kuralıyla (dört parmak akım, baş parmak alan) akım yönünü bul; belirli bakış yönüne göre saat yönü/tersi yaz.",
       "Mıknatıs yaklaşırken ve uzaklaşırken akım yönleri zıttır.",
       "Devre açıksa akım yoktur ama ε vardır (ve yön yine Lenz ile bulunur)."],
      ["Kapalı iletken halka/bobin", "Akı değişimi var"],
      ["Akı sabitse akım yok", "İndüksiyon alanı dış alanı yok etmez, yalnız değişime karşı koyar"],
      ["İndüksiyon alanını daima dış alana zıt almak", "Bakış yönünü (üstten/alttan) karıştırmak", "Dış alan yönü ile indüksiyon alan yönünü karıştırmak"]),
    M(["Enerji korunumu: indüksiyon akımı değişimi kolaylaştırsaydı sistem kendi kendine enerji kazanırdı; bu yüzden tepki karşı koyar.",
       "Değişimi 'küçültmeye' çalışan alan: artışı azaltmak için zıt, azalışı azaltmak için aynı yönlü."],
      ["Her indüksiyon olayı"], ["Nitel"], ["Lenz'i 'dış alana zıt' diye ezberlemek"]),
    M(["Dört adım: (1) dış alan yönü, (2) artış/azalış, (3) indüksiyon alanı = artışta zıt / azalışta aynı, (4) sağ el → akım."],
      ["Standart soru"], ["Yön kavramına dikkat"], ["3. adımı atlamak"]),
    None,
    "Lenz: artışa zıt, azalışa aynı yönlü alan. Üstten bakışta, aşağı inen N kutbu için akı aşağı artıyor → yukarı alan → saat yönünün tersi akım; uzaklaşırken saat yönünde.",
    "Yatay duran iletken bir halkaya üstten bir mıknatısın N kutbu yaklaştırılıyor (mıknatıs aşağı iniyor; N kutbu aşağıya bakıyor, alan çizgileri aşağı doğru). Üstten bakışta halkadaki indüksiyon akımının yönü nedir? Mıknatıs uzaklaşırken ne olur? Halka kesikse?",
    ["Dış alan aşağı ve artıyor → indüksiyon alanı yukarı (karşı koyar).", "Sağ el: baş parmak yukarı → dört parmak üstten bakışla saat yönünün tersi.",
     "Uzaklaşırken alan azalıyor → indüksiyon alanı aşağı (aynı yönlü) → akım saat yönünde.", "Kesik halkada akım yok (ε var, akım yok)."],
    "Yaklaşırken saat yönünün tersi, uzaklaşırken saat yönünde; kesik halkada akım yok.",
    VEC + """
# z yukarı; halka xy düzleminde, normal +z; üstten bakışta saat yönünün tersi = +z normale göre pozitif
b0, rate, A = 1.0, 0.5, 0.01
def eps_for(Bz_of_t, t, h=1e-6):
    phi = lambda s: Bz_of_t(s) * A
    return -(phi(t + h) - phi(t - h)) / (2 * h)
# yaklaşma: aşağı yönlü alan büyüklüğü artıyor: B_z = −(b0 + rate t)
e_in = eps_for(lambda s: -(b0 + rate * s), 1.0)
# uzaklaşma: aşağı yönlü alan büyüklüğü azalıyor
e_out = eps_for(lambda s: -(b0 - rate * s), 0.2)
assert e_in > 0 and e_out < 0                      # ε>0: +z normale göre saat yönünün tersi akım
# bağımsız doğrulama: gerçek akım yönlü halkanın merkezindeki Biot–Savart alanı
ring_ccw = circle(0.1)                             # üstten bakışta saat yönünün tersi
ring_cw = circle(0.1, ccw=False)
Bc_ccw = biot(ring_ccw, (0, 0, 0)); Bc_cw = biot(ring_cw, (0, 0, 0))
assert Bc_ccw[2] > 0 and Bc_cw[2] < 0
# yaklaşma: indüksiyon alanı yukarı (dış alana zıt), akım ccw
assert (e_in > 0) == (Bc_ccw[2] > 0)
ext_in = -1.0                                      # dış alan aşağı
assert Bc_ccw[2] * ext_in < 0                      # indüksiyon alanı dış alana zıt (artış)
# uzaklaşma: akım cw → indüksiyon alanı aşağı = dış alanla aynı yönlü (azalışı yavaşlatır)
assert (e_out < 0) == (Bc_cw[2] < 0) and Bc_cw[2] * ext_in > 0
# kesik halka: dolaşım yok → akım sıfır (R sonsuz)
assert (e_in / float("inf")) == 0.0
""")

SOLUTIONS["magnet-falling-through-ring"] = S(
    M(["Bileziğin kapalı mı kesikli mi olduğuna bak: kesikli halkada akım yolu yoktur → akım yok, manyetik kuvvet yok → mıknatıs serbest düşer (a = g).",
       "Kapalı iletken bilezikte: mıknatıs yaklaşırken ve uzaklaşırken akı değişir → indüksiyon akımı oluşur (yönleri zıt).",
       "Lenz: indüksiyon akımı değişime karşı koyar → mıknatısa her iki durumda da hareketine ZIT (yukarı) kuvvet etki eder: yaklaşırken iter, uzaklaşırken çeker.",
       "Serbest cisim diyagramı: mg aşağı, manyetik frenleme kuvvetini yukarı çiz; net kuvvet küçülür, ivme g'den küçük, düşme süresi uzar.",
       "Plastik (iletken olmayan) halkada kapalı olsa da akım oluşmaz → serbest düşme."],
      ["Mıknatıs bilezik ekseni boyunca düşer", "Hava direnci ihmal"],
      ["Mıknatıs hızlandıkça frenleme artar; çok uzun borularda limit hıza yaklaşılır", "Bileziğin direnci çok küçükse etki büyür"],
      ["Mıknatıs bileziğin içinden geçerken kuvvetin yön değiştirdiğini sanmak", "Kesikli bilezikte de akım sanmak", "Plastik halkada fren olduğunu sanmak"]),
    M(["Enerji korunumu: mıknatısın kinetik/potansiyel enerjisinin bir kısmı bilezikte ısıya dönüşür; bu enerjiyi bilezik mıknatıstan frenleme kuvvetiyle çeker.",
       "Akım hareketi kolaylaştırsaydı mıknatıs bileziğe girerken hızlanıp sonsuz enerji üretirdi; bu yüzden kuvvet hep harekete zıttır.",
       "Kesik bilezikte enerji dönüşümü olmaz."],
      ["Her kapalı iletken halka"], ["Nitel"], ["Kuvvetin yönünü değiştiğini sanmak"]),
    M(["Karar ağacı: iletken değil / kesik → serbest düşme; kapalı iletken → her zaman yukarı fren kuvveti (yaklaşırken ve uzaklaşırken)."],
      ["Standart sorular"], ["Çok halka varsa her halkada ayrı"], ["Fren kuvvetini yalnız girişte düşünmek"]),
    M(["Güç yolu: ısıl güç P = i²R ≥ 0; F·ϑ = −P olduğundan kuvvet daima harekete zıttır (enerji argümanı)."],
      ["Kapalı iletken halka"], ["Nicel akım hesabı gerektirmez"], ["Güç eksi işaretini atlamak"]),
    "Mıknatıs–halka: kapalı iletken → yukarı fren (giriş ve çıkışta) + akım yönü zıt; kesik/plastik → serbest düşme. İvme g'den küçük, süre uzun.",
    "Bir mıknatıs h yüksekliğinden, ekseni boyunca (a) kapalı bakır bileziğin, (b) kesikli bakır bileziğin içinden bırakılıyor. Her durumda akımı, kuvvetleri ve düşme sürelerini karşılaştırınız. Mıknatıs bileziğe girerken ve çıkarken manyetik kuvvetin yönü nedir?",
    ["(a) Akı değişir → akım oluşur; Lenz → mıknatısa yukarı yönlü kuvvet: girerken itme, çıkarken çekme (akım yönleri zıt).", "(b) Akım yolu yok: akım ve kuvvet yok, serbest düşme.",
     "Serbest cisim diyagramı (a): mg aşağı, F_m yukarı → a < g → süre (a)'da daha uzun."],
    "(a) Akım var, kuvvet hep yukarı, süre uzun; (b) akım ve kuvvet yok, serbest düşme.",
    """
import math
# dipol–halka akısı (eksen üzerinde): Φ(z) = Φ0 / (1 + (z/a)^2)^{3/2}, z: halka düzleminden yükseklik
Phi0, a, g, m = 1.0, 0.05, 10.0, 0.1
dPhi = lambda z: -3 * Phi0 * z / a ** 2 / (1 + (z / a) ** 2) ** 2.5
def fall(Rring):
    z, v, t, dt = 0.4, 0.0, 0.0, 1e-5
    i_signs, F_signs = set(), []
    while z > -0.4:
        eps = -dPhi(z) * v                         # ε = −dΦ/dt
        i = eps / Rring if Rring != float("inf") else 0.0
        F = i * dPhi(z)                            # güç dengesi: F·v = −i²R → F = i·dΦ/dz
        if v != 0 and i != 0:
            i_signs.add(i > 0); F_signs.append(F > 0)
        acc = -g + F / m
        v += acc * dt; z += v * dt; t += dt
    return t, i_signs, F_signs
t_free, _, _ = fall(float("inf"))
t_ring, i_signs, F_signs = fall(0.005)
assert abs(t_free - math.sqrt(2 * 0.8 / g)) < 5e-3      # kesik bilezik: serbest düşme
assert t_ring > t_free * 1.05                           # kapalı bilezik: düşme uzar
assert i_signs == {True, False}                         # girerken ve çıkarken akım yönleri zıt
assert all(F_signs)                                     # fren kuvveti hep yukarı (z yönünde +)
""")

SOLUTIONS["induction-applications"] = S(
    M(["Cihazda 'akı nerede, neden değişiyor?' sorusunu sor (titreşen tel, yaklaşan araç, değişen akım, dönen kuple).",
       "Akı değişmiyorsa ε yoktur (elektrogitarda tel sabitken, loop dedektöründe araç yokken).",
       "ε = N·ΔΦ/Δt: ε'yu artırma yolları → N ↑, ΔΦ ↑ (daha güçlü alan, daha büyük genlik/alan), Δt ↓ (daha hızlı değişim, yüksek frekans).",
       "Kablosuz şarjda mesafe büyüdükçe alt bobinden geçen akı azalır → ε ve aktarılan enerji azalır; alıcı bobinin N'si artarsa ε artar.",
       "Enerji dönüşümü: santralde mekanik → elektrik (hareketle akı değişimi)."],
      ["Kapalı devre ya da algılayıcı", "Akı değişimi nedeni belli"],
      ["Program hesap vermeyebilir; oran yorumu", "Alan düzgün değilse akı konumla da değişir"],
      ["Tel durunca da sinyal oluşur sanmak", "Mesafe artınca ε artar sanmak", "Yalnız B'ye bakıp Δt'yi unutmak"]),
    M(["Bu cihazlar 'hareketi ya da değişimi' elektrik sinyaline çevirir: değişim yoksa sinyal yok.",
       "Algılayıcılar (loop dedektörü, elektrogitar) ε'nın varlığını/değerini ölçerek değişimi haber verir.",
       "Enerji, hareket eden kaynağın işinden gelir."],
      ["İndüksiyon cihazları"], ["Nitel"], ["Cihazı enerji kaynağı sanmak"]),
    M(["Anahtar soru: akı değişiyor mu? Hızı ne? Sonra N, B, A, Δt etmenlerini sırala."],
      ["Standart sorular"], ["Karmaşık sistemde birden çok değişim"], ["Etmen yönünü yanlış okumak"]),
    None,
    "İndüksiyon uygulamaları: akı değişmiyorsa sinyal yok. Elektrogitar ε frekansı = tel frekansı; mesafe artar → ε azalır; N artar → ε artar.",
    "Elektrogitarda mıknatıslı bir çelik tel, bobinin önünde 440 Hz ile titreşiyor. Tel durunca ε ne olur? ε'nun frekansı nedir? Bobinin sarım sayısı 2 katına çıkarılırsa ve titreşim genliği 3 katına çıkarsa (frekans sabit) ε kaç katı olur? Telefonu şarj alanından uzaklaştırırsak ne olur?",
    ["Tel durunca akı sabit → ε = 0.", "Akı tel frekansında periyodik değişir → ε'nun frekansı 440 Hz.", "ε ∝ N·ΔΦ: ΔΦ genlikle orantılı → ×2 ×3 = ×6.", "Uzaklaşınca bobinden geçen akı azalır → ε ve aktarılan enerji azalır."],
    "ε = 0; 440 Hz; ε 6 katı; uzaklaşınca ε azalır.",
    """
import math
def amp_eps(N, dphi_amp, f):
    # Φ(t) = Φ0 + ΔΦ sin(2π f t) → ε = −N dΦ/dt, genlik N·ΔΦ·2πf
    return N * dphi_amp * 2 * math.pi * f
f0, N0, d0 = 440.0, 100, 1e-6
eps0 = amp_eps(N0, d0, f0)
# sayısal türev ile genlik ve frekans doğrulaması
dt = 1e-6
phi = lambda t: 5e-6 + d0 * math.sin(2 * math.pi * f0 * t)
vals = [-(N0 * (phi(k * dt + dt) - phi(k * dt - dt)) / (2 * dt)) for k in range(0, 10000)]
assert abs(max(vals) - eps0) / eps0 < 1e-3
zc = sum(1 for k in range(1, len(vals)) if vals[k - 1] * vals[k] < 0)
assert abs(zc / 2 / (len(vals) * dt) - f0) < 2.0           # ε frekansı 440 Hz
assert abs(amp_eps(2 * N0, 3 * d0, f0) / eps0 - 6) < 1e-12
# tel durunca ε = 0
still = lambda t: 5e-6
assert abs(-(N0 * (still(1e-3 + dt) - still(1e-3 - dt)) / (2 * dt))) == 0.0
# uzaklaşma: halka akısı ~ 1/(R²+z²)^{3/2} azalır
R = 0.03
flux = lambda z: 1.0 / (R ** 2 + z ** 2) ** 1.5
assert flux(0.01) > flux(0.03) > flux(0.06)
""")
