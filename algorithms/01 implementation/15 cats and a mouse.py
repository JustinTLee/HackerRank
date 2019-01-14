#!/bin/python3

import sys

def catAndMouse(x, y, z):
    # if cat A is closer to mouse C than cat B is, then cat A wins
    if (abs(x - z) < abs(y - z)):
        return ["Cat A"]
    # if cat B is closer to mouse C than cat A is, then cat B wins
    elif (abs(x - z) > abs(y - z)):
        return ["Cat B"]
    # if both cats are equidistant to the mouse, the mouse wins
    elif (abs(x - z) == abs(y - z)):
        return ["Mouse C"]

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print (" ".join(map(str, result)))