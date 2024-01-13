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
        """return the new sizes of the sides of the square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
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

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __eq__(self, other):
        return self.area() == other.area()
