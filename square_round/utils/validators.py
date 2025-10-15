def validate_positive(value: float, name: str):
    """
    Ensure that a numeric value is positive.

    Args:
        value (float): The value to check.
        name (str): The name of the variable for error messages.

    Raises:
        TypeError: If value is not a number.
        ValueError: If value is not positive.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
