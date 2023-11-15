//ejemplo de semaforo en c con hilos , donde el ejemplo es una piscina con 8 pistas de nado y 10 personas que quieren nadar, pero cuando entran a nadar tienen un nueva seccion critica protegida por un mutex al cual le sumaran un 1 cada vez que entre llamada contador este mutex estara dentro de la seccion critica del semaforo, osea dentro del semaforo, finalmente imprimira el valor de contador

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 10
#define P 8

sem_t semaforo;
int contador = 0;
pthread_mutex_t mutex;

void * nadar(void *arg){
    int id = *(int *)arg;
    printf("Persona %d quiere nadar \n", id);
    sem_wait(&semaforo);
    printf("Persona %d esta nadando \n", id);
    pthread_mutex_lock(&mutex);
    contador++;
    printf("contador = %d \n", contador);
    pthread_mutex_unlock(&mutex);
    sleep(1);
    printf("Persona %d termino de nadar \n", id);
    sem_post(&semaforo);
}

int main(){
    pthread_t hilos[N];
    int id[N];
    sem_init(&semaforo, 0, P);
    pthread_mutex_init(&mutex, NULL);
    for(int i = 0; i < N; i++){
        id[i] = i;
        pthread_create(&hilos[i], NULL, nadar, &id[i]);
    }
    for(int i = 0; i < N; i++){
        pthread_join(hilos[i], NULL);
    }
    sem_destroy(&semaforo);
    pthread_mutex_destroy(&mutex);
    printf("contador = %d \n", contador);
    return 0;
}