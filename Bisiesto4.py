def dayOfYear(year, month, day):
    doy = ["Sat","Sun","Mon","Tue","Wed","Thu","Fri"] # Days of week
    monthvalue = [1,4,4,0,2,5,0,3,6,1,4,6]        # Months value zellers rule
    century = [1700,1800,1900,2000]      # Zellers rule 
    value = [4,2,0,6]   # Zellers rule
    rem = 0     # Remainder Variable
    r = []      # Empty List to compare remainder and to a doy
    y = str(year)   # Converting year into string
    y = int(y[2:4]) # Taking last two digits of string & if used return the function ends 
    y = int(year)   # here returning last two digits 
    m = int(month)
    d = int(day)
    mo = [] # Empty list for comparing month with monthly values
    dd = 0   
    if dd == 0 :
        for i in range(len(monthvalue)) :
            mo.append(i)    # Creating mo list
            if m in mo:
                mo[i] == monthvalue[i]
        dd = y // 4 + d + m 
    if m >= 2 :                  
            dd -= 1
            dd += y
    for i in range(len(value)) :
        if y in century :
            y = century[i] == value[i]
            dd += y
            
    rem = dd % 7
    for i in range(len(doy)) :
        r.append(i) # Creating r list
        if rem in r :
            rem = r[i] == doy[i]
    print(rem)
        
          
print(dayOfYear(2000, 12, 31)) # Giving output False  "\n None
