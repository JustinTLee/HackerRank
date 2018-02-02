#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    maxAmount = 0
    spend = 0
    
    nKeyboards = len(keyboards)
    nDrives = len(drives)
    
    # loop through the possible combinations and replace max if higher than previous max values
    # but lower than or equal to spending limit
    for m in range(nKeyboards):
        for n in range(nDrives):
            if (keyboards[m] + drives[n] > maxAmount) & (keyboards[m] + drives[n] <= s):
                maxAmount = keyboards[m] + drives[n]
                
    if maxAmount == 0:
        return -1
    else:
        return maxAmount
            

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)