'''
Question 1: 5 points

Modified version of problem #414 from project Euler 
(https://projecteuler.net/problem=414)


6174 is a remarkable number; if we sort its digits in increasing order
and subtract that number from the number you get when you sort the digits
in decreasing order, we get 7641-1467=6174. Even more remarkable is that 
if we start from any 4 digit number and repeat this process of sorting and
subtracting, we'll eventually end up with 6174 or immediately with 0 if 
all digits are equal. This also works with numbers that have less than 4 
digits if we pad the number with leading zeroes until we have 4 digits.
E.g. let's start with the number 0837:
8730-0378=8352
8532-2358=6174

6174 is called the Kaprekar constant. The process of sorting and 
subtracting and repeating this until either 0 or the Kaprekar constant 
is reached is called the Kaprekar routine.

Write a Python program to calculate the number of steps to reach the 
Kaprekar constant for values 8730 and 9730.
'''
KAPREKAR_CONSTANT = 6174

def kaprekarCount(number):
    count = 0
    while True:
        number_list = list(str(number))
        number_list.sort()
        number_forward = ''.join(number_list)
        
        number_list.sort(reverse = True)
        number_backward = ''.join(number_list)
        print(number_forward, number_backward)
        number_forward_int =  int(number_forward)
        number_backward_int =  int(number_backward)
        if number_backward_int > number_forward_int:
            number = number_backward_int - number_forward_int
        else:
            number = number_forward_int - number_backward_int
        print(number)
        count = count+1
        if (number == KAPREKAR_CONSTANT) or (number == 0):
            break
    return count

nSteps = kaprekarCount(8730)
print('The number of steps to reach Kaprekar constant for 8370 is', nSteps)
nSteps = kaprekarCount(9730)
print('The number of steps to reach Kaprekar constant for 9370 is', nSteps)
userNumber = input('Please enter a 4 digit number: ')
userNumber = int(userNumber)
print(kaprekarCount(userNumber))

