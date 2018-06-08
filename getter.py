import nltk
from nltk.corpus import wordnet as wn


# function to list out synsets of a chosen word, their lemma_names and the synsets' definitions
def description_of_synsets(word):
	for synset in wn.synsets(word):
		print(synset, synset.lemma_names(),"-", synset.definition())

description_of_synsets('monitor')

