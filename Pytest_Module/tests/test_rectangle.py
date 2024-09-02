import pytest
from Pytest_Module.source import shapes as shapes


def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(length=10, breadth=15)
    assert my_rectangle.area() == 10 * 15

def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(length=10, breadth=15)
    assert my_rectangle.perimeter() == (10 * 2) + (15 * 2)


def test_not_equal(my_rectangle, random_rectangle):
    assert my_rectangle != random_rectangle