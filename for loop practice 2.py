x = 10 # number of rows

print("FOURTH")
for i in range(x):
    for j in range(x - i):# loops determines the number of astriks in the row
        print("*", end=" ") 
    print("")
    for y in range(x - j): # alines to the right
        print("  ", end = "")
