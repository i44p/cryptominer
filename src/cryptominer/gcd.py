import inspect

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
    
    def Euclidean(self) -> int:
        return 5


