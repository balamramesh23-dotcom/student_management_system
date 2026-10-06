import csv
import json
from pathlib import Path

from backend.student import Student

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "students.csv"
HEADERS = [
    "id",
    "name",
    "age",
    "course",
    "department",
    "year",
    "subject_marks",
    "date",
]


def load_students():
    students = []
    if not DATA_FILE.exists():
        return students

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "subject_marks" in (reader.fieldnames or []):
                marks = json.loads(row.get("subject_marks") or "{}")
                department = row["department"]
                year = row["year"]
            else:
                grade = row.get("grade", "")
                marks = {}
                if grade.replace(".", "", 1).isdigit():
                    marks = {"Overall": float(grade)}
                department = "Unknown"
                year = "Unknown"

            marks = {subject: float(mark) for subject, mark in marks.items()}
            students.append(
                Student(
                    row["id"],
                    row["name"],
                    row["age"],
                    row["course"],
                    department,
                    year,
                    marks,
                    row["date"],
                )
            )

    return students


def save_students(students):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)
        for student in students:
            row = student.to_row()
            row[6] = json.dumps(row[6])
            writer.writerow(row)
