from sympy import Symbol
from ..points.point import Point

class Support:
    '''
    A support is a element in beams that limited a movement in a axis 

    pointImplementation: Punto en el que es aplicado
    horizontal: Restriccion de movimiento horizontal, es decir, existe reacción
    vertical: Restriccion de movimiento vertical, es decir, existe reacción
    moment: Restriccion de rotación, es decir, existe reacción
    rotate_degrees: Rotacion del apoyo
    '''
    def __init__(self, pointImplementation, horizontal = False, vertical = False, moment = False, rotate_degrees = 0) -> None:
        if not isinstance(pointImplementation, Point):
            raise TypeError('Point necesariamente debe ser class Point')
        
        pointImplementation.addSupport()
        if not pointImplementation.structure == None:
            pointImplementation.structure.addSupport(self)
        
        self.__name = pointImplementation.name
        self.__vars = []
        self.__structure = pointImplementation.structure

        if horizontal:
            self.__nameH = 'hor_{}'.format(self.__name)
            self.__H = Symbol(self.__nameH)
            self.__vars.append(self.__H)        
        if vertical:
            self.__nameV = 'vert_{}'.format(self.__name)
            self.__V = Symbol(self.__nameV)
            self.__vars.append(self.__V)
        if moment:
            self.__nameM = 'mom_{}'.format(self.__name)
            self.__M = Symbol(self.__nameM)
            self.__vars.append(self.__M)     

        self.__rotateDegrees = rotate_degrees
        self.__coord = pointImplementation.coordinates
    

    def __str__(self) -> str:
        return 'Support {name}: {coord}'.format(name=self.__name, coord=self.__coord)
    
    @property
    def structure(self) -> object:
        return self.__structure

    @property
    def vars(self):
        return self.__vars

    @property
    def name(self):
        return self.__name

    @property
    def rotateDegrees(self):
        return self.__rotateDegrees
    
    @rotateDegrees.setter
    def rotateDegrees(self, degrees):
        self.__rotateDegrees = degrees


    
    

        
        
        