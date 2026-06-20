# re.findall() 在字符串中查找符合正则表达式的所有

import re

my_str = "France has previously intercepted several vessels linked to Russia’s shadow fleet, which carries Russian oil in defiance of international sanctions."

new_str = re.findall('r', my_str)

print(new_str)

new_str1 = re.findall('r.', my_str)

print(new_str1)


