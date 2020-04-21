class Rectangle:
    num_rectangles = 0
    '''
    built-int methods
    '''
    #method to assign the lenght, width, and color of the rectangle
    def __init__(self, length = 0 , width = 0, color = "black"):
        self.length = length
        self.width = width
        self.color = color
        
        Rectangle.num_rectangles += 1

    #change the way the class prints
    def __repr__(self):
        return "Rectangle with length " + str(self.length) + \
            " and width " + str(self.width)
        
    #fix definition of objects being equal
    def __eq__(self, other):
        return self.width == other.width and \
            self.length == other.length
            
    #adds the widths and lengths of two recangles to get a new recangle
    def __add__(self, other):
        return Rectangle(self.length + other.length, self.width + other.width)
        
    #subtracts the widths and lengths of the recangles to get a new rectangle
    def __sub__(self, other):
        #subtracts the smaller of the widths from the other
        if(self.width < other.width):
            newWidth = other.width - self.width
        else:
            newWidth = self.width - other.width
        
        #subtracts the smaller of the lengths from the other
        if(self.length < other.length):
            newLength = other.length - self.length
        else:
            newLength = self.length - other.length

        return Rectangle(newWidth, newLength)

    '''
    additional methods
    '''   
    #method will calculate the area of the rectangle   
    def get_area(self):
        return self.length*self.width
        
    #method will calculate the perimeter of the rectangle
    def get_perimeter(self):
        return self.length*2 + self.width*2


print(Rectangle.num_rectangles)
rect1 = Rectangle(4, 6, "blue")
print(Rectangle.num_rectangles)
print(rect1.color)

rect2 = Rectangle(5, 9, "red")
print(Rectangle.num_rectangles)
print(rect2.color)

rect3 = Rectangle(5, 9)
print(Rectangle.num_rectangles)
print(rect3.color)
