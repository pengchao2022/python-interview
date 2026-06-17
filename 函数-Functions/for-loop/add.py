# 写一个函数通用型计算1-100 的和

def add_num(start_num, end_num):
    total = 0
    for i in range(start_num, end_num+1):
        total += i

    return total


# 定义一个运行函数
def run_app():
    start_num = int(input("Please enter your start nnumber here: "))
    end_num = int(input("Please enter your end number here: "))
    result = add_num(start_num, end_num) # 将接收到的参数传递给主程序
    if result: # 如果result 不是 None， 或者不是 空字符串 就会执行打印
        print(f"from {start_num} add to {end_num} result is: {result}")


# 运行程序  
run_app()


