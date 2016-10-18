import os
# import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader


# import glob

# path = 'corpus'

# filenames = ''
# # listing files to read one by one and do works on them later
# for filename in glob.glob('*.txt'):
#     filenames.append(filename)

# direct = ""
corpus_dir = os.getcwd() + "\corpus"
thunderData = PlaintextCorpusReader(corpus_dir, '.*')
for infile in sorted(thunderData.fileids()):
    print(infile)
    with thunderData.open(infile, encoding="utf8") as fin:
        print(fin.read().strip())


# thunderData.2016-09-19.txt

# corpus_dir = corpus_dir + "\corpus\\2016-09-19.txt"
# print(corpus_dir)
# f = open(corpus_dir, encoding="utf8") #without specifying encoding there will be an error. file can't be read
# content = f.read()
# print(content)
# content = content.split()
