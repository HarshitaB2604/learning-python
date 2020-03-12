#*****************FUNCTIONS**************
def printIt(array):
  #prints the 2D array properly
  for r in range(len(array)):
    for c in range(len(array[0])):
      print(str(array[r][c]) + " ", end = "")

    print("")


#*****************Main**************
#4 X 5 array A
N = []
#set up 2D array
for i in range(4):
  N.append([])

#initilize to 1 2 3 4 5 in each row
for r in range(len(N)):
  for c in range(5):
    N[r].append(c+1)

printIt(N)

#4 X 5 array B
#initilize array B 
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
'''
for r in range(len(N)):
  for c in range(5):
    N[r][c] = r + 1

printIt(N)
