import cryptominer
import pytest

from helpers import *


@pytest.mark.parametrize("test_input,expected", [
    # (cryptominer.Coprimes(1234, 54), 2)
    (cryptominer.Coprimes(2548, 22), (5, -579))
])
def test_coprimes_defined(test_input, expected):
    AssertFor(test_input, expected)

def test_coprimes_generated():
    for a in range(1, 10_000):
       for b in range(1, 10_000):
           u, v = cryptominer.Coprimes(a, b)
           assert a * u + b * v == cryptominer.GreatestCommonDivisor(a, b).Euclidean()

