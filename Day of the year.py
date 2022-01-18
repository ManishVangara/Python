def isYearLeap(year):

    if year < 1582:
        print("Not within the Gregorian calendar period!")
        return False
    elif year % 4 != 0 :
        print("Common year")
        return False
    elif year % 100 == 0  and year % 400 == 0 :
        print('This is a centurial leap year')
        return True
    elif year % 100 == 0 and year % 400 != 0 :
        print("This is a centurial year but not a leap year")
        return False
    else :
        print('This is a leap year')
        return True

def daysInMonth(year, month):
    numDaysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

    if year < 1582 and month < 1 or month > 12 :
        return None
    elif isYearLeap(year) and month == 2 :
        return 29
    else :
        return numDaysInMonth [month-1]

def dayofYear(year,month,day):
    #Validate Input
    if year < 1582 :
        return None
    if month > 12 or month < 1 :
        return None
    if day > 31 or day < 1 :
        return None

    # Calculate days 
    totalDays = day
    month = month -1 
    while month > 0 :
        totalDays += daysInMonth(year,month)
        month -= 1
    
    return totalDays