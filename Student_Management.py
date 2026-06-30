import json
import os

FILE_NAME = "students.json"

# Load students
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save students
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    course = input("Enter Course: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student Added Successfully!")

# View students
def view_students(students):
    if not students:
        print("No students found!")
        return

    print("\n===== Student Records =====")

    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}")
        print(f"Name     : {student['name']}")
        print(f"Roll No  : {student['roll_no']}")
        print(f"Course   : {student['course']}")

# Search student
def search_student(students):
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print(f"Name    : {student['name']}")
            print(f"Roll No : {student['roll_no']}")
            print(f"Course  : {student['course']}")
            return

    print("Student Not Found!")

# Delete student
def delete_student(students):
    roll_no = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

# Main Program
students = load_students()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        delete_student(students)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")