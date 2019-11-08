# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:41:33 2019
# Assignment 2: Allow user to input any number of numbers. press Enter to move on and 
2.1. print the list. 
2.2. print the sum of all numbers in list. 
2.3. print number of elements in List
2.4. print average
2.5 find and print smallest value in list
2.6 find and print largest value in list

# Test cases:
1. enter any numbers with space (i.e. -100 0 100) -> Expect to pass
2. enter strings / double bytes characters /number wihtout space -> Expect to catch 
    exception and ask to enter numbers
3. enter q or "Q" to quit -> Expect to exit program
4. enter blank to exit the program -> Expect to exit program
 
@author: Liddy Hsieh
"""
while True: 
    # try ... except loop 
    try:      
        # ask for input
        numbers_string=input('Please enter a list of any number seperated by space\n'\
                             '[press Enter when done or q to quit]: ')
        
        print()
        if numbers_string == '':
            print('Nothing typed?! Stop the program. ')
            break
        if numbers_string.upper() == "Q":
            print("Bye. Have a great day!")
            break
 
   
        # separate input via space  
        numbers_list=numbers_string.split()
        # 2.1. print the list.
        print('You typed the following in list: ' , numbers_list, '\n')      
               
        #2.2. print the sum of all numbers in list.
        print('*** Converting String to int and doing some calcuation below ***')
        sum = 0
        for number in numbers_list: 
            sum += int(number)
        print("- Sum of all numbers in list: ", sum)    
        
        #2.3. print number of elements in List
        # conver numbers in list into int
        numbers_list= [int(number) for number in numbers_list]   
        print("- Number of int elements in List: ", numbers_list)
        
        #2.4. print average in list
        # find length of list
        size=len(numbers_list)
        ave=sum/size
        print("- Average of all numbers in list:  ", ave)
        
        #2.5 find and print smallest value in list
        #2.6 find and print largest value in list
        n=1
        smallest = int(numbers_list[0])
        largest = int(numbers_list[0])
        while (n<size):
            if smallest > int(numbers_list[n]):
                smallest = int(numbers_list[n]) 
            if largest < int(numbers_list[n]):  
                largest = int(numbers_list[n])
            n+=1        
        print("- Smallest value in list is: " , smallest)
        print("- Largest value in list is: " , largest)
    # try ... except loop    
    except ValueError as error:
        print ('Hey, that was not an integer. Error message - ', error)    
        continue  # go back to the while statement
            