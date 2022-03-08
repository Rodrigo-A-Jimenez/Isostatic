
#Creacion de estructura en base a los elementos creados.
class Structure():
    def __init__(self) -> None:
        self.__elements = []
        self.__points = []
        self.__loads = []
        self.__supports = []

    def addPoint(self, point):
        self.__points.append(point)
    
    def addSupport(self, support):
        self.__supports.append(support)

    def addLoads(self, load):
        self.__loads.append(load)

    def addElement(self, element):
        self.__elements.append(element)
        




