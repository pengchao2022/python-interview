# 提取段多种的单词包括含有数字的单词 

# 结果会返回一个 单词 含有数字的单词 列表

import re

text = "This is a classic “Natural Language Processing” (NLP) task. " \
"It teaches you how to map data to occurrences," \
" which is the logic used by search engines to index web pages or " \
"by social media platforms to identify trending hashtags." \
" Designed by Maxwell @2026 ."

words = re.findall(r'\w+', text)

print(words)



