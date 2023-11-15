import Nodo
ND = Nodo

class Pila(object):
    def __init__(self):
        self.__primero = None
        
    def agregarNodo(self, rut, nombre):
        new = ND.Nodo(rut, nombre)
        pAux = self.__primero
        validar = True
        #No hay nodos en la pila
        if self.__primero == None:
            self.__primero = new
        #Hay un nodo en la pila
        else:
            new.pSig = self.__primero
            self.__primero = new
                
    def agregarNodoIntermedio(self, rutAnterior, rut, nombre):
        new = ND.Nodo(rut, nombre)
        pAuxA = self.__primero
        pAuxB = None
        validar = True
        while(validar):
            #Insertar cuando hay match
            if pAuxA != None:
                #es el primero
                if pAuxA.getRut() == rutAnterior and pAuxA == self.__primero:
                    #inserto en el primero
                    new.pSig = pAuxA
                    self.__primero = new 
                    validar = False
                elif pAuxA.pSig.getRut() == rutAnterior:
                    pAuxB = pAuxA.pSig
                    new.pSig = pAuxB
                    pAuxA.pSig = new
                    validar = False
                else:
                    pAuxA = pAuxA.pSig
            else:
                print("El rut no existe")
        
    def eliminarNodo(self):
        pAux = self.__primero
        validar = True
        while(validar):
            #eliminar el primer nodo
            if pAux != None:
                 self.__primero = pAux.pSig
                 pAux.pSig = None
                 pAux = None
                 validar = False
            else:
                print("Lista vacia")
                validar = False
    
    def eliminarNodoIntermedio(self, rut):
        pAux = self.__primero
        pAuxA = None
        validar = True
        while(validar):
            if pAux != None:
                #eliminar el primer nodo y unico
                if pAux.getRut() == rut and pAux.pSig == None and pAux == self.__primero:
                    self.__primero = None
                    validar = False
                #eliminar el primer nodo y no unico
                elif pAux.getRut() == rut and pAux.pSig != None and pAux == self.__primero:
                    self.__primero = pAux.pSig
                    pAux.pSig = None
                    pAux = None
                    validar = False
                #eliminar el ultimo nodo
                elif pAux.pSig.getRut() == rut and pAux.pSig.pSig == None:
                    pAux.pSig = None
                    validar = False
                #eliminar nodo intermedio
                elif pAux.pSig.getRut() == rut and pAux.pSig.pSig != None:
                    pAuxA = pAux.pSig
                    pAux.pSig = pAux.pSig.pSig
                    pAuxA.pSig = None
                    pAuxA = None
                    validar = False
                else:
                    pAux = pAux.pSig
                    
    def getAllPila (self):
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
                print("Fin de la pila")
                validar = False