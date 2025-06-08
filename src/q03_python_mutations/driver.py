from util import mutate_string

if __name__ == "__main__":
    s = input("Enter a string: ")
    i, c = input("Enter position and character: ").split()
    s_new = mutate_string(s, int(i), c)
    print("Modified string:", s_new)
