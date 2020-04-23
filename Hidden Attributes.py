class Rectangle:
    """
    This class represents a rectangle. It
    has a length and a width and is capable
    of computing its own area.
    """
    #keeps track of rectangles with an even area
    __num_rectangles = 0
    
    def __init__(self, length = 0, width = 0):
        """
        Initializes a rectangle with an optional
        length and width.
        """
        self.length = length
        self.width = width
    
    def __repr__(self):
        """
        Returns a string representation of the
        rectangle.
        """
        return "rectangle with length: " + str(self.length) \
            + " and width: " + str(self.width)
    
    def get_area(self):
        """Returns the rectangle's area."""
        if((self.length * self.width)%2 == 0):
            Rectangle.__num_rectangles += 1
            return self.length * self.width
        else:
            return "Area is not an even value"


r1 = Rectangle(2, 6)
print r1
print r1.get_area()


r2 = Rectangle(3, 5)
print r2
print r2.get_area()
