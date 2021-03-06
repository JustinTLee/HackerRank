n = int(input())
arrX = list(map(int, input().strip().split(' ')))
arrF = list(map(int, input().strip().split(' ')))

def median(ar):
    # get vector length
    n = len(ar)
    
    if n % 2 == 0:
        ind1 = int(n/2) - 1
        ind2 = int(n/2)
        median = (ar[ind1] + ar[ind2])/2
        pos = list([ind1, ind2])
    else:
        ind = int((n - 1)/2)
        median = ar[ind]
        pos = list([ind])
        
    return median, pos

def quartiles(n, arrX):
    arrX.sort()
    
    Q2, pos = median(arrX)

    if len(pos) == 1:
        Q1, _ = median(arrX[:int(pos[0])])
        Q3, _ = median(arrX[(int(pos[0]) + 1):])
    else:
        Q1, _ = median(arrX[:(int(pos[0]) + 1)])
        Q3, _ = median(arrX[int(pos[1]):])
        
    if Q1 % 1 == 0:
        Q1 = int(Q1)
    if Q2 % 1 == 0:
        Q2 = int(Q2)
    if Q3 % 1 == 0:
        Q3 = int(Q3)
    
    return Q1, Q2, Q3

def iterateFreqs(X, F):
    nX = len(X)
    
    newX = []
    
    # make a new list reproducing all of the X inputs and their corresponding frequencies
    for m in range(nX):
        for n in range(F[m]):
            newX.append(X[m])
            
    return newX

def iqr(arrX):
    # get the quartiles
    
    Q1, _, Q3 = quartiles(len(arrX), arrX)
    
    iqr = Q3 - Q1
    
    return iqr

freqX = iterateFreqs(arrX, arrF)
freqX.sort()
valIQR = float(iqr(freqX))
print(valIQR)