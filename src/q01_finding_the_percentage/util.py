def s_mark(student_marks, query_name):
   
    if query_name in student_marks:
        average_mark = sum(student_marks[query_name]) / len(student_marks[query_name])
        return round(average_mark, 2)
    return None
