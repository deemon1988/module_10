import threading
import time


def increment(name):
  global counter
  lock.acquire()
  for i in range(10):
    counter += 1
    print(name, counter)
  lock.release()

def decrement(name):
  global counter
  lock.acquire()
  for i in range(10):
    counter -= 1
    print(name, counter)
  lock.release()

lock = threading.Lock()
counter = 0

thread1 = threading.Thread(target=increment, args=('thread1',))
thread2 = threading.Thread(target=decrement, args=('thread2',))
thread3 = threading.Thread(target=increment, args=('thread3',))
thread4 = threading.Thread(target=decrement, args=('thread4',))

thread1.start()
print(threading.current_thread())
thread2.start()
print(threading.current_thread())
thread3.start()
print(threading.current_thread())
thread4.start()
print(threading.current_thread())