#algoritmo de lista enlazada doble

#clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato    # dato que almacena el nodo
        self.siguiente = None   # puntero al siguiente nodo
        self.anterior = None   # puntero al nodo anterior
    
    def __str__(self):
        return str(self.dato)   # método para convertir el dato a una cadena y poder imprimirlo

#clase lista enlazada doble
class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None   # puntero al primer nodo de la lista
        self.cola = None   # puntero al último nodo de la lista
        self.tam = 0   # tamaño de la lista

    # método para imprimir la lista
    def __str__(self):
        s = ""   # cadena vacía para ir concatenando los datos
        p = self.cabeza   # puntero para recorrer la lista
        while p:
            s += str(p) + " "   # convertir el dato del nodo a una cadena y concatenarla a la cadena s
            p = p.siguiente   # avanzar al siguiente nodo
        return s   # devolver la cadena con los datos

    # método para insertar un dato al final de la lista
    def insertar(self, dato):
        nodo = Nodo(dato)   # crear un nuevo nodo con el dato a insertar
        if self.cabeza == None:   # si la lista está vacía
            self.cabeza = nodo   # el nuevo nodo será la cabeza y la cola de la lista
            self.cola = nodo
        else:
            self.cola.siguiente = nodo   # el siguiente del último nodo es el nuevo nodo
            nodo.anterior = self.cola   # el anterior del nuevo nodo es el último nodo
            self.cola = nodo   # actualizar el puntero a la cola
        self.tam += 1   # incrementar el tamaño de la lista

    # método para eliminar un dato de la lista
    def eliminar(self, dato):
        p = self.cabeza   # puntero para recorrer la lista
        q = None   # puntero al nodo anterior al que se está recorriendo
        while p:
            if p.dato == dato:   # si se encontró el dato a eliminar
                if q == None:   # si el nodo a eliminar es la cabeza de la lista
                    self.cabeza = p.siguiente   # la nueva cabeza es el siguiente del nodo a eliminar
                else:
                    q.siguiente = p.siguiente   # el siguiente del nodo anterior al que se está recorriendo es el siguiente del nodo a eliminar
                if p == self.cola:   # si el nodo a eliminar es la cola de la lista
                    self.cola = q   # la nueva cola es el nodo anterior al que se está recorriendo
                self.tam -= 1   # disminuir el tamaño de la lista
                return True   # devolver True para indicar que se eliminó el dato
            q = p   # actualizar el nodo anterior al que se está recorriendo
            p = p.siguiente   # avanzar al siguiente nodo
        return False   # si no se encontró el dato, devolver False
    
    # método para buscar un dato en la lista
    def buscar(self, dato):
        p = self.cabeza  # puntero para recorrer la lista
        while p:
            if p.dato == dato: # si se encontró el dato
                return True # devolver True
            p = p.siguiente # avanzar al siguiente nodo
        return False # si no se encontró el dato, devolver False
    
    # método para obtener el tamaño de la lista
    def __len__(self):
        return self.tam # devolver el tamaño de la lista
    
    # método para obtener la posición de un dato en la lista
    def pos(self, dato):
        p = self.cabeza # puntero para recorrer la lista
        i = 0 # contador para la posición
        while p:
            if p.dato == dato: # si se encontró el dato
                return i # devolver la posición
            i += 1 # incrementar la posición
            p = p.siguiente # avanzar al siguiente nodo
        return -1 # si no se encontró el dato, devolver -1
    
    # método para obtener el dato de una posición en la lista
    def __getitem__(self, i):
        p = self.cabeza # puntero para recorrer la lista
        j = 0 # contador para la posición
        while p:
            if j == i: # si se encontró la posición
                return p.dato # devolver el dato
            j += 1 # incrementar la posición
            p = p.siguiente # avanzar al siguiente nodo
        return None # si no se encontró la posición, devolver None
    
    # método para modificar el dato de una posición en la lista
    def __setitem__(self, i, dato):
        p = self.cabeza # puntero para recorrer la lista
        j = 0 # contador para la posición
        while p:
            if j == i: # si se encontró la posición
                p.dato = dato # modificar el dato
                return True # devolver True
            j += 1 # incrementar la posición
            p = p.siguiente # avanzar al siguiente nodo
        return False # si no se encontró la posición, devolver False
    
if __name__ == "__main__":
    lista = ListaEnlazadaDoble()
    lista.insertar(1)
    lista.insertar(2)
    lista.insertar(3)
    lista.insertar(4)
    lista.insertar(5)
    lista.insertar(6)
    print(lista)
    lista.eliminar(3)
    print(lista)
    print(lista.buscar(3))
    print(lista.buscar(4))
    print(len(lista))
    print(f"Posición de 4: {lista.__getitem__(4)}")
    print(f"Posición de 4: {lista.pos(4)}")
    print(f"Posición de 3: {lista.pos(3)}")