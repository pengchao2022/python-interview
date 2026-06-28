# 在条件判断中主动抛出异常


def divide(a, b):

    if b == 0:
        raise RuntimeError('除数不能为零!')
    else:
        return a // b
    


def run_app():

    num1 = int(input("请在此输入第一个数字: "))
    num2 = int(input("请在此输入第二个数字: "))

    result = divide(num1, num2)

    print(result)



run_app()

