"""Example — build a POS-tag frequency profile of a paragraph.

Run::

    python examples/05_tag_profile.py
"""

from collections import Counter

from brill_postaggers import BrillPostagger


def main() -> None:
    paragraph = (
        "Os antigos navegadores partiram do porto ao amanhecer. "
        "O vento forte empurrava as velas brancas para sul. "
        "Depois de muitos dias no mar, avistaram finalmente a costa."
    )
    tagger = BrillPostagger.from_pretrained("pt")

    counts: Counter = Counter()
    for sentence in paragraph.split(". "):
        counts.update(tag for _, tag in tagger.tag(sentence))

    print("tag profile (most common):")
    for tag, n in counts.most_common():
        print(f"  {tag:<6} {n}")


if __name__ == "__main__":
    main()
