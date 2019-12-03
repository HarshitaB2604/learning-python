x = 9 # number of rows

ast = 1

print("FIRST")
for i in range(x):
    for j in range(ast): # prints the number of astriks in the row depending on the row number
        print("*", end=" ")
    
    ast = ast + 1 # increments the number of astrikts in the row
    print("")
