#!/bin/python3

import sys

def countingValleys(n, s):
    # initalize valley count
    nValleys = 0
    
    # start at 0
    elevation = 0
    
    for k in range(n):
        # if we move up, add 1 to elevation
        if s[k] == "U":
            elevation += 1
        # if we move down, subtract 1 from elevation
        elif s[k] == "D":
            elevation -= 1
            
        # if we are at elevation is -1 and the previous direction was "D", we are descending into a valley
        if (elevation == - 1) & (s[k] == "D"):
            nValleys += 1
            
    return nValleys
        

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)