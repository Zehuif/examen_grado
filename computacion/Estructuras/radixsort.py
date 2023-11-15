def radixsort(arr):
    # Encontrar el valor máximo en la lista
    max_val = max(arr)
    
    # Comenzar con el dígito menos significativo
    exp = 1
    
    # Iterar mientras aún haya dígitos por procesar
    while max_val // exp > 0:
        # Llamar a counting_sort para ordenar los elementos por el dígito actual
        arr = counting_sort(arr, exp)
        # Mover al siguiente dígito
        exp *= 10
    
    # Devolver la lista ordenada
    return arr

def counting_sort(arr, exp):
    # Inicializar la salida y el contador
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Contar el número de elementos en cada "bucket"
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Hacer una suma acumulativa en el contador
    for i in range(1, 10):
        count[i] += count[i-1]
    
    # Ordenar los elementos de la lista en la salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copiar los elementos ordenados de la salida de vuelta a la lista original
    for i in range(n):
        arr[i] = output[i]
    
    # Devolver la lista ordenada
    return arr