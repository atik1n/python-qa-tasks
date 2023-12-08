import math
from .shape import *


class Rectangle(Shape):
    def __init__(self, width: float = 1.0, height: float = 1.0, x: float = 0, y: float = 0):
        self.width = width
        self.height = height
        self.position = x, y

    def _draw(self):
        self._draw_log(f"Rectangle {repr_f(self._width, self._height)}")

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = validate_f(value)
        if self._width <= 0:
            raise RuntimeError("Value must be greater than zero")

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = validate_f(value)
        if self._height <= 0:
            raise RuntimeError("Value must be greater than zero")

    @property
    def box(self) -> tuple[float, float]:
        return self._width, self._height

    @box.setter
    def box(self, value: tuple[float, float]):
        self._width, self._height = validate_t(value, 2, validate_f)
