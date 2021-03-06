from random import randint
from nltk.corpus import CategorizedPlaintextCorpusReader


reader = CategorizedPlaintextCorpusReader(
    r'/home/vahid/data/mix20_rand700_tokens_cleaned/tokens', r'.*\.txt', cat_pattern=r'(\w+)/*')
print(reader.categories())
print(reader.fileids())

posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')

fileP = posFiles[randint(0, len(posFiles)-1)]
fileN = negFiles[randint(0, len(posFiles)-1)]
print(fileP)
print(fileN)

for w in reader.words(fileP):
    print(w + ' ', end='')
    if (w is '.'):
        print()

for w in reader.words(fileN):
    print(w + ' ', end='')
    if (w is '.'):
        print()
