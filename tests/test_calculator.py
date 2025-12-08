"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        calc = Calculator()
        assert calc.add(5, 3) == 8

    def test_add_negative_numbers(self):
        #Test adding two negative numbers.
        calc = Calculator()
        assert calc.add(-5, -3) == -8

    def test_add_positive_and_negative(self):
        #Test adding positive and negative numbers.
        calc = Calculator()
        assert calc.add(5, -3) == 2

    def test_add_negative_and_positive(self):
        #Test adding negative and positive numbers.
        calc = Calculator()
        assert calc.add(-5, 3) == -2


    def test_add_positive_with_zero(self):
        #Test adding positive number with zero.
        calc = Calculator()
        assert calc.add(5, 0) == 5

    def test_add_zero_with_positive(self):
        #Test adding zero with positive number.

        calc = Calculator()
        assert calc.add(0, 5) == 5
    
    def test_add_float(self):
        #Test adding floating point numbers.
        calc = Calculator()
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)

    # Kills the mutant "validate only a"
    def test_add_validates_second_arg(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(1, InvalidInputException.MAX_VALUE + 1)

    def test_add_both_operands(self):
        calc = Calculator()
        assert calc.add(50, 1) == 51 # Normal addition
        assert calc.add(1, 50) == 51 # Ensures addition works regardless of argument order.
        assert calc.add(3, 2) != 2   # Kills mutant that incorrectly return the secomd argument (b))
        assert calc.add(2, 2) == 4   # Addition for equal operand 
    
    def test_add_max_boundary(self):
        #Boundary check
        #Check boundary conditions at max and min values.
        calc = Calculator()
        assert calc.add(InvalidInputException.MAX_VALUE, 0) == InvalidInputException.MAX_VALUE
        assert calc.add(0, InvalidInputException.MAX_VALUE) == InvalidInputException.MAX_VALUE

class TestSubtraction:
    """Tests for the subtract method."""
    def test_subtract_positive_numbers(self):
        #Test subtracting positive numbers.
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
    def test_sub_negative_numbers(self):
        #Test subtracting negative numbers.
        calc = Calculator()
        assert calc.subtract(-5, -3) == -2

    def test_sub_positive_and_negative(self):
        #Test subtracting positive and negative numbers.
        calc = Calculator()
        assert calc.subtract(5, -3) == 8

    def test_sub_float(self):
        #Test subtracting floating point numbers.
        calc = Calculator()
        assert calc.subtract(2.5, 3.7) == pytest.approx(-1.2)

    def test_sub_validates_second_arg(self):
        #Check that subtract raises InvalidInputException if the second argument exceeds the allowed maximum.
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1, InvalidInputException.MAX_VALUE + 1)

    # Reinforced test to kill “return a”, “return b”, or “a - b → a + b”
    def test_sub_both_operands(self):
        calc = Calculator()
        assert calc.subtract(50, 1) == 49  # Normal subtraction (positive result)
        assert calc.subtract(1, 50) == -49 # Normal subtraction (negative result)
        assert calc.subtract(2, 2) != 2    # Kills mutant that incorrectly return the first argument (a))
        assert calc.subtract(2, 2) == 0    # Confirm zero result


    
    def test_sub_max_boundary(self):
        #Boundary check
        #Check boundary conditions at max and min values.
        calc = Calculator()
        assert calc.subtract(InvalidInputException.MAX_VALUE, 0) == InvalidInputException.MAX_VALUE
        assert calc.subtract(0, InvalidInputException.MIN_VALUE) == InvalidInputException.MAX_VALUE


    def test_subtract_validates_first_argument_too_large(self):
        #Check that subtract raises an exception if the first argument exceeds the maximum allowed value.
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(InvalidInputException.MAX_VALUE + 1, 0)
  
