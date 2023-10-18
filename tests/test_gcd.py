import cryptominer
import pytest

from helpers import *


@pytest.mark.parametrize("test_input,expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (7, True),
    (9, False),
    (17, True),
    (23, True),
    (25, False),
    (6_700_417, True)
])
def test_is_prime(test_input, expected):
    assert cryptominer.is_prime(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (cryptominer.GreatestCommonDivisor(1234, 54), 2),
    (cryptominer.GreatestCommonDivisor(2548, 22), 2)
])
def test_gcd(test_input, expected):
    AssertFor(test_input, expected)
