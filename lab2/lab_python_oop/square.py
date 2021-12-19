from color import FigureColor
from rectangle import Rectangle

class Square(Rectangle):
    figure_type = "Квадрат"

    def __init__(self, length: float, color: str):
        self.c = FigureColor(color)
        self.l = length

    def square(self) -> float:
        return self.l**2
    
    def __repr__(self):
        return '{} {} длиной {} и площадью, равной {}'.format(self.c, self.get_figure_type(),
        self.l, self.square())