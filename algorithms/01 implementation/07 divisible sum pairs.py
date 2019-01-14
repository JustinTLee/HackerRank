#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # sort the array
    ar.sort()
    
    # initialize count variable
    intCount = 0
    
    # cycle through all possible values in array
    for N in range(n - 1):
        for M in range(N + 1, n):
            # if sum of aN and aM is divisible by k, count that is a true positive
            if ((ar[N] + ar[M]) % k == 0):
                intCount += 1
                
    return intCount

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)