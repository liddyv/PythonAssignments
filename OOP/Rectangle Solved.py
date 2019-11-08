# Rectangle class - text based
#
# Changes:
# - Class name Rectangle -> Rectangle
# - Change __init__ to accept width, height instead of size, save both
# - Show method
#      First loop must go from 0 to self.width - 2
#      Second loop must go from 0 to self.height - 2
# - Remove getSize, add getWidth, getHeight
# - Remove setSize, add setSize, setHeight
# - Change area calculation in getArea
#
# Allows you to set initial data, then change the data, and show the rect as text
# Because of fonts, Rectangles will probably not show as exactly Rectangle (you can use Courier if you wish)

class Rectangle():
    """Represents a Rectangle
    """

    def __init__(self, width, height, hChar, vChar, cornerChar):
        ''' Initializes a Rectangle
        Pass in the size, the character to used for the horizontal edge, vertical edge, and corners.
        '''
        self.width = width
        self.height = height
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        ''' Print the Rectangle in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''       
        print()
        topAndBottom = self.cornerChar
        regularLine = self.vChar
        
        for i in range(0, self.width - 2):
            topAndBottom = topAndBottom + self.hChar
            regularLine = regularLine + ' '

        topAndBottom = topAndBottom + self.cornerChar
        regularLine = regularLine + self.vChar
        #print(topAndBottom)
        #print(regularLine)
        
        
        print(topAndBottom)
        for i in range(0, self.height - 2):
            print(regularLine)
        print(topAndBottom)
        

    def getWidth(self):
        ''' Return the width of  the rect'''
        return self.width

    def getHeight(self):
        ''' Return the height of the rect.'''
        return self.height

    def getArea(self):
        ''' Return the area of the rect'''
        area = self.width * self.height
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

    def setWidth(self, newWidth):
        ''' Set a new width size '''
        self.width = newWidth

    def setHeight(self, newHeight):
        ''' Set a new height '''
        self.height = newHeight



# Test code
# Create a Rectangle of size 5
oRectangle1 = Rectangle(4, 7, '-', '&', '*')  # pass in h, w, horizonal, vertical, and edge characters
oRectangle1.show()
print('Size is:', oRectangle1.getWidth(), "by", oRectangle1.getHeight(), " area is:", oRectangle1.getArea())

'''
# Create another Rectangle of size 10
oRectangle2 = Rectangle(20, 3, '-', '|', '*')
oRectangle2.show()
print('Size is:', oRectangle2.getWidth(), "by", oRectangle2.getHeight(), " area is:", oRectangle2.getArea())

# Tell the first Rectangle to modify its data
oRectangle1.setWidth(12)
oRectangle1.setHeight(3)
oRectangle1.setHorizontalChar('^')
oRectangle1.setVerticalChar('?')
oRectangle1.setCornerChar('$')
oRectangle1.show()
print('Size is:', oRectangle1.getWidth(), "by", oRectangle1.getHeight(), " area is:", oRectangle1.getArea())
print()

# Add code here to ask the user questions, and create and show a new Rectangle based on the answers
userWidth = input('What is the (integer) width? ')
userWidth = int(userWidth)
userHeight = input('What is the (integer) height? ')
userHeight = int(userHeight)
userHChar = input('What should we use for the horizontal character? ')
userVChar = input('What should we use for the vertical character? ')
userCChar = input('What should we use for the corner character? ')
oRectangle3 = Rectangle(userWidth, userHeight, userHChar, userVChar, userCChar)
oRectangle3.show()
print('Size is:', oRectangle3.getWidth(), "by", oRectangle3.getHeight(), " area is:", oRectangle3.getArea())

'''
