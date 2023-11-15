#include <iostream>
#include <unistd.h>
#include <stdio.h>

// Compilar y ejecutar:
// g++ -o pipes pipes.cpp
// ./pipes

using namespace std;

int main()
{
    FILE *ls = popen("ls", "r"); // Ejecuta el comando "ls" y abre un pipe de lectura
    FILE *grep = popen("grep cpp", "w"); // Ejecuta el comando "grep cpp" y abre un pipe de escritura
    
    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), ls)) { // Lee la salida del comando "ls" línea por línea
        fputs(buffer, grep); // Escribe cada línea en el pipe del comando "grep"
    }
    
    pclose(ls); // Cierra el pipe del comando "ls"
    pclose(grep); // Cierra el pipe del comando "grep"
    
    return 0;
}


