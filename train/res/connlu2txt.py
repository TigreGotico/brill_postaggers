

path = "/home/miro/Dev/postag/res/es_ancora-ud-train.conllu"
dataset = ""
with open(path, "r") as f:
    for l in f.read().split("\n"):
        if l.strip().startswith("#"):
            continue
        splits = l.split("\t")
        if len(splits) == 1 or not splits[0].isdigit():
            dataset += "\n"
            continue
        word = splits[1]
        tag = splits[3]
        if word and tag:
            dataset += f"\n{word}\t{tag}"

with open(path.replace(".conllu", ".txt"), "w") as f:
    f.write(dataset)