import nltk
from nltk.corpus import wordnet as wn

#Goal: write a nob word- translate to english-get hypo/hyper- translate/ see them into Norwegian again

n = input('Enter a Norwegian word: ')


def from_nob_to_en(word):
    for synset in wn.synsets(word, lang='nob'):
        noblem = synset.lemmas('nob')
        #print(synset,"\nThe norwegian lemmas are: ", noblem, '\nThe English translation is: ', synset.lemma_names(), ": \nThe hypernym is: ", synset.hypernyms(),"\nThe hyponym is: ", synset.hyponyms(), '\n')
        synhyp = synset.hypernyms()
        print("\nThe norwegian lemmas are: ", noblem," \nThe hypernym is: ",synset.hypernyms())


from_nob_to_en(n)


hypo = wn.synset('ferry.n.01').lemmas('nob')
#print(hypo)
hype = wn.synset('vessel.n.02').lemmas('nob')
#print(hype)