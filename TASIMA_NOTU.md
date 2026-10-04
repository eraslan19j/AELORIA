# AELORIA — DEPOYA TAŞIMA NOTU

## Durum: Neden son değişiklikler GitHub'da görünmüyor?

Bu çalışma oturumunun GitHub bağlantısı, oturumun pull request'i kapatıldığı için
kesildi. Bu oturumdan yeni commit **gönderilemiyor** (push komutu platform
tarafından engelleniyor). Yazılan her şey yerel repoda commit'li ve eksiksiz duruyor.

**GitHub'da şu an bulunan son commit:** `a7ccd87` — "Bölüm 5 (Borç)".
(Bu ana kadar başarıyla gönderilenler: `f2b99c4` Önsöz + Bölüm 1-3, `ce4726f`
ad sistemi + Bölüm 4, `a7ccd87` Bölüm 5.)

**GitHub'da OLMAYAN, yerelde bekleyen üç commit:**

| Commit | İçerik |
|---|---|
| `37d2866` | 3. ad revizyonu (Vareyn / Sorelis / Karnath / Ferron, Veyra ve yedi kol), `durum/EVREN.md`, **Bölüm 6 — Boş Beşik** |
| `ff881ab` | Kalan eski ad referanslarının temizliği, `arac/birlestir.py`, `AELORIA_tam_metin.md` |
| `a35546d` | `README.md` tam sürüm, durum dosyası sayıları |

Ayrıca bu üç commit'ten **önceki** hâlde de düzeltilmiş olanlar var: Bölüm 4 ve
Bölüm 5'in içindeki adlar (Gümüşçat → Zeravan vb.) yalnız `37d2866` ile
GitHub'a gidecek.

---

## Çözüm: yeni bir oturumda taşıma (2 dakika)

Bu klasörde iki taşıma dosyası var:

- **`AELORIA.bundle`** — bütün geçmişi içeren tek dosya (kesin çözüm).
- **`AELORIA_eklemeler.patch`** — yalnız son üç commit'in yaması (GitHub'daki
  `a7ccd87` üzerine uygulanır).

### Yol A — Bundle ile (önerilen)

Yeni bir AELORIA oturumu açın ve şunu söyleyin:

> AELORIA devam. `AELORIA.bundle` dosyasını depoya uygula ve kendi arena dalına
> commit'leyip push et; sonra `durum/DURUM_DOSYASI.md`'yi oku ve Bölüm 7'den devam et.

Yeni oturumdaki ajan şu komutları çalıştırır:

```bash
git bundle verify AELORIA.bundle
git fetch AELORIA.bundle "arena/01a106f3-aeloria:refs/heads/aeloria-tasima"
git merge --ff-only aeloria-tasima     # kendi arena dalında
git push origin HEAD                    # kendi oturum dalına
```

Sonra yeni dal için bir pull request açılır; ana dala birleştirilir.

### Yol B — Yama ile

```bash
git fetch origin
git checkout -b aeloria-tasima origin/arena/01a106f3-aeloria   # a7ccd87'de
git am AELORIA_eklemeler.patch
git push origin aeloria-tasima
```

### Yol C — Dosyaları elle kopyalama

Bütün metin dosyaları düz Markdown. `roman/`, `durum/` ve `README.md` dosyalarını
kopyalayıp yeni oturumda commit'lemek de yeterlidir; içerik birebir aynıdır.

---

## İçeriğin doğruluğunu kontrol etme (taşımadan sonra)

Metin dosyalarında şu satır geçmeli; eski adlar geçmemeli:

- Geçmeli: `Zeravan, Taşkıran, Miren, Semum, Kemik ve Delisu`
- Geçmemeli: `Gümüşçat`, `Taşyatak`, `Akçasu`, `Acısu`, `Kemiksu`,
  `Kapankaya`, `Akçaliman`, `Kırkburç`, `Tuzsaz`, `Kadran`, `Elvun`,
  `Urdran`, `Melvan`, `Varyn`, `Sorel`, `Karn`, `Ferro`

```bash
grep -rnwE "Gümüşçat|Taşyatak|Akçasu|Acısu|Kemiksu|Kapankaya|Akçaliman|Kırkburç|Tuzsaz|Kadran|Elvun|Urdran|Melvan" roman/ durum/ README.md | grep -v AD_BILIMI.md
# çıktı boş olmalı
```

---

## Bu depodaki güncel içerik özeti

| Dosya | Ne var |
|---|---|
| `roman/00…06` (7 dosya) | Önsöz + Bölüm 1-6, toplam **22.694 kelime** |
| `AELORIA_tam_metin.md` | Hepsini tek dosyada birleştirilmiş hâlde (22.825 kelime, başlık notlarıyla) |
| `durum/DURUM_DOSYASI.md` | Kanon, isim defteri, açık tohumlar, bölüm planı, sıradaki iş: Bölüm 7 |
| `durum/AD_BILIMI.md` | Ad kuralları ve üç taslağın tam değişiklik kaydı |
| `durum/EVREN.md` | Ejderha, kan büyüsü, kadim güçler, kitap ailesi, tarih şeridi |
| `arac/birlestir.py` | `python3 arac/birlestir.py` → birleşik metni yeniler |
