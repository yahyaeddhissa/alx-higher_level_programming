#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in "Python - Almost a circle" project.

    Attributes:
        __nb_objects (int): The number of instances of Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Create a new Base instance.

        Args:
            id (int): The identifier of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
