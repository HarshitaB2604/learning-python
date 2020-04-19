import random

def find(ar, val):
    while True:
        try:
            found = ar.index(val)
            break
        except ValueError:
            found = -1
            break
        
class NameHat():
    #create empt hat of names
    def __init__(self):
        self.hat = []
    
    #prints the names in the hat
    def __repr__(self):
        ar = ""
        for i in range(len(self.hat)):
            ar = ar + self.hat[i] + " "
            
        return ar
    
    #adds a name to the hat if it isn't already there
    def insert_name(self, n):
        #checks if the name is already in the array
        while True:
            try:
                found = self.hat.index(n)
                break
            except ValueError:
                found = -1
                break
        
        if(found == -1):
            self.hat.append(n)
    
    #removes a random name from name hat
    def draw_name(self):
        val = random.choice(self.hat)
        return self.hat.remove(val)
        



names = NameHat()
names.insert_name("John")
names.insert_name("Bob")
names.insert_name("Rose")
names.insert_name("Lily")
names.insert_name("Mira")
names.insert_name("John")

print(names)
print("\n")
names.draw_name()
print(names)
