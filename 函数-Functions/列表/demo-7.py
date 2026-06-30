# 编写一个程序，接收用户输入的一串由空格分隔的单词，然后打印出其中仅包含数字的单词。

text = input("请在此输入一串字符中间以空格隔开:")


# 生成列表
words = text.split()


# 列表推导式
result = [word for word in words if word.isdigit()]


print(result)

