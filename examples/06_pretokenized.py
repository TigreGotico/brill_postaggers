"""Example — tag your own tokens, bypassing the built-in tokenizer.

Run::

    python examples/06_pretokenized.py
"""

from brill_postaggers import BrillPostagger


def main() -> None:
    tagger = BrillPostagger.from_pretrained("en")

    # Already-tokenized input: feed the wrapped NLTK model directly.
    tokens = ["state", "-", "of", "-", "the", "-", "art", "design"]
    print("pre-tokenized:", tagger.tagger.tag(tokens))

    # Compare with the convenience path that tokenizes for you.
    print("via tag()   :", tagger.tag("state-of-the-art design"))


if __name__ == "__main__":
    main()
