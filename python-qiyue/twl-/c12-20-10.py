#使用@语法糖.其实质是：f1 = decorator(f1)
#被装饰函数的调用方式不变！
#被装饰函数带参数
#正确！这应是最好的方式。
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
def f1(a):   
    print('hello')
    time.sleep(1)
    print(a)
@decorator
def f2(b):
    print('Hello')
    time.sleep(1)
    print(b)
f1('Python')
f2('World')