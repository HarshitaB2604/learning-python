import copy
#***************FUNTIONS**************
def printArray(array):
  #prints the 2D array properly
  for r in range(len(array)):
    for c in range(len(array[0])):
      print(str(array[r][c]) + " ", end = "")

    print("")

def flipHorizontal(ar):
  #flips the array horizontally

  #make a copy of the array and process that
  newArH = copy.deepcopy(ar)
 
  for row in range(len(newArH)):
    switch = len(newArH[0]) - 1
    
    #flip the array horizontally
    for col in range(int(len(newArH[0])/2)):
      temp = newArH[row][col]
      newArH[row][col] = newArH[row][switch]
      newArH[row][switch] = temp
      switch = switch - 1

  #print the new Array
  printArray(newArH)

def flipVertical(ar):
  #flips the array vertically

  #make a copy of the array and process that
  newArV = copy.deepcopy(ar)
  
  switch = len(newArV) - 1
  
  
  if(len(newArV) % 2 == 1):
    for row in range(int((len(newArV) - 1)/2)):
      #swaps the top and bottom rows then moves closer to the center
      temp = newArV[row]
      newArV[row] = newArV[switch]
      newArV[switch] = temp
      switch = switch - 1
  else:
    for row in range(int(len(newArV) /2)):
      #swaps the top and bottom rows then moves closer to the center
      temp = newArV[row]
      newArV[row] = newArV[switch]
      newArV[switch] = temp
      switch = switch - 1
  
  #print the array
  printArray(newArV)

#******************MAIN***************

#5 X 5 array
a = []
a.append([0, 2, 0, 0, 0])
a.append([0, 2, 0, 0, 0])
a.append([0, 2, 2, 0, 0])
a.append([0, 2, 0, 2, 0])
a.append([0, 2, 0, 0, 2])

ar = a
flipHorizontal(a)
print("\n\n")
flipVertical(a)
