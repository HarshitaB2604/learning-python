#function calculates the GPA value
def GPAcalc(g):
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
    
    return GPA
    
'''
Main
'''
grade = input("Enter your letter grade: ")

#prints your GPA
print("Your GPA score is: " + str(GPAcalc(grade)))
