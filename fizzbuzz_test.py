# pylint: disable=unused-variable 
"""Units test for FizzBuzz"""

# import the code to be tested
from fizzbuzz import Fizz, Buzz, FizzBuzz

# import method to test errors
from pytest import raises

def describe_a_FizzBuzz_program_that ():
    """A program to play the FizzBuzz game."""

    def has_a_smoke_test ():
        """Make sure our testing infrastructure is working."""
        assert True == True

    def describes_a_function_Fizz_that ():
        """Tests related to our Fizz() function."""

    def throws_an_error_if_no_input ():
        with raises(TypeError) as exception_info:
            Fizz() # pylint: disable=no-value-for-parameter
            assert exception_info.type == TypeError
            assert "missing 1 required positional argument" in str(exception_info.value)

    def returns_Fizz_if_x_is_multiple_of_3 ():
        """
        Checks to see if a number is a multiple of 3, 
        Returns 'Fizz' if it is.
        Returns the input if it is not
        """
        #if it is a multiple of three then it is equal to zero
        #if it is a non-number of three then it is not equal to zero
        assert Fizz(3) == 'Fizz'        # multiple of three 
        assert Fizz(2) == 2             # non-multiple of three
        assert Fizz(0) == 'Fizz'        # zero
        assert Fizz(-3) == 'Fizz'       # negative multiple of three
        assert Fizz(-4) == -4           # negative non-multiple of three
        assert Fizz('Buzz') == 'Buzz'   # non-number input       

    def describes_a_function_Buzz_that ():
        """Tests related to our Buzz() function."""

        def throws_an_error_if_no_input ():
            with raises(TypeError) as exception_info:
                Buzz() # pylint: disable=no-value-for-parameter
                assert exception_info.type == TypeError
                assert "missing 1 required positional argument" in str(exception_info.value)

    def returns_Buzz_if_x_is_multiple_of_5 ():
        """
        Checks to see if a number is a multiple of 5, 
        Returns 'Buzz' if it is.
        Returns the input if it is not
        """
        #if it is a multiple of five then it is equal to zero
        #if it is a non-number of five then it is not equal to zero
        assert Buzz(5) == 'Buzz'        # multiple of five 
        assert Buzz(2) == 2             # non-multiple of five
        assert Buzz(0) == 'Buzz'        # zero
        assert Buzz(-5) == 'Buzz'       # negative multiple of five
        assert Buzz(-4) == -4           # negative non-multiple of five
        assert Buzz('Fizz') == 'Fizz'   # non-number input

    def describes_a_function_FizzBuzz_that ():
        """Tests related to our FizzBuzz() function."""

        def throws_an_error_if_no_input ():
            with raises(TypeError) as exception_info:
                FizzBuzz() # pylint: disable=no-value-for-parameter
                assert exception_info.type == TypeError
                assert "missing 1 required positional argument" in str(exception_info.value)

    def returns_FizzBuzz_if_x_is_multiple_of_15 ():
        """
        Checks to see if a number is a multiple of 15, 
        Returns 'FizzBuzz' if it is.
        Returns the input if it is not
        """
        assert FizzBuzz(15) == 'FizzBuzz'   # multiple of fifteen 
        assert FizzBuzz(2) == 2             # non-multiple of fifteen
        assert FizzBuzz(0) == 'FizzBuzz'    # zero
        assert FizzBuzz(-15) == 'FizzBuzz'  # negative multiple of fifteen
        assert FizzBuzz(-4) == -4           # negative non-multiple of fifteen
        assert FizzBuzz('Fizz') == 'Fizz'   # non-number input