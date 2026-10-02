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
assert abs(eps_tab[0] + 0.04) < 1e-12 and abs(eps_tab[3]) < 1e-12 and abs(eps_tab[5] - 0.06) < 1e-12
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
Phi0, a, g, m = 0.01, 0.05, 10.0, 0.1       # Φ0 küçük: frenleme orta şiddette (terminal hız ~ m/s) → kısa simülasyon
dPhi = lambda z: -3 * Phi0 * z / a ** 2 / (1 + (z / a) ** 2) ** 2.5
def fall(Rring):
    z, v, t, dt = 0.4, 0.0, 0.0, 1e-4
    n = 0
    i_signs, F_signs = set(), []
    while z > -0.4 and n < 100000:                 # adım sınırı: sonsuz döngü olmasın
        n += 1
        eps = -dPhi(z) * v                         # ε = −dΦ/dt
        i = eps / Rring if Rring != float("inf") else 0.0
        F = i * dPhi(z)                            # güç dengesi: F·v = −i²R → F = i·dΦ/dz
        if v != 0 and i != 0:
            i_signs.add(i > 0); F_signs.append(F > 0)
        acc = -g + F / m
        v += acc * dt; z += v * dt; t += dt
    assert z <= -0.4                               # halkadan geçip aşağı çıktı
    return t, i_signs, F_signs
t_free, _, _ = fall(float("inf"))
t_ring, i_signs, F_signs = fall(0.01)
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
vals = [-(N0 * (phi(k * dt + dt) - phi(k * dt - dt)) / (2 * dt)) for k in range(0, 200000)]
assert abs(max(vals) - eps0) / eps0 < 1e-3
# sıfır geçiş anları (doğrusal interpolasyon); iki ardışık yukarı geçiş = 1 periyot
ups = [(k - 1 + vals[k - 1] / (vals[k - 1] - vals[k])) * dt for k in range(1, len(vals)) if vals[k - 1] < 0 <= vals[k]]
assert abs((len(ups) - 1) / (ups[-1] - ups[0]) - f0) < 0.5           # ε frekansı 440 Hz
assert abs(amp_eps(2 * N0, 3 * d0, f0) / eps0 - 6) < 1e-12
# tel durunca ε = 0
still = lambda t: 5e-6
assert abs(-(N0 * (still(1e-3 + dt) - still(1e-3 - dt)) / (2 * dt))) == 0.0
# uzaklaşma: halka akısı ~ 1/(R²+z²)^{3/2} azalır
R = 0.03
flux = lambda z: 1.0 / (R ** 2 + z ** 2) ** 1.5
assert flux(0.01) > flux(0.03) > flux(0.06)
""")

# ============================ FİZ.11.2.12 — Alternatif akım ============================
SOLUTIONS["ac-factors-identification"] = S(
    M(["Basit jeneratörde akı Φ(t) = N·B·A·cos(2π·f·t) biçiminde değişir; ε = −dΦ/dt olduğundan ε_maks = N·B·A·(2π·f), ε'un frekansı çerçevenin dönme frekansı f'ye eşittir.",
       "Her etmen için sor: 'Akının değişim hızını artırır mı?' N, B, A ve f ε_maks'ı doğru orantılı değiştirir.",
       "Frekansı YALNIZ dönme frekansı belirler; N, B ve A değişince ε_maks değişir, frekans değişmez.",
       "Çarpan yöntemi: ε_maks'ın yeni değeri = (N çarpanı)(B çarpanı)(A çarpanı)(f çarpanı); frekans çarpanı = yalnız f çarpanı.",
       "Eşleştirme tablosu: N, B, A → yalnız büyüklük; dönme hızı → hem büyüklük hem frekans; yönelim ve çerçeve şekli frekansı etkilemez."],
      ["Düzgün manyetik alan", "Çerçeve sabit açısal hızla dönüyor", "Çerçeve ekseni alana dik"],
      ["Kitabın 12. Etkinlik düzeneği nitel ve oran düzeyindedir; ε_maks = N·B·A·ω ifadesi türetmedir, kitapta ayrı formül olarak yer almaz", "Hız sabit değilse dalga sinüs biçiminden sapar"],
      ["Sarım sayısı artınca frekansın da arttığını sanmak", "Yüzey alanı büyüyünce frekansın azaldığını sanmak", "Dönme hızı artınca yalnız frekansın arttığını, büyüklüğün değişmediğini sanmak"]),
    M(["Akı ne kadar hızlı değişirse ε o kadar büyük olur: daha çok sarım, daha güçlü alan, daha büyük alan veya daha hızlı dönüş akı değişimini büyütür.",
       "Frekans, saniyedeki tur sayısıdır: çerçeve her turda bir tam salınım yapar; N, B, A turu hızlandırmaz.",
       "Bisiklet dinamosunda hız artınca lamba hem parlar hem daha sık yanıp söner: iki etki birlikte görülür."],
      ["Düzgün alanda dönen çerçeve"], ["Nitel"], ["Büyüklük ile frekansı aynı şey sanmak"]),
    M(["Sorudaki etmeni bul: N, B ya da A ise 'büyüklük ×k, frekans aynı'; dönme hızı ise 'büyüklük ×k, frekans ×k'. Birden çok etmen varsa büyüklük çarpanlarını çarp."],
      ["Her değişiklik tek tek tanımlı"], ["Etmenler birbirini götürebilir (B ×2, A ×1/2 → büyüklük aynı)"], ["Frekans çarpanını N, B, A'ya da uygulamak"]),
    M(["Eğim yolu: Φ–t grafiğinde etmen değişince tepe değer ve eğim nasıl değişir diye grafik çiz; f artarsa eğri sıkışır (periyot kısalır), N·B·A artarsa genlik büyür."],
      ["Grafik karşılaştırması"], ["Nicel eğim hesabı gerekmez"], ["Genlikle periyodu karıştırmak"]),
    "Dört etmenin ikisi sınıfı: (N, B, A) yalnız büyüklüğü, dönme hızı büyüklüğü VE frekansı artırır. 'Frekans' tuzağı: N, B, A'ya frekans bağlamak.",
    "Düzgün manyetik alanda sabit hızla dönen N sarımlı bir çerçeve ε_maks = E₀ ve f₀ frekanslı bir alternatif gerilim üretiyor. (a) N iki katına, (b) dönme sıklığı 3 katına, (c) B yarıya ve A 4 katına, (d) B 2 katına ve dönme sıklığı yarıya çıkarılırsa ε_maks ve frekans nasıl değişir?",
    ["ε_maks ∝ N·B·A·f; frekans ∝ f.",
     "(a) ε_maks ×2, frekans aynı.", "(b) ε_maks ×3, frekans ×3.", "(c) ε_maks ×(1/2)(4) = ×2, frekans aynı.", "(d) ε_maks ×(2)(1/2) = ×1 (değişmez), frekans ×1/2."],
    "(a) 2E₀, f₀; (b) 3E₀, 3f₀; (c) 2E₀, f₀; (d) E₀, f₀/2.",
    """
import math
def emf_wave(N, B, A, f, T=2.0, dt=1e-4):
    # Φ(t) = N·B·A·cos(2π f t); ε = −dΦ/dt sayısal merkezi farkla
    phi = lambda t: N * B * A * math.cos(2 * math.pi * f * t)
    n = int(T / dt)
    return [-(phi(k * dt + dt) - phi(k * dt - dt)) / (2 * dt) for k in range(n)], dt
def peak_and_freq(N, B, A, f):
    e, dt = emf_wave(N, B, A, f)
    ups = [(k - 1 + e[k - 1] / (e[k - 1] - e[k])) * dt for k in range(1, len(e)) if e[k - 1] < 0 <= e[k]]
    return max(e), (len(ups) - 1) / (ups[-1] - ups[0])
N0, B0, A0, f0 = 50, 0.2, 0.01, 5.0
E0, F0 = peak_and_freq(N0, B0, A0, f0)
assert abs(E0 - N0 * B0 * A0 * 2 * math.pi * f0) / E0 < 1e-3 and abs(F0 - f0) < 0.05
cases = {"a": (2 * N0, B0, A0, f0), "b": (N0, B0, A0, 3 * f0), "c": (N0, B0 / 2, 4 * A0, f0), "d": (N0, 2 * B0, A0, f0 / 2)}
expect = {"a": (2, 1), "b": (3, 3), "c": (2, 1), "d": (1, 0.5)}
for k, args in cases.items():
    e, fr = peak_and_freq(*args)
    assert abs(e / E0 - expect[k][0]) < 2e-3 and abs(fr / F0 - expect[k][1]) < 5e-3, k
""")

SOLUTIONS["ac-loop-graphs"] = S(
    M(["Konum–akı eşleşmesi: çerçeve alana dik (yüzeyle alan dik) → Φ en büyük, ε = 0; çerçeve alana paralel → Φ = 0, |ε| en büyük (akı en hızlı değişir).",
       "Akım yönü: çerçevenin alan çizgilerini kesme yönü yarım turda bir yönde, diğer yarım turda zıt yöndedir; bir turda akım iki kez yön değiştirir.",
       "Φ–t kosinüs benzeriyse ε–t sinüs benzeridir: ε, Φ–t grafiğinin eğimiyle (−) orantılıdır; ε, akıya göre T/4 (90°) kaymıştır.",
       "Φ–t'de tepe ya da çukurdan geçerken eğim sıfırdır → ε = 0; Φ–t sıfırdan geçerken eğim en dik → |ε| en büyük.",
       "Osiloskop: dalganın tepe yüksekliği (kare sayısı × V/kare) en büyük gerilimi; bir tam dalganın yatay uzunluğu (kare × s/kare) periyodu verir; f = 1/T.",
       "İki dalgayı aynı ölçekle karşılaştır: tepe oranı = gerilim oranı; periyot oranının TERSİ = frekans oranı."],
      ["Düzgün alan, sabit dönme hızı", "Osiloskopta iki kanalın ölçeği aynı ya da ölçek oranı biliniyor"],
      ["Ölçek (V/kare, s/kare) iki kanalda farklıysa kare sayısını doğrudan karşılaştırmak yanlıştır", "Dönme hızı sabit değilse dalga sinüs olmaz"],
      ["Φ–t grafiğini ε–t grafiği sanmak", "Akı sıfırken akımın da sıfır olduğunu sanmak", "Periyodu kare sayısını yanlış okuyarak (tepeden çukura) yarım alınması"]),
    M(["Gerilimi akının kendisi değil değişim hızı belirler: dik dururken yüzeyden geçen akı en büyük ama o an değişmiyor (tepe noktası).",
       "Alana paralelken çerçeve alan çizgilerini 'kesiyor': akı sıfırdan geçiyor ve değişimi en hızlı.",
       "Tam tur: iki kez akı en büyük (zıt yönlü), iki kez sıfır; akım iki kez yön değiştirir, iki kez mutlak değerce en büyük olur."],
      ["Her an için"], ["Nitel"], ["Akı büyük = akım büyük sanmak"]),
    M(["Üç kural: Φ tepe/çukur → ε = 0; Φ sıfır → |ε| en büyük; ε–t, Φ–t'ye göre T/4 geri/ileri. Osiloskopta: yükseklik → gerilim, genişlik → periyot (frekans ters)."],
      ["Bir periyotluk sinüs benzeri grafik"], ["Eğrisel olmayan dalgada geçersiz"], ["Frekansı periyotla doğru orantılı almak"]),
    None,
    "Φ–t ile ε–t'yi hep eğim ilişkisiyle bağla: akı tepedeyse ε sıfır. Osiloskopta tepe = gerilim, genişlik = periyot (frekans ters). Bir turda 2 yön değişimi.",
    "Düzgün alanda sabit hızla dönen çerçevenin Φ–t grafiği t = 0'da en büyük değerden başlayan kosinüs eğrisidir (T periyot). (a) ε = 0 hangi anlardadır, |ε| hangi anlarda en büyüktür? (b) T/4 ve 3T/4 anlarında akım yönleri nasıldır? (c) Bir turda akım kaç kez yön değiştirir? (d) Osiloskop ekranında (her iki kanal 1 V/kare, 2 ms/kare) mavi dalga tepede 4 kare, bir tam dalga 4 kare; sarı dalga tepede 2 kare, bir tam dalga 8 kare ise mavi ve sarı dalganın en büyük gerilim ve frekans oranları nedir?",
    ["(a) Φ tepe/çukur anlarında (0, T/2, T) eğim 0 → ε = 0; Φ = 0 olan T/4 ve 3T/4'te eğim en dik → |ε| en büyük.",
     "(b) T/4'te ε bir işaretlidir, 3T/4'te zıt işaretlidir: akım yönleri zıt.", "(c) ε iki kez sıfırdan geçip işaret değiştirir → bir turda 2 kez yön değiştirir.",
     "(d) V_mavi = 4 V, V_sarı = 2 V → oran 2; T_mavi = 8 ms, T_sarı = 16 ms → f_mavi = 125 Hz, f_sarı = 62,5 Hz → frekans oranı 2."],
    "(a) ε = 0: 0, T/2, T; |ε| en büyük: T/4, 3T/4. (b) zıt yönlü. (c) 2 kez. (d) Gerilim oranı 2, frekans oranı 2 (mavi büyük).",
    """
import math
T = 1.0
phi = lambda t: math.cos(2 * math.pi * t / T)
h = 1e-6
eps = lambda t: -(phi(t + h) - phi(t - h)) / (2 * h)          # ε = −dΦ/dt (N=1)
# (a) ε = 0 anları akı tepe/çukurunda; |ε| en büyük anlar akının sıfır olduğu anlarda
for t in (0.0, 0.5, 1.0):
    assert abs(eps(t)) < 1e-4 and abs(abs(phi(t)) - 1) < 1e-12
for t in (0.25, 0.75):
    assert abs(phi(t)) < 1e-12 and abs(abs(eps(t)) - 2 * math.pi / T) < 1e-3
# (b) T/4 ve 3T/4'te zıt işaret
assert eps(0.25) > 0 > eps(0.75)
# (c) bir periyotta işaret değişimi sayısı
ts = [k / 10000.0 for k in range(1, 10000)]
signs = [eps(t) > 0 for t in ts]
assert sum(1 for a, b in zip(signs, signs[1:]) if a != b) == 1       # (0,1) içinde T/2'de bir değişim; ε t=0 ve t=T'de de sıfırdan geçer → periyotta 2 değişim
assert eps(1e-3) > 0 and eps(1 - 1e-3) < 0 and eps(1 + 1e-3) > 0     # t=0'da ve t=T'de işaret değişir
# ε–t, Φ–t'ye göre çeyrek periyot kaymış: ε maksimumu (t=T/4), Φ maksimumundan (t=0) T/4 sonra
t_eps_max = max(ts, key=eps)
assert abs(phi(0.0) - 1.0) < 1e-12 and abs(t_eps_max - 0.25) < 1e-3
# (d) osiloskop: tepe yüksekliği (kare) × V/kare ve bir tam dalga genişliği (kare) × s/kare
V_per_div, s_per_div = 1.0, 2e-3
blue = dict(peak_div=4, wave_div=4); yellow = dict(peak_div=2, wave_div=8)
Vb, Vy = blue["peak_div"] * V_per_div, yellow["peak_div"] * V_per_div
Tb, Ty = blue["wave_div"] * s_per_div, yellow["wave_div"] * s_per_div
assert Vb / Vy == 2 and abs((1 / Tb) / (1 / Ty) - 2) < 1e-12 and abs(1 / Tb - 125) < 1e-9 and abs(1 / Ty - 62.5) < 1e-9
# örnekle: dalgaları üretip tepe ve frekansı ölç
def measure(V0, f, dt=1e-5, dur=0.1):
    y = [V0 * math.sin(2 * math.pi * f * k * dt) for k in range(int(dur / dt))]
    ups = [k for k in range(1, len(y)) if y[k - 1] < 0 <= y[k]]
    return max(y), (len(ups) - 1) / ((ups[-1] - ups[0]) * dt)
pb, fb = measure(Vb, 1 / Tb); py, fy = measure(Vy, 1 / Ty)
assert abs(pb / py - 2) < 1e-3 and abs(fb / fy - 2) < 1e-2
""")

SOLUTIONS["ac-led-data-interpretation"] = S(
    M(["Veri tablosunda kontrol değişkeni yöntemini uygula: yalnız BİR etmenin değiştiği satır çiftini bul.",
       "O çiftte çıktı (en büyük gerilim ya da parlaklık) nasıl değişti? Etmen ×k iken çıktı ×k ise doğru orantı; sabitse etki yok.",
       "Orantı katsayısını (çıktı/etmen) her satırda hesapla: hepsi aynı çıkmalı; farklı çıkan satır hatalı kayıttır, doğru değeri katsayıdan bul.",
       "Birden çok değişkenin aynı anda değiştiği satırlarda tek etmene yorum yapılmaz; çarpanları ayırmak için ek satır gerekir.",
       "AC/DC ayrımı: DC kaynakta kararlı durumda akım sabit → komşu devrede akı sabit → ε = 0, lamba yanmaz (yalnız anahtar kapanıp açılırken anlık sıçrama); AC kaynakta akım ve akı sürekli değişir → ε oluşur → lamba yanar, parlaklık dalgalıdır."],
      ["Her satırda yalnız tek etmen değişen en az bir çift var", "Ölçüm yöntemi satırlar arasında aynı"],
      ["Doğrusal olmayan ilişkide katsayı sabit çıkmaz (grafiği çiz)", "Ölçüm hatası küçükse küçük sapmalar hata sayılmaz, belirgin sapma aranır", "DC devrede anahtar açılıp kapanırken kısa süreli ε oluşur"],
      ["Tek satırdan genelleme yapmak", "AC kaynakta akıyı sabit saymak", "DC kaynakta lambanın sürekli yanacağını sanmak"]),
    M(["Akı değişimi yoksa gerilim yoktur: DC komşu devresinde akı sabit, AC komşu devresinde akı sürekli değişir.",
       "LED/lamba parlaklığı ε'un büyüklüğünü yansıtır: akı daha hızlı değiştikçe daha parlak.",
       "Tablo yorumu fiziksel mantığa dayanır: ε ∝ akı değişim hızı ∝ dönme hızı, N, B, A."],
      ["Kapalı devre"], ["Nitel"], ["Parlaklığı akının büyüklüğüne bağlamak"]),
    M(["Satır çiftinde yalnız bir değişken → çıktı oranına bak. Katsayı sütunu ekle (çıktı/etmen). Tuhaf satır = hata. DC → yanmaz, AC → yanar."],
      ["Tablo düzenli"], ["Çoklu değişim satırı yorumlanamaz"], ["Katsayıyı ters bölmek"]),
    None,
    "Tabloda önce 'tek değişkenli satır çifti', sonra 'çıktı/etmen' katsayısı. Katsayısı sapan satır hatalıdır. DC komşu devre: akı sabit → lamba yanmaz.",
    "Bir jeneratör deneyinde çerçeveyi döndürürken ölçülen en büyük gerilimler (n: dönme sıklığı, tur/s; B: alan; N: sarım) şöyledir: (n=1, B=0,1 T, N=100) → 0,63 V; (2, 0,1, 100) → 1,26 V; (3, 0,1, 100) → 2,90 V; (1, 0,2, 100) → 1,26 V; (1, 0,1, 200) → 1,26 V. (a) Hangi satır hatalı kaydedilmiştir, doğrusu kaç V olmalıdır? (b) Gerilim n, B ve N ile nasıl değişir? (c) Çerçevenin komşusundaki devreye önce DC, sonra AC üreteci bağlanıyor; hangi durumda lamba yanar?",
    ["n, B, N ayrı ayrı değişen satır çiftleri: gerilim hep aynı çarpanla artıyor → doğru orantı.",
     "Katsayı V/n: 0,63; 0,63; 0,97 (!) → üçüncü satır tutarsız; V = 3·0,63 = 1,89 ≈ 1,9 V olmalı.",
     "B, N ikişer katına çıkınca gerilim ikişer katı: V ∝ n·B·N.",
     "DC: akı sabit, ε = 0 → lamba yanmaz (anlık sıçrama hariç). AC: akı değişir, ε oluşur → lamba yanar, parlaklık dalgalanır."],
    "3. satır hatalı (≈ 1,9 V olmalı); V ∝ n·B·N; lamba yalnız AC kaynakta yanar.",
    """
