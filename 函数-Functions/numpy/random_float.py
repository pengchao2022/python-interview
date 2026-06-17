import numpy as np

num1 = np.random.rand(5) # 生成 5 个0-1 之间的小数

expect_num = np.round(num1, 2)

print(f"original 5 little numbers are: {num1}")

print(f"expected 5 little numbers are: {expect_num}")


