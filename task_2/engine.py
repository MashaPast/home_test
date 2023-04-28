from typing import List
from task_2.figure import Circle, Triangle, Rectangle, Figure
from task_2.helpers.colors import AvailableColors


class Engine2D:
    """
    Class representing the Engine2D
    """

    def __init__(self):
        """
        Initializes an Engine2D object

        :param current_color: Current color for rendering
        :param canvas: Canvas for adding figures

        """
        self.current_color: str = AvailableColors.default_color.name
        self.canvas: List[Figure] = []

    def add_circle(self, center_point: tuple, radius: int):
        """
        Adds a circle to the canvas

        :param center_point: Coordinates of the circle center point
        :param radius: Radius of circle
        :return: None
        """
        circle = Circle(self.current_color, center_point, radius)
        self.canvas.append(circle)

    def add_triangle(self, a: int, b: int, c: int):
        """
        Adds a triangle to the canvas

        :param a: First side
        :param b: Second side
        :param c: Third side
        :return: None
        """
        triangle = Triangle(self.current_color, a, b, c)
        self.canvas.append(triangle)

    def add_rectangle(self, width: int, length: int):
        """
        Adds a rectangle to the canvas

        :param width: Width of rectangle
        :param length: Length of rectangle
        :return: None
        """
        rectangle = Rectangle(self.current_color, width, length)
        self.canvas.append(rectangle)

    def draw(self):
        """
        Draws all the figures from the canvas list and then cleans it

        :return: None
        """
        [el.draw() for el in self.canvas]
        self.canvas = []

    def change_color(self, new_color: str):
        """
        Changes rendering color

        :param new_color: New rendering color
        :return: None

        Raises:
        ValueError: If new color is not available.
        """
        if not (new_color.lower() in AvailableColors.__members__):
            raise ValueError(f"No such color {new_color}. "
                             f"Choose from these colors {tuple(AvailableColors.__members__.keys())}")
        self.current_color = new_color.lower()