import math
rows = [(1, 0.1, 100, 0.63), (2, 0.1, 100, 1.26), (3, 0.1, 100, 2.90), (1, 0.2, 100, 1.26), (1, 0.1, 200, 1.26)]
base = rows[0]
# her satırı taban satırla karşılaştır: beklenen = V0 · (n/n0)(B/B0)(N/N0)
exp = [base[3] * (n / base[0]) * (B / base[1]) * (N / base[2]) for n, B, N, V in rows]
bad = [i for i, (e, r) in enumerate(zip(exp, rows)) if abs(e - r[3]) / e > 0.05]
assert bad == [2] and abs(exp[2] - 1.89) < 1e-9
# fiziksel modelden: ε_maks = N B A 2π n, A = 0,01 m²
A = 0.01
V = lambda n, B, N: N * B * A * 2 * math.pi * n
for n, B, N, Vm in rows:
    if (n, B, N) != (3, 0.1, 100):
        assert abs(V(n, B, N) - Vm) < 0.01
assert abs(V(3, 0.1, 100) - 1.885) < 0.01
# komşu devre: ε = −M·di/dt; DC kararlı halde sıfır, AC'de sıfır değil
M_, R_, L_, V0 = 0.5, 2.0, 0.1, 6.0
i_dc = lambda t: (V0 / R_) * (1 - math.exp(-R_ * t / L_))      # anahtar kapanışından sonra
h = 1e-7
eps = lambda f, t: -M_ * (f(t + h) - f(t - h)) / (2 * h)
assert abs(eps(i_dc, 1e-3)) > 1.0                              # anahtar kapanırken anlık sıçrama (geçici)
assert abs(eps(i_dc, 2.0)) < 1e-9                              # kararlı durum: ε ≈ 0 → lamba yanmaz
i_ac = lambda t: 3.0 * math.sin(2 * math.pi * 50 * t)
assert max(abs(eps(i_ac, k * 1e-4)) for k in range(200)) > 100  # AC: ε sürekli oluşur
""")

SOLUTIONS["ac-effective-max-values"] = S(
    M(["Isı eşdeğerliği: aynı direnç, aynı sürede aynı ısıyı açığa çıkarıyorsa DC'nin değeri AC'nin ETKİN değerine eşittir (V_etkin = V_DC, i_etkin = i_DC).",
       "Etkin değerlerle Ohm yasası geçerlidir: i_etkin = V_etkin / R.",
       "Maksimum değer: V_maks = √2·V_etkin ve i_maks = √2·i_etkin (√2 ≈ 1,41).",
       "Ters yön: etkin değer = maksimum değer / √2.",
       "Voltmetre ve ampermetre etkin değeri okur; şebeke gerilimi (ör. 220 V) etkin değerdir, tepe değeri 220√2 ≈ 311 V'tur.",
       "Isıl güç etkin değerlerle: P = i_etkin²·R = V_etkin²/R; AC'nin bir periyottaki ortalama ısıl gücü budur."],
      ["Sinüs biçimli alternatif akım", "Saf dirençli devre (program kapsamında yalnız etkin/maksimum değer ve ısı eşdeğerliği vardır)"],
      ["Kare ya da üçgen dalgada √2 oranı geçerli değildir (yalnız sinüs için)", "Reaktans, empedans ve faz farkı programda yoktur"],
      ["V_maks hesabında √2 yerine 2 ile çarpmak", "DC'deki değeri AC'nin maksimum değeri sanmak", "Şebeke geriliminin maksimum olduğunu sanmak"]),
    M(["Sinüs biçimli akım zamanın büyük bölümünde tepe değerinden küçüktür; aynı ısıyı verebilmek için DC'nin değerinden √2 kat büyük tepeye çıkması gerekir.",
       "Isıtma etkisi akımın yönünden bağımsızdır (i²R): AC'nin karesel ortalaması DC'nin karesine eşitlenir.",
       "Ölçü aletlerinin etkin değeri göstermesi, ısı etkisinin ölçülmesinden gelir."],
      ["Isıl etki"], ["Nitel"], ["Etkin değeri ortalama değer sanmak (ortalama sıfırdır)"]),
    M(["Tek satır: 'DC eşdeğeri → etkin; maksimum = etkin·1,41'. 'Voltmetre okuyor / şebeke 220 V' → etkin."],
      ["Sinüs biçimli AC"], ["Sinüs dışı dalga"], ["√2 yerine 2"]),
    M(["Güç yolu: P_AC(ortalama) = ½ V_maks²/R = V_DC²/R → V_maks = √2 V_DC (ısıl güçlerin eşitlenmesi)."],
      ["Aynı direnç, sinüs dalga"], ["Program ısı eşdeğerliğiyle yetinir"], ["Ortalama gücü tepe gücü sanmak"]),
    "'DC değeri verilmiş + aynı ısı' → AC etkin değeri o değerdir. Maksimum için ×√2 (×1,41). Voltmetre ve şebeke değeri etkin değerdir; ortalama değer sıfırdır.",
    "3 Ω'luk bir ısıtıcı 12 V'luk DC kaynağa bağlandığında belli sürede açığa çıkan ısıyı aynı sürede bir AC kaynak da veriyor. AC kaynağın etkin gerilimi ve akımı ile maksimum gerilimi ve akımı nedir? Şebeke gerilimi 230 V etkin ise tepe gerilimi yaklaşık kaç volttur? AC devredeki voltmetre hangi değeri gösterir? (√2 = 1,41 alınız)",
    ["DC: i = V/R = 12/3 = 4 A. Aynı ısı → AC etkin değerleri V_etkin = 12 V, i_etkin = 4 A.",
     "V_maks = 12√2 ≈ 17 V; i_maks = 4√2 ≈ 5,7 A.", "230 V şebeke: V_maks = 230·1,41 ≈ 325 V.", "Voltmetre etkin değeri (12 V) gösterir, tepe değeri değil."],
    "V_etkin = 12 V, i_etkin = 4 A; V_maks ≈ 17 V, i_maks ≈ 5,7 A; şebeke tepesi ≈ 325 V; voltmetre etkin değeri okur.",
    """
import math
R, Vdc = 3.0, 12.0
Pdc = Vdc ** 2 / R
Vmax = Vdc * math.sqrt(2)
# bağımsız: bir periyotta ortalama ısıl güç (sayısal integral)
n = 100000
Pavg = sum(((Vmax * math.sin(2 * math.pi * (k + 0.5) / n)) ** 2) / R for k in range(n)) / n
assert abs(Pavg - Pdc) / Pdc < 1e-6                       # aynı ısı → V_etkin = V_dc
Vrms = math.sqrt(sum((Vmax * math.sin(2 * math.pi * (k + 0.5) / n)) ** 2 for k in range(n)) / n)
assert abs(Vrms - Vdc) < 1e-6 and abs(Vmax - 16.97) < 0.01 and abs(Vmax / R - 5.657) < 0.01
assert abs(230 * 1.41 - 324.3) < 0.1
# ortalama değer sıfır (ölçü aletinin okuduğu etkin değer, ortalama değil)
assert abs(sum(Vmax * math.sin(2 * math.pi * (k + 0.5) / n) for k in range(n)) / n) < 1e-9
# başarısız durum: kare dalgada V_etkin = V_maks (√2 geçersiz)
Vsq = sum(((Vdc) ** 2) for _ in range(n)) / n
assert abs(math.sqrt(Vsq) - Vdc) < 1e-12 and abs(math.sqrt(Vsq) * math.sqrt(2) - Vdc) > 1
""")

SOLUTIONS["ac-frequency-period-counting"] = S(
    M(["Periyot T = 1/f (f: saniyedeki tam salınım sayısı).",
       "Bir periyotta akım 2 kez yön değiştirir, 2 kez sıfırdan geçer (lamba 2 kez söner) ve mutlak değerce 2 kez tepe değerine ulaşır (biri +, biri −).",
       "Saniyede sayım: yön değiştirme = sıfır geçiş = lambanın sönme sayısı = mutlak değerce tepe sayısı = 2f.",
       "Verilen süredeki tam periyot sayısı = f·t; süre T'nin katıysa sayım tam çıkar.",
       "Frekans değişince: T = 1/f kadar ters değişir (f ×2 → T ×1/2); tepe değer frekansa bağlı değildir, i–t grafiğinde tepeler aynı yükseklikte kalır, dalgalar sıkışır.",
       "Şebeke tablosu: gerilim ve frekans iki ayrı özelliktir; aynı frekanslı şebekeler (ör. 50 Hz) birbirine bağlanabilir, gerilim farkı için transformatör gerekir."],
      ["Sinüs biçimli AC", "Frekans tam salınım/s olarak verilmiş"],
      ["Başlangıç anı sayıma bir fazla/eksik sıfır geçişi ekleyebilir; sayım tam periyot sayısında kesindir", "Frekans radyan/s (ω) verilirse f = ω/2π"],
      ["T = f yazmak", "Bir periyottaki sıfır geçiş sayısını 1 sanmak", "Frekans artınca tepe değerin de arttığını sanmak"]),
    M(["Akım bir yönde tepe yapıp sıfıra iner, sonra zıt yönde tepe yapıp sıfıra döner: bir tam salınımda iki sıfır, iki tepe.",
       "Lamba akımın yönüne bakmaz; akım her sıfır geçişinde (saniyede 2f kez) çok kısa süre söner ama bu insan gözüyle fark edilmez.",
       "Frekans, jeneratörün saniyedeki tur sayısıdır; tepe değeri alan, alan ve sarım belirler."],
      ["Sinüs dalga"], ["Nitel"], ["Frekansı tepe sayısıyla karıştırmak"]),
    M(["f'yi ikiyle çarp: saniyedeki yön değişimi, sönme ve tepe sayısı. T = 1/f. 'Tepe değer değişir mi?' → frekans değişince hayır."],
      ["Sinüs biçimli AC"], ["Süre 1 s değilse süre ile çarp"], ["f yerine T'yi çarpmak"]),
    None,
    "Saniyede 2f: yön değişimi, sönme, mutlak tepe. T = 1/f. Frekans artınca grafik sıkışır, tepe değer aynı kalır.",
    "Şebeke frekansı 60 Hz olan bir ülkede şebekeye bağlı lamba için (a) periyodu, (b) 1 saniyede akımın kaç kez yön değiştirdiğini, kaç kez mutlak değerce en büyük değere ulaştığını ve lambanın kaç kez söndüğünü, (c) 0,05 s'de kaç tam periyot olduğunu bulunuz. (d) Frekans 120 Hz'e çıkarılırsa i–t grafiğinde periyot ve tepe değeri nasıl değişir?",
    ["(a) T = 1/60 s ≈ 16,7 ms.", "(b) Saniyede 2f = 120: 120 kez yön değiştirir, 120 kez mutlak değerce tepeye ulaşır, lamba 120 kez söner.",
     "(c) f·t = 60·0,05 = 3 tam periyot.", "(d) f ×2 → T ×1/2 (≈ 8,3 ms); tepe değer değişmez."],
    "(a) 1/60 s; (b) 120, 120, 120; (c) 3 tam periyot; (d) periyot yarıya iner, tepe değer aynı kalır.",
    """
import math
def count(f, dur=1.0, dt=1e-5, phase=0.1):
    n = int(dur / dt)
    i = [math.sin(2 * math.pi * f * k * dt + phase) for k in range(n + 1)]
    zeros = sum(1 for a, b in zip(i, i[1:]) if a * b < 0)
    a_ = [abs(x) for x in i]
    peaks = sum(1 for k in range(1, n) if a_[k] > a_[k - 1] and a_[k] >= a_[k + 1] and a_[k] > 0.999)
    return zeros, peaks, max(i)
z60, p60, m60 = count(60.0)
assert abs(1 / 60.0 - 0.016667) < 1e-5 and z60 == 120 and p60 == 120     # yön değişimi = sıfır = tepe = 2f
assert abs(60.0 * 0.05 - 3) < 1e-12 and count(60.0, dur=0.05)[0] in (5, 6)  # 3 periyot ≈ 6 sıfır geçişi (başlangıç fazına göre ±1)
z120, p120, m120 = count(120.0)
assert z120 == 240 and p120 == 240 and abs(m120 - m60) < 1e-6              # tepe değeri sabit
assert abs((1 / 120.0) / (1 / 60.0) - 0.5) < 1e-12                          # periyot yarıya iner
""")

# ============================ FİZ.11.2.13 — Transformatör (program: hesaplamasız, oran/yorum) ============================
SOLUTIONS["transformer-structure-experiment"] = S(
    M(["Tabloda birincil sarım sayısı (Np) ve birincil gerilim (Vp) sabit satırları seç; yalnız ikincil sarım sayısı (Ns) değişiyor.",
       "Ns kaç kat artınca ikincil gerilim (Vs) kaç kat arttığına bak: aynı çarpan → Vs, Ns ile doğru orantılıdır; benzer biçimde Np artınca (Vp sabit) Vs azalır.",
       "Her satırda Vs/Ns (ya da Vs/Vp ile Ns/Np) oranını karşılaştır: aynı olmalı; farklı çıkan satır hatalı kayıttır.",
       "Ns > Np ise Vs > Vp (yükseltici); Ns < Np ise Vs < Vp (alçaltıcı); Ns = Np ise Vs ≈ Vp.",
       "DC kaynak bağlanırsa kararlı durumda birincil akım sabit, çekirdekteki akı sabit, ikincil bobinde gerilim oluşmaz (Vs = 0); yalnız anahtar kapanıp açılırken kısa süreli sıçrama olur.",
       "Yapı: birincil bobin kaynağa bağlıdır ve akıyı üretir; demir çekirdek akıyı ikincil bobine taşır; ikincil bobin yüke gerilim verir."],
      ["Alternatif akım kaynağı", "Demir çekirdekte akı iki bobine de ulaşıyor (ideal modele yakın)", "Satırlar arası yalnız bir değişken değişiyor"],
      ["Program hesaplamayı dışlar; kitapta var: Vp/Vs = Np/Ns (s. 268)", "Çekirdek açık ya da bobinler uzaktaysa akı kaçar, ölçülen Vs beklenenden küçük çıkar", "DC'de ilk anda ölçülen kısa değer kararlı değer değildir"],
      ["Birincil ve ikincil sütunlarını karıştırmak", "DC'de de sürekli ikincil gerilim beklemek", "Birden çok değişken değişen satırı tek etmenin etkisi saymak"]),
    M(["İkincil bobinde gerilimi oluşturan şey çekirdekteki akının DEĞİŞİMİdir; AC bu akıyı sürekli değiştirir, DC değiştirmez.",
       "Her sarım çekirdekteki aynı akı değişiminden aynı gerilim alır: sarım sayısı arttıkça sarımların gerilimleri seri toplanır → Vs ∝ Ns.",
       "Demir çekirdek akı çizgilerini ikincil bobine yönlendirdiği için transformatör verimli çalışır."],
      ["AC ile çalışan transformatör"], ["Nitel"], ["Bobini 'gerilim depolayan' eleman sanmak"]),
    M(["Tek satır: 'Vs'nin Vp'ye oranı Ns'nin Np'ye oranına eşit' → bir satırdan ikinci satıra çarpanla git. DC bağlıysa → Vs = 0."],
      ["AC, düzenli tablo"], ["DC / çekirdeksiz yapı"], ["Oranı ters (Np/Ns) kurmak"]),
    M(["Sayısal yol: Vs = Vp·(Ns/Np) ile eksik hücre hesaplanır; sonuç ölçülenle karşılaştırılır (program hesaplamayı dışlar; kitapta var)."],
      ["İdeal transformatör"], ["Program hesaplamayı dışlar; kitapta var"], ["Hesabı program kapsamında sanmak"]),
    "Transformatör deneyi: Vs ∝ Ns (Vp, Np sabit); Np büyürse Vs küçülür. Tek tek satır çiftleriyle orantıyı kontrol et. DC bağlanırsa kararlı durumda Vs = 0.",
    "Birincil bobini 600 sarımlı, Vp = 3 V (AC) olan bir deneyde ikincil sarım sayısı değiştirilerek şu Vs değerleri ölçülüyor: Ns = 300 → 1,5 V; Ns = 600 → 3,0 V; Ns = 1200 → 6,0 V; Ns = 1800 → 7,5 V. (a) Hangi satır tutarsızdır, doğru değer ne olmalıdır? (b) Vs ile Ns arasındaki ilişkiyi yorumlayınız. (c) Birincil bobine 3 V'luk DC kaynak bağlanırsa kararlı durumda voltmetre ne gösterir? Hangi bobin akıyı üretir, çekirdek ne iş yapar?",
    ["Vs/Ns: 1,5/300 = 3,0/600 = 6,0/1200 = 0,005 V/sarım; 7,5/1800 = 0,0042 → 1800 sarımlı satır tutarsız.",
     "Doğru değer: 0,005·1800 = 9,0 V.", "(b) Ns ikiye katlanınca Vs iki katı: Vs ∝ Ns (Vp, Np sabit). Ns < Np → alçaltıcı, Ns > Np → yükseltici.",
     "(c) DC: kararlı durumda akı sabit → Vs = 0. Birincil bobin akıyı üretir, demir çekirdek akıyı ikincil bobine taşır."],
    "1800 sarımlı satır hatalı (9,0 V olmalı); Vs ∝ Ns; DC'de kararlı durumda voltmetre 0 gösterir.",
    """
import math
rows = [(300, 1.5), (600, 3.0), (1200, 6.0), (1800, 7.5)]
Np, Vp = 600, 3.0
ratio = [Vs / Ns for Ns, Vs in rows]
bad = [i for i, r in enumerate(ratio) if abs(r - 0.005) / 0.005 > 0.05]
assert bad == [3] and abs(0.005 * 1800 - 9.0) < 1e-12
# fiziksel model: çekirdek akısı Φ(t) ortak; Vp = Np dΦ/dt, Vs = Ns dΦ/dt (AC)
w = 2 * math.pi * 50
phi = lambda t: -Vp / (Np * w) * math.cos(w * t)
h = 1e-7
dphi = lambda t: (phi(t + h) - phi(t - h)) / (2 * h)
for Ns, Vs in rows[:3]:
    Vs_pred = max(Ns * dphi(k * 1e-4) for k in range(200))          # tepe oranı: Vs/Vp = Ns/Np
    assert abs(Vs_pred / Vp - Ns / Np) < 1e-3
# DC: birincil akım R–L devresi; Vs = M di/dt kararlı durumda sıfır
R, L, M_ = 1.5, 0.2, 0.15
i = lambda t: (3.0 / R) * (1 - math.exp(-R * t / L))
Vs_dc = lambda t: M_ * (i(t + h) - i(t - h)) / (2 * h)
assert Vs_dc(1e-3) > 1.0 and abs(Vs_dc(5.0)) < 1e-9                 # anlık sıçrama var, kararlı durumda 0
""")

SOLUTIONS["transformer-turns-voltage-current-ratio"] = S(
    M(["Sarım sayılarını karşılaştır: Ns < Np → alçaltıcı, Ns > Np → yükseltici. Hangi bobinin kaynağa bağlı (birincil) olduğuna dikkat et.",
       "Gerilim yönü: yükselticide Vs > Vp, alçaltıcıda Vs < Vp (gerilim sarım sayısıyla aynı yönde değişir).",
       "İdeal transformatörde güç korunur: giriş gücü = çıkış gücü. Gerilim kaç kat artarsa akım o kadar kat AZALIR (ters).",
       "Akım yönü: yükselticide is < ip; alçaltıcıda is > ip.",
       "Oran dili: Vs/Vp = Ns/Np ve is/ip = Np/Ns (akım oranı sarım oranının tersi).",
       "Gerçek transformatörde kayıplar vardır (bobin ısınması, çekirdek kaçakları): çıkış gücü giriş gücünden küçüktür, fark ısıya gider."],
      ["İdeal (kayıpsız) transformatör", "AC kaynak", "Birincil bobin kaynağa bağlı"],
      ["Program hesaplamayı dışlar; kitapta var: Vp/Vs = Np/Ns = is/ip (s. 273)", "Gerçek transformatörde is/ip oranı Np/Ns'den küçüktür", "DC'de çalışmaz"],
      ["Akım oranını sarım oranıyla doğru orantılı almak", "Birincil–ikincil bobinleri karıştırmak", "Gerilim kazanıldığı için gücün de arttığını sanmak"]),
    M(["Güç korunumu: yükseltici transformatör 'gerilim kazandırır' ama akımdan öder; enerji yoktan var olmaz.",
       "Her sarımın gerilimi eşittir: sarım sayısı çok olan bobinde toplam gerilim büyüktür; güç aynıysa akım küçüktür.",
       "Gerçek cihazda ısıya giden kısım nedeniyle çıkış gücü daima girişten azdır."],
      ["Enerji korunumu"], ["Nitel"], ["Gerilimi artıran trafonun enerji de artırdığını sanmak"]),
    M(["Üç adım: (1) Ns/Np → tür, (2) gerilim aynı yönde, (3) akım ters yönde. İdealde P_giriş = P_çıkış; gerçekte P_çıkış < P_giriş."],
      ["İdeal transformatör"], ["Kayıplı gerçek trafo"], ["Akımı da aynı yönde değiştirmek"]),
    M(["Sayısal yol: Vs = Vp·Ns/Np, is = ip·Np/Ns, P = Vp·ip = Vs·is (program hesaplamayı dışlar; kitapta var)."],
      ["İdeal transformatör"], ["Program hesaplamayı dışlar; kitapta var"], ["Sarım oranını ters yazmak"]),
    "Trafo sorusunda 'gerilim sarımla aynı yönde, akım sarımın tersi, güç eşit'. Alçaltıcı → ikincil akım büyük. Gerçek trafoda çıkış gücü küçük (ısı).",
    "İdeal bir transformatörün birincil bobini 1200, ikincil bobini 300 sarımlıdır. (a) Yükseltici mi alçaltıcı mı? (b) Vs, Vp'nin kaçta kaçıdır; is, ip'nin kaç katıdır? (c) Giriş ve çıkış güçleri nasıl karşılaştırılır? (d) Sarım sayıları yer değiştirirse (birincil 300, ikincil 1200) gerilim ve akımlar nasıl değişir? (e) Gerçek transformatörde güç ilişkisi nasıl olur?",
    ["(a) Ns < Np → alçaltıcı.", "(b) Vs/Vp = Ns/Np = 1/4 → Vs = Vp/4; is/ip = Np/Ns = 4 → is = 4·ip.",
     "(c) Vs·is = (Vp/4)(4ip) = Vp·ip → güçler eşit.", "(d) Yükseltici olur: Vs = 4Vp, is = ip/4; güç yine eşit.", "(e) Gerçekte P_çıkış < P_giriş (fark ısı)."],
    "(a) Alçaltıcı; (b) Vs = Vp/4, is = 4 ip; (c) eşit; (d) yükseltici: Vs = 4 Vp, is = ip/4; (e) P_çıkış < P_giriş.",
    """
