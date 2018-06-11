import nltk
from nltk.corpus import wordnet as wn


# function to list out synsets of a chosen word, their lemma_names, the norwegian bokmål lemmas and the synsets' definitions
def description_of_synsets(word):
	for synset in wn.synsets(word):
		print(synset, synset.lemma_names(), wn.lemmas(word, lang = 'nob'),": \n", synset.definition(), "\n")

description_of_synsets('monitor')

