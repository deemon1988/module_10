# Домашнее задание по теме "Очереди для обмена данными между потоками"

import threading
import time
from queue import Queue
from random import randint


class Table():
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

    def __str__(self):
        return f"{self.number}, {self.guest}"

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3,10))


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
                    guest.start()       # где стартовать ?
                else:
                    print(f"{guest.name} в очереди")
                    self.queue.put(guest)
                    continue


    def discuss_guests(self):
        guests_threads = []
        tables_data = []
        for thread in threading.enumerate():
            if isinstance(thread, Guest):
                guests_threads.append(thread)
        for table in self.tables:
            if table.guest in guests_threads:
                tables_data.append(table)

        #is_guest = True
        while len(guests_threads):
            for guest in guests_threads:
                guest.join()
                if guest.is_alive():
                    is_guest = True  # guest.join() ?
                else:
                    print(f"{guest.name} покушал(-а) и ушёл(ушла)")
                    #is_guest = False
                    empty_table = [t for t in tables_data if t.guest == guest]
                    guests_threads.remove(guest)
                    print(f"Оставшиеся потоки: {guests_threads}")
                    print()

                    table = empty_table.pop()
                    #tables_data = list(map(lambda x: table if x.guest == guest else x, tables_data))
                    if not self.queue.empty():
                        print(f"Стол номер {table.number} свободен")
                        await_guest = self.queue.get()
                        print(f"{await_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest =  await_guest
                        guests_threads.append(await_guest)
                        await_guest.start()
                        is_guest = True

        print(threading.enumerate())
        print(f"Строка на выходе")




table1 = Table(1)
table2 = Table(2)
guest1 = Guest('Vasya')
guest2 = Guest('Vanya')
guest3 = Guest('Danya')
cafe = Cafe(table1, table2)

cafe.guest_arrival(guest1, guest2, guest3)
cafe.discuss_guests()