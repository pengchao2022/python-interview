# 编写一个程序，使用 map() 函数生成一个列表，该列表的元素是介于1和20之间（包含两端）的数字的平方。


new_list = []

for i in range(1, 21):

    new_list.append(i)

result = map(lambda x: x ** 2, new_list)

expect_list = list(result)

print(expect_list)

