"""
Tests for the hello_world module of sample_package
"""

from sample_package import hello_world
import pytest


def test_hello_world():
    assert hello_world.hello_world() == "Hello World!"


def test_raise_exception():
    with pytest.raises(hello_world.SampleException):
        assert hello_world.raise_exception()
