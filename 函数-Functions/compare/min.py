# 定义一个比较函数，返回最小值

def find_min(lst):    # 传一个列表
    min_num = lst[0]
    for _, num in enumerate(lst):
        if num < min_num:
            min_num = num

    return min_num



# 定义主函数运行函数
def app_run():
    input_str = input("请输入一连串的数字 中间以空格隔开: ")
    # 将字符串 转换为字符列表 
    list_str = input_str.split() # 以空格分隔
    # 将字符列表转换为整型列表 整型才能比较大小
    list_int = [int(x) for x in list_str]
    # 将得到的整形列表作为参数传递给比较函数
    result = find_min(list_int)
    if result:
        print(f"最小值为: {result}")

    return 0

# 运行程序
app_run()


