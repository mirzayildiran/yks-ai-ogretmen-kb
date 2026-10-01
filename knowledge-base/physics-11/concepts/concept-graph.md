# 11. Sınıf Fizik — Kavram Grafiği

> Otomatik üretildi: `scripts/build_concepts.py` (kaynak veri: `scripts/data_concepts.py`). Elle düzenleme yapma.

- **Kavram:** 137 (104 11. sınıf, 33 ön koşul)
- **İlişki:** 220
- Kavram tanımları ve ilişkiler yapay zekâ tarafından yazıldı, **uzman incelemesi bekliyor** (güven: MEDIUM). Resmî anahtar kavramlar HIGH.

Okuma: `A --> B` = A, B'yi gerektirir (REQUIRES). Kesikli ok: özel durum / parçası.

## Ünite 1: KUVVET VE HAREKET

```mermaid
flowchart LR
  acisal_hiz["Açısal hız"]
  acisal_ivme["Açısal ivme"]
  agirlik(["Ağırlık"])
  bagli_cisim_sistemi["Aynı ivmeli bağlı cisim sistemleri"]
  bilesenlerin_bagimsizligi["Hareket bileşenlerinin bağımsızlığı"]
  bileske_kuvvet["Bileşke (net) kuvvet"]
  cizgisel_hiz["Çizgisel hız"]
  cizgisel_surat["Çizgisel sürat"]
  donerek_oteleme["Dönerek öteleme hareketi"]
  dusey_duzlemde_cembersel["Düşey düzlemde çembersel hareket"]
  duzgun_cembersel_hareket["Düzgün çembersel hareket"]
  egik_duzlem["Eğik düzlem"]
  egimli_viraj["Eğimli viraj"]
  etki_tepki["Etki-tepki kuvvetleri (Newton'ın 3. Yasası)"]
  eylemsizlik["Eylemsizlik"]
  frekans(["Frekans"])
  gerilme_kuvveti["İp gerilme kuvveti"]
  grafik_egim_alan(["Grafikte eğim ve alan"])
  hareket_grafikleri(["Konum-zaman, hız-zaman, ivme-zaman grafikleri"])
  hava_direnci["Hava (akışkan) direnç kuvveti"]
  hiz(["Hız"])
  iki_boyutta_sabit_ivmeli_hareket["İki boyutta sabit ivmeli hareket"]
  ivme(["İvme"])
  kayarak_oteleme["Kayarak öteleme hareketi"]
  kesit_alani["Kesit alanı"]
  kinetik_surtunme["Kinetik sürtünme kuvveti"]
  konum(["Konum"])
  kutle(["Kütle"])
  kuvvet(["Kuvvet"])
  limit_hiz["Limit hız"]
  maksimum_statik_surtunme["Maksimum statik sürtünme (harekete geçme sınırı)"]
  maksimum_yukseklik["Maksimum yükseklik"]
  menzil["Menzil"]
  merkezcil_ivme["Merkezcil ivme"]
  merkezcil_kuvvet["Merkezcil kuvvet"]
  newton_birinci_yasa["Newton'ın 1. Hareket Yasası (eylemsizlik ilkesi)"]
  newton_ikinci_yasa["Newton'ın 2. Hareket Yasası (temel yasa)"]
  normal_kuvvet["Normal (tepki) kuvveti"]
  oran_oranti(["Doğru ve ters orantı"])
  parabolik_yorunge["Parabolik yörünge"]
  periyot(["Periyot"])
  sabit_hizli_hareket(["Sabit hızlı hareket"])
  sabit_ivmeli_hareket(["Bir boyutta sabit ivmeli hareket"])
  serbest_cisim_diyagrami["Serbest cisim diyagramı"]
  serbest_dusme["Serbest düşme"]
  skaler_nicelik(["Skaler nicelik"])
  statik_surtunme["Statik sürtünme kuvveti"]
  surat(["Sürat"])
  surtunme_katsayisi["Sürtünme katsayısı"]
  surtunme_kuvveti["Sürtünme kuvveti"]
  tepe_noktasi_hareket["Tepe noktası (yukarı yönlü serbest düşmede)"]
  trigonometrik_oranlar(["Trigonometrik oranlar (sin, cos, tan)"])
  ucus_suresi["Uçuş süresi"]
  vektor_bilesenleri(["Vektörün bileşenlerine ayrılması"])
  vektorel_nicelik(["Vektörel nicelik"])
  yaricap_vektoru["Yarıçap vektörü"]
  yatay_duzlemde_cembersel["Yatay düzlemde düzgün çembersel hareket"]
  yatay_viraj["Yatay viraj"]
  yer_cekimi_ivmesi["Yer çekimi ivmesi"]
  yer_degistirme(["Yer değiştirme"])
  vektor_bilesenleri --> vektorel_nicelik
  vektor_bilesenleri --> trigonometrik_oranlar
  yer_degistirme --> konum
  yer_degistirme --> vektorel_nicelik
  hiz --> yer_degistirme
  surat --> skaler_nicelik
  ivme --> hiz
  sabit_hizli_hareket --> hiz
  sabit_ivmeli_hareket --> ivme
  hareket_grafikleri --> grafik_egim_alan
  hareket_grafikleri --> sabit_ivmeli_hareket
  agirlik --> kuvvet
  agirlik --> kutle
  frekans --> periyot
  serbest_dusme -.->|özel durum| sabit_ivmeli_hareket
  serbest_dusme --> yer_cekimi_ivmesi
  serbest_dusme --> hareket_grafikleri
  yer_cekimi_ivmesi --> ivme
  hava_direnci -.->|özel durum| surtunme_kuvveti
  tepe_noktasi_hareket -.->|parçası| serbest_dusme
  tepe_noktasi_hareket --> ivme
  maksimum_yukseklik -.->|parçası| serbest_dusme
  iki_boyutta_sabit_ivmeli_hareket --> vektor_bilesenleri
  iki_boyutta_sabit_ivmeli_hareket --> sabit_hizli_hareket
  iki_boyutta_sabit_ivmeli_hareket --> serbest_dusme
  iki_boyutta_sabit_ivmeli_hareket --> bilesenlerin_bagimsizligi
  iki_boyutta_sabit_ivmeli_hareket --> trigonometrik_oranlar
  bilesenlerin_bagimsizligi --> vektor_bilesenleri
  parabolik_yorunge -.->|parçası| iki_boyutta_sabit_ivmeli_hareket
  menzil -.->|parçası| iki_boyutta_sabit_ivmeli_hareket
  menzil --> ucus_suresi
  ucus_suresi -.->|parçası| iki_boyutta_sabit_ivmeli_hareket
  ucus_suresi --> serbest_dusme
  bileske_kuvvet --> kuvvet
  bileske_kuvvet --> vektorel_nicelik
  eylemsizlik --> kutle
  newton_birinci_yasa --> bileske_kuvvet
  newton_birinci_yasa --> eylemsizlik
  newton_ikinci_yasa --> bileske_kuvvet
  newton_ikinci_yasa --> ivme
  newton_ikinci_yasa --> kutle
  etki_tepki --> kuvvet
  serbest_cisim_diyagrami --> kuvvet
  serbest_cisim_diyagrami --> vektorel_nicelik
  normal_kuvvet --> kuvvet
  gerilme_kuvveti --> kuvvet
  bagli_cisim_sistemi --> newton_ikinci_yasa
  bagli_cisim_sistemi --> serbest_cisim_diyagrami
  bagli_cisim_sistemi --> gerilme_kuvveti
  egik_duzlem --> vektor_bilesenleri
  egik_duzlem --> serbest_cisim_diyagrami
  egik_duzlem --> agirlik
  surtunme_kuvveti --> kuvvet
  surtunme_kuvveti --> normal_kuvvet
  statik_surtunme -.->|özel durum| surtunme_kuvveti
  kinetik_surtunme -.->|özel durum| surtunme_kuvveti
  maksimum_statik_surtunme -.->|parçası| statik_surtunme
  surtunme_katsayisi -.->|parçası| surtunme_kuvveti
  limit_hiz --> hava_direnci
  limit_hiz --> agirlik
  limit_hiz --> newton_birinci_yasa
  duzgun_cembersel_hareket --> cizgisel_hiz
  duzgun_cembersel_hareket --> periyot
  duzgun_cembersel_hareket --> yaricap_vektoru
  cizgisel_hiz --> hiz
  cizgisel_hiz --> vektorel_nicelik
  cizgisel_surat --> surat
  cizgisel_surat --> periyot
  acisal_hiz --> periyot
  acisal_hiz --> frekans
  acisal_ivme --> acisal_hiz
  merkezcil_ivme --> cizgisel_hiz
  merkezcil_ivme --> ivme
  merkezcil_kuvvet --> merkezcil_ivme
  merkezcil_kuvvet --> newton_ikinci_yasa
  merkezcil_kuvvet --> bileske_kuvvet
  yatay_duzlemde_cembersel -.->|özel durum| duzgun_cembersel_hareket
  yatay_duzlemde_cembersel --> merkezcil_kuvvet
  dusey_duzlemde_cembersel -.->|özel durum| duzgun_cembersel_hareket
  dusey_duzlemde_cembersel --> merkezcil_kuvvet
  dusey_duzlemde_cembersel --> agirlik
  dusey_duzlemde_cembersel --> gerilme_kuvveti
  yatay_viraj -.->|özel durum| yatay_duzlemde_cembersel
  yatay_viraj --> statik_surtunme
  egimli_viraj -.->|özel durum| duzgun_cembersel_hareket
  egimli_viraj --> merkezcil_kuvvet
  egimli_viraj --> normal_kuvvet
  egimli_viraj --> vektor_bilesenleri
```

