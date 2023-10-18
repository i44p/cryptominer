import cryptominer
import pytest

from helpers import *


@pytest.mark.parametrize("test_input,expected", [
    (cryptominer.GreatestCommonDivisor(1234, 54), 2),
    (cryptominer.GreatestCommonDivisor(2548, 22), 2)
])
def test_gcd(test_input, expected):
    AssertFor(test_input, expected)
