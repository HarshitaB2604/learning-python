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
        return "Reactangle with length " + str(self.length) + " and width " + str(self.width)
    
    '''
    additional methods
    '''   
    #method will calculate the area of the reactangle   
    def get_area(self):
        return self.length*self.width
        
    #method will calculate the perimeter of the reactangle
    def get_perimeter(self):
        return self.length*2 + self.width*2


rect = Rectangle(4, 6)
print(rect)

rect2 = Rectangle()
print(rect2)
