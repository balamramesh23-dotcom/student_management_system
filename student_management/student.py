import datetime

from student_management.analysis import (
    calculate_average,
    calculate_status,
    needs_improvement,
)


class Student:
    def __init__(self, student_id, name, age, course, department, year, marks=None, date=None):
        self.id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.department = department
        self.year = year
        self.marks = marks or {}
        self.date = date or str(datetime.date.today())

    @property
    def average(self):
        return calculate_average(self.marks)

    @property
    def status(self):
        return calculate_status(self.marks)

    @property
    def needs_improvement(self):
        return needs_improvement(self.marks)

    def show(self):
        marks_text = ", ".join(
            f"{subject}: {mark:g}" for subject, mark in self.marks.items()
        )
        print(
            f"{self.id} | {self.name} | Age: {self.age} | Course: {self.course} | "
            f"Department: {self.department} | Year: {self.year} | "
            f"Marks: {marks_text or 'None'} | Average: {self.average:.2f} | "
            f"Status: {self.status}"
        )

    def to_row(self):
        return [
            self.id,
            self.name,
            self.age,
            self.course,
            self.department,
            self.year,
            self.marks,
            self.date,
        ]
