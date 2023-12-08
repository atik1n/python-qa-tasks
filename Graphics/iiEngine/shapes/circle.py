from .shape import *


class Circle(Shape):
    def __init__(self, radius: float = 1.0, x: float = 0, y: float = 0):
        self.radius = radius
        self.position = x, y

    def _draw(self):
        self._draw_log(f"Circle ({self._radius})")

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = validate_f(value)
        if self._radius <= 0:
            raise RuntimeError("Value must be greater than zero")
