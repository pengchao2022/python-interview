# 练习题目：创建一个 Car 类，包含品牌（brand）、型号（model）和年份（year）属性。定义一个 start_engine() 方法，用于打印一条描述汽车启动的格式化信息。

class Car(object):

    # 构造函数 初始化方法
    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year


    # 定义 start_engine() 方法
    def start_engine(self):

        print(f"{self.year} 款式 {self.brand} {self.model} 开始启动了...")


# 创建对象实例
my_car = Car('BMW', '425i', '2026')

# 调用方法
my_car.start_engine()


        