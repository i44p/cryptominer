import cryptominer
import pytest

from helpers import *


@pytest.mark.parametrize("test_input,expected", [
    (cryptominer.Coprimes(2548, 22), (5, -579)),
    (cryptominer.Coprimes(25_521, 470), (-3, 163))
])
def test_coprimes_defined(test_input, expected):
    AssertFor(test_input, expected)


def test_coprimes_generated():
    for a in range(2, 1_000):
        for b in range(2, 200):
            AssertForFunc(cryptominer.Coprimes(a, b),
                          lambda u, v: a * u + b * v)
