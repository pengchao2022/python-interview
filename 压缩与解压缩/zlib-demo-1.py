# 编写一个程序，对字符串 "hello world!hello world!hello world!hello world!" 进行压缩，然后再解压缩还原。


import zlib

original_string = "hello world!hello world!hello world!hello world!"

print(f"原始字符串为: {original_string}")

print(f"原始字符串的长度为: {len(original_string)}")


# 压缩字符串 将字符串 转换为 字节码
compressed = zlib.compress(original_string.encode())

print(f"压缩后的字节码为: {compressed}")

print(f"压缩后的字节码长度为: {len(compressed)}")


# 解压缩
decompressed = zlib.decompress(compressed).decode()

print(f"解压后的字符串为: {decompressed}")

print(f"解压后的字符串长度为: {len(decompressed)}")


# 判断解压前后是否一致

print(f"判断是否一致: {original_string == decompressed}")


