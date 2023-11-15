#ejemplo de uso de semaforos en python, con un caso de una piscina con 8 carriles los cuales deben ser usados por nadadores de forma exclusiva

import threading
import time
import random

semaforo = threading.Semaphore(8)

class Proceso(threading.Thread):
    def run(self):
        while (True):
            semaforo.acquire()
            print("estamos corriendo")
            # tiempo para dterminar la serie
            time.sleep(random.randint(1, 7))
            # encolar la serie
            print("sacada una serie")
            semaforo.release()


if __name__ == "__main__":
    #for i in range(10):
        #print(i)
        #Proceso().start()

    Proceso().start()
    Proceso().start()
    Proceso().start()
    Proceso().start()
    Proceso().start()
    Proceso().start()
    Proceso().start()
    Proceso().start()
    Proceso().start()
    Proceso().start()

