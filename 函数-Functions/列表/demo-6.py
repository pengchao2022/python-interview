# 找出 1000 到 3000 之间的每一位都能被2 整数的所有数字，注意，是个十百千都能被2 整除
# 并以逗号分隔输出为一行

def check_every_bit_even_num(start_num, end_num):

    # 定义一个列表接收符合条件的数字
    result = []

    for i in range(int(start_num), int(end_num) + 1):
        if all(int(d) % 2 == 0 for d in str(i)):
            result.append(str(i))


    return ','.join(result)

def run_app():
    user_input = input("请在此输入起始和结束数字并以空格分隔: ")

    # 去掉输入字符串前后的空格
    clean_str = user_input.strip()

    # 将字符串转换为列表并以空格分割
    list_str = clean_str.split()

    start_num = list_str[0]
    end_num = list_str[1]

    expect_number_string = check_every_bit_even_num(start_num, end_num)

    print(expect_number_string)


run_app()

