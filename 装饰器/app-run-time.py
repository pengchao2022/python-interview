## 编写一个程序，计算并打印执行 100000000 次 "1+1" 操作所花费的时间。

## 使用装饰器

import time

def calculate_time(func):

    """装饰器来计算程序运行时间"""

    def wrapper(*args, **kwargs):

        start_time = time.time()

        func()

        end_time = time.time()

        cost_time = end_time - start_time

        print(f"程序运行时间为: {cost_time:.10f}")

    return wrapper

@calculate_time
def run_app():

    for _ in range(100000000):

        result = 1 + 1


run_app()