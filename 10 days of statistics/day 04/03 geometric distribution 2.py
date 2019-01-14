ratios = list(map(float, input().strip().split(' ')))
nInspections = int(input())

p = ratios[0]/ratios[1]

def geom_pmf(p, k, type = "success"):
    if type == "success":
       return p*(1 - p) ** (k - 1)
    elif type == "failure":
       return p*(1 - p) ** k

def geom_cmf(p, k, type = "success"):
    # initialize sum
    P_k = 0
    
    for K in range(1, k + 1):
        P_k += geom_pmf(p, K, type)
        
    return P_k

print(round(geom_cmf(p, nInspections), 3))