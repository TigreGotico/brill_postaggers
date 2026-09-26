"""Example — enumerate supported languages and tag a sample in each.

Run::

    python examples/02_languages.py
"""

from brill_postaggers import BrillPostagger

SAMPLES = {
    "pt": "o gato preto dorme no sofá",
    "es": "el rápido zorro marrón salta sobre el perro",
    "fr": "le chat noir dort sur le canapé",
    "en": "the quick brown fox jumps over the lazy dog",
}


def main() -> None:
    print("supported codes:", sorted(BrillPostagger.MODELS))
    for lang, text in SAMPLES.items():
        tagger = BrillPostagger.from_pretrained(lang)
        tagged = tagger.tag(text)
        print(f"\n[{lang}] {text}")
        print(" ", tagged)


if __name__ == "__main__":
    main()
