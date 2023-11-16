import cryptominer
import pytest

from helpers import *


@pytest.mark.parametrize("test_input,expected", [
    (cryptominer.ModularMultiplicativeInverse(5, 11), 9),
    (cryptominer.ModularMultiplicativeInverse(2, 7), 4),
    (cryptominer.ModularMultiplicativeInverse(6, 7), 6),
    (cryptominer.ModularMultiplicativeInverse(7, 5), 3),
    (cryptominer.ModularMultiplicativeInverse(11, 15), 11),
])
def test_modmul_inverse(test_input, expected):
    AssertFor(test_input, expected)
