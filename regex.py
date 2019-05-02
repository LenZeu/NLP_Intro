# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:22:36 2019

@author: zeugn
Homework 2
Natural Language Processing
"""

#Question Number 2

#Load the required libraries
import nltk
import glob
import os
import re
import pandas as pd


#Change the working directory
os.getcwd()

#Load all txt files
#Concatenate all txt files and write them to one file
read_file = glob.glob(r'''C:\\Users\zeugn\Documents\NSF\*.txt''')
with open("result.txt", "wb") as outfile:
    for f in read_file:
        with open(f,"rb") as infile:
            outfile.write(infile.read())

#Read txt files that contains all the abstract files    
first_file = 'result.txt'
fin = open(first_file)
raw_text = fin.read()
type(raw_text)

#tokenize the text using the nltk tokenizer
tokens = nltk.word_tokenize(raw_text)
text = nltk.Text(tokens)
text

#Find the file name
pattern1 = re.compile(('a\d\d\d\d\d\d\d'))
matches = re.findall(pattern1,raw_text)
col1 = []
for m in matches:
    col1.append(m)
len(col1)

#Fine the NSF Organization
pattern2 = re.compile('(?:^|\W)Org(?:$|\W)\s+\:\s\w\w\w')
matches = re.findall(pattern2,raw_text)
col2 = []
for m in matches:
    col2.append(m[-3:])
len(col2)
        
#Find the total award amount
pattern3 = re.compile('(?:^|\W)Amt.(?:$|\W)\s+\:\s\$\d+')
matches = re.findall(pattern3,raw_text)
col3 = []
for m in matches:
    m.find('$')
    col3.append(m[m.find('$'):])
len(col3)


#Extract each of the abstract text using indexing
title_index = 0
abstract_index = 0
col4= []
for i in range(4015):
    title_index = raw_text.find('Title',title_index + 1)
    abstract_index = raw_text.find('Abstract',abstract_index + 1)
    abstract = raw_text[abstract_index+20:title_index]
    abstract = abstract.strip()
    abstract = abstract.strip('\n')
    abstract = abstract.replace('\n', '')
    col4.append(abstract)
    
len(col4)    
col4[0]


len(col1)
len(col2)
len(col3)
len(col4)

#Create a dataframe to convert the extracted data to tabular format
df = pd.DataFrame({'File': col1,
                   'NSF':col2,
                   'Total Amnt': col3,
                   'Abstract': col4}
                   )
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 20)
df


#Question Number 3

#Load more libraries
from nltk.tokenize import sent_tokenize
import re

#Create the sentences of first abstract and prepare outputs
first_abstract = col4[0]
sent = sent_tokenize(first_abstract)
for i in range(len(sent)):
    new_sent = sent[i].strip()
    print( str(col1[0]) + "|" + str(i+1) + "|" + re.sub(' +',' ', new_sent))
print("Number of sentences: " + str(i+1)  )



#Create the sentences of second abstract and prepare outputs
second_abstract = col4[1]
sent = sent_tokenize(second_abstract)
for i in range(len(sent)):
    new_sent = sent[i].strip()
    print( str(col1[1]) + "|" + str(i+1) + "|" + re.sub(' +',' ', new_sent))
print("Number of sentences: " + str(i+1)  )

#Create the sentences of third abstract and prepare outputs
third_abstract = col4[2]
sent = sent_tokenize(third_abstract)

for i in range(len(sent)):
    new_sent = sent[i].strip()
    print( str(col1[2]) + "|" + str(i+1) + "|" + re.sub(' +',' ', new_sent))
print("Number of sentences: " + str(i+1)  )



#Create all abstracts by using looping
 
for i in range(len(col4)): 
    sentences = sent_tokenize(col4[i])
    for x in range(len(sentences)):
            new_sent = sentences[x].strip()
            print( str(col1[i]) + "|" + str(i+1) + "|" + re.sub(' +',' ', new_sent))
    print("Number of sentences: " + str(x+1)  )
        
    
    
    
    
    
    






    

    
    
    
        


    
    
    
    
    
    


            
         






            








          
         