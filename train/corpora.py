from os.path import join


class TextCorpusReader:
    def __init__(self, corpus_id, folder=None):
        self.corpus_id = corpus_id
        self.folder = folder or "res"
        self.corpora = []
        self.load()

    def load(self):
        self.corpora = []
        with open(join(self.folder, self.corpus_id),
                  errors='surrogateescape') as fi:
            lines = fi.read().split("\n\n")
            for l in lines:
                if not l:
                    continue
                tagged_words = [tuple(w.split("\t"))
                                for w in l.split("\n")
                                if len(w.split("\t")) == 2]
                self.corpora += [tagged_words]

    def lines(self, *args, **kwargs):
        for f in self.corpora:
            yield f

    def words(self, *args, **kwargs):
        for l in self.lines():
            for w in l:
                yield w[0]

    def sentences(self, *args, **kwargs):
        for l in self.lines():
            yield " ".join([w[0] for w in l])

    def paragraphs(self, *args, **kwargs):
        for l in self.sentences():
            yield l

    def tagged_words(self):
        for l in self.lines():
            for w in l:
                yield w

    def tagged_sentences(self):
        for l in self.lines():
            yield l


class CatalanUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("ca_ancora-ud-train.txt")


class SpanishUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("es_ancora-ud-train.txt")


class GalicianUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("gl_ctg-ud-train.txt")


class BasqueUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("eu_bdt-ud-train.txt")


class PortugueseUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("pt_bosque-ud-train.txt")


class EnglishUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("en_ewt-ud-train.txt")


class FrenchUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("fr_gsd-ud-train.txt")


class ItalianUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("it_vit-ud-train.txt")


class GermanUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("de_gsd-ud-train.txt")


class DutchUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("nl_alpino-ud-train.txt")


class DanishUniversal(TextCorpusReader):
    def __init__(self):
        super().__init__("da_ddt-ud-train.txt")
