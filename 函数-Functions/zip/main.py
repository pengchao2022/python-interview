# 将多个可迭代对象打包成一个元组列表

names =['maxwell', 'allen', 'pengchao']

ages = [25, 36, 38]

genders = ['female', 'male', 'male']


# 打包强制转换为列表 

employee_info = list(zip(names, ages, genders))

print(employee_info)

