import math
import time

import pytest
from Pytest_Module.source import functions as my_funcs

def test_add():
    result = my_funcs.add(num_one = 4, num_two = 6)
    assert result == 10

def test_divide():
    result = my_funcs.divide(num_one = 10, num_two = 5)
    assert result == 2

def test_multiply():
    result = my_funcs.multiply(num_one = 10, num_two = 5)
    assert result == 50

#  strings
def test_add_strings():
    result = my_funcs.add(num_one="i like ", num_two="Movies & Series")
    assert result == "i like Movies & Series"

# working with errors
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_funcs.divide(num_one=5, num_two=0)





@pytest.mark.slow
def test_slow():
    time.sleep(4)
    result = my_funcs.divide(num_one=10, num_two=5)
    assert result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_funcs.add(num_one=10, num_two=20)


@pytest.mark.xfail(reason="we know we cannot divide by zero")
def test_divide_zero_broken():
    my_funcs.divide(num_one=0, num_two=5)

# Parameterization

@pytest.mark.parametrize("val, result", [(49, 7), (1, 1), (0, 0), (81,9)])
def test_square_root(val, result):
    assert result == math.sqrt(val)
