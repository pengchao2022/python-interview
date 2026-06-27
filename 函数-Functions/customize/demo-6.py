# 定义一个函数，该函数能够接受一个整数作为输入，如果该数字是偶数，则打印 "It is an even number"，否则打印 "It is an odd number"


def determine_num(num):

    if num % 2 == 0:
        return "It is an even number"
    
    else:
        return "It is an odd number"
    

def run_app():

    num = int(input("请在此输入一个整数: "))

    result = determine_num(num)

    print(result)


run_app()

