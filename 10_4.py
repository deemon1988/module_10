import threading
from threading import Thread


# def count_up(name, n):
#     for i in range(n):
#         print(name, i, sep=": ")
#
#
# t1 = Thread(target=count_up, args=("Thread1", 25))
# t2 = Thread(target=count_up, args=("Thread2", 25))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

import datetime
import json
# from random import randint
# res = []
files = ["file1.json", "file2.json", "file3.json", "file4.json"]
# for file in files:
#     def random_numbers():
#         for _ in range(100_000):
#             yield randint(0, 10000)
#             #res.append(randint(0, 10000))
#     with open(file, "w") as f:
#         json.dump(list(random_numbers()), f)
#     #res = []

def main():
    res_to_count = []
    start = datetime.datetime.now()
    # total_sum = sum(num for file in files for num in json.load(open(file, 'r')))
    # print(total_sum)
    for file in files:
        with open(file, "r") as f:
            data = json.load(f)
            res_to_count.extend(data)
    sum(res_to_count)

    end = datetime.datetime.now()
    return end - start


time_calc = []
for i in range(100):
    res = []
    time_calc.append(main())

print(sum([calc.microseconds for calc in time_calc])/len(time_calc))