import pytest
from task_2.engine import Engine2D
from task_2.helpers.colors import AvailableColors


class TestEngine2D:
    def test_add_figure(self):
        e = Engine2D()
        e.add_circle(center_point=(0, 1), radius=5)
        assert len(e.canvas) == 1

    def test_several_figures(self):
        e = Engine2D()
        e.add_triangle(a=2, b=3, c=4)
        e.add_circle(center_point=(0, 1), radius=5)
        e.add_rectangle(width=5, length=10)

        assert len(e.canvas) == 3

    def test_cleaning_after_draw(self):
        e = Engine2D()
        e.add_triangle(a=2, b=3, c=4)
        assert len(e.canvas) == 1
        e.draw()
        assert e.canvas == []

    def test_change_color(self):
        e = Engine2D()
        e.add_circle(center_point=(0, 1), radius=5)
        e.change_color(new_color=AvailableColors.white.name)
        e.add_rectangle(width=5, length=10)

        assert e.canvas[0].color == AvailableColors.default_color.name
        assert e.canvas[1].color == AvailableColors.white.name

    def test_negative_change_color(self):
        invalid_color: str = "no_such_color"
        e = Engine2D()
        with pytest.raises(ValueError) as error:
            e.change_color(invalid_color)
        assert str(error.value) == f"No such color {invalid_color}. " \
                                   f"Choose from these colors {tuple(AvailableColors.__members__.keys())}"
