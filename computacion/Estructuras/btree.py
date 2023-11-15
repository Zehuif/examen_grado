class BNode:
    def __init__(self, leaf=False):
        # Indica si es una hoja del árbol
        self.leaf = leaf
        # Lista que guarda las claves del nodo
        self.keys = []
        # Lista que guarda los hijos del nodo
        self.child = []

class BTree:
    def __init__(self, t):
        # Inicializa el árbol B con la raíz como una hoja vacía
        self.root = BNode(leaf=True)
        # Grado mínimo del árbol B
        self.t = t

    def search(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                # Si encuentra la clave, retorna el nodo y su índice
                return (x, i)
            elif x.leaf:
                # Si no encuentra la clave y está en una hoja, retorna None
                return None
            else:
                # Si no encuentra la clave y no está en una hoja, busca en el hijo correspondiente
                return self.search(k, x.child[i])
        else:
            # Busca desde la raíz
            return self.search(k, self.root)

    def insert(self, k):
        r = self.root
        if len(r.keys) == (2 * self.t) - 1:
            # Si la raíz está llena, se crea un nuevo nodo y se divide la raíz
            s = BNode()
            self.root = s
            s.child.insert(0, r)
            self.split_child(s, 0)
            self.insert_nonfull(s, k)
        else:
            self.insert_nonfull(r, k)

    def insert_nonfull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            # Si el nodo es una hoja, se inserta la clave en orden y se actualizan los índices
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            # Si el nodo no es una hoja, se busca el hijo adecuado y se llama recursivamente a la función
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                # Si el hijo está lleno, se divide el hijo y se busca el hijo adecuado
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_nonfull(x.child[i], k)

    def split_child(self, x, i):
        # Separa el i-ésimo hijo de x en dos nodos
        # x: nodo padre
        # i: índice del hijo que se dividirá
        t = self.t
        y = x.child[i]
        z = BNode(leaf=y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]
        if not y.leaf:
            z.child = y.child[t:(2 * t)]
            y.child = y.child[0:(t - 1)]

    def print_tree(self, x=None, level=0):
        # Imprime el árbol en orden, con un formato jerárquico
        # x: nodo actual que se está imprimiendo
        # level: nivel actual en el árbol
        if x is None:
            x = self.root
        print("Level ", level, " ", len(x.keys), end=":")
        print(x.keys)
        level += 1
        if not x.leaf:
            for i in range(len(x.child)):
                self.print_tree(x.child[i], level)

if __name__ == '__main__':
    B = BTree(3)

    for i in range(10):
        B.insert(i)

    B.print_tree()