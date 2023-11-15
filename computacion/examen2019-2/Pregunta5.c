#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <chrono>
#include <cmath>
#include <semaphore.h>

void simularPartido(int partido_id, int ronda_id, sem_t semRonda, std::mutexmutexHoraActual, std::chrono::system_clock::time_point horaActual, intpartidosTerminados, int partidosPorRonda) {
    sem_wait(semRonda);

    std::unique_lock<std::mutex> lock(mutexHoraActual);
    auto inicioPartido =horaActual;
    lock.unlock();

    // Simular duración del partido (20 a 40 minutos)
    int duracionPartido = 20 + rand() % 21;
    std::this_thread::sleep_for(std::chrono::minutes(duracionPartido));

    lock.lock();
    horaActual = std::max(horaActual, inicioPartido + std::chrono::minutes(duracionPartido));
    (partidosTerminados)++;

    if (partidosTerminados == partidosPorRonda) {
        *horaActual += std::chrono::minutes(30);
        *partidosTerminados = 0;
        for (int i = 0; i < partidosPorRonda; i++) {
            sem_post(semRonda);
        }
    }
    lock.unlock();
}

int main() {
    int numEquipos = 8;
    int numRondas = static_cast<int>(std::log2(numEquipos));
    std::chrono::system_clock::time_point horaActual = std::chrono::system_clock::now();

    sem_t semRonda;
    sem_init(&semRonda, 0, 0);
    std::mutex mutexHoraActual;
    int partidosTerminados = 0;

    for (int ronda_id = 0; ronda_id < numRondas; ronda_id++) {
        int partidosPorRonda = numEquipos / (1 << (ronda_id + 1));
        std::vector<std::thread> hilosPartidos(partidosPorRonda);

        for (int partido_id = 0; partido_id < partidosPorRonda; partido_id++) {
            hilosPartidos[partido_id] = std::thread(simularPartido, partido_id, ronda_id, &semRonda, &mutexHoraActual, &horaActual, &partidosTerminados, partidosPorRonda);
        }

        for (int partido_id = 0; partido_id < partidosPorRonda; partido_id++) {
            hilosPartidos[partido_id].join();
        }
    }

    sem_destroy(&semRonda);
    return 0;
}