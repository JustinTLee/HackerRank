d1 = list(map(int, input().strip().split(' ')))
d2 = list(map(int, input().strip().split(' ')))
d3 = list(map(int, input().strip().split(' ')))
d4 = list(map(int, input().strip().split(' ')))
d5 = list(map(int, input().strip().split(' ')))

x = list([d1[0], d2[0], d3[0], d4[0], d5[0]])
y = list([d1[1], d2[1], d3[1], d4[1], d5[1]])

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

def linreg(X, Y):
    # get statistics for each vector
    n = len(X)
    meanX = mean(X)
    meanY = mean(Y)
    stdX = std(n, X)
    stdY = std(n, Y)
    rXY = pearson(n, X, Y)
    
    # calculate slope and intercept
    b1 = rXY*stdY/stdX
    b0 = meanY - b1*meanX
    
    return b0, b1

b0, b1 = linreg(x, y)
output = b0 + b1*80
print(round(output, 3))