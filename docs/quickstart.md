# Quickstart: zero to tagged

`brill_postaggers` does part-of-speech tagging for 11 languages, using
pre-trained Brill models behind one small class. You give it a sentence, and
it gives you back `(word, tag)` tuples, using the
[Universal Dependencies](https://universaldependencies.org/u/pos/) tagset.

## 1. Install

```bash
pip install brill_postagger        # PyPI dist name
```

The import name is plural: `brill_postaggers`. The only runtime dependency is
`nltk`. The 11 models travel inside the wheel as package data, so you do not
need a separate download of model files.

## 2. The one thing to understand

There is a single public class, `BrillPostagger`. You almost never construct
it by path. Instead, call `from_pretrained(lang)`, which loads the bundled
model for that language code:

```python
from brill_postaggers import BrillPostagger

tagger = BrillPostagger.from_pretrained("pt")
print(tagger.tag("como está o tempo lá fora?"))
# [('como', 'SCONJ'), ('está', 'AUX'), ('o', 'DET'), ('tempo', 'NOUN'),
#  ('lá', 'ADV'), ('fora', 'ADV'), ('?', 'PUNCT')]
```

`tag()` word-tokenizes the sentence with NLTK first, then tags each token. The
return value is a list of `(token, tag)` tuples in sentence order, with
punctuation included.

## 3. First call, end to end

```python
from brill_postaggers import BrillPostagger

tagger = BrillPostagger.from_pretrained("en")
for word, tag in tagger.tag("the quick brown fox jumps over the lazy dog"):
    print(f"{word:<8} {tag}")
```

The first time you construct any tagger, NLTK fetches its `punkt_tab`
tokenizer tables (`nltk.download('punkt_tab')`). This needs network access
once. After that, it is cached under `~/nltk_data`.

## 4. Pick a language

Language codes are the keys of `BrillPostagger.MODELS`:

```python
from brill_postaggers import BrillPostagger

print(sorted(BrillPostagger.MODELS))
# ['ca', 'da', 'de', 'en', 'es', 'eu', 'fr', 'gl', 'it', 'nl', 'pt']
```

`from_pretrained` lowercases the code and strips a region suffix after a
hyphen, so `"PT-BR"` and `"pt"` both resolve to the Portuguese model.
`"pt_PT"` (underscore) is not split and raises `KeyError`. See
[advanced.md](advanced.md) for how to guard against that.

---
[Home](../README.md) · [API reference →](api.md)
