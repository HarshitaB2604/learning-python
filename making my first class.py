class Rectangle:

    #method to assign the lenght and width of the reactangle
    def __init__(self, length = 0 , width = 0):
        self.length = length
        self.width = width
    #method will calculate the area of the reactangle   
    def get_area(self):
        return self.length*self.width


rect = Rectangle(4, 6)
print(rect.length)
print(rect.width)
print("Area: " + str(rect.get_area()))

rect2 = Rectangle()
