'''
This program will stort the rows of a 2D array based on the first number in each array
'''

#***************Functions**************
def sort(array):
  #sorts the rows based on the 1st element in the row
  for i in range(len(array) - 1):
    for row in range(len(array) - 1):
      if(array[row + 1][0] < array[row][0]):
        temp = array[row]
        array[row] = array[row + 1]
        array[row + 1] = temp


def printAr(array):
  #prints the 2D array properly
  for r in range(len(array)):
    for c in range(len(array[0])):
      print(str(array[r][c]) + "\t", end = "")

    print("")


#**************Main***********
a = []
a.append([34, 38, 50, 44, 39])
a.append([42, 36, 40, 43, 44])
a.append([24, 31, 46, 40, 45])
a.append([43, 47, 35, 31, 26])
a.append([37, 28, 20, 36, 50])

sort(a)
printAr(a)
