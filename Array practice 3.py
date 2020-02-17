w = ["Algorithm", "Logic", "Filter", "Software", "Network", "Parameters", "Analyze", "Algorithm", "Functionality", "Viruses"]

s = []

#adds the lenght of each element to the s array
for i in range(len(w)):
  s.append(len(w[i]))

#prints out the lenght and the word
for x in range(len(w)):
  print(str(s[x]) + ": " + w[x])
