x = 9 # number of rows
space = x - 1# num of spaces needed before printing the astriks

ast = 1 #num of astriks

print("THIRD")
for i in range(x):
    
    for y in range(space):
        print("  ", end = "")
    
    for j in range(ast):
        print("*", end=" ")
    
    space = space - 1
    ast = ast + 1
    print("")
