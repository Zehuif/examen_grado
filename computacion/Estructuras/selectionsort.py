#algoritmo de ordenamiento selecction sort

def selectionsort(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

if __name__ == "__main__":
    lista = [3, 5, 2, 1, 4]
    print(selectionsort(lista))

    