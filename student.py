def add_student(students):
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def display_students(students):
    if not students:
        print("No students found.")
    else:
        for student in students:
            print("\nRoll Number:", student["roll_no"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])


def search_student(students):
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found.")


def delete_student(students):
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def update_student(students):
    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            print("Student updated successfully!")
            return

    print("Student not found.")

