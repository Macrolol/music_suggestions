"""
da_exceptions.py: This file holds the exceptions common between the data access classes.
"""

__author__ = "Michael Dormon"

class DatabaseConnectionError(Exception):
    """
    An error raised when the database connection fails.
    """
    pass

class UnexpectedDatabaseError(Exception):
    """
    An error raised when the database returns an unexpected result or error.
    """
    pass


class NotFoundError(Exception):
    """
    Exception raised by the any method when the asked for entity does not
    exist in the database.
    """
    pass


class DuplicateError(Exception):
    """
    Exception raised by the any method when the entity already exists in the
    database.
    """
    pass

class InvalidDataError(Exception):
    """
    Exception raised by the any method when the data given is invalid.
    """
    pass