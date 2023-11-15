import ClaseLista
lt = ClaseLista

aux = True
cola = lt.Lista()
while(aux):
    cola.agregarNodo("11111111-1", "Juan Perez")
    cola.agregarNodo("11111111-2", "Juan Perez2")
    cola.agregarNodo("11111111-4", "Juan Perez4")
    cola.agregarNodoIntermedio("11111111-2", "11111111-3", "Juan Perez3")
    #eliminar la cabeza
    #cola.eliminarNodo("11111111-1")
    #eliminar la cola
    #cola.eliminarNodo("11111111-4")
    #eliminar un nodo intermedio
    #cola.eliminarNodo("11111111-3")
    #Cambiar nombre del nodo 2
    cola.setRutNombre("11111111-2","Joaquin Villaculon")
    cola.getRutPosition("11111111-2")
    cola.getAllLista()
    aux2 = input()
    if aux2 == "n":
        aux = False