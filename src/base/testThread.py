# 多进程的实现：
# 在Unix，linux，mac上可以使用fork创建子进程，需要注意的是普通的函数调用一次返回一次，fork调用一次，父进程返回一次子进程id，子进程返回一次0
if False:
    # 在os模块中实现
    # 常用函数 os.fork() 从此行后代码开始分支，下面的代码子进程和父进程分别执行一次。（windows上不能用），其返回值存在，且在父进程是子进程id，子进程是0
    #        os.getpid() 获取当前执行的进程的id
    #        os.getppid() 获取当前进程的父进程的id
    import os
    print("Process (%S) start ..."% os.getpid())
    pid=os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    # 执行结果
    # Process (876) start...
    # I (876) just created a child process (877).      父进程执行的  通过fork后pid的值判断是父进程还是子进程
    # I am child process (877) and my parent is 876.  子进程执行的

# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

# 上述的fork方法不通用，python提供了multiprocessing模块可以跨平台使用，分别包括少量子进程，大量子进程及进程间通信
if False:
    # 其中的Process类的实例代表一个进程对象 （子进程少时使用）
    # 需要Process模块和os模块，将子进程执行的内容封装为一个函数。创建子进程实例Process时，两个参数分别是子进程执行的函数和该函数需要的变量，变量封装为一个tuple
    # 创建子进程p后通过p.start()方法启动，可以用p.join()等待子进程执行完后在执行剩下的父进程的代码，用于同步时，需要子进程的数据时使用

    from multiprocessing import Process
    import os
    # 子进程要执行的代码
    def run_proc(name):
        print('Run child process %s (%s)...' % (name, os.getpid()))

    if __name__=='__main__':
        print('Parent process %s.' % os.getpid())
        p = Process(target=run_proc, args=('test',))  # 创建子进程的实例
        print('Child process will start.')
        p.start()                                     #start()方法启动
        p.join()  #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。应该是让父进程在此处等一会，等到子进程执行完后再继续执行
        print('Child process end.')
    #运行结果：
    # Parent process 14464.
    # Child process will start.
    # Run child process test (13868)...
    # Child process end.



    # 上述Process适合单个子进程，如果大量的子进程，则用进程池pool的方式批量创建子进程 （子进程多时使用）
    from multiprocessing import Pool
    import os, time, random
    def long_time_task(name):    #每个进程池执行的内容
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (name, (end - start)))

    if __name__=='__main__':
        print('Parent process %s.' % os.getpid())
        p = Pool(4)  # 代表最多同时执行几个进程，同时是瞬时，看的是cpu的核心数，所以cpu不够太高应该也没有
                    # task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的大小是4，因此，最多同时执行4个进程。
                    # Pool的默认大小是CPU的核数，
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))  #创建并启动所有子进程
        print('Waiting for all subprocesses done...')
        p.close()
        p.join() # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
        print('All subprocesses done.')
    # 运行结果
    # Parent process 888.
    # Child process will start.
    # Run child process test (25688)...
    # Child process end.
    # Parent process 888.
    # Waiting for all subprocesses done...
    # Run task 0 (50828)...
    # Run task 1 (26584)...
    # Run task 2 (28356)...
    # Run task 3 (9968)...
    # Task 1 runs 0.39 seconds.
    # Run task 4 (26584)...
    # Task 3 runs 0.99 seconds.
    # Task 4 runs 1.02 seconds.
    # Task 2 runs 1.57 seconds.
    # Task 0 runs 2.82 seconds.
    # All subprocesses done.

    # 进程间通信 Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
    # 父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
    # 意思应该是现在传的都是python的基本类型，可以直接pickle序列化为byte型，但是，如果传自己建的类，则可能失败
    # ？？？？json有方法通过dict封装类，那pickle呢，还是用json序列化？？？？？？？
    # 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
    from multiprocessing import Process, Queue
    import os, time, random

    # 写数据进程执行的代码:
    def write(q):
        print('Process to write: %s' % os.getpid())
        for value in ['A', 'B', 'C']:
            print('Put %s to queue...' % value)
            q.put(value)             #q为Queue，将通信的消息放入queue中进行通信
            time.sleep(random.random())

    # 读数据进程执行的代码:
    def read(q):
        print('Process to read: %s' % os.getpid())
        while True:
            value = q.get(True)      #q为Queue，从queue中读数据去完成通信
            print('Get %s from queue.' % value)

    if __name__=='__main__':
        # 父进程创建Queue，并传给各个子进程：
        q = Queue()
        pw = Process(target=write, args=(q,)) #两个进程都传入消息通信用的Queue
        pr = Process(target=read, args=(q,))
        pw.start()         # 启动子进程pw，写入:
        pr.start()           # 启动子进程pr，读取:
        pw.join()         # 等待pw结束，pw结束后，因为pr一直看queue，所以pr直接读到内容，接下来就可以结束了
        pr.terminate()  #pw执行完后让pr终止。pr进程里是死循环，无法等待其结束，只能强行终止:

    # 运行结果
    # Process to read: 17500
    # Process to write: 6436
    # Put A to queue...
    # Get A from queue.
    # Put B to queue...
    # Get B from queue.
    # Put C to queue...
    # Get C from queue.




