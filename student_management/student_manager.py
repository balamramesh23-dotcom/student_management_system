import random

from student_management.analysis import PASS_MARK
from student_management.file_handler import load_students, save_students
from student_management.student import Student

SUBJECT_COUNT = 4


class StudentManager:
    def __init__(self):
        self.students = load_students()

    def save(self):
        save_students(self.students)

    def find_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def make_id(self):
        while True:
            student_id = str(random.randint(1000, 9999))
            if self.find_student(student_id) is None:
                return student_id

    @staticmethod
    def read_number(prompt, integer=False, minimum=0, maximum=100):
        while True:
            try:
                if integer:
                    value = int(input(prompt))
                else:
                    value = float(input(prompt))
                if minimum <= value <= maximum:
                    return value
            except ValueError:
                pass
            print(f"Enter a number from {minimum} to {maximum}.")

    def read_marks(self):
        marks = {}
        print(f"Enter exactly {SUBJECT_COUNT} subjects and their marks.")
        for number in range(1, SUBJECT_COUNT + 1):
            subject = input(f"Subject {number}: ").strip()
            marks[subject] = self.read_number(
                f"Marks for subject {number} (0-100): "
            )
        return marks

    def add_student(self):
        student = Student(
            self.make_id(),
            input("Enter name: ").strip(),
            self.read_number("Enter age: ", integer=True, minimum=1, maximum=120),
            input("Enter course: ").strip(),
            input("Enter department: ").strip(),
            input("Enter academic year: ").strip(),
            self.read_marks(),
        )
        self.students.append(student)
        self.save()
        print("Student added. ID is", student.id)

    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            student.show()

    def search_student(self):
        search_term = input(
            "Search name, course, department, year, or status: "
        ).lower()
        matches = []
        for student in self.students:
            details = " ".join(
                [
                    student.name,
                    student.course,
                    student.department,
                    student.year,
                    student.status,
                ]
            ).lower()
            if search_term in details:
                matches.append(student)

        if not matches:
            print("Student not found.")
            return
        for student in matches:
            student.show()

    def performance_report(self):
        if not self.students:
            print("No students found.")
            return

        print("\nPerformance report")
        ranked_students = sorted(
            self.students, key=lambda student: student.average, reverse=True
        )
        for student in ranked_students:
            print(f"{student.name}: {student.average:.2f} | {student.status}")

        print("\nStudents needing improvement:")
        students_needing_help = [
            student for student in self.students if student.needs_improvement
        ]
        if not students_needing_help:
            print("None")
            return

        for student in students_needing_help:
            weak_subjects = [
                subject
                for subject, mark in student.marks.items()
                if mark < PASS_MARK
            ]
            reason = ", ".join(weak_subjects) or "low average"
            print(f"{student.name} ({student.average:.2f}) - {reason}")

    def update_student(self):
        student_id = input("Enter student ID: ").strip()
        student = self.find_student(student_id)
        if student is None:
            print("Student not found.")
            return

        student.name = input("Enter new name: ").strip()
        student.age = self.read_number(
            "Enter new age: ", integer=True, minimum=1, maximum=120
        )
        student.course = input("Enter new course: ").strip()
        student.department = input("Enter new department: ").strip()
        student.year = input("Enter new academic year: ").strip()
        student.marks = self.read_marks()
        self.save()
        print("Student updated.")

    def delete_student(self):
        student_id = input("Enter student ID: ").strip()
        student = self.find_student(student_id)
        if student is None:
            print("Student not found.")
            return

        self.students.remove(student)
        self.save()
        print("Student deleted.")
