# for initial download of Wordnet
# nltk.download('wordnet')

help(wn)

GUI browser:
nltk.app.wordnet()


hypernym = definitions above word / superclass, hypernym_paths()
hyponym = definitions below word / subclass
meronym = items to their components, part_meronyms(), substance_meronyms(), member_meronyms()
holonym = things they are contained in
entailments = walking entails stepping
antonym = opposite
dir()
path_similarity() = score between 0 and 1 on shortest path between concepts in hypernym hierarchy


NLTK WordNet uses the method synsets(), where the desired word is entered as an argument, for example wn.synsets('dog')

We are interested in the Norwegian lemmas of the English word, which we can access by using wn.lemmas(word, lang = 'nob'),
or wn.synset('dog.n.01').lemma_names('nob'). 'nob' is Norwegian Bokmål.
