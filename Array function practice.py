import random

#**********FUNCTIONS***********
def buildArray(ar, val):
  #takes in a number and builds and arrays with that many values generated from random numbers

  for i in range(val):
    ar.append(random.randint(0, 99))

#***********MAIN********
array = []

#asks for the number of values
num = int(input("How many values to add to the array: \n"))

buildArray(array, num)
print(array)
