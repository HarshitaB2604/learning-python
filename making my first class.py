class Rectangle:
    
    #method to assign the lenght and width of the reactangle
    def __init__(self, length = 0 , width = 0):
        self.length = length
        self.width = width
        
        
rect = Rectangle(4, 6)
print(rect.length)
print(rect.width)
