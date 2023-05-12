import numpy as np

X = 'BCDBCDA'
Y = 'ABECBA'


def lcs(str1, str2):
    L = np.zeros((len(X)+1,len(Y)+1))
    for i in range(1, L.shape[0]):
        for j in range(1, L.shape[1]):
            if X[i-1] == Y[j-1]:
                L[i, j] = 1 + L[i-1, j-1]
            else:
                L[i, j] = max(L[i, j-1], L[i-1, j])
    return L


print(lcs(X, Y))
