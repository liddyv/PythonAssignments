
'''
Question 2: 5 points

https://en.wikipedia.org/wiki/Run-length_encoding

Implement an encoding scheme.

A string 
WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW 
has 67 characters. Write a Python program to convert this string to 
12W1B12W3B24W1B14W. The new string is created
by calculating the number of times a characters appears consecutively and
placing the character next to it. The new string only needs 18 character,
thus compressing the original string by 73%.
'''

sampleString = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

def runLengthEncoder(inputString):
    currentLetter = inputString[0]
    count = 0
    outputString = ''

    for nextLetter in inputString:
        if nextLetter == currentLetter:
            count = count+1 
        else:
            outputString= outputString + str(count) + str(currentLetter)
            currentLetter = nextLetter
            #print currentLetter, outputString
            count = 1
    
    outputString= outputString + str(count) + str(currentLetter)
    return outputString

print()
print('Testing Run Length Encoder')
print(runLengthEncoder(sampleString))
userString = input('Enter any string: ')
print(runLengthEncoder(userString))


