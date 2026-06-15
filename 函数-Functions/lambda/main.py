# lambda() 是一个 匿名函数
# lambda 参数: 表达式

# 函数的几种等价写法

# 方法一：

def add_t(x, y):
    return x + y

# 方法二： 不用 def ,使用 lambda

add_l = lambda x, y: x + y         # lambda 参数: 表达式

print(add_t(8, 9))

print(add_l(8, 9))


# 输出结果都是 17


# 举例 将 students 以年龄排序

students = [('kate', 20), ('jim', 16), ('lily', 80), ('sophia', 14)]

students.sort(key=lambda x: x[1]) # 按照年龄来排序

print(students)

# 输出结果为： [('sophia', 14), ('jim', 16), ('kate', 20), ('lily', 80)]





