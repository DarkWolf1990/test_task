import math
import pytest
from square_round.shapes.circle import Circle


def test_circle_area():
    circle = Circle(2)
    assert pytest.approx(circle.area(), rel=1e-5) == math.pi * 4


def test_circle_invalid_radius_type():
    with pytest.raises(TypeError):
        Circle("radius")


def test_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle(-5)
