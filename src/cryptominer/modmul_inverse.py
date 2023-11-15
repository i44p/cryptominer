from .coprimes import Coprimes


class ModularMultiplicativeInverse:
    def __init__(self, a: int, mod: int) -> None:
        self.a = a
        self.mod = mod

    def Knuth(self) -> int:
        # a == a
        # b == m
        # u == x
        # v == y
        return Coprimes(self.a, self.mod).Knuth()[0] % self.mod
