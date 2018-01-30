#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    # get minutes and seconds
    MM = s[3:5]
    SS = s[6:8]
    
    # check for AM or PM
    if (s[8:10] == "PM") & (int(s[0:2]) != 12):
        HH = str(int(s[0:2]) + 12)
    elif (s[8:10] == "AM") & (int(s[0:2]) == 12):
        HH = "00"
    else:
        HH = s[0:2]
    
    # create 24 hour string
    strNewTime = HH + ":" + MM + ":" + SS
    
    return strNewTime
        

s = input().strip()
result = timeConversion(s)
print(result)