from math import sqrt

class Pi:
    """Computes Pi the greeks way"""

    Un_registry = dict()
    Kn_registry = dict()
    Kn_registry[0] = 1
    Un_registry[0] = 0

    def __init__(self, iterations=10):
        """Sets the number of iteration for the precision of PI"""
        self.iterations = iterations

    def Kn(self, number):
        if self.Kn_registry.get(number, None) is not None:
            return self.Kn_registry[number]
        else:
            self.Kn_registry[number] = value =  self.Kn(number - 1)/sqrt(self.Kn(number - 1)**2 + ( 1 + self.Un(number - 1)) ** 2)
            return value

    def Un(self, number):
        if self.Un_registry.get(number, None) is not None:
            return self.Un_registry[number]
        else:
            self.Un_registry[number] = value =  (1 + self.Un(number - 1))/sqrt(self.Kn(number - 1)**2 + ( 1 + self.Un(number - 1)) ** 2)
            return value
    
    def compute(self):
        n = self.iterations
        kn = self.Kn(n-1)
        un = self.Un(n-1)
        return 2** n * sqrt(kn**2 + (1 - un)**2)


# Example 

pi = Pi(500)
print(pi.compute()) #3.1415926535897944
