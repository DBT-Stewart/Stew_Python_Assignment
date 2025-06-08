import numpy as np

def apply_rounding_operations(arr):
    
    np.set_printoptions(legacy='1.13')
    arr_np = np.array(arr)
    return (np.floor(arr_np), np.ceil(arr_np), np.rint(arr_np))