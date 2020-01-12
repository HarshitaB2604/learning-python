#function the GPA weighted
def GPAcalc(g):
    g = g.upper()
    if(g == "A"):
        GPA = 5
    elif(g == "B"):
        GPA = 4
    elif(g == "C"):
        GPA = 3
    elif(g == "D"):
        GPA = 2
    elif(g == "F"):
        GPA = 1
    
    #if the string entered in is not a letter grade it returns Invalid
    else:
        GPA = "Invalid"
    
    return GPA


#calcualtes the unweigted GPA
def GPAcalcUW(gU):    
    gU = gU.upper()
    if(gU == "A"):
        GPA = 4
    elif(gU == "B"):
        GPA = 3
    elif(gU == "C"):
        GPA = 2
    elif(gU == "D"):
        GPA = 1
    elif(gU == "F"):
        GPA = 0
    
    #if the string entered in is not a letter grade it returns Invalid
    else:
        GPA = "Invalid"
    
    return GPA
   
#*********MAIN********#
GPAsum = 0

classNum = int(input("How many classes are you taking"))
for i in range(classNum):
    
    #asks if the class is weighted
    grade = input("Enter your Letter Grade: ")
    weighted = int(input("Is the class weighted? (1 = yes, 0 = no) "))
    
    if (weighted == 1):
        GPAsum = GPAsum + GPAcalc(grade)
    
    else:
        GPAsum = GPAsum + GPAcalcUW(grade)
        
GPA =(GPAsum/classNum)*1.0
    
#prints your GPA
print("Your GPA weight is a " + str(GPA) + ".")
