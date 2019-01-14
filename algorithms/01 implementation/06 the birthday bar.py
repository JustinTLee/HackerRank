#!/bin/python3

import sys

def solve(n, s, d, m):
    # initialize empty list
    intCorrectFrames = 0
    
    # cycle through all possible frames
    for k in range(n - m + 1):
        
        # initialize summation variable
        valSum = 0
        
        # add up all values within frame
        for M in range(m):
            valSum += s[k + M]
            
        # compare frame to day
        if valSum == d:
            intCorrectFrames += 1
            
    return intCorrectFrames

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)