#!/bin/python3

import sys

def migratoryBirds(n, ar):
    ar.sort()
    # mode
    modeArr = [1]
    intCount = 1
    for k in range(1, n):
        if ar[k] == ar[k - 1]:
            intCount += 1
        else:
            intCount = 1

        modeArr.append(intCount)        

    mode = ar[modeArr.index(max(modeArr))]
    
    return mode

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)