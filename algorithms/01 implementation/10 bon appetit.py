#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # sum the total for all the food items
    sumFood = sum(ar)
    
    # subtract the amount in the kth item
    sumFood = sumFood - ar[k]
    
    # divide the bill by 2
    amountSplit = sumFood/2
    
    # compare to how much Brian charged Anna
    if amountSplit == b:
        return "Bon Appetit"
    else:
        return int(b - amountSplit)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)