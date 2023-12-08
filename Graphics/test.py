import pytest
import random

import iiEngine
from iiEngine import Engine2D, shapes
from iiEngine.utils import repr_f, repr_vf

EPSILON = 0.01


class TestShape:
    def test_shape_not_implemented(self):
        with pytest.raises(NotImplementedError):
            shapes.Shape()


class BaseTestShape:
    shape_type = shapes.Shape

    @pytest.fixture()
    def shape(self) -> shape_type:
        return self.shape_type()

    @pytest.fixture()
    def shape_msg(self, shape) -> str:
        raise NotImplementedError("Don't call this test directly")

    def before(self, shape) -> dict:
        return {
            "pos": shape.position,
            "scl": shape.scale,
            "rot": shape.rotation,
        }

    def test_default(self, shape):
        assert shape.position == pytest.approx((0.0, 0.0))
        assert shape.scale == pytest.approx((1.0, 1.0))
        assert shape.color == pytest.approx((1.0, 1.0, 1.0))

    def test_output(self, capfd, shape, shape_msg):
        repr_pos = repr_vf(shape.position)
        repr_scl = repr_vf(shape.scale)
        repr_rot = repr_f(shape.rotation)
        repr_col = repr_vf(shape.color)
        msg = ''.join((f"Drawing {shape_msg} at {repr_pos}, with scale {repr_scl} ",
               f"and rotated {repr_rot} degrees, colored {repr_col}\n"))
        shape.draw()
        out, err = capfd.readouterr()
        assert out == msg

    def test_invalid_position(self, shape):
        with pytest.raises(RuntimeError):
            shape.position = 0
        with pytest.raises(RuntimeError):
            shape.position = None
        with pytest.raises(RuntimeError):
            shape.position = None, None
        with pytest.raises(RuntimeError):
            shape.position = "nan"
        with pytest.raises(RuntimeError):
            shape.position = "nan", "nan"

    def test_invalid_scale(self, shape):
        with pytest.raises(RuntimeError):
            shape.scale = 0
        with pytest.raises(RuntimeError):
            shape.scale = None
        with pytest.raises(RuntimeError):
            shape.scale = None, None
        with pytest.raises(RuntimeError):
            shape.scale = "nan"
        with pytest.raises(RuntimeError):
            shape.scale = "nan", "nan"

    def test_invalid_color(self, shape):
        with pytest.raises(RuntimeError):
            shape.color = 0
        with pytest.raises(RuntimeError):
            shape.color = -1, -1, -1
        with pytest.raises(RuntimeError):
            shape.color = None
        with pytest.raises(RuntimeError):
            shape.color = None, None
        with pytest.raises(RuntimeError):
            shape.color = None, None, None
        with pytest.raises(RuntimeError):
            shape.color = "nan"
        with pytest.raises(RuntimeError):
            shape.color = "nan", "inf"
        with pytest.raises(RuntimeError):
            shape.color = "nan", "inf", "-inf"

    def test_constant_after_move(self, shape, before):
        shape.position = 10, 10
        assert (10, 10) == pytest.approx(shape.position)
        assert before["pos"] != pytest.approx(shape.position)
        assert before["scl"] == pytest.approx(shape.scale)
        assert before["rot"] == pytest.approx(shape.rotation)


class TestCircle(BaseTestShape):
    shape_type = shapes.Circle

    @pytest.fixture()
    def shape_msg(self, shape) -> str:
        return f"Circle ({shape.radius})"

    @pytest.fixture()
    def before(self, shape):
        before = super().before(shape)
        before["radius"] = shape.radius
        return before

    def test_default(self, shape):
        super().test_default(shape)
        assert shape.radius == pytest.approx(1.0)

    def test_constant_after_move(self, shape, before):
        super().test_constant_after_move(shape, before)
        assert before["radius"] == pytest.approx(shape.radius)

    def test_invalid_radius(self, shape):
        with pytest.raises(RuntimeError):
            shapes.Circle(0)
        with pytest.raises(RuntimeError):
            shapes.Circle(-1)
        with pytest.raises(RuntimeError):
            shapes.Circle("nan")
        with pytest.raises(RuntimeError):
            shapes.Circle(None)
        with pytest.raises(RuntimeError):
            shapes.Circle(shape)
        with pytest.raises(RuntimeError):
            shape.radius = 0
        with pytest.raises(RuntimeError):
            shape.radius = -1
        with pytest.raises(RuntimeError):
            shape.radius = "nan"
        with pytest.raises(RuntimeError):
            shape.radius = None
        with pytest.raises(RuntimeError):
            shape.radius = shape


