# for initial download of Wordnet
# import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet as wn

print(wn.synsets('automobile'))

for synset in wn.synsets('automobile'):
	print(synset.lemma_names())