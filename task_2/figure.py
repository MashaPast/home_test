from abc import ABC

from task_2.helpers.colors import AvailableColors


class Figure(ABC):

    def __init__(self, color: str):
        self.color = color

    def draw(self):
        pass


class Circle(Figure):
    def __init__(self, color: str, center_point: tuple, radius: int):
        super().__init__(color)
        if radius <= 0:
            raise ValueError("Such circle does not exist, radius must be greater then 0")
        self.center_point = center_point
        self.radius = radius

    def draw(self):
        print_circle: str = f"Drawing Circle: {self.center_point} with radius {self.radius}. "
        if self.color is AvailableColors.default_color.name:
            print(print_circle)

        else:
            print(print_circle + f"Color: {self.color}")


class Triangle(Figure):

    def __init__(self, color: str, a: int, b: int, c: int):
        super().__init__(color)
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Such triangle does not exist. The sum of any two sides must be greater than the third")
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print_triangle: str = f"Drawing Triangle: with side lengths a = {self.a}, b = {self.b}, c = {self.c}. "
        if self.color is AvailableColors.default_color.name:
            print(print_triangle)
        else:
            print(print_triangle + f"Color: {self.color}")


class Rectangle(Figure):
    def __init__(self, color: str, width: int, length: int):
        super().__init__(color)
        if width <= 0 or length <= 0:
            raise ValueError("Such rectangle does not exist. None of the sides can be equal to 0 or less")
        elif length < width:
            raise ValueError("Such rectangle does not exist. Length must be greater than width")
        self.width = width
        self.length = length

    def draw(self):
        print_rectangle: str = f"Drawing Rectangle: with width = {self.width} and length = {self.length}. "
        if self.color is AvailableColors.default_color.name:
            print(print_rectangle)
        else:
            print(print_rectangle + f"Color: {self.color}")
