import nltk
from nltk.corpus import wordnet as wn

print("Synsets: {}".format(wn.synsets('automobile')))

for synset in wn.synsets('automobile'):
	print("Lemma names: {}".format(synset.lemma_names()))

print("Definition: {}".format(wn.synset('automobile.v.01').definition()))

print("Name: {}".format(wn.synset('automobile.n.01').name()))

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()

for synset in types_of_motorcar:
	print(synset, synset.lemma_names())

paths = motorcar.hypernym_paths()
print(paths)