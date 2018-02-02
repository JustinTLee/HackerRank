#!/bin/python3

import sys

def pickingNumbers(a):
    a.sort()

    # initialize count
    nSubset = 0
    
    # append indices of all values in which abs(a[m] - a[n]) <= 1
    for m in range(len(a)):
        subsetList = []
        for n in range(len(a)):
            if (abs(a[m] - a[n]) <= 1) & (m != n):
                subsetList.append(a[n])
            elif (m == n):
                subsetList.append(a[m])
                
        # the abs difference between the max and min number in the new subset cannot exceed 1
        # pop the max number
        while (abs(max(subsetList) - min(subsetList)) > 1):
            subsetList.remove(max(subsetList))

        # if the length of of the subset is greater than the current max length, replace the current max length
        if (len(subsetList) > nSubset):
            nSubset = len(subsetList)

    return nSubset

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)