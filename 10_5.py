import threading
import time
# 1 usage
def some_func():
    time.sleep(4)
    raise Exception

# 2 usages
def thread_func():
    try:
        some_func()
    except Exception as e:
        print('Wow! Exception')

t1 = threading.Thread(target=thread_func)
t2 = threading.Thread(target=thread_func)
t1.start()
t2.start()
t1.join()
t1.join()