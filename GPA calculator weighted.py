#function calculates the GPA value
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
    
    if(GPA != "Invalid" and weight == 1):
        GPA = GPA + 1
    
    return GPA
    
'''
Main
'''
grade = input("Enter your letter grade: ")
weighted = int(input("Is it weighted? (1 = yes, 0 = no) "))

#prints your GPA
print("Your GPA score is: " + str(GPAcalc(grade, weighted)))
