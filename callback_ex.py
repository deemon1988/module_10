from concurrent.futures import ThreadPoolExecutor

def task_function(x):
    """Функция, выполняющая задачу в потоке"""
    return x * x

def callback_function(future):
    """Функция callback, которая вызывается после завершения задачи"""
    result = future.result()  # Получаем результат из Future
    print(f"Результат выполнения задачи: {result}")

# Создаем ThreadPoolExecutor для работы с потоками
with ThreadPoolExecutor(max_workers=2) as executor:
    # Отправляем задачу на выполнение
    future = executor.submit(task_function, 10)
    # Добавляем callback для выполнения после завершения задачи
    future.add_done_callback(callback_function)
