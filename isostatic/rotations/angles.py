from isostatic.constants.constantsSymbols import E, Inertia

modE = E
I_ = Inertia



class LinealLoad:
    def __init__(self, q1: float, q2: float, L: float, E = modE, I = I_) -> None:
        self._q1 = q1
        self._q2 = q2
        self._L = L
        self._k = 1/(E*I)
        self._angleRight = self._k * (((self._L**3)*(8*self._q1 + 7*self._q2))/(360))
        self._angleLeft = self._k * (((self._L**3)*(7*self._q1 + 8*self._q2))/(360))
    
    @property
    def angleRight(self):
        return self._angleRight
    
    @property
    def angleLeft(self):
        return self._angleLeft

class GeneralLoadLineal:
    '''
    Este metodo es un caso general que se puede desplegar a 20 casos. 
    siendo:
    a: Longitud inicial desde el apoyo izquierdo hasta el inicio de la carga
    b: Longitud de la carga en la viga
    c: Longitud final desde el final de la carga hasta el apoyo derecho
    q1: valor de la carga en el lado inicial
    q2: valor de la carga en el lado final
    
    OPCIONAL:
    importar las constantes modE y I_ para implementar distintos valores algebraicamente
    '''
    def __init__(self, q1: float, q2: float, a: float, b: float, c: float, E = modE, I = I_) -> None:
        self._L = a + b + c
        self._a = a
        self._b = b
        self._c = c
        self._q1 = q1
        self._q2 = q2
        self._k = 1/(modE*I_)

        self._angleRight = self._k*((self._L**3)/360)*(self._q1*((10*((self._b*(3*self._c+2*self._b))/(self._L**2)))-(15*((self._b+self._c)/self._L)**4)+(3*((((self._b + self._c)**5)-self._c**5)/(self._b * self._L**4)))) + self._q2*((10*((self._b*(3*self._c + self._b))/(self._L**2)))+(15*(self._c/self._L)**4)-(3*((((self._b + self._c)**5)-self._c**5)/(self._b * self._L**4)))) )

        self._angleLeft = self._k*((self._L**3)/360)*(self._q2*((10*((self._b*(3*self._a+2*self._b))/(self._L**2)))-(15*((self._a+self._b)/self._L)**4)+(3*((((self._a + self._b)**5)-self._a**5)/(self._b * self._L**4)))) + self._q1*((10*((self._b*(3*self._a + self._b))/(self._L**2)))+(15*(self._a/self._L)**4)-(3*((((self._a + self._b)**5)-self._a**5)/(self._b * self._L**4)))) )

    @property
    def angleRight(self):
        return self._angleRight
    
    @property
    def angleLeft(self):
        return self._angleLeft