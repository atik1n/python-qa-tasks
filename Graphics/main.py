import colorsys

from iiEngine import Engine2D, shapes

engine = Engine2D()
engine.add_shape(shapes.Circle())
engine.add_shape(shapes.Rectangle())
engine.color = 1.0, 0.0, 0.0
engine.add_shape(shapes.Triangle((0.5, -1), (0, 1), (1, 1)))
engine.draw()
engine.draw()
