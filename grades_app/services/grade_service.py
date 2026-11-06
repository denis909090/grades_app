from grades_app.errors.app_errors import BusinessRuleError, ResourceError
from grades_app.models.student import Student

from .file_loader import load_students_data

MAX_SUBJECTS_PER_STUDENT = 3


def read_grade_safely(raw_text: str) -> int | None:
    try:
        grade = int(raw_text)
    except ValueError:
        print(f"  '{raw_text}' не є числом")
        return None
    return grade


def convert_grades_list(raw_values: list[str | None]) -> list[int]:
    converted_grades: list[int] = []
    for raw_value in raw_values:
        try:
            converted_grades.append(int(raw_value))
        except (ValueError, TypeError) as error:

            print(f"  пропущено '{raw_value}': {error}")
    return converted_grades


def load_students(file_path: str) -> list[Student]:
    students_data = load_students_data(file_path)
    students: list[Student] = []
    for student_item in students_data:
        student = Student(student_item["name"], student_item["grades"])
        students.append(student)
    return students


def load_students_with_logging(file_path: str) -> list[Student]:
    try:
        return load_students(file_path)
    except ResourceError:
        print("  [LOG] помилка доступу до файлу, передаю далі")
        raise


def check_subject_limit(student: Student) -> None:
    subjects_count = len(student.grades)
    if subjects_count > MAX_SUBJECTS_PER_STUDENT:
        raise BusinessRuleError(
            1001,
            f"у студента {student.student_name} забагато предметів: {subjects_count}",
        )
