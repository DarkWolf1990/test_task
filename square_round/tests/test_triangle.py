import pytest
from square_round.shapes.triangle import Triangle


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert pytest.approx(t.area(), rel=1e-5) == 6.0


def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)


def test_triangle_invalid_type():
    with pytest.raises(TypeError):
        Triangle("a", 4, 5)
