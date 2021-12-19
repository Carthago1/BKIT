from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

def main():
    rectangle = Rectangle(15.5, 20, 'Чёрный')
    circle = Circle(5, 'Коричневый')
    square = Square(17, 'Белый')
    print(rectangle, circle, square, sep = '\n')

if __name__ == '__main__':
    main()