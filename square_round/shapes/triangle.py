import math
from square_round.utils.validators import validate_positive
from square_round.shapes.base import Shape


class Triangle(Shape):
    """
    Represents a triangle defined by three sides (a, b, c).
    Uses Heron's formula to calculate area.
    """

    def __init__(self, a: float, b: float, c: float):
        for side, name in zip((a, b, c), ("a", "b", "c")):
            validate_positive(side, name)

        # Проверка существования треугольника
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Invalid triangle sides")

        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Calculate the area using Heron's formula."""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
