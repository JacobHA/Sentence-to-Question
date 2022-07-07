# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 22:54:32 2018

@author: Jacob

### 
Example:
Input:
'There will be a book here.'
Output:
'Will there be a book here?'

"""
import numpy as np
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

sentence = raw_input("Enter an English sentence to be transformed into a question: \n")
sentence = sentence.lower()
sentence = sentence.replace('.', '')
question_keywords = ['is', 'will', 'are', 'was', 'were', 'am']

word_decomposition = sentence.split(' ')

for i, word_i in enumerate(word_decomposition):
    if word_i in question_keywords:
        for x in question_keywords:
            if word_decomposition.count(x) > 1:
                
                if pos_tag(word_decomposition)[i + 1][1] == 'VBN':
                    word_decomposition.insert(0, word_i)
                    word_decomposition.pop(i + 1)
                break
            else:
                word_decomposition.insert(0, word_i)
                word_decomposition.pop(i + 1)
                break
    else:
        if i == len(word_decomposition) - 2:
            if word_decomposition == sentence.split(' '): # If sentence unchanged
                # Verb reduction:
                for i in range(len(word_decomposition)):
                     if 'VB' in pos_tag(word_decomposition)[i][1]:
                         word_decomp[i] = WordNetLemmatizer().lemmatize(word_i, 'v')

                     word_decomposition.insert(0, 'Did')
     
for i, word_i in enumerate(word_decomposition): # Cycle through all words

    if 'NP' in str(np.array(pos_tag([word_i]))[0][1]): # Searches for a proper noun
        word_decomp[i] = word_i.capitalize() # Capitalizes the proper noun
                
dot_to_que = word_decomposition[len(word_decomposition)-1].replace('.', '') # Deletes . at end of sentence if it is there
word_decomp.insert(0, word_decomposition[0].capitalize()) # Capitalizes first word of sentence
word_decomposition.pop(1) # Removes the possibly lowercase first word since the capitalized version has been inserted already
question = (' ').join(word_decomposition) # Create a string to reform the question instead of word by word
if '?' not in question: # Ensures that ? is attached to end of the sentence
    question += '?' 
    
print(question) #Return the final formed question version of the input sentence
