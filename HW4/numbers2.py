# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:43:32 2019

@author: Liddy Hsieh 

Description: modify of numbers.py
    Create a program that does some simple math on a list of numbers.

Details Requirements:
- Build a loop.  Each time through the loop, ask the user to enter a number.  Your program should collect the numbers into a list - using <yourListName>.append(<value>).
- The user can enter integers or floating point numbers, and your code should convert whatever the user types into a floating point number.
- Allow the user to continue to input numbers until the user presses the Return or the Enter key (at which point the resulting input will be the empty string, ‘’).
Once the user has finished entering numbers, using one or more “for” loops, your program should:

1) Print the resulting list (one value per line)

2) Print the number of numbers in the list

3) Calculate and print the sum of all the numbers in the list

4) Calculate and print the average of all the numbers in the list

5) Determine and print out smallest number in the list

6) Determine and print the largest number in the list

(The last two are the tricky ones)

NOTE:  If you do some research, you will find that there are some built-in list functions that will do these functions for you (sum, min, max, sort, etc.).  Do NOT use these functions.  I want you to get the experience of writing “for” loops to iterate through lists.
And if you want an extra challenge, add some error detection and correction.  If the user enters something that is not a number, for example,  "abc",  the program should print out an error message, then go back and ask for the next number.
 
"""

# ask for input
numbers_list=[]
#userNumber = input("Please enter an integer (press Enter when done): ")
while True:
    userNumber = input("Please enter an integer (press Enter when done): ")  

    if userNumber == '':
        print('End the program. ')
        break
    
    try:
        userNumber=float(userNumber)
    except:
        print("Hey buddy, that wasn't a number")
        continue # go back to the while statement
    
    numbers_list.append(userNumber)
    
#1) Print the resulting list (one value per line)
print(*numbers_list, sep="\n")
print(type(numbers_list), numbers_list)    


#2) Print the number of numbers in the list
for number in range(len(numbers_list)):
    #numbers_list[number] = float(numbers_list[number])
    print (number);


smallest = int(numbers_list[0])
largest = int(numbers_list[0])
for number in numbers_list:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
    
print("- Smallest value in list is: " , smallest)
print("- Largest value in list is: " , largest)
 
