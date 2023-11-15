from math import sqrt as _sqrt


class Factorization:
    def __init__(self, a):
        self.a = a

    def Dumb(self):
        num = self.a
        factors = ()

        while num % 2 == 0:
            factors += (2,)
            num //= 2

        for factor in range(3, max(5+1, int(_sqrt(num))+1), 2):
            while num % factor == 0:
                factors += (factor,)
                num //= factor

        if num != 1:  # num is prime
            factors += (num,)

        return factors
