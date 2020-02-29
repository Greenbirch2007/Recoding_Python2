import multiprocessing


def funct_xxx(xx):
    print(xx)


if __name__ == '__main__':
    # 1,创建一个进程池
    pool = multiprocessing.Pool(3)  # 3代表最大进程数同时运行  ****但是一开始就已创建3个工作进程 加上主进程就是4个   不写就是系统最大的进程数 和CPU核数有关
    # 2,创建进程池中的通信
    queue = multiprocessing.Manager().Queue(4)  # 用法和上面一致

    # 3,添加任务
    pool.apply(func=funct_xxx,args=(1,))   # 添加任务并且阻塞等待任务执行完成   能保证顺序
    pool.apply_async(func=funct_xxx,args=(2,))  # 异步添加任务  不阻塞等待任务执行完成   ***用的多
    # 4,关闭进程池
    pool.close()
    pool.join()    ## 必须放在close或者terminate之后使用;
    print("关闭进程池")
