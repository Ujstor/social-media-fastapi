import pytest
from app.calculations import add, subtract, multiply, divide


@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (7, 1, 8),
    (10, 10, 20),
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(3, 2) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2

