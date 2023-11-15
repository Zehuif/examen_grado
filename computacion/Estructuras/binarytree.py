class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
 
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
 
    def insertar(self, valor):
        nuevo_nodo = NodoArbol(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_aux(nuevo_nodo, self.raiz)
 
    def _insertar_aux(self, nuevo_nodo, nodo_actual):
        if nuevo_nodo.valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                self._insertar_aux(nuevo_nodo, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                self._insertar_aux(nuevo_nodo, nodo_actual.derecha)
 
    def buscar(self, valor):
        return self._buscar_aux(valor, self.raiz)
 
    def _buscar_aux(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        elif nodo_actual.valor == valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_aux(valor, nodo_actual.izquierda)
        else:
            return self._buscar_aux(valor, nodo_actual.derecha)
        
    def eliminar(self, valor):
        self.raiz = self._eliminar_aux(valor, self.raiz)

    def _eliminar_aux(self, valor, nodo_actual):
        if nodo_actual is None:
            return nodo_actual
        elif valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar_aux(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_aux(valor, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            nodo_actual.valor = self._minimo_valor(nodo_actual.derecha)
            nodo_actual.derecha = self._eliminar_aux(nodo_actual.valor, nodo_actual.derecha)
        return nodo_actual
    
    def print_tree(self):
        if self.raiz is not None:
            self._print_tree(self.raiz)

    def _print_tree(self, nodo_actual):
        if nodo_actual is not None:
            self._print_tree(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self._print_tree(nodo_actual.derecha)
    
if __name__ == "__main__":

    arbol = ArbolBinarioBusqueda()
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(70)
    arbol.insertar(60)
    arbol.insertar(80)
    print(arbol.buscar(20))
    print(arbol.buscar(21))
    arbol.eliminar(20)
    print(arbol.buscar(20))
    print(arbol.buscar(30))
    arbol.print_tree()