from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.
        Must be implemented by subclasses.
        """
        raise NotImplementedError

    def compare_area(self, other: "Shape") -> bool:
        """
        Compare area with another shape.
        Returns True if areas are equal.
        """
        if not isinstance(other, Shape):
            raise TypeError(f"Expected Shape, got {type(other).__name__}")
        return self.area() == other.area()
