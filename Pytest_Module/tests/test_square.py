import pytest
from Pytest_Module.source import shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(4,16), (3, 9), (12, 144)])  # s x s
def test_different_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(10, 40), (5, 20), (3, 12)])  # 2(s + s)
def test_different_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter