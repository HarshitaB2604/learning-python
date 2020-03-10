'''
This progam will flip a given 2D array
'''
def flipIt(ar):
  #flips the array
  for row in range(len(ar)):
    switch = len(ar[0]) - 1
    
    for col in range(int(len(ar[0])/2)):
      temp = ar[row][col]
      ar[row][col] = ar[row][switch]
      ar[row][switch] = temp
      switch = switch - 1
    
def printAr(array):
  #prints the 2D array properly
  for r in range(len(array)):
    for c in range(len(array[0])):
      print(str(array[r][c]) + " ", end = "")

    print("")

#*******************MAIN*******************
array = []
#sets up the array
array.append(["@", " ", " ", " ", " ", "@"])
array.append(["@", "@", " ", " ", " ", "@"])
array.append(["@", " ", "@", " ", " ", "@"])
array.append(["@", " ", " ", "@", " ", "@"])
array.append(["@", " ", " ", " ", "@", "@"])
array.append(["@", " ", " ", " ", " ", "@"])

flipIt(array)
printAr(array)
