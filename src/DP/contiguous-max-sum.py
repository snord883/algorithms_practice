import numpy as np

A = (5, 15, -30, 110, -50, 44, 10)


def get_contiguous_max(arr):
    if len(arr) == 0:
        return 0

    S = np.zeros(len(arr))

    for i in range(1, len(arr)):
        S[i] = arr[i] + max(0, S[i-1])
    return max(S)


def lis(arr):
    L = get_contiguous_max(arr)
    return L


print(lis(A))
