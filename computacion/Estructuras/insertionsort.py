#algoritmo de ordenamiento insercion sort

def insertionsort(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = valor
    return lista

if __name__ == "__main__":
    lista = [3, 5, 2, 1, 4]
    print(insertionsort(lista))
    