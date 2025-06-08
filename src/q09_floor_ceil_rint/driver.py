from util import apply_rounding_operations

if __name__ == '__main__':
    arr = list(map(float, input("Enter float values separated by space: ").split()))
    floor, ceil, rint = apply_rounding_operations(arr)
    print(floor)
    print(ceil)
    print(rint)
