ratios = list(map(float, input().strip().split(' ')))

proportion = ratios[0]/100
nPistons = int(ratios[1])

def nchoosek(n, k):
    # create factorial results
    nFactorial = 1
    kFactorial = 1
    nkFactorial = 1
    
    for N in range(1, n + 1):
        nFactorial *= N
        
    for K in range(1, k + 1):
        kFactorial *= K
        
    for NK in range(1, (n - k) + 1):
        nkFactorial *= NK
        
    # return combination ratio
    return (nFactorial/(kFactorial*nkFactorial))
        

def bin_pmf(p, n, k):
    # calculate binomial probability for having seen those results
    nCk = nchoosek(n, k)
    p_k = nCk*(p ** k)*((1 - p) ** (n -k))
    
    return p_k
    
def bin_cmf(p, n, k):
    P_k = 0
    
    # perform PMF on every number lower than or equal to k and sum them up
    for K in range(k + 1):
        P_k += bin_pmf(p, n, K)

    return P_k

print(round(bin_cmf(proportion, nPistons, 2), 3))
print(round(1 - bin_cmf(proportion, nPistons, 1), 3))