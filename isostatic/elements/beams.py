from ..points.point import Point

class Beam():
    '''
    Beam, es un elemento viga
    '''
    def __init__(self,initialPoint: Point, endPoint: Point) -> None:

        initialPoint.addElement(self) #Requiere test
        endPoint.addElement(self) # requiere test

        self.__beamName = str(initialPoint.name + endPoint.name)
        self.__initialPoint = initialPoint
        self.__endPoint = endPoint
        self.__modulusVector = self.__endPoint - self.__initialPoint
        self.__L = self.__modulusVector.modulus()

    def __repr__(self) -> str:
        return 'Beam: ' + self.__beamName
    
    def __str__(self) -> str:
        return 'Beam: ' + self.__beamName
