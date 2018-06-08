import nltk
from nltk.corpus import wordnet as wn

global word
global synset_word

def find_synsets(word):
	synset_word = wn.synsets(word)
	print(synset_word)
	return synset_word

def print_norwegian_words(synset_word):
	nor_words = synset_word.hypernyms()
	for synset in nor_words:
		print(synset, synset.lemma_names(lang = 'nob'))

find_synsets('cat')

#print_norwegian_words(synset_word)

#print("Name: {}".format(wn.synset('automobile.n.01').name()))

#motorcar = wn.synset('car.n.01')
#types_of_motorcar = motorcar.hypernyms()

#for synset in types_of_motorcar:
#	print(synset, synset.lemma_names(lang = 'nob'))


