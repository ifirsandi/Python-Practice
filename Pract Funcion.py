def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4 != 0):
        leap = False
    elif (year%100 != 0):
        leap = True
    elif (year%400 != 0):
        leap = False
    else :
        leap = True
    
    return leap

year = int(raw_input())
print is_leap(year)
