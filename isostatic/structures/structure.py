
#Creacion de estructura en base a los elementos creados.
class ModelEstructure():
    def __init__(self) -> None:
        self.__elements = []
        self.__points = []
        self.__loads = []
        pass

    def __addPoint(self, point):
        self.__points.append(point)

    def __addLoads(self, load):
        self.__loads.append(load)

    def addElement(self, element):
        self.__elements.append(element)
        




