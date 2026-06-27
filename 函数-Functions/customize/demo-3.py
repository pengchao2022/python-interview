# 定义一个函数，该函数能够接收两个字符串形式的整数，计算它们的和，然后在控制台中打印出来

def sumNum():

    num1 = int(input("请在此输入第一个数字: ").strip())

    num2 = int(input("请在此输入第二个数字: ").strip())

    result = num1 + num2

    print(f"{num1} + {num2} = {result}")


sumNum()


