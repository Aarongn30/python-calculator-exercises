import pytest
from calc import compute

def test_add():
    assert compute('2', '3', 'add') == 5

def test_sub():
    assert compute(5, 2, 'sub') == 3

def test_mul():
    assert compute('3', '4', 'mul') == 12

def test_div():
    assert compute('10', '2', 'div') == 5

def test_div_by_zero():
    with pytest.raises(ValueError):
        compute('1', '0', 'div')

def test_invalid_number():
    with pytest.raises(ValueError):
        compute('a', '2', 'add')
