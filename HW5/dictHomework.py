# Optional dictionary homework

inventoryDict = {'apples':{'price':.50, 'color':'red', 'amount':50},\
          'bananas':{'price':.60, 'color':'yellow', 'amount':100},\
          'cucumbers':{'price':.60, 'color':'green', 'amount':75},\
          'dates':{'price':.25, 'color':'brown', 'amount':250}\
          }


while True:  # for each person

    userName = input('Please enter your name, or press Enter to quit: ')
    if userName == '':
        break

    userPurchaseList = []   # will hold the information about this user's purchases

    for foodName in inventoryDict.keys():        
        thisFoodDict = inventoryDict[foodName]  # dereference to get to the dict for this food
        thisPrice = thisFoodDict['price']
        thisColor = thisFoodDict['color']
        thisAmount = thisFoodDict['amount']

# Additional stuff for manipulating overall inventory
        if thisAmount == 0:
            print('Sorry, we do not have any more ' + thisColor + ' ' + foodName)
            continue
#

        question = 'How many ' + thisColor + ' ' + foodName + ' at ' + str(thisPrice) + ' each would you like to buy? '
        userAmount = input(question)
        userAmount = int(userAmount)

        if userAmount > 0:  # if the user purchased some of this food ...
# Check if we have enough
            if userAmount > thisAmount:
                print('Sorry, we only have ' + str(thisAmount) + ' left')
                userAmount = thisAmount
#
            subTotal = userAmount * thisPrice

            print('OK. Those will cost $' + str(subTotal))
            # Build a dictionary of the users amount, food, price, and subtotal, add to inventory list
            userPurchaseList.append({'amount': userAmount, 'food': foodName, 'price': thisPrice, 'subtotal': subTotal})

#   Change overall inventory
            thisFoodDict['amount'] = thisFoodDict['amount'] - userAmount
#
                
    # total and print receipt
    total = 0.0
    print()
    
    for itemDict in userPurchaseList:  # Iterate through user's list of purchases
        subTotal = itemDict['subtotal']  # convert to a number
        total = total + subTotal
        print(str(itemDict['amount']) + ' ' + itemDict['food'] + ' at ' + \
                str(itemDict['price']) + ' = ' + str(subTotal))

        
    print()
    print('Total for ' + userName + ' is $' + str(total))
    print()
    #print(inventoryDict)  # testing
    #print()

print('Bye')
        
        

    
    
                
                

           
