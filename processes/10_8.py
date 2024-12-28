# Домашнее задание по теме "Многопроцессное программирование"
import threading
import time
from datetime import timedelta
from multiprocessing import Pool
from pathlib import Path


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not len(line):
                break
            all_data.append(line.strip())


# path = Path('Files')
# filenames = [path.name + '/' + f.name for f in path.iterdir()]
#
# start_time = time.time()
#
# for i in filenames:
#     thread = threading.Thread(target=read_info, args=(i,))
#     thread.start()
#     thread.join()
# end_time = time.time()
# elapsed = str(timedelta(seconds=end_time - start_time))
# print(f"{elapsed} (линейный)")


if __name__ == '__main__':
    start_time = time.time()

    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
    with Pool(processes=len(filenames)) as p:
        p.map(read_info, filenames)
        # p.apply_async(map(read_info, filenames))

    end_time = time.time()
    elapsed = str(timedelta(seconds=end_time - start_time))
    print(f"{elapsed} (многопроцессный)")
