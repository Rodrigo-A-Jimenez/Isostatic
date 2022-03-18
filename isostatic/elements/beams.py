from ..points.point import Point

class Beam():
    '''
    Beam, es un elemento viga
    '''
    def __init__(self, initialPoint: Point, endPoint: Point) -> None:

        if not (initialPoint.structure == endPoint.structure ):
            raise TypeError('Los puntos no pertencen a la misma estructura')
        
        if not initialPoint.structure == None:
            initialPoint.structure.addElement(self)
        
        initialPoint.addElement(self) 
        endPoint.addElement(self) 

        self.__beamName = str(initialPoint.name + endPoint.name)

        self.__initialPoint = initialPoint
        self.__endPoint = endPoint

        self.__modulusVector = self.__endPoint - self.__initialPoint
        self.__L = self.__modulusVector.modulus()

        self.__structure = initialPoint.structure
        self.__loads = []


    def addLoad(self, load):
        self.__loads.append(load)

    @property
    def structure(self) -> object:
        return self.__structure

    @property
    def loads(self):
        return self.__loads
    
    @property
    def initialPoint(self):
        return self.__initialPoint
    
    @property
    def endPoint(self):
        return self.__endPoint
    
    @property
    def modulusVector(self):
        return self.__modulusVector

    def __repr__(self) -> str:
        return 'Beam: ' + self.__beamName
    
    def __str__(self) -> str:
        return 'Beam: ' + self.__beamName
