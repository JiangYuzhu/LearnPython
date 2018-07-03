##多个装饰器

def deco_1(f):
    print('Enter into deco_1')
    def wrapper1(*args,**kwargs):
        print('Enter into wrapper1')
        f(*args,**kwargs)
    return wrapper1
def deco_2(f):
    print('Enter into deco_2')
    def wrapper2(*args,**kwargs):
        print('Enter into wrapper2')
        f(*args,**kwargs)
    return wrapper2
@deco_1
@deco_2
def f(a,b):
    print('Result is： %d'%(a+b))
f(3,8)
#f(a,b)=deco_1(deco_2(f(a,b)))
