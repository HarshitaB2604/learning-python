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

# --------------------------MAIN FUNCTION----------------------------------


def get_guess():
    # get the guess from the user
    guessL = create_list()

    lenght = True
    list_range = True
    dubble_num = True
    # repeat everything until guess meets all conditions
    while(lenght and list_range and dubble_num):
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


print(get_guess())
