#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # look for the intersection between the two lines
    # v1*t + x1 = v2*t + x2 -> t = (x2 - x1)/(v1 - v2)
    # v1*t + x1 will be where they intersect
    
    if ((x2 - x1 < 0) | (v1 - v2 < 0)) | ((v1 == v2) & (x1 != x2)):
        return "NO"
    elif (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"
    
#     t = (x2 - x1)/(v1 - v2)
    
#     if (t >= 0) & (t % 1 == 0):
#         return "YES"
#     else:
#         return "NO"

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)