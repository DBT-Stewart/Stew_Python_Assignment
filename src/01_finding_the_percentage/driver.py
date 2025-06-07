from util import s_mark

if __name__ == "__main__":
    n = int(input("Enter number of students: "))
    student_marks = {}

    for _ in range(n):
        name, *line = input("Enter name and marks: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter student to query: ")
    result = s_mark(student_marks, query_name)
    
    if result is not None:
        print(f"{result:.2f}")
    else:
        print("Student not found.")
