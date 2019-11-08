# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 07:55:02 2019
Homework 1: Question 1
Description: 
    Write a Python program with a function named kaprekarCount.  It should
    accept a number as input, and return the number of steps needed to reach
    the Kaprekar constant of 6174 or zero.
    Modified version of problem #414 from project Euler 
    (https://projecteuler.net/problem=414)
    
@author: Liddy Hsieh
"""

# define constant
KAPREKAR_CONSTANT = 6174

# return an ascending list of integer
def sortListAsc(number):
    # using list comprehension to convert number to list of integers
    numberList = [int(x) for x in str(number)]
    ascending_numberList = sorted(numberList)
    #print("asceding list of numbers: " + str(ascending_numberList))
    return ascending_numberList       

# return an descending list of integer
def sortListDes(number): 
    # using list comprehension to convert number to list of integers
    numberList = [int(x) for x in str(number)]
    descending_numberList = sorted(numberList, reverse=True)
    #print("descending list of numbers: " + str(descending_numberList))
    return descending_numberList

# convert a list of integers into a single integer
def convertListToSingleInt(sorted_numberList):
    # converting integer list to string list
    s = [str(i) for i in sorted_numberList]
    # Join list items using join()
    sorted_number = int("".join(s))
    return sorted_number

# return substraction
def sub(ascending_number, descending_number):
    subNumber = descending_number - ascending_number
    return subNumber

'''
The process of sorting and subtracting and repeating this 
until either 0 or the Kaprekar constant is reached
'''
def kaprekarCount(number):
    count = 0
     # till == 6174 or 0
    while ( number!=KAPREKAR_CONSTANT and number!=0):
        # sorting 
        #ascending_number = "".join((sorted(str(number)))
        #descending_number = "".join(sorted(str(number), reverse=True))
        ascending_numberList = sortListAsc(number)
        ascending_number = convertListToSingleInt(ascending_numberList)
        #print(ascending_number)
    
        descending_numberList = sortListDes(number)
        descending_number = convertListToSingleInt(descending_numberList)
        #print(descending_number)
    
        print( str(ascending_number) + " " + str(descending_number) )
        
        # subtracting
        number = sub(ascending_number, descending_number)
        print(str(number))

        count+=1
        # print(count)
    return count

# main
while True:
    # ask for input from user
    number=input("Please type in a 4 digit number (press Enter when done): ")
    #print("You typed: " + str(number))
    size = len(number) # get length of number
    if number == '':
        print('End the program. ')
        break
    if size != 4:
        print('You need to type in 4 digit number!')
        continue
    try:
        # convert string to int
        number=int(number)
    except:
        print("Hey buddy, that wasn't a number. Please enter a 4 digit number")
        continue # go back to the while statement    
    # call the function
    answer = kaprekarCount(number)
    print("The number of steps to reach Kaprekar constant for " + str(number) + " is " + str(answer) + "\n")
       