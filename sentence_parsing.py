"""
Homework 3 
IST 664 - NLP
Lennart Zeugner
This script was written by Lennart Zeugner for the purpose of the NLP class at Syracuse University
Code and concepts have been taken from the ppt slides from IST 664 as well as the provided labs. 
"""

import nltk

#Part 1: Create a grammar and parse the given sentences

grammar = nltk.CFG.fromstring("""
  S -> NP VP | PP VP | NP NP
  VP -> V NP | V PP | V VP | V Adv | V VP | Adv NP | Adv VP
  NP -> N | Det NP | Adj NP | N Adv | N NP | Det | N VP | Adj
  PP -> P VP | P NP | P 
  V -> 'had' | 'came' | 'visit' | 'may' | 'go' | 'are'
  Det -> 'a' | 'Their'
  N -> 'party' | 'two' | 'days' | 'kids'
  Adj -> 'nice' | 'naive'
  Adv -> 'yesterday' | 'ago' | 'now' | 'not' | 'always'
  P -> 'to' | 'me' | 'She' | 'We' | 'You'
  """)

rd_parser = nltk.RecursiveDescentParser(grammar)

lst_sent1 = "We had a nice party yesterday".split()
print(lst_sent1)
for tree in rd_parser.parse(lst_sent1):
    print (tree)
    
lst_sent2= "She came to visit me two days ago".split()
print(lst_sent2)
for tree in rd_parser.parse(lst_sent2):
    print (tree)
    
    
lst_sent3 = "You may go now".split()
print(lst_sent3)
for tree in rd_parser.parse(lst_sent3):
    print (tree)
    
lst_sent4 = "Their kids are not always naive".split()
print(lst_sent4)
for tree in rd_parser.parse(lst_sent4):
    print (tree)
    
#Part 2: Create three more sentences that can be parsed by using the created grammar
    
lst_sent5 = "You are always naive".split()
print(lst_sent5)
for tree in rd_parser.parse(lst_sent5):
    print (tree)
    

lst_sent6 = "Their kids are not nice".split()
print(lst_sent6)
for tree in rd_parser.parse(lst_sent6):
    print (tree)
    
    
lst_sent7 = "We had a nice visit two days ago".split()
print(lst_sent7)
for tree in rd_parser.parse(lst_sent7):
    print (tree)
   
    

#Part 3: Create a probabilistic grammar and use the previous sentences as the mini corpus
#Since the probability of each word class needs to add up to 1, I have simply split the probabilites equally by the number of words contained in each word class
    
prob_grammar = nltk.PCFG.fromstring("""
  S -> NP VP [0.1] | PP VP [0.75] | NP NP [0.15]
  VP -> V NP [0.14] | V PP [0.14] | V VP [0.14] | V Adv [0.14] | V VP [0.14] | Adv NP [0.14] | Adv VP [0.16]
  NP -> N [0.125] | Det NP [0.125] | Adj NP [0.125] | N Adv [0.125] | N NP [0.125] | Det [0.125] | N VP [0.125] | Adj [0.125]
  PP -> P VP [0.33] | P NP [0.33] | P [0.34]
  V -> 'had' [0.17] | 'came' [0.17] | 'visit' [0.17] | 'may' [0.17] | 'go' [0.17] | 'are' [0.15]
  Det -> 'a' [0.5] | 'Their' [0.5]
  N -> 'party' [0.25] | 'two' [0.25] | 'days' [0.25] | 'kids' [0.25]
  Adj -> 'nice' [0.5] | 'naive' [0.5]
  Adv -> 'yesterday' [0.2] | 'ago' [0.2] | 'now' [0.2] | 'not' [0.2] | 'always' [0.2]
  P -> 'to' [0.2] | 'me' [0.2] | 'She' [0.2] | 'We' [0.2] | 'You' [0.2]
  """)

viterbi_parser = nltk.ViterbiParser(prob_grammar)

for tree in viterbi_parser.parse(lst_sent1):
    print (tree)
    
for tree in viterbi_parser.parse(lst_sent2):
    print (tree)    
   
for tree in viterbi_parser.parse(lst_sent3):
    print (tree)    

for tree in viterbi_parser.parse(lst_sent4):
    print (tree) 