from sympy import Symbol
from ..points.point import Point

class Support:
    '''
    A support is a element in beams that limited a movement in a axis 
    '''
    def __init__(self, pointImplementation, horizontal = False, vertical = False, moment = False, rotate_degrees = 0) -> None:
        if not isinstance(pointImplementation, Point):
            raise TypeError('Point necesariamente debe ser class Point')
        if horizontal:
            self.__nameH = 'hor_{}'.format(pointImplementation.name)
            self.__H = Symbol(self.__nameH)        
        if vertical:
            self.__nameV = 'vert_{}'.format(pointImplementation.name)
            self.__V = Symbol(self.__nameV)     
        if moment:
            self.__nameM = 'mom_{}'.format(pointImplementation.name)
            self.__M = Symbol(self.__nameM)           
        
        self.__rotate_degrees = rotate_degrees
        self.__coord = pointImplementation.coordinates
    

        
        
        