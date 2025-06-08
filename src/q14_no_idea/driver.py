from util import calculate_happiness

if __name__ == '__main__':
    n, m = map(int, input("Enter n and m: ").split())
    arr = list(map(int, input("Enter the array elements: ").split()))
    A = set(map(int, input("Enter set A: ").split()))
    B = set(map(int, input("Enter set B: ").split()))

    result = calculate_happiness(arr, A, B)
    print("Happiness Score:", result)
