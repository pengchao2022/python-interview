# 合并两个字典
# 使用 dict.update 方法

dict1 = {"name": "maxwell", "age": 38, "city": "shanghai"}

dict2 = {"hobby": "basketball", "height": 180, "weight": 150}

# 合并两个字典

dict1.update(dict2)

print(dict1)

"""
注意： dict.update() 方法没有返回值 

所以 你不能使用 result = dict1.update(dict2)

因为没有返回值，所以 result = None


"""

