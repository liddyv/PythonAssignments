# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 18:16:09 2019
Homework 1 -Question 2
Description: 
    Write a program that takes a starting string, and implements a run-length encoding scheme 
    to output a new string.  The idea is to analyze  any starting string, looking for "runs" of the 
    same character, and outputs a new string that is made up of:
    <count><character><count><character><count><character> ...

    As an example, start with the string: 
    WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
    that has 67 characters. Your code should convert this string to:
    12W1B12W3B24W1B14W
    
@author: Liddy Hsieh
"""
# Way 1
def runLengthEncoding(inputString):
    currentLetter = inputString[0]
    count = 0
    outputString = ''
    
    for nextLetter in inputString:
        if currentLetter == nextLetter :
            count += 1

        else :
            outputString += str(count) + currentLetter
            currentLetter = nextLetter
            count = 1
    
    outputString += str(count) + currentLetter
    
    return outputString 
    

'''
# Way 2
def runLengthEncoding(string):
    i = 0
    size = len(string) # get length of input
    #result = [] #another approach
    result = ''

    while( i< size) :
        count = 1;
        currentChar = string[i]
        currentCount = count
        
        while( i < size-1 and string[i] == string[i+1] ) :
            count+=1
            currentCount = count
            currentChar = string[i]
            i+=1 
            
        i+=1
        
        #result.append(str(currentCount) + currentChar) #append all CountChar as a list
        result += str(currentCount) + currentChar
    
    #newString = ''.join(result) # convert a list into single string
    #return newString
    
    return result
'''    

# main         
while True:
    # ask for input from user
    string=input("Please type in any string (press Enter when done): ")
    #print("You typed: " + str(number))
    
    if string == '':
        print('End the program. ')
        break
    #Call Run-Length Encoding function
    rle = runLengthEncoding(string)
    print(rle)