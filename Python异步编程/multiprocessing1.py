import multiprocessing
import time

def func(queue):
    if not queue.empty():
        for i in range(queue.qsize()):
            print(queue.get_nowait())    #  get_nowait()  ===get(True,0)   0是时间默认-1 T阻塞状态
            time.sleep(1)

def main():
    # 创建一个进程间通信队列
    queue = multiprocessing.Queue(3) 

    # 声明一个进程
    pro = multiprocessing.Process(target=func,args=(queue,))
    # 创建一个进程并开启
    pro.start()

    for i in range(3):
        queue.put_nowait('消息%s'%i)

    if not queue.full():
        queue.put_nowait("消息4")     #  put_nowait()===put('xxdata',True,0) 0是时间默认-1
    else:
        print("消息队列满了")

    pro.join()
    pro.terminate()  # 杀死进程
    a= pro.is_alive()  # 判断是否还活着 有一定的延时行
    print(a)


if __name__=="__main__":
    main()
