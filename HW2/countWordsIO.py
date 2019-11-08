# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:46:28 2019
@Home work #2, Question 2 - File IO:
@Description: Write a program that will read the file, 
    count the frequency of the words and store it as a csv file.
- def removePunctuation(inputList): removes all the punctuation (periods, 
    commas, double quote) from the words, and returns a list of "cleaned" words.
- def findcount(input): # count the frequency of each word return a dictionary 
    of {<word1>:<count1>, <word2>:<count2>, ...}   
- def writecountfile(csvFileName, aDict): writes the content of aDict variable 
to a csv file with two columns. 
The result should be a file that looks like this (one line for each word and count):
any,1
embellish, 2
wait,1
remember,1
etc.   

@author: Liddy Hsieh
"""
# import string library function  
import string 
from FileReadWrite import *  # means import everything as though it were typed here

DATA_FILE_PATH = 'red-headed-league.txt'
CSV_FILE_NAME = 'output_countWordsIO.csv'


def removePunctuation(inputList):
    #get all punctuation for removal
    removedPunctuation = string.punctuation
    #print(removedPunctuation)
    inputList = ''.join(i for i in inputList if i not in removedPunctuation)
    #print(inputList, type(inputList))
    return inputList
    
    
def findcount(inputList):
    wordCount = {} #dictionary
    
    '''
    for word in inputList:
        if word not in wordCount:
            wordCount[word] = 0
        wordCount[word] += 1
    return wordCount   
    '''
    # Alternative way - using set and build-in .count()
    #Give set of unique words
    unique_words = set(inputList)
    for word in unique_words:
        #print('Frequency of %s is : %d ' %(word, input.count(word)))
        wordCount[word] = inputList.count(word)
    return wordCount
    

def writecountfile(csvFileName, aDict):
    '''
    # Alternative way: not using import
    with open(csvFileName, 'w') as f:
        for word, count in aDict.items():
            f.write('%s,%s\n' %(word, count))
    '''        
    output = ''
    for word, count in aDict.items():
       output += '%s,%s\n' %(word, count)         
    # write to the file             
    writeFile(csvFileName, output)

    
def cleanStrToList(dirtyData):
    #to lower case
    dirtyDataString_lowerCase = dirtyData.lower() 
    # remove all Punctuations
    cleanedString = removePunctuation(dirtyDataString_lowerCase) 
    # to a list
    cleanedList = cleanedString.split() 
    return cleanedList

        
    
# Start up code
if not fileExists(DATA_FILE_PATH):
    print('Hi, file NOT exist yet!')
else:  
    #read the whole file into a variable
    dirtyDataString = readFile(DATA_FILE_PATH) 
    # clean up the data and convert to a list
    cleanedList = cleanStrToList(dirtyDataString)
    # find words count as dictionary
    wordCountDic = findcount(cleanedList) 
    print(wordCountDic, type(wordCountDic))
    # write to a file
    writecountfile(CSV_FILE_NAME, wordCountDic)
    