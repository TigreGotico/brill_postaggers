# Advanced: recipes and gotchas

## Guard an unknown language

`from_pretrained` raises `KeyError` for a code it does not ship. Check against
`MODELS` before loading, or catch the error:

```python
from brill_postaggers import BrillPostagger

def safe_tagger(lang: str):
    code = lang.split("-")[0].lower()
    if code not in BrillPostagger.MODELS:
        return None
    return BrillPostagger.from_pretrained(code)

print(safe_tagger("pt-PT") is not None)   # True
print(safe_tagger("ja"))                  # None
```

## Load each language once

Constructing a tagger unpickles a model and calls `nltk.download('punkt_tab')`.
Build one tagger per language and keep it. A small cache avoids repeat work
when you tag text in several languages:

```python
from functools import lru_cache
from brill_postaggers import BrillPostagger

@lru_cache(maxsize=None)
def tagger_for(lang: str) -> BrillPostagger:
    return BrillPostagger.from_pretrained(lang)

tagger_for("pt").tag("bom dia")
tagger_for("pt").tag("boa noite")   # same instance, no reload
```

## Tag many sentences

`tag()` works one sentence at a time. Wrap it to process a batch:

```python
from brill_postaggers import BrillPostagger

tagger = BrillPostagger.from_pretrained("en")
sentences = ["I like cats.", "Dogs run fast."]
tagged = [tagger.tag(s) for s in sentences]
for s in tagged:
    print(s)
```

## Pull out only the words of a given class

The return value is plain tuples, so filtering is ordinary Python. Extract
the nouns, or the surface forms of any UD class:

```python
from brill_postaggers import BrillPostagger

tagger = BrillPostagger.from_pretrained("pt")
tagged = tagger.tag("o gato preto dorme no sofá")
nouns = [w for w, tag in tagged if tag == "NOUN"]
print(nouns)   # ['gato', 'sofá']
```

## Skip tokenization when you already have tokens

`tag()` runs `nltk.word_tokenize` for you. If your pipeline already produced
tokens, call the wrapped NLTK model directly through the `.tagger` attribute
and keep your own tokenization:

```python
from brill_postaggers import BrillPostagger

tagger = BrillPostagger.from_pretrained("en")
tokens = ["state", "-", "of", "-", "the", "-", "art"]
print(tagger.tagger.tag(tokens))
```

## Build a frequency profile

Counting tags is a one-liner with `collections.Counter`. This gives a cheap
syntactic fingerprint of a text:

```python
from collections import Counter
from brill_postaggers import BrillPostagger

tagger = BrillPostagger.from_pretrained("es")
text = "el rápido zorro marrón salta sobre el perro perezoso"
counts = Counter(tag for _, tag in tagger.tag(text))
print(counts.most_common(3))
```

## Gotchas

- The PyPI dist name is `brill_postagger` (singular). The import name is
  `brill_postaggers` (plural).
- The first construction needs network access for `nltk.download('punkt_tab')`.
  After it caches to `~/nltk_data`, offline use works.
- `from_pretrained` only splits on `-`, so `"pt_PT"` (underscore) is not
  normalized and raises `KeyError`. Pass the bare code or a `-` separated locale.
- Tags follow the UD scheme, not the Penn Treebank scheme. Expect `NOUN`,
  not `NN`, and `PUNCT` for punctuation.
- Accuracy reflects the source UD treebank for each language. Out-of-domain
  or heavily code-switched text degrades gracefully but is not the training
  target.

## Where in the toolchain

`brill_postaggers` is a leaf POS-tagging component of the TigreGotico NLP
toolchain: a dependency-light tagger you can drop into a larger pipeline when
you need UD part-of-speech tags without pulling in a heavy model stack. It
holds no entry points and is not an OVOS/OPM plugin. Import it as a plain
library.

---
[← API reference](api.md) · [Home](../README.md)
