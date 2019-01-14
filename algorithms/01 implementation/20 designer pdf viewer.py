#!/bin/python3

import sys

def designerPdfViewer(h, word):
    # create a dictionary of all the letters in the alphabet and their corresponding heights
    alphabet = list(map(chr, range(97, 123)))
    heights = dict(zip(alphabet, h))
    
    # find the max height
    maxHeight = 0
    for k in word:
        if maxHeight < heights[k]:
            maxHeight = heights[k]
            
    # multiply height by word length and return
    return maxHeight*len(word)

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)