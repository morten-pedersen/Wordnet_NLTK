# for initial download of Wordnet
# import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet as wn

print("Synsets: {}".format(wn.synsets('automobile')))

for synset in wn.synsets('automobile'):
	print("Lemma names: {}".format(synset.lemma_names()))

print("Definition: {}".format(wn.synset('automobile.v.01').definition()))