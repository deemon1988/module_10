import threading
import time
from threading import currentThread


def func1():
    for i in range(0,10):
        time.sleep(0.5)
        print(i,threading.currentThread())


def func2(x):
    for i in range(10):
        time.sleep(1)
        print(i,threading.currentThread())


thread = threading.Thread(target=func2, args=(1,), daemon=True)
thread.start()
#thread.join()
print(thread.is_alive())
func1()

print(threading.currentThread())
print(threading.enumerate())