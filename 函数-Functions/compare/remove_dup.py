# 定义一个函数，用来移除重复元素

def remove_duplicated(lst): # 传一个列表

    result = []    # 去除重复元素的新列表

    for item in lst:
        if item not in result:
            result.append(item)

    return result



# 定义一个运行函数，输入一连串的数字
def app_run():
    input_str = input("请在此输入一连串的数字并以空格进行分隔: ")
    # 将字符串转换为字符列表   
    list_str = input_str.split() # 以空格分隔
    # 将字符列表转换为整数列表
    list_int = [int(x) for x in list_str]
    # 将整数列表作为参数传入函数
    result = remove_duplicated(list_int)

    if result:
        print(result)


# 运行输入
app_run()




