import math
from square_round.utils.validators import validate_positive
from square_round.shapes.base import Shape

class Circle(Shape):
    """
    Represents a circle with a given radius.
    """

    def __init__(self, radius: float):
        validate_positive(radius, "radius")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2
