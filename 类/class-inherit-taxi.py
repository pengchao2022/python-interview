# 题目要求：编写一个 Python 程序，创建一个 Vehicle（交通工具）父类，
# 里面有一个基础费用（base fare）。
# 然后创建一个 Taxi（出租车）子类，
# 在父类的基础费用上，用 super() 加上 10% 的维护费。

class Vehicle:

    # 构造对象 初始化方法
    def __init__(self, base_fare):

        self.base_fare = base_fare


    
    # 基础费用
    def calculate_fare(self):

        return self.base_fare
    

# 创建子类
class Taxi(Vehicle):

    def __init__(self, base_fare):
        super().__init__(base_fare)


    # 子类的费用计算方法 重写 父类 方法 
    def calculate_fare(self):
        maintenance_fee = self.base_fare * 0.10
        return self.base_fare + maintenance_fee
    

# 创建子类对象
taxi = Taxi(100)

# 调用方法
print(f"基础费用: {taxi.base_fare}")

print(f"总费用: {taxi.calculate_fare():.2f}")




        
        