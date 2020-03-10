'''
This program will flip a given 2D array by printing it backwards
'''
def flipIt(ar):
  #flips the array
  for r in range(len(array) - 1, -1, -1):
    for c in range(len(array[0])):
      print(str(array[r][c]) + " ", end = "")

    print("")
    
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
