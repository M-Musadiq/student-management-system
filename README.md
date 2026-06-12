# Student Management System

A simple command-line application to manage student records. Built with Python using only the standard library.

## Features

- **Add Student** — Register a new student with name, roll number, grade, and age
- **Delete Student** — Remove a student by roll number
- **Search Student** — Find students by name or roll number (partial match supported)
- **Show All Students** — Display all records in a formatted table
- **Persistent Storage** — Data is saved automatically to a JSON file

## Requirements

- Python 3.6 or higher
- No external packages required

## Project Structure

```
student_management/
├── main.py           # CLI menu and application logic
├── student.py        # Student class
├── file_handler.py   # JSON load/save utilities
└── students.json     # Student data (created/updated at runtime)
```

## How to Run

1. Open a terminal and navigate to the project folder:

   ```bash
   cd student_management
   ```

2. Start the application:

   ```bash
   python main.py
   ```

   On Windows, if `python` is not recognized, try:

   ```bash
   py main.py
   ```

3. Use the menu to add, delete, search, or list students. Choose **5** to exit.

## Usage Example

```
Student Management System started...

==================================================
       STUDENT MANAGEMENT SYSTEM
==================================================
  1. Add Student
  2. Delete Student
  3. Search Student
  4. Show All Students
  5. Exit
==================================================
Enter your choice (1-5):
```

## Data Storage

Student records are stored in `student_management/students.json`. The file is created automatically on first run if it does not exist.

## Author

M-Musadiq
