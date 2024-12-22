import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(10):
            # Захват блокировки
            self.lock.acquire()
            try:
                print(f'Пополнение № {_}:')
                amount = random.randint(50, 500)
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

                # Если баланс >= 500 и блокировка захвачена, освобождаем её
                if self.balance >= 500 and self.lock.locked():
                    print(f"Баланс достиг 500, освобождаю блокировку.")
                    self.lock.release()  # Освобождаем блокировку
            finally:
                # Если блокировка не освобождена, освобождаем её
                if self.lock.locked():
                    self.lock.release()
            time.sleep(0.5)  # имитация случайной задержки

    def take(self):
        for _ in range(10):
            # Захват блокировки
            self.lock.acquire()
            try:
                print(f'Запрос на Снятие № {_}:')
                amount = random.randint(50, 500)
                print(f"Запрос на {amount}")
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")
                    self.lock.release()
            finally:
                # Освобождаем блокировку после выполнения операции
                if self.lock.locked():
                    self.lock.release()
            time.sleep(0.5)  # имитация случайной задержки


# Создание экземпляра банка
bank = Bank()

# Создание потоков для пополнения и снятия
deposit_thread = threading.Thread(target=bank.deposit)
take_thread = threading.Thread(target=bank.take)

# Запуск потоков
deposit_thread.start()
take_thread.start()

# Ожидание завершения потоков
deposit_thread.join()
take_thread.join()

