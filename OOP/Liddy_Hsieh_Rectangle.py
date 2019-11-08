# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:01:26 2019

@author: Liddy Hsieh

"""

# Rectangle class - text based
# Allows you to set initial data, then change the data, and show the Rectangle as text
# Because of fonts, rectangles will probably not show as exactly Rectangle

class Rectangle():
    """Represents a Rectangle
    """

    def __init__(self, height, width, hChar, vChar, cornerChar):
        ''' Initializes a Rectangle
        Pass in the height, width, the character to used for the horizontal edge, vertical edge, and corners.
        '''
        self.height = height
        self.width = width
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar
        
    '''
    def make_row(self, width, hChar, vChar, cornerChar):
        return cornerChar*(width>0) + hChar*(width-2) + cornerChar*(width>1)
            
    def make_rectangle(self, height, width, hChar, vChar, cornerChar):
        top_row = self.make_row(width, hChar, vChar, cornerChar)
        mid_row = self.make_row(width, ' ', ' ', vChar)
        #combine [top_row] list*1  + [mid_row] list*(height-2) + [top_row] list*1
        rows = [top_row]*(height>0) + [mid_row]*(height-2) + [top_row]*(height>1)
        rectangle = '\n'.join(rows)
        return rectangle
    '''

    def make_row(self, width, hChar, vChar, cornerChar):
        return ( cornerChar*(width>0) + hChar*(width-2) + cornerChar*(width>1) )
            
    def make_rectangle(self):
        top_row = self.make_row(self.width, self.hChar, self.vChar, self.cornerChar)
        mid_row = self.make_row(self.width, ' ', ' ', self.vChar)
        #combine [top_row] list*1  + [mid_row] list*(height-2) + [top_row] list*1
        rows = [top_row]*(height>0) + [mid_row]*(height-2) + [top_row]*(height>1)
        rectangle = '\n'.join(rows)
        return rectangle

    def show(self):
        ''' Print the rectangle in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''       
        print()
        # draw this rectangle
        #print(self.make_rectangle(self.height, self.width, self.hChar, self.vChar, self.cornerChar))
        print(self.make_rectangle())

    def getWidth(self):
        ''' Returns the size of an edge of the Rectangle '''
        return self.width
    
    def getHeight(self):
        ''' Returns the size of an edge of the Rectangle '''
        return self.height

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
    def setWidth(self, newWidth):
        self.width = newWidth
        
    def setHeight(self, newHeight):
        self.height = newHeight    
        
    def getArea(self):
        return self.width * self.height
    
    

# Test code
# Create a rectangle of height 10, width 5
oRectangle1 = Rectangle(10, 5, '-', '|', '*')  # pass in size, horizonal, vertical, and edge characters
oRectangle1.show()
print('Width is:', oRectangle1.getWidth(), ' Height is:', oRectangle1.getHeight(), " area is:", oRectangle1.getArea())


# Create another rectangle of height 8, width 2
oRectangle2 = Rectangle(8, 2, '-', '|', '*')
oRectangle2.show()
print('Width is:', oRectangle2.getWidth(), ' Height is:', oRectangle2.getHeight(), " area is:", oRectangle2.getArea())

# Tell the first rectangle to modify its data, and print
oRectangle1.setWidth(7)
oRectangle1.setHeight(12)
oRectangle1.setHorizontalChar('^')
oRectangle1.setVerticalChar('?')
oRectangle1.setCornerChar('$')
oRectangle1.show()
print('Width is:', oRectangle1.getWidth(), ' Height is:', oRectangle1.getHeight(), " area is:", oRectangle1.getArea())
print()


# Add code here to ask the user questions (about size, horizontal, vertical and corner char's)
height = int(input('What is the (integer) height of an edge? '))
width = int(input('What is the (integer) width of an edge? '))
hChar = input('What should we use for the horizontal character? ')
vChar = input('What should we use for the vertical character? ')
cChar = input('What should we use for the corner character? ')

# Then create and show a new rectangle (orectangle3) based on the user's answers
oRectangle3 = Rectangle(height, width, hChar, vChar, cChar)
oRectangle3.show()

# Finally, show the new rectangle's size and area with this line:
print('Width is:', oRectangle3.getWidth(), ' Height is:', oRectangle3.getHeight(), " area is:", oRectangle3.getArea())


