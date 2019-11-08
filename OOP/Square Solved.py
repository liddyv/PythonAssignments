# Square class - text based
# Allows you to change set initial data, then change the data, and show the square as text
# Because of fonts, squares will probably not show as exactly square

class Square():
    """Represents a square
    """

    def __init__(self, size, hChar, vChar, cornerChar):
        ''' Initializes a square
        Pass in the size, the character to used for the horizontal edge, vertical edge, and corners.
        '''
        self.size = size
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        ''' Print the square in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''       
        print()
        # Build up two strings, using the characters specified, for the given size:
        #   topAndBottom represents the top and bottoms lines
        #   regularLine represents all the lines in between
        '''
        topAndBottom = self.cornerChar
        regularLine = self.vChar
        
        for i in range(0, self.size - 2):
            topAndBottom = topAndBottom + self.hChar
            regularLine = regularLine + ' '
        
        
        topAndBottom = topAndBottom + self.cornerChar
        regularLine = regularLine + self.vChar
        '''
        # OR
        
        topAndBottom = self.cornerChar + (self.hChar * (self.size - 2)) + self.cornerChar
        regularLine = self.vChar + (' ' * (self.size - 2)) + self.vChar             

        # Print the top line, all regular lines, and the bottom line
        print(topAndBottom)
        for i in range(0, self.size - 2):
            print(regularLine)
        print(topAndBottom)

    def getSize(self):
        ''' Return the size of all edges of the square'''
        return self.size

    def getArea(self):
        ''' Return the area of the square'''
        area = self.size * self.size
        return area

    def setHorizontalChar(self, newHChar):
        ''' Set a new horizontal character '''
        self.hChar = newHChar
        
    def setVerticalChar(self, newVChar):
        ''' Set a new vertical character '''
        self.vChar = newVChar

    def setCornerChar(self, newCornerChar):
        ''' Set a new corner character '''
        self.cornerChar = newCornerChar

    def setSize(self, newSize):
        ''' Set a new edge size '''
        self.size = newSize


# Test code
# Create a square of size 5
oSquare1 = Square(5, '-', '|', '*')  # pass in size, horizonal, vertical, and edge characters
oSquare1.show()
print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())

# Create another square of size 10
oSquare2 = Square(10, '-', '|', '*')
oSquare2.show()
print('Size is:', oSquare2.getSize(), " area is:", oSquare2.getArea())

'''
# Tell the first square to modify its data
oSquare1.setSize(7)
oSquare1.setHorizontalChar('^')
oSquare1.setVerticalChar('?')
oSquare1.setCornerChar('$')
oSquare1.show()
print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())
print()

# Add code here to ask the user questions (about size, horizontal, vertical and corner char's)
userSize = input('What is the (integer) size of an edge? ')
userSize = int(userSize)  # convert to integer
userHChar = input('What should we use for the horizontal character? ')
userVChar = input('What should we use for the vertical character? ')
userCChar = input('What should we use for the corner character? ')

# Then create and show a new Square (oSquare3) based on the user's answers
oSquare3 = Square(userSize, userHChar, userVChar, userCChar)
oSquare3.show()

# Finally, show the new square's size and area with this line:
print('Size is:', oSquare3.getSize(), " area is:", oSquare3.getArea())
'''
