import iiEngine.shapes as shapes
from iiEngine.utils import *


class Engine2D:
    class Canvas:
        def __init__(self):
            self._color: tuple[int, int, int] = (1, 1, 1)
            self._shapes: list[shapes.Shape] = list()

        @property
        def color(self) -> tuple[float, float, float]:
            return self._color

        @color.setter
        def color(self, value: tuple[float, float, float]):
            self._color = validate_t(value, 3, validate_f)
            if any(_ < 0 for _ in self._color):
                raise RuntimeError("Value must be greater than zero")

        def add_shape(self, shape: shapes.Shape):
            if not isinstance(shape, shapes.Shape):
                raise RuntimeError("Shape must be an instance of Shape")

            shape.color = self._color
            self._shapes.append(shape)

        def draw(self):
            for shape in self._shapes:
                shape.draw()
            self._shapes = list()

    _canvas: Canvas = Canvas()

    @property
    def color(self) -> tuple[float, float, float]:
        return self._canvas.color

    @color.setter
    def color(self, color: tuple[float, float, float]):
        self._canvas.color = color

    def add_shape(self, shape: shapes.Shape):
        self._canvas.add_shape(shape)

    def draw(self):
        self._canvas.draw()
