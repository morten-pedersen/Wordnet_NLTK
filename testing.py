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
types_of_motorcar = mcar.hyponyms()
#types_of_motorcar[]

for synset in types_of_motorcar:
   # for lemma in synset.lemmas():
      print(sorted(synset.lemma_names()))


'''
'''
print(mcar.hypernyms())
paths = mcar.hypernym_paths()
print(len(paths))
for synset in paths[0]: #paths[1]
    print(synset.name())

'''
'''
tree_part= wn.synset('tree.n.01').part_meronyms()
tree_type= wn.synset('tree.n.01').substance_meronyms()
tree_member= wn.synset('tree.n.01').member_holonyms()
print(tree_part,'\n', tree_type,'\n',tree_member)
'''

'''
for synset in wn.synsets('mint', wn.NOUN):
    print(synset.name() + '-', synset.definition())

sub=wn.synset('mint.n.04').substance_holonyms()
par=wn.synset('mint.n.04').part_holonyms()
mem=wn.synset('mint.n.04').member_holonyms() #empty

print(sub,'\n', par,'\n',mem)
'''
'''
ent =wn.synset('eat.v.01').entailments()

print(ent)

print(wn.lemma('horizontal.a.01.horizontal').antonyms())
'''


