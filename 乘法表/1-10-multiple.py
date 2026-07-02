# 打印 1 到 10 的乘法表

for i in range(1, 11):

    for j in range(1, i + 1):

        print(f"{j} x {i} = {i * j}", end="\t")


    # 换行
    print()

    