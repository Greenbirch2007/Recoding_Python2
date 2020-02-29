"""解决多线程共享数据引起竞争的问题-互斥锁"""
import threading

g_number = 0


def hello(lock):
    for i in range(10):
        global g_number
        # 申请加锁
        lock.acquire()
        g_number += 1
        # 释放互斥锁
        # time.sleep(1)
        print('hello')
        lock.release()

def world(lock):
    for i in range(10):
        global g_number
        lock.acquire()
        g_number += 1
        print("world")
        lock.release()


if __name__ == '__main__':

    # 申请一个锁
    lock = threading.Lock()

    # 将锁传入线程中
    hello_thd = threading.Thread(target=hello,args=(lock,))
    world_thd = threading.Thread(target=world,args=(lock,))

    hello_thd.start()
    world_thd.start()

    hello_thd.join()
    world_thd.join()

    print(g_number)
