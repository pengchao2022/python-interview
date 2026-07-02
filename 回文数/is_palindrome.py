# 练习题目：编写一个程序，判断一个给定的数字是否是回文数（即正着读和反着读都一样）。

# 练习目的：这个练习帮助你理解“反转逻辑”。反转字符串很简单，但反转整数需要一些技巧——比如使用除法和取模运算，或者先将整数转换为字符串。这说明不同的数据类型需要不同的处理方法。

# 给定输入：

# 情况 1：number = 121（是回文数）
# 情况 2：number = 125（不是回文数）

def is_palindrome(num):

    str_num = str(num)

    return str_num == str_num[::-1] # 反转顺序


def run_app():

    num = int(input("请在此输入您的数字:"))

    result = is_palindrome(num)

    if result:

        print(f"{num} 是回文数")

    else:

        print(f"{num} 不是回文数")


run_app()

