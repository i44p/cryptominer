

class Coprimes:
    """Calculates u, v in equation of coprime a, b: au + bv = 1"""
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def Knuth(self) -> tuple[int]:
        ...