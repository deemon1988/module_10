import threading
from threading import Event
import time

def first_worker():
    print('Первый рабочий приступил к своей задаче')
    event.wait()
    print('Первый рабочий продолжил выполнять задачу')
    time.sleep(5)
    print('Первый рабочий закончил выполнять задачу')

def second_worker():
    print('Второй рабочий приступил к своей задаче')
    time.sleep(10)
    print('Второй рабочий закончил выполнять задачу')
    event.set()

event = Event()
# event.set()
# event.clear()
# print(event.is_set())
thread1 = threading.Thread(target=first_worker)
thread2 = threading.Thread(target=second_worker)
thread1.start()
thread2.start()