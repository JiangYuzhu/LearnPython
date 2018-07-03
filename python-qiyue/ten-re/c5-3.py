
# 匹配0次、1次或无限多次
# * 匹配0次或无限多次；匹配前面的子表达式任意次，示例中等价于n{0,}
# + 匹配1次或无限多次；匹配前面的子表达式1次或多次，示例中等价于n{1,}
# ？匹配0次或1次;匹配前面的子表达式0次或1次，示例中等价于n{0,1}

import re

a = 'pytho0python1pythonn2'

r = re.findall('python*',a)
print(r)
r = re.findall('python{0,}',a)
print(r)

r = re.findall('python+',a)
print(r)
r = re.findall('python{1,}',a)
print(r)

r1 = re.findall('python?',a)
print(r1)
r1 = re.findall('python{0,1}',a)
print(r1)
r2 = re.findall('python{1,2}',a)
print(r2)
r3 = re.findall('python{1,2}?',a)
print(r3)
