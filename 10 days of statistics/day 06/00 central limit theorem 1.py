from math import erf, sqrt

maxWeight = float(input())
nBoxes = float(input())
mean = float(input())
std = float(input())

# sum of normal random variables is also normally distributed
# with mean equal to sum of means of rvs
sumMeans = nBoxes*mean

# variance equal to sum of variance of rvs
sumSTD = sqrt(nBoxes*(std ** 2))

def norm_cdf(mean, std, x):
    # standardize input for error function
    standardX = (x - mean)/(std*sqrt(2))
    
    # CDF of normal distribution is 1/2*(1 + erf(X))
    P_x = 0.5*(1 + erf(standardX))
    
    return P_x

print(round(norm_cdf(sumMeans, sumSTD, maxWeight), 4))