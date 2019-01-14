#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    # shifts the frame
    remainder = (s + (m - 1)) % n
    
    # remember that 0 is equal to n
    if remainder == 0:
        return n
    else:
        return remainder
    
t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)