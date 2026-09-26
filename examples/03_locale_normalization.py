"""Example — region-suffixed locales resolve to the base language model.

Run::

    python examples/03_locale_normalization.py
"""

from brill_postaggers import BrillPostagger


def main() -> None:
    text = "bom dia, como vai você?"
    for locale in ("pt", "PT", "pt-BR", "PT-PT"):
        tagger = BrillPostagger.from_pretrained(locale)
        tagged = tagger.tag(text)
        print(f"{locale:<6} -> {tagged}")


if __name__ == "__main__":
    main()
