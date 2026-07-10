# pop() 函数 

# 列表的 pop()用于移除指定索引位置的元素

# 语法 list.pop(index)

# 返回值： 被移除元素本身

numbers = [1, 2, 3, 4, 5]

num1 = numbers.pop() # 不传入参数时， 返回列表最后的那个元素

print(num1)  # 5    

print(numbers)

num2 = numbers.pop(1)  # 1 是索引 index 从 0 开始

print(num2)     # 2

print(numbers)


list1 = ['a', 'b', 'c', 'd']

char1 = list1.pop()  # 返回列表最后一个元素

print(char1) # d

print(list1)


char1 = list1.pop(0)

print(char1) # a

print(list1)


