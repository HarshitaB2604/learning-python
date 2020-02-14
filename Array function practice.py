import random

#**********FUNCTIONS***********
def buildArray(ar, val):
  #takes in a number and builds and arrays with that many values generated from random numbers

  for i in range(val):
    ar.append(random.randint(10, 99))

def sumArray(ar):
  sum = 0
  for i in range(len(ar)-1):
    sum = sum + ar[i]

  return sum  

#***********MAIN********
array = []

#asks for the number of values
num = int(input("How many values to add to the array: \n"))

#builds the array
buildArray(array, num)
print(array)

#find the sum
print("Total: " + str(sumArray(array)))
