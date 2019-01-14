from math import erf, sqrt

nValues = float(input())
mean = float(input())
std = float(input())
CI = float(input())
zscore = float(input())

A = mean - zscore*std/sqrt(nValues)
B = mean + zscore*std/sqrt(nValues)

print(round(A, 2))
print(round(B, 2))