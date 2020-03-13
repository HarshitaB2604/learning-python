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
  newAr = ar
 
  for row in range(len(newAr)):
    switch = len(newAr[0]) - 1
    
    #flip the array horizontally
    for col in range(int(len(newAr[0])/2)):
      temp = newAr[row][col]
      newAr[row][col] = newAr[row][switch]
      newAr[row][switch] = temp
      switch = switch - 1

  #print the new Array
  printArray(newAr)

def flipVertical(ar):
  #flips the array vertically

  #make a copy of the array and process that
  newAr = ar
  
  switch = len(newAr) - 1
  
  '''
  if(len(newAr) % 2 == 1):
    for row in range(int((len(newAr) - 1)/2)):
      #swaps the top and bottom rows then moves closer to the center
      temp = newAr[row]
      newAr[row] = newAr[switch]
      newAr[switch] = temp
      switch = switch - 1
  else:
    for row in range(int(len(newAr) /2)):
      #swaps the top and bottom rows then moves closer to the center
      temp = newAr[row]
      newAr[row] = newAr[switch]
      newAr[switch] = temp
      switch = switch - 1
  '''
  #print the array
  printArray(newAr)

#******************MAIN***************

#5 X 5 array
a = []
a.append([0, 2, 0, 0, 0])
a.append([0, 2, 0, 0, 0])
a.append([0, 2, 2, 0, 0])
a.append([0, 2, 0, 2, 0])
a.append([0, 2, 0, 0, 2])

flipHorizontal(a)
print("\n\n")
flipVertical(a)
