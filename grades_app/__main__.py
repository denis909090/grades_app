from grades_app.errors.app_errors import AppError, BusinessRuleError, ResourceError, ValidationError
from grades_app.models.student import Student
from grades_app.services import (
    check_subject_limit,
    convert_grades_list,
    load_students_with_logging,
    read_grade_safely,
)
from grades_app.services.file_loader import load_students_data

GOOD_FILE = "data/students.json"
BROKEN_FILE = "data/students_broken.json"
MISSING_FILE = "data/no_such_file.json"


def demo_try_except() -> None:

    print("\n try/except ")
    print("Успішний шлях:", read_grade_safely("85"))
    print("Помилковий шлях:", read_grade_safely("abc"))


def demo_try_except_else_finally() -> None:
    print("\n  try/except/else/finally ")
    print("Успішний шлях:")
    load_students_data(GOOD_FILE)
    print("Помилковий шлях:")
    try:
        load_students_data(MISSING_FILE)
    except ResourceError as error:
        print("  перехоплено:", error)


def demo_multiple_exception_types() -> None:

    print("\n  except (ValueError, TypeError) ")
    raw_values = ["90", "abc", None, "75"]
    print("Результат:", convert_grades_list(raw_values))


def demo_custom_exceptions() -> None:
    print("\n Власні виключення ")
    try:
        Student("Іван", [120])
    except ValidationError as error:
        print("Конкретний клас ValidationError:", error)

    try:
        check_subject_limit(Student("Олена", [80, 90, 70, 60]))
    except BusinessRuleError as error:
        print("Конкретний клас BusinessRuleError:", error)
    try:
        check_subject_limit(Student("Олена", [80, 90, 70, 60]))
    except AppError as error:
        print("Через базовий клас AppError:", error)


def demo_exception_chain() -> None:
    print("\n Ланцюжок виключень (raise from) ")
    try:
        load_students_data(BROKEN_FILE)
    except ResourceError as error:
        print("Доменна помилка:", error)
        print("Оригінальна причина (__cause__):", repr(error.__cause__))


def demo_reraise() -> None:

    print("\n Повторне піднесення (raise) ")
    try:
        load_students_with_logging(MISSING_FILE)
    except ResourceError:
        print("У main: помилку перехоплено після логування")


def demo_star_import() -> None:
    print("\n __all__ і from grades_app.services import * ")
    star_namespace: dict = {}
    exec("from grades_app.services import *", star_namespace)
    exported_names = sorted(name for name in star_namespace if not name.startswith("__"))
    print("Експортовано:", exported_names)
    print("load_students_data експортовано?", "load_students_data" in star_namespace)


def demo_introspection() -> None:
    print("\n Інтроспекція ")
    print("__name__:", load_students_data.__name__)
    print("__annotations__:", load_students_data.__annotations__)
    print("__doc__ класу Student:", Student.__doc__)
    help(Student.average_grade)


def main() -> None:
    demo_try_except()
    demo_try_except_else_finally()
    demo_multiple_exception_types()
    demo_custom_exceptions()
    demo_exception_chain()
    demo_reraise()
    demo_star_import()
    demo_introspection()


if __name__ == "__main__":
    main()
