
#匹配模式参数
#re.I,re.S

import re

language = 'PythonC#\njavaPHP'

r = re.findall('c#',language)
print(r)
r = re.findall('c#',language,re.I) #第三个参数：匹配模式参数；re.I表示忽略大小写
print(r)

#多个匹配模式参数之间通过 | 连接
r = re.findall('c#.{1}',language) # . 是除了换行符\n之外的所有字符
print(r)
r = re.findall('c#.{1}',language,re.I|re.S) #re.S改变了.的行为，使其也包含了\n
print(r)
