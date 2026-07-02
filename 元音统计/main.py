# 练习题目：编写一个程序，统计给定句子中元音字母（a、e、i、o、u）出现的总次数。

# 练习目的：这个练习帮助你理解“成员测试”。通过判断一个字符是否属于某个特定组（元音字母），你可以学习如何根据类别筛选数据。这是构建文本分析工具或垃圾邮件过滤系统的基础。

# 给定输入：sentence = "Learning Python is fun!"

def count_vowels(sentence):

    vowels = 'aeiou'
    count = 0

    for char in sentence:
        if char in vowels:
            count += 1

    return count


def run_app():

    user_sentence = input("请在此输入您的英文句子: ")
    sentence = user_sentence.strip()

    result = count_vowels(sentence)

    print(f"元音统计结果为: {result}")


run_app()

