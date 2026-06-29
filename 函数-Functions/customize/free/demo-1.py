# 编写一个程序，计算 1/2 + 2/3 + 3/4 + ... + n/(n+1) 的值，其中 n 通过控制台输入（n > 0）。

# 示例：如果输入以下 n：

# 5

# 那么程序的输出应为：

# 3.55

# 如果输入数据提供给问题，则应假定为控制台输入。

def sum(num):

    total = 0
    for i in range(1, num + 1):
        total += i / (i + 1)

    return total


def run_app():

    num = int(input("请在此输入您的数字: "))
    result = sum(num)

    print(f"结果为: {result:.2f}")


run_app()