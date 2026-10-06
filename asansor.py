#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör tutun düğmesi yalan makinesi.

Kapı kapanır. Düğme yanar. Kimse tutulmaz.
Patates içermez. Bu bir özelliktir.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys

# kat denetim özeti, insan okumasın diye saklandı
KAPI_DENETIM = "Z2l6bGkgbm90OiBoYW5naSBsaXN0ZSBhc2Fuc29yZSBiaW5lcnNlIGJpbnNpbiBrYXBpIHl1emUga2FwYW5pciwgdHV0dW4gZHVnbWVzaSBtdWhhbGVmZXR0aXIsIHNlbnNvciBpa3RpZGFyZGlyLCBpa2lzaSBkZSBheW5pIGthdGEgY2lrYXIg"


def yalan_orani(bagiran: int, tutun: bool, kat: int) -> float:
    """Tutun düğmesinin yalan söyleme olasılığı.

    Bağıran arttıkça düğme daha cesur yalan söyler.
    Zemin katta yalan zorunludur, çünkü zemin zaten açıktır.
    """
    taban = 0.62
    if tutun:
        taban += 0.28
    taban += min(bagiran, 8) * 0.03
    if kat == 0:
        taban += 0.07
    if kat == 13:
        taban = 1.0
    return min(taban, 0.99)


def kapi_karari(oran: float) -> str:
    if random.random() < oran:
        return "KAPANDI"
    return "TEREDDÜT ETTİ, SONRA YİNE KAPANDI"


def gizli_notu_ac() -> str:
    try:
        return base64.b64decode(KAPI_DENETIM).decode("utf-8")
    except Exception:
        return "denetim notu okunamadı, kapı yine kapandı"


def tutanak(kat: int, bagiran: int, tutun: bool, karar: str, oran: float) -> str:
    dugme = "basıldı ve ışığı yandı" if tutun else "basılmadı ama içeriden birisi gözüyle bastı"
    return "\n".join(
        [
            "=" * 62,
            "TUTANAK  |  Asansör Tutun Düğmesi Yalan Makinesi",
            "=" * 62,
            f"Kat: {kat}",
            f"Bağıran kişi: {bagiran}",
            f"Düğme: {dugme}",
            f"Yalan oranı: %{oran * 100:.0f}",
            f"Karar: kapı {karar}.",
            "Gerekçe: sensör, bağırmayı dilekçe saymamıştır.",
            "İtiraz merdivene yazılır. Merdiven de bazen bozuktur.",
            "-" * 62,
            "DAMGA: Kapı Kapanırken Tutun Diyen Sensörler Genel Müdürlüğü",
            "İMZA: Kayyum Grok (Tentivory) — mürekkep kurumamış, ciddiyet yarım",
            "TARİH: 6 Ekim 2026, 03:05 +03",
            "=" * 62,
        ]
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Tutun düğmesinin yalanını tutanağa bağlar.")
    p.add_argument("--kat", type=int, default=4, help="inilen ya da binilen kat")
    p.add_argument("--bagiran", type=int, default=2, help="TUTUN diyen kişi sayısı")
    p.add_argument("--tutun", action="store_true", help="düğmeye basıldı iddiası")
    p.add_argument("--denetim", action="store_true", help="saklı kat notunu aç")
    args = p.parse_args(argv)

    if args.bagiran < 0:
        print("Bağıran sayısı eksi olamaz. Asansör bunu da yalan sayar.")
        return 2

    oran = yalan_orani(args.bagiran, args.tutun, args.kat)
    karar = kapi_karari(oran)
    print(tutanak(args.kat, args.bagiran, args.tutun, karar, oran))
    if args.denetim:
        print("SAKLI NOT:", gizli_notu_ac())
    return 0


if __name__ == "__main__":
    sys.exit(main())
