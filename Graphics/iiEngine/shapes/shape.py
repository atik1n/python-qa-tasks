from ..utils import *


class Shape:
    _pos: tuple[float, float] = (0.0, 0.0)
    _rot: float = 0
    _scl: tuple[float, float] = (1.0, 1.0)
    _col: tuple[float, float, float] = (1.0, 1.0, 1.0)

    def __init__(self, x: float = 0, y: float = 0):
        raise NotImplementedError("Do not use base Shape class")

    def _draw(self):
        raise NotImplementedError("Do not use base Shape class")

    def draw(self):
        self._draw()

    @property
    def position(self):
        return self._pos

    @position.setter
    def position(self, value: tuple[float, float]):
        self._pos = validate_t(value, 2, validate_f)


    @property
    def rotation(self) -> float:
        return self._rot

    @rotation.setter
    def rotation(self, value: float):
        self._rot = validate_f(value)

    @property
    def scale(self) -> tuple[float, float]:
        return self._scl

    @scale.setter
    def scale(self, value: tuple[float, float]):
        self._scl = validate_t(value, 2, validate_f)

    @property
    def color(self) -> tuple[float, float, float]:
        return self._col

    @color.setter
    def color(self, value: tuple[float, float, float]):
        self._col = validate_t(value, 3, validate_f)
        if any(_ < 0 for _ in self._col):
            raise RuntimeError("Value must be greater than zero")

    def _draw_log(self, msg: str):
        repr_pos = repr_vf(self._pos)
        repr_scl = repr_vf(self._scl)
        repr_rot = repr_f(self._rot)
        repr_col = repr_vf(self._col)
        msg = f"Drawing {msg} at {repr_pos}, with scale {repr_scl} and rotated {repr_rot} degrees, colored {repr_col}"
        print(msg)
