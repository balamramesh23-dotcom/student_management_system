# Student Management System

A simple Python CLI app to manage student records and marks.

## Run the project

```powershell
Set-Location "C:\Users\pc\Desktop\main project\main project"
py .\main.py
```

If `py` is not available, use:

```powershell
python .\main.py
```

## Menu options

1. Add student
2. View students
3. Search student
4. Update student
5. Delete student
6. Performance report
7. Exit

## Rules

- Python 3 is required.
- Each student has 4 subject marks.
- Age must be between 1 and 120.
- Each subject mark must be between 0 and 100.
- A student passes only if every subject mark is at least 40.
- The average is calculated from all subject marks.
- A student is marked for improvement if they fail a subject or have an average below 50.

## Project structure

```text
main project/
├── student_management/
│   ├── __init__.py
│   ├── analysis.py
│   ├── file_handler.py
│   ├── student.py
│   └── student_manager.py
├── data/
│   └── students.csv
├── .gitignore
├── main.py
└── README.md
```

Student data is saved in `data/students.csv`. The app reads and writes records from that file.
