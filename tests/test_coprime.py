import cryptominer
import pytest

from helpers import *

def test_coprime():
    a, b = cryptominer.Coprime(12, 6).Knuth()
    assert a * b == 12
    # r = 100
    # for a in range(2, r, 10):
    #     for b in range(2, r, 10):
    #         gcd = cryptominer.GreatestCommonDivisor(a, b).Euclidean()
    #         AssertForFunc(cryptominer.Coprime(a, b).Knuth(), lambda x, y: x * y == gcd)
