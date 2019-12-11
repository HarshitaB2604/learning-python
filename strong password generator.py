word = input("Enter a word")
word = word.lower() # makes everything in lower case so it is easier to compare

#determines if the password is long enough
if(len(word) < 8):
    print("Password not long enough")

else:
    #only asks user for a number if their word for the pasword is long enough
    passnum = input("Enter a number")
    
    #replace certain chracters with others to make a strong password
    word = word.replace("e", "@")
    word = word.replace("s", "$")
    word = word.replace("t", "+")
    
    password = word.capitalize() + passnum
    #prints out the final strong passowrd
    print(password)
