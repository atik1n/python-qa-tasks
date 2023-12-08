import math
from typing import Any, Callable, Optional


def validate_f(value: Any) -> float:
    """
    Валидатор, может ли привестись значение к float

    :param value: значение, что нужно проверить
    :raises RuntimeError: если значение некорректно
    """
    try:
        value = float(value)
        if not math.isfinite(value):
            raise RuntimeError("Value must be a number")
        return value
    except (ValueError, TypeError):
        raise RuntimeError("Value must be a number")


def validate_t(value: Any, tlen: int = 1, func: Optional[Callable] = None) -> tuple:
    """
    Валидатор, что значение является кортежом длины len и применяет ко всем значениям func

    :param value: значение, что нужно проверить
    :param tlen: длина кортежа
    :param func: функция, что должна быть применена ко всем значениям
    :raises RuntimeError: если значение некорректно
    """
    if not isinstance(value, tuple):
        raise RuntimeError("Value must be tuple")
    if not len(value) == tlen:
        raise RuntimeError(f"Value must be tuple of size {tlen}")
    if func:
        try:
            value = tuple(map(func, value))
        except (ValueError, TypeError):
            raise RuntimeError("Values failed to comply with provided function: Value Error")
    return value
