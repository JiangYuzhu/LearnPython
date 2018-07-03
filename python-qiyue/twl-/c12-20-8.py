
#使用@语法糖？
#被装饰函数的调用方式不变！
#正确
import time
def decorator(f): 
    def wrapper(x):
        startTime = time.time()
        f(x)
        endTime = time.time()
        usecs = (endTime - startTime)*1000000
        print('Time is %d us'%usecs)
    return wrapper
@decorator
def func(a):   #被装饰函数带有参数
    print('hello')
    time.sleep(1)
    print(a)
func('Python')
func('World')