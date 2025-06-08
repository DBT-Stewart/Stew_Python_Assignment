from util import max_of_row_minimums

if __name__ == '__main__':
    n, m = map(int, input("Enter rows and columns: ").split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = max_of_row_minimums(matrix)
    print(result)
