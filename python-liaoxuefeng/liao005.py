
#高阶函数-map/reduce
#python内建了map()、reduce()函数

#1.map()函数接收两个参数：一个是函数，一个是iterable对象。map将传入的函数
#依次作用于序列的每个元素，并将结果作为新的iterator对象返回。

def f(x):
    return x*x
L = [1,2,3,4,5,6,7,8,9,10]
r = map(f,L)
print(list(r))

r2 = map(str,L)
print(list(r2))

#2.reduce()函数。
#reduce()函数接收两个参数：一个是函数，一个是iterable对象。这个函数作用于
#这个序列上，这个函数每次必须接收两个参数，reduce把结果继续和序列的下一个元素
#做累计计算。
#reduce(f,[X1,X2,X3,X4]) = f(f(f(x1,x2),x3),x4)

#把序列[1,3,5,7,9]变换成整数：13579：
from functools import reduce
def fn(x,y):
    return 10*x + y
r3 = reduce(fn,[1,3,5,7,9])
print(r3)
