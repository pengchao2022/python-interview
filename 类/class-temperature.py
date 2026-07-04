# 题目要求：编写一个 Python 程序，创建一个 Temperature 类，
# 用来存储摄氏温度。
# 添加两个方法：to_fahrenheit() 
# 将温度转换为华氏度（°F）并返回，to_kelvin() 
# 将温度转换为开尔文（K）并返回。

class Temperature:

    def __init__(self, celsius):

        self.celsius = celsius   # celsius 是摄氏度


    # 摄氏温度 转换为 华氏温度 
    def to_fahrenheit(self):

        return self.celsius * 9 / 5 + 32
    

    # 摄氏温度 转换为 开尔文温度
    def to_kelvin(self):

        return self.celsius + 273.15
    
# 创建实例 对象
t = Temperature(38.5)

# 调用方法
th = t.to_fahrenheit()

tk = t.to_kelvin()

# 打印出温度
print(f"当前温度{t.celsius:.2f} 转换为华氏温度为: {th:.2f}")

print(f"当前温度{t.celsius:.2f} 转换为开尔文温度为: {tk:.2f}")


        
