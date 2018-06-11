pip install nltk
for initial download of Wordnet
nltk.download('wordnet')
nltk.download('omw')

help(wn) for help.

GUI browser:
nltk.app.wordnet()

**synset()**: a set of synonyms that share a common meaning. A synset in NLTK is the "ID" for each word, and used to
access most other methods
**lemmas()** can be called from synset. Lists words of the same meaning, with their synset and lemma names
**lemma_names()**: lists lemma names of a synset
Can have relations between them, using derivationally_related_forms(), pertainyms() and antonyms()
**hypernyms()** = definitions above word / superclass, hypernym_paths()
**hyponyms()** = definitions below word / subclass
**meronym** = lists items that are components to this word, part_meronyms(), substance_meronyms(), member_meronyms()
**holonym** = reverse to meronym: part_holonyms(), substance_holonyms(), member_holonyms()
**entailments()** = walking entails stepping
**antonyms()** = lists word(s) with opposite meanings. Has to be called from lemmas, and specified which item in index
to list antonyms from, for example:
`walk = wn.synset('walk.v.01')`
`walk.lemmas()[0].antonyms()`
**pertainyms()**: lists words pertaining to the word (belonging to). Needs to be called in same way as antonyms()
**derivationally_related_forms()**: lists derivationally related forms. Needs to be called in same way as antonyms()
**path_similarity()** = score between 0 and 1 on shortest path between concepts in hypernym hierarchy. Needs to be called
using two variables representing the synsets you want to compare:
`tree = wn.synset('tree.n.01')
forest = wn.synset('forest.n.01')
tree.path_similarity(forest)`


We are interested in the Norwegian lemmas of the English word, which we can access by using either of the following:
`wn.lemmas(word, lang = 'nob')
wn.synset('dog.n.01').lemma_names('nob')`

or access them from Norwegian:
`wn.synsets('hund', lang = 'nob')
wn.lemmas('hund', lang = 'nob')`


