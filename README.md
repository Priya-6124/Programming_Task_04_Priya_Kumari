# Python Programming Task 04

## Functions, File Handling & Student Management System

### 📌 Objective

The objective of this task is to learn and implement:

* Functions
* Modular Programming
* File Handling
* Data Management
* Structured Programming

This project contains Python solutions for all parts of Task 04.

---

# 👨‍🎓 Student Details

| Field      | Details                                              |
| ---------- | ---------------------------------------------------- |
| Name       | Priya Kumari                                         |
| Internship | Python Programming Internship                        |
| Task       | Task 04                                              |
| Topic      | Functions, File Handling & Student Management System |

---

# 📂 Project Structure

```text
Programming_Task_04_PriyaKumari
│
├── calculator_functions.py
├── student_manager.py
├── marks_analyzer.py
├── file_handling.py
├── password_vault.py
├── activity_logger.py
│
├── student_data.txt
├── password_vault.txt
├── activity_log.txt
│
├── Screenshots
│   ├── calculator_output.png
│   ├── student_manager_output.png
│   ├── marks_analyzer_output.png
│   ├── file_handling_output.png
│   ├── password_vault_output.png
│   └── activity_logger_output.png
│
└── README.md
```

---

# Part A: Calculator Using Functions

## Description

A menu-driven calculator application that performs arithmetic operations using separate functions.

### Operations

* Addition
* Subtraction
* Multiplication
* Division

### Functions Used

```python
addition()
subtraction()
multiplication()
division()
```

### Features

* Menu-driven interface
* Reusable functions
* Division-by-zero handling
* Continuous execution until user exits

### Sample Output

```text
===== CALCULATOR MENU =====

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter Choice: 1
Enter First Number: 10
Enter Second Number: 20

Result: 30
```

---

# Part B: Student Information Manager

## Description

This program accepts student information from the user and displays it in a formatted manner using functions.

### Inputs

* Student Name
* Roll Number
* Branch
* Semester

### Functions Used

```python
get_student_details()
display_student_details()
```

### Sample Output

```text
===== STUDENT INFORMATION =====

Name      : Priya Kumari
Roll No   : 101
Branch    : CSE
Semester  : 5
```

---

# Part C: Marks Analysis System

## Description

This program accepts marks for five subjects and calculates:

* Total Marks
* Percentage
* Grade

### Grade Criteria

| Percentage   | Grade |
| ------------ | ----- |
| 90 and Above | A     |
| 80 and Above | B     |
| 70 and Above | C     |
| 60 and Above | D     |
| Below 60     | F     |

### Functions Used

```python
calculate_total()
calculate_percentage()
calculate_grade()
display_result()
```

### Sample Output

```text
===== MARKS REPORT =====

Total Marks : 446
Percentage  : 89.2%
Grade       : B
```

---

# Part D: File Handling Challenge

## Description

This program stores student details inside a text file and then reads the stored data.

### File Created

```text
student_data.txt
```

### Stored Information

* Name
* Roll Number
* Branch
* Marks

### Functions Used

```python
save_student_record()
read_student_record()
```

### Sample Output

```text
Student Record Saved Successfully

Reading File...

Name: Priya
Roll No: 101
Branch: CSE
Marks: 85
```

---

# Part E: Password Vault Simulator

## Description

This program stores website credentials inside a text file and allows users to view saved records.

### File Created

```text
password_vault.txt
```

### Stored Information

* Website Name
* Username
* Password

### Functions Used

```python
add_record()
display_records()
```

### Features

* Add Records
* Display Records
* Persistent File Storage

### Sample Output

```text
Website : Gmail
Username: user@gmail.com
Password: Test@123
```

---

# Bonus Challenge: Activity Logger

## Description

A simple logging utility that records user activities along with date and time.

### File Created

```text
activity_log.txt
```

### Logged Information

* Date
* Time
* Program Name
* User Activity

### Function Used

```python
create_log()
```

### Sample Log Entry

```text
Date: 2026-06-12
Time: 16:45:22
Program Name: Activity Logger
User Activity: Added Student Record
----------------------------------------
```

---

# Python Concepts Used

This project demonstrates the following Python concepts:

* Functions
* Parameters and Arguments
* Return Statements
* Lists
* Conditional Statements
* Loops
* File Handling
* Reading Files
* Writing Files
* Appending Data
* Exception Handling
* Menu-Driven Programming
* Data Storage
* Logging Systems

---

# How to Run

Open a terminal inside the project folder and execute:

```bash
python calculator_functions.py
```

```bash
python student_manager.py
```

```bash
python marks_analyzer.py
```

```bash
python file_handling.py
```

```bash
python password_vault.py
```

```bash
python activity_logger.py
```

---

# Learning Outcomes

Through this task, I learned:

* Creating and using functions
* Organizing code using modular programming
* Reading and writing files in Python
* Storing and retrieving data from text files
* Implementing menu-driven programs
* Creating a simple password vault
* Building a basic activity logging system

---

# Conclusion

Task 04 provided practical experience with Python functions, file handling, and structured programming. The programs developed in this task demonstrate how real-world applications store, process, and manage data using reusable and organized code.
