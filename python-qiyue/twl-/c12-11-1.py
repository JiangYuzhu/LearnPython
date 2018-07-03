#装饰器（五）：被装饰函数有关键字参数
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
def f3(arg1,arg2,**arg3): #未加装饰器的一个带有关键字参数的函数
    print(arg1,arg2)
    print(arg3)
f1('Python')
f2('Hello','Python')
f3('x','y',a=1,b=2,c='abc')