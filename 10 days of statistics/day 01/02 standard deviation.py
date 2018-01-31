n = int(input())
arrX = list(map(int, input().strip().split(' ')))

def mean(ar):
    # get vector length
    n = len(ar)

    # mean
    mean = sum(ar)/n

    return mean

def std(n, X):
    # get the mean
    meanX = mean(X)

    # get total squared deviation from mean
    sqError = 0
    for k in range(n):
        sqError += (X[k] - meanX) ** 2
        
    var = sqError/n
    std = var ** 0.5
    
    return std

valSTD = std(n, arrX)
print(round(valSTD, 1))