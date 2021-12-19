from abc import ABC, abstractmethod

class Figure(ABC):
    figure_type  = None

    @abstractmethod
    def square():
        pass
    
    @abstractmethod
    def calculate_perimetr():
        pass

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type