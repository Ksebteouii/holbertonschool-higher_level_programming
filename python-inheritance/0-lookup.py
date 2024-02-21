#!/usr/bin/python3

"""
This module provides a function to look up
attributes and methods of an object.
"""

def lookup(obj):
    """
    Retrieve a list of an object's attributes/methods.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of the attributes and methods of the object.
    """
    return dir(obj) 
