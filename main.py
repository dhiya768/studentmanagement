import student

students = []

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student.add_student(students)

    elif choice == "2":
        student.display_students(students)

    elif choice == "3":
        student.search_student(students)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")

