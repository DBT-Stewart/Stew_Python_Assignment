from util import filter_emails

def main():
    n = int(input())
    emails = [input() for _ in range(n)]

    filtered = filter_emails(emails)
    filtered.sort()
    for email in filtered:
        print(email)

if __name__ == "__main__":
    main()
