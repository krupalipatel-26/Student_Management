import json
import os
from student import Student

# -----------------------------
# File Paths
# -----------------------------

DATABASE_FILE = "students.json"
BACKUP_FILE = "students_backup.json"


# -----------------------------
# Initialize Database
# -----------------------------

def initialize_database():
    """
    Creates students.json if it doesn't exist.
    """
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as file:
            json.dump([], file, indent=4)


# Create database when program starts
initialize_database()


# -----------------------------
# Load Students
# -----------------------------

def load_students():
    """
    Reads all students from students.json.
    Returns a list of dictionaries.
    """

    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []

    except FileNotFoundError:
        return []


# -----------------------------
# Save Students
# -----------------------------

def save_students(students):
    """
    Saves student list into JSON file.
    """

    with open(DATABASE_FILE, "w") as file:
        json.dump(students, file, indent=4)


# -----------------------------
# Add Student
# -----------------------------

def add_student(roll, name, age, gender, course, marks):
    """
    Adds a new student.
    """

    students = load_students()

    # Check duplicate Roll Number
    for student in students:
        if student["roll"] == str(roll):
            print("\n❌ Roll Number already exists.")
            return

    try:
        student = Student(
            roll,
            name,
            age,
            gender,
            course,
            marks
        )

        students.append(student.to_dict())
        save_students(students)

        print("\n✅ Student Added Successfully!")

    except ValueError:
        print("\n❌ Invalid input.")


# -----------------------------
# View Students
# -----------------------------

def view_students():
    """
    Displays all students.
    """

    students = load_students()

    if not students:
        print("\nNo students found.")
        return

    print("\n" + "=" * 90)
    print(
        f"{'Roll':<10}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Gender':<12}"
        f"{'Course':<18}"
        f"{'Marks':<10}"
    )
    print("=" * 90)

    for student in students:
        print(
            f"{student['roll']:<10}"
            f"{student['name']:<20}"
            f"{student['age']:<8}"
            f"{student['gender']:<12}"
            f"{student['course']:<18}"
            f"{student['marks']:<10}"
        )

    print("=" * 90)
    print(f"\nTotal Students : {len(students)}")

# -----------------------------
# Search Student
# -----------------------------

def search_student(roll):
    """
    Search a student by Roll Number.
    """

    students = load_students()

    for student in students:
        if student["roll"] == str(roll):

            print("\nStudent Found")
            print("-" * 40)
            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Age         : {student['age']}")
            print(f"Gender      : {student['gender']}")
            print(f"Course      : {student['course']}")
            print(f"Marks       : {student['marks']}")
            print("-" * 40)

            return student

    print("\n❌ Student not found.")
    return None


# -----------------------------
# Update Student
# -----------------------------

def update_student(roll):
    """
    Update an existing student's information.
    """

    students = load_students()

    for student in students:

        if student["roll"] == str(roll):

            print("\nLeave field blank to keep old value.\n")

            name = input(f"Name ({student['name']}): ")
            age = input(f"Age ({student['age']}): ")
            gender = input(f"Gender ({student['gender']}): ")
            course = input(f"Course ({student['course']}): ")
            marks = input(f"Marks ({student['marks']}): ")

            if name:
                student["name"] = name.title()

            if age:
                try:
                    student["age"] = int(age)
                except ValueError:
                    print("Invalid age. Old value kept.")

            if gender:
                student["gender"] = gender.title()

            if course:
                student["course"] = course.title()

            if marks:
                try:
                    student["marks"] = float(marks)
                except ValueError:
                    print("Invalid marks. Old value kept.")

            save_students(students)

            print("\n✅ Student Updated Successfully!")
            return

    print("\n❌ Student not found.")


# -----------------------------
# Delete Student
# -----------------------------

def delete_student(roll):
    """
    Delete a student by Roll Number.
    """

    students = load_students()

    for student in students:

        if student["roll"] == str(roll):

            confirm = input(
                f"Delete {student['name']}? (Y/N): "
            ).strip().lower()

            if confirm == "y":

                students.remove(student)
                save_students(students)

                print("\n✅ Student Deleted Successfully!")

            else:

                print("\nDeletion Cancelled.")

            return

    print("\n❌ Student not found.")
# -----------------------------
# Sort Students by Name
# -----------------------------

def sort_by_name():
    """
    Display students sorted alphabetically by name.
    """

    students = load_students()

    if not students:
        print("\nNo students found.")
        return

    students.sort(key=lambda student: student["name"].lower())

    print("\n" + "=" * 90)
    print("STUDENTS SORTED BY NAME")
    print("=" * 90)

    print(
        f"{'Roll':<10}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Gender':<12}"
        f"{'Course':<18}"
        f"{'Marks':<10}"
    )

    print("-" * 90)

    for student in students:
        print(
            f"{student['roll']:<10}"
            f"{student['name']:<20}"
            f"{student['age']:<8}"
            f"{student['gender']:<12}"
            f"{student['course']:<18}"
            f"{student['marks']:<10}"
        )


