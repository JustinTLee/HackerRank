#!/bin/python3

import sys

def breakingRecords(score):
    # get list size
    nGames = len(score)
    
    # initialize counts
    nLow = 0
    nHigh = 0
    
    for k in range(nGames):
        # initialize high and low scores to be the first score
        if k == 0:
            lowScore = score[0]
            highScore = score[0]
        else:
            # get the new high and low scores for the list thus far
            newLowScore = min(score[:(k + 1)])
            newHighScore = max(score[:(k + 1)])
            
            # if high and low scores are different then add a count and swap out the high and low scores
            if newLowScore != lowScore:
                nLow += 1
                lowScore = newLowScore
                
            if newHighScore != highScore:
                nHigh += 1
                highScore = newHighScore
                
    return nHigh, nLow

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))