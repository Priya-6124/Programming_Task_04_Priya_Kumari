# student_manager.py

def get_student_details():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    branch = input("Enter Branch: ")
    semester = input("Enter Semester: ")

    return name, roll_no, branch, semester


def display_student_details(name, roll_no, branch, semester):
    print("\n===== STUDENT INFORMATION =====")
    print("Name      :", name)
    print("Roll No   :", roll_no)
    print("Branch    :", branch)
    print("Semester  :", semester)


name, roll_no, branch, semester = get_student_details()

display_student_details(name, roll_no, branch, semester)
