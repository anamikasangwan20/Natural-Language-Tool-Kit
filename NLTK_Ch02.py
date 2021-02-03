#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:41:57 2020

@author: anamika
"""
"""
Highlights of this chapter: Text Corpora and its properties, conditional frequency distribution,  
"""

print("\n--- 2.1 Accessing Text Corpora ---\n")

import nltk                                                          # Notes: See fileids in Gutenberg corpus | Corpus is a large body of text. Gutenberg collection contains 25,000 free electronic books
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')                # Notes: Pick out the text Emma from Jane Austen and name it emma. Count the number of words in it.
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))     # Notes: Use the concordance function on emma.
print("Number of words in emma file in gutenberg corpus: ",len(emma))                                                                     # Notes: Library/Package --> Package --> Object --> Method/Function  ==  NLTK --> corpus --> gutenberg --> words
from nltk.corpus import gutenberg                                    # Notes: Avoid using long statements by using 'the import statement'
for fileid in gutenberg.fileids():                                   # Notes: Loop over all fileids in Gutenberg corpus and print following statistics: avg chars/word; avg words/sentence; a lexical diversity score; fileids.
    char_count = len(gutenberg.raw(fileid))
    word_count = len(gutenberg.words(fileid))
    sent_count = len(gutenberg.sents(fileid))
    vocab_count = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(char_count/word_count), round(word_count/sent_count), round(word_count/vocab_count), fileid)
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')      # Notes: Dispalay the longest sentence from the macbeth text and its length
print("\n112th Macbeth sentence: ", macbeth_sentences[111])
print("\nNumber of sentences in Macbeth: ", len(macbeth_sentences))
longest_length = max(len(s) for s in macbeth_sentences)
longest_sentence = [sentence for sentence in macbeth_sentences if len(sentence) == longest_length]    
print ("\nLength of longest sentence in Macbeth: ", longest_length)
print ("\nLongest sentence in Macbeth: ", longest_sentence)

from nltk.corpus import webtext                                     # Notes: Web and Chat Corpus. Gutenberg contains formal literature, it is important to consider less formal language as well. 
for fileids in webtext.fileids():                                   # Notes: From the web and chat corpus print the fileids with first 65 characters
    print(fileids, webtext.raw(fileids)[:65], "\n")
from nltk.corpus import nps_chat                                    # Notes: Instant messaging chat session corpus. Contains over 10,000 'posts'
chatroom = nps_chat.posts('10-19-20s_706posts.xml')                 # Notes: format = dd_mm-age_numberofposts.xml
print(chatroom[123])

# Notes: Borwn corpus and its categories
# Notes: Reuters corpus 
# Notes: Insuagral Address Corpus
# Notes: Annotated Text Corpora
# Notes: Corpora in other languages
# Notes: Loading your own corpus



print("\n--- 2.2 Conditional Frequency Distributions ---\n")        # Notes: Conditional Frequency distribution helps us maintain different frequency distributions for each category. This can be used to study systematic diferences between the categories. Example, female and male trend in 'names' corpus. 

text = ['The','Fulton','County','Grand','Jury','said']              # Notes: Probability terms analog here: event = word; condition = category; So, (condition, event) = (category, word)
pairs = [('news','The'),('news','Fulton'),('news','County'),('news','Grand')]                # Notes: Following from above... FreqDist needs a list of words as input; Conditional FreqDist needs a list of pairs i.e. (category, words) as input
from nltk.corpus import brown                                       # Notes: Create a Conditional Frequency Distribution from brown corpus
cfd_brown = nltk.ConditionalFreqDist((category,event) for category in brown.categories() for event in brown.words(categories=category))     # Note: This is a nested for loop in one line in python

genre_word = [(genre, word) for genre in ['news','romance'] for word in brown.words(categories=genre)]   # Notes: Create a list of pairs from the news and romance genre in brown corpus
print('The number of (genre, word) pairs in news and romance categories: ',len(genre_word))
cfd = nltk.ConditionalFreqDist((genre_word))                        # Notes: Print CFD for 'news' category, then 'romance' category 
print('CFD for news category: ', cfd['news'])
print('CFD for romance category: ', cfd['romance'])
print('20 most common words from news category', cfd['news'].most_common(20))                # Notes: Print the 20 most common words from 'news' category
print('Frequency of \'could\' in the category \'romance\':', cfd['romance']['could'])        # Notes: Print the frequency of the word 'could' in the category 'romance'

print("\n--- Plotting and Tabulating distributions ---\n")
from nltk.corpus import inaugural                                                            # Notes: Plot frequency/occurences of words 'starting with' - america and citizen - in each inaugral address. This shows trend of those words over time. No need to normalize counts for document length.
cfd_inaugural = nltk.ConditionalFreqDist((target, fileid[:4]) for fileid in inaugural.fileids() for w in inaugural.words(fileid) for target in ['america', 'citizen'] if w.lower().startswith(target))          # Notes: Here the x-axis has years, different curves represent the words. So, CFD is not always simple and direct. 
cfd_inaugural.plot()
cfd_inaugural.tabulate()

 # Notes: "Cumulative" Word Length Distributions on udhr corpus for 6 languages. Solution: Languages are the fileids in udhr. X-axis has word lengths. Different curves represent languages.
languages = ['Chickasaw', 'English', 'German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd_word_length = nltk.ConditionalFreqDist((language, len(w)) for language in languages for w in nltk.corpus.udhr.words(language+'-Latin1'))   
cfd_word_length.plot(cumulative=True)                               # Notes: Cumulative = True plots the cumulative frequency and not individual


print("\n--- Generating random text with Bigrams ---\n")

 

print("\n--- 2.3 More Python: Reusing Code (Functions) ---\n")
# <Usual Defining functions>

print("\n--- 2.4 Lexical Resources ---\n")
                                                                    # Notes: A lexicon or a lexical resource is a collection of words/phrases along with associated information such as part of speech or sense definition. Examples from previous chapters: vocabulary, frequency distribution, concordance. Simplest kind of lexicon is a sorted list of words.
                                                                    # Notes: A lexical entry consists of a headword/lemma, part of speech/lexical category, sense definition/gloss
                                                                    # Notes: Wordlist Corpus is a corpus of words and can be used to perform spell check in a text.
def unusual_words(text):                                            # Notes: Find out unusual words or mis-spelt words in a text by comparing text dictionary with wordlist corpus
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab                            # Notes: text_vocab and english_vocab are not lists but sets here. In python, sets can be subtracted. Sets can have any data type, but both should have similar.
    return sorted(unusual)
unusual_words_gutenberg = unusual_words(nltk.corpus.gutenberg.words())
unusual_words_nps_chat = unusual_words(nltk.corpus.nps_chat.words())
        
                                                                    
from nltk.corpus import stopwords                                   # Notes: Stopword corpus: stopwords are words that highly frequent and so add little information (lexical content), they are less useful in making a distinction among texts. They are often filtered out before linguistic processing.
stopwords.words('english')                                          # Notes: Display stopwords in english language
def lexical_content_fraction(text):                                 # Notes: Lexical content in a text: Construct a function to compute what fraction of words in a text are not in the stopwords list
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)
lexical_content_fraction(nltk.corpus.reuters.words())
    
def word_puzzle(puzzle,length):                                     # Notes: Write a program to solve a word puzzle
    puzzle_letters = nltk.FreqDist(puzzle)                          # Solution: The resulting words should (a) consist middle letter (b) be longer than length (c) valid i.e. exist in word corpus vocabulary
    obligatory = puzzle[int(len(puzzle)/2)]                         # the middle index; puzzle will always have an odd number of characters and indexing starts from zero
    return [w for w in nltk.corpus.words.words() if len(w)>=length and obligatory in w and nltk.FreqDist(w) <= puzzle_letters]
word_puzzle('egivrvonl',6)    

names = nltk.corpus.names
names.fileids()
gender_ambiguous_names = [w for w in nltk.corpus.names.words('male.txt') and nltk.corpus.names.words('female.txt')]                                     # Notes: Names Corpus - Find names that occur in both male and female categories in the names corpus i.e. ambiguous gender names
cfd_gender_names = nltk.ConditionalFreqDist((gender, name[-1]) for gender in ['male','female'] for name in nltk.corpus.names.words(gender+'.txt'))      # Notes: Use the CFD plot to see pattern in girl and boy names with the ending character in the name. Solution: The x-axis is the letters and diffrerent curves refer to the 2 genders.
cfd_gender_names.plot()
cfd_gender_names.tabulate()

print("\n--- Pronouncing dictionary ---\n")
print("\n--- Comparative wordlists ---\n")
print("\n--- Shoebox and Toolbox Lexicons ---\n")


print("\n--- 2.5 WordNet ---\n")

print("\n--- Senses and synonyms ---\n") 
from nltk.corpus import wordnet as wn                               # Notes: Explore synonyms with the help of synsets in wordNet. Synonyms => words that have similar meaning.
wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names()                                 # Notes: 'synsets' generates a list of synonyms, 'synset' calls the mentioned synset.
wn.synset('car.n.01').definition()
wn.synset('car.n.01').examples() 
wn.synset('car.n.01').lemmas()                                      # Notes: Pairing a word with a synset is called a lemma.
wn.lemma('car.n.01.automobile')
wn.lemma('car.n.01.automobile').synset()
wn.lemma('car.n.01.automobile').name()
for synset in wn.synsets('car'):                                    # Notes: Print the lemma names of all the synsets of car
    print (synset.lemma_names())
wn.lemmas('car')
wn.synsets('dish')                                                  # Notes: Your Turn: Write down all the senses of the word dish that you can think of. Now, explore this word with the help of WordNet, using the same operations we used above. Solution: dish senses: food dish, dish antenna, dish verb meaning stopped working, petri dish in labs
for synset in wn.synsets('dish'):
    print (synset.lemma_names())
    print (synset.definition())
    print (synset.examples())

# Notes: The WordNet Hierarchy

# More Lexical Relations

# Semantic Similarity

    
# System Design: concordance gives information that can help in the preparation of a dictionary from a text.


