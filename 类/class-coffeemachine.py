# 题目要求：编写一个 Python 程序，\
# 创建一个 CoffeeMachine 类，
# 用于追踪三种资源：水（water）、咖啡（coffee）和牛奶（milk）
# （单位：毫升/克）。添加一个 make_latte() 方法，
# 检查是否有足够的资源来制作拿铁——如果有，扣除对应用量并打印成功信息；如果不够，打印资源不足的提示。

class CoffeeMachine:

    def __init__(self, water, coffee, milk):

        self.water = water
        self.milk = milk
        self.coffee = coffee


    # 创建方法
    # 制作拿铁
    def make_latte(self):

        # 定义 需要的资源
        need_water = 100
        need_coffee = 50
        need_milk = 150


        # 检查传入的资源是否满足制作拿铁的资源需求
        if self.water < need_water:
            print(f"水不足！ 需要: {need_water}ml, 但是当前只有: {self.water}ml")
            return       # 如果水不足，终止程序，不在向下执行
        
        
        if self.coffee < need_coffee:
            print(f"咖啡不足！ 需要: {need_coffee}g, 但是当前只有: {self.coffee}g")
            return
        

        if self.milk < need_milk:
            print(f"牛奶不足! 需要: {need_milk}ml, 但是当前只有: {self.milk}ml")
            return
        

        # 当上述条件都满足时 执行制作咖啡操作
        print("拿铁制作成功！")

        # 制作后扣除需要的资源，返回剩余的资源
        self.water -= need_water
        self.coffee -= need_coffee
        self.milk -= need_milk

        print(f"剩余资源详情: 水 {self.water}ml 咖啡 {self.coffee}g 牛奶 {self.milk}ml")


# 创建对象实例
machine = CoffeeMachine(500, 500, 500)

# 调用方法
machine.make_latte()


        