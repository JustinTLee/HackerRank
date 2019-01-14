#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    for nHashes in range(1, n + 1):
        nSpaces = n - nHashes
        strStair = " " * nSpaces + "#" * nHashes
        print(strStair)
        
    return

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)