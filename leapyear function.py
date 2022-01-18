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

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
