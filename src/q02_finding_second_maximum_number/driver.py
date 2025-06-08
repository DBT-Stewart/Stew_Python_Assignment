from util import sec_large

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements separated by space: ").split()))
    result = sec_large(arr)

    if result is not None:
        print("Second largest:", result)
    else:
        print("Not enough unique numbers to determine second largest.")
