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
        assert getattr(cls, method_name)() == target_output
