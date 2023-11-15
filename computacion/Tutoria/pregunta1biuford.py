tutorias = {}

validar = True

while (validar):
    print("1. Añadir una tutoría")
    print("2. Añadir un profesor a una tutoría")
    print("3. Imprimir las tutorías y sus profesores")
    print("4. Eliminar un profesor de una tutoría")
    print("5. Eliminar una tutoría")
    print("6. Actualizar el nombre de un profesor de una tutoría")
    print("7. Actualizar el nombre de una tutoría")
    print("8. Terminar el programa")

    entry = str(input("Que desea hacer?: "))
    
    if entry == "1":
        name = str(input("Ingrese nombre de tutoría: "))
        tutorias[name] = {"profesores": []}
        
    elif entry == "2":
        name = str(input("Ingrese nombre del profesor: "))
        nameTuto = str(input("Ingrese nombre de la tutoría a ingresar al profesor: "))
        verify = False
        for clave, valor in tutorias.items():
            if clave == nameTuto:
                verify = True
        if verify:
            tutorias[nameTuto]["profesores"].append(name)
        else:
            print("El nombre de la tutoría no se encuentra registrada")

    elif entry == "3":
        for clave, valor in tutorias.items():
            print(" ")
            print(clave + ":", valor)
        print(" ")
        
    elif entry == "4":
        name = str(input("Ingrese nombre del profesor: "))
        nameTuto = str(input("Ingrese nombre de la tutoría del profesor a eliminar: "))
        verify = False
        for clave, valor in tutorias.items():
            if clave == nameTuto:
                verify = True
        if verify:
            if name in tutorias[nameTuto]["profesores"]:
                tutorias[nameTuto]["profesores"].remove(name)
            else:
                print("El nombre del profesor ingresado no esta registrado en ela tutoría indicada")
        else:
            print("El nombre de la tutoría no se encuentra registrada")
            
    elif entry == "5":
        nameTuto = str(input("Ingrese nombre de la tutoría a eliminar: "))
        verify = False
        for clave, valor in tutorias.items():
            if clave == nameTuto:
                verify = True
        if verify:
            del tutorias[nameTuto]
        else:
            print("El nombre de la tutoría no se encuentra registrada")
            
    elif entry == "6":
        name = str(input("Ingrese nombre del profesor a actualizar: "))
        nameTuto = str(input("Ingrese nombre de la tutoría del profesor a eliminar: "))
        newName = str(input("Ingrese nombre del nuevo profesor: "))
        verify = False
        for clave, valor in tutorias.items():
            if clave == nameTuto:
                verify = True
        if verify:
            if name in tutorias[nameTuto]["profesores"]:
                tutorias[nameTuto]["profesores"][tutorias[nameTuto]["profesores"].index(name)] = newName
            else:
                print("El nombre del profesor ingresado no esta registrado en ela tutoría indicada")
        else:
            print("El nombre de la tutoría no se encuentra registrada")
            
    elif entry == "7":
        nameTuto = str(input("Ingrese nombre de la tutoría a actualizar: "))
        newNameTuto = str(input("Ingrese nombre de la nueva tutoría: "))
        verify = False
        for clave, valor in tutorias.items():
            if clave == nameTuto:
                verify = True
        if verify:
            tutorias[newNameTuto] = tutorias[nameTuto]
            del tutorias[nameTuto]
        else:
            print("El nombre de la tutoría no se encuentra registrada")
    
    elif entry == "8":  
        validar = False