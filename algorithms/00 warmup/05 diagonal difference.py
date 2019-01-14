#!/bin/python3

import sys

def diagonalDifference(a):
    # get matrix row size
    nRows = len(a)
    
    # initialize diagonal vars
    intPrimDiag = 0
    intSecnDiag = 0
    
    # loop over number of rows
    for m in range(nRows):
        intPrimDiag += a[m][m]
        intSecnDiag += a[m][nRows - m - 1]
        
    # return abs of diagonal difference
    return abs(intPrimDiag - intSecnDiag)
            

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)