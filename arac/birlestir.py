# -*- coding: utf-8 -*-
"""Bölüm dosyalarını okuma sırasına göre tek dosyada birleştirir.
Kullanım: python3 arac/birlestir.py"""
import os

SIRA = [
    "00_onsoz_buzun_altinda.md",
    "01_kirk_yedi.md",
    "02_kursun.md",
    "03_sol_el.md",
    "04_rahip_yazisi.md",
    "05_borc.md",
    "06_bos_besik.md",
]

BASLIK = (
    "# AELORIA — UZUN ÇÖZÜLME\n\n"
    "*(Bu dosya `arac/birlestir.py` ile üretilir; elle düzenlenmez. "
    "Kaynak dosyalar `roman/` klasöründedir.)*\n\n---\n"
)

SON_NOT = (
    "\n\n---\n\n## SON NOT\n\n"
    "*Bu noktaya kadar toplam {kelime} kelime yazıldı. Roman devam ediyor: "
    "Perde 1 (Bölüm 7-10), Perde 2 (11-25), Perde 3 (26-40) ve sonsöz.*\n"
)


def main():
    parcalar = [BASLIK]
    toplam = 0
    for ad in SIRA:
        yol = os.path.join("roman", ad)
        if not os.path.exists(yol):
            continue
        metin = open(yol, encoding="utf-8").read().strip()
        toplam += len(metin.split())
        parcalar.append("\n\n---\n\n")
        parcalar.append(metin)
        parcalar.append("\n")
    parcalar.append(SON_NOT.format(kelime="{:,}".format(toplam).replace(",", ".")))
    open("AELORIA_tam_metin.md", "w", encoding="utf-8").write("".join(parcalar))
    print("yazıldı: AELORIA_tam_metin.md —", toplam, "kelime")


if __name__ == "__main__":
    main()
