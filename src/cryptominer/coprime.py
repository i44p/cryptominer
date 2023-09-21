from .gcd import GreatestCommonDivisor

class Coprime:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def Knuth(self) -> int:
        x_last, y_last = 1, 0
        x, y = 0, 1
        remainder, mod = divmod(self.a, self.b)
        remainder_last = self.b
        while remainder != 0:
            t = x
            x = x_last - mod * x
            x_last = t
            
            t = y
            y = y_last - mod * y
            y_last = t
            
            t = remainder
            remainder, mod = divmod(remainder_last, remainder)
            remainder_last = t
            
        return x, (remainder_last - self.a * x) // self.b
        