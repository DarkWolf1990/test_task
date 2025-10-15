import pytest
from square_round import Circle, Triangle, calculate_area


def test_calculate_area_circle():
    c = Circle(3)
    assert pytest.approx(calculate_area(c), rel=1e-5) == 28.27433388


def test_calculate_area_triangle():
    t = Triangle(3, 4, 5)
    assert pytest.approx(calculate_area(t), rel=1e-5) == 6.0


def test_calculate_area_invalid():
    with pytest.raises(TypeError):
        calculate_area("not_a_shape")
