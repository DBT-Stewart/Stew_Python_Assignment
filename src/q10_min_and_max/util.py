import numpy as np

def max_of_row_minimums(matrix):
    arr = np.array(matrix)
    return np.max(np.min(arr, axis=1))
