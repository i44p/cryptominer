

class Coprimes:
    """Calculates u, v in equation of coprime a, b: au + bv = 1"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Knuth(self) -> tuple[int]:
        mod, remainder = divmod(self.a, self.b)
        remainder_last = self.b

        x_last_last, x_last, x = 1, 0, 1

        while remainder != 0:
            mod, new_remainder = divmod(remainder_last, remainder)
            remainder_last, remainder = remainder, new_remainder
            x_last_last, x_last = x_last, x
            x = x_last_last - mod * x_last

        return (x_last, (remainder_last - self.a * x_last) // self.b)
