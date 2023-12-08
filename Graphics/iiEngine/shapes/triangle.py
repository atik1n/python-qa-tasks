import math
from .shape import *


class Triangle(Shape):
    _points: tuple[tuple[float, float], tuple[float, float], tuple[float, float]]

    def __init__(self, a: tuple[float, float], b: tuple[float, float], c: tuple[float, float],
                 x: float = 0, y: float = 0):
        self.points = a, b, c
        self.position = x, y

    def _draw(self):
        self._draw_log(f"Triangle {', '.join([repr_vf(point) for point in self._points])}")

    def _area(self) -> float:
        return math.fabs((self._points[1][0] - self._points[0][0]) * (self._points[2][1] - self._points[0][1]) -
                         (self._points[2][0] - self._points[0][0]) * (self._points[1][1] - self._points[0][1])) / 2

    @property
    def points(self) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float]]:
        return self._points

    @points.setter
    def points(self, value: tuple[tuple[float, float], tuple[float, float], tuple[float, float]]):
        def _point(value: tuple[float, float]):
            return validate_t(value, 2, validate_f)
        self._points = validate_t(value, 3, _point)
        if self._area() <= 0:
            raise RuntimeError("Area of triangle must be greater than 0")
