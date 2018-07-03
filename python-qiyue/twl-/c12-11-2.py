#装饰器（五）：被装饰函数有关键字参数.
#装饰器可以装饰多个函数才有意义。
#这里是比较完整的装饰器形态！
import time
def decorator(f):
    def wrapper(*args,**kwargs):
        print(time.time())
        f(*args,**kwargs) 
        ##调用方式。无论函数定义的参数是什么样的，都可以使用可变参数加上关键字参数来调用。##
    return wrapper
@decorator
def f1(arg1):
    print("The argument is "+ arg1)
@decorator
def f2(arg1,arg2):
    print('The argument are '+arg1 +' and '+arg2)
@decorator
def f3(arg1,arg2,**arg3):
    print(arg1,arg2)
    print(arg3)
f1('Python')
f2('Hello','Python')
f3('x','y',a=1,b=2,c='abc')