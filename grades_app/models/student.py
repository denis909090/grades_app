from grades_app.errors.app_errors import ValidationError

MIN_GRADE = 0
MAX_GRADE = 100


class Student:
    def __init__(self, student_name: str, grades: list[int]) -> None:
        self.student_name = student_name
        self.grades = grades
        for grade in grades:
            if grade < MIN_GRADE or grade > MAX_GRADE:
                raise ValidationError("grade", f"оцінка {grade} поза діапазоном 0-100")

    def average_grade(self) -> float:
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)
