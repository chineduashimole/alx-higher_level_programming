#!/usr/bin/python3

"""Square class definition"""


class Square:
    """Square class body"""

    def __init__(self, size=0):
        """Initializing a new Square.
        Args:
            size (int): The size of the new square being initialized
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
