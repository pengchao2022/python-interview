# 提取段落中的纯单词

# 不包含数字

# 返回一个 纯单词 列表

import re

text = "This is a classic “Natural Language Processing” (NLP) task. " \
"It teaches you how to map data to occurrences," \
" which is the logic used by search engines to index web pages or " \
"by social media platforms to identify trending hashtags." \
" Designed by Maxwell @2026 ."


words = re.findall(r'[a-zA-Z]+', text)


print(words)

