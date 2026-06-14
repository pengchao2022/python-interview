# replace() 用于替换

my_text = "Good morning, Kate.winslet, How is going today ?"

new_text = my_text.replace("."," ") # 将 Kate.winslet 之间的 . 替换为空格

print(new_text)

# 输出结果为： Good morning, Kate winslet, How is going today ?

text_1 = my_text.replace("K", "k") # 将 Kate.winslet 中大些的K 替换为小写的 k

print(text_1)

# 输出结果为： Good morning, kate.winslet, How is going today ?

text_2 = my_text.replace("Kate.winslet", "maxwell ma")

print(text_2)

# 输出结果为： Good morning, maxwell ma, How is going today ?










