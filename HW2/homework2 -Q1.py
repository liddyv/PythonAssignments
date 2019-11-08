'''
A stack follows LIFO (last-in, first-out). LIFO is the case where the last  
element added is the first element  that can be retrieved. 
Consider a list with values [7, 1, 2, 3]. Create functions stackadd and 
stackretrieve to add and pop elements from the list in LIFO order 
respectively. Add 5 to the queue. Follow the LIFO rules to pop 
one element at a time until the list is empty. After each function call, 
print the contents of the list.

'''


def stackAdd(myStack, item):
    # Lists are mutable, so original will be changed
    myStack.append(item)
    

def stackRetrieve(myStack):
    # Lists are mutable, so original will be changed
    element = myStack.pop()
    return element

stack1 = [7, 1, 2, 3]
print(stack1)
print("Add an element")
stackAdd(stack1, 5)
print(stack1)


while True:
    if len(stack1) == 0:
        break
    print()
    item = stackRetrieve(stack1)
    print("Next value from the stack is:", item)
    print("New contents are:", stack1)
    
