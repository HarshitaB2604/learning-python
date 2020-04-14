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
        names = ""
        for i in range(len(self.hat)):
            names = names + self.hat[i] + "\n"
            
        return names
    
    #adds a name to the hat if it isn't already there
    def insert_name(self, n):
        if(find(self.hat, n) == -1):
            self.hat.append(n)


names = NameHat()
names.insert_name("John")

print(names)
