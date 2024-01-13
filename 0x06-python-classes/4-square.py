#!/usr/bin/python3

"""Square class definition"""


class Square:
    """Square class body"""

    def __init__(self, size=0):
        """Initializing a new Square.
        Args:
            size (int): The size of the new square being initialized
        """
        self.size = size

    @property
    def size(self):
        """return the new size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the new area of the square."""
        return (self.__size * self.__size)
