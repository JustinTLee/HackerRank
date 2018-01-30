#!/bin/python3

import sys

def miniMaxSum(arr):
    arr.sort()
    min = sum(arr[:4])
    max = sum(arr[1:])

    print(min, max)
    return min, max

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)