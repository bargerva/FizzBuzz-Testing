"""A FizzBuzz program"""

# import necessary support classes
from numbers import Number

def Fizz(x): 
    """
        Checks to see if an input is numeric and is a multiple of 3. 
        Returns 'Fizz' if it is.
        Returns the input if it is not.
    """
    return 'Fizz' if isinstance(x,Number) and x % 3 == 0 else x

def Buzz(x): 
    """
        Checks to see if an input is numeric and is a multiple of 5. 
        Returns 'Buzz' if it is.
        Returns the input if it is not.
    """
    return 'Buzz' if isinstance(x, Number) and x % 5 == 0 else x

def FizzBuzz(x):
    """
        Checks to see if a number is a multiple of 15, 
        Returns 'FizzBuzz' if it is.
        Returns the input if it is not
    """
    return 'FizzBuzz' if isinstance(x, Number) and x % 15 == 0 else x

def play_FizzBuzz(start, end):
    """
        Generate the output for an actual FizzBuzz game
        starting at 'start' and ending at 'end'.
    """
    #initialize the output to be an empty collection (array)
    output = []
    # Loop through numbers from start to end
    for x in range(start, end + 1):
        output.append(Buzz(Fizz(FizzBuzz(x))))
    #return the output array
    return output

def can_play_FizzBuzz(start, end):
    """ 
    Demonstrate that we can generate the correct output
    for a minimal test case of the actual FizzBuzz game.
    """
    assert play_FizzBuzz(1, 15) == [
        1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'
    ]
    