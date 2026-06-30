# 二分查找举例

def bin_search(li, element): # li 是列表， element 是元素

    bottom = 0
    top = len(li) - 1

    # 只要范围有效就继续查找
    while top >= bottom:
        mid = (top + bottom) // 2 # 使用整除符号 //

        if li[mid] == element:
            return mid # 找到后直接返回索引
        
        elif li[mid] > element:
            top = mid -1

        else:
            bottom = mid + 1


    return -1 # 循环仍然未找到 返回 -1

def run_app():
    li = [2, 5, 7, 9, 11, 17, 222]

    print("列表:", li)

    test_element = [11, 12]

    for element in test_element:
        
        result = bin_search(li, element)

        if result != -1:

            print(f"元素{element} 在索引 {result} 处")

        else:

            print(f"元素{element} 不在列表中")


run_app()


