import multiprocessing
import os

def worker(name):
    print(f"进程 {name}，PID: {os.getpid()}")

if __name__ == "__main__":
    # 创建两个进程
    p1 = multiprocessing.Process(target=worker, args=("A",))
    p2 = multiprocessing.Process(target=worker, args=("B",))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
# 输出（PID 各不相同）：
# 进程 A，PID: 12345
# 进程 B，PID: 12346