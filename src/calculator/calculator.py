"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    MAX_VALUE = 1000000
    MIN_VALUE = -1000000

    def _validate_input(self, *values):
        for value in values:
            if value>self.MAX_VALUE or value<self.MIN_VALUE:
                raise InvalidInputException(
                    f"Input value {value} is outside the valid range "
                    f"[{self.MIN_VALUE}, {self.MAX_VALUE}]"
                )




class Calculator:
    """Calculator class providing basic arithmetic operations."""
    def __init__(self):
        self.validator = InvalidInputException()


    def add(self, a, b):
        """Add two numbers.
        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.validator._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.validator._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.validator._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        self.validator._validate_input(a, b)
        if b == 0:
            raise ValueError()
        return a / b






