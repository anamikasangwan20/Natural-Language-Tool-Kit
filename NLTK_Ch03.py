#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:44:43 2020

@author: anamika
"""
"""
Highlights of this chapter: Accessing text from Web; Stemming and Tokenization; Python: strings, files, regular expressions.
"""

print("\n--- 3.1 Accessing text from a Web and Disk ---\n")

from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"      # Note: This url is not html, it is txt 
#url = "https://www.nltk.org/book/ch03.html"                # run this to see the difference
response = request.urlopen(url)
raw = response.read().decode('utf8')
print("Type of raw text: ",type(raw))
print("Length of raw text: ",len(raw))
print("The first 80 elements of raw text: ",raw[:80])

print("\n--- Tokenizing the accessed text ---\n")

from nltk import word_tokenize                              # Notes: nltk is used now to tokenize but not for any of the tasks above
tokens = word_tokenize(raw)
print("Type of tokens: ",type(tokens))                      # Notes: We have extracted a list of words 'tokens' from a string 'raw'. This forms NLP building block.
print("The length of tokens: ",len(tokens))                        
print("The first 10 elements of token: ",tokens[:10])  
import nltk
text = nltk.Text(tokens) 
print("\nConverting tokens to text:\n")                     # Notes: Tokens can be transformed to 'text' to use text's methods for linguistic processing from Chapter 1
print("Type of text: ",type(text))                          # Notes: Notice the difference in 'type' of text from 'type' of tokens
print("The length of text: ",len(text))
print("The first 10 elements of text: ",text[:10])     
print(text.collocations())
print("\nTrimming content from the raw text:\n")
raw.find("PART I")
raw.rfind("End of Project Gutenberg's Crime")
raw = raw[5336:1157743]
raw.find("PART I")

print("\n--- Accessing raw text from html (install BeautifulSoup) ---\n")

from bs4 import BeautifulSoup
#url = "https://www.nltk.org/book/ch03.html"
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')
print("First 50 elements html from of the webpage: ", html[:50])
raw = BeautifulSoup(html, 'html.parser').get_text()
print("First 50 elements of raw form of the webpage: ", raw[:50])
tokens1 = word_tokenize(raw)
print("First 50 elements of tokenized raw form of the webpage: ", tokens1[:50])
# Unwanted elements: 

print("\n--- Processing Search Engine Results ---\n")


print("\n--- Processing RSS Feeds ---\n")


print("\n--- Reading Local Files ---\n")


print("\n--- Extracting Text from PDF, MSWord and other Binary Formats ---\n")


print("\n--- Capturing User Input ---\n")


print("\n--- The NLP Pipeline ---\n")



print("\n--- 3.2 Strings: Text processing at the lowest level ---\n")

print("\n--- Basic Operations with Strings ---\n")


print("\n--- Printing Strings ---\n")

print("\n--- Accessiing Individual Characters ---\n")


print("\n--- Accessing Substrings ---\n")


print("\n--- More Operations on Strings ---\n")


print("\n--- The Difference between Lists and Strings ---\n")


print("\n--- 3.3 Text Processing with Unicode ---\n")

print("\n--- Extracting Encoded text from files ---\n")


print("\n--- Using your local ending in Python ---\n")
    

print("\n--- 3.4 Regular Expressions for detecting word patterns (pattern matching) ---\n")
# Problem-based approach to RE
import nltk
import re                                                               # Notes: 're' library is needed for regular expressions
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]    # Notes: List of words to search
[w for w in wordlist if re.search('ed$', w)]                            # Notes: RE: words ending with ed
[w for w in wordlist if re.search('^..j..t..$',w)]                      # Notes: RE: 8-letter word with j as its 3rd letter and t as ots 6th letter
[w for w in wordlist if re.search('^e-?mail$',w)]                       # Notes: RE: all words e-mail or email
sum(1 for w in wordlist if re.search('^e-?mail$',w))                    # Notes: RE: count all occurences of e-mail or email in text (1 line code)
[w for w in wordlist if re.search('^[ghi][onm][jkl][def]$',w)]          # Notes: RE: T9 system - words produced with 4653
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
[w for w in chat_words if re.search('^m+i+n+e+$',w)]                    # Notes: RE: mine or mminee or miiiine or miinneeeee...
[w for w in chat_words if re.search('^[ha]+$',w)]                       # Notes: RE: ah or a or aaaa or ahhhh or hahahaha or h...
wsj = sorted(set(nltk.corpus.treebank.words()))
[w for w in wsj if re.search('^[0-9]+\.[0-9]+$',w)]                     # Notes: RE: all decimals
[w for w in wsj if re.search('[A-Z]+\$$',w)]                            # Notes: RE: uppercase alphabets ending with '$'
[w for w in wsj if re.search('^[0-9]{4}$',w)]                           # Notes: RE: 4 digit numbers (can represent years)
[w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$',w)]                  # Notes: RE: '10-day', '10-lap', '10-year', '100-share', '12-point', '12-year'
[w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$',w)]     # Notes: RE: ['black-and-white', 'bread-and-butter', 'father-in-law', 'machine-gun-toting','savings-and-loan']
[w for w in wsj if re.search('(ed|ing)$',w)]                            # Notes: RE: words ending in 'ed' or 'ing'
    
# Notes: T9 system: 1- 2-abc 3-def 4-ghi 5-jkl 6-mno 7-pqrs 8-tuv 9-wxyz
# Question: What is a unicode? (what is a glyph?)


print("\n--- 3.5 Useful Applications of Regular Expressions ---\n")

print("\n--- Extracting Word Pieces ---\n")

print("\n--- Doing More With Word Pieces ---\n")

print("\n--- Finding Word Stems ---\n")

print("\n--- Searching Tokenized Text ---\n")


print("\n--- 3.6 Normalizing Text ---\n")

print("\n--- Stemmers ---\n")

print("\n--- Lemmatization ---\n")


print("\n--- 3.7 Regular Expression for Tokenizing Text ---\n")

print("\n--- Simple Approaches to Tokenization ---\n")

print("\n--- NLTK's Regular Expression Tokenizer ---\n")

print("\n--- Further Issues with Tokenization ---\n")


print("\n--- 3.8 Segmentation ---\n")

print("\n--- Sentence Segmentation ---\n")

print("\n--- Word Segmentation ---\n")


print("\n--- 3.9 Formatting: From Lists to Strings ---\n")

print("\n--- From Lists to Strings ---\n")

print("\n--- Strings and Formats ---\n")

print("\n--- Lining Things Up ---\n")

print("\n--- Writing Results to a File ---\n")

print("\n--- Text Wrapping ---\n")




















