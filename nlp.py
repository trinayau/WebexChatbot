# NLP logic with spaCy

import spacy
nlp = spacy.load("en_core_web_md")
# creating spacy object
s1=nlp("Will it rain today?")
s2 =nlp("Is it going to rain today?")
similarity = s1.similarity(s2) #spacy how similar are these statements
print(similarity) #tells u how similar it is

#

