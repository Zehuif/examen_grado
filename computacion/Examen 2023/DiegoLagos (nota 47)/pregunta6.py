#pregunta6 - Diego Lagos - Examen de Grado 2023-1
#Ojo es es pseudocódigo
################################################################################
horarios = {}
mesas10 = {}
mesas11 = {}
mesas12 = {}
mesas13 = {}
mesas14 = {}
mesas15 = {}


horarios["10:00"] = mesas10
horarios["11:00"] = mesas11
horarios["12:00"] = mesas12
horarios["13:00"] = mesas13
horarios["14:00"] = mesas14
horarios["15:00"] = mesas15


def consulta():
    print("#############################################")
    print("opción 1: reservar mesa")
    print("opción 2: comer sin reserva")
    print("opción 3: comer con reserva")    
    print("opción 4: salir")
    print("Que desea hacer?")

    respuesta = int(input("Ingrese una opción: "))
    if respuesta == 1:
        print("A que hora desea reservar?")
        print("opción 1: 10:00-11:00")
        print("opción 2: 11:00-12:00")
        print("opción 3: 12:00-13:00")
        print("opción 4: 13:00-14:00")    
        print("opción 5: 14:00-15:00")
        print("opción 6: 15:00-16:00")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print("Que mesa desea reservar?")
            print("Ingrese un número de mesa entre el 1 y el 5:")
            mesa = int(input("Mesa: "))
            if mesa == 1:
                mesas10[1] = "reservada"
                print("mesa 1 a las 10:00 reservada")
            if mesa == 2:
                mesas10[2] = "reservada"
                print("mesa 2 a las 10:00 reservada")
            if mesa == 3:
                mesas10[3] = "reservada"
                print("mesa 3 a las 10:00 reservada")
            if mesa == 4:
                mesas10[4] = "reservada"
                print("mesa 4 a las 10:00 reservada")
            if mesa == 5:
                mesas10[5] = "reservada"
                print("mesa 5 a las 10:00 reservada")
            else:
                print("Opción no válida")
        if opcion == 2:
            print("Que mesa desea reservar?")
            print("Ingrese un número de mesa entre el 1 y el 5:")
            mesa = int(input("Mesa: "))
            if mesa == 1:
                mesas11[1] = "reservada"
                print("mesa 1 a las 11:00 reservada")
            if mesa == 2:
                mesas11[2] = "reservada"
                print("mesa 2 a las 11:00 reservada")
            if mesa == 3:
                mesas11[3] = "reservada"
                print("mesa 3 a las 11:00 reservada")
            if mesa == 4:
                mesas11[4] = "reservada"
                print("mesa 4 a las 11:00 reservada")
            if mesa == 5:
                mesas11[5] = "reservada"
                print("mesa 5 a las 11:00 reservada")
            else:
                print("Opción no válida")
        if opcion == 3:
            print("Que mesa desea reservar?")
            print("Ingrese un número de mesa entre el 1 y el 5:")
            mesa = int(input("Mesa: "))
            if mesa == 1:
                mesas12[1] = "reservada"
                print("mesa 1 a las 12:00 reservada")
            if mesa == 2:
                mesas12[2] = "reservada"
                print("mesa 2 a las 12:00 reservada")
            if mesa == 3:
                mesas12[3] = "reservada"
                print("mesa 3 a las 12:00 reservada")
            if mesa == 4:
                mesas12[4] = "reservada"
                print("mesa 4 a las 12:00 reservada")
            if mesa == 5:
                mesas12[5] = "reservada"
                print("mesa 5 a las 12:00 reservada")
            else:
                print("Opción no válida")
        if opcion == 4:
            print("Que mesa desea reservar?")
            print("Ingrese un número de mesa entre el 1 y el 5:")
            mesa = int(input("Mesa: "))
            if mesa == 1:
                mesas13[1] = "reservada"
                print("mesa 1 a las 13:00 reservada")
            if mesa == 2:
                mesas13[2] = "reservada"
                print("mesa 2 a las 13:00 reservada")
            if mesa == 3:
                mesas13[3] = "reservada"
                print("mesa 3 a las 13:00 reservada")
            if mesa == 4:
                mesas13[4] = "reservada"
                print("mesa 4 a las 13:00 reservada")
            if mesa == 5:
                mesas13[5] = "reservada"
                print("mesa 5 a las 13:00 reservada")
            else:
                print("Opción no válida")
        if opcion == 5:
            print("Que mesa desea reservar?")
            print("Ingrese un número de mesa entre el 1 y el 5:")
            mesa = int(input("Mesa: "))
            if mesa == 1:
                mesas14[1] = "reservada"
                print("mesa 1 a las 14:00 reservada")
            if mesa == 2:
                mesas14[2] = "reservada"
                print("mesa 2 a las 14:00 reservada")
            if mesa == 3:
                mesas14[3] = "reservada"
                print("mesa 3 a las 14:00 reservada")
            if mesa == 4:
                mesas14[4] = "reservada"
                print("mesa 4 a las 14:00 reservada")
            if mesa == 5:
                mesas14[5] = "reservada"
                print("mesa 5 a las 14:00 reservada")
            else:
                print("Opción no válida")
        if opcion == 6:
            print("Que mesa desea reservar?")
            print("Ingrese un número de mesa entre el 1 y el 5:")
            mesa = int(input("Mesa: "))
            if mesa == 1:
                mesas15[1] = "reservada"
                print("mesa 1 a las 15:00 reservada")
            if mesa == 2:
                mesas15[2] = "reservada"
                print("mesa 2 a las 15:00 reservada")
            if mesa == 3:
                mesas15[3] = "reservada"
                print("mesa 3 a las 15:00 reservada")
            if mesa == 4:
                mesas15[4] = "reservada"
                print("mesa 4 a las 15:00 reservada")
            if mesa == 5:
                mesas15[5] = "reservada"
                print("mesa 5 a las 15:00 reservada")
            else:
                print("Opción no válida")
        else:
            print("Ingrese una opción válida")
        return respuesta

    elif respuesta == 2:
        print("A que hora llegaron los comensales sin reserva?")
        print("opción 1: 10:00-11:00")
        print("opción 2: 11:00-12:00")
        print("opción 3: 12:00-13:00")
        print("opción 4: 13:00-14:00")    
        print("opción 5: 14:00-15:00")
        print("opción 6: 15:00-16:00")
        horaN = int(input("Opción: "))
        if horaN == 1:
            print("mesas disponibles: ")
            for i in range(1,6):
                if horarios["10:00"][i] == "disponible":
                    print(i)
        if horaN == 2:
            print("mesas disponibles: ")
            for i in range(1,6):
                if horarios["11:00"][i] == "disponible":
                    print(i)
        if horaN == 3:
            print("mesas disponibles: ")
            for i in range(1,6):
                if horarios["12:00"][i] == "disponible":
                    print(i)
        if horaN == 4:
            print("mesas disponibles: ")
            for i in range(1,6):
                if horarios["13:00"][i] == "disponible":
                    print(i)
        if horaN == 5:
            print("mesas disponibles: ")
            for i in range(1,6):
                if horarios["14:00"][i] == "disponible":
                    print(i)

    elif respuesta == 3:
        print("A que hora llegaron los comensales con reserva?")
        print("opción 1: 10:00-11:00")
        print("opción 2: 11:00-12:00")
        print("opción 3: 12:00-13:00")
        print("opción 4: 13:00-14:00")
        print("opción 5: 14:00-15:00")
        HoraS = int(input("Opción: "))
        if HoraS == 1:
            print("En que mesa tenían reserva?")
            mesa = int(input("Mesa: "))
            if horarios["10:00"] == "reservada":
                print("bienvenidos")
            elif horarios["10:00"] == "disponible":
                print("mesa no reservada")
        if HoraS == 2:
            print("En que mesa tenían reserva?")
            mesa = int(input("Mesa: "))
            if horarios["11:00"] == "reservada":
                print("bienvenidos")
            elif horarios["11:00"] == "disponible":
                print("mesa no reservada")
        if HoraS == 3:
            print("En que mesa tenían reserva?")
            mesa = int(input("Mesa: "))
            if horarios["12:00"] == "reservada":
                print("bienvenidos")
            elif horarios["12:00"] == "disponible":
                print("mesa no reservada")
        if HoraS == 4:
            print("En que mesa tenían reserva?")
            mesa = int(input("Mesa: "))
            if horarios["13:00"] == "reservada":
                print("bienvenidos")
            elif horarios["13:00"] == "disponible":
                print("mesa no reservada")
        if HoraS == 5:
            print("En que mesa tenían reserva?")
            mesa = int(input("Mesa: "))
            if horarios["14:00"] == "reservada":
                print("bienvenidos")
            elif horarios["14:00"] == "disponible":
                print("mesa no reservada")
        return respuesta


    elif respuesta == 4:
        print("Gracias por usar el sistema")
        return respuesta
    else:
        print("opción no válida")
    print("#############################################")


respuesta = 0
while respuesta != 4:
    respuesta = consulta()

