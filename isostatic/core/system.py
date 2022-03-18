from isostatic import X, Y, Z, Beam


class CoordinateSystem():
    def __init__(self, element: Beam)-> None:
        self.__X = X
        self.__Y = Y
        self.__Z = Z
        self.__origin = element.initialPoint
        self.__endSystem = element.endPoint
        self.__unitVector = element.modulusVector/element.modulusVector.modulus()
        
    @property
    def x(self):
        return self.__X
    
    @property
    def y(self):
        return self.__Y
    
    @property
    def z(self):
        return self.__Z