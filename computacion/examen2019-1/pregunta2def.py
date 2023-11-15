Value1 = 1
PiscinaPrincipal = {"Pista1":"","Pista2":"","Pista3":"","Pista4":"","Pista5":"","Pista6":"","Pista7":"","Pista8":""}
PiscinaPractica = {"Pista1":"","Pista2":"","Pista3":"","Pista4":"","Pista5":"","Pista6":"","Pista7":"","Pista8":""}


def main():
    
    print("Sistema de Cometidores")
    
    while(True):
        
        print("1.Reellenar Piscina Principal")
        print("2.Reellenar Piscina Practica")
        print("3.Vaciar Piscina")
        eleccion = str(input("Elige lo que haras: "))
      
        if eleccion == '1':
            for i in range(0,8):
               nombre = str(input("Nombre del competidor de la pista", i, ":")) 

               PiscinaPrincipal['pista%s' % i] = {nombre}
        
        elif eleccion == '2':
            for i in range(0,8):
               nombre = str(input("Nombre del competidor de la pista", i, ":")) 

               PiscinaPrincipal['pista%s' % i] = {nombre}
            
        elif eleccion == '3':
            print("vaciando")
            for i in range(0,8):
                PiscinaPrincipal['pista+%s', i] = {""}

        else:
            print("Tamos pal webeo")
    
main()