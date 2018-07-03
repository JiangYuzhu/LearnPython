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
def func():   
    print('hello')
    time.sleep(1)
    print('Python')

func()

##AOP编程思想