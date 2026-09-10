import database

database.create_table()

while True:
    print("\n===== Student Database =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        course = input("Enter course: ")

        database.add_student(name, roll_no, course)
        print("Student added successfully!")

    elif choice == "2":
        students = database.view_students()

        if not students:
            print("No students found.")
        else:
            print("\n--- Student Details ---")
            for student in students:
                print("ID:", student[0])
                print("Name:", student[1])
                print("Roll No:", student[2])
                print("Course:", student[3])
                print("-------------------")

    elif choice == "3":
        roll_no = input("Enter roll number to search: ")

        student = database.search_student(roll_no)

        if student:
            print("\nStudent Found!")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Roll No:", student[2])
            print("Course:", student[3])
        else:
            print("Student not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
