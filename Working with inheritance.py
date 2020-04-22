class Food:
    def __init__(self):
        self.category = ""
        self.calories = 0
        
    def __repr__(self):
        return "category: <" + self.category + \
            ">, calories: <" + str(self.calories) + ">"
    

class Vegetable(Food):
    def __init__(self):
        #call init method for the superclass
        Food.__init__(self)
        
        #init of this class
        self.category = "veggies"
    
class Broccoli(Vegetable):
    def __init__(self):
        #call init method for the superclass
        Vegetable.__init__(self)
        
        #init of this class
        self.calories = 100
        
#*****************MAIN*******************
        
br = Broccoli()
print(br)
