#!/usr/bin/python3
"""
Defines the addition function of an integer 
"""

def add_integer(a, b=98):
    """Return the sum of two integers a and b. Before addition is performed,
    float arguments are typecasted to ints

    Args:
        a: first argument
        b: second argument

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
