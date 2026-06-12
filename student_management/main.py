"""Main entry point for the Student Management System CLI application."""

from student import Student
from file_handler import load_students, save_students


def display_menu():
    """Display the main menu options to the user."""
    print("\n" + "=" * 50)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("  1. Add Student")
    print("  2. Delete Student")
    print("  3. Search Student")
    print("  4. Show All Students")
    print("  5. Exit")
    print("=" * 50)


def get_non_empty_input(prompt):
    """Get input from user and ensure it is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty. Please try again.")


def get_valid_age():
    """Get a valid positive integer age from the user."""
    while True:
        age_input = get_non_empty_input("Enter age: ")
        try:
            age = int(age_input)
            if age > 0:
                return age
            print("Error: Age must be a positive number.")
        except ValueError:
            print("Error: Age must be a number.")


def roll_number_exists(students, roll_no):
    """Check if a roll number already exists in the student list."""
    return any(student.roll_no == roll_no for student in students)


def add_student(students):
    """Add a new student to the list after validation."""
    print("\n--- Add New Student ---")

    name = get_non_empty_input("Enter name: ")
    roll_no = get_non_empty_input("Enter roll number: ")

    if roll_number_exists(students, roll_no):
        print(f"Error: Roll number '{roll_no}' already exists. Unique roll number required.")
        return students

    grade = get_non_empty_input("Enter class/grade: ")
    age = get_valid_age()

    new_student = Student(name=name, roll_no=roll_no, grade=grade, age=age)
    students.append(new_student)

    if save_students(students):
        print(f"Success: {name} successfully added!")
    else:
        print("Warning: Student added but file save failed.")

    return students


def delete_student(students):
    """Delete a student by roll number."""
    print("\n--- Delete Student ---")
    roll_no = get_non_empty_input("Enter roll number to delete: ")

    for index, student in enumerate(students):
        if student.roll_no == roll_no:
            removed_name = student.name
            students.pop(index)
            if save_students(students):
                print(f"Success: {removed_name} (Roll: {roll_no}) deleted.")
            else:
                print("Warning: Student deleted but file save failed.")
            return students

    print(f"Error: Student with roll number '{roll_no}' not found.")
    return students


def search_student(students):
    """Search students by name or roll number (partial match supported)."""
    print("\n--- Search Student ---")
    query = get_non_empty_input("Enter name or roll number: ").lower()

    results = [
        student
        for student in students
        if query in student.name.lower() or query in student.roll_no.lower()
    ]

    if results:
        print(f"\n{len(results)} result(s) found:")
        display_students_table(results)
    else:
        print(f"Error: No student found with '{query}'.")


def display_students_table(students):
    """Display students in a formatted table in the terminal."""
    if not students:
        print("\nNo students found. Please add a student first.")
        return

    # Column widths for neat alignment
    roll_width = 10
    name_width = 20
    grade_width = 8
    age_width = 5

    separator = "-" * 50

    print(f"\n{separator}")
    print(
        f"| {'Roll No':<{roll_width - 1}}"
        f"| {'Name':<{name_width - 1}}"
        f"| {'Grade':<{grade_width - 1}}"
        f"| {'Age':<{age_width - 1}}|"
    )
    print(separator)

    for student in students:
        print(
            f"| {student.roll_no:<{roll_width - 1}}"
            f"| {student.name:<{name_width - 1}}"
            f"| {student.grade:<{grade_width - 1}}"
            f"| {student.age:<{age_width - 1}}|"
        )

    print(separator)
    print(f"Total students: {len(students)}")


def show_all_students(students):
    """Display all students in a formatted table."""
    print("\n--- Show All Students ---")
    display_students_table(students)


def main():
    """Run the main program loop with menu-driven CLI."""
    print("Student Management System started...")
    students = load_students()
    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                students = add_student(students)
            elif choice == "2":
                students = delete_student(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                show_all_students(students)
            elif choice == "5":
                print("\nThank you! Program ended. Goodbye!")
                break
            else:
                print("Error: Invalid choice. Please enter a number between 1 and 5.")
    except KeyboardInterrupt:
        print("\nProgram ended. Goodbye!")


if __name__ == "__main__":
    main()
