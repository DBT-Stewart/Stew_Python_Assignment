import numpy as np

def calculate_stats(matrix):
    arr = np.array(matrix)
    mean_result = np.mean(arr, axis=1)
    variance_result = np.var(arr, axis=0)
    std_dev_result = round(np.std(arr, axis=None), 11)
    return mean_result, variance_result, std_dev_result