from fractions import Fraction as Fr
import math
def ideal(Np, Ns, Vp, ip):
    Vs = Vp * Fr(Ns, Np)
    is_ = ip * Fr(Np, Ns)                    # güç korunumu: Vp·ip = Vs·is
    return Vs, is_
Vp, ip = Fr(120), Fr(1)
Vs, is_ = ideal(1200, 300, Vp, ip)
assert Vs == Vp / 4 and is_ == 4 * ip and Vs * is_ == Vp * ip
Vs2, is2 = ideal(300, 1200, Vp, ip)
assert Vs2 == 4 * Vp and is2 == ip / 4 and Vs2 * is2 == Vp * ip
# bağımsız: akı yolu — Vp = Np dΦ/dt, Vs = Ns dΦ/dt; akım ters oranda (ortalama güç eşitliği) sinüsle doğrulanır
w = 2 * math.pi * 50
n = 20000
vp = [120 * math.sin(w * k / (50.0 * n)) for k in range(n)]
vs = [v * 300 / 1200 for v in vp]            # Vs/Vp = Ns/Np
ip_t = [1.0 * math.sin(w * k / (50.0 * n)) for k in range(n)]
is_t = [i * 1200 / 300 for i in ip_t]        # is/ip = Np/Ns
Pin = sum(a * b for a, b in zip(vp, ip_t)) / n
Pout = sum(a * b for a, b in zip(vs, is_t)) / n
assert abs(Pin - Pout) / Pin < 1e-9
# gerçek trafo: verim < 1 → is, idealden küçük; çıkış gücü girişten küçük
eta = 0.9
is_real = eta * float(is_)
assert is_real < float(is_) and abs(float(Vs) * is_real - eta * float(Vp * ip)) < 1e-9
# başarısız model: akımı sarım oranıyla doğru orantılı almak güç korunumunu bozar
is_wrong = ip * Fr(300, 1200)
assert Vs * is_wrong != Vp * ip
""")

SOLUTIONS["transformer-chain-and-lamp-comparison"] = S(
    M(["Her transformatör için çarpan: k = Ns/Np (ikincil sarım / birincil sarım). k > 1 yükseltici, k < 1 alçaltıcı.",
       "Özdeş lambalarda parlaklık, lambanın uçlarındaki ikincil gerilimin büyüklüğüne bağlıdır (daha büyük gerilim → daha parlak); aynı kaynağa bağlı trafolarda k'yı karşılaştırarak sırala.",
       "Ardışık bağlı iki transformatörde ilkinin ikincil gerilimi ikincinin birincil gerilimidir: toplam çarpan k₁·k₂ (çarpılır, toplanmaz).",
       "Hedef gerilim için gerekli son çarpanı bul: k_gerekli = V_hedef / V_ara; sarım sayısını buna göre değiştir.",
       "Yapıyı kontrol et: demir çekirdeksiz/açık çekirdekli ya da DC kaynaklı transformatörde ikincil gerilim oluşmaz (ya da çok küçüktür); o lamba yanmaz.",
       "Güç sorusu varsa özdeş lambada P ∝ V² (daha büyük gerilimde daha parlak)."],
      ["İdeal transformatörler", "AC kaynak", "Lambalar özdeş ve doğrusal (direnç sabit)"],
      ["Program hesaplamayı dışlar; kitapta var: kitap 47. Alıştırma sayısal değerlerle sorar", "Lamba direnci sıcaklıkla değişir; parlaklık sıralaması yine de gerilim sıralamasıyla uyumludur", "Çekirdeksiz yapıda oran kullanılamaz"],
      ["Çarpma yerine toplama yapmak", "Oranı (Ns/Np) ters kurmak", "Sarım sayısı fazla olan lambanın hep en parlak olduğunu sanmak (Ns/Np oranına bak)"]),
    M(["Her aşamada gerilim sarım oranı kadar ölçeklenir; aşamalar arka arkaya olduğundan ölçekler çarpılır.",
       "Lamba parlaklığı o lambaya aktarılan güçle ilgilidir; özdeş lambada güç gerilimin karesiyle artar.",
       "Akı olmadan (DC ya da çekirdeksiz) enerji aktarımı yoktur."],
      ["Ardışık trafolar"], ["Nitel"], ["Ara gerilimi atlamak"]),
    M(["k = Ns/Np'yi her trafo için yaz; sırala; zincirde çarp. 'Son gerilim = V₀' için k₁k₂ = 1 yap."],
      ["İdeal trafolar"], ["Çekirdeksiz yapı"], ["k'yı ters yazmak"]),
    None,
    "k = Ns/Np'yi her trafoda yaz; zincirde çarp; parlaklık sırası = k sırası (aynı kaynak). DC ya da çekirdeksiz yapı → lamba yanmaz.",
    "Aynı AC kaynağa (gerilimi V) bağlı üç ideal trafonun sarım sayıları: K (Np = 200, Ns = 100), L (Np = 100, Ns = 300), M (Np = 150, Ns = 150). Her birinin ikincil bobinine özdeş birer lamba bağlı. (a) Lambaları parlaklığa göre sıralayınız. (b) L'nin ikincil bobini, birincil bobini 300 ve ikincil bobini 150 sarımlı bir trafonun birincil bobinine bağlanırsa son gerilim kaç V olur? (c) Son gerilimin tam V olması için ikinci trafonun ikincil sarım sayısı ne olmalıdır? (d) N trafosu DC kaynağa bağlıysa N'nin lambası yanar mı?",
    ["(a) k_K = 100/200 = 1/2, k_L = 3, k_M = 1 → gerilimler V/2, 3V, V → parlaklık L > M > K.",
     "(b) İkinci trafonun k = 150/300 = 1/2 → toplam k = 3·(1/2) = 3/2 → son gerilim 1,5 V.",
     "(c) k_toplam = 1 için k₂ = 1/3 → Np₂ = 300 ise Ns₂ = 100.", "(d) DC'de çekirdekteki akı sabit → ikincil gerilim yok → lamba yanmaz."],
    "(a) L > M > K; (b) 1,5 V; (c) 100 sarım; (d) yanmaz.",
    """
from fractions import Fraction as Fr
def secondary(V, Np, Ns, ac=True, core=True):
    if not ac or not core:
        return Fr(0)
    return V * Fr(Ns, Np)
V = Fr(100)
VK, VL, VM = secondary(V, 200, 100), secondary(V, 100, 300), secondary(V, 150, 150)
assert VK == V / 2 and VL == 3 * V and VM == V and VL > VM > VK
# lamba gücü P = V²/R (özdeş lamba): sıralama gerilim sıralamasıyla aynı
assert VL ** 2 > VM ** 2 > VK ** 2
V_end = secondary(secondary(V, 100, 300), 300, 150)
assert V_end == Fr(3, 2) * V
# (c) son gerilim V olsun: Ns2
Ns2 = [n for n in range(1, 1000) if secondary(secondary(V, 100, 300), 300, n) == V]
assert Ns2 == [100]
# (d) DC kaynak ya da çekirdeksiz yapı → ikincil gerilim yok
assert secondary(V, 100, 300, ac=False) == 0 and secondary(V, 100, 300, core=False) == 0
# başarısız model: gerilimleri toplamak yanlış sonuç verir
assert V * Fr(3) + V * Fr(1, 2) != V_end
""")

SOLUTIONS["transformer-transmission-loss"] = S(
    M(["İletilen güç aynıysa P = V·i: iletim gerilimi ne kadar artarsa hattaki akım o kadar azalır (ters orantı).",
       "Hat telinde kayıp Joule ısınmasıdır: P_kayıp = i²·R. Kayıp akımın KARESİYLE orantılıdır.",
       "Gerilim n kat artarsa akım 1/n, kayıp 1/n² olur. Hat direnci k kat olursa kayıp k kat olur.",
       "Birleşik oran: P_kayıp'ın yeni değeri = (akım çarpanı)²·(R çarpanı); akım çarpanı = 1/(gerilim çarpanı).",
       "Hat modelini yorumla: santral yanında yükseltici (K), şehirde ara/alçaltıcı (L, M): iletim yüksek gerilimde, tüketim güvenli düşük gerilimde yapılır.",
       "Neden direnç azaltılmaz? Daha kalın tel çok pahalı ve ağırdır; gerilimi yükseltmek ekonomik yoldur."],
      ["İletilen güç sabit", "Hat direnci sabit (ya da çarpanı verilmiş)", "İdeal transformatörler (kayıp yalnız hatta)"],
      ["Program hesaplamayı dışlar; kitapta var: P = V·i ve P_kayıp = i²·R (s. 263)", "Yük direnci sabitse gerilim artınca akım ARTAR (sabit güç varsayımı geçersiz olur)", "P_kayıp = V²/R'de V, hattın iki ucu arasındaki gerilim olmalı, şebeke gerilimi değil"],
      ["P = i²R yerine P = iR yazmak", "Yükseltici ve alçaltıcıyı yanlış yere koymak", "Gerilim artınca akımın da arttığını sanmak"]),
    M(["Aynı güç için gerilimi artırmak, daha az yük taşımak demektir: akım azalır, telin ısınması çok azalır.",
       "Akım yarıya inince ısınma dörtte birine iner: telin uçları arasındaki gerilim düşümü (i·R) de yarıya iner ve güç = (düşüm)·(akım) olduğundan iki etki çarpılır (i²R).",
       "Alçaltıcı transformatör, yüksek gerilimli hattı güvenli kullanım gerilimine indirir."],
      ["Enerji iletimi"], ["Nitel"], ["Kaybı artıran şeyin gerilim olduğunu sanmak"]),
    M(["Gerilim n kat ↑ → akım n kat ↓ → kayıp n² kat ↓. Direnç çarpanı doğrudan kayıp çarpanıdır."],
      ["Sabit güç, sabit hat"], ["Yük değişirse geçersiz"], ["n yerine n² kullanmamak"]),
    M(["Sayısal yol: i = P/V, P_kayıp = i²R ile iki durumu hesapla ve oranla (program hesaplamayı dışlar; kitapta var)."],
      ["Sabit güç"], ["Program hesaplamayı dışlar; kitapta var"], ["Birimleri (kV → V) çevirmemek"]),
    "İletimde 'gerilim ×n → akım /n → kayıp /n²'. Direnç çarpanı kayıp çarpanıdır. Yükseltici santral yanında, alçaltıcı tüketici yanında.",
    "Bir santralin ürettiği güç aynı iletim hattından taşınıyor. (a) İletim gerilimi 5 katına çıkarılırsa hattaki akım ve hattaki enerji kaybı kaç katına çıkar? (b) Gerilim değişmeden hat direnci yarıya inerse kayıp ne olur? (c) Gerilim 4 katına çıkarılır ve eski telin yerine direnci 2 katı olan bir tel kullanılırsa kayıp kaç katı olur? (d) K (santral yanı) ve M (ev yanı) transformatörleri hangi türdedir?",
    ["Sabit güç: i ∝ 1/V; P_kayıp = i²R.", "(a) i ×1/5, kayıp ×1/25.", "(b) Kayıp ×1/2.", "(c) i ×1/4 → i² ×1/16; R ×2 → kayıp ×2/16 = ×1/8.", "(d) K yükseltici, M alçaltıcı."],
    "(a) i → 1/5, kayıp → 1/25; (b) kayıp yarıya iner; (c) kayıp 1/8; (d) K yükseltici, M alçaltıcı.",
    """
P, R = 1.0e6, 10.0                          # W, Ω
loss = lambda V, R_: (P / V) ** 2 * R_       # P_kayıp = i² R, i = P/V
V0 = 20e3
L0 = loss(V0, R)
assert abs(loss(5 * V0, R) / L0 - 1 / 25) < 1e-12
assert abs((P / (5 * V0)) / (P / V0) - 1 / 5) < 1e-12
assert abs(loss(V0, R / 2) / L0 - 0.5) < 1e-12
assert abs(loss(4 * V0, 2 * R) / L0 - 1 / 8) < 1e-12
assert abs(L0 - 25e3) < 1e-6 and abs(loss(100e3, R) - 1e3) < 1e-6      # 2,5 % → 0,1 %
# başarısız durum 1: yük direnci sabitse gerilim artınca akım artar (sabit güç varsayımı geçersiz)
R_load = 100.0
i_load = lambda V: V / R_load
assert i_load(5 * V0) > i_load(V0)
# başarısız durum 2: kayıpta şebeke gerilimi kullanmak (V²/R, V hattın iki ucu arasında değil) hatalı sonuç verir
V_drop = (P / V0) * R                        # hat uçları arasındaki gerilim düşümü
assert abs(V_drop ** 2 / R - L0) < 1e-9 and abs(V0 ** 2 / R - L0) > 1e6
""")

SOLUTIONS["transformer-applications-record"] = S(
    M(["Kayıt tablosunda her satır için kaynak gerilimini (şebeke ya da önceki kademe) ve cihazın gerekli gerilimini yaz.",
       "Cihaz gerilimi < kaynak gerilimi → alçaltıcı; cihaz gerilimi > kaynak gerilimi → yükseltici; eşitse transformatör gerekmez.",
       "Yazılı rolü bu kuralla karşılaştır; çelişen hücre yanlıştır, eksik hücreyi aynı kuralla doldur.",
       "Rol, transformatörün hangi bobininin kaynağa bağlı olduğuna bağlıdır; aynı trafo ters bağlanırsa rolü de tersine döner.",
       "Cihazın etiketi (ör. 110 V) cihazın ihtiyaç duyduğu gerilimdir, şebeke gerilimi değildir; şebekeden farklıysa dönüştürücü (transformatör) gerekir.",
       "Her kayıtta üç öge olsun: uygulama, rol (yükselten/alçaltan), kaynak (kitap sayfası / araştırma)."],
      ["Alternatif akım şebekesi", "Cihaz geriliminin ve kaynak geriliminin değerleri belli"],
      ["Transformatör yalnız gerilimin büyüklüğünü değiştirir; doğru akımla çalışan cihaz (telefon şarjı) ayrıca doğrultucu ister", "Program yalnız rolü yorumlatır; sayısal sarım oranı hesabı programda yoktur", "Hat modelinde santral yanı yükseltici, tüketici yanı alçaltıcıdır; ara trafoda kademeye bakılmalı"],
      ["Uygulama ile rolünü karıştırmak", "Cihaz etiketindeki gerilimi şebeke gerilimi sanmak", "Ters bağlanan trafonun rolünü sabit saymak"]),
    M(["Transformatörün görevi, mevcut gerilimi cihazın istediği gerilime dönüştürmektir: yüksek gerilimli hat → ev gerilimi → cihaz gerilimi.",
       "İletim hatlarında yükseltme, kaybı azaltmak içindir; evde alçaltma güvenlik ve cihaz uyumu içindir.",
       "Uygun olmayan gerilimde çalışan cihaz yanabilir (110 V cihaz 220 V şebekede) ya da çalışmaz."],
      ["Kullanım alanı yorumu"], ["Nitel"], ["Transformatörün enerji ürettiğini sanmak"]),
    M(["Her satırda iki sayıyı karşılaştır: cihaz < kaynak → alçaltıcı; cihaz > kaynak → yükseltici. Yazılı rolle uyuşmuyorsa hatalı."],
      ["AC kaynak"], ["Ters bağlama, doğrultucu gereksinimi"], ["Sayıların yerini karıştırmak"]),
    None,
    "Tabloda rol = (cihaz gerilimi ile kaynak gerilimini karşılaştır). Küçülüyorsa alçaltıcı, büyüyorsa yükseltici. 110 V cihaz + 220 V şebeke → alçaltıcı dönüştürücü gerekir.",
    "Bir öğrenci kayıt tablosuna şunları yazmıştır: (1) Cep telefonu şarj aleti: 230 V → 5 V, alçaltıcı. (2) Mikrodalga fırının yüksek gerilim bölümü: 230 V → 2000 V, alçaltıcı. (3) Santral çıkışı: 10 kV → 150 kV, yükseltici. (4) Şehir girişi: 150 kV → 10 kV, yükseltici. (5) 110 V ile çalışan cihaz 230 V şebekede: dönüştürücü gerekir, yükseltici. Hangi hücreler hatalıdır, doğru roller nedir? 110 V'luk cihaz dönüştürücüsüz 230 V şebekeye bağlanırsa ne olur?",
    ["Kural: cihaz/çıkış gerilimi < giriş → alçaltıcı; > giriş → yükseltici.",
     "(1) 5 < 230 → alçaltıcı (doğru). (2) 2000 > 230 → YÜKSELTİCİ (yazılan hatalı). (3) 150 kV > 10 kV → yükseltici (doğru). (4) 10 kV < 150 kV → ALÇALTICI (yazılan hatalı).",
     "(5) 110 V < 230 V → ALÇALTICI dönüştürücü (yazılan hatalı).", "Dönüştürücüsüz bağlanırsa cihaz gereğinden yüksek gerilim alır; zarar görür/yanar."],
    "Hatalı hücreler 2, 4, 5: doğru roller yükseltici, alçaltıcı, alçaltıcı; dönüştürücüsüz bağlanırsa cihaz yüksek gerilimle zarar görür.",
    """
def role(v_in, v_out):
    return "alçaltıcı" if v_out < v_in else "yükseltici" if v_out > v_in else "gerekmez"
table = [(1, 230, 5, "alçaltıcı"), (2, 230, 2000, "alçaltıcı"), (3, 10e3, 150e3, "yükseltici"),
         (4, 150e3, 10e3, "yükseltici"), (5, 230, 110, "yükseltici")]
