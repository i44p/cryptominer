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
    (6_700_417, True),
    (81_057_226_637, False)
])
def test_is_prime(test_input, expected):
    assert cryptominer.is_prime(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    # (cryptominer.Coprimes(1234, 54), 2)
    (cryptominer.Factorization(82_798_848), (2,) * 8 + (3,) * 5 + (11,) * 3),
    (cryptominer.Factorization(81_057_226_635), (3,) * 3 + (5,) + (7,) * 3 + (11,) * 2 + (17,) + (23,) + (37,))
])
def test_factorization(test_input, expected):
    AssertFor(test_input, expected)
