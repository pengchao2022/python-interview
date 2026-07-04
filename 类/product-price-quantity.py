# 题目要求：编写一个 Python 程序，创建一个 Product 类，
# 包含三个实例属性：name（名称）、price（价格）和 quantity（数量）。
# 添加一个 total_value() 方法，
# 通过价格乘以数量来计算并返回库存总价值。

class Product:

    # 构造函数 初始化方法
    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity



    # 方法一 total_value
    def total_value(self):

        return self.price * self.quantity
    
# 创建对象实例
p1 = Product('Orange', 5.58, 304)

# 调用方法
print(f"{p1.name} 总价值为: {p1.total_value()}")

        