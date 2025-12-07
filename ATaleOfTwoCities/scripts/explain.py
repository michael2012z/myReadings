import spacy

nlp = spacy.load("en_core_web_sm")


def loadNewWordList():
    newWords = []
    with open("../../vocabulary/c1.txt", "r", encoding="utf-8") as f:
        c1Lines = f.readlines()
        c1Lines = list(filter(lambda x: not x.startswith("# "), c1Lines))
        c1Lines = [line.strip() for line in c1Lines]
    newWords.extend(c1Lines)

    with open("../../vocabulary/c2.txt", "r", encoding="utf-8") as f:
        c2Lines = f.readlines()
        c2Lines = list(filter(lambda x: not x.startswith("# "), c2Lines))
        c2Lines = [line.strip() for line in c2Lines]
    newWords.extend(c2Lines)

    return newWords

newWords = loadNewWordList()
print(newWords)


def explain(inText):
    words = inText.split()
    for word in words:
        if len(word) > 2:
            doc = nlp(word)
            lemma = doc[0].lemma_
            if lemma in newWords:
                print(word + " -> " + lemma)
    return inText

for chapter_index in range(2, 3):
    outLines = []
    with open(f"../raw/chapter_{chapter_index:02d}.txt", "r", encoding="utf-8") as inF:
        inLines = inF.readlines()
        
        for inLine in inLines:
            outLine = explain(inLine)
            outLines.append(outLine)

    with open(f"../chapter_{chapter_index:02d}.txt", "w", encoding="utf-8") as outF:
        outF.writelines(outLines)
