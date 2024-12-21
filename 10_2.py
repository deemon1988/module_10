import threading
from threading import Thread
import time
from time import sleep


class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print(f'Поток {self.name} запущен')
        self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершен')

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f"{name} {time.ctime(time.time())}")
            counter -= 1


thread1 = MyThread('thread1', 3, 0.1)
thread2 = MyThread('thread2',3, 0.2)
thread1.start()
thread2.start()

