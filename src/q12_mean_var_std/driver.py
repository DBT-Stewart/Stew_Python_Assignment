from util import calculate_stats

if __name__ == '__main__':
    import numpy as np

    n, m = map(int, input("Enter rows and columns: ").split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    mean, var, std_dev = calculate_stats(matrix)
    print(np.array2string(mean, separator=' '))
    print(np.array2string(var, separator=' '))
    print(std_dev)
