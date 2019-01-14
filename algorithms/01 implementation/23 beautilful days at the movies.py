#!/bin/python3

import sys

def beautifulDays(i, j, k):
    # initialize beautiful dates count
    nBeautifulDates = 0
    
    # create range of dates
    for date in range(i, j + 1):
        # get difference between date and reverse date
        revDate = int(str(date)[::-1])
        
        # evaluate whether date is a beautiful date
        if abs(date - revDate) % k == 0:
            nBeautifulDates += 1
    
    return nBeautifulDates
        

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)