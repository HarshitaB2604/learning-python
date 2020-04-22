class Food:
    def __init__(self):
        #set default calorie count to 0 and have no category
        self.category = ""
        self.calories = 0
        
    def __repr__(self):
        return "category: " + self.category + \
            ", calories: " + str(self.calories) + ""
    

class Vegetable(Food):
    def __init__(self):
        #call init method for the superclass
        Food.__init__(self)
        
        #init of this class
        #change the category to veggies
        self.category = "veggies"
    
class Broccoli(Vegetable):
    def __init__(self):
        #call init method for the superclass
        Vegetable.__init__(self)
        
        #init of this class
        #change the calorie count
        self.calories = 100

        
#*****************MAIN****************
foodList = [Food(), Vegetable(), Broccoli(), 5]

#prints out the instance in the list if it is an instance of FOod or it's dub class
for inst in range(len(foodList)):
    if (isinstance(foodList[inst], Food)):
        print(foodList[inst])
    else:
        print(str(inst) + " is not a food")
