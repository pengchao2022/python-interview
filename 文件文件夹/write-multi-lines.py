# 多行文件的写入 与 读取

lines = [

"Hello, this is maxwell from the python developer's team,\n"
"I like python programming very much,\n"
"Today is the year of 2026,\n"
"THis is just a test.\n"
]
# 写入多行
with open('maxwell-10.txt', 'a') as file:

    file.writelines(lines)

# 读取全部
with open('maxwell-10.txt', 'r') as file:

    content = file.read() # 读取全部

# 打印出来验证
print(content)

