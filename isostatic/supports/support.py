from sympy import Symbol
from ..points.point import Point

class Support:
    def __init__(self, Point, horizontal = False, vertical = False, moment = False, rotate_degrees = 0) -> None:
        if not isinstance(Point, Point):
            raise TypeError('Point necesariamente debe ser class Point')
        if horizontal:
            self.__nameH = 'hor_{}'.format(Point.name)
            self.__H = Symbol(self.__nameH)        
        if vertical:
            self.__nameV = 'vert_{}'.format(Point.name)
            self.__V = Symbol(self.__nameV)     
        if moment:
            self.__nameM = 'mom_{}'.format(Point.name)
            self.__M = Symbol(self.__nameM)           
        
        self.__rotate_degrees = rotate_degrees
    
    
        
        
        