import pytest
from Pytest_Module.source import shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, breadth=15)


@pytest.fixture
def random_rectangle():
    return shapes.Rectangle(length=5, breadth=6)
