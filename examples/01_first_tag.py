"""Example — load a Portuguese tagger and tag a sentence.

Run::

    python examples/01_first_tag.py
"""

from brill_postaggers import BrillPostagger


def main() -> None:
    tagger = BrillPostagger.from_pretrained("pt")
    tagged = tagger.tag("como está o tempo lá fora?")
    for word, tag in tagged:
        print(f"{word:<8} {tag}")


if __name__ == "__main__":
    main()
