#!/bin/python3

import sys

# method #1
# def climbingLeaderboard(scores, alice):
#     arAliceRank = []
    
#     sortedScores = list(set(scores))
#     sortedScores.sort(reverse = True)
    
#     for k in range(len(alice)):
#         m = 0
#         while (m != len(sortedScores)):
#             if alice[k] < sortedScores[m]:
#                 m += 1
#             else:
#                 break
            
#         print(m + 1)
        # arAliceRank.append(m + 1) 
    
    # return arAliceRank

# method #2
def climbingLeaderboard(scores, alice):
    arAliceRank = []
    
    n = len(alice)

    scores.extend(alice)
    newScores = list(set(scores))
    newScores.sort(reverse = True)
    
    alice.sort(reverse = True)
    
    print(newScores)
    print(alice)
    
    for k in range(n):
        print(newScores)
        arAliceRank.append(newScores.index(alice[k]) + 1)
        newScores.remove(alice[k])
        
    arAliceRank.reverse()
    
    return arAliceRank
    

# method #3
# def climbingLeaderboard(scores, alice):
#     arAliceRank = []
    
#     for k in range(len(alice)):
#         # append Alice's current score to the list of scores
#         # newScores = list(scores)
#         # newScores.append(alice[k])
#         scores.append(alice[k])
        
#         # create a new list of unique scores and sort it in decreasing order
#         # sortedScores = list(set(newScores))
#         sortedScores = list(set(scores))
#         sortedScores.sort(reverse = True)
        
#         # find where Alice's score is
#         indAliceScore = sortedScores.index(alice[k])
#         print(indAliceScore + 1)
#         # arAliceRank.append(indAliceScore + 1)

#     # return arAliceRank

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))