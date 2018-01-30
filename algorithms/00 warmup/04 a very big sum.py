#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    intOutput = int(0)
    
    # sum up all integers in list
    for k in range(n):
        intOutput += ar[k]
        
    return intOutput
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)