# subprocess模块 可以让我们在windows的cmd命令行执行命令
if False:
    # 在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的
    import subprocess
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])  #此代码类似 cmd命令行输入 nslookup www.python.org
    print('Exit code:', r)
    #如果命令行的命令需要后续的输入，则可以通过communicate()方法输入
    import subprocess
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode("gbk"))
    print('Exit code:', p.returncode)
    # 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
    # set q=mx
    # python.org
    # exit

    # 运行结果
    # $ nslookup
    # 默认服务器:  public1.114dns.com
    # Address:  114.114.114.114
    # > > 服务器:  public1.114dns.com
    # Address:  114.114.114.114
    # python.org      MX preference = 50, mail exchanger = mail.python.org
    # >
    # Exit code: 0


# 多线程
# 写了如何实现多线程，以及多线程时对于临界资源如何加锁，还要python的缺点GIL锁
if False:
    # 任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
    # 大部分情况下我们使用Python的threading模块帮助实现多线程，如果实现不了，可以使用更基础的模块_thread
    # 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
    # 即t = threading.Thread(target=loop, name='LoopThread',args=(5,)) 创建新线程实例
    # t.start() 启动新线程 t.join() 等待t执行玩再执行后面的代码，用于同步
    # threading.current_thread().name返回当前线程的名字 主线程为MainThread 创建的线程名字为自己输入的名字LoopThread
    # current_thread() 返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定（如果不起名字Python就自动给线程命名为Thread-1，Thread-2……）
    import time, threading
    def loop():                      # 新线程执行的代码:
        print('thread %s is running...' % threading.current_thread().name)
        n = 0
        while n < 5:
            n = n + 1
            print('thread %s >>> %s' % (threading.current_thread().name, n))
            time.sleep(1)
        print('thread %s ended.' % threading.current_thread().name)

    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

    # 执行结果
    # thread MainThread is running...
    # thread LoopThread is running...
    # thread LoopThread >>> 1        
    # thread LoopThread >>> 2
    # thread LoopThread >>> 3
    # thread LoopThread >>> 4
    # thread LoopThread >>> 5
    # thread LoopThread ended.
    # thread MainThread ended.

    # 多进程：各个进程间无关联，不共用资源
    # 多线程：各个线程共用其所属进程的资源（如变量），所以临界变量必须加锁，否则会产生意料之外的结果
    # 创建一个锁就是通过threading.Lock()来实现：
    # lock.acquire() 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
    # lock.release() 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。用try...finally来确保锁一定会被释放
    import time, threading
    balance = 0           # 假定这是你的银行存款  多个线程共享此资源会导致其结果出现问题
    def change_it(n):    # 先存后取，结果应该为0。对临界资源进行改变，改变后为保持原来不变，但是不加锁其结果可能会变
        global balance
        balance = balance + n
        balance = balance - n
    lock = threading.Lock() # 创建一个锁就是通过threading.Lock()来实现：
    def run_thread(n):
        for i in range(100000):
            lock.acquire()   # 先要获取锁
            try:           #不太理解为啥放入try finally保证锁一定被释放，可能是防止try中内容有异常吧
                change_it(n)# 获取锁后，可以放心地改变balance的值
            finally:
                lock.release()# 改完了一定要释放锁

    t1 = threading.Thread(target=run_thread, args=(5,))  # 创建新线程1，并传入参数5
    t2 = threading.Thread(target=run_thread, args=(8,))  # 创建新线程2，并传入参数8
    t1.start()
    t2.start()
    t1.join()
    t2.join()               #保证两个线程都执行完后在显示现在的临界变量balance的值，其应该为0
    print(balance)


    # Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。即使100个线程跑在100核CPU上，也只能用到1个核。
    # 在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，
    # Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。因为多个Python进程有各自独立的GIL锁，互不影响
    # GIL锁：
    # 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
    # 必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
    # 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，