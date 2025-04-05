#Student grade program
def get_grade(score):
    if 90 <= score <= 100:
        return "Grade A"
    elif 80 <= score < 90:
        return "Grade B"
    elif 70 <= score < 80:
        return "Grade C"
    elif 60 <= score < 70:
        return "Grade D"
    else:
        return "Fail"


marks = float(input("Enter your marks: "))
grade = get_grade(marks)
print("Your grade is:", grade)
