# 编写一个除法函数 使用 try/except 语句来捕获可能出现的异常。

def divide(a, b):

    try:
        return a / b
    
    except ZeroDivisionError:
        return "Error, 除数不能为零!"
    


def run_app():

    num1 = int(input("请在此输入第一个数: "))
    num2 = int(input("请在此输入第二个数: "))

    result = divide(num1, num2)

    print(result)


run_app()

