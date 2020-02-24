#****************************FUNCTIONS*************************
def addEvent(name, month, day, year):
  #adds an event to the personal calender
  nameInput = input("What is the event: ")
  monthInput = int(input("What is the month (number): "))
  dayInput = int(input("What is the date: "))
  yearInput = int(input("What is the year: "))

  #checks if the month number is valid
  if(monthInput < 1 or monthInput > 12):
    monthInput = 1
  
  #checks if the day input is invalid
  #finds the number of days in the months entered
  daysInMonth = checkDays(monthInput, leap_year(yearInput))
  if(dayInput > daysInMonth):
    dayInput = 1

  #adds the event to the arrays
  name.append(nameInput)
  month.append(monthName(monthInput))
  day.append(str(dayInput))
  year.append(str(yearInput))

'''
def printEvents(arrayName, arrayMonth, arrayDay, arrayYear):
  #takes in the four arrays and prints thier contents
  for name in range(len(arrayName)):
    print(arrayName[name])
    print("Date: " + arrayMonth[name] + arrayDay[name] + ", " + arrayYear[name])

def printMonth(monthNum, arrayName, arrayMonth, arrayDay, arrayYear):
  #prints the events in a specific month
  
'''

#other supporting functions
def monthName(num):
  if(num == 1):
    month = "January"
  elif(num == 2):
    month = "February"
  elif(num == 3):
    month = "March"
  elif(num == 4):
    month = "April"
  elif(num == 5):
    month = "May"
  elif(num == 6):
    month = "June"
  elif(num == 7):
    month = "July"
  elif(num == 8):
    month = "August"
  elif(num == 9):
    month = "September"
  elif(num == 10):
    month = "October"
  elif(num == 11):
    month = "November"
  else:
    month = "December"

  return month

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
while(event != "NO"):
  addEvent(eventName, eventMonth, eventDay, eventYear)
  event = input("Do you want to enter another date? NO to stop. ")

#print the events
print("******************** List of Events ********************")

#print events in a specific month
monthNum = int(input("What month would you like to see? (Enter the month number) "))
print("\n\n")
print("********** Events in " + monthName(monthNum) + " **********")

