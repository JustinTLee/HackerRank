from math import erf, sqrt

arrInput = list(map(float, input().strip().split(' ')))
q1 = float(input())
q2 = list(map(float, input().strip().split(' ')))
    
def norm_cdf(mean, std, x):
    # standardize input for error function
    standardX = (x - mean)/(std*sqrt(2))
    
    # CDF of normal distribution is 1/2*(1 + erf(X))
    P_x = 0.5*(1 + erf(standardX))
    
    return P_x

print(round(norm_cdf(arrInput[0], arrInput[1], q1), 3))
print(round(norm_cdf(arrInput[0], arrInput[1], q2[1]) - norm_cdf(arrInput[0], arrInput[1], q2[0]), 3))