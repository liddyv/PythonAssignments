# Square class - text based
# Allows you to set initial data, then change the data, and show the square as text
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
  
    def make_row(self, size, hChar, vChar, cornerChar):
        return cornerChar*(size>0) + hChar*(size-2) + cornerChar*(size>1)
            
    def make_square(self, size, hChar, vChar, cornerChar):
        #create the first and the last row
        top_row = self.make_row(size, hChar, vChar, cornerChar)
        #create the middle row
        mid_row = self.make_row(size, ' ', ' ', vChar)
        #combine [top_row] list*1  + [mid_row] list*(height-2) + [top_row] list*1 
        rows_list = [top_row]*(size>0) + [mid_row]*(size-2) + [top_row]*(size>1)
        #display items in the list line by line
        square = '\n'.join(rows_list)
        return square

    def show(self):
        ''' Print the square in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''       
        print()
        # draw this Square
        print(self.make_square(self.size, self.hChar, self.vChar, self.cornerChar))

    def getSize(self):
        ''' Returns the size of an edge of the Square '''
        return self.size

    def setHorizontalChar(self, newHChar):
        ''' Sets a new horizontal character '''
        self.hChar = newHChar
        
    def setVerticalChar(self, newVChar):
        ''' Sets a new vertical character '''
        self.vChar = newVChar

    def setCornerChar(self, newCornerChar):
        ''' Sets a new corner character '''
        self.cornerChar = newCornerChar

    # Must add 2 additional methods: setSize and getArea
    def setSize(self, newSize):
        self.size = newSize
        
    def getArea(self):
        return self.size * self.size
        #return size * size # NameError: name 'size' is not defined


# Test code
# Create a square of size 5
oSquare1 = Square(5, '-', '|', '*')  # pass in size, horizonal, vertical, and edge characters
oSquare1.show()

print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())

# Create another square of size 10
oSquare2 = Square(10, '-', '|', '*')
oSquare2.show()
print('Size is:', oSquare2.getSize(), " area is:", oSquare2.getArea())

# Tell the first square to modify its data, and print
oSquare1.setSize(7)
oSquare1.setHorizontalChar('^')
oSquare1.setVerticalChar('?')
oSquare1.setCornerChar('$')
oSquare1.show()
print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())
print()


# Add code here to ask the user questions (about size, horizontal, vertical and corner char's)
size = int(input('What is the (integer) size of an edge? '))
hChar = input('What should we use for the horizontal character? ')
vChar = input('What should we use for the vertical character? ')
cChar = input('What should we use for the corner character? ')

# Then create and show a new Square (oSquare3) based on the user's answers
oSquare3 = Square(size, hChar, vChar, cChar)
oSquare3.show()

# Finally, show the new square's size and area with this line:
print('Size is:', oSquare3.getSize(), " area is:", oSquare3.getArea())


