from sympy import Symbol, re

modE = Symbol('E')
I_ = Symbol('I')

class LinealLoad:
    def __init__(self, q1: float, q2: float, L: float, E = modE, I = I_) -> None:
        self._q1 = q1
        self._q2 = q2
        self._L = L
        self.k = 1/(E*I)
        self._angleRight = k * (((self._L**3)*(8*self._q1 + 7*self._q2))/(360))
        self._angleLeft = k * (((self._L**3)*(7*self._q1 + 8*self._q2))/(360))
    
    @property
    def angleRight(self):
        return self._angleRight
    
    @property
    def angleLeft(self):
        return self._angleLeft

