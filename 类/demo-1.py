# define a class and input output changed

class InputOutString(object):
    
    # 构造函数 初始化方法 这个是必须的
    def __init__(self):
        self.s = ""

    # 方法1
    def getString(self):
        self.s = input("Please type an English string here: ")


    # 方法2 
    def printString(self):
        print(f"Your changed string is: {self.s.upper()}")


# 创建对象并调用对象的方法    
strObj = InputOutString()
strObj.getString()
strObj.printString()

