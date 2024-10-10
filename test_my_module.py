#test_my_module.py

import pytest
from my_module import add, subtract

# Test for the add function
def test_add():
    assert add(2, 3) == 5  # Expected result is 5
    assert add(-1, 1) == 0  # Expected result is 0
    assert add(0, 0) == 0  # Expected result is 0

# Test for the subtract function
def test_subtract():
    assert subtract(5, 3) == 2  # Expected result is 2
    assert subtract(10, 5) == 5  # Expected result is 5
    assert subtract(0, 0) == 0  # Expected result is 0

