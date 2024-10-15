#!/usr/bin/env python
import json
from pathlib import Path

infile = Path(__file__).parent / "raw" / "corpus-webis-tldr-17.json"
outfile = Path(__file__).parent / "corpus-not-clean" / "tldr17.txt"
outfile.parent.mkdir(exist_ok=True)


def process_file():
    with open(infile, "r") as indata, open(outfile, "w") as out:
        for line in indata:
            data = json.loads(line)
            content = data["content"].strip()
            print(content, file=out, end=" ")


if __name__ == "__main__":
    process_file()
