# 定义一个名为 American 的类，并创建它的子类 NewYorker。

class American(object):

    pass


class NewYorker(American):

    pass


# 创建类的实例（对象）
anAmerican = American()

aNewYorker = NewYorker()

print(anAmerican)

print(aNewYorker)

# 验证是否是子类
print(issubclass(NewYorker, American))

print(issubclass(American, NewYorker))

