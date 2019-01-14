n = int(input())
X = list(map(float, input().strip().split(' ')))
Y = list(map(float, input().strip().split(' ')))

def spearman(n, X, Y):
    sumDiff = 0
    
    # sort the vectors
    Xsorted = sorted(X)
    Ysorted = sorted(Y)
    
    # rank the vectors
    
    # sum the squared difference between the two vectors for each column
    for k in range(n):
        sumDiff += ((Xsorted.index(X[k]) + 1) - (Ysorted.index(Y[k]) + 1)) ** 2

    # output the coefficient
    return 1 - 6*sumDiff/(n ** 3 - n)

print(round(spearman(n, X, Y), 3))