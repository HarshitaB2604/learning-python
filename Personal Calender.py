#****************************FUNCTIONS*************************
def addEvent(name, month, day, year):
  #adds an event to the personal calender


def printEvents(arrayName, arrayMonth, arrayDay, arrayYear):
  #takes in the four arrays and prints thier contents

def printMonth(monthNum, arrayName, arrayMonth, arrayDay, arrayYear):
  #prints the events in a specific month


#other supporting functions
def leap_year(y):
  #determins if the year is a leap year

  if(y % 4 == 0):
    return 1
  else:
    return 0

def checkDays(month, leap):
  #determines the number of days in the month

  if(month < 8 and month % 2 == 1):
    numofDays = 31
  elif(month < 8 and month % 2 == 0 and month != 2):
    numofDays = 30
  elif(month >= 8 and month % 2 == 0):
    numofDays = 31
  elif(month >= 8 and month % 2 == 1):
    numofDays = 30
  else:
    #the number of days in feb in a leap year
    if(leap == 1):
      numofDays = 29
    #the number of days in feb in a normal year
    else:
      numofDays = 28
    
  return numofDays

#****************************MAIN***************************

#the arrays
eventName = []
eventMonth = []
eventDay = []
eventYear = []

#Code
#add the events
event = ""
while(event != "no"):
  addEvent(eventName, eventMonth, eventDay, eventYear)
  event = "Do you want to enter another date? no to stop."

#print the events
print("******************** List of Events ********************")

#print events in a specific month
print()

