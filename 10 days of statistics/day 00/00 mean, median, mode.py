# get raw inputs
n = int(input())
ar = sorted(list(map(int, input().strip().split(' '))))

def descripstats(n, ar):
    # mean
    mean = sum(ar)/n

    # median
    if n % 2 == 0:
        median = (ar[int(n/2) - 1] + ar[int(n/2)])/2
    else:
        median = ar[int((n - 1)/2)]

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
    
    print(mean)
    print(median)
    print(mode)
    
    return

descripstats(n, ar)