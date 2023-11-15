def tiempoMili(e):
  return e.tiempo

def olimpiadas(lista_participantes, participantes):
    cantidad_eventos = int(participantes/8)
    print("Cantidad de eventos: ",cantidad_eventos)
    lista_participantes.sort(key=tiempoMili)#Se asume que el algoritmo de ordenamiento sera MergeSort
    esquemaA = []
    contador_evento = 0
    i = 0
    while(contador_evento < cantidad_eventos):
        esquemaA.append(lista_participantes[i + 6])
        esquemaA.append(lista_participantes[i + 4])
        esquemaA.append(lista_participantes[i + 2])
        esquemaA.append(lista_participantes[i + 0])
        esquemaA.append(lista_participantes[i + 1])
        esquemaA.append(lista_participantes[i + 3])
        esquemaA.append(lista_participantes[i + 5])
        esquemaA.append(lista_participantes[i + 7])
        i=i+8
        contador_evento=contador_evento + 1

    for particpante in esquemaA:
        print(particpante.id, "", end = '')
    print("")

    esquemaB = []
    contador_evento = 0
    while(contador_evento < cantidad_eventos):
        esquemaB.append(lista_participantes[contador_evento + 6*cantidad_eventos])
        esquemaB.append(lista_participantes[contador_evento + 4*cantidad_eventos])
        esquemaB.append(lista_participantes[contador_evento + 2*cantidad_eventos])
        esquemaB.append(lista_participantes[contador_evento + 0*cantidad_eventos])
        esquemaB.append(lista_participantes[contador_evento + 1*cantidad_eventos])
        esquemaB.append(lista_participantes[contador_evento + 3*cantidad_eventos])
        esquemaB.append(lista_participantes[contador_evento + 5*cantidad_eventos])
        esquemaB.append(lista_participantes[contador_evento + 7*cantidad_eventos])
        contador_evento=contador_evento + 1
    
    for particpante in esquemaB:
        
        print(particpante.id , "", end = '')


entradas = ["16", "16 945258", 
"5 974925",
"6 1025304",
"1 988751",
"8 945030",
"2 999421",
"14 955708",
"3 1031388",
"13 1007447",
"11 981563",
"10 969338",
"15 1029284",
"4 1055499",
"12 963144",
"7 980324",
"9 941296"]

participantes = int(entradas.pop(0))

entradasNew = []
class participante:
    def __init__(self, r=0, i=0):
        self.id = r
        self.tiempo = i

for entrada in entradas:
    aux = participante(int(entrada.split(" ")[0]),int(entrada.split(" ")[1]))
    entradasNew.append(aux)


olimpiadas(entradasNew, participantes)