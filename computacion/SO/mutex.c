#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// Compilar con: gcc -pthread -o mutex mutex.c
// Ejecutar con: ./mutex

// Variable compartida entre los hilos
int counter = 0;

// Mutex para proteger la sección crítica
pthread_mutex_t mutex;

// Función que será ejecutada por cada hilo
void *increment_counter(void *arg) {
    int i;
    for (i = 0; i < 1000000; i++) {
        // Inicio de la sección crítica: adquirimos el mutex
        pthread_mutex_lock(&mutex);

        // Incrementamos la variable compartida dentro de la sección crítica
        counter++;

        // Fin de la sección crítica: liberamos el mutex
        pthread_mutex_unlock(&mutex);
    }
    // El hilo ha completado su trabajo, por lo que puede salir de la función
    pthread_exit(NULL);
}

int main() {
    pthread_t thread1, thread2;

    // Inicializamos el mutex antes de utilizarlo
    pthread_mutex_init(&mutex, NULL);

    // Creamos dos hilos que ejecutarán la misma función
    if (pthread_create(&thread1, NULL, increment_counter, NULL)) {
        fprintf(stderr, "Error al crear el hilo 1\n");
        return EXIT_FAILURE;
    }
    if (pthread_create(&thread2, NULL, increment_counter, NULL)) {
        fprintf(stderr, "Error al crear el hilo 2\n");
        return EXIT_FAILURE;
    }

    // Esperamos a que los hilos terminen su trabajo antes de continuar
    if (pthread_join(thread1, NULL)) {
        fprintf(stderr, "Error al esperar el hilo 1\n");
        return EXIT_FAILURE;
    }
    if (pthread_join(thread2, NULL)) {
        fprintf(stderr, "Error al esperar el hilo 2\n");
        return EXIT_FAILURE;
    }

    // Destruimos el mutex una vez que ya no es necesario utilizarlo
    pthread_mutex_destroy(&mutex);

    // Imprimimos el valor final de la variable compartida
    printf("Valor final de counter: %d\n", counter);

    return EXIT_SUCCESS;
}