phase = input("Enter your word or phase: ")

num = False
numInPhase = 0

if(phase.isdigit()):
    print("All numbers")
    
else:
    for i in range(len.phase):#loop is supposed to check for numbers
        '''
        *start at first character in phase and check if it is a number
        *if it is a number set num to true and numInPhase to the number
        *if not check the next character and repeat
        '''
        if(num):
            print("Contains a " + str(numInPhase))
            
        num = False
        
    
    print("Does not contain numbers")
