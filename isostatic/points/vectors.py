'''class Vector se definira para los vectores fuerza
se puede definir: 
- a traves de un modulo y direccion,
- a traves de dos puntos (pero los puntos de este paquete son articulaciones en la estructura)
- 

'''
from operator import mod
from isostatic.core.system import CoordinateSystem
from sympy import cos, pi, sin


class Vector():
    def __init__(self, pointX, module: float|list , gravitational:bool = True ,inclination:float=pi/2) -> None:
        if isinstance(module, float) or isinstance(module, int):
            self.__mod = module
            
            self.__notation = []
            if inclination == pi/2:
                self.__notation.append(0)
            else:
                self.__notation.append(-self.__mod * cos(inclination))
            
            if gravitational:
                self.__notation.append(-self.__mod * sin(inclination))
            else:
                self.__notation.append(-self.__mod * sin(inclination))
                
        elif isinstance(module, list):
            self.__mod = 0
            for i in module:
                self.__mod += i**2
            self.__mod = self.__mod**0.5
            
            self.__notation = module
        
        self.__implementation = pointX
        
        self.__gravitational = gravitational
        self.__inclination = inclination
            
    @property
    def notation(self):
        return self.__notation
    
    @property
    def module(self):
        return self.__mod
            
        