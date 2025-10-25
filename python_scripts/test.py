# test_add_numbers.py
from add import add_numbers

def test_add():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(25, 25) == 50
    assert add_numbers(2, 20) == 22
