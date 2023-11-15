import time
from threading import Thread
from threading import Lock

def myfunc(i, k, mutex):
    mutex.acquire(1)
    time.sleep(1)
    i = i - k
    mutex.release()


mutex = Lock()
cantidad_participantes_total = 27

t = Thread(target=myfunc, args=(cantidad_participantes_total, 9,mutex))
t.start()

