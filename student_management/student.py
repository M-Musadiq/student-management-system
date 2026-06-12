"""Student class module for the Student Management System."""


class Student:
    """Represents a single student with basic details."""

    def __init__(self, name, roll_no, grade, age):
        """Initialize a Student object."""
        self.name = name
        self.roll_no = roll_no
        self.grade = grade
        self.age = age

    def to_dict(self):
        """Convert student data to a dictionary for JSON storage."""
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "grade": self.grade,
            "age": self.age,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        return cls(
            name=data["name"],
            roll_no=data["roll_no"],
            grade=data["grade"],
            age=int(data["age"]),
        )

    def __str__(self):
        """Return a readable string representation of the student."""
        return f"{self.name} (Roll: {self.roll_no}, Grade: {self.grade}, Age: {self.age})"
