# 定义一个类
class Calculator():


    # 构造函数，初始化方法
    def __init__(self, brand):
        self.brand = brand
        self.result = 0    # 不要声明 result ,因为这是一个固定的默认初始值


    # 方法一 加
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    # 方法二 减
    def substract(self, a, b):
        self.result = a - b
        return self.result
    
    # 方法三 乘
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    

    # 方法四 除
    def divide(self, a, b):
        # 判断除数不能为 0
        if b == 0:
            return "error: divided number can not be zero"
        else:
            self.result = a / b
            return self.result
        

    # 显示结果
    def show_result(self):
        print(f"{self.brand} calculator result is : {self.result}")


# 创建对象
calc = Calculator('cisco')

print(calc.add(99, 1))
print(calc.substract(200, 100))
print(calc.divide(100, 0))
print(calc.divide(200, 4))
print(calc.multiply(40, 30))
calc.show_result()


