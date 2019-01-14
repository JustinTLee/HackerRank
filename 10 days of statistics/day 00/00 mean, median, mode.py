# get raw inputs
n = int(input())
ar = sorted(list(map(int, input().strip().split(' '))))

def mean(ar):
    # get vector length
    n = len(ar)

    # mean
    mean = sum(ar)/n

    return mean

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

def mode(ar):
    n = len(ar)

    # mode
    modeArr = [1]
    intCount = 1
    for k in range(1, n):
        if ar[k] == ar[k - 1]:
            intCount += 1
        else:
            intCount = 1

        modeArr.append(intCount)        

    mode = ar[modeArr.index(max(modeArr))]
    
    return mode

valMean = mean(ar)
valMedian, _ = median(ar)
valMode = mode(ar)

print(valMean)
print(valMedian)
print(valMode)