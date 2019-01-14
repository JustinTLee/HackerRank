n = int(input())
X = list(map(float, input().strip().split(' ')))
Y = list(map(float, input().strip().split(' ')))

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
        
    # calculate variance and standard deviation
    var = sqError/n
    std = var ** 0.5
    
    return std

def pearson(n, X, Y):
    # get statistics for each input vector
    meanX = mean(X)
    meanY = mean(Y)
    stdX = std(n, X)
    stdY = std(n, Y)
    
    sumDev = 0
    
    # sum the covariance deviation from the mean 
    for N in range(n):
        sumDev += (X[N] - meanX)*(Y[N] - meanY)

    # divide that deviation by the standard deviations of each vector   
    return sumDev/(n*stdX*stdY)

print(round(pearson(n, X, Y), 3))