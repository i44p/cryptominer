

def is_prime(num: int) -> bool:
    if num % 2 == 0:
        if num == 2:
            return True
        return False
    for i in range(3, num // 2, 2):
        if num % i == 0:
            return False
    return True


class GreatestCommonDivisor:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Euclidean_recursive(self) -> int:
        mod, remainder = divmod(self.a, self.b)
        if mod == 0:
            return self.a
        return GreatestCommonDivisor(self.b, mod).Euclidean_recursive()

    def Euclidean(self) -> int:
        mod, remainder = divmod(self.a, self.b)
        remainder_last = self.b
        while remainder != 0:
            remainder_last = remainder
            mod, remainder = divmod(remainder_last, mod)

        return remainder_last
