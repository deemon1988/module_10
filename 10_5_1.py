import threading
import sys
import time


# 1 usage
def excepthook_2(args, a, b):
    print('handeled')
    print(args)
    print(a)
    print(b)


sys.excepthook = excepthook_2


# 2 usages
def some_func():
    time.sleep(1)
    raise Exception


# 1 usage
def excepthook(args):
    print(args.thread.is_alive())
    print(args.thread.name)


threading.excepthook = excepthook
t1 = threading.Thread(target=some_func)
t2 = threading.Thread(target=some_func)
t1.start()
t2.start()
t1.join()
t2.join()
raise Exception
