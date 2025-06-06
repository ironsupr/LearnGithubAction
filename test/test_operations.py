from src.math_operation import add, subtract
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(10, 5) == 5