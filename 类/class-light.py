# 题目要求：编写一个 Python 程序，
# 创建一个 Light 类，
# 包含三个方法：turn_on() 开灯，turn_off() 关灯，status() 
# 返回灯的当前状态（开或关）。

class Light:

    def __init__(self):
        self.is_on = False # 默认灯是关闭的 全局变量


    # 方法一 turn_on()
    def turn_on(self):

        self.is_on = True
        print("灯已经开启了")


    # 方法二 turn_off()
    def turn_off(self):

        self.is_on = False
        print("灯已经关闭了")


    # 方法三 status()
    def status(self):

        if self.is_on:
            return "灯是开着的"
        
        else:
            return "灯是关闭的"
        

# 创建对象实例

light = Light()

# 调用方法
light.turn_on()
print(light.status())

light.turn_off()
print(light.status())

