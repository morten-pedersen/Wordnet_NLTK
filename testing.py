import nltk
from nltk.corpus import wordnet as wn

syn = wn.synsets('motorcar')

mcar = wn.synset('car.n.01')

name = mcar.name()
lena = mcar.lemma_names()
lem = mcar.lemmas()
defi = mcar.definition()
ex = mcar.examples()
hype = mcar.hypernyms()
hypo = mcar.hyponyms()


#print(syn, "\n", name, "\n", lena, "\n", lem, "\n", defi, "\n", ex, "\n", hype, "\n", hypo)
'''
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[26]
'''
#print(sorted([lemma.name for synset in types_of_motorcar for lemma in synset.lemmas]))
'''
print(motorcar.hypernyms())
paths = motorcar.hypernym_paths()
print(len(paths))
synset.name for synset in paths[0]:
'''