import cryptominer

from helpers import *

def test_methodlist():
    gcd = cryptominer.GreatestCommonDivisor(1, 3)
    AssertFor(gcd, 5)
