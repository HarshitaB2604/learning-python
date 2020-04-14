import random

class NameHat():
    #create empt hat of names
    def __init__(self):
        self.hat = []
    
    #prints the names in the hat
    def __repr__(self):
        names = ""
        for i in range(len(self.hat)):
            names = names + self.hat[i] + "\n"
            
        return names
    
    def insert_name(self, n):
        while True:
            try:
                found = self.hat.index(n)
                break
            except ValueError:
                found = -1
                break
            
        if(found == -1):
            self.hat.append(n)


name = NameHat.insert_name("Honey")


print(name)
