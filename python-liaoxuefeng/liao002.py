
#列表生成式

# 1. 生成自然数2次幂序列,使用for循环：
L = []
for x in range(1,11):
    L.append(x*x)
print(L)

#2.使用列表生成式(list exprehensions)
L = [x*x for x in range(1,11)]
print(L)

#3.列表生成式可以在for后面加if判断，比如生成仅偶数、奇数的序列
L1 = [x*x for x in range(1,11) if x % 2 == 0]
L2 = [x*x for x in range(1,11) if x % 2 == 1]
print(L1)
print(L2)

#4.for循环可以嵌套
L = [m+n for m in 'ABC' for n in 'XYZ']
print(L)

#5.列出当前目录下的所有文件(包含目录)名。
import os
L = [d for d in os.listdir('c:\\python-Files')]
print(L)
print(os.listdir('c:\\python-files'))

#6.for循环可以使用多个变量，比如dict的items()可以同时迭代key和value：
D = {'X':'A','Y':'B','Z':'C'}
for k,v in D.items():
    print(k,'=',v)

print([k + '=' + v for k,v in D.items()])
