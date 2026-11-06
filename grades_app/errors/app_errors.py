class AppError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        
        return f"[AppError] {self.message}"


class ValidationError(AppError):
    def __init__(self, field_name: str, message: str) -> None:

        super().__init__(message)
        self.field_name = field_name

    def __str__(self) -> str:

        return f"[ValidationError] поле '{self.field_name}': {self.message}"


class ResourceError(AppError):
    def __init__(self, resource_path: str, message: str) -> None:
        super().__init__(message)
        self.resource_path = resource_path

    def __str__(self) -> str:
        return f"[ResourceError] ресурс '{self.resource_path}': {self.message}"


class BusinessRuleError(AppError):
    def __init__(self, error_code: int, message: str) -> None:
        super().__init__(message)
        self.error_code = error_code

    def __str__(self) -> str:
        return f"[BusinessRuleError {self.error_code}] {self.message}"
