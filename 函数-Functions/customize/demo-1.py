# 定义一个函数 计算两书之和 

def add(num1, num2):

    result = num1 + num2

    return result


def run_app():

    num1 = int(input("请在此输入第一个数字: ").strip())

    num2 = int(input("请在此输入第二个数字: ").strip())

    expect_result = num1 + num2

    print(expect_result)

run_app()

