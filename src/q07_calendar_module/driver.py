from util import get_day_name

if __name__ == '__main__':
    month, day, year = map(int, input("Enter date in MM DD YYYY format: ").split())
    print(get_day_name(month, day, year))
