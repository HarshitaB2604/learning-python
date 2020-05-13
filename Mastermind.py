import random

def create_comp_list():
    li = []
    #create a list
    for i in range(4):
        li.append(random.randint(1, 7))
    
    #go through each number to make sure it's unique 
    for inst in range(len(li)):
        for j in range(len(li)):
            if(li[inst] == li[j] and inst != j):
                li[j] = random.randint(1, 7)

    return li
    
def get_guess():
    guessL = []
    #set up answer
    actual = create_comp_list()
    
    #take a guess
    guess = input("Enter 4 numbers as guesses: ")
    
    #check the lenght of the guess is only 4 numbers
    while(len(guess) != 4):
        print("Your guess must consist of 4 numbers!")
        guess = input("Enter 4 numbers as guesses: ")
    
    #change the guess into a list
    for i in range(len(guess)):
        guessL.append(guess[i])
        
    #check if any number is greater than 7 or less than 1
    for i in range(len(guessL)):
        if(guessL[i] > 7 or guess[i] < 1):
            outOfRange = True
            break
        else:
            outOfRange = False
            break
    while(outOfRange):
        print("ou can only use numbers 1-7 as guesses!")
        guess = input("Enter 4 numbers as guesses: ")
        
        for i in range(len(guessL)):
            if(guessL[i] > 7 or guess[i] < 1):
                outOfRange = True
                break
            else:
                outOfRange = False
                break
        
print get_guess()
