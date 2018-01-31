#!/bin/python3

import sys

def solve(year):
    # divisible by 400
    # divisible by 4 and not divisible by 100
    if year < 1918:
        if (year % 4 == 0):
            date = "12.09." + str(year)
        else:
            date = "13.09." + str(year)
    elif year == 1918:
        date = "26.09.1918"
    else:
        if (year % 400 == 0):
            date = "12.09." + str(year)
        elif ((year % 4 == 0) & (year % 100 != 0)):
            date = "12.09." + str(year)
        else:
            date = "13.09." + str(year)
        
    return date

year = int(input().strip())
result = solve(year)
print(result)