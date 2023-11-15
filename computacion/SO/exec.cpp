#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

// Compilar y ejecutar:
// g++ -o exec exec.cpp
// ./exec

int main (int argc, char *argv[])
{
    //father y child son los pid de los procesos
    pid_t father, child;
    father = getpid();
    printf("Father: %d\n", father);
    child = fork();

    //Si el pid es 0, es el proceso hijo y ejecuta el comando ls
    if (child == 0) {
        printf("Proceso hijo, pronto a llamar a exec\n");
        execl("/bin/ls", "ls", "-l", NULL);
        printf("Proceso hijo, despues de llamar a exec\n");
    } 
    
    //Si el pid es mayor que 0, es el proceso padre
    else if (child > 0) {
        printf("Proceso padre, el proceso hijo es: %d \n", child);
    }

    return 0;
}