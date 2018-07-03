
#装饰器（四）：被装饰函数的形参个数不同;（可变参数）
#装饰器可以装饰多个函数才有意义。
import time
def decorator(f):
    def wrapper(*args):
        print(time.time())
        f(*args)
    return wrapper
@decorator
def f1(arg1):
    print("The argument is "+ arg1)
@decorator
def f2(arg1,arg2):
    print('The argument are '+arg1 +' and '+arg2)
f1('Python')
f2('Hello','Python')