from math import exp

means = list(map(float, input().strip().split(' ')))
meanA = means[0]
meanB = means[1]

def poisson_pmf(mean, k):
    
    # calculate the factorial
    kFactorial = 1
    for K in range(1, k + 1):
        kFactorial *= K
        
    # calculate the PMF
    return ((mean ** k)*exp(-mean)/(kFactorial))

# expected value of Poisson distribution is lambda
# is lambda equal to repairs per day?
# E{X^2} = E{X} + E{X}^2 for Poisson distribution
CA = 160 + 40*(meanA + meanA ** 2)
CB = 128 + 40*(meanB + meanB ** 2)

print(round(CA, 3))
print(round(CB, 3))