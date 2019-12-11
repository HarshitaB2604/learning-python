word = input("Enter a word")
word = word.lower()

#determines if the password is long enough
if(len(word) < 8):
    print("Password not long enough.")

else:
    #only asks user for a number if their word for the pasword is long enough
    passnum = input("Enter a number")
    
    word = word.replace("e", "@")
    word = word.replace("s", "$")
    word = word.replace("t", "+")
    word = word.replace(" ", "")
    
    password = word.capitalize() + passnum
    print("Password: " + password)
