from figure import Figure
from color import FigureColor

class Rectangle(Figure):
    figure_type = "Прямоугольник"

    def __init__(self, width: float, height: float, color: str):
        self.w = width
        self.h = height
        self.c = FigureColor(color)

    def square(self) -> float:
        return self.w * self.h
    
    def __repr__(self):
        return '{} {} шириной {}, высотой {} и площадью, равной {}'.format(self.c, self.get_figure_type(),
        self.w, self.h, self.square())