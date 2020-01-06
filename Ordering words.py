word1 = input("First word: ").upper()
word2 = input('Second word: ').upper()

#tesing which word comes first alphabetically then 
#prints the words in alphabetically order in upper case

if(word1 < word2):  
    print(word1 + "\n" + word2)
else:
    print(word2 + "\n" + word1)
   
