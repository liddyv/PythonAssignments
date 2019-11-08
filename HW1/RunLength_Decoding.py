# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:57:25 2019
Homework 1 -Question 3
Description: 
    Write the reverse function from Question 2 - a run-length-decoder.  That is, write a program with a
    function that  takes a run-length-encoded string, and produces the original string.  
    
    For example, if you pass in:   12W1B12W3B24W1B14W
    your function should return the original string from Question 2:        
    WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

    Another simple example:
    Pass in:  3a4b10c2d
    Should return:  aaabbbbccccccccccdd

@author: Liddy Hsieh
"""

def runLengthDecoding(encoding) :

    myList = []
    i = 0    
    #size = len(encoding)
    currentCount = 0
    currentChar =''
    count = ''
    
    for i, char in enumerate(encoding) :  
        if char.isdigit() :
            count = str(count) + str(char)
            currentCount = int(count)
            currentChar=''  # reset           
        elif char.isalpha() : 
            currentChar = char
            count = 0    #reset    
        # get # of CurrentCount of currentChar and then append
        myList.append(currentCount*currentChar)   
        # convert list to a single String
        newString = ''.join(myList)      
    return newString
 
   
# main         
while True:
    # ask for input from user
    encodedString=input("Please type in a run-length-encoded string (press Enter when done): ")
    #print("You typed: " + str(number))
    
    if encodedString == '':
        print('End the program. ')
        break
    #Call Run-Length Encoding function
    
    rld = runLengthDecoding(encodedString)
    print(rld)
        
       

