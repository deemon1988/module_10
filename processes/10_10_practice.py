import random
import time
from threading import Thread
import queue

class Bulka(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            time.sleep(random.randint(1,2))
            if random.random() > 0.9:
                self.queue.put('подгорелая булка')
            else:
                self.queue.put('нормальная булка')


class Kotleta(Thread):
    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run(self):
        while self.count:
            print(self.queue.qsize())
            bulka = self.queue.get()
            if bulka == 'нормальная булка':
                time.sleep(random.randint(1,3))
                self.count -= 1
            print(f'булок к приготовлению осталось: {self.count}')



queue = queue.Queue(maxsize=10)

t1 = Bulka(queue)
t2 = Kotleta(queue, 10)

t1.start()
t2.start()