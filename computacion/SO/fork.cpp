#include <iostream>
#include <unistd.h>

using namespace std;

// Compilar y ejecutar:
// g++ -o fork fork.cpp
// ./fork

int main()
{
    int pid = fork(); // Crea un proceso hijo y obtiene su ID de proceso
    
    if (pid == 0) { // Si el ID de proceso es 0, se trata del proceso hijo
        cout << "Hola desde el proceso hijo con pid "<< getpid() << endl;
    } else if (pid > 0) { // Si el ID de proceso es mayor que 0, se trata del proceso padre
        cout << "Hola desde el proceso padre con pid "<< getpid() << endl;
    } else { // Si el ID de proceso es menor que 0, hubo un error al crear el proceso hijo
        cerr << "Error al crear el proceso hijo." << endl;
        return 1;
    }
    
    return 0;
}