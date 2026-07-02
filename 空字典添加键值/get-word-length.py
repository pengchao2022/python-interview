# 练习题目：创建一个包含 5 个单词的列表。编写一个循环，遍历列表中的每个单词，并打印出每个单词以及它的字符数量。

# 给定输入：words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]


# for 循环版 返回字典

def get_word_list(user_str):

    result = {} # 定义一个空字典

    for word in user_str:

        result[word] = len(word)

    return result

def run_app():

    user_input = input("请在此输入一连串的字符， 字符之间以逗号隔开: \n")

    user_str = [x.strip() for x in user_input.strip().split(',')]

    result = get_word_list(user_str)

    print(result)


if __name__ == "__main__":

    run_app()

    