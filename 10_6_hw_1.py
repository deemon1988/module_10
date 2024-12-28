# Домашнее задание по теме "Очереди для обмена данными между потоками"

import threading
import time
from itertools import zip_longest
from queue import Queue
from random import randint


class Table():
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

    def __str__(self):
        return f"Стол: {self.number}, {self.guest.name}"


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        r_time = randint(3, 10)
        # print(r_time)
        time.sleep(r_time)


class Cafe():
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):

        for tab, guest in zip_longest(self.tables, guests):
            if not tab == None and not guest == None:
                tab.guest = guest
                print(f"{guest.name} сел за стол номер {tab.number}")
                tab.guest.start()

            elif tab == None and not guest == None:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):

        def guest_alive():
            for t in self.tables:
                if not t.guest == None:
                    if t.guest.is_alive():
                        yield t
                    elif not self.queue.empty():
                        print(f"{t.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {t.number} свободен")
                        await_guest = self.queue.get()
                        print(f"{await_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
                        t.guest = await_guest
                        t.guest.start()
                        yield t
                    else:
                        print(f"{t.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {t.number} свободен")
                        t.guest = None

        while True:
            guests_serviced = list(guest_alive())
            if not len(guests_serviced):
                break


# table1 = Table(1)
# table2 = Table(2)
# guest1 = Guest('Vasya')
# guest2 = Guest('Vanya')
# guest3 = Guest('Danya')
# cafe = Cafe(table1, table2)
#
# cafe.guest_arrival(guest1, guest2, guest3)
# cafe.discuss_guests()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)

start_time = time.time()
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
end_time = time.time()
print(f"Время выполнения: {end_time - start_time} c.")
