#!/bin/python3

import sys

def solve(grades):
    # initialize list size
    nGrades = len(grades)
    
    for k in range(nGrades):
        if (grades[k] >= 38) & ((5 - grades[k] % 5) < 3):
            grades[k] = grades[k] + (5 - grades[k] % 5)
            
        print(grades[k])
        
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))