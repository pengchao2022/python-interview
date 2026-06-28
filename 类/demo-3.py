# 定义一个名为 Circle 的类，该类可以通过半径进行构造。Circle 类有一个可以计算面积和周长的方法。

import math

class Circle(object):


    # 构造函数 初始化方法，并传入 半径
    def __init__(self, radius):

        self.radius = radius


    # 方法一 计算面积
    def area(self):

        return math.pi * self.radius ** 2
    

    # 方法二 计算周长
    def perimeter(self):

        return 2 * math.pi * self.radius
    


# 创建对象 实例
circle = Circle(4)

# 调用方法
banjing = circle.radius

mianji = circle.area()

zhouchang = circle.perimeter()


# 打印出来  

print(f"半径是: {banjing}")

print(f"面积是: {mianji:.2f}")

print(f"周长是: {zhouchang:.2f}")


