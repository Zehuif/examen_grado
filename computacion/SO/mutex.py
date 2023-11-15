#ejemplo de uso de un mutex en python

import threading
import time
import random

mutex = threading.Lock()

class Proceso(threading.Thread):
    def run(self):
        while (True):
            mutex.acquire()
            print("estamos corriendo")
            # tiempo para dterminar la serie
            time.sleep(random.randint(1, 7))
            # encolar la serie
            print("sacada una serie")
            mutex.release()

if __name__ == "__main__":
    for i in range(10):
        Proceso().start()


