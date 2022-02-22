

class Point:
    '''
    A point is a position of a place in the space.
    But Isostatic only supports two-dimensions.

    '''
    def __init__(self, name, *args) -> None:
        if not isinstance(name, str):
            raise TypeError('name tiene que ser string')
        self.__args = [*args]
        self.__name = name

    def __str__(self) -> str:
        return (r'{type}: {coord}'.format(type = 'Point',coord = self.__args))

    def __repr__(self) -> str:
        return (r'{type}: {coord}'.format(type = 'Point',coord = self.__args))

    def __len__(self) -> int:
        return len(self.__args)

    def components(self):
        pass

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

    
        
