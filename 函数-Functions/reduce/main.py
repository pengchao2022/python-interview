# 进行 累积 计算

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

my_number = (reduce(multiply, numbers))

print(my_number)



