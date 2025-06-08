from util import calculate_determinant

if __name__ == '__main__':
    n = int(input("Enter matrix size (N): "))
    matrix = [list(map(float, input().split())) for _ in range(n)]
    result = calculate_determinant(matrix)
    print(result)
