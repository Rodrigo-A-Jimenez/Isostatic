

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

    
        
