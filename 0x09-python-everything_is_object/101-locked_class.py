#!/usr/bin/python3
"""This defines the term locked class"""

class LockedClass:
    """ Only allow initialization of the attribute first_name"""

    __slots__ = ["first_name"]
