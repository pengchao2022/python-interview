import time

def log(func):
    def log_record():
        timestamp = time.time()
        readable_time = time.ctime(timestamp)
        print(f"{readable_time} we are calling your application {func.__name__} function")
        func()

    return log_record




@log
def add():
    num1 = int(input("Please type your first numebr here:"))
    num2 = int(input("Please type your second number here:"))
    result = num1 + num2
    print(f"{num1}+{num2}={result}")


@log
def sub():
    num1 = int(input("Please type your first numebr here:"))
    num2 = int(input("Please type your second number here:"))
    result = num1 - num2
    print(f"{num1}-{num2}={result}")



add()

sub()
