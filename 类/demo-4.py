# 定义一个名为 Rectangle 的类，该类可以通过长度和宽度进行构造。Rectangle 类有一个可以计算面积的方法。

class Rectangle(object):

    # 构造函数 初始化方法 传入长 宽
    def __init__(self, length, width):
        self.length = length
        self.width = width


    # 方法一 计算面积   
    def area(self):
        return self.length * self.width
    

    # 方法二 计算周长
    def perimeter(self):
        return 2 * (self.length + self.width)
    

# 创建对象 实例
rect = Rectangle(18, 10)

# 调用方法
chang = rect.length

kuan = rect.width

mianji = rect.area()

zhouchang = rect.perimeter()


# 打印出来
print(f"长为: {chang}")

print(f"宽为: {kuan}")

print(f"面积为: {mianji}")

print(f"周长为: {zhouchang}")


        