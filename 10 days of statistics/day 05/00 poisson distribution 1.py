from math import exp

mean = float(input())
X = int(input())

def poisson_pmf(mean, k):
    
    # calculate the factorial
    kFactorial = 1
    for K in range(1, k + 1):
        kFactorial *= K
        
    # calculate the PMF
    return ((mean ** k)*exp(-mean)/(kFactorial))

print(round(poisson_pmf(mean, X), 3))