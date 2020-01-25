#determines if the year is a leap Year
def leap_year(y):
  if(y % 4 == 0):
    return 1
  else:
    return 0

#determines the number of days in the month
def number_of_days(month, leap):
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
      numOfDays = 28
    
  return numofDays

#calculates the number of days left in the year
def days_left(d, m, leap): #asks for day, month, and wheater its a leap year
    #calculate the days in the monhts left
    days_in_months = 0
    for monthNum in range(m+1, 13):
        days_in_months = days_in_months + number_of_days(monthNum, leap)

    #calculate the days left in the currect month
    days_in_month = number_of_days(m, leap) - d #subtract the total days in this month by that date

    daysLeft = days_in_month + days_in_months
    
    return daysLeft
''''
******************************MAIN********************************
'''
day = int(input("Please enter a date\nDay: "))

#only if the day is a valid number, between 1 and 31 will it let the user continue
#otherwise it prints and error message and keeps promting them to enter a valid day
while(day < 1 or day > 31):
  print("Error: Please enter a valid day of the month")
  day = int(input("Please enter a date\nDay: "))

month = int(input("Month: "))
#makes it so the user enters a valid month
while(month < 1 or month > 12):
  print("Error. Please enter a valid month number")
  month = int(input("Month: "))

year = int(input("Year: "))



#gives the user the menu
menu = int(input("Please choose an option from the menu \nMenu:\n1)\tCalculate the number of days in the given month.\n2)\tCalculate the number of days left in the given year. \n"))

#routes the patch for the certain menu choice or return Invalid if it is not one of the choices
while(menu < 1 or menu > 2):
  print("Invalid. Please choose an option from the Menu")
  
  #gives the user the menu
  menu = int(input("Please choose an option from the menu \nMenu:\n1)\tCalculate the number of days in the given month.\n2)\tCalculate the number of days left in the given year. \n"))

#calculates the days in the month if the user chose 1
if(menu == 1):
    #run the number of days function and use the month and the value from the leap year function incase month is feb
    print(number_of_days(month, leap_year(year)))

else:
    print(days_left(day, month, leap_year(year)))
