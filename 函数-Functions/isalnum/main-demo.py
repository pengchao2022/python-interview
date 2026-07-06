
# isalnum() 字符串方法 检查字符串是否只包含字母(a-z, A-Z)和数字(0-9)

# "abc"    ← 纯字母
# "123"    ← 纯数字
# "abc123" ← 字母+数字混合


print("Helloworld".isalnum())

print("Helloworld2026".isalnum())

print("2026".isalnum())


print("Helloworld 2026".isalnum()) # False 不能含有空格

print("Hellowrld,2026".isalnum()) # False 不能含有标点符号

print("Helloworld@2026".isalnum()) # False 不能含有特殊符号

