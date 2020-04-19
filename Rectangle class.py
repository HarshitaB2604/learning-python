class Rectangle:
    '''
    built-int methods
    '''
    #method to assign the lenght and width of the reactangle
    def __init__(self, length = 0 , width = 0):
        self.length = length
        self.width = width

    #change the way the class prints
    def __repr__(self):
        return "Reactangle with length " + str(self.length) + \
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
    #method will calculate the area of the reactangle   
    def get_area(self):
        return self.length*self.width
        
    #method will calculate the perimeter of the reactangle
    def get_perimeter(self):
        return self.length*2 + self.width*2


rect1 = Rectangle(4, 6)
rect2 = Rectangle(5, 9)
rect3 = Rectangle(5, 9)
print(str(rect1) + "\n" + str(rect2) + "\n" + str(rect3))

rect4 = rect1 + rect2
print(rect4)
rect5 = rect3 - rect1
print(rect5)
