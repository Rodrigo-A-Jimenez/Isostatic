
class Point:
    '''
    A point is a position of a place in the space.
    But Isostatic only supports two-dimensions.
    Use for build a structure
    '''
    def __init__(self, name, *args) -> None:
        if not isinstance(name, str):
            raise TypeError('name tiene que ser string')
        self.__args = [*args]
        self.__name = name
        self.__stateSupport = False


    def __str__(self) -> str:
        return (r'{type}: {coord}'.format(type = 'Point',coord = self.__args))

    def __repr__(self) -> str:
        return (r'{type}: {coord}'.format(type = 'Point',coord = self.__args))

    def __len__(self) -> int:
        return len(self.__args)
    
    def modulus(self):
        __mod = 0
        for i in self.coordinates:
            __mod += i**2
        
        return __mod**0.5

    def addSupport(self):
        self.__stateSupport = True
    
    @property
    def stateSupport(self):
        return self.__stateSupport

    @property
    def coordinates(self):
        return self.__args

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise (TypeError('name tiene que ser string'))
        
        self.__name = name

    #Sobrescritura de operadores
    def __eq__(self, __o: object) -> bool:
        if self.coordinates == __o.coordinates:
            return True
        else:
            return False

    def __add__ (self, __other):
        __sum = []
        for i, j in zip(self.coordinates, __other.coordinates):
            __sum.append(i+j)
        return Point(str(self.name + __other.name), *__sum)

    def __sub__(self, __other: object):
        __substraction = []
        for i, j in zip(self.coordinates, __other.coordinates):
            __substraction.append(i-j)
        return Point(str(self.name + '-' + __other.name), *__substraction)

A = Point('A', 1, 2, 3)
A.coordinates
        
