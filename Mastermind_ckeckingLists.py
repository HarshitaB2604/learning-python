import random

computer_list = [1, 2, 3, 5]
user_list = [1, 2, 3, 5]


def check_values(num_arry, guesses):
    # will hold the key colors that will be returned
    key = []

    # loops to
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

    return check_win(key)


def check_win(response_list):
    count = 0
    for i in range(len(response_list)):
        if(response_list[i] == "RED"):
            count += 1

    if(count == 4):
        return "YOU WON! :)"
    else:
        return "SORRY, YOU LOST :("


print(check_values(computer_list, user_list))
