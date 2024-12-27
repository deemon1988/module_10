# Домашнее задание по теме "Многопроцессное программирование"
import threading
import time
from datetime import timedelta
from multiprocessing import Pool
from pathlib import Path
from time import sleep
from turtledemo.penrose import start


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not len(line):
                break
            all_data.append(line.strip())
    #print(all_data)

# path = Path('Files')
# filenames = [path.name +'/' +f.name for f in path.iterdir()]
# print(filenames)
#
#
# start_time = time.time()
# for i in filenames:
#     thread = threading.Thread(target=read_info, args=(i,))
#     thread.start()
# end_time = time.time()
# print(str(timedelta(seconds=end_time - start_time)))


if __name__ == '__main__':

    start_time = time.time()
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
    with Pool(processes = len(filenames)) as p:
        #p.map(read_info, filenames)
        p.apply_async(map(read_info, filenames))

    end_time = time.time()
    print(str(timedelta(seconds=end_time-start_time)))
