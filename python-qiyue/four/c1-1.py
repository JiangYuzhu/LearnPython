##将字符串各个字符作为列表的元素
strings = 'abcd1234'
L = []
for i in strings:
    L.append(i)
print(L)

##计算X的N次幂值
import time
def power(x,n):
    s = 1
    startTime = time.time()
    while n > 0:
        n = n -1
        s = s * x
    print(s)
    endTime = time.time()
    msecs = (endTime - startTime)*1000
    print(msecs)
power(3,5000)

##计算n的阶乘：n!
#方法一：n!=n*(n-1)!,使用递归函数
def factorial(n):
    if n == 1:
        return 1
    while n > 1:
        return n*factorial(n-1)
print(factorial(998)) #我的电脑递归深度998.
#方法二：使用循环n!=1*2*3*....*n
def fact(n):
    fact = 1
    # if n == 1:
    #     return fact
    while n > 1:
        fact = n * fact
        n = n - 1
    return fact
print(fact(6))
#方法三：尾递归，函数返回时调用自身，不包含表达式。
#尾递归无论调用多少次，都只占用一个栈帧，不会导致栈溢出。
def fact2(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)
result = fact2(5)
print(result)
