#!/usr/bin/env python

from pathlib import Path

folder = Path(__file__).parent / "raw" / "leipzig"
outfile = Path(__file__).parent / "corpus-not-clean" / "combined-leipzig.txt"
outfile.parent.mkdir(exist_ok=True)


def process_files():
    with open(outfile, "w") as out:
        for file in folder.glob("*.txt"):
            process_file(file, out)


def process_file(filename: Path, outfile):
    print(f"Processing {filename}")
    with open(filename, "r") as file:
        for line in file:
            linedata = line.split("\t", maxsplit=1)[-1]
            print(linedata, file=outfile, end="")


if __name__ == "__main__":
    process_files()