wrong = [i for i, vin, vout, r in table if role(vin, vout) != r]
assert wrong == [2, 4, 5]
assert [role(vin, vout) for i, vin, vout, r in table if i in wrong] == ["yükseltici", "alçaltıcı", "alçaltıcı"]
# ters bağlama: aynı trafoyu çevirince rol tersine döner
assert role(5, 230) == "yükseltici" and role(230, 5) == "alçaltıcı"
# cihazın etiketi (110 V) şebeke değildir: gerilim oranı 230/110 > 1 → dönüştürücüsüz bağlanınca aşırı gerilim
assert 230 / 110 > 1.5
# başarısız durum: eşit gerilimde trafo gerekmez
assert role(230, 230) == "gerekmez"
""")


# =====================================================================================================
# KISA YOLLAR (SHORTCUTS) — Ünite 2
# Kapsam: 11.2.1 / 11.2.2 / 11.2.5 / 11.2.13 hesapsız — kısa yollar oran, yön, tablo yorumu düzeyindedir;
# numeric_check yalnız kısa yolun doğruluğunu tam yöntemle sınar (öğrenciden sayısal hesap beklenmez).
# =====================================================================================================

# ---------------- Coulomb ve elektrik alan ----------------
SHORTCUTS += [
    SC("inverse-square-multiplier-method", "Çarpan yöntemi: q çarpanları / d çarpanının karesi / k çarpanı",
       ["coulomb-ratio-generalization", "coulomb-collinear-net-force", "efield-point-charge-ratio"],
       "F (ya da E) yeni = F·(q₁ çarpanı)(q₂ çarpanı)(k çarpanı)/(d çarpanı)²; E için yalnız kaynak yükü (q) çarpanı, F için iki yük çarpanı.",
       "F = k·q₁q₂/d² ve E = k·q/d² bağıntıları çarpımsal olduğundan her değişkenin çarpanı bağımsız olarak çarpılır; d'nin çarpanı ters kare gelir.",
       ["Noktasal (ya da küresel simetrik, uzak) yükler", "Ortam k'si değişiyorsa çarpanı verilmiş", "Yük miktarları sabit kalıyor"],
       ["d çarpanını karesiz kullanmak ('d iki katına çıkınca F yarıya iner') yanlıştır", "Yükler arasında temas/paylaşım varsa yeni yükler önce bulunmalı (çarpımın işareti bile değişebilir)", "Çok yakın mesafede iletken kürelerin yük dağılımı bozulur, noktasal model geçersiz", "Program hesaplamayı dışlar; oran düzeyinde kullanılır, kitapta k·q₁q₂/d² var"],
       "LOW", [TB("s. 159 14. adım tablosu"), TB("s. 163 1. Alıştırma"), DV("F = k·q₁·q₂/d² çarpımsal; ortak sabitler oranda sadeleşir")],
       """
import random
from fractions import Fraction as Fr
random.seed(11)
F = lambda k, q1, q2, d: k * q1 * q2 / d ** 2
for _ in range(300):
    k = 9e9; q1, q2 = random.uniform(1e-9, 9e-9), random.uniform(1e-9, 9e-9); d = random.uniform(0.01, 0.2)
    a, b, c, e = (random.choice([Fr(1, 3), Fr(1, 2), 2, 3, 4]) for _ in range(4))
    full = F(k * float(e), q1 * float(a), q2 * float(b), d * float(c)) / F(k, q1, q2, d)
    assert abs(full / float(a * b * e / c ** 2) - 1) < 1e-9
# başarısız durum 1: d çarpanını karesiz almak
assert abs(F(1, 1, 1, 2) / F(1, 1, 1, 1) - 1 / 2) > 0.2           # gerçek 1/4, yanlış kısa yol 1/2
# başarısız durum 2: temas sonrası yük paylaşımı (özdeş iletken küreler): çarpım ve işaret değişir
q1, q2 = 4.0, -2.0
q1n = q2n = (q1 + q2) / 2
assert q1 * q2 < 0 < q1n * q2n                                      # çekmeden itmeye geçer; eski çarpanlarla çarpmak yanlış
""")
    ,
    SC("constant-ratio-column-table", "Sabit oran sütunu: tablodan model testi ve eksik hücre",
       ["coulomb-data-table-graph", "efield-data-table-graph", "wire-field-data-model", "solenoid-data-model", "wire-force-data-model"],
       "Tabloya modelin 'çıktı·(ters etmenler)/(doğru etmenler)' sütununu ekle (F·d²/q₁q₂, E·d²/q, B·d/i, B·L/(iN), F/(B·i·L·sinθ)); sütun sabitse model doğrudur ve eksik hücre bu sabitle tamamlanır, sabit değilse model yanlıştır.",
       "Doğru orantı ve ters orantı bileşenlerinden oluşan bir bağıntı (y = c·∏xᵢ^pᵢ) her satırda aynı c'yi verir; yanlış üs sütunu sabit tutmaz.",
       ["Çıktıyı etkileyen tüm değişkenler tabloda bulunuyor", "Üs değerleri (modelde 1 ya da 2) bilinir ya da denenir", "Ölçüm hatası küçük (tolerans payıyla)"],
       ["Ölçüm gürültüsü varsa oran tam sabit çıkmaz: tolerans düşünülmeli, tek sapmaya bakıp modeli reddetmemek", "Tabloda tablo dışı bir değişken (ortam, sıcaklık) de değişmişse sütun sabit çıkmaz", "Yanlış üsle (ör. 1/d yerine 1/d²) sütun sabit çıkmaz — bu bir hata değil, modelin yanlış olduğunu gösterir", "Program yalnız yorumu ister; sabitin sayısal değeri sorulmaz"],
       "MEDIUM", [TB("s. 158 10. adım"), TB("s. 167 10. adım"), TB("s. 204 Örnek cevabı"), TB("s. 208 6.–7. adım"), TB("s. 220 7.–9. adım"), DV("y = c·∏ xᵢ^pᵢ ⇒ y/∏ xᵢ^pᵢ = c")],
       """
import random, math
random.seed(3)
# her yasa: (şekil fonksiyonu, sabit c): y = c·şekil → sütun y/şekil sabittir
laws = {"coulomb": (lambda q1, q2, d: q1 * q2 / d ** 2, 9.0), "efield": (lambda q, d: q / d ** 2, 9.0),
        "wire": (lambda i, d: i / d, 0.2), "solenoid": (lambda i, N, L: i * N / L, 1.2),
        "force": (lambda B, i, L, s: B * i * L * s, 1.0)}
for name, (shape, c) in laws.items():
    n = shape.__code__.co_argcount
    rows = [[random.uniform(0.5, 5) for _ in range(n)] for _ in range(6)]
    ys = [c * shape(*r) for r in rows]
    cs = [y / shape(*r) for y, r in zip(ys, rows)]               # sütun: çıktı / (doğru etmenler / ters etmenler)
    assert max(cs) - min(cs) < 1e-9 * max(cs)                      # sütun sabit
    hidden = ys[-1]                                                # eksik hücre: sabitle tamamlanır
    assert abs(cs[0] * shape(*rows[-1]) - hidden) < 1e-9 * hidden
# başarısız durum 1: yanlış üs → sütun sabit değil
rows = [(q, d) for q, d in [(1, 1), (1, 2), (2, 3), (1, 4)]]
wrong = [9.0 * q / d ** 2 * d / q for q, d in rows]                # d çarpanı (1 yerine 2 üs) yanlış
assert max(wrong) - min(wrong) > 1.0
# başarısız durum 2: gürültü — %5 hata ile tam eşitlik testi başarısız, tolerans testi başarılı
noisy = [9.0 * (1 + random.uniform(-0.05, 0.05)) for _ in range(6)]
assert max(noisy) != min(noisy) and (max(noisy) - min(noisy)) / 9.0 < 0.12
""")
    ,
    SC("two-row-exponent-log-slope", "İki satırdan üs bulma: p = ln(y₂/y₁)/ln(x₂/x₁)",
       ["coulomb-data-table-graph", "efield-data-table-graph", "wire-field-data-model", "solenoid-data-model"],
       "Yalnız bir değişkenin (x) değiştiği iki satırda çıktı y'nin üssü p = ln(y₂/y₁)/ln(x₂/x₁): d için ≈ −2 → ters kare; −1 → ters orantı; +1 → doğru orantı. Grafik: log–log doğrusu.",
       "y = c·xᵖ ise ln y = ln c + p·ln x doğrusaldır; iki noktadan eğim p'yi verir.",
       ["Satır çifti yalnız bir değişkende farklı", "Güç yasası biçimli ilişki"],
       ["İki değişkenin birden değiştiği satır çiftinde sonuç yanlıştır (ör. q ve d birlikte değişirse p anlamsızdır)", "İlişki güç yasası değilse (ör. doygunluk, eşik) tek üs yoktur", "Ölçüm hatası tek çiftte büyük etki yapar: mümkünse iki çift kullan"],
       "MEDIUM", [TB("s. 158 10. adım"), TB("s. 167 9.–10. adım"), DV("ln y = ln c + p·ln x doğru denklemi")],
       """
import math
y = lambda q, d: 3.0 * q / d ** 2
# tek değişkenli çift: d ×3 → y ÷9 → p = −2
p = math.log(y(2, 6) / y(2, 2)) / math.log(6 / 2)
assert abs(p + 2) < 1e-12
# q ×3 → p = +1
assert abs(math.log(y(6, 2) / y(2, 2)) / math.log(3) - 1) < 1e-12
# başarısız: iki değişken birden değişir (q ×3 ve d ×3) → p = −1 gibi görünür (yanlış üs)
p_bad = math.log(y(6, 6) / y(2, 2)) / math.log(3)
assert abs(p_bad + 2) > 0.5
# başarısız: güç yasası olmayan ilişki (y = d + 1/d) için iki farklı çiftte farklı üs çıkar
f = lambda d: d + 1 / d
p1 = math.log(f(2) / f(1)) / math.log(2); p2 = math.log(f(4) / f(2)) / math.log(2)
assert abs(p1 - p2) > 0.3
""")
    ,
    SC("coulomb-sign-product-direction", "İşaret çarpımı → yön; kuvvetler eşit (Newton 3); ivme ∝ 1/m",
       ["coulomb-direction-newton3", "coulomb-free-charge-dynamics"],
       "(+)(+) ve (−)(−) → itme; (+)(−) → çekme. İki yükün birbirine uyguladığı kuvvetler eşit büyüklükte, zıt yönlü; serbest bırakılırsa ivmelerin oranı kütlelerin tersi.",
       "Coulomb kuvveti yük çarpımının işaretiyle yön kazanır ve ikili etkileşim etki–tepki çiftidir; F = m·a ⇒ a = F/m.",
       ["İki noktasal yükün etkileşimi", "Yalnız elektriksel kuvvet (ağırlık ihmal)"],
       ["Üçüncü bir yük varsa net kuvvet vektörel toplamdır; tek çiftin yönü yetmez", "Kuvvet yaklaşırken artar: sabit ivme formülleri kullanılamaz", "Birine kuvvet uygulayan yük büyük diye kuvvetin büyük olduğu sanılır: büyüklükler eşittir"],
       "LOW", [TB("s. 162 Örnek"), TB("s. 164 3. Alıştırma"), TB("s. 165 4. Alıştırma"), DV("Newton'un 3. yasası, Coulomb yasası")],
       """
import random
random.seed(5)
def force_on_1(q1, x1, q2, x2):
    d = x1 - x2
    return q1 * q2 / d ** 2 * (1 if d > 0 else -1)                # (x ekseni) k = 1
for _ in range(500):
    q1, q2 = random.choice([-1, 1]) * random.uniform(0.5, 9), random.choice([-1, 1]) * random.uniform(0.5, 9)
    x1, x2 = random.uniform(-5, 5), random.uniform(-5, 5)
    if abs(x1 - x2) < 0.1: continue
    f1, f2 = force_on_1(q1, x1, q2, x2), force_on_1(q2, x2, q1, x1)
    assert abs(f1 + f2) < 1e-9                                      # eşit büyüklük, zıt yön
    repel = (f1 > 0) == (x1 > x2)                                   # 1. yük diğerinden uzağa itiliyor mu
    assert repel == (q1 * q2 > 0)                                   # işaret çarpımı kuralı
    m1, m2 = random.uniform(1, 9), random.uniform(1, 9)
    assert abs((f1 / m1) / (f2 / m2) + m2 / m1) < 1e-9              # |a1|/|a2| = m2/m1
# başarısız: üçüncü yük varsa tek çifte bakmak net yönü verir mi? (verme)
qs, xs = [1.0, -1.0, 3.0], [0.0, 1.0, 1.5]
net_on_2 = force_on_1(qs[1], xs[1], qs[0], xs[0]) + force_on_1(qs[1], xs[1], qs[2], xs[2])
only_pair = force_on_1(qs[1], xs[1], qs[0], xs[0])
assert (net_on_2 > 0) != (only_pair > 0)                            # net yön, tek çiftin yönünden farklı
""")
    ,
    SC("collinear-f-unit-table", "Doğrusal yük dizisinde F birimi tablosu ve net kuvvetlerin toplamı sıfır",
       ["coulomb-collinear-net-force", "efield-superposition-collinear"],
       "Tüm çiftler için 'q-çarpımı/(d çarpanı)²' değerini F (ya da E₀) biriminde yaz, yön işaretle ekle; her yüke gelen net kuvveti topla. Kontrol: üç yükün net kuvvetlerinin toplamı sıfırdır.",
       "Her çiftin kuvveti ayrı hesaplanır (süperpozisyon) ve iç kuvvetler Newton 3 ile ikişer ikişer götürür.",
       ["Yükler aynı doğru üzerinde", "Her çift için noktasal Coulomb kuvveti"],
       ["Yükler aynı doğru üzerinde değilse işaretli toplama yetmez, vektör bileşenleri gerekir", "Toplamın sıfır çıkması sonuçların doğruluğunun gerekli koşuludur, yeterli değil", "Alan sorusunda (E₀) toplam sıfır kontrolü uygulanmaz; yalnız kuvvetlerde geçerli"],
       "MEDIUM", [TB("s. 163 1. Alıştırma"), TB("s. 276 ÖD-3"), TB("s. 172 Örnek"), DV("Süperpozisyon + Newton 3")],
       """
import random
from fractions import Fraction as Fr
random.seed(8)
def nets(q, x):
    out = []
    for i in range(len(q)):
        s = Fr(0)
        for j in range(len(q)):
            if j != i:
                d = x[i] - x[j]
                s += q[i] * q[j] / d ** 2 * (1 if d > 0 else -1)
        out.append(s)
    return out
for _ in range(200):
    q = [Fr(random.choice([-3, -2, -1, 1, 2, 3])) for _ in range(3)]
    x = sorted(random.sample(range(0, 12), 3)); x = [Fr(v) for v in x]
    assert sum(nets(q, x)) == 0                                     # toplam sıfır
# başarısız: alan sorusunda toplam sıfır kuralı yok
q, x = [Fr(1), Fr(-2), Fr(1)], [Fr(0), Fr(1), Fr(3)]
def E(p):
    s = Fr(0)
    for qq, xx in zip(q, x):
        d = p - xx
        s += qq / d ** 2 * (1 if d > 0 else -1)
    return s
assert sum(E(p) for p in (Fr(-1), Fr(2), Fr(5))) != 0
""")
    ,
    SC("field-lines-three-rules", "Alan çizgisi üç kuralı: çıkış + / giriş −; çizgi sayısı ∝ |q|; sıklık ∝ E",
       ["efield-direction-and-lines", "magnet-field-lines-pattern"],
       "Çizgi çıkıyorsa yük pozitif, giriyorsa negatif; çizgi sayısı oranı yük büyüklükleri oranına eşit; birim alandaki çizgi sayısı o noktadaki alan büyüklüğünü gösterir.",
       "Çizgi sayısı, yükü saran kapalı yüzeyden geçen toplam alan çizgisi sayısıdır (Gauss yasası ile q'ya orantılı); çizgi yoğunluğu |E| ile orantılı çizilir.",
       ["Çizgiler aynı çizimde, aynı ölçekte çizilmiş", "Yükü tamamen çevreleyen yüzeyden çıkan toplam çizgi sayılıyor"],
       ["Yükü çevrelemeyen yüzeyde net çizgi sayısı sıfırdır (giren ve çıkan eşit)", "Farklı çizimler arası çizgi sayısı karşılaştırılamaz (ölçek yok)", "Çizgiler birbirini kesmez; kesişen çizgili şekil yanlıştır", "Program hesaplamayı dışlar; yalnız nitel kullanım"],
       "HIGH", [TB("s. 173 6. Alıştırma"), TB("s. 185 Özet"), DV("Gauss yasası: Φ_E = q/ε₀ — kapalı yüzeyden çıkan çizgi sayısı ∝ q")],
       """
import math
def flux(q, pos, R=1.0, n=60):
    # küre yüzeyi üzerinden net alan çizgisi (E·n dA); k = 1
    s = 0.0
    for a in range(n):
        th = math.pi * (a + 0.5) / n
        for b in range(2 * n):
            ph = math.pi * (b + 0.5) / n
            nx, ny, nz = math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)
            rx, ry, rz = R * nx - pos[0], R * ny - pos[1], R * nz - pos[2]
            r3 = (rx * rx + ry * ry + rz * rz) ** 1.5
            s += q * (rx * nx + ry * ny + rz * nz) / r3 * R * R * math.sin(th) * (math.pi / n) ** 2
    return s
f1 = flux(1.0, (0, 0, 0)); f2 = flux(2.0, (0.3, -0.2, 0.1)); fm = flux(-1.0, (0.2, 0.2, 0))
assert abs(f1 / (4 * math.pi) - 1) < 1e-3 and abs(f2 / f1 - 2) < 1e-2 and abs(fm / f1 + 1) < 1e-2    # çıkış +, sayı ∝ |q|, giriş −
# sıklık ∝ |E|: d → 2d alan 1/4
assert abs((1 / 1 ** 2) / (1 / 2 ** 2) - 4) < 1e-12
# başarısız: yükü çevrelemeyen yüzeyden net çizgi sıfır
assert abs(flux(1.0, (3.0, 0, 0))) < 1e-3
""")
    ,
    SC("deflection-sign-q-over-m", "Sapma yönünden işaret; aynı hızda sapma ∝ |q|/m",
       ["efield-charged-particle-deflection", "efield-force-balance-droplet"],
       "Parçacık hangi levhaya sapıyorsa o levhanın TERSİ işaretlidir (pozitif levhaya sapan negatif); sapmayan yüksüzdür; aynı hızla girenlerde sapma miktarı oranı |q|/m oranına eşittir.",
       "F = qE yönü işarete bağlı; yatay hız v ile levha boyunca geçme süresi t = L/v ortak, dikey sapma y = ½(qE/m)t² ∝ q/m.",
       ["Düzgün alan, parçacıklar levhalara paralel ve aynı v ile giriyor", "Yer çekimi ihmal ya da hesaba katılmış"],
       ["Girişte hızlar farklıysa sapma ∝ q/(m·v²) olur, yalnız q/m oranı yetmez", "Parçacık levhaya çarparsa ya da levha dışına çıkarsa y = ½at² geçersiz", "Yer çekimi ihmal edilemeyecek kadar büyükse (ağır damlacık) net kuvvete bakılmalı"],
       "MEDIUM", [TB("s. 176 Elektron tabancası"), TB("s. 275 ÖD-2"), DV("y = ½(qE/m)(L/v)²")],
       """
def deflect(q, m, v, E=1000.0, L=0.1, steps=4000):
    t_end = L / v; dt = t_end / steps; y = vy = 0.0
    for _ in range(steps):
        vy += q * E / m * dt; y += vy * dt                           # +y: pozitif levhadan negatif levhaya (alan yönü)
    return y
y1 = deflect(1e-6, 1e-3, 50.0)
y2 = deflect(3e-6, 1e-3, 50.0); y3 = deflect(1e-6, 3e-3, 50.0); yn = deflect(-1e-6, 1e-3, 50.0); y0 = deflect(0.0, 1e-3, 50.0)
assert abs(y2 / y1 - 3) < 5e-3 and abs(y3 / y1 - 1 / 3) < 5e-3     # sapma ∝ q/m
assert y1 > 0 > yn and y0 == 0.0                                     # işaret: alan yönünde / ters yönde / sapmaz
# başarısız: farklı hız → oran q/m'den farklı
y4 = deflect(1e-6, 1e-3, 100.0)
assert abs(y4 / y1 - 1) > 0.5 and abs(y4 / y1 - 0.25) < 5e-3
""")
    ,
    SC("plate-field-v-over-d", "Paralel levhalarda E oranı = (V çarpanı)/(d çarpanı) — üretece bağlıysa",
       ["efield-uniform-plates"],
       "Levhalar üretece bağlıyken E = V/d: gerilim çarpanı bölü uzaklık çarpanı; çizgiler paralel ve eşit aralıklıdır. Yalnız levhalar ayrılıp yük sabitse E değişmez.",
       "Düzgün alanda gerilim V = E·d. Üreteç V'yi sabit tutarsa d artınca E azalır.",
       ["Levhalar sonsuz büyük gibi (düzgün alan)", "Levhalar üretece bağlı (V verilmiş/sabit)"],
       ["Üreteçten ayrılmış (yük sabit) levhalarda d değişince E değişmez (E = σ/ε₀); V değişir", "Levha kenarlarında alan düzgün değildir", "Program hesaplamayı dışlar; oran yorumu"],
       "MEDIUM", [TB("s. 176 Paralel levha"), TB("s. 177 9. Alıştırma"), TB("s. 178 10. Alıştırma a"), DV("V = E·d")],
       """
import random
random.seed(2)
eps0 = 8.85e-12
for _ in range(200):
    V, d = random.uniform(5, 50), random.uniform(0.01, 0.1)
    a, b = random.choice([0.5, 1.5, 2, 3]), random.choice([0.5, 2, 4])
    full = ((a * V) / (d / b)) / (V / d)
    assert abs(full - a * b) < 1e-9                                  # V çarpanı a, d çarpanı 1/b → E çarpanı a·b
