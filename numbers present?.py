phase = input("Enter your word or phase: ")

num = False
numPlace = 0

if(phase.isdigit()):
    print("All numbers")
    
else:
    for i in range(9):#loop is supposed to check for numbers
        
        #finds if the phrase contains a certian number
        numPlace = phase.find(str(i))
        
        #only if a number in found change num to true
        if(numPlace != -1):
            num = True
        if(num):
            print("Contains a " + str(numInPhase))
            
        num = False
        
    
    print("Does not contain numbers")
