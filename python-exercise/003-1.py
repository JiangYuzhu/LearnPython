
#一个整数加上100和加上268都是一个完全平方数。该整数是多少？

#思路：

import math

for i in range(10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if x * x == i + 100 and y * y == i+268:
        print(i,x,y)

#python内置函数range()返回的结果是一个整数序列的对象，常用于for循环。
print(type(range(10)))  #class 'range',不是列表。
#help(range)
#可以用list函数返回列表：
print(list(range(10)))
#range(10)等于：range(0,10,1),转换后的列表为：[0,1,2,3,4,5,6,7,8,9]
#语法：range(start,stop [,step]),star默认为0，step默认为1，stop不包含在内

