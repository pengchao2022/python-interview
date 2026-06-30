# 定义一个名为 Shape 的类及其子类 Square。Square 类有一个初始化函数，它接受一个长度作为参数。两个类都有一个 area 函数，可以打印形状的面积，
# 其中 Shape 的面积默认是 0。

class Shape(object):

    # 构造方法 函数初始化
    def __init__(self):
        self.area_value = 0


    # 方法一 计算面积
    def area(self):
        print(self.area_value)


# 定义子类
class Square(Shape):

    def __init__(self, length):    # 调用父类的构造方法
        super().__init__()
        self.length = length
        self.area_value = length ** 2


    def area(self):
        return super().area()      # 调用父类的 area 方法
    


# 创建对象 实例
shape = Shape()

square = Square(30) # 子类要求传递一个 length 参数 

# 调用方法
shape.area()

square.area()