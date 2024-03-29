pip install nltk
for initial download of Wordnet
nltk.download('wordnet')
nltk.download('omw')

help(wn) for help.

GUI browser:
nltk.app.wordnet()





**synsets()**: lists synsets of a word, useful for when the synset is not known. Example: 


`wn.synsets('dog')` 


**synset()**: a set of synonyms that share a common meaning. A synset in NLTK is the "ID" for each word, and used to
access most other methods. 


**lemmas()**: Lists words of the same meaning, with their synset and lemma names. Can be called from synset. 


**lemma_names()**: lists lemma names of a synset. 
Can have relations between them, using derivationally_related_forms(), pertainyms() and antonyms().


**definition()**: lists definition of a synset. Called directly from synset


**name()**: lists name of synset. Called from synset.


**examples()**: lists examples of a synset. Called from synset.


**hypernyms()**: definitions above word / superclass, hypernym_paths()


**hyponyms()**: definitions below word / subclass


**hypernym_paths()**: lists the paths of the synset to its highest hypernym. Callable from synset.


**root_hypernyms()**: lists the highest hypernym of the synset. Callable from synset. 


**hypernym_distances()**: lists distance between hypernyms from a synset. Callable from synset.


**lowest_common_hypernyms()**: lists the lowest common hypernym between two synsets. Example:


`wn.synset('tree.n.01').lowest_common_hypernyms(wn.synset('forest.n.01'))`


**min_depth()**: returns a number of how specific a synset is, meaning how deep the synset is in the hyponym tree


**meronym**: lists items that are components to this word, part_meronyms(), substance_meronyms(), member_meronyms()


**holonym**: reverse to meronym: part_holonyms(), substance_holonyms(), member_holonyms()


**entailments()**: walking entails stepping


**antonyms()**: lists word(s) with opposite meanings. Has to be called from lemmas, and specified which item in index
to list antonyms from, for example:


`walk = wn.synset('walk.v.01')
`

`walk.lemmas()[0].antonyms()
`

**pertainyms()**: lists words pertaining to the word (belonging to). Needs to be called in same way as antonyms()


**derivationally_related_forms()**: lists derivationally related forms. Needs to be called in same way as antonyms()


**path_similarity()**: score between 0 and 1 on shortest path between concepts in hypernym hierarchy. Needs to be called
using the synset of the words you want to compare:


`tree = wn.synset('tree.n.01')`


`forest = wn.synset('forest.n.01')
`


`tree.path_similarity(forest)
`


or


`
wn.synset('tree.n.01').path_similarity(wn.synset('forest.n.01'))
`


**dir()**: shows lexical relations and other methods on a synset. Example:


`dir(wn.synset('tree.n.01'))`




We are interested in the Norwegian lemmas of the English word, which we can access by using either of the following:


`wn.lemmas(word, lang = 'nob')
`

`wn.synset('dog.n.01').lemma_names('nob')
`


or access them from Norwegian:


`wn.synsets('hund', lang = 'nob')
`

`wn.lemmas('hund', lang = 'nob')
`


Språkbanken has a word net consisting of 50,000 synsets (in both bokmål and nynorsk) at 
Norsk Ordvev: https://www.nb.no/sprakbanken/show?serial=oai%3Anb.no%3Asbr-27&lang=nb (updated Feb 2016)


Resources:

http://compling.hss.ntu.edu.sg/omw/


https://www.nb.no/forskning/sprakbanken

