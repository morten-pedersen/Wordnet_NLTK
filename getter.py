import nltk
from nltk.corpus import wordnet as wn


# function to list out synsets of a chosen word, their lemma_names and the synsets' definitions
def description_of_synsets(word):
	for synset in wn.synsets(word):
		print(synset, ":", "\nEnglish lemma names: {}".format(synset.lemma_names()),
			  "\nNorwegian lemmas: {}".format(synset.lemmas(lang = 'nob')),
			  "\nDefinition: {}".format(synset.definition()), "\n")


# function to list the English synset of a given Norwegian lemma
def get_english_synset(word):
	for synset in wn.synsets(word, lang = 'nob'):
		print(synset, synset.lemma_names(), ": \n", synset.definition(), "\n")


def get_hype(word):
	for synset in wn.synsets(word, lang = 'nob'):
		syn = synset.hypernyms()
		for x in range(len(syn)):
			print("Norwegian word: {}".format(word), "\nEnglish synset: {}".format(synset), "\nHypernym: {}".format(syn),
		  "\nHypernym in Norwegian: {}".format(x.lemmas('nob')), "\n")

get_hype('kjøretøy')