#algoritmo de lista enlazada simple
class Nodo:
    def __init__(self, dato):
        self.dato = dato # Atributo para almacenar el valor del nodo.
        self.siguiente = None # Atributo para almacenar la referencia al siguiente nodo.

    def __str__(self):
        return str(self.dato) # Devuelve el valor del nodo como una cadena.

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None # Atributo para almacenar la referencia al primer nodo de la lista.
        self.cola = None # Atributo para almacenar la referencia al último nodo de la lista.
        self.tam = 0 # Atributo para almacenar el tamaño actual de la lista.

    def __str__(self):
        s = "" # Cadena vacía para ir concatenando los valores de los nodos.
        p = self.cabeza # Puntero para recorrer la lista.
        while p:
            s += str(p) + " " # Agrega el valor del nodo actual a la cadena.
            p = p.siguiente # Avanza al siguiente nodo.
        return s

    def insertar(self, dato):
        nodo = Nodo(dato) # Crea un nuevo nodo con el valor proporcionado.
        if self.cabeza == None:
            # Si la lista está vacía, el nuevo nodo es el primer y el último nodo.
            self.cabeza = nodo # Actualiza la referencia del primer nodo.
            self.cola = nodo # Actualiza la referencia del último nodo.
        else:
            # Agrega el nuevo nodo al final de la lista y actualiza la referencia del último nodo.
            self.cola.siguiente = nodo
            self.cola = nodo
        self.tam += 1 # Incrementa el tamaño de la lista.

    def eliminar(self, dato):
        p = self.cabeza
        q = None
        while p:
            if p.dato == dato:
                if q == None:
                    # Si el nodo a eliminar es el primero de la lista, actualiza la referencia del primer nodo.
                    self.cabeza = p.siguiente
                else:
                    # Si el nodo a eliminar no es el primero, actualiza la referencia del nodo anterior.
                    q.siguiente = p.siguiente
                self.tam -= 1 # Decrementa el tamaño de la lista.
                return True # Indica que el nodo fue eliminado.
            q = p
            p = p.siguiente
        return False # Indica que el nodo no fue encontrado.

    def buscar(self, dato):
        p = self.cabeza
        while p:
            if p.dato == dato:
                return True # Indica que el nodo fue encontrado.
            p = p.siguiente
        return False # Indica que el nodo no fue encontrado.

    def __len__(self):
        return self.tam # Devuelve el tamaño actual de la lista.

    def pos(self, dato):
        p = self.cabeza
        i = 0
        while p:
            if p.dato == dato:
                return i # Devuelve la posición del nodo.
            i += 1
            p = p.siguiente
        return -1 # Indica que el nodo no fue encontrado.
    
if __name__ == "__main__":
    lista = ListaEnlazada()
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
    print(f"Posición de 4: {lista.pos(4)}")
    print(f"Posición de 3: {lista.pos(3)}")