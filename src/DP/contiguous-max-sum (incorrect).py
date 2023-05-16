import numpy as np

A = (5, 15, -30, 10, -5, 40, 10)


def get_contiguous_max(arr):
    result = []
    max_result = 0
    if len(arr) == 0:
        return result

    for l in range(1, len(arr) + 1):
        for start_i in range(len(arr) + 1 - l):
            end_i = start_i + l
            tmp_result = np.sum(arr[start_i:end_i])
            if tmp_result > max_result:
                max_result = tmp_result
                result = arr[start_i:end_i]

    return result


def lis(arr):
    L = get_contiguous_max(arr)
    return L


print(lis(A))
