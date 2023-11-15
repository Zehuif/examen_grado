#include <stdio.h>
#include <stdlib.h>

//compilar con: gcc segfault.c -o segfault
//ejecutar con: ./segfault

int main (int argc, char *argv[])
{
    char *p = NULL;
    *p = 0;
    return 0;
}