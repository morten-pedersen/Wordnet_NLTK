import nltk
from nltk.corpus import wordnet as wn

def findSynsets(word):
	synset_word = wn.synsets(word)
	print(synset_word)



#print("Name: {}".format(wn.synset('automobile.n.01').name()))

#motorcar = wn.synset('car.n.01')
#types_of_motorcar = motorcar.hypernyms()

#for synset in types_of_motorcar:
#	print(synset, synset.lemma_names(lang = 'nob'))


