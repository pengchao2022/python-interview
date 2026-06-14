# map() 函数，对可迭代对象中的每个元素应用函数

def square(x):
    return x ** 2       # x 的二次方

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = list(map(square, my_list))

print(new_list)



# 输出结果为 ： [1, 4, 9, 16, 25, 36, 49, 64] 为每个元素的平方

