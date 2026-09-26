# Brill Postagger

`brill_postaggers` is a Python package for part-of-speech tagging. It uses the
Brill Tagging algorithm and ships pre-trained models for several languages. It
uses the NLTK library for tokenization and tagging.

The models are trained with [UniversalDependencies](https://github.com/UniversalDependencies) datasets.

## Installation

Install the package with pip:

```bash
pip install brill_postagger
```

## Usage

To use the Brill Postagger, load the pre-trained model for a language, then
use it to tag a sentence.

Example usage:

```python
from brill_postaggers import BrillPostagger

# Initialize the tagger for Portuguese (pt)
tagger = BrillPostagger.from_pretrained("pt")

# Tag a sentence
result = tagger.tag("como está o tempo lá fora?")
print(result)
```

See [docs/quickstart.md](docs/quickstart.md) for a full walkthrough,
[docs/api.md](docs/api.md) for the class reference, and
[docs/advanced.md](docs/advanced.md) for recipes and gotchas.

### Supported Languages

Each language below has its own pre-trained model:

- Catalan (`ca`)
- Danish (`da`)
- German (`de`)
- English (`en`)
- Spanish (`es`)
- Basque (`eu`)
- French (`fr`)
- Galician (`gl`)
- Italian (`it`)
- Dutch (`nl`)
- Portuguese (`pt`)

### Related projects

- [TigreGotico/crf_query_xtract](https://github.com/TigreGotico/crf_query_xtract), a CRF-based query-extraction tagger in the same TigreGotico NLP toolchain.
- [TigreGotico/tugatagger](https://github.com/TigreGotico/tugatagger), a Portuguese POS tagger.

### Contributing

If you would like to contribute to the project, submit issues or pull
requests. Contributions are welcome.

### License

This project uses the MIT License. See the [LICENSE](LICENSE) file for
details.
