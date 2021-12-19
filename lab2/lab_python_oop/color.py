class FigureColor:

    def __init__(self, color = None):
        self._color = color

    color = property()

    @color.setter
    def color(self, value):
        self._color = value

    @color.getter
    def color(self):
        return self._color
        
    def __str__(self):
        return self.color