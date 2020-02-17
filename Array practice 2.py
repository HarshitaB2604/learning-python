w = ["Algorithm", "Logic", "Filter", "Software", "Network", "Parameters", "Analyze", "Algorithm", "Functionality", "Viruses"]


aWords = []
for i in range(len(w)):
  found = w[i][0].find("A")
  if(found == 0):
    aWords.append(w[i])

for word in range(len(aWords)):
  print(aWords[word])
