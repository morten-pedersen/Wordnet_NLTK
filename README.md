# for initial download of Wordnet
# nltk.download('wordnet')

help(wn)

GUI browser:
nltk.app.wordnet()

'''
hypernym = definitions above word / superclass
hyponym = definitions below word / subclass
meronym = items to their components, part_meronyms(), substance_meronyms(), member_meronyms()
holonym = things they are contained in
entailments = walking entails stepping
antonym = opposite
dir()
path_similarity() = score between 0 and 1 on shortest path between concepts in hypernym hierarchy
'''