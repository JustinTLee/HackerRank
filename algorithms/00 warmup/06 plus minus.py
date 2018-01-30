#!/bin/python3

import sys

def plusMinus(arr):
    # initialize counts of positive, negative, and zero numbers
    nPos = 0
    nNeg = 0
    nZero = 0
    
    # get size of list
    nArr = len(arr)
    
    for k in range(nArr):
        if arr[k] > 0:
            nPos += 1
        elif arr[k] < 0:
            nNeg += 1
        elif arr[k] == 0:
            nZero += 1
            
    floatPos = float(nPos/nArr)
    floatNeg = float(nNeg/nArr)
    floatZero = float(nZero/nArr)
    
    print(floatPos)
    print(floatNeg)
    print(floatZero)
    
    return floatPos, floatNeg, floatZero

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)