import threading

def custom_thread_excepthook(args):
    print(f"Исключение в потоке {args.thread.name}: {args.exc_type.__name__}: {args.exc_value}")
    print(f"{args.exc_traceback}")
# Переопределяем threading.excepthook
threading.excepthook = custom_thread_excepthook

def worker():
    raise RuntimeError("Ошибка в потоке")

# Создаём поток
thread = threading.Thread(target=worker, name="TestThread")
thread.start()
thread.join()


import sys
def custom_excepthook(exc_type, exc_value, traceback):
    print(f"Исключение в главном потоке: {exc_type.__name__}: {exc_value}")
    print(traceback)

# Переопределяем sys.excepthook
sys.excepthook = custom_excepthook

# Провоцируем исключение
raise ValueError("Это ошибка в главном потоке")
