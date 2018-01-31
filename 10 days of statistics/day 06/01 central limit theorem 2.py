from math import erf, sqrt

maxTickets = float(input())
nStudents = float(input())
mean = float(input())
std = float(input())

# sum of normal random variables is also normally distributed
# with mean equal to sum of means of rvs
sumMeans = nStudents*mean

# variance equal to sum of variance of rvs
sumSTD = sqrt(nStudents*(std ** 2))

def norm_cdf(mean, std, x):
    # standardize input for error function
    standardX = (x - mean)/(std*sqrt(2))
    
    # CDF of normal distribution is 1/2*(1 + erf(X))
    P_x = 0.5*(1 + erf(standardX))
    
    return P_x

print(round(norm_cdf(sumMeans, sumSTD, maxTickets), 4))