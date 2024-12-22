# Домашнее задание по теме "Блокировки и обработка ошибок"

import random
import threading
import time


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(10):
            self.lock.acquire()
            amount = random.randint(50, 500)
            print(f"Пополнение № {_}:")
            if self.balance >= 500 and self.lock.locked():
                print(f"Баланс достиг 500, освобождаю блокировку.")
                self.lock.release()
            else:
                self.balance += amount
                print(f"Количество {amount}. Баланс: {self.balance}")
                self.lock.release()
            time.sleep(0.1)

    def take(self):
        for _ in range(10):
            self.lock.acquire()
            amount = random.randint(50, 500)
            print(f"Снятие № {_}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Количество - {amount}. Баланс: {self.balance}")
                self.lock.release()
            else:
                print(f"Количество - {amount}. Баланс недостаточен, освобождаю блокировку.")
                self.lock.release()
            time.sleep(0.1)

    def __del__(self):
        print(f"\nИтоговый баланс: {self.balance}")


bk = Bank()
thread1 = threading.Thread(target=bk.deposit)
thread2 = threading.Thread(target=bk.take)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