Yuvarlak kutu = önceki sınıflardan gelen ön koşul kavramı.

| Öğrenme çıktısı | 11. sınıf kavramları | Ön koşul kavramları |
|---|---|---|
| FİZ.11.1.1 | Serbest düşme, Yer çekimi ivmesi | Hız, İvme, Bir boyutta sabit ivmeli hareket, Kütle |
| FİZ.11.1.2 | Serbest düşme, Yer çekimi ivmesi, Tepe noktası (yukarı yönlü serbest düşmede), Maksimum yükseklik | Grafikte eğim ve alan, Konum, Yer değiştirme, Hız, İvme, Bir boyutta sabit ivmeli hareket, Konum-zaman, hız-zaman, ivme-zaman grafikleri |
| FİZ.11.1.3 | Yer çekimi ivmesi, Tepe noktası (yukarı yönlü serbest düşmede), Maksimum yükseklik, İki boyutta sabit ivmeli hareket, Hareket bileşenlerinin bağımsızlığı, Parabolik yörünge, Menzil, Uçuş süresi | Vektörel nicelik, Vektörün bileşenlerine ayrılması, Trigonometrik oranlar (sin, cos, tan), Grafikte eğim ve alan, Yer değiştirme, Hız, İvme, Sabit hızlı hareket, Bir boyutta sabit ivmeli hareket, Konum-zaman, hız-zaman, ivme-zaman grafikleri |
| FİZ.11.1.4 | Bileşke (net) kuvvet, Eylemsizlik, Newton'ın 1. Hareket Yasası (eylemsizlik ilkesi), Newton'ın 2. Hareket Yasası (temel yasa), Etki-tepki kuvvetleri (Newton'ın 3. Yasası) | İvme, Kuvvet, Kütle |
| FİZ.11.1.5 | Bileşke (net) kuvvet, Newton'ın 1. Hareket Yasası (eylemsizlik ilkesi), Newton'ın 2. Hareket Yasası (temel yasa), Etki-tepki kuvvetleri (Newton'ın 3. Yasası), Serbest cisim diyagramı, Normal (tepki) kuvveti, İp gerilme kuvveti, Aynı ivmeli bağlı cisim sistemleri, Eğik düzlem | Bir boyutta sabit ivmeli hareket, Kuvvet, Ağırlık |
| FİZ.11.1.6 | Sürtünme kuvveti, Statik sürtünme kuvveti, Kinetik sürtünme kuvveti, Maksimum statik sürtünme (harekete geçme sınırı), Kayarak öteleme hareketi, Dönerek öteleme hareketi |  |
| FİZ.11.1.7 | Newton'ın 2. Hareket Yasası (temel yasa), Normal (tepki) kuvveti, Eğik düzlem, Sürtünme kuvveti, Statik sürtünme kuvveti, Kinetik sürtünme kuvveti, Maksimum statik sürtünme (harekete geçme sınırı), Sürtünme katsayısı, Kayarak öteleme hareketi, Dönerek öteleme hareketi | Doğru ve ters orantı, Grafikte eğim ve alan |
| FİZ.11.1.8 | Hava (akışkan) direnç kuvveti, Newton'ın 1. Hareket Yasası (eylemsizlik ilkesi), Sürtünme kuvveti, Limit hız, Kesit alanı | Kütle, Ağırlık |
| FİZ.11.1.9 | Düzgün çembersel hareket, Yarıçap vektörü, Çizgisel hız | Vektörel nicelik |
| FİZ.11.1.10 | Bileşke (net) kuvvet, Newton'ın 2. Hareket Yasası (temel yasa), İp gerilme kuvveti, Statik sürtünme kuvveti, Düzgün çembersel hareket, Çizgisel hız, Çizgisel sürat, Açısal hız, Açısal ivme, Merkezcil ivme, Merkezcil kuvvet, Yatay düzlemde düzgün çembersel hareket, Düşey düzlemde çembersel hareket, Yatay viraj, Eğimli viraj | Skaler nicelik, Doğru ve ters orantı, Sürat, Ağırlık, Periyot, Frekans |

## Ünite 2: ELEKTRİK VE MANYETİZMA

```mermaid
flowchart LR
  akim_makarasi["Akım makarası"]
  alternatif_akim["Alternatif (değişken) akım"]
  bileske_elektriksel_alan["Bileşke elektriksel alan"]
  birincil_ikincil_sarim["Birincil ve ikincil sarım"]
  coulomb_sabiti["Coulomb sabiti"]
  coulomb_yasasi["Coulomb Yasası"]
  direnc(["Elektriksel direnç"])
  dunyanin_manyetik_alani["Dünya'nın manyetik alanı"]
  duz_telin_manyetik_alani["Akım geçen düz telin manyetik alanı"]
  elektrik_akimi(["Elektrik akımı"])
  elektrik_motoru["Elektrik motoru"]
  elektrik_yuku(["Elektrik yükü"])
  elektriksel_alan["Elektriksel alan"]
  elektriksel_alan_cizgileri["Elektriksel alan çizgileri"]
  elektriksel_kuvvet["Elektriksel kuvvet"]
  elektromiknatis["Elektromıknatıs"]
  elektroskop(["Elektroskop"])
  enerji_donusumu(["Enerji dönüşümü"])
  etkin_deger["Alternatif akımda etkin değer"]
  faraday_induksiyon_yasasi["Faraday'ın indüksiyon yasası"]
  faraday_kafesi["Faraday kafesi"]
  frekans(["Frekans"])
  iletimde_enerji_kaybi["Elektrik iletiminde enerji kaybı"]
  induksiyon_akimi["İndüksiyon akımı"]
  induksiyon_gerilimi["İndüksiyon gerilimi (indüksiyon emk)"]
  jenerator["Elektrik jeneratörü"]
  kuvvet(["Kuvvet"])
  lenz_yasasi["Lenz Yasası"]
  manyetik_aki["Manyetik akı"]
  manyetik_alan["Manyetik alan"]
  manyetik_alan_cizgileri["Manyetik alan çizgileri"]
  manyetik_alan_katsayisi["Manyetik alan katsayısı"]
  manyetik_kutup(["Manyetik kutup"])
  manyetik_kuvvet["Manyetik kuvvet"]
  miknatis(["Mıknatıs"])
  noktasal_yuk["Noktasal yük"]
  oersted_deneyi["Ørsted deneyi"]
  oran_oranti(["Doğru ve ters orantı"])
  periyot(["Periyot"])
  potansiyel_fark(["Potansiyel fark (gerilim)"])
  pusula(["Pusula"])
  sag_el_kurali["Sağ el kuralı"]
  sarim_sayisi["Sarım sayısı"]
  tele_etki_eden_manyetik_kuvvet["Manyetik alanda akım geçen tele etki eden kuvvet"]
  ters_kare_iliskisi(["Ters kare ilişkisi"])
  transformator["Transformatör"]
  vektorel_nicelik(["Vektörel nicelik"])
  frekans --> periyot
  manyetik_kutup -.->|parçası| miknatis
  direnc --> potansiyel_fark
  direnc --> elektrik_akimi
  elektrik_akimi --> elektrik_yuku
  elektriksel_kuvvet --> elektrik_yuku
  elektriksel_kuvvet --> kuvvet
  coulomb_yasasi --> elektriksel_kuvvet
  coulomb_yasasi --> noktasal_yuk
  coulomb_yasasi --> ters_kare_iliskisi
  coulomb_yasasi --> oran_oranti
  coulomb_sabiti -.->|parçası| coulomb_yasasi
  noktasal_yuk --> elektrik_yuku
  elektriksel_alan --> elektriksel_kuvvet
  elektriksel_alan --> vektorel_nicelik
  elektriksel_alan --> ters_kare_iliskisi
  elektriksel_alan_cizgileri -.->|parçası| elektriksel_alan
  bileske_elektriksel_alan --> elektriksel_alan
  bileske_elektriksel_alan --> vektorel_nicelik
  faraday_kafesi --> elektriksel_alan
  manyetik_alan --> miknatis
  manyetik_alan --> vektorel_nicelik
  manyetik_alan_cizgileri -.->|parçası| manyetik_alan
  dunyanin_manyetik_alani -.->|özel durum| manyetik_alan
  elektrik_akimi ==>|oluşturur| manyetik_alan
  duz_telin_manyetik_alani --> elektrik_akimi
  duz_telin_manyetik_alani --> manyetik_alan
  duz_telin_manyetik_alani --> sag_el_kurali
  duz_telin_manyetik_alani --> oran_oranti
  manyetik_alan_katsayisi -.->|parçası| duz_telin_manyetik_alani
  akim_makarasi --> duz_telin_manyetik_alani
  akim_makarasi --> sarim_sayisi
  akim_makarasi --> sag_el_kurali
  elektromiknatis --> akim_makarasi
  manyetik_kuvvet --> manyetik_alan
  manyetik_kuvvet --> kuvvet
  tele_etki_eden_manyetik_kuvvet -.->|özel durum| manyetik_kuvvet
  tele_etki_eden_manyetik_kuvvet --> elektrik_akimi
  tele_etki_eden_manyetik_kuvvet --> sag_el_kurali
  elektrik_motoru --> tele_etki_eden_manyetik_kuvvet
  elektrik_motoru --> enerji_donusumu
  manyetik_aki --> manyetik_alan
  manyetik_aki ==>|oluşturur| induksiyon_gerilimi
  faraday_induksiyon_yasasi --> manyetik_aki
  faraday_induksiyon_yasasi -.->|parçası| induksiyon_gerilimi
  induksiyon_gerilimi --> potansiyel_fark
  induksiyon_gerilimi ==>|oluşturur| induksiyon_akimi
  induksiyon_akimi --> elektrik_akimi
  lenz_yasasi --> induksiyon_akimi
  lenz_yasasi --> manyetik_aki
  alternatif_akim --> induksiyon_akimi
  alternatif_akim --> periyot
  etkin_deger -.->|parçası| alternatif_akim
  jenerator --> induksiyon_gerilimi
  jenerator --> enerji_donusumu
  jenerator ==>|oluşturur| alternatif_akim
  transformator --> induksiyon_gerilimi
  transformator --> alternatif_akim
  transformator --> sarim_sayisi
  birincil_ikincil_sarim -.->|parçası| transformator
  iletimde_enerji_kaybi --> direnc
  iletimde_enerji_kaybi --> elektrik_akimi
```

Yuvarlak kutu = önceki sınıflardan gelen ön koşul kavramı.

| Öğrenme çıktısı | 11. sınıf kavramları | Ön koşul kavramları |
|---|---|---|
| FİZ.11.2.1 | Elektriksel kuvvet, Coulomb Yasası, Coulomb sabiti, Noktasal yük | Doğru ve ters orantı, Ters kare ilişkisi, Kuvvet, Elektrik yükü, Elektroskop |
| FİZ.11.2.2 | Noktasal yük, Elektriksel alan, Elektriksel alan çizgileri, Bileşke elektriksel alan | Vektörel nicelik, Ters kare ilişkisi, Elektrik yükü, Elektroskop |
| FİZ.11.2.3 | Elektriksel alan, Faraday kafesi |  |
| FİZ.11.2.4 | Manyetik alan, Manyetik alan çizgileri, Dünya'nın manyetik alanı | Mıknatıs, Manyetik kutup, Pusula |
| FİZ.11.2.5 | Manyetik alan, Ørsted deneyi, Akım geçen düz telin manyetik alanı, Sağ el kuralı, Manyetik alan katsayısı | Doğru ve ters orantı, Elektrik akımı, Pusula |
| FİZ.11.2.6 | Manyetik alan, Sağ el kuralı, Manyetik alan katsayısı, Akım makarası, Sarım sayısı | Elektrik akımı |
| FİZ.11.2.7 | Akım makarası, Elektromıknatıs |  |
| FİZ.11.2.8 | Manyetik alan, Sağ el kuralı, Manyetik kuvvet, Manyetik alanda akım geçen tele etki eden kuvvet | Vektörel nicelik, Doğru ve ters orantı, Kuvvet, Elektrik akımı |
| FİZ.11.2.9 | Manyetik kuvvet, Elektrik motoru | Enerji dönüşümü |
| FİZ.11.2.10 | Manyetik alan, Manyetik akı |  |
| FİZ.11.2.11 | Sarım sayısı, Manyetik akı, İndüksiyon gerilimi (indüksiyon emk), İndüksiyon akımı, Faraday'ın indüksiyon yasası, Lenz Yasası, Elektrik jeneratörü | Enerji dönüşümü, Potansiyel fark (gerilim) |
| FİZ.11.2.12 | İndüksiyon gerilimi (indüksiyon emk), İndüksiyon akımı, Elektrik jeneratörü, Alternatif (değişken) akım, Alternatif akımda etkin değer | Periyot, Frekans |
| FİZ.11.2.13 | Sarım sayısı, Transformatör, Birincil ve ikincil sarım, Elektrik iletiminde enerji kaybı | Potansiyel fark (gerilim), Elektriksel direnç |

## Ünite 3: OPTİK

```mermaid
flowchart LR
  asal_eksen["Asal eksen"]
  aydinlanma["Aydınlanma"]
  ayna_tepe_noktasi["Tepe noktası (küresel ayna)"]
  cukur_ayna["Çukur ayna"]
  duzlem_ayna["Düzlem ayna"]
  egrilik_merkezi["Merkez (eğrilik merkezi)"]
  fiber_optik["Fiber optik"]
  gercek_derinlik["Gerçek derinlik"]
  goruntu["Görüntü (gerçek / sanal)"]
  gorunur_derinlik["Görünür derinlik"]
  gorus_alani["Görüş alanı"]
  iraksak_mercek["Iraksak (kalın kenarlı) mercek"]
  isik(["Işık ve ışın"])
  isik_akisi["Işık akısı"]
  isik_siddeti["Işık şiddeti"]
  kirilma(["Kırılma"])
  kirma_indisi["Ortamın ışığı kırma indisi"]
  kuresel_ayna["Küresel ayna"]
  kuresel_aynada_goruntu["Küresel aynada görüntü oluşumu"]
  mercek["Mercek"]
  mercekte_goruntu["Mercekte görüntü oluşumu"]
  odak_noktasi(["Odak noktası"])
  odak_uzakligi["Odak uzaklığı"]
  optik_merkez["Optik merkez"]
  ozel_isinlar["Özel ışınlar"]
  prizma["Prizma"]
  sapma_acisi["Sapma açısı"]
  sinir_acisi["Sınır açısı"]
  skaler_nicelik(["Skaler nicelik"])
  snell_yasasi["Snell Yasası"]
  tam_yansima["Tam yansıma"]
  tek_renkli_isik["Tek renkli ışık"]
  ters_kare_iliskisi(["Ters kare ilişkisi"])
  trigonometrik_oranlar(["Trigonometrik oranlar (sin, cos, tan)"])
  tumsek_ayna["Tümsek ayna"]
  yakinsak_mercek["Yakınsak (ince kenarlı) mercek"]
  yansima(["Yansıma"])
  yansima_yasalari["Yansıma yasaları"]
  odak_noktasi --> isik
  yansima --> isik
  kirilma --> isik
  isik_siddeti --> isik
  isik_akisi --> isik_siddeti
  isik_akisi --> skaler_nicelik
  aydinlanma --> isik_akisi
  aydinlanma --> ters_kare_iliskisi
  yansima_yasalari --> yansima
  duzlem_ayna --> yansima_yasalari
  duzlem_ayna --> goruntu
  goruntu --> isik
  gorus_alani -.->|parçası| duzlem_ayna
  kuresel_ayna --> yansima_yasalari
  cukur_ayna -.->|özel durum| kuresel_ayna
  tumsek_ayna -.->|özel durum| kuresel_ayna
  asal_eksen -.->|parçası| kuresel_ayna
  asal_eksen -.->|parçası| mercek
  ayna_tepe_noktasi -.->|parçası| kuresel_ayna
  egrilik_merkezi -.->|parçası| kuresel_ayna
  odak_noktasi -.->|parçası| kuresel_ayna
  odak_noktasi -.->|parçası| mercek
  odak_uzakligi --> odak_noktasi
  ozel_isinlar --> odak_noktasi
  ozel_isinlar --> asal_eksen
  kuresel_aynada_goruntu --> kuresel_ayna
  kuresel_aynada_goruntu --> ozel_isinlar
  kuresel_aynada_goruntu --> goruntu
  kirma_indisi --> kirilma
  snell_yasasi --> kirma_indisi
  snell_yasasi --> trigonometrik_oranlar
  sinir_acisi --> snell_yasasi
  tam_yansima --> sinir_acisi
  gorunur_derinlik --> kirilma
  gorunur_derinlik --> kirma_indisi
  fiber_optik --> tam_yansima
  prizma --> snell_yasasi
  prizma --> tek_renkli_isik
  sapma_acisi --> kirilma
  sapma_acisi -.->|parçası| prizma
  mercek --> kirilma
  yakinsak_mercek -.->|özel durum| mercek
  iraksak_mercek -.->|özel durum| mercek
  optik_merkez -.->|parçası| mercek
  mercekte_goruntu --> mercek
  mercekte_goruntu --> ozel_isinlar
  mercekte_goruntu --> goruntu
```

Yuvarlak kutu = önceki sınıflardan gelen ön koşul kavramı.

| Öğrenme çıktısı | 11. sınıf kavramları | Ön koşul kavramları |
|---|---|---|
| FİZ.11.3.1 | Işık şiddeti, Işık akısı, Aydınlanma | Skaler nicelik, Ters kare ilişkisi, Işık ve ışın |
| FİZ.11.3.2 | Yansıma yasaları, Düzlem ayna, Görüntü (gerçek / sanal), Görüş alanı | Yansıma |
| FİZ.11.3.3 | Yansıma yasaları, Küresel ayna, Çukur ayna, Tümsek ayna, Asal eksen, Tepe noktası (küresel ayna), Merkez (eğrilik merkezi), Odak uzaklığı, Özel ışınlar | Işık ve ışın, Yansıma, Odak noktası |
| FİZ.11.3.4 | Görüntü (gerçek / sanal), Küresel ayna, Çukur ayna, Tümsek ayna, Özel ışınlar, Küresel aynada görüntü oluşumu |  |
| FİZ.11.3.5 | Ortamın ışığı kırma indisi, Snell Yasası, Sınır açısı, Tam yansıma, Sapma açısı | Trigonometrik oranlar (sin, cos, tan), Kırılma |
| FİZ.11.3.6 | Ortamın ışığı kırma indisi, Görünür derinlik, Gerçek derinlik | Kırılma |
| FİZ.11.3.7 | Sınır açısı, Tam yansıma, Fiber optik |  |
| FİZ.11.3.8 | Ortamın ışığı kırma indisi, Snell Yasası, Tam yansıma, Prizma, Tek renkli ışık, Sapma açısı | Kırılma |
| FİZ.11.3.9 | Asal eksen, Odak uzaklığı, Özel ışınlar, Mercek, Yakınsak (ince kenarlı) mercek, Iraksak (kalın kenarlı) mercek, Optik merkez | Işık ve ışın, Kırılma, Odak noktası |
| FİZ.11.3.10 | Görüntü (gerçek / sanal), Özel ışınlar, Mercek, Yakınsak (ince kenarlı) mercek, Iraksak (kalın kenarlı) mercek, Mercekte görüntü oluşumu |  |
