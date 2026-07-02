

# 斐波那契列表是 前两个数字的和 等于 紧挨着 后面的那个数字

# 打印指定当前项的斐波那契额列表

def get_fibonacci(n):

    a = 0 # a 为当前项
    b = 1

    fibo_list = []

    for _ in range(n):

        fibo_list.append(a)

        a, b = b, a + b # 更新 当前项 a 的值， 后面的一项 始终是前两项的和 a + b


    return fibo_list


def run_app():

    n = int(input("请在此输入您要打印的项: \n"))

    fibo_list = get_fibonacci(n)

    print(fibo_list)



if __name__ == "__main__":  # 只有直接运行这个文件时 才运行 run_app 函数

    run_app()