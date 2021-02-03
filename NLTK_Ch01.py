#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:40:36 2020

@author: anamika
"""
"""
Highlights of this chapter: contextual similarity, string operations, frequency distributions, collocations
"""

import nltk
#nltk.download()
from nltk.book import *                                     # Notes:  NLTK = open source 'library', book = 'module' in the library, * => all 'items' in the book module
print("\n'Text1' item is: ",text1)                          # Notes: text1 is an item from the book module in NLTK library 
print(text3[:10])                                           # Notes: 'text' is a list of strings (words and punctuations)

print("\n--- 1.3 Searching Text ---\n")

text1.concordance("monstrous")                              # Notes: 'concordance view' shows us every occuren e of the word with some 'context'
                                                            # Notes: Uses: Search the book of Genesis to find out how long some people lived, using text3.concordance("lived").
text1.similar('monstrous')                                  # Notes: similar gives us words appearing in similar range of contexts
text2.similar('monstrous')                                  # Notes: notice the difference in contexts in text1 and text2 for same word

text1.common_contexts(["monstrous","very"])                 # Notes: used to find contexts shared by the words
text2.common_contexts(["monstrous","very"])

text4.dispersion_plot(["citizens","democracy","freedom","duties","America", "Vietnam"])
                                                            # Notes: text4 is an artificial text created by joining the texts of the Inaugral Address Corpus end-to-end
                                                            # Notes: dispersion_plot plots location of a word in the text. There are stripes in a row, each stripe represents
                                                            # an occurence of the word and each row represents the entire text.
                                                            # numpy and matplotlib are needed to rpoduce this plot    
text3.generate()                                            # Notes: generates some random text of the style of text
text4.generate()
            
print("\n--- 1.4 Counting Vocabulary ---\n")

len(text3)                                                  # Notes: tokens in a text. Tokens are words or punctuation symbols OR technically a sequence of characters that we want to treat as a group
len(set(text3))                                             # Notes: types in a text OR number of words in vocabulary of a text
#sorted(set(text3))                                         # Notes: generates a list of vocabulary *caution: too long*
len(set(text3))/len(text3)                                  # Notes: lexical richness I - lexical diversity of the text
len(text3)/len(set(text3))                                  # Notes: lexical richness II - average number of times each word type occurs in the text
text3.count("smote")
100 * text4.count("a")/len(text4)
"""Exercise"""
text5.count("lol")
100 * text5.count("lol")/len(text5)
def lexical_diversity(sent):
    return len(set(sent))/len(sent)


print("\n--- 2 Texts as a list of words (Python list) ---\n")

print("\n--- 2.1 Lists ---\n")

sent1 = ["Call","me", "Ishmael","."]                        # Notes: sentence as a list of words/tokens
print("\nsent1 is: ",sent1)
print("Length of sent1: ",len(sent1))
print("Lexical diversity of sent1: ",lexical_diversity(sent1))
sent2 = ["The", "family", "of","Dashwood","has","long","been","settled","in","Sussex","."]
sent3 = ["In","the","beginning","God","created","heaven","and","the","earth","."]
print("\nsent2 is: ",sent2)
print("\nsent3 is: ",sent3)
print(["Monty","Python"]+["and","the","holy","grail"])      # Notes: Adding two sentences
print("\nConcateating sent3 and sent2: ",sent3 + sent2)     # Notes: Concatenating
sent1.append("Some")                                        # Notes: Appending to a sentence
print("\nAppended sent1: ",sent1)


print("\n--- 2.2 Indexing Lists ---\n")

text4[173]
text4.index("awaken")
text5[16715:16735]                                          # Notes: Slicing OR extracting mangeable pieces of language from a large text
text6[1130:1142]

print("\n--- 2.3 Variables ---\n")
# <usual>

print("\n--- 2.4 Strings ---\n")

name = "Monty"                                              # Notes: Defining a string (it is not ["Monty"], that's a list)
name[0]                                                     # Notes: Indexing
name[:4]                                                    # Notes: Slicing
name*2                                                      # Notes: Multiplying a string
name+"!"                                                    # Notes: Adding a string
' '.join(["Monty","Python"])                                # Notes: list to a string using separator
"Monty Python".split(" ")                                   # Notes: string to list using separator
          

print("\n--- 3 Simple Statistics ---\n")

print("\n--- 3.1 Statistics: Frequnecy Distribution ---\n")

fdist1 = FreqDist(text1)                                    # Notes: FreqDist is defined in the * book module
print("Most common words : ",fdist1.most_common(50))   
print("\nNumber of hapaxes : ",len(fdist1.hapaxes()))       # Notes: hapaxes = words that occur once in the text
print("\nFirst 10 hapaxes : ",fdist1.hapaxes()[:10])

print("\n--- 3.2 Statistics: Fine-grained selection of words ---\n")

V = set(text1)
long_words = [w for w in V if len(w) > 15]                  # Notes: We decide the length of what a 'long' word will be
print("\nLong Words in text1: ",long_words)

Vocab = set(text2)
long_words2 = [w for w in Vocab if len(w) > 16]
print("\nLong Words in text2: ",long_words2)

def long_words(text,n):
    vocab = set(text)
    long = [word for word in vocab if len(word) > n]
    return long

print("\nLong Words in text4: ",long_words(text4,15))
print("\nLong Words in text5: ",long_words(text5,15)[:10])

print("\n--- 3.3 Statistics: Collocations and Bigrams ---\n")

bigram_list = list(bigrams(['more','is','said','than','done']))     # Notes: Generates a list of bigrams from given words' list. 'bigram' generates an object, 'list' coverts it into a list.
print("Bigram list: \n",bigram_list)                                # bigrams will results in: <generator object bigrams at 0x10fb8b3a8>: This is Python's way of saying that it is ready to compute a sequence of items, in this case, bigrams.

print("\nCollocations:")
text4.collocations()                                    # Notes: collocation is a word-pair (or a sequence of words) that (i) occurs together quite often, and (ii) is resistant to substituion with similar-sense words. E.g. red wine (yes), maroon wine (no!); United States (yes), Divided States (no!)
text8.collocations()                                    # collocations are essentially 'frequent bigrams' except for the fact that in a collocation the individual words are less frequent i.e. rare words in a text. E.g. 'than before' is a bigram, 'United States' is a collocation

                        
print("\n--- 3.4 Counting other things ---\n")          # Notes: i.e. counting other than words


print("\n--- 4 Python: Decisons and Control ---\n")


print("\n--- 4.1 Conditionals ---\n")


print("\n--- 4.2 Operating On Every Element ---\n")

print("\n--- 4.3 Nested Code Blocks ---\n")

print("\n--- 4.4 Looping With Conditions ---\n")


print("\n--- 8 Exercises ---\n")























