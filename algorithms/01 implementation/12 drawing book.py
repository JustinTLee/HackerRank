#!/bin/python3

import sys

def solve(n, p):
    # starting from the front
    if p % 2 == 1:
        front = (p - 1)/2
    else:
        front = p/2
        
    # starting from the back
    if n % 2 == 1:
        if p % 2 == 0:
            back = (n - (p + 1))/2
        else:
            back = (n - p)/2
    else:
        if p % 2 == 1:
            back = ((n - p) + 1)/2
        else:
            back = (n - p)/2

    # return the least value
    if back <= front:
        return int(back)
    else:
        return int(front)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)