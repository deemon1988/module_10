# Домашнее задание по теме "Потоки на классах"

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f"{self.name} на нас напали!")
        self.battle()

    def battle(self):
        days_gone = 0
        while self.enemies:
            time.sleep(1)
            self.enemies -= self.power
            days_gone += 1
            print(f"{self.name} сражается {days_gone} день, врагов осталось {self.enemies} ")
        print(f"{self.name} одержал победу спустя {days_gone} дней(дня)")


knight1 = Knight('sir Lancelot', 10)
knight1.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()
