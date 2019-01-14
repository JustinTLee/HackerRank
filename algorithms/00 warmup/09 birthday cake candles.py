#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # find the maximum value in ar
    maxVal = max(ar)
    
    # find all the places where ar is equal to the max value
    # and sum the add the number to the running total
    nMax = 0
    
    for k in range(n):
        if ar[k] == maxVal:
            nMax += 1

    # return the sum
    return nMax

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)