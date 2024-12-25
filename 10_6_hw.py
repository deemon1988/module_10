import threading
import time
from queue import Queue
from random import randint


class Table():
    def __init__(self, number, name=None):
        self.number = number
        self.name = name


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        rand_time = randint(3,10)
        print(rand_time)
        time.sleep(rand_time)


class Cafe():
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        it = iter(self.tables)
        for guest in guests:
            if len(self.tables):
                try:
                    table =  next(it)
                    if table:
                        table.name = guest.name
                        print(f"{guest.name} сел за стол номер {table.number}")
                        guest.start()
                except StopIteration:
                    print(f"{guest.name} в очереди")
                    self.queue.put(guest)
                    continue





    def discuss_guests(self):
        pass


table1 = Table(1)
table2 = Table(2)
guest1 = Guest('Vasya')
guest2 = Guest('Vanya')
guest3 = Guest('Danya')
cafe = Cafe(table1, table2)

cafe.guest_arrival(guest1, guest2, guest3)