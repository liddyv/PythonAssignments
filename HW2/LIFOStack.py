# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:59:50 2019
@Home work #2, Question 1 - Stacks
@Description: A stack follows LIFO (last-in, first-out). 
- Start with a list with values [7, 1, 2, 3]. 
- Create functions stackadd and stackretrieve to add and pop elements from the list in 
LIFO order respectively. 
- Add 5 to the stack. 
- pop one element at a time until the list is empty. 
- After each function call, print the contents of the list.
@author: Liddy Hsieh

"""

def stackadd(stackIn, element):
    #add elements to the end of the list
    stackIn.append(element)
    
    
def stackretrieve(stackIn):
    # pop element from the end of the list
    return stackIn.pop()    

#main loop
userStack = [7, 1, 2, 3] 
print(userStack)    
print('Add an element')   
stackadd(userStack, 5) #Add 5 to the stack.
print(userStack)

#pop one element at a time until the list is empty.
while len(userStack) > 0:
    print()
    print('Next value from the stack is: ', stackretrieve(userStack) )
    print('New contents are:', userStack)
