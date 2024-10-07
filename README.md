# Granite English Corpus

This repository contains the character-based ngrams (unigrams, bigrams, trigrams) used for the development of the [Granite Layout](https://github.com/fohrloop/granite-layout) which are compatible with the [Keyboard Layout Optimizer](https://github.com/dariogoetz/keyboard_layout_optimizer) by Dario Götz. The corpus was cleaned from untypical characters before creating the ngrams (see below for details).

The used  corpus is a mixture of two dataset with following weights

- 40% Leipzig (10% News, 10% Web-public com, 10% Web-public UK & 10% Wikipedia)
- 60% Reddit TLDR17

Other related repos: [granite-code-ngrams](https://github.com/fohrloop/granite-code-ngrams) and [granite-finnish-ngrams](https://github.com/fohrloop/granite-finnish-ngrams).

# How the corpus was created

## The Granite Leipzig dataset
The Granite English corpus (`ngrams/english`) is a mixture of following from the [Leipzig Corpora Collection](https://wortschatz.uni-leipzig.de/en/download)[^leipzig]:

- News 2023 1M dataset (`eng_news_2023_1M.tar.gz`)
- Web-public com 1M dataset (`eng-com_web-public_2018_1M.tar.gz`)
- Web public United Kingdow 1M dataset (`eng-uk_web-public_2018_1M.tar.gz`)
- Wikipedia 2016 1M dataset (`eng_wikipedia_2016_1M.tar.gz`)

The Granite Eglish Leipzig dataset uses only the `*-sentences.txt` file from each, containing 4M English sentences in total. The sentence numbering and the tab was removed, and all the data from the four `*-sentences.txt` was merged into one. After cleaning the data, the `ngrams` binary from the [Keyboard Layout Optimizer](https://github.com/dariogoetz/keyboard_layout_optimizer) was used to form the Granite Leipzig ngrams (`ngrams/leipzig`).


<details>
<summary>Script used to create `combined-leipzig.txt`</summary>

```python
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
```

</details>

## The Granite Reddit TLDR17 dataset

IThe `tldr17` dataset was created from the [Webis-TLDR-17 Corpus](https://zenodo.org/records/1043504)[^tldr17]. The corpus was created by extracting the "content" field from each of the rows, stripping whitespace from the beginning and end of each, adding single space between contents, and combining all of that into a single 5.6GB text file (`tldr17.txt`).


<details>
<summary>Script used to create `tldr17.txt`</summary>

```python
import json
from pathlib import Path

infile = Path(__file__).parent / "raw" / "corpus-webis-tldr-17.json"
outfile = Path(__file__).parent / "corpus-not-clean"  / "tldr17.txt"
outfile.parent.mkdir(exist_ok=True)


def process_file():
    with open(infile, "r") as indata, open(outfile, "w") as out:
        for line in indata:
            data = json.loads(line)
            content = data["content"].strip()
            print(content, file=out, end=" ")


if __name__ == "__main__":
    process_file()
```

</details>

## The Granite English dataset

The Granite English ngrams were created from the  `leipzig` and the `tldr17` by first normalizing the ngram files using the `normalize.py` script from the [Keyboard Layout Optimizer](https://github.com/dariogoetz/keyboard_layout_optimizer)

```
python ./scripts/ngrams/normalize.py /somepath/ngrams/<corpusname>
```

and then merging the ngram files with weighting using the `ngram_merge` binary from the Keyboard Layout Optimizer:

```
❯ ./target/release/ngram_merge english/ngrams/english english/ngrams/leipzig:0.4 english/ngrams/tldr17:0.6
```

The used version of the Keyboard Layout Optimizer is specified by commit [f93bd06](https://github.com/dariogoetz/keyboard_layout_optimizer/commit/f93bd06820790ae746fbe66445bdf4427260fd31).

## Cleaning the datasets

Before creating the ngrams, only following ASCII alphanumerics (62 characters):
```
qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890
```

and following punctuation and special characters (33 characters):

```
,.!?;:_'"^~#%&/\()[]{}<>=+-*`@$€|
```

were accepted to the ngrams. The conversion script below was used to either remove or replace characters which belong to the following set:

```
¡£¤§«­®°²³´¶·¹»½¾¿ÁÃÅÆÉÌÓ×ØßàáâãåæçèéêëìíîïðñòóôõøúûüýāăćčīłŋōŠšūŽžə͜͡αβεηικλμνοπρςστυАЩавдеиклмнорстأابةتخدرسعقلمنهويนรลอาเ​‒–—―‘’“”•…₹™→−─│┆┌┐└┘┬┴═╞╡╪♪♫月语𞤫
```


<details>
<summary>Corpora cleanup script</summary>

This is the cleanup script which was used to clean the English, Code and Finnish corpora. 

```python
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
```
</details>



[^leipzig]: D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages. In: Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012
[^tldr17]: Syed, S., Voelske, M., Potthast, M., & Stein, B. (2017). Webis-TLDR-17 Corpus [Data set]. EMNLP 2017 Workshop on New Frontiers in Summarization (EMNLP 2017). Zenodo. https://doi.org/10.5281/zenodo.1043504