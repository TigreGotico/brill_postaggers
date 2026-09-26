"""Example — filter tagged tokens by Universal Dependencies POS class.

Run::

    python examples/04_filter_by_class.py
"""

from brill_postaggers import BrillPostagger


def main() -> None:
    tagger = BrillPostagger.from_pretrained("pt")
    text = "o velho navegador português descobriu novas terras"
    tagged = tagger.tag(text)

    nouns = [w for w, tag in tagged if tag == "NOUN"]
    adjectives = [w for w, tag in tagged if tag == "ADJ"]
    verbs = [w for w, tag in tagged if tag == "VERB"]

    print("sentence  :", text)
    print("nouns     :", nouns)
    print("adjectives:", adjectives)
    print("verbs     :", verbs)


if __name__ == "__main__":
    main()
