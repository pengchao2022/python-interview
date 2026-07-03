# 练习题目：编写一个程序，打开一个已有的 .txt 文件，并统计这个文件里总共有多少个单词

import re

def count_words(filename):

    with open(filename, 'r') as file:

        content = file.read()

    # 使用正则表达式 提取 字母和数字 组成的单词，排除掉 标点符号 ，遇见's 不分割
    words = re.findall(r"\b\w+(?:'\w+)?\b", content)

    # 正则表达式 返回的是一个字符串列表
    # 统计列表的长度 就是 单词的个数
    return len(words)


def run_app():

    filename = input("请在此输入您的文件名:\n").strip()

    count_result = count_words(filename)

    print(count_result)


if __name__ == "__main__":

    run_app()

    