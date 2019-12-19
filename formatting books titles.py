'''
* this program takes in the title of a book, the authors first and last name from the user until the user types STOP
  and stores it in a file it creats
* then it print out each line with the book title in upper case along with the authors last name, first name capitilized 
'''
# Saving filepath to a variable
# makes a smoother transition to the Sandbox
filepath = "books.txt"

# When finished copy all code after this line into the Sandbox
# Open the file
outFile = open (filepath, 'w') 

# Write your program below
title = input("Enter a title of a book. Enter STOP to stop ")
authorF = input("Enter the first name of the author ")
authorL = input("Enter the last name of the author ")

while(title != 'STOP'):
  #formats the tile and the authors name to store it in one line
  outFile.write(title.upper() + "\t" + authorL.capitalize() + ", " + authorF.capitalize() + "\n")

  title = input("Enter a title of a book. Enter STOP to stop ")
  if(title != 'STOP'):
    authorF = input("Enter the first name of the author ")
    authorL = input("Enter the last name of the author ")

outFile.close()

#printing the books
inFile = open('books.txt', 'r')

line = inFile.readline()
while(line):
  print(line)
  line = inFile.readline()

inFile.close()
