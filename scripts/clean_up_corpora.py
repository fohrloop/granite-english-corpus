#!/usr/bin/env python

from pathlib import Path

root = Path(__file__).parent.parent


TYPABLE_CHARS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
TYPABLE_CHARS += r""",.!?;:_'"^~#%&/\()[]{}<>=+-*`@$€|"""
TYPABLE_CHARS += " \t\n"
ALLOWED_CHARACTERS = set(TYPABLE_CHARS)
ALLOWED_CHARACTERS_FINNISH = ALLOWED_CHARACTERS | set("äöÄÖ")

replacements_finnish = {
    "¹": "1",
    "²": "2",
    "³": "3",
    "½": "1/2",
    "¾": "3/4",
    "Á": "A",
    "Ã": "A",
    "Å": "A",
    "Æ": "AE",
    "É": "E",
    "Ì": "I",
    "Ó": "O",
    "×": "x",
    "Ø": "Ö",
    "ß": "ss",
    "à": "a",
    "á": "a",
    "â": "a",
    "ã": "a",
    "å": "a",
    "æ": "ae",
    "ç": "c",
    "è": "e",
    "é": "e",
    "ê": "e",
    "ë": "e",
    "ì": "i",
    "í": "i",
    "î": "i",
    "ï": "i",
    "ð": "d",
    "ñ": "n",
    "ò": "o",
    "ó": "o",
    "ô": "o",
    "õ": "o",
    "ø": "ö",
    "ú": "u",
    "û": "u",
    "ü": "u",
    "ý": "y",
    "ā": "a",
    "ă": "a",
    "ć": "c",
    "č": "c",
    "ī": "i",
    "ł": "l",
    "ŋ": "NG",
    "ō": "o",
    "Š": "S",
    "š": "s",
    "ū": "u",
    "Ž": "Z",
    "ž": "z",
    "α": "a",
    "β": "b",
    "ε": "e",
    "η": "e",
    "ι": "i",
    "κ": "k",
    "λ": "l",
    "μ": "m",
    "ν": "n",
    "ο": "o",
    "π": "p",
    "ρ": "r",
    "ς": "s",
    "σ": "s",
    "τ": "t",
    "υ": "u",
    "А": "A",
    "Щ": "Shch",
    "а": "a",
    "в": "v",
    "д": "d",
    "е": "e",
    "и": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "р": "r",
    "с": "s",
    "т": "t",
    "‒": "-",
    "–": "-",
    "—": "--",
    "―": "--",
    "−": "-",
    "─": "-",
    "‘": "'",
    "’": "'",
    "´": "'",
    "“": '"',
    "”": '"',
    "«": '"',
    "»": '"',
    "•": "*",
    "·": "*",
    "…": "...",
    "™": "(tm)",
    "­®": "(r)",
}
replacements = replacements_finnish.copy()
replacements["Ø"] = "O"
replacements["ø"] = "o"


def process_file(input_path, output_path, replacements, allowed_chars):
    chunk_size = 50 * 1024 * 1024  # 50 MB chunk size
    with open(input_path, "r", encoding="utf-8") as infile, open(
        output_path, "w", encoding="utf-8"
    ) as outfile:
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break  # End of file

            for old_str, new_str in replacements.items():
                chunk = chunk.replace(old_str, new_str)
            chunk = "".join(char for char in chunk if char in allowed_chars)
            outfile.write(chunk)


def cleanup_folder(
    folder: Path,
    folder_out: Path,
    allowed_characters: set[str],
    used_replacements: dict[str, str],
):
    folder_out.mkdir(exist_ok=True)
    for file in folder.glob("*.txt"):
        file_out = folder_out / file.name
        print(f"Processing {file} -> {file_out}")
        process_file(file, file_out, used_replacements, allowed_characters)


if __name__ == "__main__":
    import time

    start = time.time()
    for lang in ("english", "code", "finnish"):
        langfolder = root / lang
        allowed_characters = (
            ALLOWED_CHARACTERS_FINNISH if lang == "finnish" else ALLOWED_CHARACTERS
        )
        used_replacements = replacements_finnish if lang == "finnish" else replacements
        cleanup_folder(
            langfolder / "corpus-not-clean",
            langfolder / "corpus-clean",
            allowed_characters,
            used_replacements,
        )
    print("Done in", time.time() - start, "seconds")
