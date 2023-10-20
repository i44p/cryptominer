from .factorization import Factorization


class CongruenceClass:
    def __init__(self, m):
        self.m = m

    def Definition(self):
        return list(range(self.m))


class CongruenceSystem:
    def __init__(self, m):
        self.m = m

    def Definition(self):
        cong_class = CongruenceClass(self.m).Definition()[1:]

        factors = Factorization(self.m).Dumb()

        return [rem for rem in cong_class
                if not any(map(lambda factor: rem % factor == 0, factors))]
