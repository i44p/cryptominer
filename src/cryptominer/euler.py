from .factorization import Factorization

class Euler:
    def __init__(self, m):
        self.m = m
    
    def Euler(self):
        result = 1
        
        factors = Factorization(self.m).Dumb()
        
        if not factors:
            return self.m - 1
        
        for factor in set(factors):
            k = factors.count(factor)
            result *= factor**k - factor**(k-1)
        
        return result
                
