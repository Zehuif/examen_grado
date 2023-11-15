import Pila
lt = Pila

aux = True
pila = lt.Pila()
while(aux):
    pila.agregarNodo("11111111-1", "Juan Perez")
    pila.agregarNodo("11111111-2", "Juan Perez2")
    pila.agregarNodo("11111111-4", "Juan Perez4")
    pila.agregarNodoIntermedio("11111111-2", "11111111-3", "Juan Perez3")
    #eliminar la cabeza
    #pila.eliminarNodo()
    #eliminar la pila
    #pila.eliminarNodoIntermedio("11111111-1")
    #eliminar un nodo intermedio
    #pila.eliminarNodoIntermedio("11111111-4")
    #pila.eliminarNodoIntermedio("11111111-3")
    #Cambiar nombre del nodo 2
    pila.getAllPila()
    aux2 = input()
    if aux2 == "n":
        aux = False