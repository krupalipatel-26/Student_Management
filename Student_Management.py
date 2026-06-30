from database import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    sort_by_name,
    sort_by_marks,
    topper,
    student_count,
    backup_database,
    restore_database
)


def menu():
    while True:
        print("\n" + "=" * 50)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students by Name")
        print("7. Sort Students by Marks")
        print("8. Show Topper")
        print("9. Student Count")
        print("10. Backup Database")
        print("11. Restore Database")
        print("12. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            roll = input("Roll Number: ")
            name = input("Name: ")
            age = input("Age: ")
            gender = input("Gender: ")
            course = input("Course: ")
            marks = input("Marks: ")

            add_student(
                roll,
                name,
                age,
                gender,
                course,
                marks
            )

        elif choice == "2":
            view_students()

        elif choice == "3":
            roll = input("Enter Roll Number: ")
            search_student(roll)

        elif choice == "4":
            roll = input("Enter Roll Number to Update: ")
            update_student(roll)

        elif choice == "5":
            roll = input("Enter Roll Number to Delete: ")
            delete_student(roll)

        elif choice == "6":
            sort_by_name()

        elif choice == "7":
            sort_by_marks()

        elif choice == "8":
            topper()

        elif choice == "9":
            student_count()

        elif choice == "10":
            backup_database()

        elif choice == "11":
            restore_database()

        elif choice == "12":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid Choice! Please try again.")


if __name__ == "__main__":
    menu()
