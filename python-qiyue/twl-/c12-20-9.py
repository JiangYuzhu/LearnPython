#使用@语法糖？
#被装饰函数的调用方式不变！

import time

def decorator(f): 
    def wrapper():
        startTime = time.time()
        f()
        endTime = time.time()
        usecs = (endTime - startTime)*1000000
        print('Time is %d us'%usecs)
    return wrapper
@decorator
def f1():   
    print('hello')
    time.sleep(1)
    print('Python')
@decorator
def f2():
    print('Hello')
    time.sleep(1)
    print('World')
f1()
f2()