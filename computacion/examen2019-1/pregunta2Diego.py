piscina1 = {}
piscina2 = {}

#version de hector
piscinas = {
    'piscinaPrincipal': [{},{},{},{},{},{},{},{}],
    'piscinaPractica': ['nadador1', 'nadador2', 'nadador3', 'nadador4', 'nadador5', 'nadador6', 'nadador7', 'nadador8']
}

#codigo deberda
Value1 = 1
PiscinaPrincipal = {"Pista1":"","Pista2":"","Pista3":"","Pista4":"","Pista5":"","Pista6":"","Pista7":"","Pista8":""}
PiscinaPractica = {"Pista1":"","Pista2":"","Pista3":"","Pista4":"","Pista5":"","Pista6":"","Pista7":"","Pista8":""}


print("ingrese los participantes de la competencia que se realizara ahora")
pista = str(input("Ingrese nombre de la pista: "))
nombre = str(input("Ingrese nombre del competidor: "))
PiscinaPrincipal[pista] = {nombre}


def consulta(contador1, contador2):
    print("#############################################")
    print("opción 1: ingresar participante")
    print("opción 2: Salir")
    print("Que desea hacer?")


    respuesta = int(input("Ingrese una opción: "))
    if respuesta == 1:
        print("que número de participante desea ingresar?")
        participantevar = str(input("participante: "))
        print|("ingrese el número de la piscina")
        piscinavar = int(input("piscina: "))
        if piscinavar == 1 & contador1 >= 8:
                print("piscina llena")
                return respuesta
        if piscinavar == 2 & contador2 >= 8:
                print("piscina llena")
                return respuesta
        if participantevar == 1 & piscinavar == 1:
            piscinas[piscina1]['nadador4'] = piscinavar
        elif participantevar == 2 & piscinavar == 1:
            piscinas[piscina1]['nadador5'] = piscinavar
        elif participantevar == 3 & piscinavar == 1:
            piscinas[piscina1]['nadador3'] = piscinavar
        elif participantevar == 4 & piscinavar == 1:
            piscinas[piscina1]['nadador6'] = piscinavar
        elif participantevar == 5 & piscinavar == 1:
            piscinas[piscina1]['nadador2'] = piscinavar
        elif participantevar == 6 & piscinavar == 1:
            piscinas[piscina1]['nadador7'] = piscinavar
        elif participantevar == 7 & piscinavar == 1:
            piscinas[piscina1]['nadador1'] = piscinavar
        elif participantevar == 8 & piscinavar == 1:
            piscinas[piscina1]['nadador8'] = piscinavar
        if participantevar == 1 & piscinavar == 2:
            piscinas[piscina1]['nadador4'] = piscinavar
        elif participantevar == 2 & piscinavar == 2:
            piscinas[piscina1]['nadador5'] = piscinavar
        elif participantevar == 3 & piscinavar == 2:
            piscinas[piscina1]['nadador3'] = piscinavar
        elif participantevar == 4 & piscinavar == 2:
            piscinas[piscina1]['nadador6'] = piscinavar
        elif participantevar == 5 & piscinavar == 2:
            piscinas[piscina1]['nadador2'] = piscinavar
        elif participantevar == 6 & piscinavar == 2:
            piscinas[piscina1]['nadador7'] = piscinavar
        elif participantevar == 7 & piscinavar == 2:
            piscinas[piscina1]['nadador1'] = piscinavar
        elif participantevar == 8 & piscinavar == 2:
            piscinas[piscina1]['nadador8'] = piscinavar
        
        return respuesta

    elif respuesta == 2:
        print("Adios")
        return respuesta



if __name__ == "__main__":
    pass
    respuesta = 0
    while respuesta != 2:
        respuesta = consulta()
