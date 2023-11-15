#debo realizar un punto de recogida por lo que sera una lista de puntos de recogida
# luego debo realizar 3 filas en los puntos de recogida donde seran de los niveles de toxicidad: Bajo , Medio y Alto

# Lista de desechos en punto de recogida


class Nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    

def agregar_al_final(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    if nodo_inicial == None:
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial


def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo


def imprimir_lista(nodo):
    while nodo != None:
        print(f"Tenemos {nodo.dato}")
        nodo = nodo.siguiente


def obtener_cabeza(nodo_inicial):
    return nodo_inicial


def obtener_cola(nodo_inicial):
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    return temporal


def existe(nodo, busqueda):
    while nodo != None:
        if nodo.dato == busqueda:
            return True
        nodo = nodo.siguiente
    return False


def eliminar(nodo, busqueda):
    if nodo == None:
        return
    if nodo.dato == busqueda:
        return nodo.siguiente
    temporal = nodo
    while temporal.siguiente != None:
        if temporal.siguiente.dato == busqueda:
            if temporal.siguiente.siguiente != None:
                temporal.siguiente = temporal.siguiente.siguiente
            else:
                temporal.siguiente = None
                return nodo
        temporal = temporal.siguiente
    return nodo

#quitar el primer elemento de la lista	
def quitar(nodo):
    if nodo == None:
        return
    if nodo.siguiente != None:
        nodo = nodo.siguiente
    else:
        nodo = None
    return nodo


def rellenar(nodo, nodo2, nodo3):
    nodo = agregar_al_final(nodo, "Basurabajo1")
    nodo = agregar_al_final(nodo, "Basurabajo2")
    nodo = agregar_al_final(nodo, "Basurabajo3")    
    nodo = agregar_al_final(nodo, "Basurabajo4")
    nodo = agregar_al_final(nodo, "Basurabajo5")
    nodo = agregar_al_final(nodo, "Basurabajo6")
    nodo = agregar_al_final(nodo, "Basurabajo7")
    nodo = agregar_al_final(nodo, "Basurabajo8")
    nodo = agregar_al_final(nodo, "Basurabajo9")
    nodo = agregar_al_final(nodo, "Basurabajo10")
    nodo2 = agregar_al_final(nodo2, "Basuramedio1")
    nodo2 = agregar_al_final(nodo2, "Basuramedio2")
    nodo2 = agregar_al_final(nodo2, "Basuramedio3")
    nodo2 = agregar_al_final(nodo2, "Basuramedio4")
    nodo2 = agregar_al_final(nodo2, "Basuramedio5")
    nodo2 = agregar_al_final(nodo2, "Basuramedio6")
    nodo2 = agregar_al_final(nodo2, "Basuramedio7")
    nodo2 = agregar_al_final(nodo2, "Basuramedio8")
    nodo2 = agregar_al_final(nodo2, "Basuramedio9")
    nodo2 = agregar_al_final(nodo2, "Basuramedio10")
    nodo3 = agregar_al_final(nodo3, "Basuraalto1")
    nodo3 = agregar_al_final(nodo3, "Basuraalto2")
    nodo3 = agregar_al_final(nodo3, "Basuraalto3")
    nodo3 = agregar_al_final(nodo3, "Basuraalto4")
    nodo3 = agregar_al_final(nodo3, "Basuraalto5")
    nodo3 = agregar_al_final(nodo3, "Basuraalto6")
    nodo3 = agregar_al_final(nodo3, "Basuraalto7")
    nodo3 = agregar_al_final(nodo3, "Basuraalto8")
    nodo3 = agregar_al_final(nodo3, "Basuraalto9")
    nodo3 = agregar_al_final(nodo3, "Basuraalto10")
    



def main():
    #creamos las listas de los puntos de recogida
    Lista_Bajo = None
    Lista_Medio = None
    Lista_Alto = None

    rellenar(Lista_Bajo,Lista_Medio,Lista_Alto)


main()
