from util import merge_the_tools

if __name__ == "__main__":
    string = input("Enter the string: ")
    k = int(input("Enter the segment size k: "))

    results = merge_the_tools(string, k)
    for part in results:
        print(part)
