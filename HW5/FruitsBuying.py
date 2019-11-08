# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:32:52 2019
# Assignment 2: Dictionary
Description: Write a program that allows any number of users (hint: "while" loop) 
to make purchases of any number of each item, and prints a detailed receipt.
# to iterate through all different foods in the top level dictionary
 for foodName in inventoryDict.keys() 
# Check inventory and give customers only what you have
# Don't print fruit in the receipt if buy 0 (Not buying)
# Add eggplant to inventory and make sure program works without any changes
@author: Liddy Hsieh
"""

fruitDic = {}

invDict = {'apples':{'price':.50, 'color':'red', 'amount':50},\
           'bananas':{'price':.60, 'color':'yellow', 'amount':100},\
           'cucumbers':{'price':.60, 'color':'green', 'amount':75},\
           'dates':{'price':.25, 'color':'brown', 'amount':250},\
           'eggplant':{'price':.100, 'color':'purple', 'amount':120},\
           'eggplant2':{'price':1.00, 'color':'purple', 'amount':120}}

while True:
    
    totalFruitPrice = 0 #reset for each user
    userName = input('Please enter your name, or press Enter to quit: ')
    if userName == '':
        break
        
    for foodName in invDict.keys():
        #print(foodName)
        oneFruitDict = invDict[foodName]
        # print(oneFruitDict) # i,e. {'price':.50, 'color':'red', 'amount':50}
        fruitSellPrice = float(oneFruitDict['price'])
        #print(fruitSellPrice)
        fruitColor = oneFruitDict['color']
        #print(fruitColor)
        fruitAmount = oneFruitDict['amount']
        #print(fruitAmount)
        
        numFruit = int( input( 'How many %s %s at %.2f each would you like to buy? ' %(fruitColor, foodName, fruitSellPrice)) )
        #check inventory
        if numFruit > fruitAmount:
            print('Sorry, we only have %d left' % fruitAmount)
            numFruit = fruitAmount
        
        # Calculate each fruit's sold price
        fruitSoldPrice = fruitSellPrice * float(numFruit)
        
        
        '''
        Create a list of dictionaries, where each dictionary represents the 
        purchase of a particular item. i.e. {'apples': [1, 0.5, 0.5], 
        'bananas': [2, 0.6, 1.2], 'cucumbers': [2, 0.6, 1.2], 'dates': [2, 0.25, 0.5]}
        '''
        fruitDic[foodName] =  [numFruit, fruitSellPrice, fruitSoldPrice]
    
        # decreate the fruite amount (Check this part)
        fruitAmount = fruitAmount - numFruit
        
        # Calcaulate total price
        totalFruitPrice += fruitSoldPrice
        
        # print sold price of each fruit
        print('OK. Those will cost $', fruitSoldPrice)

    print() 
    for foodName in fruitDic.keys():
        eachFruitDict = fruitDic[foodName]
        # print receipt - only bought items
        if (eachFruitDict[2] !=0):
            #    2 apples at 0.50 = 1.0
            print( '%d %s at %.2f = %.1f' %(eachFruitDict[0], foodName, eachFruitDict[1], eachFruitDict[2]) )
            
 
    #print(fruitDic)
    print()
    print( 'Total for %s is $%.2f ' %(userName, totalFruitPrice) )  
