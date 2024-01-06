#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """represents a rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initialize the rectangle class
        Args: 
            width: this represents the width of the rectangle
            height: this represents the height of the triangle
    
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
