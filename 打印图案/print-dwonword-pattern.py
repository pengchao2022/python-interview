# 输入一个数字 打印出 递减的 图案

# 如下所示：

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 

def print_downwords_pattern(number):

    for i in range(number, 0, -1): # 注意田间了步长 递减 

        for j in range(i, 0, -1): # 依然是递减

            print(j, end=" ")

        print() # 换行


def run_app():

    number = int(input("请在此输入一个数字:\n"))

    print_downwords_pattern(number)


if __name__ == "__main__":

    run_app()

    