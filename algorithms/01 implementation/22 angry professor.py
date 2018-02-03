#!/bin/python3

import sys

def angryProfessor(k, a):
    # get number of values in a below or equal to 0
    nStudentsOnTime = sum(k <= 0 for k in a)
    
    return "YES" if nStudentsOnTime < k else "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)