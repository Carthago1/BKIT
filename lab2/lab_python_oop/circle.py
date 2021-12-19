from figure import Figure
from color import FigureColor
from math import pi

class Circle(Figure):
    figure_type = 'Круг'

    def __init__(self, radius: float, color: str):
        self.r = radius
        self.c = FigureColor(color)

    def square(self) -> float:
        return pi * self.r**2

    def __repr__(self):
        return '{} {} радиусом {} и площадью, равной {}'.format(self.c, self.get_figure_type(),
        self.r, self.square())