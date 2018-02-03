#!/bin/python3

import sys

def hurdleRace(k, height):
    # subtract the max hurdle height from the max height he can jump
    minDrinks = max(height) - k
    
    if minDrinks <= 0:
        return 0
    else:
        return minDrinks

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)