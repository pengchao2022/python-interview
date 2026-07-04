# 编写一个 Python 程序，
# 创建一个 Vehicle 父类，
# 包含 name 和 max_speed 
# 属性以及一个 display() 方法。
# 然后创建一个 Bus 子类，
# 它继承 Vehicle 的所有内容但不添加任何新内容，
# 并确认 Bus 的实例可以访问父类的方法。

class Vehicle:

    def __init__(self, name, max_speed):

        self.name = name
        self.max_speed = max_speed


    # 创建display() 方法
    def display(self):

        print(f"车辆名称: {self.name} 车辆最大速度: {self.max_speed}")


# 创建子类 bus
class Bus(Vehicle):

    pass # 什么都不增加


# 创建子类对象
bus1 = Bus('BMW', 250)

# 调用方法
bus1.display()


        