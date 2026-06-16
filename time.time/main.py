# time.time() 返回当前时间的时间戳

import time

current_time = time.time()    # 返回的是时间戳 timestamp 是一个 浮点数 

transfered_time = time.ctime(current_time) # time.ctime 返回人类可读的时间


print(current_time)
print(transfered_time)

print("the app is starting in progress")

time.sleep(4) # 延迟 4 秒

print(" the app finished starting")



