
#group分组

import re

s ='life is short,i use python'
r = re.search('life.*python',s)  #分组，等同于（life.*python）
print(r.group()) #group可包含参数，0为默认值，记录的是正则表达式完整的字符串
r = re.search('life(.*)python',s)
print(r.group(0))
print(r.group(1))

r = re.findall('life(.*)python',s)
print(r)

s = 'life is short,i use python,i love python'
r = re.search('life(.*)python(.*)python',s)
print(r.group(0))
print(r.group(1))
print(r.group(2))

print(r.group(0,1,2))

print(r.groups())
