# marks_analyzer.py

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total):
    return total / 5


def calculate_grade(percentage):

    if percentage >= 90:
        return "A"

    elif percentage >= 80:
        return "B"

    elif percentage >= 70:
        return "C"

    elif percentage >= 60:
        return "D"

    else:
        return "F"


def display_result(marks, total, percentage, grade):

    print("\n===== MARKS REPORT =====")

    for i in range(5):
        print(f"Subject {i+1}: {marks[i]}")

    print("\nTotal Marks :", total)
    print("Percentage  :", round(percentage, 2), "%")
    print("Grade       :", grade)


marks = []

for i in range(5):
    mark = float(input(f"Enter Marks for Subject {i+1}: "))
    marks.append(mark)

total = calculate_total(marks)

percentage = calculate_percentage(total)

grade = calculate_grade(percentage)

display_result(marks, total, percentage, grade)
