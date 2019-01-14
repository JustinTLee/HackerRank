#!/bin/python3

import sys

def permutationEquation(p):
    # map p results to dictionary
    rangeToN = list(range(1, len(p) + 1))
    pDict = dict(zip(p, rangeToN))
    
    results = []
    # run through dictionary twice to get y's
    for k in range(1, len(p) + 1):
        results.append(pDict[pDict[k]])
        
    return results

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))