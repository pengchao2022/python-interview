# 题目要求：编写一个 Python 程序，
# Vehicle 父类中有一个 seating_capacity() 方法，
# 接受一个 capacity 参数。
# 创建一个 Bus 子类，重写这个方法，
# 给它一个默认的载客量 50，
# 并在内部使用 super() 调用父类的版本。

class Vehicle:

    def __init__(self, name, max_speed):

        self.name = name
        self.max_speed = max_speed



    def seating_capacity(self, capacity):

        return f"{self.name} has seats {capacity}"
    

# 创建子类
class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)
    

# 创建子类对象
bus = Bus('BMW', 250)

# 调用方法
print(bus.seating_capacity())


        