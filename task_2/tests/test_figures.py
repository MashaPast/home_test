import pytest

from task_2.helpers.colors import AvailableColors
from task_2.figure import Circle, Triangle, Rectangle


class TestFigures:

    @pytest.mark.parametrize('figure, expected_stdout',
                             [(Circle(color=AvailableColors.default_color.name, center_point=(0, 1), radius=1),
                               "Drawing Circle: (0, 1) with radius 1."),
                              (Triangle(color=AvailableColors.default_color.name, a=2, b=3, c=4),
                               "Drawing Triangle: with side lengths a = 2, b = 3, c = 4."),
                              (Rectangle(color=AvailableColors.default_color.name, width=1, length=2),
                              "Drawing Rectangle: with width = 1 and length = 2.")])
    def test_stdout(self, capfd, figure, expected_stdout):
        figure.draw()
        stdout = capfd.readouterr()[0].strip()
        assert stdout == expected_stdout

    @pytest.mark.parametrize('radius',
                             [0, -1])
    def test_neg_create_circle(self, radius):
        with pytest.raises(ValueError) as error:
            Circle(color=AvailableColors.black.name, center_point=(0, 1), radius=radius)
        assert str(error.value) == "Such circle does not exist, radius must be greater then 0"

    def test_neg_create_triangle(self):
        with pytest.raises(ValueError) as error:
            Triangle(color=AvailableColors.black.name, a=2, b=3, c=1)
        assert str(error.value) == "Such triangle does not exist. " \
                                   "The sum of any two sides must be greater than the third"

    @pytest.mark.parametrize('width, length',
                             [(0, 3),
                              (4, 0),
                              (-1, 3),
                              (4, -1)])
    def test_neg_create_rectangle(self, width, length):
        with pytest.raises(ValueError) as error:
            Rectangle(color=AvailableColors.default_color.name, width=width, length=length)
        assert str(error.value) == "Such rectangle does not exist. None of the sides can be equal to 0 or less"

    def test_neg_create_rectangle_length_is_less_than_width(self):
        with pytest.raises(ValueError) as error:
            Rectangle(color=AvailableColors.default_color.name, width=5, length=3)
        assert str(error.value) == "Such rectangle does not exist. Length must be greater than width"
