# 输入一串整数，找到最大的那个数

def find_max(lst):
    max_num = lst[0]
    for _, num in enumerate(lst):
        if num > max_num:
            max_num = num

    return max_num


# 定义主函数
def app_run():
    input_str = input("请在此输入一脸串的整数，并以空格隔开: ")
    list_str = input_str.split()
    list_int = [int(x) for x in list_str]
    # 调用比较函数
    result = find_max(list_int)
    if result:
        print(f"最大的数为: {result}")
    return None


# 运行函数
app_run()

