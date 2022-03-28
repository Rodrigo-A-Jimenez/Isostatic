
from sympy import atan, cos, pi, sin


class Vector():
    def __init__(self, pointX, module: float | list, gravitational: bool = True, inclination: float = pi/2) -> None:
        if not isinstance(gravitational, bool):
            raise TypeError("gravitational must be a boolean")

        if isinstance(module, float) or isinstance(module, int):
            self.__mod = module
            self.__inclination = inclination

            self.__notation = []
            if inclination == pi/2:
                self.__notation.append(0)
            else:
                self.__notation.append(-self.__mod * cos(inclination))

            if gravitational:
                self.__notation.append(-self.__mod * sin(inclination))
            else:
                self.__notation.append(-self.__mod * sin(inclination))

        elif isinstance(module, list):
            self.__mod = 0
            for i in module:
                self.__mod += i**2
            self.__mod = self.__mod**0.5

            self.__notation = module
            self.__inclination = atan(module[1]/module[0])

        self.__implementation = pointX

        self.__gravitational = gravitational

    def forceMoment(self):
        return self.implementation * self.__notation[1]

    @property
    def notation(self):
        return self.__notation

    @property
    def module(self):
        return self.__mod

    @property
    def inclination(self):
        return self.__inclination

    @property
    def implementation(self):
        return self.__implementation

    @property
    def gravitational(self):
        return self.__gravitational

    def __add__(self, __o: object) -> object:
        if len(self.__notation) != len(__o.notation):
            raise ValueError("The vectors must have the same size")
        __result = [x+y for x, y in zip(self.notation, __o.notation)]
        return Vector(self.implementation, __result, self.gravitational)

    def __sub__(self, __o: object) -> object:
        if len(self.__notation) != len(__o.notation):
            raise ValueError("The vectors must have the same size")
        __result = [x-y for x, y in zip(self.notation, __o.notation)]
        return Vector(self.implementation, __result, self.gravitational)
