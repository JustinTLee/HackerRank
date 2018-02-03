#!/bin/python3

import sys

def utopianTree(n):
    # if N is divisible by 2, multiply by 2, else add 1
    if n == 0:
        return 1
    else:
        startHeight = 1
        for N in range(0, n):
            if N % 2 != 0:
                startHeight += 1
            else:
                startHeight *= 2
    
    return startHeight

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)