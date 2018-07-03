
#贪婪与非贪婪
#python默认是贪婪模式
# {3,6}?,加上一个？变成非贪婪模式

import re

s = 'python10&C#\rjava C++___ \n php \t98=()~`'

r = re.findall('[a-z]{3,6}',s)  #贪婪模式
print(r)

r1 = re.findall('[a-z]{3,6}?',s)  #非贪婪模式.有什么意义呢？
r2 = re.findall('[a-z]{3}',s)
print(r1)
print(r2)   