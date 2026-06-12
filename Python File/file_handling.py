# file_handling.py

def save_student_record():

    name = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    with open("student_data.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Roll No: {roll_no}\n")
        file.write(f"Branch: {branch}\n")
        file.write(f"Marks: {marks}\n")

    print("\nStudent Record Saved Successfully")


def read_student_record():

    print("\nReading File...\n")

    with open("student_data.txt", "r") as file:
        content = file.read()
        print(content)


save_student_record()

read_student_record()