class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        # Test multiplying two positive numbers
        calc = Calculator()
        assert calc.multiply(2, 4) == 8

    # Reinforced test to kill “return a”, “return b”, or “* → +”
    def test_multiply_both_operands(self):
        calc = Calculator()
        assert calc.multiply(5, 3) != 5 # kills mutants that return first arg
        assert calc.multiply(5, 3) != 3 # kills mutants that return second arg
        assert calc.multiply(2, 3) != 2 # kills mutants that return first arg
        assert calc.multiply(2, 3) != 3 # kills mutants that return second arg

    def test_multiply_max_boundary(self):
        #Boundary test
        calc = Calculator()
        # Ensure that input is validated before multiplication
        assert calc.multiply(InvalidInputException.MAX_VALUE, 1) == InvalidInputException.MAX_VALUE
        assert calc.multiply(1, InvalidInputException.MAX_VALUE) == InvalidInputException.MAX_VALUE

    def test_multiply_first_arg_too_large(self):
         #Test to ensures that multiplying a number that’s too large as the first argument raises InvalidInputException
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            
            calc.multiply(InvalidInputException.MAX_VALUE + 1, 1)

    def test_multiply_second_arg_too_large(self):
         #Test to ensures that multiplying a number that’s too large as the second argument raises InvalidInputException
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1, InvalidInputException.MAX_VALUE + 1)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        # Test dividing two positive numbers
        calc = Calculator()
        assert calc.divide(4, 2) == 2

    def test_divide_by_zero(self):
        # Test that dividing by zero raises ValueError
        calc = Calculator()
        with pytest.raises(ValueError, match=""):
            calc.divide(5, 0)


    # Reinforced test to kill “return a”, “return b”, “/ → *”
    def test_div_both_operands(self):
        calc = Calculator()
        assert calc.divide(9, 3) == 3       # correct result
        assert calc.divide(5, 3) != 5     # Mutant returning first operand instead of result
        assert calc.divide(9, 3) != 27   # Not multiplication
        assert calc.divide(5, 3) != 3     # Mutant returning second operand instead of result
        assert calc.divide(0, 5) == 0       # Tests division when the numerator is 0
        assert calc.divide(5, 1) == 5       # Tests division when the denominator is 1
    
    def test_divide_max_boundary(self):
        # Boundary test
        calc = Calculator()
        assert calc.divide(InvalidInputException.MAX_VALUE, 1) == InvalidInputException.MAX_VALUE

    def test_divide_first_arg_too_large(self):
        #Test to ensures that dividing a number that’s too large as the first argument raises InvalidInputException
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(InvalidInputException.MAX_VALUE + 1, 1)

    def test_divide_second_arg_too_large(self):
        #Test to ensures that dividing a number that’s too large as the second argument raises InvalidInputException
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1, InvalidInputException.MAX_VALUE + 1)

    

class TestInvalidInput:
    """Tests for invalid input handling."""

    def test_too_large_first_arg(self):
        # Test that adding a number larger than the allowed maximum in the first argument raises an exception
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(InvalidInputException.MAX_VALUE + 1, 0)

    def test_too_large_second_arg(self):
        # Test that adding a number larger than the allowed maximum in the second argument raises an exception
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, InvalidInputException.MAX_VALUE + 1)

    def test_too_small_first_arg(self):
        # Test that adding a number smaller than the allowed minimum in the first argument raises an exception
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(InvalidInputException.MIN_VALUE - 1, 0)

    def test_too_small_second_arg(self):
        # Test that adding a number smaller than the allowed minimum in the second argument raises an exception
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, InvalidInputException.MIN_VALUE - 1)

    def test_at_max_ok(self):
        # Test that the maximum allowed value is accepted without raising an exception
        calc = Calculator()
        calc.validator._validate_input(InvalidInputException.MAX_VALUE)

    def test_at_min_ok(self):
        # Test that the minimum allowed value is accepted without raising an exception
        calc = Calculator()
        calc.validator._validate_input(InvalidInputException.MIN_VALUE)

    def test_value_below_min(self):
        # Test that a value below the minimum raises an InvalidInputException with the correct error message
        calc = Calculator()

        with pytest.raises(InvalidInputException, match="outside the valid range"):
            calc.validator._validate_input(InvalidInputException.MIN_VALUE - 1)


      
    


