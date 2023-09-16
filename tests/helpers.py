import inspect


def get_methods(cls) -> list:
    return [
        method for method, _ in inspect.getmembers(cls, predicate=inspect.ismethod)
        if not method.startswith('__') and not method.endswith('__')
    ]


def AssertFor(cls, target_output):
    for method_name in get_methods(cls):
        assert getattr(cls, method_name)() == target_output
