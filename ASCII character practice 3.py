'''
* takes an input from the user
* If the input is a character then the program prints its ASCII number
* if the input is not a character the program prints Not a character

asciichar = input("Enter a character: ")

if(len(asciichar) == 1):
   print("ASCII #" + str(ord(asciichar)))

else:
   print("Not a character")