# başarısız: yük sabit (üreteç ayrılmış) → E değişmez, V = E d değişir
A, Q = 0.01, 1e-9
E = lambda d: Q / (eps0 * A)                                         # d'den bağımsız
V = lambda d: E(d) * d
assert E(0.02) == E(0.04) and V(0.04) == 2 * V(0.02)
""")
    ,
    SC("force-comparison-hover-rule", "qE ile mg karşılaştır: =  askıda, > yukarı ivme, < aşağı ivme",
       ["efield-force-balance-droplet", "wire-force-balance-dynamics"],
       "Elektriksel (ya da manyetik) kuvvetin büyüklüğünü ağırlıkla karşılaştır: eşitse dengede, büyükse kuvvet yönünde, küçükse ağırlık yönünde ivme; yönü kuvvetin işaretinden ve alan yönünden kontrol et.",
       "Net kuvvet F_net = F_e − mg (yukarı pozitif); a = F_net/m, işareti hareketin yönünü verir.",
       ["Tek doğrultuda (düşey) iki baskın kuvvet", "Kuvvet ve ağırlık aynı doğru üzerinde"],
       ["Hava direnci ya da başka kuvvet varsa yalnız iki kuvvete bakmak yetmez", "Alan yatay/eğikse bileşenlere ayırmadan karşılaştırma yapılamaz", "Elektron gibi çok hafif parçacıklarda mg ihmal edilir (qE ≫ mg)"],
       "MEDIUM", [TB("s. 277 ÖD-5"), TB("s. 284 ÖD-13"), TB("s. 228 29. Alıştırma"), DV("ΣF = m·a")],
       """
import random
random.seed(4)
g = 10.0
def displacement_sign(Fe, m, t=0.05, dt=1e-5):
    y = v = 0.0
    for _ in range(int(t / dt)):
        a = (Fe - m * g) / m; v += a * dt; y += v * dt
    return y
for _ in range(100):
    m = random.uniform(0.01, 1.0)
    Fe = m * g * random.choice([0.5, 1.0, 1.7, 3.0])
    y = displacement_sign(Fe, m)
    rule = 0 if abs(Fe - m * g) < 1e-12 else (1 if Fe > m * g else -1)
    assert (y > 1e-9) == (rule == 1) and (y < -1e-9) == (rule == -1) and (abs(y) < 1e-9) == (rule == 0)
# başarısız: hava direnci / başka kuvvet — yalnız iki kuvvete bakmak yetmez (limit hıza ulaşınca denge)
kdrag, m = 5.0, 0.1
v = 0.0
for _ in range(200000):
    v += ((0.5 * m * g * 3) - m * g - kdrag * v) / m * 1e-5            # Fe > mg ama sürüklenme varsa sınırlı hız
assert abs(v - (0.5 * m * g * 3 - m * g) / kdrag) < 1e-3
""")
    ,
]

# ---------------- Mıknatıs, akım ve manyetik alan, manyetik kuvvet ----------------
SHORTCUTS += [
    SC("magnet-pole-scale-reading", "Mıknatıs–terazi: aynı kutup itme → okuma artar; zıt kutup çekme → okuma azalır",
       ["magnet-pole-interaction"],
       "Teraziye konan mıknatısın üstündeki (dışarıdan tutulan) mıknatıs aynı kutupla bakıyorsa aşağı iter, okuma ağırlıktan büyük olur; zıt kutupla bakıyorsa yukarı çeker, okuma küçülür; mesafe azaldıkça fark büyür.",
       "Terazi, üzerindeki cisme gelen toplam aşağı yönlü kuvveti (ağırlık + manyetik kuvvet bileşeni) okur; manyetik kuvvet kutup işaretiyle yön kazanır.",
       ["Üstteki mıknatıs terazi dışında bir desteğe bağlı", "Kuvvet düşey doğrultuda"],
       ["İki mıknatıs da aynı terazinin üzerindeyse iç kuvvetler götürür: okuma yalnız toplam ağırlıktır", "Mıknatısın yatay kayması/dönmesi olursa düşey bileşene bakılmalı", "Kuvvet mesafeyle monoton değildir: program yalnız 'yaklaştıkça artar' nitel ilişkisini ister"],
       "LOW", [TB("s. 192 Örnek"), TB("s. 279 ÖD-8"), DV("Terazi okuması = (ağırlık ± F_manyetik)/g")],
       """
g = 10.0
def reading(m, p_low, p_up, r, ext_support=True):
    F = p_low * p_up / r ** 2                       # >0 itme (k = 1), kutup işaretleri çarpılır
    return (m * g + (F if ext_support else 0.0)) / g
base = 0.5
rep, att = reading(base, +1, +1, 0.1), reading(base, +1, -1, 0.1)
assert rep > base > att
assert reading(base, +1, +1, 0.05) - base > reading(base, +1, +1, 0.1) - base      # yaklaştıkça fark büyür
assert (reading(base, +1, -1, 0.05) - base) < (reading(base, +1, -1, 0.1) - base)
# başarısız: iki mıknatıs da aynı terazide → iç kuvvet götürür, okuma değişmez (toplam ağırlık)
def reading_both(m1, m2):
    return (m1 * g + m2 * g) / g
assert reading_both(0.5, 0.3) == 0.8
""")
    ,
    SC("compass-3-4-5-vector", "Dik iki alan: bileşke Pisagor (3-4-5), yön tanθ = karşı/komşu",
       ["magnet-vector-compass-earth"],
       "Birbirine dik iki alan B₁, B₂ ise bileşke √(B₁²+B₂²) (3-4-5, 5-12-13 üçlüleriyle hızlı), pusula iğnesinin N ucu bileşke yönünde, B₁ ile açısı tanθ = B₂/B₁.",
       "Dik vektörlerin bileşkesi Pisagor; pusula N ucu o noktadaki net alanın yönünü gösterir.",
       ["Alanlar birbirine dik", "Pusula yalnız yatay düzlemdeki alana duyarlı (Dünya'nın düşey bileşeni dikkate alınmaz)", "Dünya alanı varsa vektör olarak eklenir"],
       ["Alanlar dik değilse (örn. 60°) Pisagor yanlış sonuç verir; paralelkenar kuralı gerekir", "Dünya'nın manyetik alanını unutmak yönü kaydırır", "Alan çizgilerine teğetin yönü ile pusula N ucunu karıştırmak"],
       "LOW", [TB("s. 194 15. Alıştırma"), TB("s. 196 Örnek"), TB("s. 197 17. Alıştırma"), DV("Dik vektörlerin bileşkesi")],
       """
import math, random
random.seed(7)
for a, b in [(3, 4), (5, 12), (8, 15), (7, 24)]:
    r = math.hypot(a, b); assert abs(r - round(r)) < 1e-12
for _ in range(200):
    B1, B2 = random.uniform(1, 10), random.uniform(1, 10)
    res = (B1, B2)                                              # B1 doğuya, B2 kuzeye (dik)
    assert abs(math.hypot(*res) - math.sqrt(B1 ** 2 + B2 ** 2)) < 1e-12
    assert abs(math.atan2(B2, B1) - math.atan(B2 / B1)) < 1e-12
# başarısız: iki alan 60° ise Pisagor yanlış
B1, B2, ang = 3.0, 4.0, math.radians(60)
vec = (B1 + B2 * math.cos(ang), B2 * math.sin(ang))
assert abs(math.hypot(*vec) - 5.0) > 1.0
""")
    ,
    SC("wire-field-side-table", "Düz tel: yön tablosu (akım ↑ → sağda ⊗, solda ⊙; akım → → üstte ⊙, altta ⊗)",
       ["wire-field-direction-rhr", "wire-field-superposition"],
       "Sayfa düzleminde akım yukarıya ise telin sağındaki noktada alan sayfaya girer (⊗), solundakinde çıkar (⊙); akım sağa ise üstteki noktada alan sayfadan çıkar (⊙), alttakinde girer (⊗). Akım ters olunca hepsi ters.",
       "Biot–Savart: B yönü dl × r̂ (r̂ telden noktaya); x sağa, y yukarı, z sayfadan dışarı.",
       ["Sayfa: x sağa, y yukarı, z sayfadan okura doğru", "Akım yönü (geleneksel) verilmiş"],
       ["Elektron akışı verilmişse geleneksel akım TERS yöndedir: tablo da ters uygulanır", "Aynı yönlü iki akımın arasında alanlar zıttır (toplam azalır); yalnız tek telin tablosu üst üste binmez", "Telin kendisi üzerindeki ya da çok yakın nokta için model geçersiz", "Sağ elini yanlış (sol) kullanmak"],
       "HIGH", [TB("s. 203 Şekil 2.22"), TB("s. 205 19. Alıştırma a"), DV("dl × r̂ vektör çarpımı")],
       VEC + """
# yön tablosu: akım yönü → (noktanın yeri → alan işareti z bileşeni)
P = {"sağ": (1.0, 0, 0), "sol": (-1.0, 0, 0), "üst": (0, 1.0, 0), "alt": (0, -1.0, 0)}
def Bz(p0, p1, point):
    return biot(line(p0, p1, 1000), point)[2]
up = ((0, -50, 0), (0, 50, 0)); right = ((-50, 0, 0), (50, 0, 0))
assert Bz(*up, P["sağ"]) < 0 and Bz(*up, P["sol"]) > 0           # akım ↑: sağda ⊗ (−z), solda ⊙ (+z)
assert Bz(*right, P["üst"]) > 0 and Bz(*right, P["alt"]) < 0      # akım →: üstte ⊙, altta ⊗
assert Bz(up[1], up[0], P["sağ"]) > 0                             # akım ters → alan ters
# başarısız: aynı yönlü iki akım arasında alanlar zıt, orta noktada toplam sıfır
left_wire = ((-1, -50, 0), (-1, 50, 0)); right_wire = ((1, -50, 0), (1, 50, 0))
mid = (0.0, 0.0, 0.0)
b_total = Bz(*left_wire, mid) + Bz(*right_wire, mid)
assert abs(b_total) < 1e-6 and abs(Bz(*left_wire, mid)) > 1e-4
""")
    ,
    SC("rhr-solenoid-fingers-current", "Makara: dört parmak akım yönünde, baş parmak N ucu",
       ["solenoid-direction-poles-compass", "emag-verify-and-apply"],
       "Sağ el dört parmağı sarım akımı yönünde kıvrılırsa baş parmak makaranın içindeki alan yönünü, yani N kutbunu gösterir; akım ters çevrilince kutuplar yer değiştirir.",
       "Her sarım bir halka akımıdır; halka akımının eksen alanı sağ el kuralıyla belirlenir ve sarımların alanları eksende aynı yöne toplanır.",
       ["Bakılan taraftan sarımın akış yönü doğru okunmuş", "Makara içinde alan (N ucu) kuralı; dışta alan N'den S'ye döner"],
       ["Bakış yönü değişince 'saat yönü' ters okunur: akımı sarımın üzerinde izle", "Pusula makara dışında ve yanında ise iğne alanın dışarıdaki (N'den S'ye) yönünü gösterir; baş parmak kuralı o noktada ters yön verir", "Demir çekirdek alanı büyütür ama yönü değiştirmez"],
       "MEDIUM", [TB("s. 209 Değerlendirme 1"), TB("s. 296 ÖD-26"), DV("Halka akımının eksen alanı (Biot–Savart)")],
       VEC + """
def stack(ccw, n_rings=40, L=1.0, R=0.05):
    pts = []
    for k in range(n_rings):
        z = L * (k + 0.5) / n_rings
        pts.append(circle(R, n=120, z=z, ccw=ccw))
    return pts
def Bz_at(rings, P):
    s = 0.0
    for r in rings:
        s += biot(r, P)[2]
    return s
ccw, cw = stack(True), stack(False)
assert Bz_at(ccw, (0, 0, 0.5)) > 0 and Bz_at(cw, (0, 0, 0.5)) < 0   # ccw: alan +z yönünde (N ucu +z tarafı); akım ters → ters
# başarısız: makaranın DIŞINDA (yan tarafında) alan yönü içtekinin tersidir
assert Bz_at(ccw, (0.4, 0, 0.5)) < 0
""")
    ,
    SC("rhr-wire-force-cross-product-table", "Akımlı tel: F = i·L × B yön tablosu (⊙ ve ⊗ ile)",
       ["wire-force-direction-rhr", "loop-force-directions", "parallel-wires-force"],
       "Akım sağa ise: alan dışarı (⊙) → kuvvet aşağı; alan içeri (⊗) → kuvvet yukarı; alan yukarı → kuvvet sayfadan dışarı (⊙). Akım ya da alandan yalnız biri ters olursa kuvvet ters, ikisi birden ters olursa aynı kalır; akım alana paralelse kuvvet sıfır.",
       "F = i·L × B (vektör çarpımı); x̂ × ẑ = −ŷ, x̂ × (−ẑ) = ŷ, x̂ × ŷ = ẑ.",
       ["Sayfa: x sağa, y yukarı, z sayfadan dışarı", "Geleneksel akım yönü", "Alan düzgün"],
       ["Elektron akımı için ters yön: elektron hareket yönü verilmişse akım yönü karşıtıdır", "Alan akımla paralel ya da antiparalelse kuvvet sıfırdır (sin 0° = 0)", "Alan düzgün değilse kenarlara göre farklı olabilir", "Sol el kullanmak ya da avuç ve baş parmak rollerini karıştırmak"],
       "HIGH", [TB("s. 225 Şekil 2.26"), TB("s. 226 26. Alıştırma"), TB("s. 289 ÖD-19"), DV("Vektör çarpımı F = i·(L × B)")],
       VEC + """
X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
neg = lambda v: tuple(-a for a in v)
table = {("sağa", "dışarı"): neg(Y), ("sağa", "içeri"): Y, ("sağa", "yukarı"): Z, ("yukarı", "dışarı"): X, ("yukarı", "içeri"): neg(X)}
cur = {"sağa": X, "yukarı": Y}; fld = {"dışarı": Z, "içeri": neg(Z), "yukarı": Y}
for (c, f), direction in table.items():
    assert close(cross(cur[c], fld[f]), direction), (c, f)
# tek tersleme → ters; ikisi birden → aynı
F0 = cross(X, Z)
assert close(cross(neg(X), Z), neg(F0)) and close(cross(X, neg(Z)), neg(F0)) and close(cross(neg(X), neg(Z)), F0)
# başarısız: akım alana paralel → kuvvet sıfır
assert close(cross(X, X), (0, 0, 0)) and close(cross(X, neg(X)), (0, 0, 0))
# elektron akışı (negatif taşıyıcı, +x yönünde hareket) → geleneksel akım −x → kuvvet tersine
assert close(cross(neg(X), Z), neg(cross(X, Z)))
""")
    ,
    SC("sin-theta-special-angles", "F = B·i·L·sinθ özel açılar: 90° → 1, 30°/150° → ½, 0°/180° → 0",
       ["wire-force-magnitude-angle", "wire-force-data-model"],
       "θ telle alan arasındaki açıdır: sin 90° = 1 (en büyük), sin 30° = sin 150° = ½, sin 45° ≈ 0,7, sin 0° = sin 180° = 0 (kuvvet sıfır).",
       "|i·L × B| = i·L·B·sinθ; sinüs özel açılar tablosundan hazır.",
       ["θ telin uzunluk yönüyle alan çizgileri arasındaki açı", "Düzgün alan"],
       ["Açı alan yönüyle değil de teli içeren yüzeyle (ya da alana dik doğrultuyla) verilmişse sinüs yerine kosinüs gerekir", "Akı formülünde (Φ = BA cosθ) θ yüzey NORMALİ ile alan arasındadır; ikisini karıştırmak sık hatadır", "0° ya da 180° için kuvvet sıfırdır, hareket başlamaz"],
       "MEDIUM", [TB("s. 225 Model"), TB("s. 227 27. Alıştırma"), DV("Vektör çarpımı büyüklüğü: |a × b| = ab·sinθ")],
       VEC + """
import math
table = {90: 1.0, 30: 0.5, 150: 0.5, 45: math.sqrt(2) / 2, 0: 0.0, 180: 0.0, 60: math.sqrt(3) / 2}
B, i, L = 0.4, 5.0, 0.3
for deg, s in table.items():
    th = math.radians(deg)
    w = (L * math.cos(th), L * math.sin(th), 0.0)              # tel yönü: alana (x ekseni) θ açısında
    Fv = mul(i, cross(w, (B, 0.0, 0.0)))
    assert abs(norm(Fv) - B * i * L * s) < 1e-12
# başarısız: açı alanla değil alana DİK doğrultuyla verilirse sin yerine cos kullanılır
th_perp = math.radians(30)                                      # tel, alana dik doğrultuyla 30°
th_true = math.radians(90) - th_perp
assert abs(math.sin(th_perp) - math.sin(th_true)) > 0.3
""")
    ,
    SC("wire-field-i-over-d", "Düz tel: B ∝ i/d (karesiz); B ortamla K çarpanıyla değişir",
       ["wire-field-ratio", "wire-field-superposition", "wire-field-data-model"],
       "B oranı = (i çarpanı)(K çarpanı)/(d çarpanı); d'nin KARESİ yoktur. 'i ve d aynı çarpanla değişirse B değişmez.'",
       "Biot–Savart integralinden sonsuz uzun düz tel için B = 2K·i/d (tel çevresinde çemberlerin çevresi d ile orantılı).",
       ["Sonsuz uzun (d ≪ tel boyu) ince düz tel", "Aynı ortam ya da K çarpanı verilmiş"],
       ["Telin uç bölgesinde ya da kısa teller için 1/d geçersizdir", "Halka telin merkezi ya da makara için başka bağıntılar vardır", "Program hesaplamayı dışlar; oran yorumu", "Ters kare ile (E alanı gibi) karıştırmak"],
       "LOW", [TB("s. 202 Düz telin alanı"), TB("s. 200 9.–10. adım"), DV("Biot–Savart integrali, sonsuz tel")],
       """
import math
def B_finite(d, h, n=40000):
    s = 0.0; dz = 2 * h / n
    for k in range(n):
        z = -h + (k + 0.5) * dz
        s += d / math.hypot(d, z) ** 3 * dz
    return s
long = (B_finite(1.0, 500.0), B_finite(2.0, 500.0), B_finite(3.0, 500.0))
assert abs(long[0] / long[1] - 2) < 2e-3 and abs(long[0] / long[2] - 3) < 3e-3       # B ∝ 1/d
# i ×3 ve d ×3 → B aynı
assert abs((3.0 / 3.0) - 1) < 1e-12
# süperpozisyon: iki telde toplam alan, tek tek alanların toplamı
assert abs(B_finite(1.0, 500.0) + B_finite(3.0, 500.0) - (long[0] + long[2])) < 1e-12
# başarısız: kısa tel (yarı uzunluk = d) → 1/d geçersiz
short = (B_finite(1.0, 1.0), B_finite(2.0, 1.0))
assert abs(short[0] / short[1] - 2) > 0.3
""")
    ,
    SC("solenoid-n-over-L-factor", "Makara: B ∝ i·(N/L) — N ve L'yi birlikte düşün; demir çekirdek K'yi büyütür",
       ["solenoid-ratio-generalization", "emag-verify-and-apply", "solenoid-data-model"],
       "B oranı = (i çarpanı)(N çarpanı)(K çarpanı)/(L çarpanı); N ve L aynı çarpanla değişirse (sarım yoğunluğu aynı) B değişmez; yarıçap ve tel rengi etkisizdir.",
       "İdeal uzun makarada içte B = 4π·K·i·N/L; sarımların alanları eksende toplanır.",
       ["Makara boyu çapından çok büyük (L ≫ R)", "Alanı makara içinde, ortada ölçülüyor", "İdeal makara: içte düzgün, dışta ~0"],
       ["Kısa ve geniş makarada (L ≲ R) B ≈ K'ya bağlı farklı bir ifadeyle N/L'ye değil N/R'ye bağlıdır; kısa yol geçersiz", "Demir çekirdek K'yi çarpar ama doyuma ulaşır", "Makaranın uçlarında alan ortadakinin yaklaşık yarısıdır", "Program hesaplamayı dışlar; oran düzeyinde"],
       "MEDIUM", [TB("s. 209 11. adım"), TB("s. 211 Örnek"), TB("s. 281 ÖD-10"), DV("Halka akımı eksen alanlarının toplamı")],
       """
