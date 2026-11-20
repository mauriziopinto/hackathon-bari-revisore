"""Crea lo zip del lavoro del gruppo, da scaricare prima che l'ambiente si chiuda.

Uso, dalla cartella del repository:
    python3 strumenti/consegna.py 2

Scrive consegna/gruppo-<n>.zip con tutto il repository tranne le buste, le cache di Python e la cartella .git.
Poi scaricate il file dall'esplorazione file dell'IDE: tasto destro su consegna/gruppo-<n>.zip, Download.
"""
import sys
import zipfile
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
ESCLUSE = {"buste", "consegna", "__pycache__", ".git", ".pytest_cache"}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"1", "2", "3", "4"}:
        sys.exit("Uso: python3 strumenti/consegna.py <numero del gruppo, da 1 a 4>")
    uscita = RADICE / "consegna" / f"gruppo-{sys.argv[1]}.zip"
    uscita.parent.mkdir(exist_ok=True)
    n = 0
    with zipfile.ZipFile(uscita, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(RADICE.rglob("*")):
            relativo = f.relative_to(RADICE)
            if f.is_file() and not ESCLUSE & set(relativo.parts) and f.suffix != ".pyc":
                z.write(f, Path(f"gruppo-{sys.argv[1]}") / relativo)
                n += 1
    print(f"Creato {uscita.relative_to(RADICE)}: {n} file, {uscita.stat().st_size // 1024} KB.")
    print("Scaricatelo dall'esplorazione file dell'IDE (tasto destro, Download) e controllate di averlo sul vostro computer.")


if __name__ == "__main__":
    main()
