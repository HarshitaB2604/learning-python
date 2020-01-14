import math

#calculates the GPA
def GPAcalc(g, weight):
    g = g.upper()
    if(g == "A"):
        GPA = 4
    elif(g == "B"):
        GPA = 3
    elif(g == "C"):
        GPA = 2
    elif(g == "D"):
        GPA = 1
    elif(g == "F"):
        GPA = 0
    
    #if the string entered in is not a letter grade it returns Invalid
    else:
        GPA = "Invalid"
    
    #adds the weight to the GPA
    if(GPA != "Invalid" and weight == 1):
        GPA = GPA + 1
    
    print("Your GPA score is: " + str(GPA))
    
    return GPA


#finds the total GPA
def classTotal(num):    
    
    GPAsum = 0
    
    for x in range(num):
        grade = input("Enter your Letter Grade: ")
        weighted = int(input("Is the class weighted? (1 = yes, 0 = no) "))
        
        GPAsum = GPAsum + GPAcalc(grade, weighted)
    
    GPAtotal = (GPAsum/num)*1.0
    
    return GPAtotal
   
#*********MAIN********#
classNum = int(input("How many classes are you taking"))


#prints your GPA
print("\nYour GPA weight is a " + str(classTotal(classNum)) + ".")