# -----------------------------
# Sort Students by Marks
# -----------------------------

def sort_by_marks():
    """
    Display students sorted by marks (Highest First).
    """

    students = load_students()

    if not students:
        print("\nNo students found.")
        return

    students.sort(
        key=lambda student: student["marks"],
        reverse=True
    )

    print("\n" + "=" * 90)
    print("STUDENTS SORTED BY MARKS")
    print("=" * 90)

    print(
        f"{'Rank':<6}"
        f"{'Roll':<10}"
        f"{'Name':<20}"
        f"{'Marks':<10}"
    )

    print("-" * 50)

    rank = 1

    for student in students:
        print(
            f"{rank:<6}"
            f"{student['roll']:<10}"
            f"{student['name']:<20}"
            f"{student['marks']:<10}"
        )
        rank += 1


# -----------------------------
# Display Topper
# -----------------------------

def topper():
    """
    Display the student with highest marks.
    """

    students = load_students()

    if not students:
        print("\nNo students found.")
        return

    top_student = max(
        students,
        key=lambda student: student["marks"]
    )

    print("\n" + "=" * 45)
    print("🏆 CLASS TOPPER")
    print("=" * 45)

    print(f"Roll Number : {top_student['roll']}")
    print(f"Name        : {top_student['name']}")
    print(f"Age         : {top_student['age']}")
    print(f"Gender      : {top_student['gender']}")
    print(f"Course      : {top_student['course']}")
    print(f"Marks       : {top_student['marks']}")


# -----------------------------
# Student Count
# -----------------------------

def student_count():
    """
    Display total number of students.
    """

    students = load_students()

    print("\n" + "=" * 35)
    print("STUDENT STATISTICS")
    print("=" * 35)
    print(f"Total Students : {len(students)}")

    if students:

        average = sum(student["marks"] for student in students) / len(students)

        highest = max(student["marks"] for student in students)
        lowest = min(student["marks"] for student in students)

        print(f"Average Marks : {average:.2f}")
        print(f"Highest Marks : {highest}")
        print(f"Lowest Marks  : {lowest}")

    print("=" * 35)

import shutil
import csv


# -----------------------------
# Backup Database
# -----------------------------

def backup_database():
    """
    Create a backup of the student database.
    """

    if not os.path.exists(DATABASE_FILE):
        print("\n❌ Database not found.")
        return

    try:
        shutil.copy(DATABASE_FILE, BACKUP_FILE)
        print("\n✅ Backup Created Successfully!")

    except Exception as e:
        print(f"\n❌ Backup Failed: {e}")


# -----------------------------
# Restore Database
# -----------------------------

def restore_database():
    """
    Restore database from backup.
    """

    if not os.path.exists(BACKUP_FILE):
        print("\n❌ No backup found.")
        return

    try:
        shutil.copy(BACKUP_FILE, DATABASE_FILE)
        print("\n✅ Database Restored Successfully!")

    except Exception as e:
        print(f"\n❌ Restore Failed: {e}")


# -----------------------------
# Export to CSV
# -----------------------------

def export_to_csv():
    """
    Export student records to CSV file.
    """

    students = load_students()

    if not students:
        print("\n❌ No student records found.")
        return

    try:
        with open("students.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Roll Number",
                "Name",
                "Age",
                "Gender",
                "Course",
                "Marks"
            ])

            for student in students:
                writer.writerow([
                    student["roll"],
                    student["name"],
                    student["age"],
                    student["gender"],
                    student["course"],
                    student["marks"]
                ])

        print("\n✅ Data Exported to students.csv")

    except Exception as e:
        print(f"\n❌ Export Failed: {e}")


# -----------------------------
# Reset Database
# -----------------------------

def reset_database():
    """
    Delete all student records.
    """

    confirm = input(
        "\n⚠ Are you sure you want to delete ALL records? (YES/NO): "
    ).strip().upper()

    if confirm == "YES":

        save_students([])

        print("\n✅ Database Reset Successfully!")

    else:

        print("\nOperation Cancelled.")


# -----------------------------
# About Project
# -----------------------------

def about():
    """
    Display project information.
    """

    print("\n" + "=" * 50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("Version : 1.0")
    print("Language: Python")
    print("Storage : JSON")
    print("Features:")
    print(" • Add Student")
    print(" • View Student")
    print(" • Search Student")
    print(" • Update Student")
    print(" • Delete Student")
    print(" • Sort by Name")
    print(" • Sort by Marks")
    print(" • Student Statistics")
    print(" • Backup & Restore")
    print(" • Export to CSV")
    print("=" * 50)