word = input("Enter a word")

#determines if the password is long enough
if(len(word) < 8):
    print("Password not long enough.")

else:
    #only asks user for a number if their word for the pasword is long enough
    passnum = input("Enter a number")
    
    word = word.replace("e", "@")
    
    #makes the word lower case after recplacing all the e's
    word = word.lower()
    word = word.replace("s", "$")
    word = word.replace("t", "+")
    
    password = word.capitalize() + passnum
    print("Password: " + password)
