# API reference

Everything public lives in one module: `brill_postaggers`.

```python
from brill_postaggers import BrillPostagger
```

## `class BrillPostagger`

A thin wrapper around a pickled NLTK Brill tagger.

### `BrillPostagger.MODELS`

Class attribute. A `dict[str, str]` mapping a language code to the model file
stem that ships in the package:

```python
BrillPostagger.MODELS == {
    "ca": "ca_ancora-ud-brill",
    "da": "da_ddt-ud-brill",
    "de": "de_gsd-ud-brill",
    "en": "en_ewt-ud-brill",
    "es": "es_ancora-ud-brill",
    "eu": "eu_bdt-ud-brill",
    "fr": "fr_gsd-ud-brill",
    "gl": "gl_ctg-ud-brill",
    "it": "it_vit-ud-brill",
    "nl": "nl_alpino-ud-brill",
    "pt": "pt_bosque-ud-brill",
}
```

The stems encode the source treebank (for example `pt_bosque` is the Portuguese
Bosque UD treebank). Use the keys to enumerate supported languages:

```python
for code in sorted(BrillPostagger.MODELS):
    print(code)
```

### `BrillPostagger.from_pretrained(lang: str) -> BrillPostagger`

Static method. The normal entry point. It:

1. normalizes `lang` with `lang.split("-")[0].lower()`, so `"PT-BR"` -> `"pt"`,
2. looks the code up in `MODELS` (raising `KeyError` for an unknown code),
3. loads the bundled `<stem>.pkl` from the package directory,
4. returns a ready `BrillPostagger`.

```python
tagger = BrillPostagger.from_pretrained("es")
```

The region split only handles a `-` separator, so `"pt-BR"` normalizes but
`"pt_PT"` is passed through and would `KeyError`; pass the bare two-letter code
when in doubt.

### `BrillPostagger(model: str)`

Constructor. `model` is the absolute path to a pickled NLTK tagger. Loading any
instance calls `nltk.download('punkt_tab')` so the tokenizer is available. You
rarely call this directly — prefer `from_pretrained` — but it lets you load a
model you trained yourself:

```python
tagger = BrillPostagger("/path/to/my_lang-brill.pkl")
```

### `BrillPostagger.tag(sentence: str) -> list[tuple[str, str]]`

Instance method. Word-tokenizes `sentence` with `nltk.word_tokenize`, then runs
the Brill tagger over the tokens. Returns a list of `(token, tag)` tuples in
order, with punctuation kept as its own token:

```python
tagger = BrillPostagger.from_pretrained("pt")
tagger.tag("o gato dorme.")
# [('o', 'DET'), ('gato', 'NOUN'), ('dorme', 'VERB'), ('.', 'PUNCT')]
```

Tags are [Universal Dependencies POS tags](https://universaldependencies.org/u/pos/):
`ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`,
`PRON`, `PROPN`, `PUNCT`, `SCONJ`, `SYM`, `VERB`, `X`.

## Instance attributes

| Attribute | Type | Notes |
| --- | --- | --- |
| `tagger` | NLTK Brill tagger | The unpickled model; exposes its own `.tag(tokens)` over pre-tokenized lists. |

If you already have tokens, you can bypass `word_tokenize` and call the
underlying model directly:

```python
tagger = BrillPostagger.from_pretrained("en")
tagger.tagger.tag(["hello", "world"])
# [('hello', 'INTJ'), ('world', 'NOUN')]
```

## Errors

| Condition | Raised |
| --- | --- |
| Unknown language code in `from_pretrained` | `KeyError` |
| Bad path in `BrillPostagger(model)` | `FileNotFoundError` |

## Where next

- [quickstart.md](quickstart.md) — install and first call
- [advanced.md](advanced.md) — guards, batching, reuse, tagset filtering
</content>
