# 属于一段英文语句，统计下里面的单词数量 

import re

def count_words_in_sentence(sentence):

    words = re.findall(r'[a-zA-Z0-9]+', sentence)

    words_num = len(words)

    return words_num, words



def run_app():

    user_sentence = input("请在此输入你的英文语句: ")

    words_num, words = count_words_in_sentence(user_sentence)

    print(f"这段英文里面共有{words_num} 个单词")

    print(f"所有单词是: {words}")
    

run_app()


