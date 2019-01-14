ratios = list(map(float, input().strip().split(' ')))
nInspections = int(input())

p = ratios[0]/ratios[1]

def geompmf(p, k, type = "success"):
    if type == "success":
       return p*(1 - p) ** (k - 1)
    elif type == "failure":
       return p*(1 - p) ** k

print(round(geom_pmf(p, nInspections), 3))