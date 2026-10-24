# Monitor the number of students in the weekend school

#Features to have (add students, remove students, display students, quit)
#add students details (name, age, grade, parents name, parents contact number)

students = []


def show_students(students):
    """Display all students currently registered"""

    print()
    print("Current Students:")
    print()

    if len(students) == 0:
        print("No students registered yet.")
    else:
        for student in students:
            print("-" * 35)
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            print(f"Parent's Name: {student['parent_name']}")
            print(f"Parent's Contact: {student['parent_contact']}")

    print()
    print("Options: add / view / search / remove / quit")


def prompt_for_student():
    """Prompt for the student's details"""

    name = input("Enter student's name: ").strip().title()
    age = int(input("Enter student's age: (in numbers e.g. 5) "))
    grade = input("Enter student's grade: ").strip().title()
    parent_name = input("Enter parent's full name: ").strip().title()
    parent_contact = input("Enter parent's contact number: ").strip()

    return {
        "name": name,
        "age": age,
        "grade": grade,
        "parent_name": parent_name,
        "parent_contact": parent_contact
    }


def add_student(students):
    """Add a new student"""

show_students(students)