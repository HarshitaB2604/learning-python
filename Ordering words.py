word1 = input("First word: ")
word2 = input('Second word: ')

#tesing which word comes first alphabetically then 
#prints the words in alphabetically order in upper case

if(word1 < word2):  
    print(str(word1.upper()) + "\n" + str(word2.upper()))
else:
    print(str(word2.upper()) + "\n" + str(word1.upper()))
   
