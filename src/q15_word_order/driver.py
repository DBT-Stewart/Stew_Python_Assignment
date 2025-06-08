from util import word_order_counter

if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(n)]
    count, values = word_order_counter(words)
    print(count)
    print(" ".join(map(str, values)))
