# this decrator is to calculate the app running time

import time

def decrator(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        cost_time = end_time - start_time
        print(f"程序运行时间为: {cost_time}")

    return inner


@decrator
def my_app():
    time.sleep(10)



my_app()