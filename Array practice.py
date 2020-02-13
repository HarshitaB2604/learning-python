#****************FUNCTIONS****************
def printArrEBack(a):
  for i in range(len(a)-1, -1, -1):
    print(a[i])


# ***************MAIN*******************
letters = []

#102 is ASCII num for f and 119 ASCII num for w
for letter in range(102, 120):
	letters.append(chr(letter))

printArrEBack(letters)
