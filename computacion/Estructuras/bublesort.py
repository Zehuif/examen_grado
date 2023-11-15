#algoritmo de ordenamiento burbuja

def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista



if __name__ == "__main__":
    lista = [3, 5, 2, 1, 4]
    print(burbuja(lista))