import numpy as np

def calculate_determinant(matrix):
    arr = np.array(matrix)
    return round(np.linalg.det(arr), 2)
