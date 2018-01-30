#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # initialize counts for each fruit
    nApples = 0
    nOranges = 0
    
    # get list dimensions
    nAppleThrows = len(apples)
    nOrangeThrows = len(oranges)
    
    # loop over apple throws
    for m in range(nAppleThrows):
        if s <= a + apples[m] <= t:
            nApples += 1
            
    # loop over orange throws
    for n in range(nOrangeThrows):
        if s <= b + orange[n] <= t:
            nOranges += 1
            
    print(nApples)
    print(nOranges)

    return

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)