n = int(input())
arrX = list(map(int, input().strip().split(' ')))
arrW = list(map(int, input().strip().split(' ')))

def weightedMean(n, arrX, arrW):
    weightedSum = 0
    weights = 0
    
    for k in range(n):
        weightedSum += arrX[k]*arrW[k]
        weights += arrW[k]
        
    return round(weightedSum/weights, 1)

print(weightedMean(n, arrX, arrW))