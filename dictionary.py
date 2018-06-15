import nltk
from nltk.corpus import wordnet as wn


# function to list out synsets of a chosen word, their lemma_names and the synsets' definitions
w = input('Enter a English word: ')

def description_of_synsets(word):
    for synset in wn.synsets(word):
            print(synset, ":", "\nEnglish lemma names: {}".format(synset.lemma_names()),
                  "\nNorwegian lemmas: {}".format(synset.lemmas(lang='nob')),
                  "\nDefinition: {}".format(synset.definition()), "\n")

if wn.synsets(w):
    description_of_synsets(w)
else:
    print('Did not find the word: ', w)


'''
#dictionary from sentistrength
file=(open('Dictionary.txt','r'))
for line in file:
   print(line)

with open('Dictionary.txt', 'r') as file1:
    with open('some_file_2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('some_output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
'''