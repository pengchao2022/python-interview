# 输入
# Tom,19,80
# John,20,90
# Jonny,17,91
# json,21,85

# 输出
# [('John', '20', '90'), ('Jonny', '17', '91'), ('Tom', '19', '80'), ('json', '21', '85')]
# 多级排序练习


def main():

    print("请在此输入元组，每行一个，输入空行结束")
    
    data = []
    while True:
        line = input().strip()
        if not line: #空行结束
            break
        data.append(line)

    # 处理数据
    tuples_list = []
    for line in data:
        name, age, height = line.split(',')
        tuples_list.append((name, int(age), int(height)))

    sorted_list = sorted(tuples_list, key=lambda x: (x[0], x[1], x[2]))

    result = [(name, str(age), str(height)) for name, age, height in sorted_list]

    print(result)


main()
