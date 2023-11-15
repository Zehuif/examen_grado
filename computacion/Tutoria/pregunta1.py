tutorias = {}
def consulta(contador):
    print("#############################################")
    print("opción 1: consultar profesor")
    print("opción 2: consultar materia")
    print("opción 3: insertar datos")
    print("opción 4: salir")
    print("Que desea hacer?")

    respuesta = int(input("Ingrese una opción: "))
    if respuesta == 1:
        print("lol")
        return respuesta

    elif respuesta == 2:
        print("lol")
        return respuesta

    elif respuesta == 3:
        print("Ingrese nombre del profesor")
        profesor = str(input("Nombre: "))
        print("ingrese tematica")

        tematica = str(input("Tematica: "))
        d_name = "" % profesor
        print (d_name)
        return respuesta
    
    elif respuesta == 4:
        print("Gracias por usar el sistema")
        return respuesta
    else:
        print("opción no válida")
    print("#############################################")

profesores = []
dbase = dict([
      ('Profesor', ''),
      ('Tutoría', ''),
])
competidor1 = {"nombre": "Juan", "edad": 32, "prueba": "50M"}

respuesta = 0
contador = 0
while respuesta != 4:
    respuesta = consulta(contador)

