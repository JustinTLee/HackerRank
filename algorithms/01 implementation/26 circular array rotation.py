#!/bin/python3

import sys

def circularArrayRotation(a, n, k, m):
    # rotate through list of 1 to n instead of actual list
    locA = list(range(1, n + 1))
    
    newLocA = [ai + k*(n - 1) for ai in locA]
    
    results = []
    for M in m:
        if newLocA[M] % n == 0:
            results.append(a[n - 1])
        else:
            results.append(a[newLocA[M] % n - 1])
            
    return results
    

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
       m_t = int(input().strip())
       m.append(m_t)
    result = circularArrayRotation(a, n, k, m)
    print ("\n".join(map(str, result)))