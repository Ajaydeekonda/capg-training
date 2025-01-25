def student_progress(marks):
    total_marks = total(marks)
    percent = percentage(total_marks)
    _grade = grade(percent)
    
    return total_marks, percent, _grade    

def total(marks):
    return sum(marks)

def percentage(total_marks):
    return (total_marks / 500) * 100  # Fix the division by 500

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 50:
        return "C"
    else:
        return "Fail"


if __name__ == "__main__":
    student_name = input("Enter the Student's name: ")
    marks = list(map(int, input("Enter the marks (separated by space): ").split()))
    total_marks, percent, _grade = student_progress(marks)
    
    print(f"Student Name: {student_name}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Grade: {_grade}")
