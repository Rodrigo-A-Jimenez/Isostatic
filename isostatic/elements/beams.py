from ..points.point import Point

class beam():
    '''
    Beam, es un elemento viga
    '''
    def __init__(self,initialPoint: Point, endPoint: Point) -> None:
        self.__initialPoint = initialPoint
        self.__endPoint = endPoint
        self.__modulusVector = self.__endPoint - self.__initialPoint
        self.__L = self.__modulusVector.modulus()

        