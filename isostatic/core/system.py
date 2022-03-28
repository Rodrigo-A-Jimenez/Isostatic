'''
*******************************************
*                                         *
* author : Rodrigo Jimenez                *
* E-mail : jimenezhuancarodrigo@gmail.com *
* copyright : (c) 2022                    *
* date : 2022                             *
*                                         *
*******************************************
'''

from isostatic import X, Y, Z
from isostatic.points.vectors import Vector

def summationVectors(*args:Vector) -> Vector:
    '''
    This function receives a list of vectors and returns the sum of all of them.
    '''
    __result = Vector(0, [0, 0])
    for i in args:
        __result += i
    return __result
class CoordinateSystem():
    def __init__(self, element: object, forces:list = [])-> None:
        self.__X = X
        self.__Y = Y
        self.__Z = Z
        self.__origin = element.initialPoint
        self.__endSystem = element.endPoint
        self.__unitVector = element.modulusVector/element.modulusVector.modulus()
        
        self.__forces = forces
        
    @property
    def x(self):
        return self.__X
    
    @property
    def y(self):
        return self.__Y
    
    @property
    def z(self):
        return self.__Z
    
    def interval(self ,begin, ending):
        return [begin*self.__X , ending*self.__Y]
    
    def addForce(self, force):
        self.__forces.append(force)
        
        