# Build count of words in a file

def removePunctuation(inputText):
    outputText = ''
    punctuationTuple = ('.', ',', '"', ";")
    for char in inputText:
        if char not in punctuationTuple:
            outputText = outputText + char

    return outputText

def findCount(inputList):
    uniqueList = list(set(inputList))
    uniqueList.sort()  # not required, but is a nice touch
    countDict = {}
    for word in uniqueList:
        countDict[word] = inputList.count(word)
    return countDict
    

def writeCountFile(csvFileName, theDict):
    fileHandle = open(csvFileName, 'w')
    for key, value in theDict.items():
        outputLine = key + ',' + str(value) + '\n'
        fileHandle.write(outputLine)
    fileHandle.close()
        
# Main code

# Open the file, read the contents, close the file
fileHandle = open('red-headed-league.txt', 'r') 
text = fileHandle.read()
fileHandle.close()

text = removePunctuation(text) # eliminate all punctuation

text = text.lower()  # ensure everything is lower case

wordsList = text.split()  # split into words

countDict = findCount(wordsList)  # get the count as a dict

writeCountFile('my2.csv', countDict)  # write the output file
print(countDict)
