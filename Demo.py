"""
import _thread
import time


# 为线程定义一个函数
def print_time(treadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s:%s' % (treadName, time.ctime(time.time())))


# 创建连个线程
try:
    _thread.start_new_thread(print_time, ('Thread-1', 2))
    _thread.start_new_thread(print_time, ('Thread-2', 4))
except Exception as ex:
    print('Error:%s' % (ex))

while 1:
    pass
"""
import threading
import time
