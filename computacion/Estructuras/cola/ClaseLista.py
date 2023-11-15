#Alumno: Cristobal Alexis Urra Barboza - 19.644.373-8
import ClaseNodo
ND = ClaseNodo

class Lista(object):
    def __init__(self):
        self.__primero = None
        
    def agregarNodo(self, rut, nombre):
        new = ND.Nodo(rut, nombre)
        validar = True
        pAux = self.__primero
        while(validar):
            if pAux == None:
                self.__primero = new
                validar = False
            elif pAux.pSig == None:
                pAux.pSig = new
                validar = False
            else:
                pAux = pAux.pSig
                
    def agregarNodoIntermedio(self, rutAnterior, rut, nombre):
        new = ND.Nodo(rut, nombre)
        pAuxA = self.__primero
        pAuxB = None
        validar = True
        while(validar):
            if pAuxA != None:
                if pAuxA.getRut() == rutAnterior and pAuxA.pSig != None:
                    pAuxB = pAuxA.pSig
                    pAuxA.pSig = new
                    pAuxA.pSig.pSig = pAuxB
                    validar = False
                elif pAuxA.getRut() == rutAnterior and pAuxA.pSig == None:
                    pAuxA.pSig = new
                    validar = False
                else:
                    pAuxA = pAuxA.pSig
            else:
                print("El rut anterior no existe")
                validar = False
                
    def eliminarNodo (self, rut):
        pAux = self.__primero
        pAux2 = None
        validar = True
        while(validar):
            if pAux != None:
                if pAux.getRut() == rut and pAux == self.__primero:
                    self.__primero = pAux.pSig
                    pAux.pSig == None
                    pAux == None
                    validar = False
                    print("Rut eliminado")
                elif pAux.pSig.getRut() == rut and pAux.pSig.pSig != None:
                    pAux2 = pAux.pSig
                    pAux.pSig = pAux.pSig.pSig
                    pAux2.pSig = None
                    pAux2 = None
                    validar = False
                    print("Rut eliminado")
                elif pAux.pSig.getRut() == rut and pAux.pSig.pSig == None:
                    pAux.pSig = None
                    validar = False
                    print("Rut eliminado")
                else:
                    pAux = pAux.pSig
            else:
                print("El rut no existe")
                validar = False
                
    def getAllLista (self):
        pAux = self.__primero
        validar = True
        cont = 0
        while(validar):
            cont += 1
            if pAux != None:
                if pAux.pSig != None:
                    print(cont, " Rut:", pAux.getRut(), " Nombre:", pAux.getNombre())
                    pAux = pAux.pSig
                else:
                    print(cont, " Rut:", pAux.getRut(), " Nombre:", pAux.getNombre())
                    validar = False
            else:
                print("Fin de la lista")
                validar = False
                
    def getRutLista (self, rut):
        pAux = self.__primero
        validar = True
        while(validar):
            if pAux != None:
                if pAux.getRut == rut:
                    print("Rut:", pAux.getRut(), " Nombre:", pAux.getNombre())
                    pAux = pAux.pSig
                else:
                    pAux = pAux.pSig
            else:
                print("Fin de la lista")
                validar = False
                
    def setRutNombre (self, rut, nombre):
        pAux = self.__primero
        validar = True
        while(validar):
            if pAux != None:
                if pAux.getRut() == rut:
                    pAux.setRut(rut)
                    pAux.setNombre(nombre)
                    print("Elemento Actualizado")
                    pAux = pAux.pSig
                else:
                    pAux = pAux.pSig
            else:
                print("Fin de la lista")
                validar = False
                
    def getRutPosition (self, rut):
        pAux = self.__primero
        validar = True
        position = 1
        while (validar):
            if pAux != None:
                if pAux.getRut() == rut:
                    print ("la posición del nodo es: ", position)
                    validar = False
                else:
                    pAux = pAux.pSig
                    position += 1
            else:
                print ("No hay resultados para el rut ingresado")
                validar = False
        