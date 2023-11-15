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


Mesas = {"Mesa1":"","Mesa2":"","Mesa3":"","Mesa4":"","Mesa5":"","Mesa6":"","Mesa7":"","Mesa8":""}



ND = Nodo()

if __name__ == "__main__":
    espera = Lista
    while(true):
        print("que quiere hacer")
        print("1agregar persona a la fila")
        print("2 dejar pasar a la primera")
        aux = input("selecciona")
        if (aux== "1"):
            print("ingrese rut")
            rut = input("ingrese rut")
            nombre = input("ingrese nombre")
            ingresar = ND(rut, nombre)
            espera.agregarNodo(ingresar)

        else:
            print("Dejando pasar a la persona")
            Entrando= espera.eliminarNodo()
            # ahora ingresamos a la persona al restaurant a su mesa
            reserva = input("tiene reserva (1 si 2 no)")
            if (reserva ==1):
                #tiene reserva
                mesa = input("cual mesa")
                Mesas[mesa] = {Entrando}
            else:
                #no tiene reserva
                #busco en diccionario, no lo hare por tiempo
                mesa = "mesa1"
                Mesas[mesa] = {Entrando}