import math
def Bc(N, L, i, R, steps=4000):
    # sürekli sarım yoğunluğu n = N/L: orta noktadaki alan = n·i·∫ R²/(R²+z²)^{3/2} dz  (μ0/2 atıldı), sayısal integral
    n = N / L; dz = L / steps; s = 0.0
    for k in range(steps):
        z = -L / 2 + (k + 0.5) * dz
        s += R ** 2 / (R ** 2 + z ** 2) ** 1.5 * dz
    return n * i * s
R = 0.01
base = Bc(100, 1.0, 1.0, R)
assert abs(Bc(200, 1.0, 1.0, R) / base - 2) < 0.01                  # N ×2
assert abs(Bc(200, 2.0, 1.0, R) / base - 1) < 0.01                  # N ×2, L ×2 → B aynı
assert abs(Bc(100, 1.0, 3.0, R) / base - 3) < 1e-9                  # i ×3
assert abs(Bc(100, 2.0, 1.0, R) / base - 0.5) < 0.01                # L ×2
assert abs(Bc(100, 1.0, 1.0, 5 * R) / base - 1) < 0.05              # yarıçap etkisiz (uzun makarada)
# başarısız: kısa, geniş makara (L ≪ R): N ×2 ve L ×2 sonuç değişmez DEĞİL, B ≈ 2×
Rf = 0.05
bs = Bc(100, 0.02, 1.0, Rf)
assert abs(Bc(200, 0.04, 1.0, Rf) / bs - 1) > 0.5
""")
    ,
    SC("parallel-currents-attract", "Paralel tellerde: aynı yön çeker, zıt yön iter; kuvvetler eşit (∝ i₁i₂/d)",
       ["parallel-wires-force"],
       "Aynı yönlü akımlar birbirini çeker, zıt yönlü akımlar iter; iki telin birbirine uyguladığı kuvvetler büyüklükçe eşittir (akımlar farklı olsa da); büyüklük i₁·i₂/d ile orantılıdır.",
       "Tel 1'in tel 2'deki alanı B₁ ∝ i₁/d; F₂ = i₂·L·B₁ ∝ i₁i₂L/d. Yön F = i L × B ile bulunur; ikili etki Newton 3 çiftidir.",
       ["Uzun paralel düz teller", "d ≪ tel boyu"],
       ["Akımları farklı iki telde kuvvetin 'büyük akımlı tele daha büyük' olduğunu sanmak yanlıştır; kuvvetler eşit", "Teller paralel değilse (dik ya da eğik) büyüklük ve yön ayrıca hesaplanır", "Üç tel varsa her teldeki net kuvvet vektörel toplanır"],
       "MEDIUM", [TB("s. 228 28. Alıştırma"), DV("Biot–Savart + F = i·L×B + Newton 3")],
       VEC + """
def field_of_line(i, p0, p1, point):
    return mul(i, biot(line(p0, p1, 4000), point))               # B ∝ i, K atıldı
d = 0.5
up = (0, 0, 1)
W1 = ((0, 0, -200), (0, 0, 200)); W2 = ((d, 0, -200), (d, 0, 200))
for i1, i2, expected in [(3.0, 5.0, "çeker"), (3.0, -5.0, "iter")]:
    B1_at_2 = field_of_line(i1, *W1, (d, 0, 0)); B2_at_1 = field_of_line(i2, *W2, (0, 0, 0))
    F2 = mul(abs(i2), cross(mul(1 if i2 > 0 else -1, up), B1_at_2))
    F1 = mul(abs(i1), cross(mul(1 if i1 > 0 else -1, up), B2_at_1))
    toward = (F2[0] < 0)                                          # tel 2 tel 1'e (−x) doğru çekiliyor mu
    assert toward == (expected == "çeker")
    assert abs(norm(F1) - norm(F2)) / norm(F1) < 1e-6              # eşit büyüklük (akımlar farklı olsa da)
    assert abs(F1[0] + F2[0]) < 1e-9 * max(1, norm(F1))            # zıt yön
# büyüklük ∝ 1/d
b_near = norm(field_of_line(1.0, *W1, (0.25, 0, 0))); b_far = norm(field_of_line(1.0, *W1, (0.5, 0, 0)))
assert abs(b_near / b_far - 2) < 1e-2
""")
    ,
    SC("loop-torque-parallel-max", "Çerçeve: düzlem alana paralelken döndürme etkisi en büyük, dikken sıfır; ∝ N·i·B·A",
       ["loop-rotation-torque", "loop-force-directions"],
       "Döndürme çifti τ = N·i·B·A·sinφ (φ: yüzey normali ile B arasındaki açı): düzlem alana paralel (φ = 90°) → en büyük; düzlem alana dik (φ = 0°) → sıfır; N, i, B, A arttıkça doğru orantılı artar.",
       "Alana dik kenarlara etki eden kuvvetler eşit ve zıt yönlü olduğundan net kuvvet sıfır, ama farklı doğrultulardan geçtikleri için çift oluşturur.",
       ["Düzgün alan", "Dikdörtgen/düzlemsel çerçeve, eksen alana dik", "Sabit akım yönü"],
       ["Düzlem alana dik olunca döndürme etkisi sıfırdır: komütatörsüz motor bu ölü noktada takılır", "Akım yönü sabit kalırsa çerçeve yarım dönüşten sonra geri sürüklenir (komütatör/AC gerekir)", "Alan düzgün değilse net kuvvet sıfır olmaz", "Net kuvvet sıfırdır ama dönüş vardır: 'net kuvvet yok → dönme yok' sanılmaz"],
       "MEDIUM", [TB("s. 233 30. Alıştırma"), TB("s. 234 31. Alıştırma"), TB("s. 293 ÖD-23"), DV("τ = Σ r × (i dl × B)")],
       VEC + """
import math
def loop_torque(phi, a=0.2, b=0.3, i=2.0, Bv=0.5, n=40):
    # eksen y, B = (Bv,0,0), normal n̂ = (cosφ, 0, sinφ); düzlem: y ve w = (−sinφ, 0, cosφ)
    w = (-math.sin(phi), 0.0, math.cos(phi)); u = (0.0, 1.0, 0.0)
    corners = [add(mul(-a / 2, u), mul(-b / 2, w)), add(mul(a / 2, u), mul(-b / 2, w)), add(mul(a / 2, u), mul(b / 2, w)), add(mul(-a / 2, u), mul(b / 2, w))]
    tau = (0.0, 0.0, 0.0); Ftot = (0.0, 0.0, 0.0)
    for k in range(4):
        p, q = corners[k], corners[(k + 1) % 4]
        for s in range(n):
            p1 = add(p, mul(s / n, sub(q, p))); p2 = add(p, mul((s + 1) / n, sub(q, p)))
            dl = sub(p2, p1); mid = mul(0.5, add(p1, p2))
            dF = mul(i, cross(dl, (Bv, 0.0, 0.0)))
            tau = add(tau, cross(mid, dF)); Ftot = add(Ftot, dF)
    return norm(tau), norm(Ftot)
A, i, Bv = 0.2 * 0.3, 2.0, 0.5
for deg in (0, 30, 60, 90):
    t, F = loop_torque(math.radians(deg))
    assert abs(t - i * Bv * A * math.sin(math.radians(deg))) < 1e-9 and F < 1e-9   # net kuvvet sıfır, çift var
assert loop_torque(math.radians(0))[0] < 1e-9                                       # düzlem alana dik → sıfır
assert loop_torque(math.radians(90))[0] > loop_torque(math.radians(60))[0] > loop_torque(math.radians(30))[0]
# başarısız: akım (alan) iki katına çıkınca döndürme çifti iki katına çıkar ama net kuvvet yine sıfır — 'net kuvvet 0 → dönme yok' yanlış
t2, F2n = loop_torque(math.radians(90), i=4.0)
assert abs(t2 / loop_torque(math.radians(90))[0] - 2) < 1e-9 and F2n < 1e-9 and t2 > 0
""")
    ,
]

# ---------------- Manyetik akı ve elektromanyetik indüksiyon ----------------
SHORTCUTS += [
    SC("flux-cos-normal-angle", "Akı: yüzey normali alana paralel → en büyük, dik (düzlem ∥ alan) → 0; Φ = B·A·cosθ",
       ["flux-factors-analogy", "flux-relationship-qualitative", "flux-change-in-motion"],
       "Φ ∝ B·A·cosθ; θ yüzeyin NORMALİ ile alan arasındaki açıdır. Düzlem alana dik duruyorsa (normal alana paralel) en büyük, düzlem alana paralelse (normal alana dik) sıfır; alan çizgilerine paralel eksen etrafında dönmek akıyı değiştirmez.",
       "Φ, yüzeyden geçen alan çizgisi sayısı kadardır; yalnız yüzeye dik alan bileşeni sayılır: B·n̂·A.",
       ["Düzgün alan", "Düzlem yüzey", "θ normal ile alan arasında"],
       ["θ yüzeyle alan arasında verilmişse cos yerine sin kullanılır", "Alan düzgün değilse Φ = ∫B·dA'dır, B·A·cosθ kullanılamaz", "Akı büyük olsa da değişmiyorsa ε = 0'dır"],
       "MEDIUM", [TB("s. 239 Model"), TB("s. 240 Örnek cevap"), TB("s. 241 34. Alıştırma"), DV("Φ = ∫ B·n̂ dA, düzgün alanda B·A·cosθ")],
       """
import math
def flux(theta, A=0.2 * 0.3, B=0.5, n=50):
    # yüzey üzerinde ızgara integrali: Σ B·n̂ dA, n̂ alana (z) θ açısında
    nhat = (math.sin(theta), 0.0, math.cos(theta)); Bv = (0.0, 0.0, B)
    dA = A / (n * n)
    return sum(sum(a * b for a, b in zip(Bv, nhat)) * dA for _ in range(n * n))
A, B = 0.06, 0.5
for deg in (0, 30, 60, 90):
    assert abs(flux(math.radians(deg)) - B * A * math.cos(math.radians(deg))) < 1e-12
assert flux(0.0) > flux(math.radians(60)) > flux(math.radians(90)) - 1e-12 and abs(flux(math.radians(90))) < 1e-12
# alana paralel eksen (z) etrafında dönme: normalin alanla açısı aynı → akı sabit
assert all(abs(flux(math.radians(40)) - B * A * math.cos(math.radians(40))) < 1e-12 for _ in range(5))
# başarısız: açı yüzeyle verilirse sin kullanılmalı
theta_surface = math.radians(30)
assert abs(B * A * math.cos(theta_surface) - B * A * math.sin(theta_surface)) > 0.01
""")
    ,
    SC("ask-flux-changing-first", "Önce sor: akı değişiyor mu? (B, A ya da θ'dan biri zamanla değişmeli)",
       ["induction-experiment-factors", "induction-applications", "flux-change-in-motion"],
       "Hareket ya da düzenek verildiğinde ilk soru 'B, A veya θ zamanla değişiyor mu?': değişmiyorsa ε = 0 (akı büyük de olsa), değişiyorsa ε akı değişim hızıyla orantılı. Kapalı devre ise akım da vardır.",
       "ε = −N·dΦ/dt; Φ = B·A·cosθ'nın zamana göre türevi sıfır değilse ε vardır.",
       ["Bağlam: halka/bobin ve alan", "Hareket türü açıkça tanımlı"],
       ["Düzgün alanda ötelenen halkada akı değişmez: ε = 0 (alan sınırından geçerken değişir)", "Açık devrede ε vardır ama akım yoktur", "Alan çizgilerine paralel eksenli dönmede akı sabittir"],
       "LOW", [TB("s. 246 Şekil 2.31"), TB("s. 241 35. Alıştırma"), TB("s. 250 38. Alıştırma"), DV("ε = −dΦ/dt")],
       """
import math
B, a = 0.5, 0.1
def eps_of(phi, t, h=1e-6):
    return -(phi(t + h) - phi(t - h)) / (2 * h)
def overlap(x, w=0.4):                                  # halka sağdan alan bölgesine (x>0, genişlik w) giriyor
    lo, hi = max(x - a, 0.0), min(x, w)
    return max(0.0, hi - lo) * a
v = 2.0
phi_translate_uniform = lambda t: B * a * a                        # her yerde düzgün alan: ötelenme
phi_enter = lambda t: B * overlap(v * t)                           # alan bölgesine giriş
phi_spin_parallel = lambda t: B * a * a * math.cos(0.0)            # normal-alan açısı sabit (alan eksenli dönme)
phi_spin_perp = lambda t: B * a * a * math.cos(40 * t)             # alana dik eksenli dönme
phi_ramp = lambda t: (0.5 + 0.3 * t) * a * a                       # B zamanla artıyor
assert abs(eps_of(phi_translate_uniform, 0.1)) < 1e-9 and abs(eps_of(phi_spin_parallel, 0.1)) < 1e-9
assert abs(eps_of(phi_enter, 0.025)) > 1e-4                         # girerken (0 < x < a)
assert abs(eps_of(phi_enter, 0.15)) < 1e-9                          # tamamen içeride (a < x < w)
assert abs(eps_of(phi_spin_perp, 0.01)) > 1e-3 and abs(eps_of(phi_ramp, 0.5)) > 1e-4
# başarısız: akı büyük ama sabit → ε = 0; açık devrede ε var, akım yok
assert phi_translate_uniform(0) > 0 and abs(eps_of(phi_translate_uniform, 1.0)) < 1e-9
e = abs(eps_of(phi_ramp, 0.5)); R_open = float("inf")
assert e > 0 and e / R_open == 0.0
""")
    ,
    SC("emf-ratio-multipliers", "ε oranı = (N çarpanı)(ΔΦ çarpanı)/(Δt çarpanı); i oranı ε/R",
       ["induction-emf-ratio-calc", "induction-experiment-factors", "induction-applications"],
       "ε_yeni/ε = (N çarpanı)·(ΔΦ çarpanı)/(Δt çarpanı); akım için ayrıca direnç çarpanına bölünür. Çarpanlar çarpılır, sürenin çarpanı bölende yer alır.",
       "ε = N·ΔΦ/Δt çarpımsal olduğundan her çarpan bağımsız olarak çıkar.",
       ["Aynı biçimde tanımlı iki durum", "ΔΦ/Δt ortalama (ya da sabit) değer"],
       ["ΔΦ çarpanı, alan yönünün ters çevrilmesinde 2 gelir (0 değil): ΔΦ = Φ_son − Φ_ilk işaretli", "ε anlık değilse ortalama değerdir", "Akım için R değişiyorsa ayrıca bölünmeli; açık devrede i = 0, ε ≠ 0"],
       "MEDIUM", [TB("s. 248 Örnek"), TB("s. 246 2. soru tablosu"), TB("s. 249 37. Alıştırma"), DV("ε = N·ΔΦ/Δt")],
       """
import random
random.seed(9)
for _ in range(300):
    N, A, B1, B2, dt, R = random.randint(10, 500), random.uniform(0.001, 0.05), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0.01, 2), random.uniform(1, 50)
    eps = lambda N_, A_, b1, b2, t_: N_ * (b2 - b1) * A_ / t_
    kN, kd, kt, kR = random.choice([0.5, 2, 3]), random.choice([0.5, 2, 4]), random.choice([0.5, 2, 5]), random.choice([0.5, 2])
    e0 = eps(N, A, B1, B2, dt)
    e1 = eps(kN * N, A, B1, B1 + kd * (B2 - B1), kt * dt)          # ΔB (dolayısıyla ΔΦ) çarpanı kd
    assert abs(e1 / e0 - kN * kd / kt) < 1e-9
    assert abs((e1 / (kR * R)) / (e0 / R) - kN * kd / kt / kR) < 1e-9
# başarısız: alan yönü ters çevrilince ΔΦ = 2BA (0 değil)
B, A = 0.1, 0.02
dphi = (-B * A) - (B * A)
assert abs(dphi - (-2 * B * A)) < 1e-12 and abs(dphi) > 0
# başarısız: sabit akı → ΔΦ çarpanı sıfır, kısa yol 'ε büyük akıda büyük' demez
assert eps(100, 0.02, 5.0, 5.0, 1.0) == 0.0
""")
    ,
    SC("flux-time-slope-to-emf", "Φ–t grafiğinin eğimi → ε = −N·eğim (yatay → 0, dik → büyük)",
       ["induction-flux-time-graphs"],
       "Her doğrusal aralıkta ε = −N × (ΔΦ/Δt): yatay aralık ε = 0; dik artan → büyük negatif; dik azalan → büyük pozitif. B–t grafiğinde önce Φ = B·A.",
       "Faraday yasası ε = −N·dΦ/dt: ε, akı grafiğinin eğimidir; akının kendisi değil.",
       ["Parçalı doğrusal grafik", "Eksen birimleri SI'ya çevrilmiş (ms → s, mWb → Wb)", "N verilmiş"],
       ["Eğrisel Φ–t'de ortalama eğim ≠ anlık eğim; ε zamanla değişir", "ms ve mWb'yi çevirmeden eğim almak sonucu yanlış kılar (örn. 10³ kat)", "Φ = 0 olan anda eğim büyükse |ε| büyüktür: akı sıfır → ε sıfır sanma"],
       "MEDIUM", [TB("s. 251 40. Alıştırma"), TB("s. 252 41. Alıştırma"), DV("ε = −N·dΦ/dt")],
       """
import random
random.seed(21)
for _ in range(200):
    N = random.randint(5, 300)
    pts = [(0.0, random.uniform(-5e-3, 5e-3))]
    t = 0.0
    for _ in range(4):
        t += random.uniform(0.5, 3.0); pts.append((t, random.uniform(-5e-3, 5e-3)))
    phi = lambda x: next(p0[1] + (p1[1] - p0[1]) * (x - p0[0]) / (p1[0] - p0[0]) for p0, p1 in zip(pts, pts[1:]) if p0[0] <= x <= p1[0])
    for p0, p1 in zip(pts, pts[1:]):
        mid = (p0[0] + p1[0]) / 2
        slope = (p1[1] - p0[1]) / (p1[0] - p0[0])
        e_full = -N * (phi(mid + 1e-7) - phi(mid - 1e-7)) / 2e-7
        assert abs(e_full - (-N * slope)) < 1e-6
flat = [(0, 3e-3), (4, 3e-3)]
assert -10 * (flat[1][1] - flat[0][1]) / (flat[1][0] - flat[0][0]) == 0.0       # yatay → 0, akı büyük olsa da
# başarısız 1: eğrisel Φ = k t² → ortalama eğim ≠ anlık eğim
k = 1e-3
avg = (k * 4 ** 2 - k * 0) / 4; inst = 2 * k * 1.0
assert abs(avg - inst) > 1e-3
# başarısız 2: ms yerine s okumak 10³ hata yapar
assert abs((8e-3 / 2e-3) / (8e-3 / 2) - 1000) < 1e-9
""")
    ,
    SC("lenz-four-step", "Lenz dört adım: dış alan → artış/azalış → indüksiyon alanı (artışta zıt, azalışta aynı) → sağ el",
       ["lenz-induced-current-direction", "induction-experiment-factors"],
       "(1) Dış alan yönü, (2) artıyor mu azalıyor mu, (3) indüksiyon alanı artışta dış alana ZIT, azalışta AYNI yönlü, (4) sağ el kuralıyla akım yönü. Mıknatıs yaklaşırken ve uzaklaşırken akım yönleri zıttır.",
       "ε = −dΦ/dt işaretindeki eksi, indüksiyon akımının akıdaki DEĞİŞİME karşı koyacak yönde olması demektir (enerji korunumu).",
       ["Kapalı iletken devre", "Akı değişimi var", "Karşı koyulan şey 'dış alanın kendisi' değil 'akı DEĞİŞİMİ'dir"],
       ["'Daima dış alana zıt' kuralı yanlıştır: akı azalırken indüksiyon alanı dış alanla aynı yönlüdür", "Dış alan yön değiştirirken (yön tersine dönüş) indüksiyon alanı yön değiştirmez, çünkü akının DEĞİŞİMİ aynı işaretlidir", "Devre açıksa akım yok (ε var); bakış yönünü (üstten/alttan) karıştırmak sık hatadır"],
       "MEDIUM", [TB("s. 247 Lenz Yasası"), TB("s. 249 37. Alıştırma c"), TB("s. 286 ÖD-16"), DV("ε = −N·dΦ/dt ve sağ el kuralı (Biot–Savart)")],
       VEC + """
import math
A, R_c = 0.01, 1.0
ring_ccw, ring_cw = circle(0.1), circle(0.1, ccw=False)
Bc_ccw = biot(ring_ccw, (0, 0, 0))[2]; Bc_cw = biot(ring_cw, (0, 0, 0))[2]
assert Bc_ccw > 0 > Bc_cw                                            # ccw akım → merkezde +z alan
def induced_axial_sign(Bz, t, h=1e-6):
    eps = -(Bz(t + h) - Bz(t - h)) / (2 * h) * A                      # ε>0: +z normale göre ccw
    i = eps / R_c
    return (1 if i > 0 else -1) if abs(i) > 1e-12 else 0              # indüksiyon alanı z işareti = ccw işareti
