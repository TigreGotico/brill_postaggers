import pickle
from random import shuffle

import nltk
from corpora import (CatalanUniversal, SpanishUniversal, DutchUniversal,
                     DanishUniversal, PortugueseUniversal, GermanUniversal,
                     GalicianUniversal, EnglishUniversal, FrenchUniversal,
                     BasqueUniversal, ItalianUniversal)

for ds in [
    FrenchUniversal(),
    ItalianUniversal(),
    BasqueUniversal(),
    CatalanUniversal(),
    SpanishUniversal(),
    DutchUniversal(),
    DanishUniversal(),
    PortugueseUniversal(),
    GalicianUniversal(),
    GermanUniversal(),
    EnglishUniversal()
]:
    corpus = list(ds.tagged_sentences())
    shuffle(corpus)
    cutoff = int(len(corpus) * 0.9)
    train_data = corpus[:cutoff]
    test_data = corpus[cutoff:]

    def_tagger = nltk.DefaultTagger('NOUN')
    affix_tagger = nltk.AffixTagger(
        train_data, backoff=def_tagger
    )
    unitagger = nltk.UnigramTagger(
        train_data, backoff=affix_tagger
    )
    bitagger = nltk.BigramTagger(
        train_data, backoff=unitagger
    )
    tagger = nltk.TrigramTagger(
        train_data, backoff=bitagger
    )

    a = tagger.evaluate(test_data)

    print("Accuracy of ngram tagger : ", a)  # 0.9666686290670748

    tagger = nltk.BrillTaggerTrainer(tagger, nltk.brill.fntbl37())
    tagger = tagger.train(train_data)

    a = tagger.evaluate(test_data)

    print("Accuracy of Brill tagger : ", a)  # 0.9745613865781397

    path = ds.corpus_id.replace("train.txt", "brill.pkl")
    with open(path, "wb") as f:
        pickle.dump(tagger, f)
