# 题目要求：编写一个 Python 程序，
# 创建一个 Vehicle 类，
# 其中有一个类属性 color = "White"，
# 这个属性会被类的所有实例共享。
# 创建两个车辆对象，展示它们使用相同的默认颜色，
# 然后演示修改类属性后，所有没有单独设置颜色的实例都会跟着变化。

class Vehicel:

    color = "white" # 类属性 所有资源共享

# 创建两个实例对象
car1 = Vehicel()

car2 = Vehicel()

print(f"car1 的颜色: {car1.color}")

print(f"car2 的颜色: {car2.color}")

# 修改实例属性
Vehicel.color = "red"

print(f"car1 的颜色: {car1.color}")

print(f"car2 的颜色: {car2.color}")



