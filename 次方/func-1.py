# 练习题目：编写一个名为 exponent(base, exp) 的函数，计算并返回 base 的 exp 次方（即 base^exp）。

# 练习目的：这个练习帮助你理解“累加器模式”。虽然 Python 提供了内置的幂运算符（**），但手动实现它可以让你更清楚地看到重复乘法的过程，以及函数如何将计算结果返回给调用者。

# 给定输入：base = 2, exp = 5


def exponent(base, exp):

    return base ** exp


def run_app():

    base = int(input("请在此输入基数: \n"))

    exp = int(input("请在此输入此方: \n"))

    result = exponent(base, exp)

    print(result)

run_app()


