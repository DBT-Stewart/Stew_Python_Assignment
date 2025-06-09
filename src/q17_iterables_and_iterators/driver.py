from util import probability_of_a
if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    letters = input("Enter the letters separated by space: ").split()
    k = int(input("Enter combination length: "))

    prob = probability_of_a(letters, k)
    print(f"{prob:.3f}")