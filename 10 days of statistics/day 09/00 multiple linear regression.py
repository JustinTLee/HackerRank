import numpy as np

# import data
m, n = [int(k) for k in input().strip().split(' ')]
X = -np.ones((n, m + 1))
Y = -np.ones((n, 1))
for k in range(n):
    data = input().strip().split(' ')
    X[k, 1:(m + 1)] = data[:m]
    Y[k, 0] = data[m]

q = int(input())
newX = -np.ones((q, m + 1))
for k in range(q):
    data = input().strip().split(' ')
    newX[k, 1:(m + 1)] = data[:m]

def multipleLinReg(X, Y):
    # normal equation
    beta_vect = np.dot(np.dot(np.linalg.pinv(np.dot(X.T,X)), X.T), Y)
    
    return beta_vect
    
beta_vect = multipleLinReg(X, Y)

newY = np.dot(newX, beta_vect)

for k in range(np.shape(newY)[0]):
    print(round(newY[k, 0], 2))