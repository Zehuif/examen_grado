//ejemplo de semaforo en c con hilos , donde el ejemplo es una piscina con 8 pistas de nado y 10 personas que quieren nadar

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 10
#define P 8

sem_t semaforo;

void * nadar(void *arg){
    int id = *(int *)arg;
    printf("Persona %d quiere nadar \n", id);
    sem_wait(&semaforo);
    printf("Persona %d esta nadando \n", id);
    sleep(1);
    printf("Persona %d termino de nadar \n", id);
    sem_post(&semaforo);
}

int main(){
    pthread_t hilos[N];
    int id[N];
    sem_init(&semaforo, 0, P);
    for(int i = 0; i < N; i++){
        id[i] = i;
        pthread_create(&hilos[i], NULL, nadar, &id[i]);
    }
    for(int i = 0; i < N; i++){
        pthread_join(hilos[i], NULL);
    }
    sem_destroy(&semaforo);
    return 0;
}

