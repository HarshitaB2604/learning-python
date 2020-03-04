import random

#4 X 5 array
numbers = []
for i in range(4):
  numbers.append([])
  
for r in range(len(numbers)):
  for c in range(5):
    #add random numbers between -30 and 30 to the array
    numbers[r].append(random.randint(-30, 30))

for r in range(len(numbers)):
  for c in range(5):
    print(str(numbers[r][c]) + " ", end = "")

  print("")
