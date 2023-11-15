import cryptominer
import pytest

from helpers import *


@pytest.mark.parametrize("test_input,expected", [
    (cryptominer.CongruenceSystem(7), [1, 2, 3, 4, 5, 6]),
    (cryptominer.CongruenceSystem(9), [1, 2, 4, 5, 7, 8]),
    (cryptominer.CongruenceSystem(20), [1, 3, 7, 9, 11, 13, 17, 19]),
    (cryptominer.CongruenceSystem(12), [1, 5, 7, 11]),
    
])
def test_congruence_system(test_input, expected):
    AssertFor(test_input, expected)
