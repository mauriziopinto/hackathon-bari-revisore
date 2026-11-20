"""Apre una busta con la password che Maurizio condivide all'ora stabilita.

Uso, dalla cartella del repository, nel terminale:
    python3 strumenti/apri_busta.py 1        alle 14:00, i risultati attesi sui documenti della giornata
    python3 strumenti/apri_busta.py 2        alle 15:30, i documenti nuovi
    python3 strumenti/apri_busta.py 3        alle 16:00, i risultati attesi sui documenti nuovi
    python3 strumenti/apri_busta.py aiuto    solo se ve lo dicono Maurizio o Andrea

Lo script chiede la password e scrive il contenuto in buste/busta_<numero>/ (oppure buste/aiuto/).
Lanciatelo voi nel terminale, non chiedete a Kiro di farlo: la password la scrivete voi.
"""
import getpass
import shutil
import sys
import zipfile
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
BUSTE = {"1": "busta_1", "2": "busta_2", "3": "busta_3", "aiuto": "aiuto"}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in BUSTE:
        sys.exit("Uso: python3 strumenti/apri_busta.py 1 | 2 | 3 | aiuto")
    nome = BUSTE[sys.argv[1]]
    archivio = RADICE / "buste" / f"{nome}.zip"
    if not archivio.exists():
        sys.exit(f"Non trovo {archivio.relative_to(RADICE)}")
    destinazione = RADICE / "buste" / nome
    if destinazione.exists():
        print(f"La busta è già aperta: il contenuto è in {destinazione.relative_to(RADICE)}/")
        return
    password = getpass.getpass(f"Password della busta {sys.argv[1]}: ").strip().encode("utf-8")
    with zipfile.ZipFile(archivio) as z:
        try:
            z.extractall(RADICE / "buste", pwd=password)
        except RuntimeError:
            shutil.rmtree(destinazione, ignore_errors=True)
            sys.exit("Password sbagliata. Controllatela e riprovate.")
    print(f"Busta aperta. Il contenuto è in {destinazione.relative_to(RADICE)}/:")
    for f in sorted(destinazione.rglob("*")):
        if f.is_file():
            print(f"  {f.relative_to(RADICE)}")
    if nome == "aiuto":
        print("Copiate lo script in strumenti/ con questo comando, poi chiedete a Kiro di usarlo per leggere i file Word:")
        print("  cp buste/aiuto/estrai_testo.py strumenti/")


if __name__ == "__main__":
    main()
