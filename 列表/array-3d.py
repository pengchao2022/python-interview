# 请使用列表推导式，编写一个程序生成一个 3×5×8 的三维数组（即 3 层，每层 5 行，每行 8 列），所有元素都初始化为 0。


array = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]


print(array)

