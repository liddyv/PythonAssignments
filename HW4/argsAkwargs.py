# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 20:22:49 2019

@author: Liddy Hsieh
"""
def myFunction(*args, **kwargs):
    print('*** args ***')
    for arg in args:
        print(arg)
        
    print('== kwargs ==')
    for key, value in kwargs.items():
        print(key, value)

myFunction('alpha', 4, 25.4, True, key1='Python', haha2='is', keyword3='fun')

print()

def myTestFunctions(someVariable, someList1, someList2):
    someVariable=someVariable+1
    print('Value of someVariable', someVariable)
    someList1.append("Something was appended")
    someList2='Totally different value'

myVariable = 10
myList1=[1,2,3,4]
myList2=['a', 'b', 'c', 'd']    

myTestFunctions(myVariable, myList1, myList2)

print(myVariable)
print(myList1) # the original myList1 is changed after function (append). 
print(myList2) # The origianl myList2 NOT changed after function. 

        



