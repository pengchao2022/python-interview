# 文件的基本操作 

# 创建文件 并在文件里写入几句话



# 创建文件
file = open('maxwell-1.txt', 'w')

# 在文件里写入内容
file.write("Hello, this is Maxwell, I am a python developer\n")

file.write("Today is year 2026\n")

# 关闭文件
file.close() # 不关闭可能导致 数据丢失



