#!/usr/bin/python3
import ssl
import os
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk
import sys
import operator
from functools import reduce

#nltk.download('punkt')
from nltk.tokenize import word_tokenize


#intialize path
######CHANGE THIS BACK TO creepyCrawlingPages#####
path = os.path.join("/home/jeff/Documents/NJIT/is392/Crawler/creepyCrawlingPages")
pages = os.fsencode(path)


index={}
docCount=0
stopwordList = ["is", "the", "a", "do"]
totalVocab=0
wordCount=0
hashtable={}
unique=[]

for file in os.listdir(pages):
    filename = os.fsdecode(file)
    if filename.endswith(".html"):
        #print(filename)
        
        #CREATE A HASH TABLE
        #hashTable={}

        docCount+=1
        ######CHANGE THIS BACK TO creepyCrawlingPages#####
        page_content = open("/home/jeff/Documents/NJIT/is392/Crawler/creepyCrawlingPages/" + filename, 'r')
        page_content=page_content.read()
        #print("PAGE_CONTEENT: " + page_content)
        #page_content is contents of the entire html

        soup = BeautifulSoup(page_content, "lxml")
        txt = soup.get_text()
        #print("TEXT: " + txt)
        #txt is the html removed text


    
        temp={}

        #PARSE THAT SHIIII
        tokens = nltk.word_tokenize(txt)
        #tokens contains all words
        for t in tokens:
            
            t = t.lower()
            if t in stopwordList:
                    continue
            if t not in unique:
                unique.append(t)
                totalVocab+=1
        #print(t)
   ##########33WORKING IN HEEREE ######################3
            if t not in temp:
                wordCount=1
                temp[t] = []
                #print("DOCCOUNT IS THIS: " + str(docCount))
                temp[t].append((docCount, wordCount))
                hashtable.update(temp) 

                #temp[t].append((docCount, wordCount))
            else:
                wordCount+=1
                #print("DOCCOUNT IS THIS: " + str(docCount))
                for key, value in temp.items():
                    temp[t] = ((docCount, wordCount))
                
        #printing dict
        #for key in temp:
            #print (key, temp[key])

    ###### WORKING IN HERE  #####################

            
        #for key in temp:
        #     if key not in index:
        #         index[key] = []
        #     else:
        #         index[key].append((docCount, wordCount))




print(hashtable)



f=open('index.txt', 'w', encoding = 'utf=8')
f.write(str(hashtable))

f.close()


f1=open('vocab.txt', 'w', encoding = 'utf=8')
f1.write("TOTAL NUMBER OF VOCABULARY: " + str(totalVocab))
f1.write('\n')
f1.write('\n')
f1.close()

    #print (key, index[key])
                #wordCount+=1
                #print(docCount)
                #print(t)
                #print(wordCount)
                #temp[t].append((docCount, wordCount))
        #print(temp)

####
#            for key in temp:
#                   
                
#                print(key)
                

#                if key not in hashTable:
#                    hashTable[key] = None
#                hashTable[temp] = 
####



            #TOKENIZED NEED TO INSERT TOKENS INTO HASH TABLES
            

        
        


        




