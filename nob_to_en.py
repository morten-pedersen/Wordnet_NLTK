import nltk
from nltk.corpus import wordnet as wn

#Goal: write a nob word- translate to english-get hypo/hyper- translate/ see them into Norwegian again

n = input('Enter a Norwegian word: ')

#takes a norwegian word, translates it to english, get the english hypernyms, then the norwegian hypernyms
def get_norwegian_hypernym(word):
    for synset in wn.synsets(word, lang='nob'):
        synhype = synset.hypernyms()
        for nobhype in synhype:
            print('\nThe English translation is: ', synset.lemma_names(), " \nThe English hypernym is: ",synset.hypernyms()," \nThe Norwegian hypernym is: ", nobhype.lemmas('nob'))

#takes a norwegian word, translates it to english, get the english hyponyms, then the norwegian hyponyms
def get_norwegian_hyponym(word):
    for synset in wn.synsets(word, lang='nob'):
        synhypo = synset.hyponyms()
        for nobhypo in synhypo:
            print('\nThe English translation is: ', synset.lemma_names(), " \nThe English hyponym is: ",synset.hyponyms()," \nThe Norwegian hyponym is: ", nobhypo.lemmas('nob'))



get_norwegian_hyponym(n)
get_norwegian_hypernym(n)
