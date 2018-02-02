#!/bin/python3

import sys

def sockMerchant(n, ar):
    # sort the data in order
    ar.sort()
    
    # initialize match variable
    match = 1
    arMatch = []
    
    # cycle through socks and delete indices if k index is equal to k - 1 index
    # then delete both k and k - 1 indices and set k back to the beginning of the list
    k = 0
    while k != (len(ar)):
        if k > 0:
            if ar[k] == ar[k - 1]:
                del ar[k]
                del ar[k - 1]
                k = 0
            else:
                k += 1
        else:
            k += 1
            
    return int((n - len(ar))/2)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)