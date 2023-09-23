import inspect


def get_methods(cls) -> list[str]:
    """Возвращает все user-defined методы класса.

    Returns:
        list[str]: Список строк с названиями методов
    """
    return [
        method for method, _ in inspect.getmembers(cls, predicate=inspect.ismethod)
        if not (method.startswith('__') or method.endswith('__'))
    ]


def AssertFor(cls, target_output):
    """Сравнивает возвращаемое значение всех методов класса с заданным.

    Args:
        target_output (any type): Значение, с которым сравнивать
    """
    for method_name in get_methods(cls):
        result = getattr(cls, method_name)()
        assert result == target_output, f"method {method_name} failed (got {result} instead of {target_output})"


def AssertForFunc(cls, comparison_func):
    """Проверяет истинность функцииб в которую были переданы результаты работы всех методов класса.

    Args:
        target_output (any type): Значение, с которым сравнивать
    """
    for method_name in get_methods(cls):
        result = getattr(cls, method_name)()
        assert comparison_func(*result), f"method {method_name} failed (got {result})"
