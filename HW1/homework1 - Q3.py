
def runLengthEncoder(inputString):   #  From question 2
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



def runLengthDecoder(inputString):
    outputString = ''

    currentCount = ''
    for char in inputString:
        if char.isdigit():
            currentCount = currentCount + char
        else:
            nTimes = int(currentCount)
            outputString = outputString + (nTimes * char)
            currentCount = ''
            
    return outputString  
        
print()
print('Testing Run Length Decoder')
print(runLengthDecoder('12W1B12W3B24W1B14W'))
userString = input('Enter an encoded string: ')
print(runLengthDecoder(userString))


print()
print('Testing Run Length Encoder/Decoder')
print(runLengthDecoder(runLengthEncoder('This should be the staaaaaaarting string!!!')))

