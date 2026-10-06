PASS_MARK = 40
IMPROVEMENT_AVERAGE = 50


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks.values()) / len(marks)


def calculate_status(marks):
    if not marks:
        return "No marks"
    if all(mark >= PASS_MARK for mark in marks.values()):
        return "Pass"
    return "Fail"


def needs_improvement(marks):
    return calculate_status(marks) == "Fail" or calculate_average(marks) < IMPROVEMENT_AVERAGE
