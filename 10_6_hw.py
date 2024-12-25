# Домашнее задание по теме "Очереди для обмена данными между потоками"

import threading
import time
from operator import index
from queue import Queue
from random import randint


class Table():
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


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
        for index, guest in enumerate(guests):
            if len(self.tables):
                global table
                try:
                    table = next(it)
                except StopIteration:
                    table = None
                if not table == None:
                    self.tables[index].guest = guest
                    print(f"{guest.name} сел за стол номер {table.number}")
                    guest.start()
                else:
                    print(f"{guest.name} в очереди")
                    self.queue.put(guest)
                    continue


    def discuss_guests(self):
        guests_threads = {}
        tables_data = {}
        empty_tables = []
        for thread in threading.enumerate():
            if isinstance(thread, Guest):
                guests_threads[thread.name] = thread
        for table in self.tables:
            if table.guest.name in guests_threads:
                tables_data[table.guest] = table


        for name, guest_th in guests_threads.items():
            while not self.queue.empty():
                if not guest_th.is_alive():
                    print(f"{name} покушал(-а) и ушёл(ушла)")

                    print(f"Стол номер {tables_data[guest_th].number} свободен")

                    tables_data[guest_th].guest = None
                    empty_tables.append(tables_data[guest_th])
                    await_guest = self.queue.get()

                    print(f"{await_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tables_data[guest_th].number}")

                    tables_data[guest_th].guest =  await_guest

                    await_guest.start()




table1 = Table(1)
table2 = Table(2)
guest1 = Guest('Vasya')
guest2 = Guest('Vanya')
guest3 = Guest('Danya')
cafe = Cafe(table1, table2)

cafe.guest_arrival(guest1, guest2, guest3)
cafe.discuss_guests()