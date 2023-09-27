from .gcd import GreatestCommonDivisor


class Coprime:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Knuth(self) -> int:
        mod, remainder = divmod(self.a, self.b)
        remainder_last = self.b
        while remainder != 0:
            remainder_last = remainder
            mod, remainder = divmod(remainder_last, mod)

        return remainder_last