class TestRectangle(BaseTestShape):
    shape_type = shapes.Rectangle

    @pytest.fixture()
    def shape_msg(self, shape) -> str:
        return f"Rectangle {repr_f(shape.width, shape.height)}"

    @pytest.fixture()
    def before(self, shape):
        before = super().before(shape)
        before["width"] = shape.width
        before["height"] = shape.height
        before["box"] = shape.box
        return before

    def test_default(self, shape):
        super().test_default(shape)
        assert shape.width == pytest.approx(1.0)
        assert shape.height == pytest.approx(1.0)
        assert shape.box == pytest.approx((1.0, 1.0))
        assert shape.box == pytest.approx((shape.width, shape.height))

    def test_constant_after_move(self, shape, before):
        super().test_constant_after_move(shape, before)
        assert before["width"] == pytest.approx(shape.width)
        assert before["height"] == pytest.approx(shape.height)
        assert before["box"] == pytest.approx(shape.box)

    def test_box(self, shape):
        assert shape.box == pytest.approx((shape.width, shape.height))
        shape.width = 2.0
        assert shape.box == pytest.approx((2.0, shape.height))
        assert shape.box == pytest.approx((shape.width, shape.height))

    def test_invalid_width(self, shape):
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width=0)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width=-1)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width="nan")
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width=None)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width=shape)
        with pytest.raises(RuntimeError):
            shape.width = 0
        with pytest.raises(RuntimeError):
            shape.width = -1
        with pytest.raises(RuntimeError):
            shape.width = "nan"
        with pytest.raises(RuntimeError):
            shape.width = None
        with pytest.raises(RuntimeError):
            shape.width = shape

    def test_invalid_height(self, shape):
        with pytest.raises(RuntimeError):
            shapes.Rectangle(height=0)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(height=-1)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(height="nan")
        with pytest.raises(RuntimeError):
            shapes.Rectangle(height=None)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(height=shape)
        with pytest.raises(RuntimeError):
            shape.height = 0
        with pytest.raises(RuntimeError):
            shape.height = -1
        with pytest.raises(RuntimeError):
            shape.height = "nan"
        with pytest.raises(RuntimeError):
            shape.height = None
        with pytest.raises(RuntimeError):
            shape.height = shape

    def test_invalid_box(self, shape):
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width=0, height=0)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width=-1, height=-1)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width="nan", height="inf")
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width=None, height=None)
        with pytest.raises(RuntimeError):
            shapes.Rectangle(width=shape, height=shape)
        with pytest.raises(RuntimeError):
            shape.box = 0
        with pytest.raises(RuntimeError):
            shape.box = None
        with pytest.raises(RuntimeError):
            shape.box = None, None
        with pytest.raises(RuntimeError):
            shape.box = "nan"
        with pytest.raises(RuntimeError):
            shape.box = "nan", "inf"

class TestTriangle(BaseTestShape):
    shape_type = shapes.Triangle

    @pytest.fixture()
    def shape_msg(self, shape) -> str:
        return f"Triangle {', '.join([repr_vf(point) for point in shape.points])}"

    @pytest.fixture()
    def shape(self):
        return shapes.Triangle((0.5, -1), (0, 1), (1, 1))

    @pytest.fixture()
    def before(self, shape):
        before = super().before(shape)
        before["points"] = shape.points
        return before

    def test_default(self, shape):
        with pytest.raises(TypeError):
            shapes.Triangle()  # Нет "стандартного" треугольника

    def test_constant_after_move(self, shape, before):
        super().test_constant_after_move(shape, before)
        for rhs, lhs in zip(before["points"], shape.points):
            assert rhs == pytest.approx(lhs)

    def test_points(self, shape):
        for rhs, lhs in zip(shape.points, ((0.5, -1), (0, 1), (1, 1))):
            assert rhs == pytest.approx(lhs)
        shape.points = shape.points[::-1]
        for rhs, lhs in zip(shape.points, ((1, 1), (0, 1), (0.5, -1))):
            assert rhs == pytest.approx(lhs)

    def test_invalid_area(self, shape):
        with pytest.raises(RuntimeError):
            shapes.Triangle((0, 0), (0, 0), (0, 0))
        with pytest.raises(RuntimeError):
            shapes.Triangle((0, 0), (1, 1), (0, 0))
        with pytest.raises(RuntimeError):
            shapes.Triangle((0, 0), (0, 0.5), (0, 1))
        with pytest.raises(RuntimeError):
            shape.points = (0, 0), (0, 0), (0, 0)
        with pytest.raises(RuntimeError):
            shape.points = (0, 0), (1, 1), (0, 0)
        with pytest.raises(RuntimeError):
            shape.points = (0, 0), (0, 0.5), (0, 1)

    def test_invalid_points(self, shape):
        with pytest.raises(RuntimeError):
            shapes.Triangle(0, 0, 0)
        with pytest.raises(RuntimeError):
            shapes.Triangle(-1, -1, -1)
        with pytest.raises(RuntimeError):
            shapes.Triangle("nan", "inf", "-inf")
        with pytest.raises(RuntimeError):
            shapes.Triangle(None, None, None)
        with pytest.raises(RuntimeError):
            shapes.Triangle(shape, shape, shape)
        with pytest.raises(RuntimeError):
            shape.points = 0
        with pytest.raises(RuntimeError):
            shape.points = 0, 0
        with pytest.raises(RuntimeError):
            shape.points = 0, 0, 0


