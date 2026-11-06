import json

from grades_app.errors.app_errors import ResourceError


def load_students_data(file_path: str) -> list[dict]:
    try:

        with open(file_path, "r", encoding="utf-8") as json_file:
            students_data = json.load(json_file)
    except FileNotFoundError as original_error:
        raise ResourceError(file_path, "файл не знайдено") from original_error
    except json.JSONDecodeError as original_error:
        raise ResourceError(file_path, "файл має некоректний JSON") from original_error
    else:

        print("  файл успішно прочитано")
        return students_data
    finally:

        print("  спроба читання файлу завершена")
