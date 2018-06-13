import nltk
from nltk.corpus import wordnet as wn

#Goal: write a nob word- translate to english-get hypo/hyper- translate/ see them into Norwegian again

n = input('Enter a Norwegian word: ')

#transelates to english
def get_translation(word):
    for synset in wn.synsets(word, lang='nob'):
        print(synset, ":", "\nEnglish lemma names: ", synset.lemma_names(),"\nNorwegian lemmas: ", synset.lemmas(lang='nob'), "\nDefinition: ", synset.definition(), "\n")

#takes a norwegian word, get the english hypernyms, then the norwegian hypernyms
def get_norwegian_hypernym(word):
    for synset in wn.synsets(word, lang='nob'):
        synhype = synset.hypernyms()
        for hype in synhype:
            print(" \nThe English hypernym is: ",hype," \nThe Norwegian hypernym is: ", hype.lemmas('nob'), '\n')

#takes a norwegian word, get the english hyponyms, then the norwegian hyponyms
def get_norwegian_hyponym(word):
    for synset in wn.synsets(word, lang='nob'):
        synhypo = synset.hyponyms()
        for hypo in synhypo:
            print(" \nThe English hyponym is: ",hypo," \nThe Norwegian hyponym is: ", hypo.lemmas('nob'), '\n')



if wn.synsets(n):
    print('Did not find the word: ', n)
else:
    get_translation(n), get_norwegian_hyponym(n), get_norwegian_hypernym(n)