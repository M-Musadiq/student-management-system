"""File handling module for reading and writing student data to JSON."""

import json
import os

from student import Student


DATA_FILE = os.path.join(os.path.dirname(__file__), "students.json")


def load_students(file_path=DATA_FILE):
    """Load student list from a JSON file."""
    if not os.path.exists(file_path):
        save_students([], file_path)
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Warning: Invalid JSON format. New file created.")
        save_students([], file_path)
        return []
    except OSError as error:
        print(f"Error: File read failed: {error}")
        return []

    if not isinstance(data, list):
        print("Warning: Invalid JSON format. Empty list used.")
        return []

    students = []
    for entry in data:
        try:
            students.append(Student.from_dict(entry))
        except (KeyError, TypeError):   
            print(f"Warning: Invalid data: {entry}")

    return students


def save_students(students, file_path=DATA_FILE):
    """Save a list of Student objects to a JSON file."""

    data = [student.to_dict() for student in students]

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Error: File save failed: {error}")
        return False
