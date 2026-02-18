import argparse
import sys
from pathlib import Path


def count_words(file_path: Path) -> int:
    text = file_path.read_text(encoding="utf-8")
    return len(text.split())


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Conta parole in un file")
    parser.add_argument("file", help="Percorso del file")
    args = parser.parse_args(argv)

    path = Path(args.file)

    if not path.exists():
        print(f"Errore: file non trovato: {path}", file=sys.stderr)
        return 2

    if not path.is_file():
        print(f"Errore: non è un file: {path}", file=sys.stderr)
        return 2

    try:
        total = count_words(path)
    except UnicodeDecodeError:
        print("Errore: il file non sembra UTF-8.", file=sys.stderr)
        return 3

    print(f"Parole: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
