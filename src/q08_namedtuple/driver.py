from util import calculate_average_marks

if __name__ == '__main__':
    total_students = int(input("Enter total number of students: "))
    columns = input("Enter columns (e.g., ID NAME CLASS MARKS): ").split()
    data = [input() for _ in range(total_students)]

    avg = calculate_average_marks(total_students, columns, data)
    print(avg)
