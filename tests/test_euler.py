import cryptominer
import pytest

from helpers import *

@pytest.mark.parametrize("test_input,expected", [
    (7, 6),
    (9, 6),
    (20, 8),
    (375, 200),
    (4364547586879, 4327920227520)
])
def test_Euler(test_input, expected):
    assert cryptominer.Euler(test_input).Euler() == expected
