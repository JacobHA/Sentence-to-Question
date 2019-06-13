# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 22:54:32 2018

@author: Jacob
"""
import numpy as np
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

sentence = raw_input("Enter an English sentence to be transformed into a question: \n") #'There will be a book here.'
sentence = sentence.lower()
sentence = sentence.replace('.','')
question_keywords = ['is', 'will', 'are', 'was', 'were', 'am']

word_decomp = sentence.split(' ')

for i in range(len(word_decomp)):
    if word_decomp[i] in question_keywords:
        for x in question_keywords:
            if word_decomp.count(x) >> 1:
                
                if pos_tag(word_decomp)[i+1][1] == 'VBN':
                    word_decomp.insert(0, word_decomp[i])
                    word_decomp.pop(i+1)
                break
            else:
                word_decomp.insert(0, word_decomp[i])
                word_decomp.pop(i+1)
                break
    else:
        if i == len(word_decomp) - 2:
            if word_decomp == sentence.split(' '): # If sentence unchanged
                # Verb reduction:
                for i in range(len(word_decomp)):
                     if 'VB' in pos_tag(word_decomp)[i][1]:
                         #print "BINGO"
                         word_decomp[i] = WordNetLemmatizer().lemmatize(word_decomp[i],'v')
                         #print "Verb reduction to present tense is required:"
                word_decomp.insert(0, 'Did')
     
for i in range(len(word_decomp)): # Cycle through all words
    #print str(np.array(pos_tag([word_decomp[i]]))[0][1])
    #print [word_decomp[i]]
    if 'NP' in str(np.array(pos_tag([word_decomp[i]]))[0][1]): # Searches for a proper noun
        word_decomp[i] = word_decomp[i].capitalize() # Capitalizes the proper noun
                
dot_to_que = word_decomp[len(word_decomp)-1].replace('.', '') # Deletes . at end of sentence if it is there
word_decomp.insert(0,word_decomp[0].capitalize()) # Capitalizes first word of sentence
word_decomp.pop(1) # Removes the possibly lowercase first word since the capitalized version has been inserted already
question = (' ').join(word_decomp) # Create a string to reform the question instead of word by word
if '?' not in question: # Ensures that ? is attached to end of the sentence
    question = question + '?' 
    
print question #Return the final formed question version of the input sentence
