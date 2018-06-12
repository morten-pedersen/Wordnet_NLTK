import nltk
from nltk.corpus import wordnet as wn


# function to list out synsets of a chosen word, their lemma_names and the synsets' definitions
def description_of_synsets(word):
	for synset in wn.synsets(word):
		print(synset,":", "\nEnglish lemma names: {}".format(synset.lemma_names()),
			  "\nNorwegian lemmas: {}".format(synset.lemmas(lang = 'nob')),
			  "\nDefinition: {}".format(synset.definition()), "\n")

w = input('Enter a english word: ')
#if w != wn.synsets.lemma(): #hvordan skrive denne setningen?
#def test_dette(word):
 #   for synset in wn.synsets(word):

#try:
description_of_synsets(w)
#except Exception as e:
#    print('Can not find the word')

# function to list the English synset of a given Norwegian lemma
def get_norwegian_lemma(word):
	for synset in wn.synsets(word, lang='nob'):
		print(synset, synset.lemma_names(), ": \n", synset.definition(), "\n")

#get_norwegian_lemma('knask')