# artış: dış alan aşağı büyüyor → indüksiyon alanı yukarı (zıt)
assert induced_axial_sign(lambda s: -(1 + 0.5 * s), 1.0) == +1
# azalış: dış alan aşağı küçülüyor → indüksiyon alanı aşağı (aynı yönlü)
assert induced_axial_sign(lambda s: -(2 - 0.5 * s), 1.0) == -1
# başarısız: 'daima dış alana zıt' kuralı — dış alan +'dan −'ya düzgün değişirken indüksiyon alanı hiç yön değiştirmez
Bz = lambda s: 1.0 - 2.0 * s                                         # t=0.5'te alan yön değiştirir
signs = {induced_axial_sign(Bz, s) for s in (0.1, 0.3, 0.7, 0.9)}
assert signs == {+1}
ext_sign = [1 if Bz(s) > 0 else -1 for s in (0.1, 0.3, 0.7, 0.9)]
assert ext_sign == [1, 1, -1, -1]                                     # dış alan işaret değiştirdi; indüksiyon alanı (+) hep aynı
# kesik halka: i = ε/∞ = 0
assert (1.0 / float("inf")) == 0.0
""")
    ,
    SC("closed-conductor-braking-tree", "Mıknatıs–halka karar ağacı: kapalı iletken → yukarı fren; kesik/yalıtkan → serbest düşme",
       ["magnet-falling-through-ring", "lenz-induced-current-direction", "induction-applications"],
       "Halka kapalı ve iletkense mıknatıs girerken de çıkarken de yukarı yönlü fren kuvveti alır, düşme süresi uzar (ivme < g); halka kesik ya da yalıtkansa akım yok, fren yok, serbest düşme.",
       "Kapalı iletkende akı değişimi akım doğurur; Lenz gereği manyetik kuvvet harekete zıt (P = i²R ≥ 0 ⇒ F·v < 0).",
       ["Mıknatıs halka ekseni boyunca düşer", "Halka kapalı iletken ya da kesik/yalıtkan olarak belli"],
       ["Halka direnci çok büyükse (akım çok küçük) fren fark edilmeyecek kadar küçüktür; 'fren var' yargısı niceliksel olarak boşa çıkar", "Mıknatıs çok yavaşsa akı değişimi küçüktür, etki zayıftır", "Kuvvet yalnız girişte ya da yalnız çıkışta değil, iki durumda da yukarıdır"],
       "LOW", [TB("s. 287 ÖD-17"), DV("Lenz yasası + güç dengesi P = i²R")],
       """
import math
Phi0, a, g, m = 0.01, 0.05, 10.0, 0.1
dPhi = lambda z: -3 * Phi0 * z / a ** 2 / (1 + (z / a) ** 2) ** 2.5
def fall(R):
    z, v, t, dt, n = 0.4, 0.0, 0.0, 1e-4, 0
    while z > -0.4 and n < 100000:
        n += 1
        i = (-dPhi(z) * v) / R if R != float("inf") else 0.0
        F = i * dPhi(z)
        v += (-g + F / m) * dt; z += v * dt; t += dt
    assert z <= -0.4
    return t
t_free = fall(float("inf")); t_closed = fall(0.01); t_plastic = fall(float("inf"))
assert abs(t_free - math.sqrt(0.8 * 2 / g)) < 5e-3 and t_closed > 1.05 * t_free and t_plastic == t_free
# başarısız: çok büyük dirençli 'kapalı' halka → etki ihmal edilebilir
assert abs(fall(1e6) - t_free) / t_free < 1e-3
""")
    ,
]

# ---------------- Alternatif akım ----------------
SHORTCUTS += [
    SC("ac-factor-classification", "AC etmen eşleştirmesi: N, B, A → yalnız büyüklük; dönme sıklığı → büyüklük VE frekans",
       ["ac-factors-identification", "ac-led-data-interpretation"],
       "ε_maks çarpanı = (N)(B)(A)(f çarpanları); frekans çarpanı = yalnız f çarpanı. N, B, A değişince frekans değişmez; dönme hızı ×k ise ε_maks ×k ve frekans ×k.",
       "ε = −N·dΦ/dt, Φ = N B A cos(2π f t) ⇒ ε_maks = N·B·A·2π f; zero-crossing frekansı f'dir.",
       ["Düzgün alanda sabit hızla dönen çerçeve", "Çerçeve ekseni alana dik"],
       ["Dönme sabit değilse sinüs biçimi bozulur", "B ve A ters yönde değişirse büyüklükler birbirini götürebilir (B ×2, A ×½ → büyüklük aynı)", "Tablo verisinde çok değişkenli satırlarda tek etmene yorum yapılmaz"],
       "LOW", [TB("s. 255 6. adım a–ç"), TB("s. 262 Kontrol Noktası"), DV("ε_maks = N·B·A·2π·f")],
       """
import math
def peak_freq(N, B, A, f, T=0.5, dt=1e-4):
    phi = lambda t: N * B * A * math.cos(2 * math.pi * f * t)
    e = [-(phi(k * dt + dt) - phi(k * dt - dt)) / (2 * dt) for k in range(int(T / dt))]
    ups = [(k - 1 + e[k - 1] / (e[k - 1] - e[k])) * dt for k in range(1, len(e)) if e[k - 1] < 0 <= e[k]]
    return max(e), (len(ups) - 1) / (ups[-1] - ups[0])
base = (40, 0.3, 0.02, 20.0)
E0, F0 = peak_freq(*base)
cases = [((2, 1, 1, 1), (2, 1)), ((1, 2, 1, 1), (2, 1)), ((1, 1, 3, 1), (3, 1)), ((1, 1, 1, 2), (2, 2)), ((1, 0.5, 1, 1), (0.5, 1)), ((1, 2, 1, 0.5), (1, 0.5))]
for mult, (ke, kf) in cases:
    e, fr = peak_freq(*(b * m for b, m in zip(base, mult)))
    assert abs(e / E0 - ke) < 5e-3 and abs(fr / F0 - kf) < 1e-2, mult
# başarısız: B ×2 ve A ×½ → büyüklük aynı; frekans da aynı
e, fr = peak_freq(base[0], 2 * base[1], 0.5 * base[2], base[3])
assert abs(e / E0 - 1) < 1e-3
""")
    ,
    SC("phi-t-slope-quarter-shift", "Φ tepede ε = 0; Φ sıfırdayken |ε| en büyük (ε–t, Φ–t'ye göre T/4 kaymış)",
       ["ac-loop-graphs"],
       "Dönen çerçevede Φ–t kosinüs benzeri ise ε–t sinüs benzeridir: akı tepe/çukurdayken ε = 0, akı sıfırdan geçerken |ε| en büyük; tam turda akım iki kez yön değiştirir.",
       "ε = −N·dΦ/dt: tepe/çukur eğimin sıfır olduğu noktadır, sıfır geçişi eğimin en dik olduğu noktadır.",
       ["Sinüs biçimli dalga (sabit hızla dönen çerçeve)"],
       ["Sinüs olmayan Φ–t (ör. doğrusal artış) için 'tepede ε = 0' kuralı çalışmaz: eğim yine sıfır olmayabilir", "Φ–t ile ε–t'yi aynı grafik sanmak", "Kesin T/4 kayması yalnız sinüsün türevi için geçerlidir"],
       "MEDIUM", [TB("s. 254 2. adım"), TB("s. 256 Çalışma Yaprağı 1"), DV("d/dt cos(ωt) = −ω sin(ωt)")],
       """
import math
T = 1.0; w = 2 * math.pi / T; h = 1e-6
phi = lambda t: math.cos(w * t)
eps = lambda t: -(phi(t + h) - phi(t - h)) / (2 * h)
for t in (0.0, 0.5, 1.0):
    assert abs(phi(t)) > 0.999 and abs(eps(t)) < 1e-4                 # Φ tepe/çukur → ε = 0
for t in (0.25, 0.75):
    assert abs(phi(t)) < 1e-9 and abs(abs(eps(t)) - w) < 1e-3          # Φ = 0 → |ε| en büyük
ts = [k / 1000 for k in range(1, 1000)]
assert abs(max(ts, key=eps) - 0.25) < 2e-3                            # ε maksimumu Φ maksimumundan T/4 sonra
# başarısız: doğrusal artan akı (ramp) → Φ en büyükken ε sıfır DEĞİL
ramp = lambda t: 2.0 * t
e_ramp = -(ramp(0.99 + h) - ramp(0.99 - h)) / (2 * h)
assert abs(e_ramp) > 1.9
""")
    ,
    SC("oscilloscope-reading", "Osiloskop: tepe = kare × V/kare; periyot = kare × s/kare; f = 1/T",
       ["ac-loop-graphs", "ac-frequency-period-counting"],
       "Tepe yüksekliğini kare sayısı × (V/kare), bir tam dalganın yatay uzunluğunu kare × (s/kare) ile ölç; f = 1/T. İki dalganın oranı için ölçekler aynıysa kare sayısı oranı doğrudan kullanılır.",
       "Ekran, gerilimi düşey eksende ve zamanı yatay eksende ölçekli gösterir; periyot iki ardışık aynı fazlı nokta arasıdır.",
       ["Sinüs benzeri dalga", "Her iki kanalın ölçeği bilinir"],
       ["Kanalların ölçekleri farklıysa (1 V/kare ve 2 V/kare) kare sayısı oranı gerilim oranı değildir", "Periyot yerine tepeden çukura (yarım dalga) okumak frekansı 2 kat verir", "Merkezlenmemiş dalgada tepe, sıfır çizgisinden ölçülmelidir"],
       "MEDIUM", [TB("s. 261 43. Alıştırma"), TB("s. 260 42. Alıştırma"), DV("f = 1/T")],
       """
import math
def measure(peak_div, wave_div, v_div, t_div, dt=1e-6):
    V0, T = peak_div * v_div, wave_div * t_div
    n = int(8 * T / dt)
    y = [V0 * math.sin(2 * math.pi * k * dt / T) for k in range(n)]
    ups = [k for k in range(1, n) if y[k - 1] < 0 <= y[k]]
    return max(y), (len(ups) - 1) / ((ups[-1] - ups[0]) * dt)
Vb, fb = measure(4, 4, 1.0, 2e-3); Vy, fy = measure(2, 8, 1.0, 2e-3)
assert abs(Vb - 4.0) < 1e-3 and abs(fb - 125.0) < 0.5 and abs(Vy - 2.0) < 1e-3 and abs(fy - 62.5) < 0.5
assert abs(Vb / Vy - 2) < 1e-3 and abs(fb / fy - 2) < 1e-2
# başarısız 1: ölçekler farklı → kare oranı gerilim oranı değil
V1, _ = measure(3, 4, 1.0, 2e-3); V2, _ = measure(3, 4, 2.0, 2e-3)
assert abs(V2 / V1 - 1) > 0.5
# başarısız 2: yarım dalgayı (tepe–çukur) periyot sanmak f'yi 2 kat verir
assert abs(1 / (2e-3 * 2) - 125 * 2) < 1e-9
""")
    ,
    SC("rms-equals-max-over-root2", "V_etkin = V_maks/√2, i_etkin = i_maks/√2 (yalnız sinüs); DC eşdeğeri etkin değerdir",
       ["ac-effective-max-values"],
       "Sinüs biçimli AC'de V_maks = √2·V_etkin (≈ 1,41), i_maks = √2·i_etkin; aynı dirençte aynı ısıyı veren DC'nin değeri AC'nin etkin değeridir; voltmetre ve ampermetre etkin değeri gösterir.",
       "Bir periyotta ortalama ısıl güç ½·V_maks²/R; DC'ninkiyle eşitlenince V_etkin = V_maks/√2.",
       ["Sinüs biçimli akım/gerilim", "Direnç (program kapsamında yalnız ısı eşdeğerliği)"],
       ["Kare dalgada V_etkin = V_maks, üçgen dalgada V_etkin = V_maks/√3'tür; √2 yalnız sinüs için", "'Etkin' ile 'ortalama' farklıdır (sinüsün tam periyot ortalaması sıfırdır)", "V_maks hesabında √2 yerine 2 çarpmak"],
       "MEDIUM", [TB("s. 259 Örnek"), TB("s. 294 ÖD-24 e"), DV("⟨sin²⟩ = ½")],
       """
import math
def rms(f, n=200000):
    return math.sqrt(sum(f((k + 0.5) / n) ** 2 for k in range(n)) / n)
def avg(f, n=200000):
    return sum(f((k + 0.5) / n) for k in range(n)) / n
V = 10.0
sine = lambda x: V * math.sin(2 * math.pi * x)
assert abs(rms(sine) - V / math.sqrt(2)) < 1e-6 and abs(avg(sine)) < 1e-9
# ısıl güç eşdeğerliği: R = 5 Ω
R = 5.0
assert abs(rms(sine) ** 2 / R - (V / math.sqrt(2)) ** 2 / R) < 1e-9
# başarısız: kare ve üçgen dalga
square = lambda x: V if x < 0.5 else -V
tri = lambda x: V * (4 * x if x < 0.25 else 2 - 4 * x if x < 0.75 else 4 * x - 4)
assert abs(rms(square) - V) < 1e-9 and abs(rms(tri) - V / math.sqrt(3)) < 1e-3
assert abs(rms(square) - V / math.sqrt(2)) > 1.0
""")
    ,
    SC("ac-count-2f", "Saniyede 2f: yön değişimi, sıfır geçişi, lambanın sönmesi ve mutlak tepe sayısı; T = 1/f",
       ["ac-frequency-period-counting", "ac-loop-graphs"],
       "Frekansı f (Hz) olan AC için 1 saniyede 2f kez yön değişir, 2f kez sıfırdan geçilir (lamba 2f kez söner) ve mutlak değerce 2f kez tepeye ulaşılır; pozitif tepe sayısı f'dir; T = 1/f; süre t ise t·f tam periyot.",
       "Bir periyotta sinüs iki kez işaret değiştirir ve iki kez |tepe| yapar.",
       ["Sinüs biçimli AC", "Sayım süresi periyodun tam katı (ya da büyük)"],
       ["Sayım süresi periyottan kısa ya da tam sayı katı değilse sayım ±1 sapar", "'Tepe' pozitif tepeler anlamında kullanılırsa f'dir, mutlak değerce tepe 2f'dir", "T = f yazmak"],
       "LOW", [TB("s. 294 ÖD-24 ç–d"), TB("s. 288 ÖD-18"), TB("s. 260 42. Alıştırma"), DV("sin(2π f t) sıfır geçişleri")],
       """
import math
def counts(f, dur=1.0, dt=1e-5, phase=0.1):
    n = int(round(dur / dt))
    y = [math.sin(2 * math.pi * f * k * dt + phase) for k in range(n + 1)]
    zeros = sum(1 for a, b in zip(y, y[1:]) if a * b < 0)
    ab = [abs(v) for v in y]
    peaks_abs = sum(1 for k in range(1, n) if ab[k] > ab[k - 1] and ab[k] >= ab[k + 1] and ab[k] > 0.999)
    peaks_pos = sum(1 for k in range(1, n) if y[k] > y[k - 1] and y[k] >= y[k + 1] and y[k] > 0.999)
    return zeros, peaks_abs, peaks_pos
for f in (50.0, 60.0, 120.0):
    z, pa, pp = counts(f)
    assert z == 2 * f and pa == 2 * f and pp == f and z / 2 == f * 1.0     # saniyedeki tam periyot sayısı = f (T = 1/f)
# başarısız: periyottan kısa sayım penceresi → 2f kuralı geçersiz
z, pa, pp = counts(50.0, dur=0.004)
assert z == 0 and abs(z - 2 * 50.0 * 0.004) > 0.3               # 2f·t = 0,4 tam sayı değil; sayım kuralı anlamsız
""")
    ,
    SC("dc-steady-no-emf", "DC kararlı durumda akı sabit → ε = 0; AC'de ε sürekli (f arttıkça büyür)",
       ["ac-led-data-interpretation", "transformer-structure-experiment", "transformer-chain-and-lamp-comparison"],
       "Komşu devre/ikincil bobinde DC kaynak kararlı durumda ε = 0 verir (lamba yanmaz); AC kaynakta akı sürekli değişir: lamba yanar ve frekans arttıkça (akım genliği aynıysa) ε artar. Yalnız anahtar kapanıp açılırken kısa süreli sıçrama olur.",
       "Karşılıklı indüksiyonda ε = −M·di/dt: DC kararlı halde di/dt = 0; sinüste di/dt genliği ∝ f.",
       ["Kaynak bobinin akımı komşu bobinin akısını belirliyor", "Kararlı durum (geçici bitmiş)"],
       ["Anahtar kapanırken/açılırken geçici ε vardır: voltmetre ya da LED anlık yanıp söner", "Çekirdeksiz ya da zayıf bağlı bobinde AC'de de ε küçüktür", "Çok düşük frekansta ε çok küçük olabilir; 'AC her zaman parlak yakar' denemez"],
       "MEDIUM", [TB("s. 265 13. Etkinlik 12.–16. adım"), TB("s. 286 ÖD-16 a"), DV("ε = −M·di/dt")],
       """
import math
Mu, R, L, V0 = 0.5, 2.0, 0.1, 6.0
h = 1e-7
eps = lambda i, t: -Mu * (i(t + h) - i(t - h)) / (2 * h)
i_dc = lambda t: (V0 / R) * (1 - math.exp(-R * t / L))
assert abs(eps(i_dc, 1e-3)) > 1.0                                     # geçici sıçrama
assert abs(eps(i_dc, 5.0)) < 1e-9                                     # kararlı durum → 0
def amp(f):
    i = lambda t: 3.0 * math.sin(2 * math.pi * f * t)
    return max(abs(eps(i, k / (f * 400.0))) for k in range(400))
a50, a100 = amp(50.0), amp(100.0)
assert abs(a100 / a50 - 2) < 1e-2 and a50 > 100                       # AC: ε sürekli, f ×2 → ε ×2
# başarısız: çok düşük frekans / kuvvetsiz bağ → küçük ε
assert amp(0.01) < 0.01 * a50
""")
    ,
]

# ---------------- Transformatör (program: hesaplamasız; kısa yollar oran/yön yorumu düzeyinde) ----------------
SHORTCUTS += [
    SC("transformer-v-proportional-n", "İdeal transformatörde V ∝ N: Vs/Vp = Ns/Np (gerilim sarımla aynı yönde)",
       ["transformer-structure-experiment", "transformer-turns-voltage-current-ratio", "transformer-chain-and-lamp-comparison"],
       "Ns > Np → Vs > Vp (yükseltici); Ns < Np → alçaltıcı; tabloda Np ve Vp sabitken Vs, Ns ile doğru orantılıdır; Ns sabitken Np artarsa Vs azalır.",
       "Çekirdekteki ortak akı değişimi her sarımda aynı gerilimi indükler: Vp = Np·dΦ/dt, Vs = Ns·dΦ/dt.",
       ["İdeal transformatör", "AC kaynak", "Demir çekirdek akıyı iki bobine de taşıyor", "Yük akımı küçük"],
       ["DC kaynakta kararlı durumda Vs = 0", "Yük akımı büyükse gerçek transformatörün bobin direnci nedeniyle Vs idealden küçük olur", "Çekirdeksiz ya da açık çekirdekli yapıda akı kaçar, oran bozulur", "Program hesaplamayı dışlar; kitapta Vp/Vs = Np/Ns var (s. 273)"],
       "MEDIUM", [TB("s. 265 13. Etkinlik 12.–16. adım"), TB("s. 268 Yapı"), TB("s. 273 Vp/Vs = Np/Ns"), DV("Faraday yasası, ortak akı")],
       """
import math
Vp0, Np = 6.0, 400
w = 2 * math.pi * 50
phi = lambda t: -Vp0 / (Np * w) * math.cos(w * t)                  # Vp = Np dΦ/dt = Vp0 sin wt olacak biçimde akı
h = 1e-7
dphi = lambda t: (phi(t + h) - phi(t - h)) / (2 * h)
for Ns in (100, 400, 1600):
    Vs_peak = max(Ns * dphi(k * 1e-4) for k in range(200))
    assert abs(Vs_peak / Vp0 - Ns / Np) < 1e-3
# Ns sabit, Np artarsa (Vp sabit) Vs azalır
def Vs_for(Np_, Ns_):
    phi2 = lambda t: -Vp0 / (Np_ * w) * math.cos(w * t)
    return max(Ns_ * (phi2(k * 1e-4 + h) - phi2(k * 1e-4 - h)) / (2 * h) for k in range(200))
