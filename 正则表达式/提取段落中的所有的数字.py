# 正则表达式 提取段落中的纯数字

# 返回一个数字列表

import re

text = "This is a classic “Natural Language Processing” (NLP) task." \
" It teaches you how to map data to occurrences, " \
"which is the logic used by search engines to index " \
"web pages or by social media platforms to identify trending hashtags." \
"All rights reversed @2026 " \
"123, 9.89 -34"

# 匹配段落中的所有数字
digits = re.findall(r'-?\d+\.\d+e?-?\d*|-?\d+\.\d+|-?\d+', text)

print(digits)

