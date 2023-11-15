class Nodo(object):
    def __init__(self,  rut, nombre):
        self.__rut = rut
        self.__nombre = nombre
        self.pSig = None
    def getRut(self):
        return self.__rut

    def getNombre(self):
        return self.__nombre

    def setRut (self, rut):
        self.__rut = rut
        
    def setNombre (self, nombre):
        self.__nombre = nombre