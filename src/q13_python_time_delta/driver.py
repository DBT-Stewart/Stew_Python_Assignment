from util import time_delta

if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        t1 = input("Enter first timestamp: ")
        t2 = input("Enter second timestamp: ")
        print(time_delta(t1, t2))
