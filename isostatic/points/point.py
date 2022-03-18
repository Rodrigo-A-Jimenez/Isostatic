
class Point:
    '''
    A point is a position of a place in the space.
    But Isostatic only supports two-dimensions.
    Use for build a structure
    '''
    def __init__(self, name:str, *args, structure:object = None) -> None:
        if not isinstance(name, str):
            raise TypeError('name tiene que ser string')
            
        if not structure == None:
            structure.addPoint(self)
        
        self.__structure = structure
        self.__args = [*args]
        self.__name = name
        self.__stateSupport = False
        self.__elements = []


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
        if self.__stateSupport == True:
            raise ValueError('{} ya tiene apoyo'.format(self.__name))
        self.__stateSupport = True
    
    def addElement(self, element):
        self.__elements.append(element)
    
    @property
    def structure(self) -> object:
        return self.__structure

    @property
    def stateSupport(self):
        return self.__stateSupport

    @property
    def coordinates(self):
        return self.__args

    @property
    def name(self):
        return self.__name

    @property
    def elements(self):
        return self.__elements
    
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
    
    def __truediv__(self, __other: float):
        __division = []
        if not (isinstance(__other, int) or isinstance(__other, float)):
            raise TypeError('Dividen mus be a number, integer or float')
        for i in self.coordinates:
            __division.append(i/__other)
        return Point(str(self.name + '/'), *__division)
        

A = Point('A', 1, 2, 3)
A.coordinates
        
