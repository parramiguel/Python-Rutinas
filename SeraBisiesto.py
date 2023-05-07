def isYearLeap(year):   # Leap year formula
    if year % 4 == 0 and year % 100 != 0 :     
        return True 
    elif year % 400 == 0 :
        return True
    else :
        return False
    
            
testData = [1900, 2000, 2016, 1987]         # Test Data as reference
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
def daysInMonth(year, month): # Finding out days in months in common & leap year
    days = 0
    mo31 = [1,3,7,5,8,10,12]
    if year % 4 == 0 :              
        days = 1
        if year % 100 == 0 :
            days = 0
        if year % 400 == 0 :
            days = 1
    if month == 2 :
        return 28 + days
    if month in mo31 :
        return 31
    return 30
testYears = [1900, 2000, 2016, 1987] # Test Data as reference 
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")      

