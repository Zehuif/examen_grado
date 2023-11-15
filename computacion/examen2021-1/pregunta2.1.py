import threading
import time
import random

class Queue_de_series:
    def __init__(self):
        self.series = []

    def isEmpty(self):
        return self.series == []

    def enqueue(self, serie):
        self.series.insert(0,serie)

    def dequeue(self):
        if self.size()==0:
            print("lista vacia")
            return ("lista vacia")
        return self.series.pop()

    def size(self):
        return len(self.series)

queue = Queue_de_series()
global mutex_carril1
global mutex_carril2
global mutex_carril3
global mutex_carril4
global mutex_carril5
global mutex_carril6
global mutex_carril7
global mutex_carril8
global mutex_carril9


class Proceso_rellenador_carriles(threading.Thread):
    def run(self):
        while (True):
             # tiempo para encolar la serie
            print("encolando")
            time.sleep(random.randint(1, 5))
            time.sleep(10)
            # encolar la serie
            queue.enqueue([1,2,3,4,5,6,7,8,9])
            print("ingresado a sus carriles: ", [1,2,3,4,5,6,7,8,9] )
            time.sleep(1)
            
class Proceso_carrera(threading.Thread):
    def run(self):
        while (True):
            mutex_carril1.acquire()
            mutex_carril2.acquire()
            mutex_carril3.acquire()
            mutex_carril4.acquire()
            mutex_carril5.acquire()
            mutex_carril6.acquire()
            mutex_carril7.acquire()
            mutex_carril8.acquire()
            mutex_carril9.acquire()
            print("estamos corriendo")
            # tiempo para dterminar la serie
            time.sleep(random.randint(1, 7))
            # encolar la serie
            queue.dequeue()
            print("sacada una serie")
            mutex_carril1.release()
            mutex_carril2.release()
            mutex_carril3.release()
            mutex_carril4.release()
            mutex_carril5.release()
            mutex_carril6.release()
            mutex_carril7.release()
            mutex_carril8.release()
            mutex_carril9.release()
            print("terminamos de correr")
            # tiempo para desencolar la serie a la piscina 1
rellenador = Proceso_rellenador_carriles()
rellenador.start()
desencolador=Proceso_carrera()
desencolador.start()

rellenador.join()
desencolador.join()