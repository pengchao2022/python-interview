# 去除字符串两边的空格

my_string = "    maxwell loves python programming         "

new_string = my_string.strip()

print(new_string)

# 输出结果为： maxwell loves python programming 已经去除了空格

# 去除 “#”

sign_string = "###Welcome to China##"

new_sign_string = sign_string.strip("#")

print(new_sign_string)

# 输出结果为： Welcome to China

mixed_string = "&*$#####*********ALLEN loves Kate winslet*********&&"

clean_string = mixed_string.strip("&$#*")

print(clean_string)

# 输出结果为: ALLEN loves Kate winslet







