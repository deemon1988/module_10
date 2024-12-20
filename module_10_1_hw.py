# Домашнее задание по теме "Создание потоков"
import threading
import time


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1,word_count+1):
            file.write(f"Какое-то слово № {i} \n" )
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

def get_time(elapsed_time):
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    formatted_time = f"{int(hours):02}:{int(minutes):02}:{seconds:02}"
    return formatted_time

start_func = time.time()
wite_words(10, 'example1.txt')
wite_words(20, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_func = time.time()
elapsed_func = round(end_func - start_func, 3)

print(f"Выполнение функций завершилось за {get_time(elapsed_func)}")
start_thread = time.time()
thread1 = threading.Thread(target=wite_words ,args=(10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words ,args=(30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words ,args=(200, 'example7.txt'))
thread4 = threading.Thread(target=wite_words ,args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
print("Ожидание завершения дочернего потока...")
thread1.join()
thread2.join()
thread3.join()
thread4.join()
print("Основной поток завершен")
end_thread = time.time()
elapsed_thread = round(end_thread - start_thread, 3)
print(f"Выполнение потоков завершилось за {get_time(elapsed_thread)}")
