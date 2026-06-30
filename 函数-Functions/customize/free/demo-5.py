# 斐波那契数列按以下公式计算：

# 当 n = 0 时，f(0) = 0

# 当 n = 1 时，f(1) = 1

# 当 n > 1 时，f(n) = f(n-1) + f(n-2)

# 请编写一个程序，根据用户在控制台输入的 n，计算 f(n) 的值。

# 示例：如果输入 n = 7，程序应输出 13。


def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def run_app():

    num = int(input("请在此输入一个数字:"))
    result = fibonacci(num)
    print(f"结果是: {result}")


run_app()

