# 编写一个程序，计算以下递推公式的值：

# f(n) = f(n-1) + 100，当 n > 0 时，且 f(0) = 1

# n 由用户在控制台输入（n > 0）。

# 示例：如果输入 n = 5，则程序应输出 500。

def func(n):

    if n == 0:
        return 1
    else:
        return func(n-1) + 100
    

def run_app():

    num = int(input("请在此输入一个数字: "))
    result = func(num)

    print(result)


run_app()

