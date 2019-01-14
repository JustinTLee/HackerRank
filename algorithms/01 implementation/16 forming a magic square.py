#!/bin/python3

import sys

def formingMagicSquare(s):
    set10 = set(range(1, 10))
    
    arS = []
    for m in range(3):
        for n in range(3):
            arS.append(s[m][n])
            
    missingInts = list(set10 - set(arS))
    print(missingInts)


if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)