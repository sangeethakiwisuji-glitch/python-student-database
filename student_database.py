students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student Details ---")
    for student in students:
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Course:", student["course"])
        print("----------------------")


def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Course:", student["course"])
            return

    print("Student not found.")


while True:
    print("\n===== Student Database =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
