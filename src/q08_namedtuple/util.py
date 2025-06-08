from collections import namedtuple

def calculate_average_marks(total_students, columns, data):
    Student = namedtuple('Student', columns)
    student_info = [Student(*row.split()) for row in data]
    total_marks = sum(int(student.MARKS) for student in student_info)
    return total_marks / total_students
