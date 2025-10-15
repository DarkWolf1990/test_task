"""
A library for calculating the areas of geometric figures.
This package provides base classes and implementations for
common shapes like Circle and Triangle.
"""

from square_round.shapes.circle import Circle
from square_round.shapes.triangle import Triangle
from square_round.shapes.base import Shape

__version__ = "0.1.0"
__author__ = "darkwolf1990"
__email__ = "whitejaguar08@gmail.com"
__url__ = "https://github.com/DarkWolf1990/test_task"

__all__ = ["Circle", "Triangle", "Shape", "calculate_area"]


def calculate_area(shape: Shape) -> float:
    """
    Calculate the area of a shape.

    This function demonstrates runtime polymorphism — it can calculate
    the area without knowing the specific shape type at compile time.

    Args:
        shape (Shape): Object that inherits from Shape class (Circle, Triangle, etc.)

    Returns:
        float: Area of the shape

    Raises:
        TypeError: If shape is not an instance of Shape

    Example:
        >>> from square_round import Circle, calculate_area
        >>> circle = Circle(5)
        >>> area = calculate_area(circle)
        >>> print(f"Area: {area:.2f}")
        Area: 78.54
    """
    if not isinstance(shape, Shape):
        raise TypeError(
            f"Shape must be an instance of Shape, got {type(shape).__name__}"
        )

    return shape.area()
