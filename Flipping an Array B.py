'''
This program will flip the rows of a given 2D array. Change the order
'''
#*****************************FUNCTIONS*********************************
def flipIt(ar):
  #flips the array
  switch = len(ar) - 1
  for row in range(len(ar)):
    temp = ar[row]
    ar[row] = ar[switch]
    ar[switch] = temp
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
