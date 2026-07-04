# 编写一个 Python 程序，创建一个 Student 类，
# 存储学生的姓名和分数列表。
# 添加一个 average() 方法，计算并返回所有分数的平均值

class Student:

    # 初始化方法 构造函数
    def __init__(self, name, marks):

        self.name = name
        self.marks = marks


    # 方法一 定义 average()

    def average(self):

        return sum(self.marks) / len(self.marks)
    

# 创建实例对象
stu1 = Student('Kate', [98, 89, 103, 100, 88])


# 调用方法
print(f"{stu1.name} 平均分数为: {stu1.average()}")


        