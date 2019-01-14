#!/bin/python3

import sys

def getTotalX(a, b):
    A = []
    B = []
    
    intAMax = max(a)
    intBMin = min(b)
    
    for k in range(intAMax, intBMin + 1):
        nA = 0
        for m in range(len(a)):
            if k % a[m] == 0:
                nA += 1
                
            if nA == len(a):
                A.append(k)
        
        nB = 0
        for n in range(len(b)):
            if b[n] % k == 0:
                nB += 1
            
            if nB == len(b):
                B.append(k)

    return len(set(A).intersection(set(B)))

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
