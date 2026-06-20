# 正则匹配

import re

sentence = "My name is Maxwell, I am 37 years old, I come from Shanghai" \
           "我的名字叫麦克斯韦，我今年37岁，我来自上海"


english_words = re.findall(r'[a-zA-Z]+', sentence)

type_english_words = type(english_words)

count_english_words = len(english_words)


chinese_words = re.findall(r'[\u4e00-\u9fff]', sentence)

type_chinese_words = type(chinese_words)

count_chinese_words = len(chinese_words)


# 统计英文单词加数字

english_words_and_numbers = re.findall(r'[a-zA-Z0-9]+', sentence)

couunt_english_words_with_numbers = len(english_words_and_numbers)



print(f" english words in list are: {english_words}")

print(f"返回值类型为: {type_english_words}")

print(f"英文单词的数量为: {count_english_words}")

print(f" chinese words in list are: {chinese_words}")

print(f"返回值类型为: {type_chinese_words}")

print(f"中文字符的数量为: {count_chinese_words}")

print(f"英文单词加数字的数量为:{couunt_english_words_with_numbers}")

print(f"英文单词加数字的列表为: {english_words_and_numbers}")