class TestEngine:
    @pytest.fixture()
    def engine(self) -> iiEngine.Engine2D:
        return iiEngine.Engine2D()

    def test_draw(self, capfd, engine):
        engine.add_shape(shapes.Circle())
        engine.add_shape(shapes.Rectangle())
        engine.add_shape(shapes.Triangle((0.5, -1), (0, 1), (1, 1)))
        engine.draw()
        out, err = capfd.readouterr()
        msg = ''.join((
            "Drawing Circle (1.0) at (0.00, 0.00), with scale (1.00, 1.00) and rotated (0.00) degrees, ",
            "colored (1.00, 1.00, 1.00)\n",
            "Drawing Rectangle (1.00, 1.00) at (0.00, 0.00), with scale (1.00, 1.00) and rotated (0.00) degrees, ",
            "colored (1.00, 1.00, 1.00)\n",
            "Drawing Triangle (0.50, -1.00), (0.00, 1.00), (1.00, 1.00) at (0.00, 0.00), with scale (1.00, 1.00) ",
            "and rotated (0.00) degrees, colored (1.00, 1.00, 1.00)\n",
        ))  # "Стандартная" строка при "стандартных" фигурах, если она изменилась - что-то поменялось в формате вывода
        assert out == msg

    def test_post_draw(self, capfd, engine):
        engine.add_shape(shapes.Circle())
        engine.add_shape(shapes.Rectangle())
        engine.add_shape(shapes.Triangle((0.5, -1), (0, 1), (1, 1)))
        engine.draw()
        assert len(engine._canvas._shapes) == 0

    def test_color(self, capfd, engine):
        engine.color = 1.0, 0.0, 0.0
        engine.add_shape(shapes.Circle())
        engine.color = 0.0, 1.0, 0.0
        engine.add_shape(shapes.Rectangle())
        engine.color = 0.0, 0.0, 1.0
        engine.add_shape(shapes.Triangle((0.5, -1), (0, 1), (1, 1)))
        engine.draw()
        out, err = capfd.readouterr()
        msg = ''.join((
            "Drawing Circle (1.0) at (0.00, 0.00), with scale (1.00, 1.00) and rotated (0.00) degrees, ",
            "colored (1.00, 0.00, 0.00)\n",
            "Drawing Rectangle (1.00, 1.00) at (0.00, 0.00), with scale (1.00, 1.00) and rotated (0.00) degrees, ",
            "colored (0.00, 1.00, 0.00)\n",
            "Drawing Triangle (0.50, -1.00), (0.00, 1.00), (1.00, 1.00) at (0.00, 0.00), with scale (1.00, 1.00) ",
            "and rotated (0.00) degrees, colored (0.00, 0.00, 1.00)\n",
        ))
        assert out == msg

    def test_invalid_add(self, engine):
        with pytest.raises(RuntimeError):
            engine.add_shape(0)
        with pytest.raises(RuntimeError):
            engine.add_shape(None)
        with pytest.raises(RuntimeError):
            engine.add_shape(engine)

    def test_invalid_color(self, engine):
        with pytest.raises(RuntimeError):
            engine.color = 0
        with pytest.raises(RuntimeError):
            engine.color = -1, -1, -1
        with pytest.raises(RuntimeError):
            engine.color = None
        with pytest.raises(RuntimeError):
            engine.color = None, None
        with pytest.raises(RuntimeError):
            engine.color = None, None, None
        with pytest.raises(RuntimeError):
            engine.color = "nan"
        with pytest.raises(RuntimeError):
            engine.color = "nan", "inf"
        with pytest.raises(RuntimeError):
            engine.color = "nan", "inf", "-inf"
