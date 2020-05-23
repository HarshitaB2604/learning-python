import random

# ---------------------------SUPPORT FUNCTIONS-------------------------------


def create_list():
    # remake the list
    ar = []
    guess = input("Enter 4 numbers as guesses: ")
    for i in range(len(guess)):
        ar.append(int(guess[i]))

    return ar


def check_range(li):
    # check if any of the numbers guessed are > 7 or < 1
    for i in range(len(li)):
        if(li[i] > 7 or li[i] < 1):
            outOfRange = True
            break
        else:
            outOfRange = False

    return outOfRange


def duplicate(ar):
    # check for duplicates in the list
    for inst in range(len(ar)):
        for j in range(len(ar)):
            if(ar[inst] == ar[j] and inst != j):
                dubble = True
                break
            else:
                dubble = False

        if(dubble):
            break

    return dubble

# --------------------------MAIN FUNCTIONS----------------------------------


def create_comp_list():
    # generates the actual list
    li = []
    # create a list
    for i in range(4):
        li.append(random.randint(1, 7))

    # go through each number to make sure it's unique
    for inst in range(len(li)):
        for j in range(len(li)):
            if(li[inst] == li[j] and inst != j):
                li[j] = random.randint(1, 7)

    return li


def get_guess():
    # get the guess from the user
    guessL = create_list()

    lenght = True
    list_range = True
    dubble_num = True
    # repeat everything until guess meets all conditions
    while(lenght or list_range or dubble_num):
      # check the lenght of the guess is only 4 numbers
        while(len(guessL) != 4):
            print("Your guess must consist of 4 numbers!")
            guessL = create_list()

            # reset loop variables if the list is changed
            list_range = True
            dubble_num = True

        lenght = False

        # check if any number is greater than 7 or less than 1
        while(check_range(guessL)):
            print("You can only use numbers 1-7 as guesses!")
            guessL = create_list()

            # reset loop variables if the list is changed
            lenght = True
            dubble_num = True

        list_range = False

        # check for dupilcates in the list
        while(duplicate(guessL)):
            print("You can only use each number once!")
            guessL = create_list()

            # reset the while loop variable if the list is changed
            lenght = True
            list_range = True

        dubble_num = False

    return guessL


def check_values(num_arry, guesses):
    # will hold the key colors that will be returned
    key = []

    for i in range(len(num_arry)):
        # this variable checks if the guess isn't in the generated list
        count = 0
        for j in range(len(num_arry)):
            # if the guess is correct and in the right spot
            if(num_arry[i] == guesses[j] and i == j):
                key.append("RED")
                break
            # if the guess is correct but not in the right spot
            elif(num_arry[i] == guesses[j] and i != j):
                key.append("WHITE")
                break
            # if the guess isn't in the generated list add 1 to the counter.
            # if the counter reaches 4 the number will not be in the list
            else:
                count += 1

        if(count == 4):
            key.append("BLACK")

    random.shuffle(key)
    print(key)

    return check_win(key)


def check_win(response_list):
    # checks if the guess is correct
    count = 0
    for i in range(len(response_list)):
        if(response_list[i] == "RED"):
            count += 1

    if(count == 4):
        return True
    else:
        return False


def play_game():
    comp_list = create_comp_list()
    for chance in range(5):
        guess = get_guess()
        check = check_values(comp_list, guess)

        # if the guess is correct
        if(check):
            print("You Won!")
            break

    # if the user still hasn't gotten the right guess
    if(check == False):
        print("Sorry you lost")
        print(comp_list)

#-------------------------------------Instructions-------------------------------------------------
print('''
Your goal is to successfully guess four numbers ranging from 1-7 in the
correct order. My secret numbers will be a set of four different values.
-----------------------------------------------------------------------
Each time you make a guess, I will give a color response of three options:
BLACK, RED, WHITE
BLACK = A number you guessed isn't one of the secret numbers.
WHITE = A number you guessed IS one of the secret numbers, but not in the PLACE where you guessed it
RED = A number you guessed IS one of the secret numbers, and IS where you guessed it.
The order of the colors is random. So even if you see RED in the third spot, it does NOT
mean that your third guess is in the correct place.
-----------------------------------------------------------------------
For example, my secret numbers are 4326.
For your guess, you might say four numbers: 3671.
You guessed two of the numbers correctly, but in the wrong order!
My reponse would be 'White' 'White' 'Black' 'Black'
Which indicates that you got two numbers correct, but not in the right
locations.
----------------------------------------------------------------------
If you had guessed 7316, my response would be
'Red' 'Red' 'Black' 'Black'
indicating that you guessed two numbers correct and in the right place,
and two incorrect numbers.
----------------------------------------------------------------------
''')

#-----------------------------GAME-------------------------------------------
play_game()
