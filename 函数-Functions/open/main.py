# open() 打开文件

file_path = "/Users/allen/devops/python-interview/for_test.txt"

with open(file_path, "r") as file:
    content = file.read()
    print("文件内容:\n", content)


# 输出内容
# 文件内容:
#  I'm unable to take or view screenshots, 
# as I'm a text-only AI and don't have access to your device or screen. However, 
# I can help guide you on how to take a screenshot on your specific device (Windows, Mac, Android, iOS, etc.) 
# or assist with describing what you'd like to capture. Could you share more about what you need?   


# 写如文件内容

with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Maxwell')

    