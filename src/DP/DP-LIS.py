import numpy as np

A = (5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3)


def create_L(arr):
    n = len(arr)
    A = np.array(arr)
    L = np.ones(n)
    for i in range(1, n):
        try:
            L[i] = np.max((L[:i])[A[:i] < arr[i]]) + 1
        except ValueError:
            L[i] = L[i-1]
    return L


def lis(arr):
    L = create_L(arr)
    return L


print(lis(A))
