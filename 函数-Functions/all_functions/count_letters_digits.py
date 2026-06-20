# 题目： 编写一个程序，接受一个句子并计算其中字母和数字的数量。

# 假设程序接收以下输入：

# text
# hello world! 123
# 那么输出应为：

# text
# LETTERS 10
# DIGITS 3

def count_letters_and_digits(sentence):

    letters = 0 # 初始化
    digits = 0 # 初始化

    for char in sentence:

        if char.isalpha():
            letters += 1

        elif char.isdigit():
            digits += 1

    return letters, digits


def run_app():
    user_input = input("请在此输入一个句子:")

    count_letters, count_digits = count_letters_and_digits(user_input)

    print(f"LETTERS: {count_letters}")
    print(f"DIGITS: {count_digits}")



run_app()