assert Vs_for(800, 400) < Vs_for(400, 400)
# başarısız 1: DC → Vs = 0 (akı sabit)
assert abs(Np * 0.0) == 0.0 and abs(100 * ((3.0 - 3.0) / 1.0)) == 0.0
# başarısız 2: yüklü gerçek trafo (bobin direnci) → Vs idealden küçük
r_s, R_L = 5.0, 20.0
ideal = 12.0; loaded = ideal * R_L / (R_L + r_s)
assert loaded < ideal and abs(loaded / ideal - 0.8) < 1e-12
""")
    ,
    SC("transformer-i-inverse-n", "İdeal transformatörde i ∝ 1/N: is/ip = Np/Ns; giriş gücü = çıkış gücü",
       ["transformer-turns-voltage-current-ratio", "transformer-transmission-loss"],
       "Gerilim kaç kat artıyorsa akım o kadar kat azalır: yükselticide is < ip, alçaltıcıda is > ip; ideal transformatörde Vp·ip = Vs·is. Gerçek transformatörde çıkış gücü girişten küçüktür.",
       "Güç korunumu: Vp·ip = Vs·is ve Vs/Vp = Ns/Np ⇒ is/ip = Np/Ns.",
       ["İdeal (kayıpsız) transformatör", "AC kaynak"],
       ["Gerçek transformatörde is/ip oranı Np/Ns'ten küçüktür (kayıplar ısıya gider)", "Akım oranını sarım oranıyla doğru orantılı almak yanlıştır", "Gerilim kazanan taraf güç kazanmaz; akımdan öder"],
       "MEDIUM", [TB("s. 273 Vp/Vs = Np/Ns = is/ip"), TB("s. 270 45. Alıştırma"), TB("s. 288 ÖD-18 b, e"), DV("Enerji korunumu")],
       """
import random
from fractions import Fraction as Fr
random.seed(13)
for _ in range(300):
    Np, Ns = random.randint(10, 3000), random.randint(10, 3000)
    Vp, ip = Fr(random.randint(5, 400)), Fr(random.randint(1, 20))
    Vs = Vp * Fr(Ns, Np)
    is_ = Vp * ip / Vs                                              # güç korunumundan
    assert is_ / ip == Fr(Np, Ns) and Vs * is_ == Vp * ip
    assert (Ns > Np) == (is_ < ip) == (Vs > Vp)                     # yükseltici ↔ akım düşer
# başarısız 1: gerçek trafo (verim %90): çıkış akımı idealden küçük
eta = Fr(9, 10)
Np, Ns, Vp, ip = 1200, 300, Fr(120), Fr(1)
is_ideal = ip * Fr(Np, Ns)
is_real = eta * is_ideal
assert is_real < is_ideal and (Vp * Fr(Ns, Np)) * is_real == eta * Vp * ip
# başarısız 2: akımı sarımla doğru orantılı almak güç korunumunu bozar
assert (Vp * Fr(Ns, Np)) * (ip * Fr(Ns, Np)) != Vp * ip
""")
    ,
    SC("chain-multiply-turn-ratios", "Ardışık transformatörlerde k = Ns/Np çarpanları çarpılır",
       ["transformer-chain-and-lamp-comparison"],
       "Her trafonun k = Ns/Np çarpanını yaz; zincirde toplam çarpan k₁·k₂ (çarpım, toplam değil); hedef gerilim için son çarpan = V_hedef/V_ara.",
       "İlk trafonun ikincil gerilimi ikincinin birincil gerilimidir: V₃ = k₂·V₂ = k₂·k₁·V₁.",
       ["İdeal trafolar", "Birinin çıkışı diğerinin girişine doğrudan bağlı", "AC"],
       ["Aşamalardan biri DC ya da çekirdeksizse zincir kopar (çarpan 0)", "Gerçek trafolarda ikinci trafonun yükü birinciyi yükler; ideal kabul geçerli değildir", "Oranı ters (Np/Ns) kurmak sonucu ters çevirir", "Program hesaplamayı dışlar; çarpan düzeyinde"],
       "LOW", [TB("s. 272 47. Alıştırma"), DV("Gerilim dönüşümlerinin bileşkesi")],
       """
import random
from fractions import Fraction as Fr
random.seed(31)
def secondary(V, Np, Ns, ok=True):
    return V * Fr(Ns, Np) if ok else Fr(0)
for _ in range(300):
    V = Fr(random.randint(10, 400))
    Np1, Ns1, Np2, Ns2 = (random.randint(10, 900) for _ in range(4))
    chained = secondary(secondary(V, Np1, Ns1), Np2, Ns2)
    assert chained == V * Fr(Ns1, Np1) * Fr(Ns2, Np2)
    # hedef: son gerilim V olsun → Ns2 gerekli
    need = Fr(Np2) * Fr(Np1, Ns1)
    assert secondary(secondary(V, Np1, Ns1), Np2, need) == V
# başarısız 1: toplama yanlış sonuç
V = Fr(100); k1, k2 = Fr(3), Fr(1, 2)
assert V * (k1 * k2) != V * (k1 + k2)
# başarısız 2: ara aşama çekirdeksiz/DC → zincir kopar
assert secondary(secondary(V, 100, 300, ok=False), 300, 150) == 0
# ters çevrik oran sonucu tersine çevirir
assert V * Fr(100, 300) != V * Fr(300, 100)
""")
    ,
    SC("lamp-brightness-order-by-voltage", "Özdeş lambalarda parlaklık sırası = ikincil gerilim sırası (P ∝ V²)",
       ["transformer-chain-and-lamp-comparison"],
       "Aynı AC kaynağa bağlı trafolarda özdeş lambaların parlaklık sırası ikincil gerilim sırasıdır; k = Ns/Np'yi karşılaştır. Direnç sabitse güç oranı gerilim oranının karesidir.",
       "Lamba gücü P = V²/R; R özdeşse P yalnız V'ye bağlı ve V ile artan bir fonksiyondur.",
       ["Lambalar özdeş", "Aynı kaynak gerilimi", "İdeal trafolar"],
       ["Lamba direnci sıcaklıkla artar: sıra korunur ama güç oranı gerilim oranının karesi değildir", "Lamba anma gerilimini aşarsa yanar: sıralama anlamsızlaşır", "Farklı yük (özdeş olmayan lamba) ya da çekirdeksiz yapıda sıralama değişir"],
       "MEDIUM", [TB("s. 272 47. Alıştırma c"), DV("P = V²/R")],
       """
import random
random.seed(17)
R0, a = 10.0, 0.03                                                  # R(V) = R0 (1 + a V)  (sıcaklıkla artan direnç)
P_const = lambda V: V ** 2 / R0
P_real = lambda V: V ** 2 / (R0 * (1 + a * V))
for _ in range(300):
    V1, V2 = sorted(random.uniform(1, 40) for _ in range(2))
    if V2 - V1 < 1e-6: continue
    assert P_const(V1) < P_const(V2) and P_real(V1) < P_real(V2)    # sıra her iki modelde aynı
# başarısız: direnç sabit değilse güç oranı gerilim oranının karesi değil
V1, V2 = 10.0, 30.0
assert abs(P_const(V2) / P_const(V1) - 9) < 1e-12
assert abs(P_real(V2) / P_real(V1) - 9) > 0.5
""")
    ,
    SC("transmission-loss-i-squared", "İletimde kayıp: V ×n → i ÷n → kayıp ÷n² (P_kayıp ∝ i²R)",
       ["transformer-transmission-loss"],
       "İletilen güç sabitken hat akımı gerilimle ters orantılıdır; kayıp i²R olduğundan gerilim n kat artarsa kayıp n² kat azalır; hat direnci k kat olursa kayıp k kat olur.",
       "P = V·i ⇒ i = P/V; P_kayıp = i²·R ⇒ P_kayıp = P²R/V².",
       ["İletilen güç sabit", "Hat direnci sabit ya da çarpanı verilmiş", "Kayıp yalnız hatta"],
       ["Yük direnci sabitse gerilim artınca akım artar (sabit güç varsayımı geçersiz)", "P_kayıp = V²/R'de V hattın iki ucu arası gerilim düşümüdür, kaynak gerilimi değil", "Program hesaplamayı dışlar; oran düzeyinde (kitapta P = V·i ve P = i²R var)"],
       "MEDIUM", [TB("s. 269 Örnek"), TB("s. 294 ÖD-24 c"), TB("s. 263 P = V·i; P_kayıp = i²·R"), DV("P_kayıp = P²R/V²")],
       """
import random
random.seed(23)
loss = lambda P, V, R: (P / V) ** 2 * R
for _ in range(300):
    P, V, R = random.uniform(1e5, 1e7), random.uniform(5e3, 5e5), random.uniform(1, 50)
    n, k = random.choice([2, 3, 5, 10]), random.choice([0.5, 2, 3])
    assert abs(loss(P, n * V, R) / loss(P, V, R) - 1 / n ** 2) < 1e-12
    assert abs(loss(P, V, k * R) / loss(P, V, R) - k) < 1e-12
    assert abs(loss(P, n * V, k * R) / loss(P, V, R) - k / n ** 2) < 1e-12
# başarısız 1: yük direnci sabitse gerilim artınca akım artar
R_load = 100.0
assert (5e3 * 5) / R_load > 5e3 / R_load
# başarısız 2: kayıp için V²/R'de kaynak gerilimi kullanmak büyük hata verir
P, V, R = 1e6, 20e3, 10.0
assert abs(loss(P, V, R) - ((P / V) * R) ** 2 / R) < 1e-6 and abs(V ** 2 / R - loss(P, V, R)) > 1e6
""")
    ,
    SC("step-up-step-down-by-voltage-comparison", "Rol tablosu: çıkış/cihaz gerilimi < giriş → alçaltıcı; > giriş → yükseltici",
       ["transformer-applications-record", "transformer-transmission-loss"],
       "Kayıt tablosunda her satırda cihazın (çıkış) gerilimini şebeke (giriş) gerilimiyle karşılaştır: küçükse alçaltıcı, büyükse yükseltici, eşitse transformatör gerekmez; yazılı rolle çelişen hücre yanlıştır. Santral yanı yükseltici, tüketici yanı alçaltıcıdır.",
       "Vs/Vp = Ns/Np olduğundan Vs < Vp ancak Ns < Np ile mümkündür (alçaltıcı) ve tersi yükselticidir.",
       ["AC şebeke", "Giriş (kaynak) ve çıkış (cihaz) gerilimleri biliniyor"],
       ["Ters bağlama: aynı transformatör çıkış tarafından beslenirse rolü tersine döner", "Transformatör gerilimi AC olarak dönüştürür; DC ile çalışan cihaz (telefon şarjı) ayrıca doğrultucu ister", "Cihazın etiketindeki gerilim şebeke gerilimi değil, cihazın ihtiyacıdır", "Program yalnız rolü yorumlatır, sarım oranı hesabı sorulmaz"],
       "LOW", [TB("s. 263 Gerilim dönüştürücü"), TB("s. 265 13. Etkinlik 18. adım"), TB("s. 270 45. Alıştırma"), DV("Vs/Vp = Ns/Np")],
       """
def role(v_in, v_out):
    return "alçaltıcı" if v_out < v_in else "yükseltici" if v_out > v_in else "gerekmez"
cases = [(230, 5, "alçaltıcı"), (230, 2000, "yükseltici"), (10e3, 150e3, "yükseltici"), (150e3, 10e3, "alçaltıcı"), (230, 110, "alçaltıcı"), (230, 230, "gerekmez")]
for vin, vout, expected in cases:
    assert role(vin, vout) == expected
    # tam yöntem: sarım oranı Ns/Np = Vs/Vp → Ns < Np ⇔ alçaltıcı
    Np, Ns = 1000, 1000 * vout / vin
    assert (Ns < Np) == (expected == "alçaltıcı") and (Ns > Np) == (expected == "yükseltici")
# başarısız: ters bağlama rolü değiştirir
assert role(230, 5) == "alçaltıcı" and role(5, 230) == "yükseltici"
# başarısız: DC kaynakta transformatör rolü yok (kararlı durumda ikincil gerilim sıfır)
def secondary_dc(v_in, Np, Ns):
    return 0.0
assert secondary_dc(12.0, 100, 1000) == 0.0 and role(12.0, 120.0) == "yükseltici"
""")
    ,
]

# ---------------- Ek kısa yollar: kapalı iletken (Faraday kafesi), tablo eğilimi, motor ----------------
SHORTCUTS += [
    SC("closed-conductor-shield-decision", "Faraday kafesi: kapalı iletken kabuk → iç bölge korunur; açık/boşluklu → zayıf; yalıtkan → korumaz",
       ["fcage-verify-claims"],
       "Önce kabuğun cinsine ve kapalılığına bak: iletken ve kapalıysa içerideki alan (yaklaşık) sıfırdır; delikli/açık kabukta koruma zayıflar; yalıtkan kabuk korumaz. 'İçeride yük birikir' ifadesi yanlıştır, fazla yük dış yüzeyde toplanır.",
       "İletken kabuk yük hareketiyle eş potansiyel olur; iç bölgede yük yoksa Laplace denkleminin tek çözümü sabit potansiyeldir (E = 0).",
       ["Kabuk iletken", "Kabuk kapalı (boşluklar çok küçük)", "Elektrostatik/yavaş değişen alan"],
       ["Büyük açıklıklı ya da tel örgü gözleri alan dalgası boyundan büyükse koruma azalır", "Yalıtkan kabuk iç bölgeyi korumaz", "Kabuğun içine yerleştirilmiş yük, iç bölgede alan oluşturur (koruma dışarıdan gelen alana karşıdır)"],
       "MEDIUM", [TB("s. 182 Örnek"), TB("s. 183 11.–12. Alıştırma"), TB("s. 184 13. Alıştırma"), DV("Laplace denklemi, iç bölgede yük yok ⇒ sabit potansiyel")],
       """
N = 41
def solve(box="closed", sweeps=1500):
    # 2B Laplace: sol kenar +1, sağ kenar −1, üst/alt doğrusal (düzgün dış alan). Kabuk: 11..29 halkası.
    V = [[1.0 - 2.0 * j / (N - 1) for j in range(N)] for _ in range(N)]
    lo, hi = 11, 29
    fixed = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            edge = i in (0, N - 1) or j in (0, N - 1)
            ring = (lo <= i <= hi and lo <= j <= hi) and (i in (lo, hi) or j in (lo, hi))
            if edge:
                fixed[i][j] = True
            elif ring and box in ("closed", "gap"):
                if box == "gap" and i == lo and 17 <= j <= 23:
                    continue                                       # kabukta açıklık
                fixed[i][j] = True; V[i][j] = 0.0
    for _ in range(sweeps):
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if not fixed[i][j]:
                    V[i][j] = 0.25 * (V[i - 1][j] + V[i + 1][j] + V[i][j - 1] + V[i][j + 1])
    # iç bölgede (lo+1..hi−1) yatay alan büyüklüğü (potansiyel farkı/hücre)
    inner = [abs(V[i][j + 1] - V[i][j]) for i in range(lo + 2, hi - 1) for j in range(lo + 2, hi - 2)]
    return max(inner), 2.0 / (N - 1)
E_closed, E0 = solve("closed"); E_gap, _ = solve("gap"); E_ins, _ = solve("insulator")
assert E_closed < 0.05 * E0                       # kapalı iletken → iç alan çok küçük
assert E_closed < E_gap < E_ins                   # açıklık koruma zayıflatır; yalıtkan korumaz
assert E_ins > 0.8 * E0 and E_gap > 5 * E_closed
""")
    ,
    SC("monotonic-trend-outlier-check", "Tablo eğilimi: beklenen azalan/artan veride yönü bozan değer hatalıdır (ardışık satır karşılaştırması)",
       ["magnet-data-collection", "coulomb-data-table-graph"],
       "Çıktının mesafeyle azalması (ya da etmenle artması) bekleniyorsa ardışık satırları sırayla karşılaştır: eğilimi bozan satır hatalı kayıttır; sonra modelle (ör. 1/d²) doğru değeri bul.",
       "Fiziksel ilişki monoton (ör. B ve F mesafeyle azalır) olduğundan veride yön değiştiren nokta ölçüm/kayıt hatasıdır.",
       ["İlişkinin monoton olduğu fiziksel olarak biliniyor", "Ölçüm hatası yön değişimi yaratacak kadar büyük değil (aksi halde gerçek dalgalanma olabilir)"],
       ["Ölçüm gürültüsü küçük yön değişimleri yapar: her bozulma hata değildir (tekrarlı ölçümlerle kontrol et)", "İlişki monoton değilse (ör. kutup çevresi, çizgi sıklığı) kural uygulanamaz", "Hata monoton eğilimi bozmayacak bir değerde ise (ör. biraz yüksek) yöntem onu yakalayamaz"],
       "MEDIUM", [TB("s. 188 5.–7. adım"), TB("s. 193 14. Alıştırma"), DV("Monoton fonksiyonun ardışık farklarının işareti sabittir")],
       """
d = [1, 2, 3, 4, 5, 6]
true = [100.0 / x ** 2 for x in d]                      # azalan beklenen: B ∝ 1/d²
recorded = list(true); recorded[3] = 14.0               # d=4 satırı (doğrusu 6,25) hatalı: d=3'ten (11,1) büyük yazılmış
bad = [k + 2 for k in range(len(recorded) - 1) if recorded[k + 1] >= recorded[k]]
assert bad == [4]                                        # 4. satır (d=4) eğilimi bozuyor → yakalanır
assert abs(true[3] - 6.25) < 1e-12                       # düzeltme modelle
# başarısız 1: eğilimi bozmayan hatalı değer yakalanmaz
recorded2 = list(true); recorded2[3] = 7.5               # 6,25 yerine 7,5 → yine azalan
assert not [k for k in range(len(recorded2) - 1) if recorded2[k + 1] >= recorded2[k]] and abs(recorded2[3] - true[3]) > 1
# başarısız 2: gürültülü gerçek veri küçük yön değişimleri verir (hata sanma)
noisy = [10.0, 9.9, 9.95, 9.8]                           # gerçekte azalan; ölçüm gürültüsü 3. satırı yükseltti
assert any(noisy[k + 1] >= noisy[k] for k in range(len(noisy) - 1))
""")
    ,
    SC("commutator-half-turn-reversal", "Motor: akım yönü her yarım turda tersine çevrilmeli (komütatör); enerji dönüşümü kayıplıdır (η < 1)",
       ["motor-principle-evaluation", "loop-rotation-torque"],
       "Sabit akım yönünde döndürme çiftinin işareti yarım turda değişir ve dönüş sürmez; her yarım turda akımı ters çeviren komütatör (ya da AC) döndürme etkisini aynı işaretli tutar. Elektrik enerjisinin yalnız bir kısmı hareket enerjisine dönüşür.",
       "τ ∝ i·B·A·sinφ: φ π'yi geçince sinφ negatiftir; akım da işaret değiştirirse τ işaretini korur.",
       ["Düzgün alanda dönen çerçeve", "Komütatör yarım turda akımı ters çeviriyor"],
       ["Komütatör olmazsa çerçeve ölü noktada takılır ve salınır", "Sürtünme ve ısı kayıpları nedeniyle verim 1'den küçüktür", "Metin yargılarında (çıkarım) 'veriye dayanıyor mu?' kontrolü sayısal kısa yolun dışındadır"],
       "LOW", [TB("s. 231 Değerlendirme 2"), TB("s. 292 ÖD-22"), TB("s. 230 Fizik Gazetesi"), DV("τ = N·i·B·A·sinφ")],
       """
import math
n = 3600
tau_dc = [math.sin(2 * math.pi * k / n) for k in range(n)]                          # akım sabit (i = 1)
tau_comm = [abs(t) for t in tau_dc]                                                  # komütatör: sinφ<0 ise akım ters
assert abs(sum(tau_dc) / n) < 1e-9                                                    # sabit akımda tam turda ortalama çift sıfır
assert abs(sum(tau_comm) / n - 2 / math.pi) < 1e-3                                    # komütatörle ortalama > 0
assert min(tau_comm) >= 0
# enerji: P_mekanik = P_elektrik − kayıplar < P_elektrik
V, i, r, friction = 12.0, 2.0, 1.5, 3.0
P_el = V * i; P_mech = P_el - i ** 2 * r - friction
assert 0 < P_mech < P_el and abs(P_mech / P_el - 0.625) < 1e-12
# başarısız: komütatörsüz çerçeve ölü noktada (φ = 0) döndürme çifti sıfır
assert abs(tau_dc[0]) < 1e-12 and abs(tau_dc[n // 2]) < 1e-9
""")
    ,
]
