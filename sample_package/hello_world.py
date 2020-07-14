"""
Example module
"""


class SampleException(Exception):
    """
    An example custom exception
    """
    pass


def hello_world() -> str:
    """
    An example function that returns the string "Hello World!"
    :return: The string "Hello World!"
    """
    return "Hello World!"


def raise_exception() -> None:
    """
    An example function that raises a custom exception.
    :return:
    """
    raise SampleException("A sample exception was raised")
