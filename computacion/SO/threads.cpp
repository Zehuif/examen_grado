#include <iostream>
#include <thread>  // Biblioteca para utilizar threads
#include <unistd.h>  // Biblioteca para utilizar getpid()

// Compilar y ejecutar:
// g++ threads.cpp -pthread -o threads
// ./threads

using namespace std;

// Función que se ejecutará en el thread
void threadFunction() {
    int pid_t = getpid();  // Obtener el pid del thread
    cout << "Hola desde el thread con pid = " << pid_t << endl;
}

int main() {
    // Crear un thread y ejecutar la función threadFunction con el argumento 42
    thread t(threadFunction);  // Crear un thread y pasarle la función threadFunction y el argumento 42

    int pid = getpid();  // Obtener el pid del thread principal
    cout << "Hola desde el thread principal con pid = " << pid << endl;

    // Esperar a que el thread termine
    t.join();  // Esperar a que el thread termine de ejecutar la función

    cout << "Fin del programa" << endl;

    return 0;
}