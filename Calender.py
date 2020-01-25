#determines if the year is a leap Year
def leap_year(y):
  if(y % 4 == 0):
    return 1
  else:
    return 0

#determines the number of days in the month
def number_of_days(month, leap):
  #if the user enters a invalid month number print an error message
  if(month < 1 or month > 12):
    print("Invalid value. Please restart")
  else if(month >= 8 and month % 2 == 1):
    numOfDay = 31
  else if(month > 8 and month % 2 == 0 and month != 2):
    numOfDay = 30
  else if(month < 8 and month % 2 == 0):
    numOfDay = 31
  else if(month < 8 and month % 2 == 1):
    numOfDay = 30
  else:
    if(leap == 1):
      numOfDay = 29
    else:
      numOfDay = 28
    

  return numOfDays


#*****MAIN*****#
day = int(input("Please enter a date\nDay: "))
month = int(input("Month: "))
year = int(input("Year: "))

#gives the user the menu
