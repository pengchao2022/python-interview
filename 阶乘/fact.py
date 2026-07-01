# 输入一个数字计算阶乘

def fact(num):

    if num == 0:

        return 1
    
    else:

        return num * fact(num - 1)
    

def run_app():

    num = int(input("请在此输入您的数字: "))

    result = fact(num)

    print(f"{num} 的阶乘为: {result}")


run_app()

