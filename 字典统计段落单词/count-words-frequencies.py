# 输入一段话，统计这段话里每个单出出现的次数

import re

def count_word_frequencies(words_list):

    """
    传入一个处理好的 单词列表
    使用 get 方法
    返回一个字典
    """

    count_dict = {} # 定义一个空字典

    for word in words_list:

        count_dict[word] = count_dict.get(word, 0) + 1

    return count_dict

# 使用正则处理用户输入的段落得到一个单词列表 
def get_words_list(paragraph):

    """
    传入段落 返回一个单词列表
    """
    
    words_list = re.findall(r'[a-zA-Z]+', paragraph)

    return words_list


# 接收用户输入
def run_app():

    paragraph = input("请在此输入您的段落: \n").strip()

    words_list = get_words_list(paragraph)

    expect_dict = count_word_frequencies(words_list)

    print(expect_dict)


# 调用程序入口
if __name__ == "__main__":

    run_app()

    