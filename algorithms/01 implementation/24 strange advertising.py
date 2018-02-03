#!/bin/python3

import sys
from math import floor

def viralAdvertising(n):
    # initialize counts
    # write nRecieved as fraction so that for loop treats every input the same
    nRecieved = float(5/3)
    nLikes = float(5/3)
    
    sumLikes = 0
    
    # recieved is always the amount previous likes multiplied by 3
    # likes is always the floor of recieved divided by 2
    for k in range(n):
        nRecieved = 3*nLikes
        nLikes = int(floor(nRecieved/2))
        
        sumLikes += nLikes
        
    return sumLikes

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)